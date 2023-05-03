import os
import openai
from webex_bot.models.command import Command as cmd
import json
import time

#Input your openai API Key
openai.api_key = ""

#Input dir path in which gpt.json locates
with open("~/gpt.json", "r") as card:
    INPUT_CARD = json.load(card)

class GPT(cmd):
    def __init__(self):
        super().__init__(
            command_keyword = "gpt",
            help_message= "gpt--> you will get the reply provided by chatGPT",
            card = INPUT_CARD
        )

    def pre_execute(self, message, attachment_actions, activity):
        return "working on it... pls wait\n\"Life is tough nut to crack, isn't it?\""
    
    def execute(self, message, attachment_actions, activity):
        start = time.time()
        message = attachment_actions.inputs["input_text"]
        response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt = str(message),
                    temperature=0.3,
                    max_tokens = 3500,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
        )
        return response["choices"][0]["text"]