
import os
import traceback
import discord
from discord.ext import commands
from urllib import parse, request
import re
import datetime
import pytz
from bs4 import BeautifulSoup


bot = commands.Bot(command_prefix = '/' , description="This is a Helper Bot" )
token = os.environ['DISCORD_BOT_TOKEN']
TEST_ID = 737270360277254164

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def dii(ctx):
    await ctx.send('バカ')

@bot.command()
async def pict(ctx):
    await ctx.send('http://www.no1game.net/games/escapemen/game0056.html')      

@bot.command()
async def clear(ctx, number = 1):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
        
    async for x in ctx.message.channel.history(limit = number+1):
         if counter < number+1:
             print(x)
             mgs.append(x)
             counter += 1
    await x.channel.delete_messages(mgs)
    delmsg = await ctx.send(str(counter-1) + "件削除しました")
    print(delmsg)
    await delmsg.delete(delay=2)
  
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    OBJ = BeautifulSoup(html_content,"html.parser")
    html_content.close()
    search_results = re.findall('"videoId":"(.{11})"' , OBJ.decode())
    if search_results :
        pass
    else:
        print('nasi')
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v='+ search_results[0])
    await ctx.send('https://www.youtube.com/watch?v='+ search_results[4])
      
@bot.event
async def on_ready():
   channel1 = bot.get_channel(TEST_ID)
   await channel1.send("起動")
         
          
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel == after.channel:
        print('STATS変更')
        return
    if after.channel is None:
        print('退出')
        return
    if  after.channel is not None:
        TIME = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        STR_TIME = TIME.strftime('%Y/%m/%d %H:%M')
        print(member.display_name + ' ' + after.channel.name)
        channel2 = bot.get_channel(TEST_ID)
        await channel2.send("[" + STR_TIME +  "]" + member.display_name + "が" + after.channel.name + "にきたぞ")
        
bot.run(token)
