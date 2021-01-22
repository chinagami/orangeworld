#fun.py - COG for funny jokes and memes

import discord, requests, re, random
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
    async def comic(self, ctx, page):
        """
        Get the latest, random or specific Cyanide & Happiness comics.
        """
        html_content = request.urlopen('https://explosm.net/comics/latest')
        find_latest = re.findall('href="https://explosm.net/comics/(.{4})', html_content.read().decode())[0]

        # if the argument is an integer you can grab the page
        try:
            page = int(page)
        except:
            pass

        if isinstance(page, int) and page <= int(find_latest):
            await ctx.send('https://explosm.net/comics/' + str(page))
        elif isinstance(page, str):
            try:
                if page == 'random':
                    rand = random.randint(39, int(find_latest))
                    await ctx.send('https://explosm.net/comics/' + str(rand))
                elif page == 'latest':
                        await ctx.send('https://explosm.net/comics/' + find_latest)
                else:
                    await ctx.send('Can\'t find the comic. Try again')
            except IndexError as e:
                print("Error: Index out of range")
                await ctx.send('Can\'t find the comic. Try again.')
        else:
            await ctx.send('Can\'t find the comic. Try again.')

# register the cog to be used
def setup(bot):
    bot.add_cog(Fun(bot))