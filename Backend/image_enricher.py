import re
import zipfile
from pathlib import Path
import base64
import os
import mimetypes

from openai import OpenAI
from dotenv import load_dotenv


# -----------------------------------
# BASE DIRECTORY
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parent


# -----------------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------------

env_path = BASE_DIR / ".env"

load_dotenv(env_path)

api_key = os.getenv("XAI_API_KEY")

if not api_key:
    raise ValueError(
        "XAI_API_KEY was not found in Backend/.env"
    )

print("xAI API key loaded successfully")


# -----------------------------------
# XAI CLIENT
# -----------------------------------

client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)


# -----------------------------------
# FIND IMAGES INSIDE MARKDOWN
# -----------------------------------

def find_images(markdown_text):

    image_pattern = r'!\[\]\((.*?)\)'

    images = re.findall(
        image_pattern,
        markdown_text
    )

    return images


# -----------------------------------
# ANALYZE IMAGE USING GROK
# -----------------------------------

def analyze_image(image_path):

    print("Sending image to Grok:")

    print(image_path.name)


    # Read image as binary
    with open(image_path, "rb") as image_file:

        image_bytes = image_file.read()


    # Convert image to Base64
    encoded_image = base64.b64encode(
        image_bytes
    ).decode("utf-8")


    # Detect image type
    mime_type, _ = mimetypes.guess_type(
        image_path
    )


    if mime_type is None:

        mime_type = "image/jpeg"


    image_data_url = (
        f"data:{mime_type};base64,{encoded_image}"
    )


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


    response = client.responses.create(

        model="grok-4",

        input=[
            {
                "role": "user",

                "content": [
                    {
                        "type": "input_image",
                        "image_url": image_data_url
                    },

                    {
                        "type": "input_text",
                        "text": prompt
                    }
                ]
            }
        ]
    )


    description = response.output_text


    print("Image analyzed successfully")


    return f"""
### AI Image Interpretation

Image source: {image_path.name}

{description}
"""


# -----------------------------------
# ENRICH MARKDOWN
# -----------------------------------

def enrich_markdown(markdown_path):

    markdown_path = Path(markdown_path)

    document_folder = markdown_path.parent


    print("\nReading markdown from:")

    print(markdown_path)


    markdown_text = markdown_path.read_text(
        encoding="utf-8"
    )


    images = find_images(markdown_text)


    print("\nImages found:", len(images))


    for index, image_path in enumerate(
        images,
        start=1
    ):

        print(
            f"\nProcessing image "
            f"{index}/{len(images)}"
        )


        print("Image reference:")

        print(image_path)


        full_image_path = (
            document_folder
            / image_path
        )


        print("Full image path:")

        print(full_image_path)


        if not full_image_path.exists():

            print("IMAGE NOT FOUND")

            continue


        try:

            description = analyze_image(
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


    output_path = (
        document_folder
        / "enriched.md"
    )


    output_path.write_text(
        markdown_text,
        encoding="utf-8"
    )


    print(
        "\nEnriched markdown saved at:"
    )


    print(output_path)


# -----------------------------------
# EXTRACT ZIP
# -----------------------------------

def extract_zip(zip_path):

    zip_path = Path(zip_path)


    print("\nZIP file:")

    print(zip_path)


    if not zip_path.exists():

        print("\nZIP FILE NOT FOUND")

        return None


    extract_folder = (
        zip_path.parent
        / zip_path.stem
    )


    print("\nExtracting ZIP to:")

    print(extract_folder)


    with zipfile.ZipFile(
        zip_path,
        "r"
    ) as zip_file:

        zip_file.extractall(
            extract_folder
        )


    print(
        "\nZIP extracted successfully"
    )


    return extract_folder


# -----------------------------------
# MAIN
# -----------------------------------

zip_path = (
    BASE_DIR
    / "zip_files"
    / "Current_transformer_gb.zip"
)


extracted_folder = extract_zip(
    zip_path
)


if extracted_folder is not None:

    markdown_files = list(
        extracted_folder.rglob(
            "full.md"
        )
    )


    if len(markdown_files) == 0:

        print(
            "\nfull.md NOT FOUND"
        )


    else:

        markdown_path = (
            markdown_files[0]
        )


        print(
            "\nFound full.md:"
        )


        print(markdown_path)


        enrich_markdown(
            markdown_path
        )