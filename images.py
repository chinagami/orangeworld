# images.py - COG for image retrieval

import discord, json, requests
from urllib import request, parse
from discord.ext import commands

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # neko bot
    @commands.command()
    async def neko(self, ctx, pic):
        """
        neko, kitsune, pat, hug, waifu, cry, kiss, slap, smug, punch
        """
        try:    
            response = requests.get("https://neko-love.xyz/api/v1/" + pic)
            if response.status_code != 200:
                raise e
            else:
                neko_content = response.json()
                await ctx.send(neko_content['url'])
        except Exception as e:
            print(f'Error with {ctx.command}')

    @commands.command()
    async def dog(self, ctx):
        """Adopt a dog!"""
        try:
            response = requests.get("https://random.dog/woof.json")
            if response.status_code != 200:
                raise e
            else:
                dog_content = response.json()
                await ctx.send(dog_content['url'])
        except Exception as e:
            print(f"Error with {ctx.command}")

# register the cog to be used
def setup(bot):
    bot.add_cog(Images(bot))