
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
         
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel == after.channel:
        print('STATS変更')
        return
    if after.channel is None:
        print('退出')
        return
    if member.display_name == 'だらい' and after.channel is not None:
        print(after.channel)
        channel2 = client.get_channel(TEST_ID)
        await channel2.send( after.channel.name + "にきたぞ")
        
client.run(token)
