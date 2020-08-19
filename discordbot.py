
from discord.ext import commands
import os
import traceback
import discord
from urllib import parse, request
import re
import datetime
import asyncio
from discord.ext.commands import Bot
import platform
import random


client = Bot(command_prefix="/", pm_help = False)
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.command()
async def ping(ctx):
    await ctx.send('pong')
    
@client.command()
async def dii(ctx):
    await ctx.send("バカ")
    
    
@client.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

 
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
