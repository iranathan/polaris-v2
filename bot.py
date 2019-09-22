import discord, os, psycopg2
from utils import roblox
from utils import database
from discord.ext import commands

description = '''Bloxify help'''
bot = commands.Bot(command_prefix=['b25'], description=description, case_insensitive=True)
bot.roblox = roblox.Roblox()
bot.connection = database.Database()

@bot.event
async def on_ready():
    print('ready')

for file in os.listdir("./classes"):
    if file.endswith('.py'):
        bot.load_extension(f'classes.{file.replace(".py", "")}')

bot.run('NDcwMjc3MzI2NTIyMDIzOTQ2.XYeumw.1qfVwHPDhRYZ-p4K3BvBF7NAV5c')
