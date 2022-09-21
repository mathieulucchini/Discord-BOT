from ast import arg
from random import randint, random
from discord.ext import commands
import discord
from discord.utils import get

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 227772247090135040  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    if (message.content == "Salut tout le monde"):
        await ctx.send("Salut tout seul " + message.author.mention)
    else:
        await bot.process_commands(message)
        
@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.message.author.name)

@bot.command()
async def d6(ctx):
    await ctx.send(randint(1, 6))

@bot.command()
async def admin(ctx, arg1=None):
    if (arg1 == None):
        await ctx.send("La commande admin a besoin d'un nom d'utilisateur d'un membre du serveur pour fonctionner")
    else:
        user = ctx.message.author
        role = get(ctx.guild.roles, name="admin")
        if role == None:
            guild = ctx.guild
            await guild.create_role(name="admin")
        role = get(ctx.guild.roles, name="admin")  
        await user.add_roles(role)

@bot.command()
async def ban(ctx, user: discord.Member=None):
        if (user == None):
            await ctx.send("La commande ban a besoin d'un nom d'utilisateur d'un membre du serveur pour fonctionner")
        else:
            await ctx.guild.ban(user, reason="Pas cool")

@bot.command()
async def count(ctx):
    off = 0
    idle = 0
    on = 0
    for member in ctx.guild.members:
        status = member.status
        if (status == discord.Status.online): on += 1
        elif (status == discord.Status.idle): idle += 1
        else: off += 1
    await ctx.send(str(on) + " " + "members are online, " + str(idle) + " are idle and " +str(off) + " are off")

@bot.command()
async def xkcd(ctx):
    val = randint(1, 2674)
    await ctx.send("https://xkcd.com/" + str(val))


token = ""
bot.run(token)  # Starts the bot


