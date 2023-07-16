from typing import Optional

import openai
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage

from prompts import system_prompt, user_information


def get_cover_letter_langchain_normal_prompts(
        resume: str,
        job_description: str,
        openai_api_key: str,
        model: str,
        additional_information: Optional[str] = None
) -> str:
    llm = ChatOpenAI(
        model=model,
        temperature=0.2,
        openai_api_key=openai_api_key
    )
    prompt = system_prompt + "\n---\n" + user_information + "\n---\nCover Letter:"
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )

    additional_information = additional_information if additional_information is not None else "None"
    args = {
        "resume": resume,
        "job_description": job_description,
        "additional_information": additional_information
    }

    return llm_chain.run(args)


def get_cover_letter_langchain_chat_prompts(
        resume: str,
        job_description: str,
        openai_api_key: str,
        model: str,
        additional_information: Optional[str] = None
) -> str:
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_prompt)
    user_message_prompt = HumanMessagePromptTemplate.from_template(user_information)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, user_message_prompt]
    )

    llm = ChatOpenAI(temperature=0.2, openai_api_key=openai_api_key, model=model)
    llm_chain = LLMChain(
        llm=llm,
        prompt=chat_prompt
    )
    additional_information = additional_information if additional_information is not None else "None"
    args = {
        "resume": resume,
        "job_description": job_description,
        "additional_information": additional_information
    }

    return llm_chain.run(args)

def get_cover_letter_langchain_no_chain(
        resume: str,
        job_description: str,
        openai_api_key: str,
        model: str,
        additional_information: Optional[str] = None
) -> str:
    additional_information = additional_information if additional_information is not None else "None"
    args = {
        "resume": resume,
        "job_description": job_description,
        "additional_information": additional_information
    }
    user_message_prompt = user_information.format(**args)

    llm = ChatOpenAI(temperature=0.2, openai_api_key=openai_api_key, model=model)

    return llm([SystemMessage(content=system_prompt), HumanMessage(content=user_message_prompt)]).content

def get_cover_letter_no_langchain(
        resume: str,
        job_description: str,
        openai_api_key: str,
        model: str,
        additional_information: Optional[str] = None
) -> str:
    openai.api_key = openai_api_key
    args = {
        "resume": resume,
        "job_description": job_description,
        "additional_information": additional_information
    }
    user_message_prompt = user_information.format(**args)
    return openai.ChatCompletion.create(
        model=model,
        temperature=.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message_prompt},
        ]
    )["choices"][0]["message"]["content"]