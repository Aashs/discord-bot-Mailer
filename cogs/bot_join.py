import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(ctx):
        await ctx.send('brrr')
       
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
