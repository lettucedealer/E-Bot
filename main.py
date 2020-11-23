import discord
import os
import random
import math
from bs4 import BeautifulSoup
from discord.ext import commands
from googlesearch import search
intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(command_prefix="//", intents=intents)
bot.remove_command("help")
#define shit here

def read(file:str):
    with open(file, "r") as f:
        h = f.read(file)
        return h
def write(file:str, string:str):
    with open(file, "w") as f:
        f.write(string)
class roleShopList():
    def __init__(self):
        self.rlist = []
class roleItem():
    def __init__(self, name, price:int, flist:roleShopList):
        self.name = name
        self.price = price
        flist.rlist.append(self)
class shopList():
  def __init__(self):
    self.slist = []
class shopItem():
  def __init__(self, fnumber, fuses, fname, femoji, fdescription, fprice:int, list:shopList):
    self.number = fnumber
    self.uses = fuses
    self.name = fname
    self.description = fdescription
    self.emoji = femoji
    self.price = fprice
    list.slist.append(self)
class helpCommandList():
  def __init__(self):
    self.clist = []
class helpCommand():
  def __init__(self, fname, fdescription, list:helpCommandList):
    self.name = fname
    self.description = fdescription
    list.clist.append(self)
roleShop = roleShopList()
Femboy = roleItem("Femboy", 5000, roleShop)
Bitcoin_Investor = roleItem("Bitcoin Investor", 10000, roleShop)
Bobux_Generator = roleItem("Bobux Generator", 15000, roleShop)
theshop = shopList()
gun = shopItem("(1)", 3, "Gun", "🔫", "Next 3 robberies will always be successful and will always yield over 800 Bobux", 3000, theshop)
false_legal = shopItem("(2)", 1, "Falsified Legal Document", "📝", "Any person you use this on will be accused of burning down your house (even though you did it during a fentanyl trip) and will be sued for half of their money", 10000, theshop)
lock = shopItem("(3)", 1, "Lock", "🔒", "Next robbery against you will fail and you will end up winning money in reperations", 750, theshop)
luck_charm = shopItem("(4)", 5, "Luck Charm", "🍀", "Next 5 times you do //work, you will always gain money", 5000, theshop)
thelist = helpCommandList()
command1 = helpCommand("keepalive", "if no one uses me after a while i end up disconnecting. This will be fixed soon but my dev is too lazy to add autoping so do that for now", thelist)
command2 = helpCommand("google", "google anything using this command, u just gotta write //google (what u wanna search)", thelist)
command3 = helpCommand("suggest", "Suggest something, your suggestion will appear in the suggestion channel", thelist)
command4 = helpCommand("work and balance", "You can see how they work in #announcements, I will make a seperate page for them soon though", thelist)
async def gunScript(ctx):
  if os.path.isfile(f"{ctx.author.id}wallet") is False:
     await ctx.send("s")
@bot.command()
async def roleshop(ctx):
    desc = []
    for roles in roleShop.rlist:
        desc.append(f"**{roles.name} - {roles.price} Bobux**")
    embed = discord.Embed(
      title = "Welcome to the role shop",
      description = "\n".join(desc),
      color = discord.Colour.blue()
   )
    await ctx.send(embed=embed)
@bot.command()
async def buyrole(ctx, *, role):
    roleexchange = []
    guild = ctx.message.guild
    bought_role = discord.utils.get(guild.roles, name=role)
    print(bought_role)
    for roles in roleShop.rlist:
        if roles.name == bought_role.name:
            chosen_role = roles
            roleexchange.append(chosen_role)
            print(chosen_role.name)
    with open(f"{ctx.author.id}wallet.txt", "r") as f:
        n = f.read()
    intn = int(n)
    chosenrole = roleexchange[0]
    newn = intn - chosenrole.price
    strnew = str(newn)
    with open(f"{ctx.author.id}wallet.txt", "w") as f:
        f.write(strnew)
    await ctx.author.add_roles(bought_role)
    await ctx.send(f"Successfully bought: {chosen_role.name} Role")
@bot.command()
async def inventory(ctx):
  with open(f"{ctx.author.id}inventory.txt", "r") as f:
    s = f.read()
  embed = discord.Embed(
    title = f"{ctx.author.name}, here's whats in ur inventory",
    description = s,
    color = discord.Colour.green()
  )
  embed.set_thumbnail(url = ctx.author.avatar_url)
  await ctx.send(embed=embed)
