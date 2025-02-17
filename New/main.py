# Complex Tourney Discord Bot #
# Version one 
# Do not distribute


## Imports ##
import discord
from discord.ext import commands, tasks
import os
import platform
import random
import csv
import asyncio
import requests
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import yt_dlp as youtube_dl
import mcstatus
import logging

# Load environment variables from .env file
load_dotenv()
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
## Imports END ##

# Function to clear the screen based on the operating system
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
clear_screen()


## Discord Bot Intents ##
intents = discord.Intents.default()

intents.message_content = True ## Sets Permissions for discord, ie intent to see write and manage the server

PerlsAssistant = commands.Bot(command_prefix='$', intents=intents) ## Initialise Bot (Bot in variable names is PerlsAssistant)

responseList = open("Discord Responses", "a")
last_message = None

## WHEN BOT HAS STARTED ##
@PerlsAssistant.event # event is onready ie when bot starts
async def on_ready():
    productionVersion = 1.2  # Define the production version
    developmentVersion = 1.4  # Define the development version
    update_status.start()
    player_ping_task.start()
    await PerlsAssistant.tree.sync()
    print("Everything's all ready to go~")
    print(""">> Everything's all ready to go :)""")
    os.system('cls') # clear screen
    current_dateTime = datetime.now()
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
    print("\033[0;32m@PerlsLog \033[0;37m- \033[1;30m Listening for commands!\n")
    print("Hello Pelican!")
    print(f"Channel ID is {os.getenv('STATUS_CHANNEL_ID')}")
    players = getPlayersPing()
    print(players)
    
## SHITPOST ##
@commands.command(aliases=['ShitPost', 'Shitpost', 'SHITPOST', 'shitPost'])
async def shitpost(ctx):
    perlsShitPostLibrary = [goblinmanString,
                            whatdidyousaytomeString,
                            gotchaString,ravenString,
                            hotubManString,
                            perlsMonitorString,
                            cornnFlaekString,
                            wikiShitpostingString,
                            investigationString,
                            gymbagString]
    selectedShitPost = random.choice(perlsShitPostLibrary)
    user = ctx.author
    channel = ctx.channel
    print(user,"[",channel," ] - Ran The Shitpost Command!") ## Add counter
    await ctx.send(selectedShitPost)
    


## HELP ##
@commands.command(aliases=['HelpMe', 'Helpme', 'HELPME', 'Help'])
async def helpme(ctx):
    productionVersion = 1.1
    ## remove ()'s when finished
    ## Rizz may need to be added
    await ctx.send(f"""
    __**Help Desk**__
    **Try:**
    
    $playerPing

    **~-We hope you enjoy our commands!-~**
    <:pengu:1100294359355760650>
    --------------------------------------
    Version: {productionVersion}
    --------------------------------------
    PLEASE BE AWARE THIS IS A BETA BOT
    --------------------------------------
    """)
    user = ctx.author
    channel = ctx.channel
    print(user,"[",channel," ] - Ran The Help Command!") ## Add counter
## HELP END ##

@PerlsAssistant.tree.command(name="ping", description="Check the bot's latency.")
async def ping(interaction: discord.Interaction):
    latency = round(PerlsAssistant.latency * 1000)
    await interaction.response.send_message(f"Pong! `{latency}ms` at <t:{int(datetime.now().timestamp())}>")


@tasks.loop(minutes=1)
async def update_status():
    print("Updating Presence")
    server_ip = os.getenv("MINECRAFT_STATUS_GET_SERVER_IP") # server_ip = "milkmgn.ampere.oci.milkmgn.online" 
    server_port = os.getenv("MINECRAFT_STATUS_GET_SERVER_PORT") # server_port = "25570" 
    server = mcstatus.JavaServer.lookup(f"{server_ip}:{server_port}")
    print(server_ip, server_port)
    status = server.status()
    player_count = status.players.online
    max_players = status.players.max
    await PerlsAssistant.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{player_count}/{max_players} players online"))
    print(f"Updated Presence: {player_count}/{max_players} players online")


