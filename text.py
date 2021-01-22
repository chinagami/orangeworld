# text.py - COG for text based stuff

import discord, random, re, requests
from urllib import request
from discord.ext import commands

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *args):
        """
        Ask a question and vote on it.
        """
        poll_title = " ".join(args)
        embed = discord.Embed(
            title = "A new poll has been created!",
            description = f"{poll_title}",
            color = 0x00C997
        )
        embed.set_footer(
            text=f"Poll created by: {ctx.message.author} • React to vote!"
        )
        embed_message = await ctx.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")

    @commands.command()
    async def choose(self, ctx, *args):
        """
        Have the bot choose between multiple choices.
        """
        # splits by spaces; only single words allowed as choices
        try:
            if len(args) >= 2:
                chose = random.choice(args)
                await ctx.send(f'{chose}, I choose you!')
            else:
                raise e
        except Exception as e:
            await ctx.send('Nani! Send at least 2 choices separated by spaces.')

    @commands.command()
    async def urban(self, ctx, *args):
        """Urban dictionary that sh*t"""
        search = " ".join(args)
        # print(f"search keyword is: {search}")
        try:
            response = requests.get(f'http://api.urbandictionary.com/v0/define?term={search}')
            if response.status_code != 200:
                raise e
            else:
                # print('Successfully connected to API')
                urban_content = response.json()
        except Exception as e:
            print('Error: Failed to retrieve API call')

        definition = urban_content['list'][0]['definition']
        example = urban_content['list'][0]['example']
        link = urban_content['list'][0]['permalink']

        embed = discord.Embed(
            title = search,
            color = 0xE66700,
            url = link
        )
        embed.add_field(
            name="Definition:", 
            value=definition, 
            inline=False)
        embed.add_field(
            name="Example:", 
            value=example, 
            inline=True)
        embed.set_footer(
            text = f"Searched by: {ctx.message.author}"
        )

        embed_message = await ctx.send(embed=embed)

# register the cog to be used
def setup(bot):
    bot.add_cog(Text(bot))