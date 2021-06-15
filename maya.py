# coding=utf8
#pip imports
import discord
from discord.ext import commands
import requests #For consuming APIs, like .neko
from PIL import Image, ImageOps #For the Kyou related commands
#oldM.py handles parsing data.json which is a huge JSON file of the messages in #lecture-hall
import oldM
#imagesAPI.py handles the .images related commands using requests
import imagesAPI
#standard imports
import random
import time

#Setting up bot's prefix
bot = commands.Bot(command_prefix=".", help_command=None)

# Declaring a command
@bot.command()
async def help(ctx):
    print(ctx.channel)
    embed = discord.Embed(title="Maya", url="https://lupppiter.xyz", description="Best girl", color=0xa0200e)
    embed.set_author(name="Help")
    embed.set_thumbnail(url="https://i.imgur.com/bNQWzHY.jpg")
    embed.add_field(name="roulette", value="Play Russian Roulette", inline=False)
    embed.add_field(name="roles", value="To get back your roles if you lost Russian Roulette", inline=False)
    embed.add_field(name="ball", value="Play 8Ball", inline=False)
    embed.add_field(name="old", value="Random old message from lecture-hall", inline=False)
    embed.add_field(name="kyoufyme", value="Get monochromed", inline=False)
    embed.add_field(name="kyoufyou", value="Monochrome a url", inline=False)
    embed.add_field(name="unkyou", value="Un-monochrome a url", inline=False)
    embed.add_field(name="neko", value="Random neko girl", inline=False)
    embed.add_field(name="quote", value="Random anime quote", inline=False)
    embed.add_field(name="sus", value="Get the sus% of someone", inline=False)
    await ctx.send(embed=embed)

# Sus, it needs a @user as an argument or any type of string tbh.
@bot.command()
async def sus(ctx, *, user):
    if str(ctx.channel.id) != "826966640100376587":
      r = random.randint(1, 100)
      susness = r / 1.17
      gifs = ""
      if susness < 10:
        gifs = "https://cdn.discordapp.com/attachments/822977852236234807/834453223544586250/image0.gif"
      elif susness > 10 and susness < 30:
        gifs = "https://cdn.discordapp.com/attachments/822977852236234807/834453187939139624/image0.gif"
      elif susness > 30 and susness < 50:
        gifs = "https://cdn.discordapp.com/attachments/822977852236234807/834453203743146094/image0.gif"
      elif susness > 50 and susness < 75:
        gifs = "https://cdn.discordapp.com/attachments/822977852236234807/834453250622619678/image0.gif"
      elif susness > 75:
        gifs = "https://cdn.discordapp.com/attachments/822977852236234807/834453155285565511/image0.gif"
      dumb = f"**{user}** is **{susness:.2f}**% sus"
      embed = discord.Embed(title="", description=dumb, color=0xa0200e)
      embed.set_image(url=gifs)
      await ctx.send(embed=embed)
    else:
      await ctx.reply("Use out-of-context plz")

#CTX = context (the message, channel, author, etchttps://discordpy.readthedocs.io/en/latest/index.html)
@bot.command()
async def old(ctx):
    #out-of context channel ID
    if str(ctx.channel.id) == "826966640100376587":
      myDict = oldM.randomMsg() #create a Dict from a random msg
      embed=discord.Embed(title=myDict["fecha"], url="https://luppiter.xyz", description=myDict["autor"], color=0xa0200e)
      embed.set_author(name="Random lecture-hall message")
      embed.set_thumbnail(url=myDict["pfp"])
      if myDict["imagen"] == True: #Checks if the random message obtained has an image or not
        embed.set_image(url=myDict["mensaje"])
      else:
        embed.add_field(name="Text", value=myDict["mensaje"], inline=False)
      await ctx.reply(embed=embed)
    else:
      await ctx.reply("Use out-of-context plz")
      
@bot.command()
async def images(ctx): 
  available = "Image categories: \nwaifu neko shinobu megumin bully cuddle cry hug awoo kiss lick pat smug bonk yeet blush smile wave highfive handhold nom bite glomp slap kill happy wink poke dance cringe blush"
  await ctx.reply(available)
      