@bot.command()
async def spoiler(ctx, member:discord.Member):
    how = bot.get_user(669244309467430912)
    if ctx.author == how:
        await member.send(f"{member.name}, you've been **S P O I L E R E D**")
        await ctx.send(f"{member.name} has been spoilered")
    else:
        await ctx.send("no cuz ur not cool enough sry")
@bot.command()
async def autism(ctx, *, member:discord.Member=None):
  autcount = random.randint(1,100)
  if member is None:
    await ctx.send("You gotta specify a member")
  
  else:
    if member.name == "LMR14" or member.name == "Russian Raccoon":
      autcount = 100
    if autcount <= 10:
      emo = "**- - - - - - - - - -**"
    elif autcount > 10 and autcount <= 20:
      emo = ":clown: **- - - - - - - - -**"
    elif autcount > 20 and autcount <= 30:
      emo = ":clown: :clown: **- - - - - - - -**"
    elif autcount > 30 and autcount <= 40:
      emo = ":clown: :clown: :clown: **- - - - - - -**"
    elif autcount > 40 and autcount <= 50:
      emo = ":clown: :clown: :clown: :clown: **- - - - - -**"
    elif autcount > 50 and autcount <= 60:
      emo = ":clown: :clown: :clown: :clown: :clown: **- - - - -**"
    elif autcount > 60 and autcount <= 70:
      emo = ":clown: :clown: :clown: :clown: :clown: :clown: **- - - -**"
    elif autcount > 70 and autcount <= 80:
      emo = ":clown: :clown: :clown: :clown: :clown: :clown: :clown: **- - -**"
    elif autcount > 80 and autcount <= 90:
      emo = ":clown: :clown: :clown: :clown: :clown: :clown: :clown: :clown: **- -**"
    elif autcount >= 90:
      emo = ":clown: :clown: :clown: :clown: :clown: :clown: :clown: :clown: :clown: **-**"
    embed = discord.Embed(
      title = f"Here is {member.name}'s autism rating",
      description = f"{emo}",
      color = discord.Colour.red()
    )
    embed.set_author(name=f"{autcount}% autistic", icon_url = member.avatar_url)
    embed.set_thumbnail(url="https://www.budgetbytes.com/wp-content/uploads/2013/07/Creamy-Tomato-and-Spinach-Pasta-skillet-1-500x480.jpg")
    await ctx.send(embed=embed)
@bot.command()
async def keepdead(ctx):
  await ctx.send("fuck you")
@bot.command()
async def botsuggestion(ctx, *, suggestion):
  me = bot.get_user(548190717407920138)
  await me.send(suggestion)
@bot.event
async def on_ready():
  print("retard")
  print("committed")
  print(bot.user.id)
  await bot.change_presence(status=discord.Status.online, activity=discord.Game("//help or smth"))
@bot.event
async def on_member_join(member):
  guild = member.guild
  if guild.id == 743900259188474058:
    embed = discord.Embed(
        title = f"Hi, {member.name}, please send us your answer to the following questions with //send (your responses)",
        description = "``-Why do you want to join ecorp?``",
        color = discord.Colour.blue()
    )
  await member.send(embed=embed)
@bot.command()
async def matchmake(ctx, member1:discord.Member, member2:discord.Member):
    heartlist = []
    n = random.randint(1, 100)
    nquotient = int(math.ceil(n/10)) * 10
    print(nquotient)
    finaln = n/10
    print(finaln)
    print(n)
    for a in range(1, finaln):
        heartlist.append(":heart:")
    desc = "".join(heartlist)
    print(desc)
    embed = discord.Embed(
        title = f"{member1.name} and {member2.name} rating is: {n}",
        description = desc,
        color = discord.Colour.pink()
        )
    print("k")
    await ctx.send(embed=embed)

@bot.command()
async def sex(ctx):

    await ctx.send("You have had the sex but dont worry spoiler is cool gamer now ")
