import discord
import os
import requests
import json




client = discord.Client()


def get_quote():
    response=requests.get("https://zenquotes.io/api/random")

    json_data=json.loads(response.text)
    quote=json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    if(message.content.startswith("$hello")):
        await message.channel.send("Hello")
    if(message.content.startswith("!inspire")):
        q=get_quote()
        await message.channel.send(q)   

client.run("OTMyMjMxOTEyNjMyNzY2NTM3.YeP-oA.l_G_yTuphOSWPJLNi52Cvd_VJt4")            