@bot.command()
async def kyoufyme(ctx):
  image_url = ctx.author.avatar_url_as(static_format='png') #Gets your pfp url
  image_url= str(image_url).split("?")[0] #removes some parameters like ?format and ?size at the end of the url
  filename = str(image_url).split("/")[-1] #get the filename from the url
  response = requests.get(image_url)
  file = open(filename, "wb")
  file.write(response.content)
  file.close() #save img
  img = Image.open(filename).convert('LA') #apply greyscale filter
  img.save('greyscale.png')
  await ctx.reply(file=discord.File('greyscale.png'))
  
#Aside from context, we recieve an extra parameter, idiot, which is the url for an image, TO-DO: regex to see if the given parameter is an url or not
@bot.command()
async def kyoufyou(ctx,*,idiot):
  image_url = str(idiot)
  filename = image_url.split("/")[-1]#get filename
  response = requests.get(image_url)
  file = open(filename, "wb")
  file.write(response.content)
  file.close()
  img = Image.open(filename).convert('LA')
  img.save('greyscale.png')
  await ctx.reply(file=discord.File('greyscale.png'))
  
@bot.command()
async def quote(ctx):
  url = "https://animechan.vercel.app/api/random"
  response = requests.get(url)
  aniQoute = response.json()
  anime = aniQoute["anime"]
  character = aniQoute["character"]
  quote = aniQoute["quote"]
  embed=discord.Embed(title=anime, url="https://luppiter.xyz", description=character, color=0xa0200e)
  embed.set_author(name="Random anime quote")
  embed.add_field(name="Qoute", value=quote, inline=False)
  await ctx.reply(embed=embed)
  
@bot.command()
async def waifu(ctx,*,user):
  author = ctx.author.display_name
  category = "waifu"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)

@bot.command()
async def neko(ctx,*,user):
  author = ctx.author.display_name
  category = "neko"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def shinobu(ctx,*,user):
  author = ctx.author.display_name
  category = "shinobu"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)

@bot.command()
async def megumin(ctx,*,user):
  author = ctx.author.display_name
  category = "megumin"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def bully(ctx,*,user):
  author = ctx.author.display_name
  category = "bully"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def cuddle(ctx,*,user):
  author = ctx.author.display_name
  category = "cuddle"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def awoo(ctx,*,user):
  author = ctx.author.display_name
  category = "awoo"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def cry(ctx,*,user):
  author = ctx.author.display_name
  category = "cry"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def kiss(ctx,*,user):
  author = ctx.author.display_name
  category = "kiss"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)

@bot.command()
async def hug(ctx,*,user):
  author = ctx.author.display_name
  category = "hug"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def lick(ctx,*,user):
  author = ctx.author.display_name
  category = "lick"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def pat(ctx,*,user):
  author = ctx.author.display_name
  category = "pat"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def smug(ctx,*,user):
  author = ctx.author.display_name
  category = "smug"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def bonk(ctx,*,user):
  author = ctx.author.display_name
  category = "bonk"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def yeet(ctx,*,user):
  author = ctx.author.display_name
  category = "yeet"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def blush(ctx,*,user):
  author = ctx.author.display_name
  category = "blush"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def smile(ctx,*,user):
  author = ctx.author.display_name
  category = "smile"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def wave(ctx,*,user):
  author = ctx.author.display_name
  category = "wave"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def handhold(ctx,*,user):
  author = ctx.author.display_name
  category = "handhold"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def nom(ctx,*,user):
  author = ctx.author.display_name
  category = "nom"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)