@bot.command()
@commands.cooldown(1, 900, commands.BucketType.user)
async def rob(ctx, *, member:discord.Member):
  print(member.id)
  if os.path.isfile(f"{member.id}wallet.txt") is False:
    await ctx.send("the person you tryna rob has 0 brobux smh")
    rob.reset_cooldown(ctx)
  if member == ctx.author:
    await ctx.send("no.")
    rob.reset_cooldown(ctx)
  else:

    n = random.randint(1, 4)
    i = random.randint(100, 1000)
    if n == 1:
      desc = f"You try to rob {member.name}, but your bad or smth so you get caught. You pay {i} Bobux to them in reperations"
    else:
      desc = f"You successfully rob {member.name}, earning you {i} Bobux"
    embed = discord.Embed(
      title = "You sneak into their house...",
      description = f"``{desc}``",
      color = discord.Colour.blue()
    )
    with open(f"{ctx.author.id}wallet.txt", "r") as f:
      robbermoney = f.read()
    intr = int(robbermoney)
    print(intr)
    with open(f"{member.id}wallet.txt", "r") as f:
      membermoney = f.read()
    intm = int(membermoney)
    if intm < 1000:
      await ctx.send("the man u trying to rob is either in debt or has under 1000 bruh why are u mean")
    else:
      print(intm)
      if n == 1:
        mresult = intm + i
        rresult = intr - i
        print(mresult)
        print(rresult)
      else:
        mresult = intm - i
        rresult = intr + i
        print(mresult)
        print(rresult)
      strm = str(mresult)
      strr = str(rresult)
      with open(f"{ctx.author.id}wallet.txt", "w") as f:
        f.write(strr)
      with open(f"{member.id}wallet.txt", "w") as f:
        f.write(strm)
      await ctx.send(embed=embed)
@rob.error
async def rob_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f"You gotta wait {round(error.retry_after)}s before doing that g")
@bot.command()
async def owoify(ctx,*, text):
  funi = list(text)
  for ting in funi:
    if ting == "l" or ting == "r":
       funi[funi.index(ting)] = "w"
    if ting == "L" or ting == "R":
      funi[funi.index(ting)] = "W"
  gaming = "".join(funi)
  stop = gaming.split()
  for things in stop:
    end = random.randint(1,30+1)
    if end == 30:
      stop.insert(stop.index(things)+1, "owo")
    if end == 29:
      stop.insert(stop.index(things)+1, "UwU")
    if end == 28:
      stop.insert(stop.index(things)+1, "o3o")
    if end == 27:
      stop.insert(stop.index(things)+1, "-pounces-")
    if end == 26:
      stop.insert(stop.index(things)+1, "-nuzzles-")

  embed = discord.Embed(
    title = "Why are u making me do this",
    description = " ".join(stop),
    color = discord.Color.red()
  )
  await ctx.send(embed=embed)
@bot.command()
@commands.cooldown(1, 900, commands.BucketType.user)
async def allah(ctx):
    print("ok")
    n = random.randint(1, 1000)
    with open(f"{ctx.author.id}wallet.txt", "r") as f:
       g = f.read()
    intg = int(g)
    total = n + intg
    strtot = str(total)
    print(strtot)
    with open (f"{ctx.author.id}wallet.txt", "w") as f:
        f.write(strtot)
    embed = discord.Embed(
            title = "Mashallah, Allah has blessed you",
            description = f"You received **{n}** bobux for doing your daily prayer",
            color = discord.Color.blue()
        )
    await ctx.send(embed=embed)
@allah.error
async def allah_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f"You gotta wait {round(error.retry_after)}s before doing that g")
@bot.command()
@commands.cooldown(1, 900, commands.BucketType.user)
async def suggest(ctx, *, suggestion=None):
  if suggestion is None:
    await ctx.send("What do u wanna suggest")
  else:
    channel = bot.get_channel(744397169230086175)
    embed = discord.Embed(
      title = f"guys look {ctx.author.name} has a suggestion",
      description = suggestion,
      color = discord.Colour.blue()
    )
    embed.set_author(name = f"suggested by {ctx.author}", icon_url = ctx.author.avatar_url)
    bruh = await channel.send(embed=embed)
    await bruh.add_reaction("👍")
    await bruh.add_reaction("👎")
@suggest.error
async def suggest_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f"You gotta wait {round(error.retry_after)}s before doing that g")
    
glist = ["You flip some burgers at Mcdonalds", "The CCP rewards you for doing nothing on the 15th of April 1989", "You sell toilet paper on E-Bay", "You get a donation on LiveLeak", "Your bobux generator actually works", "You work at a company that changed their twitter pfp to a rainbow version of itself during pride month", "You got hired as a mercenary to hunt noobs", "You accidentally push your wife off a cliff 3 days after taking out a life insurance policy", "You won the Isletale contest 1st prize", "You sell C.E weapon blueprints to E-Corp"]
blist = ["You live in Sweden", "You got hit by a car lmao dumbass now you gotta pay for insurance dumb retard", "You invested in Boeing", "You give money to your favorite twitch gamer girl so she will marry you", "The Nigerian Prince still hasnt payed you back yet", "You are an employee of AOCU", "You bought the m249 in csgo but got awped while crossing mid-doors"]

