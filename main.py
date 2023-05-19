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
import csv
from array import *

## Imports END ##
os.system('cls')
intents = discord.Intents.default()

intents.message_content = True ## Sets Permissions for discord, ie intent to see write and manage the server

PerlsAssistant = commands.Bot(command_prefix='^', intents=intents) ## Initialise Bot (Bot in variable names is PerlsAssistant)

responseList = open("Discord Responses", "a")


## READ WRITE CSV FUNCTIONALITY ##
players = []
lb = []
    
with open('data.csv',mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            i = 0
            while i != len(row):
                i = i + 1
                playerNum = row[3]
                IGN = row[0]
                DISCT = row[1]
                TZONE = row[2]
                WINS = row[4]
                LOSSES = row[5]
                TWINS = row[6]
                TLOSSES = row[7]
                LBPLACE = row[8]
                
                line_count += 1
            players.insert(i,[IGN,DISCT,TZONE,playerNum,WINS,LOSSES,TLOSSES,TWINS,LBPLACE])
            lb.insert(i,[IGN,WINS,LBPLACE])
    print(f'Processed {line_count} lines.')
   

## Come back to and ride a cactus. - Terra
"""

with open('lb.csv', mode='w') as lb_file:
    perlsWriter = csv.writer(lb_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    i = 0
    if i == 0:
        ineg = 0

    else:
      ineg = i - 1
    while i != len(lb):
      firstIndex = lb[ineg,[1,2,3]]
      secondIndex = lb[i,[1,2,3]]
      if secondIndex[2] < firstIndex[2]:
          pass
      else:
        lb[i,[3]].append([i,[3]] - 1)
        lb[ineg,[3]].append([ineg,[3] + 1])

        
          #if 
      string = IGN + WINS + LBPLACE
      perlsWriter.writerow(string)
      i = i + 1
    
    
    """
    

 





## END READ WRITE CSV FUNCTIONALITY ##

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
                                                                                                                                     
                    Production Version: \033[1;32m""",productionVersion,"\033[0m| Development Version: \033[1;32m",developmentVersion,"\033[0m| Bot Started On:",current_dateTime," \n")
    Client(intents=intents)
    print(f'\033[0;32m@on_Ready \033[0;37m- \033[1;30mProcessed {line_count / 9} players.\033[0m')
    print("\033[0;32m@PerlsLog \033[0;37m- \033[1;30m Listning for commands!\n")
    print(lb)
    
## SHITPOST ##
@commands.command(aliases=['ShitPost', 'Shitpost', 'SHITPOST', 'shitPost'])
async def shitpost(ctx):
    perlsShitPostLibrary = [goblinmanString,
                            whatdidyousaytomeString,
                            gotchaString,ravenString,
                            hotubManString,
                            perlsMonitorString,
                            cornnFlaekString,
                            wikiShitpostingString]
    selectedShitPost = random.choice(perlsShitPostLibrary)
    user = ctx.author
    channel = ctx.channel
    print(user,"[",channel," ] - Ran The Shitpost Command!") ## Add counter
    await ctx.send(selectedShitPost)
    
## SHITPOST END ##



  

## ^stats ##
@commands.command(aliases=['STATS','Stats'])
async def stats(ctx):
  rand = random.randint(1,100)
  user = ctx.author
  channel = ctx.channel
  await ctx.send(f"""
  **List of stats::**
  **User:** {user}
  **Discord ID:** {ctx.author.id}
  **All-time Wins:** {row[6]}
  **All-time Losses:** {row[7]}
  **Cool-rating:** {rand}%
  -__Current Tournament__-
  **Wins:** {row[4]}
  **Losses:** {row[5]}
  **Your Leaderboard Position:**
  
  """)

  print(user,"[",channel," ] - Ran the stats Command!") ## Add counter



## GET IDS ##

@commands.command(aliases=['GETIDS','GetIDS','GetIds','GetIDs','getIDs', 'getId', 'getid'])
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
async def sendAs_error(error, ctx):
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
    
    **^getids** -- 
    **^shitpost** -- 
    **^signup** -- (In development)
    **^tourneystats** [username] --  displays wins losses and kd's (In development)
    **^fighttime** [username] -- displays the players next fight time and info about the fight (In development)
    **^ping** -- *Shows bot latency *
    **^nootnoot** -- *Noot NOOT! *

    **~-We hope you enjoy our commands!-~**
    <:pengu:1100294359355760650>
    --------------------------------------
    Version: {productionVersion}
    --------------------------------------
    PLEASE BE AWARE MOST OF THESE FEATURES HAVE NOT YET BEEN COMPLETED.
    THIS IS A BETA BOT
    --------------------------------------
    """)
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
async def signup(ctx):
  # if person who sends the message is the same person whom wrote the message
      await ctx.send("Sliiiiding into those DMs.") # once done, sends a DM with this message left in the channel.
      channel = ctx.channel
      user = ctx.author # gets the user's dm
      def check(check):
          return check.author == ctx.author and check.channel == ctx.channel
        ## First DM message.

      await user.send("""**Hello!**
      _-Blah Blah Blah-_
      Please answer a few questions and we will sort out the rest.
      **Question 1:**
      *What is your In Game Name?*

      """) ## First question ##

        
      msg = await PerlsAssistant.wait_for("message", check=check, timeout=30)
      await ctx.send(f"Your name is {msg.content}")
      IGN = msg.content  
      print(f"{msg.author} - Input -->> {msg.content}. For the question 'What is your name?'")
        
      await ctx.send("""
      Thank you for this!
      **Question 2:**
      *What is your discord tag?*
        
      """) ## Second question ##
        
      msg2 = await PerlsAssistant.wait_for("message", check=check ,timeout=30)
      DTAG = msg2.content
      await ctx.send(f"You're @{msg2.content}")
        
      
      print(f"{msg.author} - Input -->> {msg.content}. For the question 'Whats your discord?'")
      ## Writing to the .txt file: responseList

      TZONE = await PerlsAssistant.wait_for("message", check=check, timeout=30)
      DTAG = msg2.content
      await ctx.send(f"You're @{msg2.content}")
        
      
      print(f"{msg.author} - Input -->> {msg.content}. For the question 'Whats your discord?'")
      ## Writing to the .txt file: responseList
      
      await ctx.send(f"""
      Thank you so much for entering into the Complex Events!
      We hope to see a {msg.content} there!
      """) ## Ending of questions ##
      i = 0
      print(f"[^signup] - Signups this session {i}")
      print(user,"[",channel," ] - Ran The signup Command!") ## Add counter
      #perlsWriter.writerow([IGN,DTAG,TZONE])

  ## Signup DM Chain END ##
        
@commands.command()
async def getPlayers(ctx):
  await ctx.send(f'<:pengu:1100294359355760650>')
  user = ctx.author
  channel = ctx.channel
  print(user,"[",channel," ] - Ran the NootNoot Command!") ## Add counter






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
async def suggest(ctx,suggest):
  suggest = ctx.message ## reading the message sent
  channel = ctx.channel
  ctx.channel.send(suggest) ## Sending the player's suggestion
  await ctx.send('FUCKIN CRIKEY CUNT ITS WORKING MATE GDAY') ## after suggestion is read, send this
  user = ctx.author ## for the below
  print(user,"[",channel," ] - Ran the NootNoot Command!")
   ## Add counter

## Terra's testing command START ##
@commands.command(alliases=["thisIsKillingMe", "THISISKILLINGME", "FORFUCKSAKE"])
async def thisiskillingme(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.send('Whats your name?')
    msg = await PerlsAssistant.wait_for("message", check=check, timeout=30)
    await ctx.send(f"Your name is {msg.content}")

    print(f"{msg.author} - Input -->> {msg.content}. For the question 'What is your name?'")



   # Create a list of text ["Question 1","Question 2","Question 3"]
   # if not in message guild aka in dms
   # i = 0
   # PerlsAssistant.send(list[i])
  #  i += 1 ???
    #if i == 3:
        # EXIT TEXT 



   
## Terra's testing command END ##



## Add Commands to bot ##

PerlsAssistant.add_command(shitpost)
PerlsAssistant.add_command(getids)
PerlsAssistant.add_command(helpme)
PerlsAssistant.add_command(signup)
PerlsAssistant.add_command(ping)
PerlsAssistant.add_command(nootnoot)
PerlsAssistant.add_command(sendAs)
PerlsAssistant.add_command(suggest)
PerlsAssistant.add_command(thisiskillingme)
PerlsAssistant.add_command(stats)

## TERRA ADD FUN COMMANDS HERE! ##



## Add Commands to bot END ##
## Delete in emergency ##

## DO NOT SHARE ##
PerlsAssistant.run("MTA5ODg2MDg0NTQyMjg4NjkzMg.GGMh8h.qDvKf1cb9RROxHeflGqUNn2tc_ZCvmWnOqAqU4")

## DO NOT SHARE ##
