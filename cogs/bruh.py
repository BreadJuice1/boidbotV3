import discord
from discord.ext import commands

class Bruh(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # events
    @commands.Cog.listener()
    async def on_message(self, ctx):
        print(f'{ctx.created_at} | {ctx.author} | {ctx.content}')
        print(f'{ctx.mention_everyone}')
        if ctx.mention_everyone:
            await ctx.channel.send('<:bruh:688525458194694178>')
    
        await client.process_commands(ctx)
    
    # commands
    @commands.command()
    async def bruh(self, ctx):
        await ctx.send('Bruh!')

def setup(client):
    client.add_cog(Bruh(client))