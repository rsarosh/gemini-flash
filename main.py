import os
import sys
import PyPDF2
from google import genai
from dotenv import load_dotenv


def process_pdf(pdf_path):
    """Process a PDF file and extract its text content."""
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        print(f"Error: PDF file '{pdf_path}' not found")
        return None
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None


def main():
    # Default information to the LLM
    text = " I have 2 dogs in the hosue"
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_pdf> \n\n No pdf given using default information")
    else:
        pdf_path = sys.argv[1]
        if pdf_path is not None:
            if not pdf_path.lower().endswith(".pdf"):
                with open(pdf_path, "r") as file:
                    text = file.read()
            else:
                text = process_pdf(pdf_path)

    # Print the size of the extracted text in MB
    text_size_mb = len(text.encode("utf-8")) / 1e6
    print(f"Text size: {text_size_mb:.2f} MB")
    # Load environment variables
    load_dotenv()
    # Configure the Gemini API
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set GEMINI_API_KEY environment variable in .env file")

    client = genai.Client(api_key=api_key)

    # Initialize the model
    chat = client.chats.create(model="gemini-2.0-flash")

    if text:
        try:
            # Send the text to the chat model
            response = chat.send_message(text)
            response = chat.send_message("How many paws are there?")
            print("\nModel's response:")
            print(response.text)
            print("\n")
            while True:
                user_input = input("Enter message (q to quit): ")
                if user_input.lower() == "q":
                    break
                response = chat.send_message(user_input)
                print("\nModel's response:")
                print(response.text)
                print("\n")

        except Exception as e:
            print(f"Error communicating with Gemini: {e}")


if __name__ == "__main__":
    main()
