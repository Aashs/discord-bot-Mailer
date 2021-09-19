import discord
from discord.ext import commands

class report(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
      if not ctx.guild and not ctx.author.bot:
        print(ctx.content)  
        print(ctx.author) 
        for ctx.content == ['-report','yes','no']:
            pass
        else:
            await ctx.author.send('-report to create ticket')

    
    @commands.command()
    async def report(self,ctx):
        embed = discord.Embed(title="Confirm Mail creation",description="This system is used for reports concerning to the moderators.",color=0x3DFD1E)
        embed.set_footer(text=f"Respond with yes or no")
        
        await ctx.author.send(embed=embed)
        
        def check(msg):
            return msg.author == ctx.author
        
        message = await self.bot.wait_for('message', check=check)
        content = message.content
        
        content.lower()
        
        if content == 'yes':
            await ctx.author.send('Ticket created')
        if content == 'no':
            await ctx.author.send('Cancelled')

def setup(bot):
  bot.add_cog(report(bot)) 
