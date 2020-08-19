
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
    
 
@client.event
async def on_voice_state_update(member, before, after): 
    if member.id == "185767477291122689":
        alert_channel = '737270360277254164'
        voice_channel = '250171026988728320'
        channel = client.get_channel(alert_channel)
        if after.channel.id == voice_channel: 
            msg = f'{member.name} さんが {after.channel.name} に入室しました！'
            await channel.send(msg)
    
    
client.run(token)
