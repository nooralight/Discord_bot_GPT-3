import openai
import os
from dotenv import load_dotenv
load_dotenv()
OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
openai.api_key = OPEN_AI_KEY

class Gpt_API:
    def __init__(self,prompt):
        self.prompt = prompt

    def get_result(self):
        completion = openai.Completion.create(engine="text-davinci-002", prompt=self.prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)
        #print(completion)
        text = completion.choices[0].text
        return text
