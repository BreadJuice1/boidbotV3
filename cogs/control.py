import discord
from discord.ext import commands

class Control(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def rename(self, ctx, *, name):
        await ctx.guild.me.edit(nick=name)

def setup(client):
    client.add_cog(Control(client))