import os

import pytest as pytest
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

from app import chat_model_dict
from prompts import system_prompt, user_information

load_dotenv()

class TestChains():

    FAKE_RESUME = "I am a computer scientist"
    FAKE_JOB_DESCRIPTION = "This is a computer science job"
    FAKE_ADDITIONAL_INFORMATION = "We love the environment"

    @pytest.mark.parametrize("chain_type", list(chat_model_dict.keys()))
    def test_resume_chain(self, chain_type):
        result = chat_model_dict[chain_type](
            resume=self.FAKE_RESUME,
            job_description=self.FAKE_JOB_DESCRIPTION,
            additional_information=self.FAKE_ADDITIONAL_INFORMATION,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo"
        )
        assert isinstance(result, str) and len(result) > 0