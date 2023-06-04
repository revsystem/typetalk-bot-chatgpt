# coding: utf-8

from const import *

def create_prompt_to_summarise_message(user_messages: str) -> list:
    """
    Create a prompt to request a summary of the message.

    :param user_messages: The message that user posted to the Typetalk.
    :return: list
    """

    prompt = []

    prompt = [
        {
            'role': 'user',
            'content': "Please summarise the following message in approximately 30 words." + "\n" + user_messages
        },
        {
            'role': 'assistant',
            'content': '{summarised message.}'
        },
    ]

    return prompt

def get_message(prompt_message: list = []) -> str:
    """
    Get the OpenAI API responce.

    :param prompt_message: History of the conversation.
    :return: The OpenAI API responce.
    """

    response = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=prompt_message,
        temperature=OPENAI_TEMPERATURE,
        max_tokens=OPENAI_MAX_TOKENS,
        top_p=OPENAI_TOP_P,
        frequency_penalty=OPENAI_FREQUENCY_PENALTY,
        presence_penalty=OPENAI_PRESENCE_PENALTY
    )

    message = response["choices"][0]["message"]["content"]

    return message
