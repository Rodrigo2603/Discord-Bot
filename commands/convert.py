from discord.ext import commands
import requests

class Convert(commands.Cog):
    """Convert coins"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="convert", help="You can compare two coins, e.g.: !convert USD BRL ")
    async def ConverterMoeda(self, ctx, coin1, coin2):
        try:
            response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{coin1.upper()}-{coin2.upper()}")
            data = response.json()
            value = data[f'{coin1.upper()}{coin2.upper()}']
            highprice = value.get("high")
            lowprice = value.get("low")

            if (highprice or lowprice):
                await ctx.send(f"O valor máximo/mínimo da moeda {coin1} para a moeda {coin2} foi de: {highprice}/{lowprice}")
            else:
                await ctx.send(f"Não foi possível retornar o valor pois há uma ou mais moedas inválidas") 
        except Exception as error:
            await ctx.send("Não foi possível acessar o servidor, tente novamente mais tarde!")
            print(error)

async def setup(bot):
    await bot.add_cog(Convert(bot))
