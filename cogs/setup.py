import discord
from discord.ext import commands
import json

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
            embed = discord.Embed(description=f"Bot is already setted up",color=0xFF0000)
            await ctx.send(embed=embed)
        else:
            x = await ctx.guild.create_category('Mailer')
            y = await ctx.guild.create_text_channel('mailer-logs',category=x)

            embed = discord.Embed(title="Setup",description=f"Bot has been setted up!, use ``-accessrole[roles]``to give staff access to the channel.Check out more information and configurations with ``-help``.",color=0x1793FC)
            await ctx.send(embed=embed)
    

    @commands.command()
    async def access(self,ctx,arg): 
        file = open("setup_data.json")
        json.load(arg)
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
