import discord
from discord.ext import commands

class start(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
      print('Bot is ready')
      
      
    @commands.command()
    async def latency(self, ctx):
      await self.bot.ctx.send(bot.latency)


def setup(bot):
  bot.add_cog(start(bot)) 
