from dotenv import load_dotenv
import os
from langchain.llms import OpenAI

# read environment var
class Env:
    def __init__(self,path) -> None:
        self.OpenAi_Key = ""
        self.path = path
        pass
    def load(self):
        load_dotenv(self.path+"/.env")
        self.OpenAi_Key = os.getenv("OPENAI_API_KEY")
        pass


if __name__ == "__main__":
    print("start")
    env = Env(".")
    env.load()
    llm = OpenAI(openai_api_key=env.OpenAi_Key)
    print(llm.predict("你可以告诉我如何使用langchain搭建一个gpt应用吗"))
    pass