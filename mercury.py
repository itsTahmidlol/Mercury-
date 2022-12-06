# -*- coding: utf-8 -*-
# imagine skidding z.
try:
    import discord
    import os
    import json
    import aiohttp
    import base64
    import random
    import requests
    import string
    import asyncio
    
    from discord.ext import commands
    from colorama import init, Fore as f
    from server import keep_alive

except ModuleNotFoundError as err:
    print(err)


w = open('mercury.json', 'r') 
data = json.load(w)
init(autoreset = True)
bot_token = data.get('token')
prefix = data.get('prefix')
dat = 15 #Default error Delete time
activity = discord.Game(name="mercury")
channel_list = data.get('channel_list')
message_list = data.get('message_list')
keep = data.get('keeping_bot_alive')

def screen():
    print(f"""
    \n\n\t\t{f.GREEN}                       Mercury v1.2
    \t\t{f.GREEN}Authorized as: {mercury.user.name}#{mercury.user.discriminator} (ID: {mercury.user.id})
    \t\t{f.LIGHTBLUE_EX}Invitation Link: https://discord.com/api/oauth2/authorize?client_id={mercury.user.id}&permissions=8&scope=bot
    \t\t{f.LIGHTRED_EX}Enter: {f.LIGHTBLUE_EX}{prefix}help for help {f.RESET}
    \n\t=======================================================================================================
                                            \tTerminal\n
    """)

def r_color():
    r_hex = int(random.randrange(0xFFFFFF))
    return r_hex

def rand_string_gen(length):
    char = string.ascii_letters
    digit = string.digits
    gen = random.choices(char+digit, k = length)
    return gen

mercury = discord.Client(intents=discord.Intents.all())
mercury = commands.Bot(command_prefix=prefix, help_command=None, description="\nMade by 1015192535410409532", intents=discord.Intents.all(), activity=activity)

@mercury.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return

    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title="Error!", description="Permission for this command is Missing", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=10)

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Error!", description="A Required Argument is missing. Hence could not execute the command", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=dat)
        print(error)

    elif isinstance(error, discord.errors.Forbidden):
        embed = discord.Embed(title="Error!", description=f"Error 404: Forbidden Attempt {error}", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=dat)
        print(error)

    else:
        embed = discord.Embed(title="Error!", description="Unknown Error. kindly check Terminal\n(it might happened due to a bug)", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=dat)
        print(f.RED + str(error))

@mercury.event
async def on_ready():
    os.system("cls")
    screen()

