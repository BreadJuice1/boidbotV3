import discord
from discord.ext import commands

class cring(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_typing(self, channel, user : discord.Member, ctx):
        if user.is_on_mobile(): 
            await channel.send(f'{user.mention} is cring')
        

    @commands.command()
    async def iscring(self, ctx, target : discord.Member):
        if target.is_on_mobile():
            await ctx.send(f'{target.mention} is cring')
        else:
            await ctx.send(f'{target.mention} is not cring')

def setup(client):
    client.add_cog(cring(client))