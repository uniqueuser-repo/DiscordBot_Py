import os
import discord

from dotenv import load_dotenv
from ML_Algo import evaluate
import asyncio

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send("Hi, " + member.name + ", welcome to my Discord server!")
    channel = client.get_channel(641860185631096842)
    await channel.send("Welcome to " + member.name + "!")

@client.event
async def on_message(message):
    print(message.content)
    if (message.author == client.user):
        return

    if (message.content.lower() == ".bot_up help"):
        await message.channel.send(".google [query]\nReturns the google link of the query in place of [query].\nExample: .google hello"
                                   " will return https://google.com/search?q=hello\n")

    if (message.content.lower().startswith(".google")):
        query = message.content.lower()[7:]
        print(query)
        querysplit = query.split()
        printableMessage = "https://google.com/search?q="
        for element in querysplit:
            printableMessage += element + "+"
        printableMessage = printableMessage[0:-1]
        await message.channel.send("Here you go! " + printableMessage)

    if (message.content.lower().startswith(".foodme")):
        printString = evaluate()

        await message.channel.send(evaluate())

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id=641844809606365187)
    while not client.is_closed:
        counter += 1
        print("inside")
        await client.send_message(channel, evaluate())
        await asyncio.sleep(1)

client.loop.create_task(my_background_task())
client.run(TOKEN)