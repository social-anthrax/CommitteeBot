import discord
from discord.ext import commands
from discord.ext.commands.core import command
import datetime
from dateparser import parse
import calendarAPI

COMMITTEECHAT = 828691588766761021

description = '''A bot to help organise committee meetings'''

bot = commands.Bot(command_prefix='>')
intents = discord.Intents.default()
intents.members = True
token = open('discordToken.scrt').read()

calService = calendarAPI.authorize()


bot = commands.Bot(command_prefix='>', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    

@bot.command()
async def addMeeting(ctx, start, end):
    start = parse(start)
    end = parse(end)
    if ctx.channel.id == COMMITTEECHAT:
        await ctx.send(calService.addEvent(start, end))
    else: 
        await ctx.send("Not in <#828691588766761021>")


@bot.command()
async def meeting(ctx):
    if ctx.channel.id == COMMITTEECHAT:
        await ctx.send(calService.getEvents(1))
    else:
        await ctx.send("Not in <#828691588766761021>")

bot.run(token)
