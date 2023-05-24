# Complex Tourney Discord Bot #
# Version one 
# Do not distribute


## Imports ##
import random
import time
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
import data.manager as manager

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
    rows=len(players) #finding the max number of rows in the matrix, in this case 3
    columns=len(players[0])


@commands.command(aliases=['STATS','Stats'])
async def stats(ctx, message):
  rand = random.randint(1,100)
  channel = ctx.channel
  x = line_count / 9.5
  flag = False
  for i in range(rows):
      for j in range(columns):
        if players[i][j]== message:
          ## Pull the variables from the index 
          ign = players[i][j]
          wins = players[i][4]
          losses = players[i][5]
          Aloss = players[i][7]
          Awins = players[i][6]
          standing = players[i][8]
          flag = True
          break
  if flag == False:
    print ("Not found!")
    await ctx.send("ERROR! -- User is not found. Try ^signup")
  pass
  embedVar = discord.Embed(title="<:panda_flex:652189894055165952> Leaderboard <:panda_flex:652189894055165952>", description="complex pvp tourney", color=0x00ff00)
  embedVar.add_field(name="Leaderboard", value=f"""
   **<:pengu:1100294359355760650> __**List of stats**__ <:pengu:1100294359355760650>**

  **User:** {message}
  **IGN:** {ign}
  **Discord ID:** {ctx.author.id}
  <:fire:1109406181325283339> **Cool-rating:** {rand}%
  
  **-__Current Tournament__-**
  
  <:regional_indicator_w:1109404805450965042> **Wins:** {wins} 
  <:regional_indicator_l:1109404918521024512> **Losses:** {losses} 
  <:trophy:1109405254199549962> **Your Leaderboard Position:** {standing}!

  -__All Time__-
  <:champagne_glass:1109405418423336993> **All-time Wins:** {Awins}
  <:clown:1109405802642550835> **All-time Losses:** {Aloss}
  

 """, inline=False)
  await ctx(embed=embedVar)
  

  print(message,"[",channel," ] - Ran the stats Command!") ## Add counter

@commands.command(aliases=['LIVE','Live'])
async def live(ctx):
    lb.sort() 
    firstIGN = lb[0][0]
    firstLB = lb[0][2]

    secondIGN = lb[1][0]
    secondLB = lb[1][2]

    thirdIGN = lb[2][0]
    thirdLB = lb[2][2]

    fourthIGN = lb[3][0]
    fourthLB = lb[3][2]

    fifthIGN = lb[4][0]
    fifthLB = lb[4][2]

    sixthIGN = lb[5][0]
    sixthLB = lb[5][2]

    seventhIGN = lb[6][0]
    seventhLB = lb[6][2]

    eighthIGN = lb[7][0]
    eighthLB = lb[7][2]

    ninethIGN = lb[8][0]
    ninethLB = lb[8][2]

    tenthIGN = lb[9][0]
    tenthLB = lb[9][2]

  
    await ctx.send(f'''
      __**The Top 10 are as follows:**__
      **{firstIGN}** is **{firstLB}**st!
      **{secondIGN}** is **{secondLB}**nd!
      **{thirdIGN}** is **{thirdLB}**rd!
      **{fourthIGN}** is **{fourthLB}**th!
      **{fifthIGN}** is **{fifthLB}**th!
      **{sixthIGN}** is **{sixthLB}**th!
      **{seventhIGN}** is **{seventhLB}**th!
      **{eighthIGN}** is **{eighthLB}**th!
      **{ninethIGN}** is **{ninethLB}**th!
      **{tenthIGN}** is **{tenthLB}**th!

    ^stats (*your ign here*) **to see your standing**
      ''')


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
    print(f'\033[0;32m@on_Ready \033[0;37m- \033[1;30mProcessed {rows} players.\033[0m')
    print("\033[0;32m@PerlsLog \033[0;37m- \033[1;30m Listening for commands!\n")
    print("Current LB Players: ")
    print("IGN, Wins, LBPLACE")
    i = 0
    while i != 10:
        print(lb[i])
        i = i + 1
    if i == 10:
        print("\n>> Await <<\n")
        i = 0
        return i

    
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


## ADDGROUP [Child of manager.py] ##


@commands.command(aliases=['addgroup','addGroup','Addgroup'])
async def AddGroup(ctx,IGN,Group):
   print(f'\033[0;32mManager@AddGroup \033[0;37m- \033[1;30mAdded {IGN} to the tourney in group {Group}!\033[0m')
   await ctx.send(f'```Manager@AddGroup - Added {IGN} to the tourney in group {Group}!```')

   await manager.AssignGroup(ctx,IGN=IGN,Group=Group)

## Add Player
@commands.command(aliases=['addplayer','addPlayer','Addplayer'])
async def AddPlayer(ctx, IGN):
    i = len(players) + 1
    players[i].insert([IGN,IGN,'NILL',i,0,0,0,0,i,'NULL'])
    print(f'\033[0;32mManager@AddPlayer \033[0;37m- \033[1;30mAdded {IGN} to the tourney!\033[0m')
    pass
  
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
PerlsAssistant.add_command(live)
PerlsAssistant.add_command(AddGroup)
PerlsAssistant.add_command(AddPlayer)

## TERRA ADD FUN COMMANDS HERE! ##
if __name__ == '__main__':
    live(ctx)
    print("Starting")


## Add Commands to bot END ##
## Delete in emergency ##

## DO NOT SHARE ##
PerlsAssistant.run("MTA5ODg2MDg0NTQyMjg4NjkzMg.GGMh8h.qDvKf1cb9RROxHeflGqUNn2tc_ZCvmWnOqAqU4")

## DO NOT SHARE ##
