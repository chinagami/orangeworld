# utility.py - COG for basic commands

import discord, random, re
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Ping and pong!"""
        await ctx.send('pong')

    @commands.command()
    async def delete(self, ctx, num=10):
        """
        Delete a number of messages.
        """
        # TODO: catch non-integer arguments in function call
        try:
            if isinstance(num, int) and num <= 10:
                message_list=[]
                messages = await ctx.channel.history(limit=num).flatten()
                for msg in messages:
                    messages_id = re.search('\d{18}', str(msg)).group()
                    message_list.append(messages_id)
                # print(message_list)
                for msg in message_list:
                    msg_obj = await ctx.channel.fetch_message(msg)
                    await msg_obj.delete()
                await ctx.send(f'Deleted {num} messages...')
            else:
                await ctx.send('Please enter a number and is less than 10.')
        except Exception as e:
            print('Error')

# register the cog to be used
def setup(bot):
    bot.add_cog(Utility(bot))