# main_3.py - discord bot using extension! Change ahoy

import discord, random, re, os, json, requests
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

# Commands
@bot.command()
async def ping(ctx):
    """
    Ping... pong!
    """
    await ctx.send('pong')

# using urllib web scraping
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
    # splits by spaces; only single words allowed as choices
    try:
        if len(args) >= 2:
            chose = random.choice(args)
            await ctx.send(f'{chose}, I choose you!')
        else:
            raise e
    except Exception as e:
        await ctx.send('Nani! Send at least 2 choices separated by spaces.')

@bot.command()
async def delete(ctx, num=10):
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

# using requests and json API call
@bot.command()
async def joke(ctx):
    """
    Laugh at jokes.
    """
    try:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        if response.status_code != 200:
            raise e
        else:
            # print('Successfully connected to API')
            pass
    except Exception as e:
        print('Error: Failed to retrieve API call')

    joke_content = response.json()
    await ctx.send(f"{joke_content['setup']}\n||{joke_content['punchline']}||")

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