playerPing_minutes=int(os.getenv("PLAYER_PING_MINUTES"))  # Get the interval from the environment variable
@tasks.loop(minutes=playerPing_minutes)
async def player_ping_task():
    # Retrieve the channel ID from the environment variable.
    discordChannel = os.getenv("STATUS_CHANNEL_ID")
    if not discordChannel:
        print("STATUS_CHANNEL_ID environment variable is not set.")
        return

    print(f"Channel ID from env: {discordChannel}")
    try:
        channel = PerlsAssistant.get_channel(int(discordChannel))
    except Exception as e:
        print(f"Error converting channel ID: {e}")
        return

    if channel is None:
        print("Channel not found. Please check the channel ID.")
        return

    # Delete (purge) all messages in the channel.
    try:
        # Adjust the limit as needed. Note: Only messages younger than 14 days can be bulk deleted.
        deleted = await channel.purge(limit=1000)
        print(f"Deleted {len(deleted)} messages.")
    except Exception as e:
        print(f"Error purging messages: {e}")

    # Retrieve players and send the new status update.
    players = getPlayersPing()
    if not players:
        await channel.send("No players found in the database.")
        return

    embeds = []
    for player in players:
        name = player.get("Name", "Unknown")
        ping = player.get("Ping", "N/A")
        head_url = player.get("HeadURL", "")
        
        # Create an embed for each player.
        embed = discord.Embed(
            title=f"Player: `{name}`",
            description=f"Ping: `{ping}ms`",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=head_url)  # Set the player's head as the thumbnail
        embeds.append(embed)
    
    # Send all embeds in one message (Discord currently allows up to 10 embeds per message)
    await channel.send(embeds=embeds)
    
def get_minecraft_head(username):
    """Fetch the player's head texture URL using Minotar."""
    return f"https://minotar.net/avatar/{username}/32.png"  # 64x64 head image


# Function to fetch player pings from MongoDB
def getPlayersPing():
    MONGO_URI = os.getenv("MONGO")  # Get from .env file or set manually
    client = MongoClient(MONGO_URI)
    db = client["Mod"]
    collection = db["PlayerPing"]
    players_list = []
    print(players_list)
    for doc in collection.find({}, {"_id": 0, "Name": 1, "Ping": 1}):
        username = doc.get("Name")
        head_url = get_minecraft_head(username)  # Fetch head dynamically
        doc["HeadURL"] = head_url if head_url else "No head found"
        players_list.append(doc)
    return players_list

# Discord command to display player pings with heads
@PerlsAssistant.command(name="playerping")
async def player_ping(ctx):
    print(ctx.user,"[",ctx.channel,"] - Ran The playerping Command!") ## Add counter
    players = getPlayersPing()
    if not players:
        await ctx.send("No Players Online")
        return

    embeds = []
    for player in players:
        name = player.get("Name", "Unknown")
        ping = player.get("Ping", "N/A")
        head_url = player.get("HeadURL", "")
        
        # Create an embed for each player.
        embed = discord.Embed(
            title=f"Player: `{name}`",
            description=f"Ping: `{ping}ms`",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=head_url)  # Set the player's head as the thumbnail
        embeds.append(embed)
    
    # Discord now supports sending multiple embeds in one message.
    await ctx.send(embeds=embeds)


intents = PerlsAssistant.intents.default()
intents.messages = True
intents.voice_states = True

is_playing = False
music_queue = []
envCookieFile = os.getenv("COOKIE_FILE")
YDL_OPTIONS = {
    'cookiefile': envCookieFile,
    'format': 'bestaudio/best',
    'noplaylist': False,  # Allow playlists
    'nocheckcertificate': True,
    'ignoreerrors': True,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # Bind to IPv4 since IPv6 addresses cause issues sometimes
}
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}
vc = None

