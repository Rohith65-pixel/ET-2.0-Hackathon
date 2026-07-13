from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

import re
import base64
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.getcwd()
PARSE_DIR = os.path.join(BASE_DIR,'parsed_files')

API_TOKEN = os.getenv("GROQ_API_KEY")

if not API_TOKEN:
    raise ValueError(
        "GROQ_API_KEY was not found in .env"
    )

print("API TOKEN key loaded successfully")

vlm = ChatGroq(
    model='qwen/qwen3.6-27b',
    # model='openai/gpt-oss-120b',
    temperature=0.0,
    api_key=API_TOKEN
)

class ImageEnricher :
    def __init__(self,filename):
        self.filename = filename
        self.file_path = os.path.join(PARSE_DIR,filename)

    def find_images(self,markdown_text):

        image_pattern = r'!\[\]\((.*?\.jpg)\)'

        images = re.findall(
            image_pattern,
            markdown_text
        )

        return images

    def analyze_image(self,image_path):

        print(f"Sending image to Grok: {os.path.basename(image_path)}")

        prompt = """
    You are analyzing a technical industrial document.

    The document may contain electrical systems,
    mechanical equipment, thermal power plant equipment,
    maintenance diagrams, engineering drawings, graphs,
    charts or technical illustrations.

    Analyze the provided image carefully.

    Extract ONLY information visible in the image.

    Focus on:

    1. Equipment names
    2. Equipment tags and identifiers
    3. Electrical components
    4. Mechanical components
    5. Connections between components
    6. Flow direction
    7. Numerical values
    8. Units
    9. Warning limits
    10. Operating limits
    11. Labels and annotations
    12. Maintenance information
    13. Operational information

    If the image is an electrical diagram:
    Explain which components are connected and how.

    If the image is a process diagram:
    Explain the direction of flow and relationships
    between equipment.

    If the image is a graph:
    Extract axis labels, trends, thresholds and
    abnormal regions.

    If the image is a technical illustration:
    Explain the visible components and their
    relationships.

    Do not invent missing information.

    Do not provide general textbook explanations.

    If a label or value is unclear, explicitly say
    that it is unclear.

    Return factual technical text suitable for
    entity and relationship extraction by a
    GraphRAG system.
    """
        with open(image_path, "rb") as f1:
            image_bytes = f1.read()

        base64_image = base64.b64encode(image_bytes).decode("utf-8")
        message = HumanMessage(
            content=[
                {
                    "type": "text", 
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        )

        response = vlm.invoke([message])
        
        print('Done')
        description = response.content


        return f"""
    ### AI Image Interpretation

    Image source: {image_path}

    {description}
    """

    def enrich_markdown(self):


        document_folder = self.file_path

        print("\nReading markdown from:")
        markdown_path = os.path.join(self.file_path,'full.md')
        with open(markdown_path,'r') as f1:
            markdown_text = f1.read()

        images = self.find_images(markdown_text)
        print("\nImages found:", len(images))

        for index, image_path in enumerate(images,1):
            if index < 36:
                continue
            print(
                f"\nProcessing image "
                f"{index}/{len(images)}"
            )


            print("Image reference:")

            print(image_path)


            full_image_path = os.path.join(document_folder,image_path)

            print("Full image path:")

            print(full_image_path)


            if not os.path.exists(full_image_path):
                print("IMAGE NOT FOUND")
                continue


            try:

                description = self.analyze_image(
                    full_image_path
                )


            except Exception as error:

                print("ERROR ANALYZING IMAGE:")

                print(error)

                continue


            image_markdown = (
                f"![]({image_path})"
            )


            enriched_content = (
                image_markdown
                + "\n\n"
                + description
            )


            markdown_text = markdown_text.replace(
                image_markdown,
                enriched_content
            )

            output_path = os.path.join(document_folder,"enriched.md")

            with open(output_path,'w') as f2 :
                f2.write(markdown_text)

        print(
            "\nEnriched markdown saved at:"
        )

        print(output_path)
    
    def start(self) :
        self.enrich_markdown()

if __name__ == '__main__' :
    ImageEnricher(os.listdir(PARSE_DIR)[0]).start()
    # print(os.getcwd())