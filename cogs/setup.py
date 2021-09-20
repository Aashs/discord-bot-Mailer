import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def setup(self, ctx):
        all_channels = []
        for channel in ctx.guild.text_channels:
                all_channels.append(channel.id)
             
        
        for i in all_channels:
            channel = self.bot.get_channel(i)
            category_exists = False
            channel_exists = False
            if channel.name == 'Mailer-logs':
                channel_exists = True
            if category_exists == 'Mailer':
                category_exists = True

        if category_exists and channel_exists:
            print("Category and channel exists")
        elif category_exists and channel_exists == False:
            print("Category exists but channel does not")
        else:
            print("Nothing exists. We're doomed.")
    
    #d
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
