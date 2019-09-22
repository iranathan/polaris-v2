import discord
from discord.ext import commands
import psycopg2


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = bot.connection
        self.cursor = self.connection.cursor()

    def verify(self, ctx, username=None):
        roblox_id = int
        if not username:
            await ctx.send('What is your username?')
            msg = await bot.wait_for('message', check=lambda m: m.channel.id == ctx.channel.id and m.author.id == ctx.author.id)
            username = msg.content

        if not await self.bot.roblox.is_user_username(username):
            return await ctx.send('That is not a user.')
        roblox_id = self.bot.id_by_username(username)
        await ctx.send(str(roblox_id))

def setup(bot):
    bot.add_cog(Verification(bot))
