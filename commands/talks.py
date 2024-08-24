from discord.ext import commands

class Talks(commands.Cog):
    """talks with user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ola", help="greets you")
    async def hello(self, ctx):
        name = ctx.author.mention
        response = "Olá, " + name
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(Talks(bot))

