import discord, os, psycopg2
from discord.ext import commands

description = '''Bloxify help'''
bot = commands.Bot(command_prefix=['b!', 'b?'], description=description, case_insensitive=True)

bot.connection = psycopg2.connect(host="localhost",database="roblox", user="ira", password='iranathan')

for file in os.listdir("./classes"):
    if file.endswith('.py'):
        bot.load_extension(f'classes.{file.replace(".py", "")}')

bot.run('NDcwMjc3MzI2NTIyMDIzOTQ2.XPqNjg.sj-kvaWVd2DeQB281vjtHjNcdf0')