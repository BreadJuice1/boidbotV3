import discord 
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '!')

# Events
@client.event
async def on_ready():
    print('ready')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'{ctx.author} is a boid')

# Commands
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} loaded')
    await ctx.send(f'{extension} loaded')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'{extension} unloaded')
    await ctx.send(f'{extension} unloaded')

@client.command()
@commands.is_owner()
async def load_all(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    print('shutting down...')
    await ctx.send('bruh... :(')
    client.logout
    print('logged out')

@client.command(aliases=['wake up'])
@commands.is_owner()
async def wake_up(ctx):
    print('waking up...')
    client.login
    await ctx.send('im here and im queer')
    print('logged in')

client.run('Njg4MTY4MDYyMjI2MjY4MTcz.XmyRPw.ftRQrrzWND2uUN4osgPEX4D7ZSE')