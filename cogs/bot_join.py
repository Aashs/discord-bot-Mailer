import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.create_text_channel("📯announcements-and-suggestions")
        await guild.create_text_channel("💼log")
        
    
    @commands.command()
    async def latency(self, ctx):
        await ctx.send(bot.latency)
       
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
