import aiohttp
import discord


async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"Hey yo,{interaction.user.mention}")


async def neko(interaction: discord.Integration):
    url = 'https://api.waifu.pics/sfw/neko'
    data = await fetch_json(url)
    url = data['url']
    await interaction.response.send_message(url)


async def waifu(interaction: discord.Integration):
    url = 'https://api.waifu.pics/sfw/waifu'
    data = await fetch_json(url)
    url = data['url']
    await interaction.response.send_message(url)


async def shinobu(interaction: discord.Integration):
    url = 'https://api.waifu.pics/sfw/shinobu'
    data = await fetch_json(url)
    url = data['url']
    await interaction.response.send_message(url)


async def megumin(interaction: discord.Integration):
    url = 'https://api.waifu.pics/sfw/megumin'
    data = await fetch_json(url)
    url = data['url']
    await interaction.response.send_message(url)


async def say(interaction: discord.Integration, describe: str):
    await interaction.response.send_message(f"{interaction.user.mention} said: `{describe}`")


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data