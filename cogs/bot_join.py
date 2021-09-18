import discord
from discord.ext import commands

class bot_join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.create_category("Mailer")
        name = 'Mailer'
        category = discord.utils.get(guild.categories, name=name)

        await guild.create_text_channel(f'logs', category=category)

       
        
def setup(bot):
    bot.add_cog(bot_join(bot)) 
