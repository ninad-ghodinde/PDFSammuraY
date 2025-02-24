
# PDFSammurAI

PDFSammurAI is an AI-Powered PDF Assistant.It's an open source LLM application designed to interact with your PDF document.

The name PDFSammurAI is a combination of PDF and Samurai.
This innovative tool harnesses the power of AI, allowing you to engage in natural language conversations with your PDF files, extracting meaningful information and insights without the need to read through the entire document.

Try it here: https://pdfsammuray.streamlit.app/



## How to run locally
## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An active internet connection
- A Groq API key (sign up at [Groq](https://groq.com) if you don't have one)

## Cloning the Repository

To clone this repository to your local machine, follow these steps:

1. Open your terminal (Command Prompt, PowerShell, or any terminal emulator).
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:

```bash
git clone https://github.com/ninad-ghodinde/PDFSammuraY.git
```
Change into the project directory:
```bash 
cd PDFSammuraY
```
## Install the required packages:
Make sure you have pip installed, then run:

```
pip install -r requirements.txt
```
## Setting Up the Environment variables
Create a .secrets file in the root of your project directory and add your Groq API key like this:
```
touch ~/.streamlit/secrets.toml
```
And add
```
API_KEY = "your Groq API key"
```

## Running the Application
Once everything is set up, you can run the Streamlit application with the following command:
bash
```
streamlit run main.py
```
## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.
