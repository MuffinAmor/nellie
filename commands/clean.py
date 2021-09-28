import json
import os
from time import time

from discord.ext import commands

os.chdir(r'/')


class CleaningClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def clean(self, ctx):
        list_json = os.listdir("/rooms")
        for i in list_json:
            with open(f"rooms/{i}", encoding='utf-8') as fp:
                data = json.load(fp)
            for channel_id in data['cid']:
                channel = self.bot.get_channel(channel_id)
                if not channel:
                    data['cid'].remove(channel_id)
                    print(f"{channel_id} has been removed from {i}")
            with open(f"rooms/{i}", "w+") as fp:
                json.dump(data, fp, indent=4)
            print("Clean Channel")

            tokens = []
            for token in data['pics']:
                stamp = data['pics'][token]['time']
                t = round(time() - float(stamp))
                if t < 604800:
                    tokens.append(token)

            for x in tokens:
                del data['pics'][x]
                print(f"{str(x)} has been removed from {i}")
            with open(f"rooms/{i}", "w+") as fp:
                json.dump(data, fp, indent=4)

            print("Clean Pics")

            user_list = []
            for users in data['users']:
                user = self.bot.get_user(int(users))
                if not user:
                    user_list.append(users)

            for y in user_list:
                del data["users"][y]
                print(f"{y} has been removed from {i}")
            with open(f"rooms/{i}", "w+") as fp:
                json.dump(data, fp, indent=4)
            print(f"Clean Users, {i}")
        print("Clean Done")


def setup(bot):
    bot.add_cog(CleaningClass(bot))
