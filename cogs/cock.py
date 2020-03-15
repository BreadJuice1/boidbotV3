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
    
   ## @commands.commands(aliases=['number_review'])
    ##async def review2(self, ctx, *, target : str):
      ##  print(f'reviewing {target}\' cock')
        ##mouthfeel = random.randint(1, 10)
        ##taste = random.randint(1, 10)
        ##texture = random.randint(1, 10)
        ##smell = random.randint(1, 10)
        ##appearance = random.randint(1, 10)
        ##overall = (mouthfeel + taste + texture + smell + appearance) / 5
        ##await ctx.send(f'mouthfeel:{mouthfeel}\ntaste:{taste}\ntexture:{texture}\nsmell:{smell}\nappearance:{appearance}\noverall:{overall}')

def setup(client):
    client.add_cog(Cock(client))