@mercury.command(aliases=["cmd", "commands"])
async def help(ctx, category = None):
    if category is None:
        embed = discord.Embed(title="Help Command", description=f"Default Help Command. to see a category.\ntype {prefix}help **<category>**\n{prefix}cmd <attr> -> Required Attribute", color=r_color(), timestamp=ctx.message.created_at)
        embed.add_field(name="Raid", value="Raiding Commands like Purging Channels, Nuking etc.", inline=False)
        embed.add_field(name="Spam", value="Spamming Commands like Mass Creating Channel etc.", inline=False)
        embed.add_field(name="Tool", value="Some useful tools like IP Tracker etc.", inline=False)
        embed.add_field(name="Other/Misc", value="Show Other Commands.", inline=False)
        embed.set_footer(text="mercury.py | Created by 1015192535410409532")
        await ctx.send(embed=embed)

    elif category.lower() == "raid":
        embed = discord.Embed(title="Raid Commands", description="Purging Specific things in the guild", color=r_color(), timestamp=ctx.message.created_at)    
        embed.add_field(name="nuke", value="Nukes a Server using webhooks.", inline=False)
        embed.add_field(name="rcnl", value="Purge all Channels", inline=False)
        embed.add_field(name="rrole", value="Purge all Roles", inline=False)
        embed.add_field(name="remoji", value="Purges all Emojis", inline=False)
        embed.set_footer(text=" mercury.py | Raid ")
        await ctx.send(embed=embed)
    
    elif category.lower() == "spam":
        embed = discord.Embed(title="Spam Commands", description="Spamming Specific things in the guild", color=r_color(), timestamp=ctx.message.created_at)
        embed.add_field(name="scnl", value="Spams Text Channels", inline=False)
        embed.add_field(name="srole", value="Spams Roles", inline=False)
        embed.add_field(name="svoice", value="Spams Voice Channels", inline=False)
        embed.add_field(name="smgs", value="Spams Messages in every Channels", inline=False)
        embed.set_footer(text=" mercury.py | Spam ")
        await ctx.send(embed=embed)
    
    elif category.lower() == "tool":
        embed = discord.Embed(title="Tool Commands", description="some useful tools", color=r_color(), timestamp=ctx.message.created_at)
        embed.add_field(name="iplocate <ip>", value="Tracks an IP Address", inline=False)
        embed.add_field(name="nitro", value="Returns a fake nitro code", inline=False)
        embed.add_field(name="admin", value="Admin the Author or an user", inline=False)
        embed.add_field(name="guildinfo", value="Shows Info about a Guild", inline=False)
        embed.add_field(name="otax <user>", value="Returns a user's token", inline=False)
        embed.set_footer(text=" mercury.py | Tool ")
        await ctx.send(embed=embed)
    
    elif category.lower() == "misc" or category.lower() == "other":
        embed = discord.Embed(title="Other Commands", description="Other Commands (I need some Ideas about it)", color=r_color(), timestamp=ctx.message.created_at)
        embed.add_field(name="cls", value="Clears the Terminal Screen", inline=False)
        embed.add_field(name="hack <user>", value="Sent hacking Message to a user's DM", inline=False)
        embed.add_field(name="sex <user>", value="Sex a user", inline=False)
        embed.add_field(name="stop", value="stops the bot\n(only owner can use this cmd)", inline=False)
        embed.add_field(name="ping", value="Pings the Bot", inline=False)
        embed.add_field(name="activity <type> <text>", value="Change Bot's Presence Activity", inline=False)
        embed.set_footer(text=" mercury.py | Miscellaneous ")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Unknown Argument", description=f"{category} is not valid.", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=dat)
# Raid Developments 

@mercury.command()
async def rcnl(ctx, limit=-1):
    count = 0
    if limit == -1:
        for ch in list(ctx.guild.channels):
            try:
                await ch.delete()
                count += 1
            except:
                pass
    
    else:
        for ch in list(ctx.guild.channels):
            try:
                await ch.delete()
                count += 1
            except:
                pass
            if count == limit:
                break
    
    print(f"Deleted {count} channels.")

@mercury.command()
async def rrole(ctx):
    count = 0 
    for r in list(ctx.guild.roles):
        try:
            await r.delete()
            count += 1
        except:
            pass
    print(f"Deleted {count} roles.")

@mercury.command()
async def remoji(ctx):
    count = 0
    for e in list(ctx.guild.emojis):
        try:
            await e.delete()
            count += 1
        except:
            pass
    print(f"Deleted {count} emojis.")


@mercury.command()
async def scnl(ctx):
    for i in range(150):
        await ctx.guild.create_text_channel(name = random.choice(channel_list))
        await ctx.guild.create_text_channel(name = random.choice(channel_list))

@mercury.command()
async def srole(ctx, text = None):
    await ctx.message.delete()
    if text is None:
        for i in range(150):
            await ctx.guild.create_role(name = random.choice(channel_list), color = r_color())
    else:
        for i in range(150):
            await ctx.guild.create_role(name = text, color = r_color)

@mercury.command(aliases=["svoice"])
async def svc(ctx):
    await ctx.message.delete()
    for i in range(150):
        await ctx.guild.create_voice_channel(name = random.choice(channel_list))
        await ctx.guild.create_voice_channel(name = random.choice(channel_list))

