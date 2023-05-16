# Complex Tourney Discord Bot #
# Version one 
# Do not distribute


## Imports ##
import random
import discord
from discord.ext import commands
import os
import discord
from flask import ctx
from discord import Client, Member
import datetime
from libs.perlsShitPostLibrary import *
from libs.version import *

## Imports END ##

intents = discord.Intents.default()

intents.message_content = True ## Sets Permissions for discord, ie intent to see write and manage the server

PerlsAssistant = commands.Bot(command_prefix='^', intents=intents) ## Initialise Bot (Bot in variable names is PerlsAssistant)

"""
@PerlsAssistant.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  #channel = discord.TextChannel()
  #print(f'{username}: {user_message} ({channel})')
  seconds = 5 # The seconds ago to check messages.

  now = datetime.datetime.now()

  messages = 0
## ANTI SPAM ##
#DONT WORK #
  #async for message in channel.history():
      #if message.author == PerlsAssistant.user:
         # message_time = message.created_at.timestamp()
          #if message_time > now - datetime.timedelta(seconds=seconds):
           #   messages += 1

# PERL NEEDS TO FIX THIS #

      # WORKS #
          #flaggedMessages = "FUCK"
          #if user_message == flaggedMessages:
           # await message.delete()
           # return
    # DONT TOUCH THIS PLEASE <3 Perl #
 ## ANTI SPAM ##
 
"""
## WHEN BOT HAS STARTED ##
@PerlsAssistant.event # event is onready ie when bot starts
async def on_ready():
    print("Everything's all ready to go~")
    print(""">> Everything's all ready to go :)""")
    os.system('cls') # clear screen
    
    print("\033[1;30m")
    print("""
    
    
$$$$$$$\                      $$\                  $$$$$$\                      $$\             $$\                          $$\     
$$  __$$\                     $$ |                $$  __$$\                     \__|            $$ |                         $$ |    
$$ |  $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\       $$ /  $$ | $$$$$$$\  $$$$$$$\ $$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$$$$$$\ $$$$$$\   
$$$$$$$  |$$  __$$\ $$  __$$\ $$ |$$  _____|      $$$$$$$$ |$$  _____|$$  _____|$$ |$$  _____|\_$$  _|   \____$$\ $$  __$$\\_$$  _|  
$$  ____/ $$$$$$$$ |$$ |  \__|$$ |\$$$$$$\        $$  __$$ |\$$$$$$\  \$$$$$$\  $$ |\$$$$$$\    $$ |     $$$$$$$ |$$ |  $$ | $$ |    
$$ |      $$   ____|$$ |      $$ | \____$$\       $$ |  $$ | \____$$\  \____$$\ $$ | \____$$\   $$ |$$\ $$  __$$ |$$ |  $$ | $$ |$$\ 
$$ |      \$$$$$$$\ $$ |      $$ |$$$$$$$  |      $$ |  $$ |$$$$$$$  |$$$$$$$  |$$ |$$$$$$$  |  \$$$$  |\$$$$$$$ |$$ |  $$ | \$$$$  |
\__|       \_______|\__|      \__|\_______/       \__|  \__|\_______/ \_______/ \__|\_______/    \____/  \_______|\__|  \__|  \____/ 
                                                                                                                                     
                                     Version {productionVersion}                                                                                               
                                                                                                                                     
""")
    Client(intents=intents)
    

@commands.command()
async def test(ctx):
    await ctx.send("test") 

## SHITPOST ##
@commands.command()
async def shitpost(ctx):
    perlsShitPostLibrary = [goblinmanString,whatdidyousaytomeString,gotchaString]
    selectedShitPost = random.choice(perlsShitPostLibrary)
    user = ctx.author
    channel = ctx.channel
    print(user,"[",channel," ] - Ran The Shitpost Command!") ## Add counter
    await ctx.send(selectedShitPost)
## SHITPOST END ##

## GET IDS ##
@commands.command()
async def getids(ctx):
    await ctx.send(f"```ID >> {ctx.author.id} << Please use this in your signup!```")
    user = ctx.author
    channel = ctx.channel
    print(user,"[",channel," ] - Ran The GetID's Command!") ## Add counter

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
    ^ping -- Shows bot latency (Working)
    
    PLEASE BE AWARE MOST OF THESE FEATURES HAVE NOT YET BEEN COMPLETED.
    THIS IS A BETA BOT```""")
    user = ctx.author
    channel = ctx.channel
    print(user,"[",channel," ] - Ran The Help Command!") ## Add counter
## HELP END ##

## PING ##
@commands.command()
async def ping(ctx):
     await ctx.send(f"```Pong! My ping is: {round (PerlsAssistant.latency * 1000)} ms```")
     user = ctx.author
     channel = ctx.channel
     print(user,"[",channel," ] - Ran The ping Command!") ## Add counter
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
  user = ctx.author
  channel = ctx.channel
  print(user,"[",channel," ] - Ran The signup Command!") ## Add counter

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
