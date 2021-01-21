#fun.py - COG for funny jokes and memes

import discord, json, requests, re, random
from urllib import request, parse
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # API request to retrieve the hottest jokes using requests and json
    @commands.command()
    async def joke(self, ctx):
        """
        Laugh at jokes.
        """
        try:
            response = requests.get('https://official-joke-api.appspot.com/random_joke')
            if response.status_code != 200:
                raise e
            else:
                # print('Successfully connected to API')
                joke_content = response.json()
                await ctx.send(f"{joke_content['setup']}\n||{joke_content['punchline']}||")
        except Exception as e:
            print('Error: Failed to retrieve API call')

    # using urllib web scraping for the freshest Cyanide and Happiness toons
    @commands.command()
    async def comic(self, ctx, page = 'random'):
        """
        Get a "random" or "latest" comic from Cyanide & Happiness.
        """
        html_content = request.urlopen('https://explosm.net/comics/')
        find_latest = re.findall('href="https://explosm.net/comics/(.{4})', html_content.read().decode())

        if page == 'random':
            rand = random.randint(39, int(find_latest[0]))
            await ctx.send('https://explosm.net/comics/' + str(rand))
        elif page == 'latest':
                await ctx.send('https://explosm.net/comics/' + find_latest[0])
        else:
            await ctx.send('Can\'t find the comic. Try \"latest\" or no arguments.')


# register the cog to be used
def setup(bot):
    bot.add_cog(Fun(bot))