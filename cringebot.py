# bot.py
import os
import random
import discord


from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    insults = ['Go fuck yourself', 'touch grass', 'eat a dick', 'My balls have more IQ than you',
               'write that on my balls because that’s how many fucks I give about what you just said']

    if 'cringe' in str(message.content):
        response = random.choice(insults)
        await message.channel.send(response)

    lol2 = 'nice'

    if '69' in str(message.content):
        response2 = lol2
        await message.channel.send(response2)



client.run(TOKEN)
