
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

@client.event
async def on_ready():
    channel = client.get_channel(737270360277254)
    msg = "起動完了"
    await client.send_message(channel,msg)
            
@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.startswith('/dii'):
        await message.channel.send("バカ")
    
client.run(token)
