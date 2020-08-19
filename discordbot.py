
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
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/dii'):
        await client.send_message(message.channel,"バカ")
    
client.run(token)
