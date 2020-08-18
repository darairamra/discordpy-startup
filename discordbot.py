from discord.ext import commands
import os
import traceback
import discord


client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if message.content.startswith("test"):
       if client.user != message.author:
        msg = "失敗" + massage.author.name
        await message.channel.send(msg)


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
    await ctx.send('bakaaho')


bot.run(token)
client.run(token)
