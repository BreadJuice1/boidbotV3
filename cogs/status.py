from discord.ext import commands
import discord

class setgame(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.commandid = 10


    @commands.command()
    async def game(self,ctx,*,game):
        game = discord.Game(game)
        await self.bot.change_presence(status=discord.Status.online, activity=game)


def setup(bot):
    bot.add_cog(setgame(bot))
