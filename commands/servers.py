import asyncio
import json
import os
from datetime import datetime

from discord.ext import commands

from lib.ranks import is_vale

if os.path.isfile("serverlist.json"):
    with open('serverlist.json', encoding='utf8') as f:
        slist = json.load(f)
else:
    slist = {'servers': []}
    with open('serverlist.json', 'w+') as f:
        json.dump(slist, f, indent=4)

bot = commands.Bot(command_prefix='ng!')

botcolor = 0xffffff

bot.remove_command('help')

pass_list = [319708364051316750]


class servers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    @is_vale()
    async def gatherservers(self, ctx):
        slist = {'servers': []}
        for server in self.bot.guilds:
            Bot = list(member.bot for member in server.members if member.bot)
            user = list(member.bot for member in server.members if member.bot is False)
            member = list(member for member in server.members)
            disboard = list(member.bot for member in server.members if member.id
                            is 302050872383242240)
            dbl = list(member.bot for member in server.members if member.id
                       is 422087909634736160)
            discord_me = list(member.bot for member in server.members if member.id
                              is 476259371912003597)
            for current_servers in slist['servers']:
                if current_servers['id'] is server.id:
                    pass
            if str(len(disboard)) == "1":
                List1 = "Yes"
            else:
                List1 = "No"
            if str(len(dbl)) == "1":
                List2 = "Yes"
            else:
                List2 = "No"
            if str(len(discord_me)) == "1":
                List3 = "Yes"
            else:
                List3 = "No"
            if server.owner is None:
                slist['servers'].append({
                    'name': server.name,
                    'id': str(server.id),
                    'Server Region': str(server.region),
                    'Usercount': str(len(member)),
                    'Botcount': str(len(Bot)),
                    'Humancount': str(len(user)),
                    'Serverowner': "None",
                    'Sicherheitslevel': str(server.verification_level),
                    'Last Update': str(datetime.utcnow()),
                    'Disboard': List1,
                    'DBL': List2,
                    'Discord.me': List3
                })
            else:
                slist['servers'].append({
                    'name': server.name,
                    'id': str(server.id),
                    'Server Region': str(server.region),
                    'Usercount': str(len(member)),
                    'Botcount': str(len(Bot)),
                    'Humancount': str(len(user)),
                    'Serverowner': server.owner.name,
                    'Sicherheitslevel': str(server.verification_level),
                    'Last Update': str(datetime.utcnow()),
                    'Disboard': List1,
                    'DBL': List2,
                    'Discord.me': List3
                })
        await asyncio.sleep(1)
        with open('Nellie/serverlist.json', 'w+') as f:
            json.dump(slist, f, indent=4)
        await ctx.channel.send("Gather Servers sucessfully")

    @commands.Cog.listener()
    async def on_guild_leave(self, guild):
        slist = {'servers': []}
        for server in self.bot.guilds:
            Bot = list(member.bot for member in server.members if member.bot)
            user = list(member.bot for member in server.members if member.bot is False)
            member = list(member for member in server.members)
            disboard = list(member.bot for member in server.members if member.id
            is 302050872383242240)
            dbl = list(member.bot for member in server.members if member.id
            is 422087909634736160)
            discord_me = list(member.bot for member in server.members if member.id
            is 476259371912003597)
            for current_servers in slist['servers']:
                if current_servers['id'] is server.id:
                    pass
            if str(len(disboard)) == "1":
                List1 = "Yes"
            else:
                List1 = "No"
            if str(len(dbl)) == "1":
                List2 = "Yes"
            else:
                List2 = "No"
            if str(len(discord_me)) == "1":
                List3 = "Yes"
            else:
                List3 = "No"
            if server.owner is None:
                slist['servers'].append({
                    'name': server.name,
                    'id': str(server.id),
                    'Server Region': str(server.region),
                    'Usercount': str(len(member)),
                    'Botcount': str(len(Bot)),
                    'Humancount': str(len(user)),
                    'Serverowner': "None",
                    'Sicherheitslevel': str(server.verification_level),
                    'Last Update': str(datetime.utcnow()),
                    'Disboard': List1,
                    'DBL': List2,
                    'Discord.me': List3
                })
            else:
                slist['servers'].append({
                    'name': server.name,
                    'id': str(server.id),
                    'Server Region': str(server.region),
                    'Usercount': str(len(member)),
                    'Botcount': str(len(Bot)),
                    'Humancount': str(len(user)),
                    'Serverowner': server.owner.name,
                    'Sicherheitslevel': str(server.verification_level),
                    'Last Update': str(datetime.utcnow()),
                    'Disboard': List1,
                    'DBL': List2,
                    'Discord.me': List3
                })
        await asyncio.sleep(1)
        with open('Nellie/serverlist.json', 'w+') as f:
            json.dump(slist, f, indent=4)


def setup(bot):
    bot.add_cog(servers(bot))
