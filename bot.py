import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
import logging

logging.basicConfig(filename='bot.log', level=logging.INFO)

bot = commands.Bot("!", intents=discord.Intents.all())

async def load_cogs(bot):
    await bot.load_extension('manager')

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f'commands.{cog}')

load_dotenv()
TOKEN = os.getenv('TOKEN')

async def main():
    try:
        async with bot:
            await load_cogs(bot)
            await bot.start(TOKEN)
    except Exception as e:
        logging.exception(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())


