import os
import discord
import datetime
from datetime import timedelta
from dotenv import load_dotenv
from ML_Algo import evaluate
from multiprocessing import Process
import asyncio
import psutil
import traceback

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

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
    channel = client.get_channel(640793807121809408)
    await channel.send("Welcome to " + member.name + "!")

@client.event
async def on_message(message):
    print(message.content.lower())
    if message.author == client.user:
        return

    if message.author.id == 443954797520093185 or message.author.id == 116275390695079945:
        if message.content.lower().count(".foodme") > 0:
            print("CONSOLE: ignoring command from blocked user...")
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

    try:
        if message.content.lower().startswith(".foodme"):
            if len(message.content.lower().split()) > 1:  # for the case where a date is specified
                splitList = message.content.lower().split()
                dateString = splitList[1]  # acquires the specified date, stores in dateString
                date_time_obj = datetime.datetime.strptime(dateString, '%m/%d/%Y')
                if date_time_obj.weekday() == 6:
                    await message.channel.send("That's a Sunday homie. No din din.")
                else:
                    printString = createPrintStringNoMention(date_time_obj)
                    await message.channel.send(printString)
            else: # for the case where no date is specified, i.e. today
                printString = createPrintStringNoMention(datetime.datetime.today())
                await message.channel.send(printString)

            for process in psutil.process_iter():
                try:
                    if process.name().startswith("chromedriv"): # kill leftover runaway processes
                        process.terminate()
                except psutil.NoSuchProcess:
                    pass

    except ValueError as e:
        print("yikes")
        await message.channel.send(str(e))
    except Exception as e:
        print("yikes")
        await message.channel.send("Please see console! Unexpected exception:\n" + str(e))
        traceback.print_exc()

def createPrintStringMention(dateTime):
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



def createPrintStringNoMention(dateTime):
    printString = "Ratings for " + dateTime.strftime('%m/%d/%Y') + ":\n"
    evaluated, foodString = evaluate(dateTime)
    evaluated = evaluated[1:-1]
    intList = [int(i) for i in evaluated.split()]

    printString += "Wiley: " + str(intList[0]) + "\n"
    printString += "Hillenbrand: " + str(intList[1]) + "\n"
    printString += "Windsor: " + str(intList[2]) + "\n"
    printString += "Ford: " + str(intList[3]) + "\n"
    printString += "\n" + foodString

    return printString

client.run(TOKEN)
