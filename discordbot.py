
from discord.ext import commands
import os
import traceback
import discord
from urllib import parse, request
import re
import datetime

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def dii(ctx):
    await ctx.send("バカ")
    
    
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

 
@bot.event
async def on_voice_state_update(member, before, after): 
    if member.name == "Dii" or "だらい":
        alert_channel = '737270360277254164'
        voice_channel = '250171026988728320'
        channel = client.get_channel(alert_channel)
        if after.channel.id == voice_channel: 
            msg = f'{member.name} さんが {after.channel.name} に入室しました！'
            await channel.send(msg)
    
    
bot.run(token)
