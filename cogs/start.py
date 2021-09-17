import discord
from discord.ext import commands

class Start(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
      if ctx.guild is None and not ctx.author.bot:
        print(ctx.content)  
        print(ctx.author) 

        embed = discord.Embed(title="Confirm Mail creation",description="This system is used for reporting bugs,reports concerning to the moderators.",color=0x3DFD1E)
  
        msg=await ctx.author.send(embed=embed)

def setup(bot):
  bot.add_cog(Start(bot)) 
 
    #test
