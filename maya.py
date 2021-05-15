# coding=utf8
#pip imports
import discord
from discord.ext import commands
import requests
from PIL import Image, ImageOps
#oldM.py
import oldM
#standard imports
import random
import time
from random import seed
from random import randint
import oldM
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
    await ctx.send(embed=embed)

# Mecometer
@bot.command()
async def sus(ctx, *, user):
    if str(ctx.channel.id) == "826966640100376587":
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
    #print(myDict)
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
  print(response.text)
  anime = aniQoute["anime"]
  character = aniQoute["character"]
  quote = aniQoute["quote"]
  embed=discord.Embed(title=anime, url="https://luppiter.xyz", description=character, color=0xa0200e)
  embed.set_author(name="Random anime quote")
  embed.add_field(name="Qoute", value=quote, inline=False)
  await ctx.reply(embed=embed)
  
@bot.command()
async def waifu(ctx):

  url = "https://api.waifu.pics/sfw/waifu"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random waifu  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)

@bot.command()
async def neko(ctx):

  url = "https://api.waifu.pics/sfw/neko"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random neko   image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def shinobu(ctx):

  url = "https://api.waifu.pics/sfw/shinobu"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random shinobu  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)

@bot.command()
async def megumin(ctx):

  url = "https://api.waifu.pics/sfw/megumin"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random megumin image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def bully(ctx):

  url = "https://api.waifu.pics/sfw/bully"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random bully  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def cuddle(ctx):

  url = "https://api.waifu.pics/sfw/cuddle"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random cuddle  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def awoo(ctx):

  url = "https://api.waifu.pics/sfw/awoo"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random awoo  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def cry(ctx):

  url = "https://api.waifu.pics/sfw/cry"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random cry image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def kiss(ctx):

  url = "https://api.waifu.pics/sfw/kiss"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random kiss  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)

@bot.command()
async def hug(ctx):

  url = "https://api.waifu.pics/sfw/hug"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random hug image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def lick(ctx):

  url = "https://api.waifu.pics/sfw/lick"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random lick  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def pat(ctx):

  url = "https://api.waifu.pics/sfw/pat "
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random pat  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def smug(ctx):

  url = "https://api.waifu.pics/sfw/smug"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random smug  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def bonk(ctx):

  url = "https://api.waifu.pics/sfw/bonk "
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random bonk  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def yeet(ctx):

  url = "https://api.waifu.pics/sfw/yeet"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random yeet  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def blush(ctx):

  url = "https://api.waifu.pics/sfw/blush"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random blush  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def smile(ctx):

  url = "https://api.waifu.pics/sfw/smile"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random smile  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def wave(ctx):

  url = "https://api.waifu.pics/sfw/wave"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random wave  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def handhold(ctx):

  url = "https://api.waifu.pics/sfw/handhold"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random handhold  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def nom(ctx):

  url = "https://api.waifu.pics/sfw/nom"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random nom  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)

@bot.command()
async def bite(ctx):

  url = "https://api.waifu.pics/sfw/bite"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random bite  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def glomp(ctx):

  url = "https://api.waifu.pics/sfw/glomp"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random glomp  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def slap(ctx):

  url = "https://api.waifu.pics/sfw/slap"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random slap  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def kill(ctx):

  url = "https://api.waifu.pics/sfw/kill"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random kill  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def happy(ctx):

  url = "https://api.waifu.pics/sfw/happy"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random happy  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def wink(ctx):

  url = "https://api.waifu.pics/sfw/wink"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random wink  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def poke(ctx):

  url = "https://api.waifu.pics/sfw/poke"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random poke  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def dance(ctx):

  url = "https://api.waifu.pics/sfw/dance"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random dance  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)
  
@bot.command()
async def cringe(ctx):

  url = "https://api.waifu.pics/sfw/cringe"
  response = requests.get(url)
  nekoJSON = response.json()
  print(response.text)
  
  embed=discord.Embed(title="Maya", url="https://luppiter.xyz", description="Maya", color=0xa0200e)
  embed.set_author(name="Random cringe  image")
  embed.set_image(url=nekoJSON["url"])
  await ctx.reply(embed=embed)



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
      print(r)#Ok yeah I know that you may be wondering why I dont use the native math random fx, it sucks ass

      if ctx.author.name == "NightmareNanako":
        r=5
        await ctx.reply("I cant kick you bitch, you are the owner")
        
      if ctx.author.name == "Rustic": #TO-DO: Remove rustic being hardcoded, check ctx.author.roles list and parse looking for tomboy gf role https://discordpy.readthedocs.io/en/latest/api.html?highlight=user#discord.Member.roles
        r=5
        await ctx.reply("I cant kick you bitch, you are a server booster")
       #Cant kick owner and idk what will happen to your boost if you get kicked

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
    dictRoles = {
                                'Luppiter' : 'Dumbo qwq;;',
                                'El hombre castigado' : 'Taqueria de Goku',
                                'sasha' : 'Kawaii-est Music Nerd',
                                'puff' : 'White Kimchi',
                                'Aislyn Weaver' : 'Best Anime Neko',
                                'Tangy' : 'Aniki senpai',
                                'alexander' : 'Aniki senpai',
                                'human' : 'Aniki senpai',
                                'n.denel' : 'Aniki senpai',
                                'fr0ppy' : 'Aniki senpai',
                                'permolle': 'Aniki senpai',
                                'mel': 'Aniki senpai',
                                'qwer': 'Aniki senpai',
                                'TafferCat': 'Aniki senpai',
                                'coffeecan' : 'Neko Girls',
                                'h0ly gh0s7 g1rlfr13nd' : 'Neko Girls',
                                'Rustic' : 'Neko Girls',
                                'finland' : 'Neko Girls',
                                'Eggnegg' : 'Neko Girls',
                                'Agamemnon' : 'Neko Girls',
                                'pdmie' : 'Neko Girls',
                                'laura' : 'Neko Girls',
                                'Yat' : 'Neko Girls',
                                'klein' : 'Neko Girls',
                                'Kyou' : 'Cursed Trad Wife',
                                'Fnargo' : 'Trad Wife',
                                'Kiinyo' : 'Trad Wife',
                                'Telefonál a Sátánia' : 'Trad Wife',
                                'LuppterRoulette' : 'Aniki senpai'
                                }
    member = ctx.author #Creating a member Object because discord.py 1.6 sometimes has probles with ctx.author.guild.roles 
    memberName = ctx.author.name
    role1 = discord.utils.get(member.guild.roles, name=dictRoles[memberName])
    await member.add_roles(role1)

# 8ball
@bot.command()
async def ball(ctx, *, question):
    if ctx.author.name == 'Luppiter':
      respuestas = [
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
        "Reply hazy, try again."
      ]
    else:
      respuestas = [
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
        "no"
      ]
    res = random.choice(respuestas)
    desc = f"**Question**: {question}\n**Answer**: {res}"
    embed = discord.Embed(title=":8ball:", description=desc, color=0xa0200e)
    embed.set_image(url="https://media.giphy.com/media/21L0pjnc0mvHBLXehU/giphy.gif")
    await ctx.reply(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Best girl"))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Iniciando Bot a las: " + current_time)
    print("Logged in as: {}".format(bot.user.name))

bot.run("token")