@mercury.command()
async def smgs(ctx):
    await ctx.message.delete()
    for i in range(40):
        channel = random.choice(list(ctx.guild.text_channels))
        for i in range(3):
            await channel.send(random.choice(message_list))

@mercury.command(aliases=["rekt", "oogabooga"])
async def nuke(ctx):
    await ctx.message.delete()
    try:
        await rrole(ctx)
        await remoji(ctx)
        await rcnl(ctx, 70)
        await scnl(ctx)

    except:
        embed = discord.Embed(title="Error!", description="Can't nuke", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=dat)       

@mercury.event
async def on_guild_channel_create(channel):
    whook = await channel.create_webhook(name = "cock")
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(url = whook.url, session = session)
        while True:
            await webhook.send(random.choice(message_list))

@mercury.command(aliases=["iptrack"])
async def iplocate(ctx, ip = None, gmap = "None"):
    await ctx.message.delete()
    x_ = requests.get("https://extreme-ip-lookup.com/")
    if x_.status_code == 404:
        embed = discord.Embed(title="Error!", description="Website is Down.", color=r_color(), timestamp=ctx.message.created_at)
    else:
        if ip is None:
            embed = discord.Embed(title="Error!", description="Provide an IP", color=r_color(), timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
        else:    
            try:
                x = requests.get(f"https://extreme-ip-lookup.com/json/{ip}?key=JHWVEVkkBhQoa9Wu29zI")
                info = x.json()
                embed = discord.Embed(title="IP tracker", description="Successfully tracked IP", color=r_color(), timestamp=ctx.message.created_at)
                embed.add_field(name="IP", value=f"{ip}", inline=False)
                embed.add_field(name="city", value=f"{info['city']}", inline=False)
                embed.add_field(name="region/division", value=f"{info['region']}", inline=False)
                embed.add_field(name="country", value=f"{info['country']} (Domain: **{info['countryCode']}**)", inline=False)
                embed.add_field(name="continent", value=f"{info['continent']}", inline=False)
                embed.add_field(name="isp", value=f"{info['isp']}", inline=False)
                embed.add_field(name="latitude", value=f"{info['lat']}", inline=False)
                embed.add_field(name="longitude", value=f"{info['lon']}", inline=False)
                if gmap.lower() == "gmap": 
                    embed.add_field(name="Google map Link", value=f"https://www.google.com/maps/@{str(info['lat'])},{str(info['lon'])},19z", inline=False)       

                embed.set_footer(text="mercury.py | Ip Tracker")
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="Error!", description="Cant track IP", color=r_color(), timestamp=ctx.message.created_at)
                await ctx.send(embed=embed, delete_after=dat)
    
