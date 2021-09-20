import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def setup(self, ctx):
        a = await ctx.guild.create_category('Mailer')
        await ctx.guild.create_text_channel('Mailer-logs',category=a)
        embed = discord.Embed(title="Setup",description="Created a private channel called in Mailer category, use ``-accessrole[roles]`` give staff access to the channel.",color=0x1793FC)
        await ctx.send(embed=embed)
    
    
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
