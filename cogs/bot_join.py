import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self)
        await guild.create_category('Mailer')
       
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
