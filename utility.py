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

# register the cog to be used
def setup(bot):
    bot.add_cog(Utility(bot))