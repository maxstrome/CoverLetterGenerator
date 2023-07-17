# AI Cover Letter Generator

Welcome to the AI Cover Letter Generator! This open-source project uses OpenAI's GPT Models, Langchain, and Streamlit to create an interactive web application that generates a customized cover letter based on your resume and a job description. The project is designed to simplify the job application process and help job seekers create high-quality, personalized cover letters more efficiently.  This project is deployed using Streamlit cloud and can be found at [cover letter generator](https://aicoverlettergenerator.streamlit.app/).  I also wrote a medium blog post describing the code which can be found here [medium article](https://medium.com/@mstrome/langchain-streamlit-cover-letter-generator-1cbc00c858c3).

## Features

- Upload your resume in `.docx` format
- Input the company description and job details
- Generates a unique cover letter using AI

## Installation

1. Clone this repository:
`git clone https://github.com/maxstrome/CoverLetterGenerator.git`
2. Change to the project directory:
`cd ai-cover-letter-generator`
3. Install the required dependencies:
`pip install -r requirements.txt`
## Usage

1. Run the Streamlit application:
`streamlit run app.py`
2. Navigate to the URL provided in the console (usually `http://localhost:8501`).
3. Enter your OpenAI API key in the sidebar.
4. Upload your resume in `.docx` format using the file uploader.
5. Input the company description and any additional information about the job in the text areas.
6. Click the "Generate Cover Letter" button to generate your cover letter.

Once your cover letter has been generated, you can view it in the application, and you will also be given the option to download it as a Word document.

## Contributing

We welcome contributions to the AI Cover Letter Generator! If you'd like to contribute, feel free to fork this repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.


