import os
import discord
from texRender import *
from imageUtil import *
from filterMessage import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tex'):
      fullMessage = message.content
      filterMessage(fullMessage)
      #render_latex( LATEX, './out.png')
      #await message.channel.send(file=discord.File('./out.png'))


client.run(os.environ['TOKEN'])
