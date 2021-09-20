import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def setup(self, ctx):
        all_channels = []
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                all_channels.append(channel.id)
                
         for y.id in all_channels:
            if True:
                print('ye ma boi correct')
                break        
        
            x = await ctx.guild.create_category('Mailer')
            y = await ctx.guild.create_text_channel('Mailer-logs',category=x)
            embed = discord.Embed(title="Setup",description=f"Created a private channel {y.mention}, use ``-accessrole[roles]`` give staff access to the channel.",color=0x1793FC)
            await ctx.send(embed=embed)
        

    
    
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
