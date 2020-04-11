import discord
from discord.ext import commands
import random

class Cock(commands.Cog):

    def __init__(self, client):
        self.client = client
        print('bruh')
        self.ass = open('reviews.txt', 'r')
        print('bruh')
        self.lines = self.ass.readlines()

    @commands.command(aliases=['cock_review', 'cock'])
    async def review(self, ctx, *, target : str):
        print(f'reviewing {target}\' cock')
        await ctx.send(f'{random.choice(self.lines)} \nreviewing {target}\'s cock')

def setup(client):
    client.add_cog(Cock(client))