import discord
from discord.ext import tasks, commands
import os

bot = commands.Bot(command_prefix='-',intents = discord.Intents.all())

TOKEN = os.getenv('TOKEN')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Done')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')   
    await ctx.send('Done')
    

@bot.command()
async def latency(ctx):
    await ctx.send(f'{round(self.bot.latency * 1000)}ms')
  
@bot.event
async def on_ready():
    print('Bot is ready!')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
