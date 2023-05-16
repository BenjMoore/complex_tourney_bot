# Complex Tourney Discord Bot #
# Version one 
# Do not distribute


## Imports ##
import discord
from discord.ext import commands
import os
import discord
from flask import ctx
from discord import Client, Member
import datetime
## Imports END ##

intents = discord.Intents.default()

intents.message_content = True ## Sets Permissions for discord, ie intent to see write and manage the server

PerlsAssistant = commands.Bot(command_prefix='^', intents=intents) ## Initialise Bot (Bot in variable names is PerlsAssistant)


@PerlsAssistant.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = message.channel.name
  print(f'{username}: {user_message} ({channel})')
  seconds = 5 # The seconds ago to check messages.

  now = datetime.datetime.now()

  messages = 0
## ANTI SPAM ##
  for message in channel:
      if message.author == PerlsAssistant.user:
          message_time = message.created_at.timestamp()
          if message_time > now - datetime.timedelta(seconds=seconds):
              messages += 1
              if messages == 3:
                  await message.delete()
      
      flaggedMessages = "FUCK"
      if user_message == flaggedMessages:
          await message.delete()
      return
 ## ANTI SPAM ##
 

## WHEN BOT HAS STARTED ##
@PerlsAssistant.event # event is onready ie when bot starts
async def on_ready():
    print("Everything's all ready to go~")
    print(""">> Everything's all ready to go :)""")
    os.system('cls') # clear screen
    print("\033[0;35mPerl's Assistant, Version One\033[0m")
    print("\033[1;30m")
    Client(intents=intents)
    

@commands.command()
async def test(ctx):
    await ctx.send("test") 

## SHITPOST ##
@commands.command()
async def shitpost(ctx):   
    await ctx.send("""```What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.```""")
## SHITPOST END ##

## GET IDS ##
@commands.command()
async def getids(ctx):
    await ctx.send(f"```ID >> {ctx.author.id} << Please use this in your signup!```")

## GET IDS END ##

## HELP ##
@commands.command()
async def helpme(ctx):
    await ctx.send("""```
    Perls Assistant Version One
    Commands:
    ^getids -- Gets Player id  (Working)
    ^shitpost -- You get it (Working)
    ^signup -- Starts the tourney signup process (In development)
    ^tourneystats [username] -- displays wins losses and kd's (In development)
    ^fighttime [username] -- displays the players next fight time and info about the fight (In development)
    ^ping -- Shows bot latency (In development)
    
    PLEASE BE AWARE MOST OF THESE FEATURES HAVE NOT YET BEEN COMPLETED.
    THIS IS A BETA BOT```""")
## HELP END ##

## PING ##
@commands.command()
async def ping(ctx):
     await ctx.send(f"```Pong! My ping is: {round (PerlsAssistant.latency * 1000)} ms```")
## PING END ##


## Signup DM Chain ##

@commands.command()
async def signup(ctx, user: discord.User = None, *, value = None):
  if user == ctx.message.author: # if person who sends the message is the same person whom wrote the message
    await ctx.send("You can't DM yourself goofy")
    await user.send(value) # dm
  
    if user == None: 
      await ctx.send(f'```**{ctx.message.author},** Please Use a valid username```') # ctx.message.author is the person whom wrote the message
    else:
      if value == None: # if nothing is typed in the command except signup
        await ctx.send(f'```**{ctx.message.author},**  Please Use a valid username```') # ctx.message.author is the person whom wrote the message
      else:
        await user.send(value)

## Signup DM Chain END ##

## Add Commands to bot ##

PerlsAssistant.add_command(test)
PerlsAssistant.add_command(shitpost)
PerlsAssistant.add_command(getids)
PerlsAssistant.add_command(helpme)
PerlsAssistant.add_command(signup)
PerlsAssistant.add_command(ping)

## Add Commands to bot END ##
## Delete in emergency ##

## DO NOT SHARE ##
PerlsAssistant.run('MTA5ODg2MDg0NTQyMjg4NjkzMg.GGMh8h.qDvKf1cb9RROxHeflGqUNn2tc_ZCvmWnOqAqU4')

## DO NOT SHARE ##
