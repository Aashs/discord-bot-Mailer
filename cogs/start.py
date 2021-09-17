import discord
from discord.ext import commands

class Start(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
      if ctx.guild is None and not ctx.author.bot:
        print(ctx.content)  
        print(ctx.author) 

        embed = discord.Embed(title="Confirm Mail creation",description="This system is used for reporting bugs,reports concerning to the moderators.",color=0x3DFD1E)
        embed.set_footer(text=f"Respond with yes or no")
  
        message=await ctx.author.send(embed=embed)
    
        def check(msg):
            return ctx.author == ctx.author
        
        message = await self.bot.wait_for('message', check=check)
        content = message.content
        
        if content == 'yes':
            await ctx.author.send('Ticket created')
            
        if content == 'no':
            await ctx.author.send('Cancelled')

def setup(bot):
  bot.add_cog(Start(bot)) 
