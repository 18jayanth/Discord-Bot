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
with open('chat.txt','r',encoding="utf-8") as f:
    chat=f.read()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat+=f"{message.author}: {message.content}\n"
        print(f'Message from {message.author}: {message.content}')
        if self.user!=message.author:
            if self.user in message.mentions:
                print(chat)
                channel=message.channel
                
                payload = {
                    "model": "llama-3.3-70b-versatile",
                    "messages": [
                    {"role": "user", "content": f"{chat}\nBotGPT: "}
                        ]
                        }
                response = requests.post(url, json=payload, headers=headers)
                data = response.json()
                messagetosend=data["choices"][0]["message"]["content"]        
                await channel.send(messagetosend)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
