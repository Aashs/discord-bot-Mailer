
import discord
from discord.ext import commands

class Start(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        
        
def setup(bot):
    bot.add_cog(Start(bot)) 
