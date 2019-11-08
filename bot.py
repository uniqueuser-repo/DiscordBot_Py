import os
import discord
import datetime
from dotenv import load_dotenv
from ML_Algo import evaluate
import asyncio

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(641844809606365187)
    while True:
        counter += 1
        print("inside")
        await channel.send(createPrintString(datetime.datetime.today()))
        await asyncio.sleep(86400)

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
        printString = createPrintString(datetime.datetime.today())
        await message.channel.send(printString)


def createPrintString(dateToday):
    printString = "Ratings for " + dateToday.strftime('%m/%d/%Y') + ":\n"
    evaluated = evaluate()[1:-1]
    intList = [int(i) for i in evaluated.split()]

    printString += "Ford: " + str(intList[0]) + "\n"
    printString += "Wiley: " + str(intList[1]) + "\n"
    printString += "Hillenbrand: " + str(intList[2]) + "\n"
    printString += "Windsor: " + str(intList[3]) + "\n"
    return printString


client.loop.create_task(my_background_task())
client.run(TOKEN)