def search_yt(query):
    """Searches YouTube and returns the best audio URL or a list of URLs if it's a playlist"""
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            if 'entries' in info:
                # Playlist
                print(f"Found playlist with {len(info['entries'])} entries.")
                return [{'source': entry['url'], 'title': entry['title']} for entry in info['entries']]
            else:
                # Single video
                print(f"Found single video: {info['title']}")
                return [{'source': info['url'], 'title': info['title']}]
        except Exception as e:
            print(f"Error: {e}")
            return None

async def play_next():
    """Plays the next song in the queue"""
    global is_playing, vc

    if len(music_queue) > 0:
        is_playing = True
        song = music_queue.pop(0)
        print(f"Playing next song: {song['title']}")

        if vc is None or not vc.is_connected():
            vc = await song['voice_channel'].connect()

        vc.play(discord.FFmpegPCMAudio(song['source'], **FFMPEG_OPTIONS), 
                after=lambda e: asyncio.run_coroutine_threadsafe(play_next(), PerlsAssistant.loop))
        
        await song['ctx'].send(f"🎵 Now playing: **{song['title']}**")
    else:
        is_playing = False
        print("No more songs in the queue.")

@PerlsAssistant.command(name="play", help="Plays a selected song or playlist from YouTube")
async def play(ctx, *, query="Never Gonna Give You Up"):
    global is_playing, vc

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("❌ You must be in a voice channel to play music!")
        return

    songs = search_yt(query)
    if songs is None:
        await ctx.send("❌ Could not find the song. Try another search.")
        return

    for song in songs:
        song['ctx'] = ctx
        song['voice_channel'] = ctx.author.voice.channel
        music_queue.append(song)
        await ctx.send(f"✅ **{song['title']}** added to the queue.")
        print(f"Added to queue: {song['title']}")

    if not is_playing:
        await play_next()

@PerlsAssistant.command(name="pause", help="Pauses the current song")
async def pause(ctx):
    if vc and vc.is_playing():
        vc.pause()
        await ctx.send("⏸️ Music paused.")

@PerlsAssistant.command(name="resume", help="Resumes the current song")
async def resume(ctx):
    if vc and vc.is_paused():
        vc.resume()
        await ctx.send("▶️ Music resumed.")

@PerlsAssistant.command(name="skip", help="Skips the current song")
async def skip(ctx):
    global vc
    if vc and vc.is_playing():
        vc.stop()
        await play_next()
        await ctx.send("⏭️ Song skipped.")

@PerlsAssistant.command(aliases=['Stop','Leave','leave'], help="Stops music and clears the queue")
async def stop(ctx):
    global vc, music_queue, is_playing

    if vc and vc.is_connected():
        await vc.disconnect()
    music_queue.clear()
    is_playing = False
    vc = None
    await ctx.send("⏹️ Music stopped and queue cleared.")

@PerlsAssistant.command(name="queue", help="Displays the current music queue")
async def queue(ctx):
    if len(music_queue) == 0:
        await ctx.send("The queue is empty.")
    else:
        queue_list = "\n".join([f"{i+1}. {song['title']}"] for i, song in enumerate(music_queue))
        await ctx.send(f"Current queue:\n{queue_list}")

@PerlsAssistant.command(name="loop", help="Loops the current song")
async def loop(ctx):
    global vc
    if vc and vc.is_playing():
        vc.stop()
        music_queue.insert(0, music_queue[0])
        await play_next()
        await ctx.send("🔁 Song looped.")

PerlsAssistant.add_command(shitpost)
PerlsAssistant.add_command(helpme)


## TERRA ADD FUN COMMANDS HERE! ##
if __name__ == '__main__':

    print("Starting")



## DO NOT SHARE ##
TOKEN = os.getenv("DISCORD_TOKEN")
PerlsAssistant.run(TOKEN, log_handler=handler, root_logger=True)

## DO NOT SHARE ##
