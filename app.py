from dotenv import load_dotenv
import os

load_dotenv()

from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain import hub
from transformers import AutoTokenizer

google_cse_id = os.getenv("GOOGLE_CSE_ID")
google_api_key = os.getenv("GOOGLE_API_KEY")

from langchain_google_community import GoogleSearchAPIWrapper

google_search = GoogleSearchAPIWrapper(google_cse_id=google_cse_id, google_api_key=google_api_key)

respose = google_search.run("What is the meaning of life?")

print(respose)

HUGGINGFACEHUB_API_TOKEN=os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm=HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta")

chat_model=ChatHuggingFace(llm=llm)


prompt = hub.pull("hwchase17/structured-chat-agent")

print(prompt)
