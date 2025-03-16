import os
import sys
import PyPDF2
from google import genai
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel, Part


def main():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gemini.json"
    project_id = "gemini-test-453519"  # Replace with your project ID
    location = "us-central1"  # Replace with your location
    model_name = "gemini-pro" # or "gemini-pro-vision"
    prompt = "What is NIST RMF."
    vertexai.init(project=project_id, location=location)
    model = GenerativeModel(model_name)
    responses = model.generate_content(prompt)
    print(responses.text)

if __name__ == "__main__":
    main()