@bot.command()
async def buy(ctx, item:int):
  continueThis = False
  bruh = False
  n = theshop.slist[item-1]
  with open(f"{ctx.author.id}wallet.txt", "r") as f:
    money = f.read()
  intm = int(money)
  if n.price > intm:
    await ctx.send("You dont have enough money to buy that")
  else:
    if os.path.isfile(f"{ctx.author.id}inventory.txt"):
      c = open(f"{ctx.author.id}inventory.txt")
      clines = c.readlines()
      print(clines)
      for lines in clines:
        if (f"{n.name}") in lines:
          bruh = True
      if bruh:
        await ctx.send("You already have this item")
      else:
        continueThis = True
    else:
      continueThis = True
    if continueThis is True:
      ok = str(intm - n.price)
      with open(f"{ctx.author.id}wallet.txt", "w") as f:
        f.write(ok)
      with open(f"{ctx.author.id}inventory.txt", "a") as f:
        f.write(f"{n.name} {n.uses}\n")
      await ctx.send(f"Succesfully bought: {n.name}")

@bot.command()
@commands.cooldown(1, 14400, commands.BucketType.user)
async def boom(ctx):
    guild = ctx.message.guild
    bruh = random.choice(guild.members)
    print(bruh.id)
    if os.path.isfile(f"{bruh.id}wallet.txt") is False:
        embed = discord.Embed(
            title = "u just exploded someone lmao",
            description = f"``{bruh.name} didnt have an account doe :((``",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)
    else:
        with open(f"{bruh.id}wallet.txt", "r") as f:
            money = f.read()
        intmoney = int(money)
        print(intmoney)
        dividemoney = round(intmoney/4)
        n = random.randint(1, dividemoney)
        print(n)
        newmoney = intmoney - n
        strn = str(newmoney)
        with open(f"{bruh.id}wallet.txt","w") as f:
            f.write(strn)
        print("yeah")
        embed = discord.Embed(
            title = "u just exploded someone lmao",
            description = f"``{bruh.name} just got their switzerland bank blown up and lost {n} Bobux :(((``",
            color = discord.Color.red()
            )
        await ctx.send(embed = embed)
