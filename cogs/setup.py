import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def setup(self, ctx):
        all_channels = []
        all_categories = []
        for category in ctx.guild.categories:
            all_categories.append(category)
        for channel in ctx.guild.text_channels:
                all_channels.append(channel.id)
             
        category_exists = False
        channel_exists = False
        for i in all_channels:
            channel = self.bot.get_channel(i)
            if channel.name == 'mailer-logs':
                channel_exists = True
        for i in all_categories:
            if i.name == 'Mailer':
                category_exists = True

        if category_exists == True and channel_exists == True:
            embed = discord.Embed(title="Setup",description=f"Created a private channel {i.mention}, use ``-accessrole[roles]`` give staff access to the channel.",color=0x1793FC)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"Bot is already setted up",color=0xFF0000)
            await ctx.send(embed=embed)
    
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
