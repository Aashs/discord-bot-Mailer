import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def adminlogs2(self, ctx):
        all_channels = []
        all_categories = []
        for category in ctx.guild.categories:
            all_categories.append(category)
        for channel in ctx.guild.text_channels:
                all_channels.append(channel.id)
             
        category_exists = False
        channel_exists = False
        for i in all_channels:
            channel = self.client.get_channel(i)
            if channel.name == 'mailer-logs':
                channel_exists = True
        for i in all_categories:
            if i.name == 'mailer':
                category_exists = True

        if category_exists == True and channel_exists == True:
            print("Category and channel exists")
        elif category_exists == True and channel_exists == False:
            print("Category exists but channel does not")
        elif category_exists == False and channel_exists == True:
            print("Category doesn't exist but channel does exist")
        else:
            print("Nothing exists. We're doomed.")
    
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
