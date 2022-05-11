import discord
from discord.ext import commands
import keep_alive
import json
import random


with open('setting.json',mode='r',encoding='utf8') as jfile:
   jdata=json.load(jfile)

MGRoid=commands.Bot(command_prefix=jdata['prefix'])

@MGRoid.event
async def on_ready():
    print('>> bot is online <<')


@MGRoid.event
async def on_member_join(member):
  print(f'{member}join')

@MGRoid.event
async def on_member_join(member):
  channel=MGRoid.get_channel(jdata['welcome_channel'])
  await channel.send(f'{member}入境')

@MGRoid.command()
async def ping(ctx):
    await ctx.send(f'{round(MGRoid.latency*1000)}(ms)')

@MGRoid.command()
async def tu(ctx):
  random_pic=random.choice(jdata['pic'])
  await ctx.send(random_pic)

keep_alive.keep_alive()

MGRoid.run(jdata['TOKEN'])