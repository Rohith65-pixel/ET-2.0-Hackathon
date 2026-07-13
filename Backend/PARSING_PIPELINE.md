# Parsing Pipeline Documentation

## Overview

- Automates the conversion of raw documents into structured Markdown files.
- Uses the MinerU API to parse documents.
- Handles document upload, parsing, downloading, and extraction.
- Produces structured output for further processing.

---

## Purpose

- Eliminates manual document parsing.
- Automates the complete parsing workflow.
- Ensures consistent and reliable document processing.
- Prepares parsed content for downstream applications.

---

## Technologies Used

- Python 3
- MinerU REST API
- Requests
- python-dotenv
- zipfile
- pathlib

---

## Project Structure

- `datasets/` – Stores the input documents.
- `zip_files/` – Stores downloaded ZIP files.
- `parsed_files/` – Stores extracted parsing results.
- `parsing_pipeline.py` – Contains the parsing pipeline implementation.
- `.env` – Stores the MinerU API key securely.

---

## Configuration

- The MinerU API requires an authentication key.
- The API key is stored in the `.env` file.
- The key is loaded using the `python-dotenv` library during execution.

---

## MineruParser Class

- Serves as the core component of the parsing pipeline.
- Manages the complete document parsing workflow.
- Handles communication with the MinerU API.
- Coordinates uploading, downloading, and extraction processes.

---

## Constructor (`__init__()`)

- Initializes the parser with the input file path.
- Extracts the file name from the provided path.
- Creates authentication headers for API requests.
- Prepares the request payload for document parsing.

---

## `get_upload_url()`

- Sends a request to the MinerU API.
- Generates a temporary upload URL.
- Retrieves a unique batch ID.
- Stores the upload details for later use.

---

## `upload_pdf()`

- Uploads the selected document to the MinerU server.
- Uses the generated upload URL.
- Confirms successful upload before continuing.

---

## `get_zip_url()`

- Checks the parsing status periodically.
- Waits until the parsing process is completed.
- Retrieves the download URL of the parsed ZIP file.

---

## `download_zip()`

- Downloads the parsed ZIP file.
- Saves the ZIP file inside the `zip_files` directory.
- Ensures the parsed output is available locally.

---

## `extract_zip()`

- Extracts the downloaded ZIP file.
- Stores the extracted contents in the `parsed_files` directory.
- Makes the parsed Markdown file and related resources available.

---

## `start()`

- Controls the complete parsing workflow.
- Checks whether the document has already been parsed.
- Executes upload, parsing, download, and extraction sequentially.
- Prevents duplicate processing of existing documents.

---

## `check()`

- Opens the generated `full.md` file.
- Displays a portion of the parsed content.
- Helps verify successful document parsing.

---

## Input

- Accepts documents stored inside the `datasets` directory.
- Processes one document at a time.
- Supports batch processing by scanning all available files.

---

## Output

- Generates a ZIP file containing the parsed results.
- Extracts the parsed output into the `parsed_files` directory.
- Produces a `full.md` file containing the structured document content.
- Includes extracted images and tables when available.

---

## Error Handling

- Handles API request failures.
- Detects upload failures.
- Reports parsing errors.
- Handles missing ZIP files and invalid file paths.
- Displays meaningful error messages for debugging.

---

## Execution

- Recursively scans the `datasets` directory.
- Identifies all available input documents.
- Creates a `MineruParser` object for each document.
- Executes the parsing process using the `start()` method.

---

## Advantages

- Fully automates the document parsing process.
- Supports processing multiple documents.
- Prevents duplicate parsing.
- Uses secure API authentication.
- Can be integrated with AI and RAG applications.

---

## Future Enhancements

- Support parallel processing of multiple documents.
- Add retry mechanisms for failed requests.
- Implement detailed logging.
- Support additional document formats.
- Add progress tracking during parsing.

---

## Conclusion

- Provides an automated solution for document parsing using the MinerU API.
- Simplifies document processing by handling the complete parsing workflow.
- Generates structured Markdown output for downstream applications.
- Can be integrated with document analysis, RAG, and knowledge management systems.