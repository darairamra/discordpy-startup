
import os
import traceback
import discord
from urllib import parse, request
import re
import datetime


client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
TEST_ID = 737270360277254164


@client.event
async def on_ready():
   channel1 = client.get_channel(TEST_ID)
   await channel1.send("起動")
            
@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == '/dii':
        await message.channel.send("バカ")
    
        
client.run(token)
