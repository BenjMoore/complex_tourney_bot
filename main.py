# bot.py
import os
import discord
from discord.ext import commands
from flask import ctx
from discord import Member
import asyncio 
from antispam import AntiSpamHandler,Options
from antispam.enums import Library
prefix = "^"
intents = discord.Intents.all()    
PerlsAssistant = commands.Bot(command_prefix=prefix,intents=intents)
ver = 1.0


PerlsAssistant.handler = AntiSpamHandler(PerlsAssistant,library=Library.DPY)

@PerlsAssistant.event
async def on_ready():
    print(""">> Everything's all ready to go :)""")
    print("\033[0;35mPerl's Assistant, Version One\033[0m")
    print("\033[1;30m")
   

@PerlsAssistant.event
async def on_message(message):
        return

@PerlsAssistant.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''
    # Get the latency of the bot
    latency = PerlsAssistant.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@PerlsAssistant.command()
async def getids(ctx, member: Member):
    await ctx.send(f"Your ID >> {ctx.author.id} << Please use this in your signup!")

@PerlsAssistant.command()
async def whatdidyousaytome(ctx):
    await ctx.send("""What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.""")
    
@PerlsAssistant.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

PerlsAssistant.run('MTA5ODg2MDg0NTQyMjg4NjkzMg.GGMh8h.qDvKf1cb9RROxHeflGqUNn2tc_ZCvmWnOqAqU4')