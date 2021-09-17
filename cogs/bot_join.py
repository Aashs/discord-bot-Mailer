import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(ctx):
        
      
    

        
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
