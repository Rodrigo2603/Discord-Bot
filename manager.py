from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """manager"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Conectado como... {self.bot.user}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("O comando não está completo")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite !help para ver todos os comandos")
        else:
            raise error
        
async def setup(bot):
    await bot.add_cog(Manager(bot))
