import discord
from discord.ext import commands

class cring(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_typing(self, channel, user : discord.Member, ctx):
        if user.is_on_mobile(): 
            await channel.send(f'{user.mention} is cring')
        

def setup(client):
    client.add_cog(cring(client))