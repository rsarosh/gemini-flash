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
https://aistudio.google.com/
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
First you should just run the code without any parameter
``` 
 python main.py
 ```

 Then you can try by passing a file pdf file name, if it is not pdf then change the code slightly
 ```
python main.py AI_RMF_Playbook.pdf
```

# Vertex AI

Learn about Vertex AI - https://cloud.google.com/vertex-ai/docs/start/install-sdk
Learn about grounding https://ai.google.dev/gemini-api/docs/grounding?lang=python


### Steps
  1. To start a new project go to https://console.cloud.google.com/

  2. on your project page at console.cloud.google.com click on "API & Services" and enable the Vertext AI

  3. Click on cloud storage and create a bucket and upload your text file.

  4. Go to Agent Builder and click on create an agent

      Choose Custom Search 

      configure the custom search and storage etc

  5. Get the credentials from the Agent Builder and save it as gemini.json. https://developers.google.com/workspace/guides/create-credentials
  6.  read https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account
  










replace gemini copy.json file with a real file from your enviorenment. 



##  To enable the Vertex API

https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=YOURPROJECTID