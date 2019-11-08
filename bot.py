import os
import discord
import datetime
from datetime import timedelta
from dotenv import load_dotenv
from ML_Algo import evaluate
from multiprocessing import Process
import asyncio

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

client = discord.Client()



async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(640793807121809408)
    while True:
        datetimeNow = datetime.datetime.today()
        datetimeNextDay = datetime.datetime.today() + timedelta(days=1)
        datetimeNextDay = datetimeNextDay.replace(hour=9, minute=0, second=0)
        totalWait = (datetimeNextDay-datetimeNow).total_seconds()
        await channel.send(await createPrintStringNoMention(datetime.datetime.today()))
        await asyncio.sleep(totalWait)

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
    channel = client.get_channel(640793807121809408)
    await channel.send("Welcome to " + member.name + "!")

@client.event
async def on_message(message):
    print(message.content.lower())
    if message.author == client.user:
        return

    if message.content.lower() == ".bot_up help":
        await message.channel.send(".google [query]\nReturns the google link of the query in place of [query].\nExample: .google hello"
                                   " will return https://google.com/search?q=hello\n")

    if message.content.lower().startswith(".google"):
        query = message.content.lower()[7:]
        print(query)
        querysplit = query.split()
        printableMessage = "https://google.com/search?q="
        for element in querysplit:
            printableMessage += element + "+"
        printableMessage = printableMessage[0:-1]
        await message.channel.send("Here you go! " + printableMessage)

    if (message.content.lower().startswith(".foodme")):
        if len(message.content.lower().split()) > 1:
            splitList = message.content.lower().split()
            dateString = splitList[1]
            date_time_obj = datetime.datetime.strptime(dateString, '%m/%d/%Y')
            printString = await createPrintStringNoMention(date_time_obj)
            await message.channel.send(printString)
        else:
            printString = await createPrintStringMention(datetime.datetime.today())
            await message.channel.send(printString)


async def createPrintStringMention(dateTime):
    printString = createPrintStringNoMention(dateTime)

    roles = client.guilds[0].roles
    elementMention = 0
    for element in roles:
        if element.name == "Andy's croo":
            elementMention = element.mention
            break

    printString += str(elementMention)
    printString += "\n"

    return printString



async def createPrintStringNoMention(dateTime):
    printString = "Ratings for " + dateTime.strftime('%m/%d/%Y') + ":\n"
    evaluated = evaluate(dateTime)[1:-1]
    intList = [int(i) for i in evaluated.split()]

    printString += "Ford: " + str(intList[0]) + "\n"
    printString += "Wiley: " + str(intList[1]) + "\n"
    printString += "Hillenbrand: " + str(intList[2]) + "\n"
    printString += "Windsor: " + str(intList[3]) + "\n"

    return printString


client.loop.create_task(my_background_task())
client.run(TOKEN)