# import requests

# url = "https://raw.githubusercontent.com/groq/models/main/models.json"
# models = requests.get(url).json()
# print(models)
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()  
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

models = client.models.list()
for m in models.data:
    print(m.id)
