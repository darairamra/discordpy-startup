from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_voice_state_update(member, before, after):
    if before.status = none:
       msg =  member
       await ctx.send(test,msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def dii(ctx):
    await ctx.send('bakaaho')


bot.run(token)