@mercury.command()
async def nitro(ctx, as_link = "false"):
    await ctx.message.delete()
    fake_code = "".join(rand_string_gen(16))
    if as_link == "false":
        embed = discord.Embed(title="Nitro Code Generated!", description=f"{fake_code}", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)

    elif as_link.lower() == "aslink":
        embed = discord.Embed(title="Nitro Link Generated!", description=f"https://discord.gift/{fake_code}", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        await ctx.send(f"https://discord.gift/{fake_code}")

    else:
        embed = discord.Embed(title="Error!", description=f"{as_link} is not a valid argument", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=dat)

@mercury.command()
async def admin(ctx, member: discord.Member = None):
    await ctx.message.delete()
    permission = discord.Permissions()
    permission.update(administrator = True)
    role = await ctx.guild.create_role(name="new role", color=0x000000, permissions=permission) #0x000000 is default "new role" color.
    if member is None:
        user = ctx.author
        await user.add_roles(role)

    else:
        await member.add_roles(role)

@mercury.command(aliases=["guild", "serverinfo"])
async def guildinfo(ctx):
    await ctx.message.delete()
    format = "%a, %d %b %Y %I:%M %p"
    server = ctx.guild
    embed = discord.Embed(title="Server Info", description="Info of a Server.", color=r_color(), timestamp=ctx.message.created_at)
    embed.add_field(name="Server name", value=server.name, inline=False)
    embed.add_field(name="Server Created at UTC: ", value=server.created_at.strftime(format), inline=False)
    embed.add_field(name="Server Owner", value=server.owner, inline=False)
    embed.add_field(name="Total Members", value=server.member_count, inline=False)
    embed.add_field(name="Total Roles", value=len(server.roles), inline=False)
    embed.add_field(name="Total Channels", value=len(server.channels), inline=False)
    embed.set_thumbnail(url=server.icon)
    embed.set_footer(text="mercury.py | guild info")
    await ctx.send(embed=embed)

@mercury.command(aliases=["tokengrab", "grab"])
async def otax(ctx, victim: discord.Member = None):
    await ctx.message.delete()
    if victim is None:
        embed = discord.Embed(title="Error!", description="Please Select a User.", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=dat)

    else:
        id = str(victim.id)
        byte = base64.b64encode(id.encode('ascii'))
        decoded_byte = byte.decode('ascii')
        firstpart = decoded_byte[0:len(decoded_byte)-2]
        secondpart = "".join(rand_string_gen(6))
        thirdpart = "".join(rand_string_gen(30))
        fourthpart = "".join(rand_string_gen(8))
        token = f"{firstpart}.{secondpart}.{thirdpart}-{fourthpart}"
        embed = discord.Embed(title="Otaxxed!", description=f"token of {victim.name}#{victim.discriminator}\n{token}", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)

@mercury.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system("clear")
    screen()

@mercury.command()
async def hack(ctx, victim: discord.Member = None):
    await ctx.message.delete()
    if victim is None:
        embed = discord.Embed(tite="Lol.", description="Why you want to be hacked?", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.author.send(embed=embed)

    else:
        url = "https://tenor.com/view/scammer-gif-26147132"
        await victim.send(f"You have been haxxed by {ctx.author.name}#{ctx.author.discriminator}!")
        await victim.send(f"{url}")

@mercury.command()
async def sex(ctx, victim: discord.Member = None):
    await ctx.message.delete()
    url = "https://tenor.com/view/sex-funny-epic-delicious-swag-gif-18123763"
    masturbate_url = "https://tenor.com/view/funny-gag-gif-16058044"
    if victim is None:
        await ctx.send(f"{ctx.author.name}#{ctx.author.discriminator} doing gag!")
        await ctx.send(f"{masturbate_url}")
        
    else:
        await ctx.send(f"{ctx.author.name}#{ctx.author.discriminator} just sexxed {victim.name}#{victim.discriminator}")
        await ctx.send(f"{url}")

@mercury.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.message.delete()
    await ctx.bot.close()

@mercury.command()
async def ping(ctx):
    embed = discord.Embed(title="Pinged!", description=f"bot's respond time {mercury.latency*1000} ms", color=r_color(), timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)

@mercury.command()
async def activity(ctx, type, *, text):
    if type.lower() == "streaming" or type.lower() == "stream":
        await mercury.change_presence(activity=discord.Streaming(
            name=text,
            url="https://www.twitch.tv/"
        ))

    elif type.lower() == "game" or type.lower() == "gaming":
        await mercury.change_presence(activity=discord.Game(name=text))

    elif type.lower() == "listen" or type.lower() == "listening":
        await mercury.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=text))

    elif type.lower() == "watch" or type.lower() == "watching":
        await mercury.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=text
        ))

    else:
        embed = discord.Embed(title="Error!", description=f"{type} is Invalid Argument\nUse Game, Listen, Watch or Stream as a type", color=r_color(), timestamp=ctx.message.created_at)
        await ctx.send(embed=embed, delete_after=dat)

# ----------- Keeping the Bot Alive ----------------- #
if keep is True:
    keep_alive()
else:
    pass

mercury.run(token=bot_token)

# --- End --- #