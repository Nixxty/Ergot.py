#DO NOT RUN THIS FILE, INSTEAD RUN MAIN.PY SO EVERY NECESSARY PYTHON FILE RUNS WITH THE BOT.

import os, discord, GPUtil, psutil, datetime, random, string, json
from discord.ext import commands
from desktopmagic.screengrab_win32 import (getScreenAsImage)

### intents and user setting.
intents = discord.Intents.all()
user = os.environ.get('USERNAME')
###

### UID.JSON FILE READING/SPLITTING AND ASSIGNMENT
dir_p = os.path.dirname(os.path.realpath(__file__))
dir_p = os.path.join(dir_p, 'UidData.json')
with open(dir_p, 'r+') as f:
    data = json.load(f)
    f.close()
    for i in data['permissions']:
        guild_id = i['guild_id']
        channel_id = i['channel_id']
        token_id = i['token_id']
        token_ob = i['token_ob']
if token_ob == True:
    print("Channel ID: " + channel_id + "\nBot_Token: obscured, check json file if you wish to see it.")
else:
    print("Channel ID: " + channel_id + "\nBot_Token: "+token_id)
###

### SAFETY
mid = 'undefined'
if guild_id==mid or channel_id==mid or token_id==mid or token_ob==mid:
    input("RUN DATACHOV OR ELSE THIS BOT WILL NOT RUN.")
    exit()


### bot start
client = commands.Bot(command_prefix = ";;", intents=intents)
# loading all cogs
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")

@client.event #sets status
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ACTIVE'))
    print("client started")

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

"""
@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
"""


@client.command()
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()

async def ss(ctx):
      user = os.environ.get('USERNAME')
      await ctx.send("Screenshotting " + user + "'s main monitor.")
      N = 7
      res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
      image = getScreenAsImage()
      full = "tempUser" + user + str(res) + ".png"
      image.save(full)
      if os.path.exists(full):
         await ctx.send(file=discord.File("D:\\Ergotism\\" + full))
      else:
         print("Cannot find " + full + " :(")
         await ctx.send("Cannot find " + full + " :(")
      print ("removing D:Ergotism\\" + full)
      if os.path.exists(full):
         os.remove(full)
         await ctx.send("removed screenshot")
      else:
         print("cannot find " + full + " :(")
         await ctx.send("cannot find " + full + " :(")

@ss.error
async def ss_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(error)


@client.command()
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()

async def sendfile(ctx):
    await ctx.send("NIL")

@sendfile.error
async def ss_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(error)

@client.command()
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

@stats.error
async def ss_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(error)

@client.command()
@is_in_chan(int(channel_id))
@is_in_guild(int(guild_id))
@commands.is_owner()
async def shutoff(ctx):
    await ctx.send("Continue with PC shutoff? (Y/N)")

    response = await client.wait_for("message")
    if response.content == 'Y':
        await ctx.send("Proceeding: SHUTTING DOWN PC IN 10 SECONDS.")
        await ss(ctx)
        os.system("C:\Windows\System32\shutdown.exe -s -t 10")
    elif response.content == 'N':
        await ctx.send("Cancelling shutdown.")
@stats.error
async def ss_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(error)
    

client.run(token_id)
