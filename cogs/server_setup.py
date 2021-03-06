import asyncio
import discord
from discord.ext import commands
import json

class server_setup(commands.Cog):

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
            category = await ctx.guild.create_category('Mailer')
            self.bot.logs_channel = await ctx.guild.create_text_channel('mailer-logs',category=category)
            print('channel made')

            embed = discord.Embed(title="Setup",description=f"Bot has been setted up!, use ``-accessrole[roles]``to give staff access to the channel.Check out more information and configurations with ``-help``.",color=0x1793FC)
            await ctx.send(embed=embed) 



    @commands.command()
    async def access(self,ctx,*,roles:discord.Role):
        rls=[]
        for x in roles.split(" "):
            rls.append(x)
        with open("./DataBase/setup_data.json", "r") as file:
            data0 = json.load(file)
        data0[ctx.guild.id]=rls
        with open("./DataBase/setup_data.json", "w") as f:
            json.dump(data0,f,indent=4)
        await ctx.send(f"Gave Access to {r.mention for r in rls}")

    
    @commands.command()
    async def send_data(self,ctx,loop_time:int =None):
        try:
            i=0
            if loop_time is None:
                await ctx.author.send(file="setup_data.json");return
            while True:
                await ctx.author.send(f"File Sent on loop of this [message]({ctx.message.jump_url})\n Loop {i+1}",file=discord.File("setup_data.json"));return
                i=+1
            await asyncio.sleep(loop_time*3600)
        except Exception as e:await ctx.send(f"An Error Occured!! {e}")
        
        
    @commands.command()
    async def send_file(self,ctx,file):
        try:
            file = f"./{file}"
            await ctx.author.send(file=discord.File(file))
        except Exception as e:
            if isinstance(error,FileNotFound):
                await ctx.send("No Such FIle or Dir Exists")
            else:await ctx.send(f"ERROR: {error}")
            
def setup(bot):
    bot.add_cog(server_setup(bot)) 