@bot.command()
async def bite(ctx,*,user):
  author = ctx.author.display_name
  category = "bite"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def glomp(ctx,*,user):
  author = ctx.author.display_name
  category = "glomp"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def slap(ctx,*,user):
  author = ctx.author.display_name
  category = "slap"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def kill(ctx,*,user):
  author = ctx.author.display_name
  category = "kill"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def happy(ctx,*,user):
  author = ctx.author.display_name
  category = "happy"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def wink(ctx,*,user):
  author = ctx.author.display_name
  category = "wink"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def poke(ctx,*,user):
  author = ctx.author.display_name
  category = "poke"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def dance(ctx,*,user):
  author = ctx.author.display_name
  category = "dance"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)
  
@bot.command()
async def cringe(ctx,*,user):
  author = ctx.author.display_name
  category = "cringe"
  userTarget = user
  myembed = imagesAPI.apiConsumer(category,author,userTarget)
  await ctx.reply(embed=myembed)

@bot.command()
async def unkyou(ctx,*,idiot):
  image_url = str(idiot)
  filename = image_url.split("/")[-1]#get file name
  response = requests.get(image_url)
  file = open(filename, "wb")
  file.write(response.content)
  file.close()
  img = Image.open(filename).convert('L')
  colors = [
        "red",
        "lime",
        "blue",
        "yellow",
        "cyan",
        "magenta",
        "maroon",
        "olive",
        "green",
        "purple",
        "teal",
        "navy",
        "brown",
        "crimson",
        "tomato",
        "coral",
        "salmon",
        "orange",
        "gold",
        "indigo",
        "orchid",
        "sienna"      
    ]#List of random RGB color names
  img1 = ImageOps.colorize(img, black =random.choice(colors), white =random.choice(colors))#With Pillow we colorize the downloaded img with a random color for black pixels and white pixels from the previous list
  img1.save('color.png')
  await ctx.reply(file=discord.File('color.png'))


# R
@bot.command()
async def roulette(ctx):
    if str(ctx.channel.id) == "826972058256539699": #Russian Roulette channel
      list1 = [1, 2, 3, 4, 5, 6]
      r = (random.choice(list1))
      rolesList = ctx.author.roles

      if "<Role id=823011545230606336 name='Dumbo qwq;;'>" in str(rolesList): #Saving our jannies >:)
        r=5
      
      if "<Role id=823036784409575495 name='Tomboy Gf'>" in str(rolesList): #Saving our boosters >:)
        r=5

      if r == 4:
          await ctx.reply("Result in 10 seconds")
          time.sleep(10)
          await ctx.message.author.send('Get rekt \n https://discord.gg/hGAGpXMstq \n Write .roles on the #russian-roulette to get your roles back and react on #roles again') #DMs you the invite
          await ctx.guild.kick(ctx.author, reason="F")
          embed = discord.Embed(title="Russian Roulette Simulator", description="Get Rekt", color=0xa0200e)
          embed.set_image(url="https://cdn.weeb.sh/images/BJO2j1Fv-.gif")
          await ctx.reply(embed=embed)
      else:
          await ctx.reply("Result in 10 seconds")
          time.sleep(10)
          embed = discord.Embed(title="Russian Roulette Simulator", description="Safe!", color=0xa0200e)
          embed.set_image(url="https://static.wikia.nocookie.net/b__/images/f/fc/030-SniperMonkey.png/revision/latest?cb=20190522024008&path-prefix=bloons")
          await ctx.reply(embed=embed)
    else:
      await ctx.reply("Use russian-roulette plz")

@bot.command()
async def roles(ctx): #When you get kicked and have no roles, the base User role is given to you by YAGPDB bot
    await ctx.reply("Ping a janny, bot broke")

# 8ball
@bot.command()
async def ball(ctx, *, question):
    ans = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "no",
        "Don't care didn't asked"
      ]
    res = random.choice(ans)
    desc = f"**Question**: {question}\n**Answer**: {res}"
    embed = discord.Embed(title=":8ball:", description=desc, color=0xa0200e)
    embed.set_image(url="https://media.giphy.com/media/21L0pjnc0mvHBLXehU/giphy.gif")
    await ctx.reply(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Saving the Geo-Front"))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Starting Bot at: " + current_time)
    print("Logged in as: {}".format(bot.user.name))

bot.run("token")

