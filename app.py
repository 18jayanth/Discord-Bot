# This example requires the 'message_content' intent.

import discord
import requests


from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()  
token=os.getenv("MY_SECRET_KEY")

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
text= response.json()
#print(data)
#print(data["choices"][0]["message"]["content"])
print("AI:", text)

  
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        channel=message.channel
        await channel.send('Hello I am BOTGPT')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
