from discord.ext import commands
import discord
import requests

class Image(commands.Cog):
    """shows images"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="food", help="Shows food")
    async def get_random_comida(self, ctx):
        response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        data = response.json()
        url_title = data["meals"][0]["strMeal"]
        url_image = data["meals"][0]["strMealThumb"]
        url_description = data["meals"][0]["strInstructions"]

        embed = discord.Embed(
            title= url_title,
            description=url_description,
            color = 0x000000,
        )

        embed.set_author(name=self.bot.user.name)
        embed.set_image(url=url_image)

        await ctx.send(embed=embed)

    @commands.command(name="capybara", help="Shows capybaras")
    async def get_random_capivara(self, ctx):
        response = requests.get("https://api.capy.lol/v1/capybara?json=true")
        data = response.json()
        url_image = data["data"]["url"]

        embed = discord.Embed(
            title= "Imagem",
            description="",
            color = 0x000000,
        )

        embed.set_author(name=self.bot.user.name)
        embed.set_image(url=url_image)

        await ctx.send(embed=embed)

    @commands.command(name="dog", help="Shows dogs")
    async def get_random_cachorro(self, ctx):
        response = requests.get("https://api.thedogapi.com/v1/images/search")
        data = response.json()
        value = data[0]
        url_image = value.get("url")

        embed = discord.Embed(
            title= "Imagem",
            description="",
            color = 0x000000,
        )

        embed.set_author(name=self.bot.user.name)
        embed.set_image(url=url_image)

        await ctx.send(embed=embed)

    @commands.command(name="kitten", help="Shows kittens")
    async def get_random_cats(self, ctx):
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        value = data[0]
        url_image = value.get("url")

        embed = discord.Embed(
            title= "Imagem",
            description="",
            color = 0x000000,
        )

        embed.set_author(name=self.bot.user.name)
        embed.set_image(url=url_image)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Image(bot))
