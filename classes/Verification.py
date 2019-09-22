import discord
from discord.ext import commands
import psycopg2


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = bot.connection

    # TODO: add database check
    @commands.command()
    async def verify(self, ctx, username=None):
        roblox_id = int
        if not username:
            await ctx.send('What is your username?')
            msg = await self.bot.wait_for('message', check=lambda m: m.channel.id == ctx.channel.id and m.author.id == ctx.author.id, timeout=200)
            username = msg.content
        if not await self.bot.roblox.is_user_username(username):
            return await ctx.send(f'Sorry, We where unable to find the user `{username}` on ROBLOX.')
        roblox_id = await self.bot.roblox.id_by_username(username)
        code = await self.bot.roblox.code()
        example = discord.File('./images/yess.png')
        await ctx.send(f'<a:loading:482743944078163968> Please put `{code}` as your **ROBLOX** status or blurb, and then say done', file=example)
        msg = await self.bot.wait_for('message', check=lambda m: m.channel.id == ctx.channel.id and m.author.id == ctx.author.id and m.content.lower() == 'done', timeout=200)
        if msg.content.lower() == 'done': # I know this will always be true but if i have everything on the same line its ugly code.
            status = await self.bot.roblox.status(roblox_id)
            if code in status:
                edit = await ctx.send(f'✅ We have found the words in your profile we are now adding `{username}` to our database.')
                self.connection.add_user(ctx.author.id, roblox_id, username)
                await edit.edit(content=f'✅ You have been verified with the roblox account {username}')
            else:
                await ctx.send(':x: We could not find the words in your profile.')


def setup(bot):
    bot.add_cog(Verification(bot))
