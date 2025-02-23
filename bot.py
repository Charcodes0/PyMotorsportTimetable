import discord
import logging
import re

from series_requester import interpret_series

# Do we want only admins to use the bot?

author_checking = True

# Client Variables

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Secrets

#Define the bot token
token_file = open("secret/token.txt", "r")
token = token_file.read()
token_file.close()

# Define Admins
admin_id_list = []
admin_file = open("secret/admins.txt", "r")
for line in admin_file:
    txt = line.strip()
    txt = txt.split(" = ")
    admin_id_list.append(int(txt[1]))
admin_file.close()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print("Message received")

    if author_checking:
        if message.author.id not in admin_id_list:
            return

    if message.content.startswith('_'):
        print("Good Start")
        await send_message(message)

async def send_message(message):
    message_content = message.content[1:]
    msg = interpret_series(message_content, False)

    for i in msg:
        await message.channel.send(i)


client.run(token)