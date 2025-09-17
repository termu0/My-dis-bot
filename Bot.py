import discord
import os 

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Bot is ready.')

 
client.run(os.environ.get('MTQxMTM1ODM5MDk3NzgyNjg0Ng.GKVP8l.nuCyz1KZGVKdI9ZAjBE-ua6XPZA2XWSMUGYUU8'))
