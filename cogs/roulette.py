import discord
from discord.ext import commands
import random
from random import randint

class Roulette(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def roulette(self, ctx):
        print(f'{ctx.author} has initiated roulette')
        await ctx.channel.send('rolling...')
        if random.randint(1, 6) == random.randint(1, 6):
            print(f'{ctx.author} has died.')
            await ctx.channel.send(f'{ctx.author} failed the vibe check')
            await ctx.author.kick()
        else:
            print(f'{ctx.author} has passed.')
            await ctx.channel.send(f'{ctx.author} passed the vibe check')

def setup(client):
    client.add_cog(Roulette(client))