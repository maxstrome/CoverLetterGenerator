import os

import streamlit as st
from dotenv import load_dotenv

from chains import get_cover_letter_langchain_normal_prompts, get_cover_letter_langchain_chat_prompts, \
    get_cover_letter_langchain_no_chain, get_cover_letter_no_langchain
from utils import read_docx, write_string_to_word

load_dotenv()

chat_model_dict = {
    'LangChain Prompt Template': get_cover_letter_langchain_normal_prompts,
    'Langchain ChatPrompt Template': get_cover_letter_langchain_chat_prompts,
    "Langchain no chain": get_cover_letter_langchain_no_chain,
    'Custom code': get_cover_letter_no_langchain
}

def build_streamlit_app():
    # Set the title of the Streamlit app to 'Cover Letter Generator'
    st.title('Cover Letter Generator')

    # Create an input box in the sidebar of the app for the OpenAI API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key is None:
        openai_api_key = st.sidebar.text_input('OpenAI API Key')

    cover_letter_type = st.sidebar.selectbox(
        'Select the cover letter generation method',
        tuple(chat_model_dict.keys())
    )

    model = st.sidebar.selectbox(
        'Select the model you wish to use',
        (
            'gpt-3.5-turbo',
            'gpt-4'
        )
    )

    # Create a file uploader widget for uploading a docx file (the user's resume)
    resume = st.file_uploader("Upload your Resume", type='docx')
    resume_text = None

    # If a resume has been uploaded, read the text from the docx file
    if resume is not None:
        resume_text = read_docx(resume)

    # Create a text input area for pasting the company description
    job_description = st.text_area('Paste the job description here')

    # Create a text input area for pasting any additional company information
    additional_information = st.text_area('(Optional) Paste additional company information here')

    # Create a button for generating the cover letter
    if st.button('Generate Cover Letter'):
        # Check if the OpenAI key, resume, and company description are provided
        if not openai_api_key or not openai_api_key.startswith('sk-'):
            # Display a warning if the OpenAI API key is not provided or is invalid
            st.warning('Please enter your OpenAI API key!', icon='⚠️')
        elif resume is None:
            # Display a warning if the resume has not been uploaded
            st.warning('Please upload your Resume!', icon='⚠️')
        elif not job_description:
            # Display a warning if the company description is not provided
            st.warning('Please enter the company description!', icon='⚠️')
        else:
            # If all conditions are met, call the cover letter generation function
            # Show a spinner while the function is running
            with st.spinner('Generating your cover letter...'):
                result = chat_model_dict[cover_letter_type](
                    resume=resume_text,
                    job_description=job_description,
                    additional_information=additional_information,
                    openai_api_key=openai_api_key,
                    model=model
                )
            # Display a success message when the cover letter generation is completed
            st.success('Cover letter generation completed!')

            # Write the generated cover letter to the app
            st.write('**Your Generated Cover Letter:**')
            st.write(result)
            # Create a Word document
            write_string_to_word(result, filename="cover_letter.docx")

            # Create a download button for the cover letter document
            with open("cover_letter.docx", "rb") as file:
                btn = st.download_button(
                    "Download Cover Letter",
                    file,
                    file_name="Cover_Letter.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )

if __name__ == '__main__':
    build_streamlit_app()