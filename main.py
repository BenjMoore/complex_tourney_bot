# bot.py
import discord
from discord.ext import commands
import os
import discord
from flask import ctx
from discord import Client, Member

intents = discord.Intents.default()
intents.message_content = True

PerlsAssistant = commands.Bot(command_prefix='^', intents=intents)

@PerlsAssistant.event
async def on_ready():
    print("Everything's all ready to go~")
    print(""">> Everything's all ready to go :)""")
    os.system('cls')
    print("\033[0;35mPerl's Assistant, Version One\033[0m")
    print("\033[1;30m")
    
   
@commands.command()
async def test(ctx):
    await ctx.send("test") 


@commands.command()
async def shitpost(ctx):   
    await ctx.send("""What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.""")


@commands.command()
async def getids(ctx, member: Member):
    await ctx.send(f"ID >> {ctx.author.id} << Please use this in your signup!")

@commands.command()
async def helpme(ctx):
    await ctx.send("""
    Perls Assistant Version One
    Commands:
    ^getids -- Gets Player id  (Working)
    ^shitpost -- You get it (Working)
    ^signup -- Starts the tourney signup process (In development)
    ^tourneystats [username] -- displays wins losses and kd's (In development)
    ^fighttime [username] -- displays the players next fight time and info about the fight (In development)
    ^ping -- Shows bot latency (In development)
    
    PLEASE BE AWARE MOST OF THESE FEATURES HAVE NOT YET BEEN COMPLETED.
    THIS IS A BETA BOT""")

@commands.command()
async def signup(ctx, user: discord.User = None, *, value = None):
  if user == ctx.message.author:
    await ctx.send("You can't DM yourself goofy")
    await user.send(value)
  else:
    await ctx.message.delete()
    if user == None:
      await ctx.send(f'**{ctx.message.author},** Please Use a valid username')
    else:
      if value == None:
        await ctx.send(f'**{ctx.message.author},**  Please Use a valid username')
      else:
        await user.send(value)



PerlsAssistant.add_command(test)
PerlsAssistant.add_command(shitpost)
PerlsAssistant.add_command(getids)
PerlsAssistant.add_command(helpme)
PerlsAssistant.add_command(signup)
PerlsAssistant.run('MTA5ODg2MDg0NTQyMjg4NjkzMg.GGMh8h.qDvKf1cb9RROxHeflGqUNn2tc_ZCvmWnOqAqU4') ## Don't share lol.