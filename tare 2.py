import discord
from bot_logic import gen_pass
from discord. ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix= "$", intents=intents)

@bot.event
async def on_ready():
     print(f'hemos iniciado sesion como {bot.user}')

@bot.command()
async def hello(ctx):
     await ctx.send(f'Hola!')
#!!!!!     
@bot.command()     
async def bye(ctx):
     await ctx.send(f'😞')

@bot.command()     
async def password(ctx):
     await ctx.send(gen_pass(10))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run('aqui va tu token')
