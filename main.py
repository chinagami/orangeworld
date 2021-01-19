# main_3.py - discord bot using extension

import discord, random, re, os
from urllib import request, parse
from discord.ext import commands
if not os.path.isfile('config.py'):
    sys.exit("'config.py' not found! Please add config and try again")
else:
    import config


bot = commands.Bot(command_prefix=config.PREFIX, description="Test bot :)")

# Event listeners
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}') 

@bot.command()
async def ping(ctx):
    """
    Ping... pong!
    """
    await ctx.send('pong')

@bot.command()
async def comic(ctx, page = 'random'):
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

@bot.command()
async def choose(ctx, *args):
    """
    Have me choose between multiple choices.
    """
    #splits by spaces; only single words allowed as choices
    try:
        if len(args) >= 2:
            chose = random.choice(args)
            await ctx.send(f'{chose}, I choose you!')
        else:
            raise e
    except Exception as e:
        await ctx.send('Nani! Send at least 2 choices separated by spaces.')

@bot.command()
async def poll(ctx, *args):
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


@bot.listen()
async def on_message(message):
    if message.content.lower().startswith('ree'):
        num_e = len(message.content)
        ee = 'E' * num_e
        embed = discord.Embed(
            title = 'REE',
            description = f"R{ee}",
            color = 0xFF0000
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/363417628775022603.png?v=1')
        embed.set_footer(f'REE by {message.author} >:(')
        await message.channel.send(embed=embed)
        # await bot.process_commands(message)



bot.run(config.TOKEN)