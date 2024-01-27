# CONFIG YOUR API HERE :
RATE_LIMIT = 20  # sleeping time for openai per minute limitation
TOKEN_LIMIT = 5000  # token limit per message
TEMPERATURE = 1
MODEL = "gpt-3.5-turbo"

import os, time
from openai import OpenAI

# this is for printing messages in terminal
DEBUG = False


# getting open ai api key from the evnironmental variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# make content in openai wanted format
def create_message(role, content):
    return {"role": role, "content": content}


def send_message(
    intro, game_report, command, token_limit=TOKEN_LIMIT, time_limit_rate=RATE_LIMIT
):
    """
    Sending the request to api
    """

    time.sleep(time_limit_rate)
    context = [
        create_message("system", intro),
        create_message("user", game_report[-(token_limit - len(intro) - 70) :]),
        create_message("system", command),
    ]

    # connecting to Openai
    response = client.chat.completions.create(
        model=MODEL, messages=context, temperature=TEMPERATURE
    )
    # just for debugging in terminal
    if DEBUG:
        print(
            f"""
            #######################
            {intro}
            #######################
            {game_report}
            #######################
            {command}
            #######################
            -----------------------------
            {response.choices[0].message.content}
        """
        )
    # returning the response as a string
    return response.choices[0].message.content
