import discord
import os # مهم جدًا

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Bot is ready.')

# استبدل 'MY_TOKEN' بالمتغير الذي سنعرفه لاحقًا
client.run(os.environ.get('MTQxMTM1ODM5MDk3NzgyNjg0Ng.GKVP8l.nuCyz1KZGVKdI9ZAjBE-ua6XPZA2XWSMUGYUU8'))
