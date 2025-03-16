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
How to get the keys, check this page: https://ai.google.dev/gemini-api/docs/api-key

To get your keys
https://aistudio.google.com/app/apikey

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


# To enable the Vertex API
https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=YOURPROJECTID