import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def setup(self, ctx):
        embed = discord.Embed(title="Setup",description="Created a private channel called #mailer-logs, use ```-accessrole[roles]``` give staff access to the channel.",color=0x1793FC)
    
    
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
