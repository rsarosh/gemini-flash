# PDF Analysis with Google Gemini

This project uses Google's Gemini AI to analyze PDF documents.

## Setup

1. Create a virtual environment and activate it:
```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Configure your API key:
   - Rename `.env.example` to `.env`
   - Add your Google API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

Run the script with a PDF file as an argument:
```powershell
python main.py path/to/your/file.pdf
```

The script will:
1. Extract text from the PDF
2. Send the text to Gemini AI
3. Display Gemini's response



# to run the code

python main.py openintro-statistics.pdf


# calling the agent from the code
https://gemini.google.com/app/b397f0dba3753591?_gl=1*v3rfs2*_ga*MTg0NDU4NzY0LjE3MTgxMzE2NDk.*_ga_WC57KJ50ZZ*MTcxODgyMjYxNC4yLjEuMTcxODgyMjgzMy4wLjAuMA..

# Agent builder
https://cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search


# To enable the Vertex API
https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=YOURPROJECTID