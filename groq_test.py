import os
import requests
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "user", "content": "Explain binary search simply."}
    ]
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()
print(data)
print(data["choices"][0]["message"]["content"])
