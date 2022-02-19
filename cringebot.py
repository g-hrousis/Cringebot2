# bot.py
import os
import random
import discord
from discord.ext import commands

from dotenv import load_dotenv
intents = discord.Intents(messages=True, members=True, guilds=True)

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')
client = commands.Bot(command_prefix="!", intents=intents)



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
    await client.change_presence(activity=discord.Streaming(name="your sister's OnlyFans",url='https://www.youtube.com/watch?v=OLpeX4RRo28'))

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    insults = ['Go fuck yourself', 'touch grass', 'eat a dick', 'My balls have more IQ than you',
               'write that on my balls because that’s how many fucks I give about what you just said'
        ,'you look like you do discord kitten roleplay']

    if 'cringe' in str(message.content):
        response = random.choice(insults)
        await message.channel.send(response)

    lol2 = 'nice'

    if '69' in str(message.content):
        response2 = lol2
        await message.channel.send(response2)

    diseases = ["Hepatitis B ", "Rotavirus", "Ligma", "Diphtheria", "Haemophilus Influenzae Type B"
        , "Pneumococcal conjugate", "Inactivated poliovirus", "Influenza"]

    if 'canyon' in str(message.content):
        response3 = random.choice(diseases)
        await message.channel.send(response3)

    if message.content.startswith("I hate this bot"):
        dm = await message.author.create_dm()
        await dm.send("Fuck you nobody loves you")

    redditard = ["Stfu Redditard", "Get of r/datingtip and meet real women"]
    if "reddit" in str(message.content):
        response4 = random.choice(redditard)
        await message.channel.send(response4)

    weebshit = ["Bro is this really what you're doing with your life, you stinky weeb"
        , "Your waifu is made of pixels, go talk to a real women", "Pixels won't take your virginity"]

    if ("/wa") in str(message.content):
        response5 = random.choice(weebshit)
        await message.channel.send(response5)
    if ("$wa") in str(message.content):
        response5 = random.choice(weebshit)
        await message.channel.send(response5)

@client.command()
async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)





client.run(TOKEN)
