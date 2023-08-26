import os, discord, GPUtil, psutil, datetime, random, string, subprocess, asyncio
from discord.ext import commands
from desktopmagic.screengrab_win32 import (getScreenAsImage)

###
intents = discord.Intents.all()
user = os.environ.get('USERNAME')
###

client = commands.Bot(command_prefix = ";;", intents=intents)
# loading all cogs
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Logging'))
    print("client started")



    def process_exists(process_name):
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        output = subprocess.check_output(call).decode()
        last_line = output.strip().split('\r\n')[-1]

        return last_line.lower().startswith(process_name.lower())
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

@client.command()
async def sendfile(ctx):
    await ctx.send("NIL")

@client.command()
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

@client.command()
async def shutoff(ctx):
    await ctx.send("Continue with PC shutoff? (Y/N)")

    response = await client.wait_for("message")
    if response.content == 'Y':
        await ctx.send("Proceeding: SHUTTING DOWN PC IN 10 SECONDS.")
        await ss(ctx)
        os.system("C:\Windows\System32\shutdown.exe -s -t 10")
    elif response.content == 'N':
        await ctx.send("Cancelling shutdown.")
    

client.run("undefined")
