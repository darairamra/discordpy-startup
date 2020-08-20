
import os
import traceback
import discord
from urllib import parse, request
import re
import datetime
import nest_asyncio
import platform
import random
nest_asyncio.apply()

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
TEST_ID = 737270360277254


@client.event
async def on_ready():
   test_channel = discord.Object(id=TEST_ID)
　　await test_channel.send("起動")
            
@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == '/dii':
        await message.channel.send("バカ")
    
        
client.run(token)
