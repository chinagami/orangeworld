# main_3.py - discord bot using extension! Now with Cogs!

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

# Start up the COGS
if __name__ == "__main__":
    for ext in config.COGS:
        try:
            bot.load_extension(ext)
            print(f'Loaded extension {ext}')
        except Exception as e:
            print(f'Failed to load extension: {ext}')

@bot.event
async def on_command_completion(ctx):
    command = ctx.command.qualified_name
    print(f"{ctx.message.author} ID: {ctx.message.author.id} executed command {config.PREFIX}{command}")

@bot.listen()
async def on_message(message):
    if message.author.bot == True:
        return

    if message.content.lower().startswith('ree'):
        num_e = len(message.content)
        ee = 'E' * num_e
        embed = discord.Embed(
            title = 'REE',
            description = f"R{ee}",
            color = 0xFF0000
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/363417628775022603.png?v=1')
        embed.set_footer(text=f"REE by {message.author} >:(")
        await message.channel.send(embed=embed)
        # await bot.process_commands(message)
    
    if message.content.lower() == ('nice'):
        await message.channel.send("``nice``")



bot.run(config.TOKEN)