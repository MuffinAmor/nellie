'''MIT License

Copyright (c) 2021 MightyNiko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''


import asyncio
import json
import os

import discord
from discord.ext import commands

default_prefix = "n!"

intents = discord.Intents.default()
intents.reactions = True
intents.guilds = True
intents.guild_reactions = True

os.chdir(r'/')


def Lol(bot, message):
    if os.path.isfile("prefix.json"):
        with open("prefix.json") as f:
            prefixes = json.load(f)
        try:
            return prefixes.get(str(message.guild.id), default_prefix)
        except KeyError:
            return default_prefix

    else:
        prefixes = {}
        with open("prefix.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        return default_prefix


bot = commands.Bot(command_prefix=Lol, intents=intents)

TOKEN = ''

botcolor = 0xffffff

bot.remove_command('help')
########################################################################################################################

extensions = ['commands.help', 'commands.auto', 'commands.owner', 'commands.cmd', 'commands.sea',
              'commands.roo', 'commands.chat', 'commands.dbl',
              'commands.mod', 'commands.clean']


# ['commands.clean']


@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------------------')
    await status_task()


########################################################################################################################
async def status_task():
    await bot.change_presence(
        activity=discord.Activity(name='n!help', type=discord.ActivityType.watching))
    # await bot.change_presence(activity=discord.Game('working'),
    #                          status=discord.Status.idle)
    # await bot.change_presence(
    #    activity=discord.Streaming(name='1 follow = 10 Min Stream', url='https://www.twitch.tv/host_katsumi')
    # )


########################################################################################################################
@bot.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
    try:
        del prefixes[str(ctx.guild.id)]
    except KeyError:
        pass
    prefixes[ctx.guild.id] = prefix
    with open("prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send("Your Prefix has been changed to {}".format(prefix))


@bot.command()
@commands.is_owner()
async def reloadall(ctx):
    for extension in extensions:
        try:
            bot.unload_extension(extension)
            bot.load_extension(extension)
            await ctx.send("{} has been reloaded".format(extension))
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))


@bot.command()
@commands.is_owner()
async def goodnight(ctx):
    await ctx.channel.send("Sleep well")
    await bot.logout()


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        print('{} wurde geladen.'.format(extension))
        embed = discord.Embed(
            title='{} wurde geladen.'.format(extension),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    except Exception as error:
        print('{} konnte nicht geladen werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht geladen werden. [{}]'.format(extension, error),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


########################################################################################################################
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        print('{} wurde deaktiviert.'.format(extension))
        embed = discord.Embed(
            title='{} wurde deaktiviert.'.format(extension),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    except Exception as error:
        print('{} konnte nich deaktiviert werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht deaktiviert werden. [{}]'.format(extension, error),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


########################################################################################################################
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.unload_extension(extension)
        bot.load_extension(extension)
        await ctx.channel.send('{} wurde neu geladen.'.format(extension))
    except Exception as error:
        await ctx.channel.send('{} konnte nicht geladen werden. [{}]'.format(extension, error))


########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))

bot.run(TOKEN)
