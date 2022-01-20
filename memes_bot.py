import discord
import requests
import json

# make a discord client

client=discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(msg):
    if(msg.author==client.user):
        return

    if(msg.content.startswith("!hey")):
        # print(msg.id)
        await msg.channel.send("Hey from a bot")

    if(msg.content.startswith("$greet")):
        channel=msg.channel

        
        await channel.send("Say hello!")

        def check(m):
            return m.content=='hello' and m.channel==channel

        try:
            is_replied=await client.wait_for('message',check=check,timeout=5.0)
            await channel.send('Hello {.author}!'.format(is_replied))    
            print(is_replied.user_id)
            print(client.get_emoji(is_replied.id))
        except:
            response=requests.get("https://zenquotes.io/api/random")
            json_data=json.loads(response.text)
            quote=json_data[0]['q'] + " -" + json_data[0]['a']
            await msg.channel.send(quote)
            # print("TimeOut")


client.run("OTMyNTMzNDU4NjkyMDgzNzMy.YeUXdg.eRnbUaxmmSAcg59K12GZbUYq2k0")                