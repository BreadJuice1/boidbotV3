import discord
from discord.ext import commands
import random
from random import randint

class Roulette(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 300, commands.BucketType.user)
    @commands.command()
    async def roulette(self, ctx : discord.Message, target : discord.Member):
        print(f'{ctx.author} has initiated roulette')
        await ctx.channel.send('rolling...')
        if random.randint(1, 6) == random.randint(1, 6):
            print(f'{target} has died.')
            await ctx.channel.send(f'{target.mention} failed the vibe check')
            await target.kick()
        else:
            print(f'{target} has passed.')
            await ctx.channel.send(f'{target.mention} passed the vibe check')
        

def setup(client):
    client.add_cog(Roulette(client))