@boom.error
async def boom_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f"You gotta wait {round(error.retry_after)}s before doing that g")
@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def work(ctx):
  i = random.randint(1, 5)
  print(i)
  n = random.randint(100, 1000)
  if i == 1 or i == 2 or i == 3 or i== 4:
    embed = discord.Embed(
      title = "Let's see what you did today",
      description = f"``{random.choice(glist)}, you earn {n}Bobux``",
      color = discord.Colour.green()
    )
    embed.set_thumbnail(url = ctx.author.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(
      title = "Let's see what you did today",
      description = f"``{random.choice(blist)}, you lost {n} Bobux``",
      color = discord.Colour.red()
    )
    embed.set_thumbnail(url = ctx.author.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  if os.path.isfile(f"{ctx.author.id}wallet.txt") is False:
    with open(f"{ctx.author.id}wallet.txt", "w") as f:
      f.write(str(0))
  with open(f"{ctx.author.id}wallet.txt", "r") as f:
    currentmoney = f.read()
  intcurrentmoney = int(currentmoney)
  if i == 1 or i == 2 or i == 3 or i== 4:
    newmoney = (intcurrentmoney + n)
  else:
    newmoney = (intcurrentmoney - n)
  strnewmoney = str(newmoney)
  
  with open(f"{ctx.author.id}wallet.txt", "w") as f:
    f.write(strnewmoney)
@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f"You gotta wait {round(error.retry_after)}s before doing that g")
@bot.command()
async def use(ctx, item:str, member:discord.Member=None):
  def useDict(item):
    switcher ={
      "Gun":"placeholder"
    }
@bot.command()
async def balance(ctx, member:discord.Member=None):
  if member is None:
    member = ctx.author
  if os.path.isfile(f"{member.id}wallet.txt") is False:
    await ctx.send("You dont have a bank account, //work to create one")
  else:
    with open(f"{member.id}wallet.txt", "r") as f:
      bal = f.read()
    if member == ctx.author:
      await ctx.send(f"{member.mention}, you have {bal} Bobux in your bank account")
    else:
      await ctx.send(f"**{member.name}** has {bal} Bobux in their bank account")

@bot.command()
async def send(ctx, *, message=None):
  if message is None:
    await ctx.send("Please provide your responses, ex: //send yes i am very cool")
  else:
    
    channel = bot.get_channel(744037647764160524)
    id = str(ctx.author.id)
    embed = discord.Embed(
      title = f"{ctx.author} wants to verify, here is their application",
      description = "``respond by reacting with ✅ to accept and ❌ to deny``",
      color = discord.Colour.blue()
    )
    embed.add_field(name = f"{ctx.author.name}'s application, ", value = message)
    message = await channel.send(embed=embed)
    with open(f"{message.id}.txt", "w") as f:
      f.write(id)
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    
    await ctx.send("message sent")
@bot.event
async def on_reaction_add(reaction, member):
  if member.bot is False and reaction.emoji == "✅":
    print("reacted")
    invite = await bot.fetch_channel(630680633097846784)
    channel = reaction.message.channel
    with open(f"{reaction.message.id}.txt", "r") as f:
      idthing = f.read()
    print("opened")
    invitelink = await invite.create_invite(max_uses=1, unique=True)
    user = await bot.fetch_user(idthing)
    await user.send("**You have been accepted! Here's the invite link**")
    await user.send(invitelink)
    os.remove(f"{reaction.message.id}.txt")
    await channel.send("User accepted succesfully")
  if member.bot is False and reaction.emoji == "🤢":
    spoiler = bot.get_user(669244309467430912)
    print("done")
    await spoiler.send("ew premarital sex ewww disgusting noob retard")
  if member.bot is False and reaction.emoji == "❌":
    with open(f"{reaction.message.id}.txt", "r") as f:
      idthing = f.read()
    user = await bot.fetch_user(idthing)
    await user.send("Unfortunately, you have been denied, which means ur banned now. Sorry!")
@bot.command()
async def shop(ctx):
  desclist = []
  for n in theshop.slist:
    line = (f"**{n.number} {n.name}** - {n.emoji} - {n.description} - {n.price} Bobux")
    desclist.append(line)
  embed = discord.Embed(
    title = "Welcome to the shop",
    description = "\n".join(desclist),
    color = discord.Color.green()
  )
  await ctx.send(embed=embed)
@bot.command()
async def give(ctx, member:discord.Member, amount:int):
  with open(f"{ctx.author.id}wallet.txt", "r") as f:
    funi = f.read()
  print(funi)
  intf = int(funi)
  if amount > intf:
    await ctx.send("You dont have enough money to do that :((((((((((((((((")
    print(intf)
    print(amount)
  elif amount < 0:
    await ctx.send("no why are u like this")
  else:

    donatoramount = intf-amount
    print(donatoramount)
    
    with open(f"{ctx.author.id}wallet.txt", "w") as f:
      f.write(str(donatoramount))
    print(donatoramount)
    with open(f"{member.id}wallet.txt", "r") as f:
      rfuni = f.read()
    print(rfuni)
    intr = int(rfuni)
    receiver_amount = intr + amount
    stra = str(receiver_amount)
    with open(f"{member.id}wallet.txt", "w") as f:
      f.write(stra)
    print(stra)
    await ctx.send(f"Successfully donated **{amount} Bobux** to {member.name} thank you for ur generosity to poor people that are poor")



@bot.command()
async def keepalive(ctx):
  await ctx.send("thx for keeping me alive")
@bot.command()
async def help(ctx):
  embed = discord.Embed(
    title = f"Hi {ctx.author.name} ima help u",
    description = "(This is for E-Corp commands and not ESG commands)",
    color = discord.Colour.green()
  )
  embed.set_thumbnail(url = ctx.author.avatar_url)
  for n in thelist.clist:
    embed.add_field(name = n.name, value = n.description)
  embed.set_footer(text="if u got a problem or complaint dm lettucedealer")
  await ctx.author.send(embed=embed)
  await ctx.message.add_reaction("🇪")
  await ctx.send("ok i did send")
@bot.command()
async def google(ctx, *, thing=None):
  if thing is None:
    await ctx.send("what do u wanna google tho")
  else:
    guild = ctx.message.guild
    query = f"{thing}"
    embed = discord.Embed(
      title = f"Search query ``{query}``",
      color = discord.Colour.red()

    )
    embed.set_author(name=f"asked by {ctx.author.name}",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    for j in search(query, tld="co.in", num=1, stop=1): 
      await ctx.send(j) 


  
  

bot.run("NzQ0MDA5NjU3OTY5ODAzMjk1.Xzc-_Q.u5SByq7iaf51EGb2LwwpUcmt-JM")