import discord
from discord.ext import commands

class control(commands.Cog):

    def __init__(self, client):
        self.client = client

    @client.command()
    @commands.is_owner()
    async def rename(self, ctx, name):
        await client.user.edit(username=name)

def setup(client):
    client.add_cog(control(client))