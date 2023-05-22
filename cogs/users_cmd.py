import disnake
from disnake.ext import commands

class CMDUsers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot {self.bot.user} is ready work!")

    @commands.command()
    async def profile(self, ctx):
        await ctx.reply("Привет, ты используешь команду COGS!")

def setup(bot):
    bot.add_cog(CMDUsers(bot))