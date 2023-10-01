#DO NOT RUN THIS FILE, INSTEAD RUN MAIN.PY SO EVERY NECESSARY PYTHON FILE RUNS WITH THE BOT.

import os, discord, GPUtil, psutil, datetime, random, string, json, wmi, asyncio
from discord.ext import commands
from .exts.cmds import clearterminal
from desktopmagic.screengrab_win32 import (getScreenAsImage)

### intents and user setting.
intents = discord.Intents.all()
user = os.environ.get('USERNAME')
###

### UID.JSON FILE READING/SPLITTING AND ASSIGNMENT
directory_path = os.path.dirname(os.path.realpath(__file__))
directory_path = os.path.join(directory_path, 'UidData.json')
try:
    with open(directory_path, 'r+') as file:   
        jslist = json.load(file)
        file.close()
        for item in jslist['permissions']:
            guild_id = item['guild_id']
            channel_id = item['channel_id']
            token_id = item['token_id']
            token_ob = item['token_ob']
except FileNotFoundError:
    input('UidData.json was not found! try running Data checker/overwriter (option 2) before running bot in ergot.py!')
    exit()

if token_ob == True:
    print("Channel ID: " + channel_id + "\nBot_Token: obscured, check json file if you wish to see it.")
else:
    print("Channel ID: " + channel_id + "\nBot_Token: "+token_id)
###

### SAFETY
NoJsonData = 'undefined'
if guild_id==NoJsonData or channel_id==NoJsonData or token_id==NoJsonData or token_ob==NoJsonData:
    input("RUN DATACHOV OR ELSE THIS BOT WILL NOT RUN.")
    exit()

### IMPORTANT VARIABLES/PARAMETERS/LISTS/DICTIONARIES
directory_path = os.path.dirname(os.path.realpath(__file__))
### GENERAL FUNCTIONS
###




### bot start
client = commands.Bot(command_prefix = ";;", intents=intents, help_command=None)
# loading all cogs
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")

@client.event #sets status
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ACTIVE'))
    print("Bot started.")



###checks
def is_in_chan(chan_id): #function that checks if a command is ran in user set channel
    async def predicate(ctx):
        return ctx.channel and ctx.channel.id == chan_id
    return commands.check(predicate)

def is_in_guild(server_id): #function that does the same thing as chan but checks for guild instead
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == server_id
    return commands.check(predicate)
###

@client.command(name='help', description='lists all of ergots commands.')
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()

async def help(ctx):
    helptext = '```'
    for command in client.commands:
        helptext+=f'{command.name}  |  {command.description}\n'
    helptext+='```'
    await ctx.send(helptext)

@client.command(name='clearterm', description='clears the ergot terminal then takes a screenshot.')
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()


async def clearterm(ctx):
    await ctx.send("clearing terminal.")
    clearterminal(0,0)
    await ss(ctx, withprint=False)


@client.command(name='ss', description='screenshots your monitor(s) and sends the screenshot to the channel.')
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()

async def ss(ctx, withprint=True):
      user = os.environ.get('USERNAME')

      def withprinting(string):
          if withprint == True:
              print(string)
          else:
              return
          
      await ctx.send("Screenshotting " + user + "'s main monitor.")
      randomstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
      image = getScreenAsImage()
      FullPNGName = "tempUser" + user + str(randomstring) + ".png"
      FullDirectoryPathToPNG = os.path.join(directory_path, FullPNGName)

      withprinting(f"FullPNGName path to png | {FullDirectoryPathToPNG}")

      image.save(FullPNGName)

      if os.path.exists(FullPNGName):
         withprinting(f"found {FullPNGName}")
         await ctx.send(file=discord.File(FullPNGName))
      else:
         withprinting(f"Cannot find {FullPNGName} :(")
         await ctx.send("Cannot find " + FullPNGName + " :("+"\nfull path | "+FullDirectoryPathToPNG)
      withprinting(f"Removing file | {FullDirectoryPathToPNG}")

      if os.path.exists(FullPNGName):
         os.remove(FullPNGName)
         await ctx.send("removed screenshot")
      else:
         withprinting(f"Cannot find {FullPNGName} :(")
         await ctx.send("cannot find " + FullPNGName + " :(")

@client.command(name='getpns', description='gets all process names (pns for short) and outputs them.')
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()

async def getpns(ctx):
    await ctx.send("Grabbing processes..")
    remote = wmi.WMI()
    process_names_list = []
        
    for process in remote.Win32_Process():
        process_name = process.Name
        process_names_list.append(process_name)

    process_names_list = list(set(process_names_list))  # Use set to remove duplicates
    await ctx.send("```"+"\n".join(process_names_list)+"```")
    
@client.command(name='killproc', description='kills specified process NAME | ex: brave.exe')
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()

async def killproc(ctx):
    await ctx.send("input process name you wish to be terminated, type | " + '"CANCEL" to stop.')
    response = await client.wait_for('message')
    if response.content != 'CANCEL':
        await ctx.send(f"Proceeding | KILLING PROCESS: {response.content}")
        ProcessInput = ''.join(response.content.split())
        os.system("taskkill /f /im "+ ProcessInput)
        await ss(ctx,withprint=False)
    elif response.content == 'CANCEL':
        await ctx.send("Cancelling.")
        return

@client.command(name='stats', description='outputs your CPU, GPU, and RAM usage, aswell as pc runtime.')
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()

async def stats(ctx):
   gpu = GPUtil.getGPUs()[0]
   user = os.environ.get('USERNAME')
   print("monitoring CPU for 15 seconds")
   await ctx.send("Monitoring CPU for 15 seconds.")
   cpup = psutil.cpu_percent(15)
   ramm = psutil.virtual_memory()[2]
   ramu = psutil.virtual_memory()[3]/1000000000
   lsr = psutil.boot_time()
   pcr = datetime.datetime.fromtimestamp(lsr)

   print("CPU: " +str(cpup), 'RAM memory %\ used: ' +str(ramm), "RAM USED (GB): " + str(ramu), "PC Runtime/Last rebooted: " + str(pcr))

   
   embed = discord.Embed(title=user+"'s Stats", description='Shows the stats of the current users PC', color=discord.Color.random())
   embed.add_field(name="GPU TEMPS: ", value=str(gpu.temperature), inline=False)
   embed.add_field(name="CPU Usage: ", value=str(cpup), inline=False)
   embed.add_field(name="RAM mem used: ", value=str(ramm), inline=False)
   embed.add_field(name="RAM used (GB): ", value=str(ramu), inline=False)
   embed.add_field(name="PC Runtime/Last rebooted: ", value=str(pcr), inline=False)
   await ctx.send(embed=embed)


@client.command(name='shutoff', description='shuts off your PC within 10 seconds with confirmation ofc.')
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()
async def shutoff(ctx):
    await ctx.send("Continue with PC shutoff? (Y/N)")

    response = await client.wait_for('message')
    if response.content == 'Y':
        await ctx.send("Proceeding: SHUTTING DOWN PC IN 10 SECONDS.")
        await ss(ctx)
        os.system("C:\Windows\System32\shutdown.exe -s -t 10")
    elif response.content == 'N':
        await ctx.send("Cancelling shutdown.")
        return
    

client.run(token_id)
