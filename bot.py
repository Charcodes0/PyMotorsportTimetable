import os

import discord
import logging
import re

from series_requester import interpret_series, instantiate_directory

# Do we want only admins to use the bot?

author_checking = True

# Client Variables

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print("Message received")

    if author_checking:
        if message.author.id not in admin_id_list:
            return

    if message.content.startswith('_OVERRIDE'):
        await send_message(message, False)
    if message.content.startswith('_'):
        print("Good Start")
        # Shitpost testing
        if message.content.upper() == "_GENTLEMEN":
            await message.channel.send('Gentlemen, a short view back to the past. Thirty years ago, Niki Lauda told us ‘take a monkey, place him into the cockpit and he is able to drive the car.’ Thirty years later, Sebastian told us ‘I had to start my car like a computer, it’s very complicated.’ And Nico Rosberg said that during the race – I don’t remember what race - he pressed the wrong button on the wheel. Question for you both: is Formula One driving today too complicated with twenty and more buttons on the wheel, are you too much under effort, under pressure? What are your wishes for the future concerning the technical programme during the race? Less buttons, more? Or less and more communication with your engineers? ')
        await send_message(message, True)

async def send_message(message, dl : bool):
    if dl:
        message_content = message.content[1:]
    else:
        message_content = message.content[9:]
    msg = interpret_series(message_content, False, dl)

    await message.channel.send(combine_series(msg))

def combine_series(msg):
    output = ""
    for i in msg:
        if len(output) + len(i) < 1965:
            output += i
        else :
            output += "\n Max Message Length Reached!"
    return output

def ensure_secrets_exist():
    if not os.path.exists("secret"):
        os.makedirs("secret")
        open("secret/token.txt", "x").close()
        open("secret/admins.txt", "x").close()
        print("INFO: Creating secret folder and files.")

def check_files_not_empty():
    throw_error = False
    with open("secret/token.txt", "r") as file:
        if file.read() == '':
            print("INFO: Secret file is empty.")
            throw_error = True
    with open("secret/admins.txt", "r") as file:
        if file.read() == '':
            print("INFO: Admins file is empty.")
            throw_error = True
    if throw_error:
        raise ValueError(
            "Please fill in the token.txt file with your bot token, and admins.txt with the ID's of bot admins.")

# Secrets

# Ensuring files exist
ensure_secrets_exist()

# Ensuring files have data
check_files_not_empty()

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

# One Time Instantiation

instantiate_directory()

client.run(token)