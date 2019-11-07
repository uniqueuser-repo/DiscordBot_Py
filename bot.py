import os
import discord

from dotenv import load_dotenv

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
        await message.channel.send("I'm so sorry. I don't really have very many commands yet!")

    if (message.content.lower().startswith(".google")):
        query = message.content.lower()[7:]
        print(query)
        querysplit = query.split()
        printableMessage = "https://lmgtfy.com/?q="
        for element in querysplit:
            printableMessage += element + "+"
        printableMessage = printableMessage[0:-1]
        printableMessage += "&s=g"
        await message.channel.send("Here you go! " + printableMessage)



client.run(TOKEN)