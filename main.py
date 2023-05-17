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
from discord import Client, Emoji, Member
import datetime
from libs.perlsShitPostLibrary import *
from libs.version import *
from datetime import datetime
from discord.ext.commands import has_permissions, CheckFailure
## Imports END ##
os.system('cls')
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
    current_dateTime = datetime.now()
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
                                                                                                                                     
                    Production Version: """,productionVersion,"| Development Version: ",developmentVersion,"| Bot Started On: ",current_dateTime)
    Client(intents=intents)
    
## SHITPOST ##
@commands.command(aliases=['ShitPost', 'Shitpost', 'SHITPOST', 'shitPost'])
async def shitpost(ctx):
    perlsShitPostLibrary = [goblinmanString,
                            whatdidyousaytomeString,
                            gotchaString,ravenString,
                            hotubManString,
                            perlsMonitorString,
                            pickleTubString,
                            donkeyHard,
                            drinkingYesString]
    selectedShitPost = random.choice(perlsShitPostLibrary)
    user = ctx.author
    channel = ctx.channel
    print(user,"[",channel," ] - Ran The Shitpost Command!") ## Add counter
    await ctx.send(selectedShitPost)
## SHITPOST END ##

## GET IDS ##
@commands.command(aliases=['GETIDS','GetIDS','GetIds','GetIDs','getIDs'])
async def getids(ctx):
    await ctx.send(f"```Here is your Discord's ID >> {ctx.author.id} << Please use this in your signup!```")
    user = ctx.author
    channel = ctx.channel
    print(user,"[",channel," ] - Ran The GetID's Command!") ## Add counter



## GET IDS END ##

## SENDAS BOT ##

@commands.command(aliases=['SendAs','sendas'],pass_context=True)
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def sendAs(ctx, content):
        user = ctx.author
        channel = ctx.channel
        print(user,"[",channel," ] - Sent: ",content," with SendAs Command") ## Add counter
        await ctx.send(f"```{content}```")
    
@sendAs.error
async def mod_ban_error(error, ctx):
    if isinstance(error, CheckFailure):
        await PerlsAssistant.send_message(ctx.message.channel, "Looks like you don't have the perm.")
## SENDAS BOT END ##

## HELP ##
@commands.command(aliases=['HelpMe', 'Helpme', 'HELPME', 'Help'])
async def helpme(ctx):
    ## remove ()'s when finished
    ## Rizz may need to be added
    await ctx.send(f"""
    __**Help Desk**__
    **Try:**
    
    **^getids** --  (Working)
    **^shitpost** -- (Working)
    **^signup** -- (In development)
    **^tourneystats** -- [username] displays wins losses and kd's (In development)
    **^fighttime** -- [username] displays the players next fight time and info about the fight (In development)
    **^ping** -- Shows bot latency (Working)
    **^nootnoot** -- Noot NOOT! (Working)

    **~-We hope you enjoy our commands!-~**
    Version: {productionVersion}
    PLEASE BE AWARE MOST OF THESE FEATURES HAVE NOT YET BEEN COMPLETED.
    THIS IS A BETA BOT""")
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

@commands.command(aliases=['SignUp', 'Sign', 'SIGNUP', 'SIGNup'])
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

## Terra's NootNoot Command ##
@commands.command(aliases=['NootNoot','NOOTNOOT', 'Nootnoot'])
async def nootnoot(ctx):
  await ctx.send(f'<:pengu:1100294359355760650>')
  user = ctx.author
  channel = ctx.channel
  print(user,"[",channel," ] - Ran the NootNoot Command!") ## Add counter
## Terra's NootNoot Command END ##

## Terra's slut command START ##
@commands.command(aliases=['Suggest','SUGGEST', 'SUggest'])
async def suggest(ctx):
  suggest = ctx.message ## reading the message sent
  channel = ctx.get_channel(1108282222030639145) ## selecting the channel
  ctx.channel.send(suggest)
  await ctx.send('butt') ## after suggestion is read, send this
  user = ctx.author ## for the below
  
  print(user,"[",channel," ] - Ran the NootNoot Command!") ## Add counter
## Terra's slut command END ##


## Add Commands to bot ##

PerlsAssistant.add_command(shitpost)
PerlsAssistant.add_command(getids)
PerlsAssistant.add_command(helpme)
PerlsAssistant.add_command(signup)
PerlsAssistant.add_command(ping)
PerlsAssistant.add_command(nootnoot)
PerlsAssistant.add_command(sendAs)
PerlsAssistant.add_command(suggest)


## Add Commands to bot END ##
## Delete in emergency ##

## DO NOT SHARE ##
PerlsAssistant.run("MTA5ODg2MDg0NTQyMjg4NjkzMg.GGMh8h.qDvKf1cb9RROxHeflGqUNn2tc_ZCvmWnOqAqU4")

## DO NOT SHARE ##
