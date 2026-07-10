import os
import requests
import time
import zipfile
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class MineruParser :
    API_TOKEN = os.getenv('MINERU_API')

    def __init__(self,file_path) :
        self.file_path = file_path
        self.filename = os.path.basename(file_path)
        self.batch_id = None
        self.upload_url = None
        self.zip_url = None
        
        self.headers = {"Authorization": f"Bearer {self.API_TOKEN}"}
        self.payload =  {
                                "enable_formula": True,
                                "language": "en",
                                "enable_table": True,
                                "files": [
                                    {
                                        "name": self.filename,
                                        "data_id": self.filename
                                    }
                                ]
                        }
    
    def get_upload_url(self) :
        try :
            response =  requests.post(url="https://mineru.net/api/v4/file-urls/batch",headers=self.headers,json=self.payload)

            response.raise_for_status()

            result = response.json()

            self.batch_id = result["data"]["batch_id"]
            self.upload_url = result["data"]["file_urls"][0]

            print("batch ID: " + self.batch_id)
            print("Upload URL: " + self.upload_url)

        except Exception as e :
            print("get_upload_url Error: " + str(e))
            raise
    
    def upload_pdf(self) :
        if self.batch_id is None or self.upload_url is None:
            raise RuntimeError("Error: Couldnt get batch-id and upload-URL")
        
        try :
            with open(self.file_path,'rb') as f:
                print("Starting upload")

                upload_response = requests.put(self.upload_url, data=f)
                upload_response.raise_for_status()

                print("Upload PDF Status:" + str(upload_response.status_code))

        except Exception as e:
            print("upload_pdf Error: " + str(e))
            raise
    
    def get_zip_url(self) :
        try :
            while True :
                response = requests.get(url=f"https://mineru.net/api/v4/extract-results/batch/{self.batch_id}",headers=self.headers)
                response.raise_for_status()

                data = response.json()
                extract_result = data["data"]["extract_result"][0]

                if extract_result["state"] == "done":
                    self.zip_url = extract_result["full_zip_url"]
                    print("ZIP URL: " + self.zip_url)
                    break
                elif extract_result["state"] == "failed":
                    print("Failure details:", extract_result)
                    raise Exception(extract_result.get("err_msg", "Unknown parsing error"))
                else :
                    print(f"Current state: {extract_result['state']}")

                time.sleep(5)

        except Exception as e:
            print("get_zip_url Error: " + str(e))
            raise
    
    def download_zip(self) :
        if self.zip_url is None:
                raise RuntimeError("ZIP URL not available")
        
        try :
            response = requests.get(self.zip_url)
            response.raise_for_status()
            name = self.filename.rsplit('.',1)[0] + '.zip'
            
            os.makedirs(os.path.join(os.getcwd(),'zip_files'),exist_ok=True)

            with open(os.path.join(os.getcwd(),'zip_files',name),'wb') as f:
                f.write(response.content)

            print("ZIP downloaded successfully!")
        except Exception as e :
            print("fetch_pdf_content Error: " + str(e))
            raise

    def extract_zip(self) :
        name = self.filename.rsplit('.',1)[0]
        ZIP_PATH = os.path.join(os.getcwd(),'zip_files',name + '.zip')
        
        if not os.path.exists(ZIP_PATH):
            raise FileNotFoundError("Zip file not found to extract data")

        OUTPUT_PATH = os.path.join(os.getcwd(),'parsed_files',name)

        os.makedirs(os.path.join(os.getcwd(),'parsed_files'),exist_ok=True)


        with zipfile.ZipFile(ZIP_PATH,'r') as zp:
            zp.extractall(OUTPUT_PATH)

    def start(self) :
        name = self.filename.rsplit('.',1)[0]
        OUTPUT_PATH = os.path.join(os.getcwd(),'parsed_files',name)
        ZIP_PATH = os.path.join(os.getcwd(),'zip_files',name + '.zip')
        print("Starting Parsing " + self.filename)
        try :
            if not os.path.exists(OUTPUT_PATH) :
        
                if not os.path.exists(ZIP_PATH):
                    self.get_upload_url()
                    self.upload_pdf()
                    self.get_zip_url()
                    self.download_zip()
                
                self.extract_zip()
            
            print(f"{self.filename} is Parsed Sucessfully!\n")
        except Exception as e :
            print("Error: " + str(e))
    
    def check(self) :
        name = self.filename.rsplit('.',1)[0]
        OUTPUT_PATH = os.path.join(os.getcwd(),'parsed_files',name)
        if os.path.exists(OUTPUT_PATH) :
            with open(os.path.join(OUTPUT_PATH,"full.md"), "r", encoding="utf-8") as f:
                text = f.read()
            print(text[:3000])
        else :
            print(f"{self.filename} parsed file doesnt exist to check")

if __name__ == '__main__' :
    DATA_PATH = os.path.join(os.getcwd(),'datasets')
    all_file_paths = []

    def get_paths(root) :
        for content in os.listdir(root) :
            temp = os.path.join(root,content)
            if Path.is_file(temp) :
                all_file_paths.append(temp)
            else :
                get_paths(temp)

    get_paths(DATA_PATH)

    for file_path in all_file_paths :
        MineruParser(file_path).start()

    # print(len(all_file_paths),len(os.listdir(os.path.join(os.getcwd(),'zip_files'))))

    # MineruParser(all_file_paths[0]).start()

    

