import discord
from discord.ext import commands

class Bruh(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bruh(self, ctx):
        await ctx.send('Bruh!')

def setup(client):
    client.add_cog(Bruh(client))