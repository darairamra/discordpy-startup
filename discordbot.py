
import os
import traceback
import discord
from urllib import parse, request
import re
import datetime
import asyncio
import platform
import random

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
TEST_ID = 737270360277254
test_channel = client.get_channel(TEST_ID)

@client.event
async def on_ready():
    
    await test_channel.send("起動")
            
@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == '/dii':
        await message.channel.send("バカ")
    
    if message.content == '/test':
        await test_channel.send("バカ")
        
client.run(token)
