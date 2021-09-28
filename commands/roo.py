import asyncio
from datetime import datetime

import discord
from discord.ext import commands

from lib.general import prefix, get_token
from lib.ranks import mod_right_here
from lib.room import is_connected, name_check, function_room, function_roles_room, is_owner, function_users


class RoomOwner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed = False

    @commands.command()
    async def create_role(self, ctx, *args: str):
        if ctx.message.author.bot is False:
            request_owner = is_owner(ctx.author.id)
            if request_owner:
                role = ' '.join(args)
                roles = function_room(request_owner, 'request', 'roles')
                if roles and role in roles:
                    await ctx.send("Role exist already")
                else:
                    function_roles_room(request_owner, 'create', role)
                    await ctx.send("Role has been created")
            else:
                await ctx.send("You are not the Chatroomowner")

    @commands.command()
    async def delete_role(self, ctx, *args: str):
        if ctx.message.author.bot is False:
            request_owner = is_owner(ctx.author.id)
            if request_owner:
                role = ' '.join(args)
                roles = function_room(request_owner, 'request', 'roles')
                if roles and role not in roles:
                    await ctx.send("Role not exist.")
                else:
                    function_roles_room(request_owner, 'delete', role)
                    await ctx.send("Role has been deleted")

    @commands.command()
    async def show_roles(self, ctx):
        if ctx.message.author.bot is False:
            request_owner = is_owner(ctx.author.id)
            if request_owner:
                roles = function_room(request_owner, 'request', 'roles')
                if roles:
                    liste = []
                    for i in roles:
                        liste.append(i)
                    output = "\n".join(liste)
                else:
                    output = "No Custom Roles."
                embed = discord.Embed(title="Custom Roles",
                                      description=output)
                await ctx.send(embed=embed)

    @commands.command()
    async def add_role(self, ctx, user: discord.User, role: str):
        request_owner = is_owner(ctx.author.id)
        if request_owner:
            roles = function_room(request_owner, 'request', 'roles')
            if roles and role in roles:
                request_role = function_users(request_owner, 'request', str(user.id), 'roles')
                if request_role:
                    await ctx.send(f"The User **{user}** owns already a Role.\n"
                                   f"Please remove this one first.")
                else:
                    function_users(request_owner, 'role_set', str(user.id), role)
                    await ctx.send(f"The User **{user}** has become the Role: **{role}**.")
            else:
                await ctx.send("The Role not exist in your Chatroom.")
        else:
            await ctx.send("You are not the Owner of the Chatroom.")

    @commands.command()
    async def remove_role(self, ctx, user: discord.User):
        request_owner = is_owner(ctx.author.id)
        if request_owner:
            roles = function_room(request_owner, 'request', 'roles')
            if roles:
                request_role = function_users(request_owner, 'request', str(user.id), 'roles')
                if not request_role:
                    await ctx.send(f"The User **{user}** does not have a Role.")
                else:
                    function_users(request_owner, 'role_remove', str(user.id))
                    await ctx.send(f"You have removed the Role **{request_role}** from **{user}**")
            else:
                await ctx.send("The Role not exist in your Chatroom.")
        else:
            await ctx.send("You are not the Owner of the Chatroom.")

    @commands.command()
    async def edit_color(self, ctx, *args: str):
        if ctx.message.author.bot is False:
            request_owner = is_owner(ctx.author.id)
            if request_owner:
                role, new_data = ' '.join(args).split(",")
                if role and new_data:
                    function_roles_room(request_owner, 'edit', role, 'color', new_data.replace("#", "0x"))
                    await ctx.send("The Color has been edit.")
            else:
                await ctx.send("You are not the Owner of the Chatroom.")

    @commands.command()
    async def owner_transfer(self, ctx, member: discord.Member):
        if ctx.message.author.bot is False:
            request_member = is_owner(member.id)
            request_owner = is_owner(ctx.author.id)
            if request_owner:
                if request_member:
                    await ctx.send("The tagged Member owns already a Chatroom.")
                else:
                    token = get_token(16)
                    passphrase = ""
                    passphrase += token
                    await ctx.send("Please enter Passphrase")
                    try:
                        await ctx.author.send(token)
                    except discord.Forbidden:
                        await ctx.send("I am not able to send you the Key.\n"
                                       "Please open your Direct Messages.")
                    else:

                        def pred(m):
                            return m.author == ctx.author and m.channel == ctx.channel

                        try:
                            message = await self.bot.wait_for('message', check=pred, timeout=120.0)
                        except asyncio.TimeoutError:
                            await ctx.send('Ups, you waited to long.')
                        else:
                            if message.content == passphrase:
                                function_room(request_owner, 'edit', 'owner', str(member.id))
                                await ctx.send(f"Yay, {member} owns {request_owner} now!")
            else:
                await ctx.send("You do not own a Chatroom")

    @commands.command()
    async def delroom(self, ctx, *args: str):
        if not ctx.message.author.bot:
            name = '_'.join(args)
            current = prefix(str(ctx.author.guild.id))
            owner = function_room(name, 'request', 'owner')
            if name == "":
                await ctx.send("You forgot to insert the Chat-room name.\n"
                               "How to use delroom:\n"
                               "`{}delroom #Neko Dev. Army³\n"
                               "*³The Name of the Chatroom that you like delete.`"
                               .format(current))
                return
            elif owner != ctx.author.id:
                await ctx.send("Only the Roomowner can delete the Chatroom")
            else:
                function_room(name, 'delete')
                embed = discord.Embed(title="Room deleted",
                                      description="Your Chat-room **{}** has been deleted.".format(name),
                                      color=ctx.author.color)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.timestamp = datetime.utcnow()
                await ctx.channel.send(embed=embed)
                RoomChannels = function_room(name, 'request', 'cid')
                if RoomChannels:
                    for i in RoomChannels:
                        channel = self.bot.get_channel(int(i))
                        if channel:
                            await channel.edit(topic=None)

    @commands.Cog.listener()
    async def on_message(self, message):
        current = prefix(str(message.guild.id))
        if message.content.startswith(current):
            room_with_id = message.content.replace(current, "")

            lst = [room_with_id]
            vale = lst[0].split()
            number = vale.pop(-1)
            chat_name = '_'.join(vale)

            if chat_name and name_check(chat_name):
                if not number:
                    await message.channel.send(
                        "Heyo, i see you have forgot to insert the channel-id for the linked channel :eyes: ...\n"
                        "Please try again and insert one.\n"
                        "How to use add 101:\n"
                        "`{}add 636702313758851102² #Neko Dev. Army³\n"
                        "*² the ID of the Channel which you would like add,\n"
                        "*³The Name of the Chat-room that you like add the Channel.`".format(current))
                    return
                try:
                    int(number)
                except TypeError:
                    await message.channel.send(
                        "Heyo, i see you have forgot to insert the channelid for the linked channel :eyes: ...\n"
                        "Please try again and insert one.\n"
                        "How to use add 101:\n"
                        "`{}add 636702313758851102² #Neko Dev. Army³\n"
                        "*² the ID of the Channel which you would like add,\n"
                        "*³The Name of the Chatroom that you like add the Channel.`".format(current))
                    return
                if not len(str(number)) == 18:
                    await message.channel.send(
                        "Heyo, i see you have forgot to insert the channelid for the linked channel :eyes: ...\n"
                        "Please try again and insert one.\n"
                        "How to use add 101:\n"
                        "`{}add 636702313758851102² #Neko Dev. Army³\n"
                        "*²The ID of the Channel which you would like add,\n"
                        "*³The Name of the Chatroom that you like add the Channel.`".format(current))
                    return
                else:
                    channel_id = int(number)
                    connect = is_connected(channel_id, 'cid')
                    if connect:
                        await message.channel.send(
                            "I am sorry, The Command channel is allready linked with a other Chat.")
                        return
                    else:
                        msg = await message.channel.send("Please give me a moment, i will check something...")
                        channel2 = self.bot.get_channel(channel_id)
                        if channel2 is None:
                            await message.channel.send("I can't find the ID Channel, i am sorry.")
                        else:
                            owner = is_owner(message.author.id)
                            print(owner)
                            if message.author.id == 474947907913515019:
                                self.allowed = True
                            if owner and owner == chat_name:
                                self.allowed = True
                            else:
                                public = function_room(chat_name, 'request', 'open')
                                if public:
                                    for s in self.bot.guilds:
                                        for c in s.channels:
                                            if c == channel2:
                                                admins = list(
                                                    user for user in s.members if
                                                    user.guild_permissions.administrator)
                                                if message.author in admins:
                                                    self.allowed = True
                                                    break
                                else:
                                    self.allowed = False
                    topic = function_room(chat_name, 'request', 'topic')
                    await asyncio.sleep(3)
                    if self.allowed is True:
                        if channel2 is None:
                            embed = discord.Embed(title="I am sorry",
                                                  description="Chat is outside of my Range",
                                                  color=message.author.color)
                            embed.add_field(name='I have no access to the Channel',
                                            value='Please check if i have access to the Channel or it even exist')
                            embed.set_thumbnail(url=self.bot.user.avatar_url)
                            embed.set_footer(text=message.guild.name, icon_url=message.guild.icon_url)
                            embed.timestamp = datetime.utcnow()
                            await msg.edit(embed=embed)
                        elif is_connected(int(channel_id), 'cid'):
                            embed = discord.Embed(title="I am sorry",
                                                  description="Your choosed channel is already linked with a other "
                                                              "Chat.",
                                                  color=message.author.color)
                            embed.add_field(name='This Channel is allready linked',
                                            value='Ask the Groupowner of this chatgroup if you can join them with '
                                                  'ng!add '
                                                  '*channelid* *groupname*')
                            embed.set_thumbnail(url=self.bot.user.avatar_url)
                            embed.set_footer(text=message.guild.name, icon_url=message.guild.icon_url)
                            embed.timestamp = datetime.utcnow()
                            await msg.edit(embed=embed)
                        else:
                            function_room(chat_name, 'append', int(channel_id))
                            try:
                                if topic is None:
                                    await channel2.edit(
                                        topic="Chatgroup: {} | powered by: {}".format(chat_name,
                                                                                      self.bot.user.mention))
                                elif topic:
                                    await channel2.edit(topic="Chatgroup: {} | {}".format(chat_name, topic))
                            except PermissionError:
                                await message.channel.send(
                                    "Heyo, it looks like, i have not the permissions to edit the Channel-topic of {}.\n"
                                    "Please add **Manage Channels** to my Permissions and try again.".format(
                                        channel2))
                                return
                            embed = discord.Embed(title="Welcome in the Network",
                                                  description="You have been added the Channel **{}** to the Chatgroup"
                                                              "**{}**".format(channel2, chat_name),
                                                  color=message.author.color)
                            embed.add_field(name=':warning:Attention:warning:',
                                            value='Your Chatgroupname get setted in all Channels as the Topic.\n'
                                                  'When you remove or edit it, it  is  possible that the Chat doesn´t '
                                                  'work anymore')
                            embed.set_thumbnail(url=message.guild.icon_url)
                            embed.set_footer(text=message.guild.name, icon_url=message.guild.icon_url)
                            embed.timestamp = datetime.utcnow()
                            await message.channel.send(embed=embed)
                            if message.channel is not channel2:
                                await channel2.send(embed=embed)

                    else:
                        await msg.edit(
                            content="Ohaa, it looks like you haven´t enough permissions to add to this Channel\n"
                                    "You need Administrator Permissions on all Channel Server that you like "
                                    "add ^^")

    @commands.command()
    async def add_mod(self, ctx, member: discord.Member = None):
        if not ctx.message.author.bot:
            MemberId = member.id
            name = is_owner(ctx.author.id)
            if name is False:
                await ctx.send("You are not the Owner of a Chatroom!")
            else:
                if member is None:
                    await ctx.send("Please choose a User that you would like add as mod.")
                elif mod_right_here(name, MemberId):
                    await ctx.send('The User **{}** is allready in the Database as Mod'.format(member.name))
                else:
                    function_room(name, 'append_mod', MemberId)
                    await ctx.send('The User **{}** has been added as Mod in **{}**'.format(member.mention, name))

    @commands.command()
    async def remove_mod(self, ctx, user_id: int = None):
        if not ctx.message.author.bot:
            if user_id is None:
                await ctx.send("Please choose a User that you would like remove as mod.")
            else:
                MemberId = user_id
                name = is_owner(ctx.author.id)
                if not name:
                    await ctx.send("You are not the Owner of a Chatroom!")
                else:
                    if not name:
                        await ctx.send("Its looks like you don't own a Chatroom.")
                    elif not mod_right_here(name, str(MemberId)):
                        await ctx.send("The User is not set as mod.")
                    else:
                        function_room(name, 'remove_mod', MemberId)
                        await ctx.send('The User {} has been removed as Mod'.format(user_id))

    @commands.command()
    async def showmod(self, ctx, *args: str):
        if not ctx.message.author.bot:
            name = '_'.join(args)
            mods = function_room(name, 'request', 'mods')
            if name == "":
                await ctx.send("Please try again and write a valid Groupname from that you like know the Mods")
            else:
                n = ""
                for a in mods:
                    member = self.bot.get_user(int(a))
                    if member:
                        n += '{} | {}\n'.format(member.name, member.id)
                    else:
                        n += '{}\n'.format(a)
                embed = discord.Embed(title="{} MODs:".format(name), description=n, color=ctx.author.color)
                embed.timestamp = datetime.utcnow()
                await ctx.channel.send(embed=embed)

    @commands.command()
    async def roomsetup(self, ctx, *args: str):
        if ctx.message.author.bot is False:
            name = '_'.join(args)
            owner = function_room(name, 'request', 'owner')
            if name == "":
                await ctx.send("You need to write the name of the Chatroom which you like setup. Please try again!")
            elif not ctx.author.id == owner:
                await ctx.send("Please create a Chatroom before you do any settings.")
            else:
                await ctx.send("───────────────────────────────────────────────────────────")
                await asyncio.sleep(3)
                await ctx.send("Welcome to the Chatroomsetup for **{}**\n"
                               "Please write in which Language your Chatroom is.\n"
                               "You have 20 seconds time and 15 Characters for this field.\n"
                               "When you like skip this setting type *skip*\n"
                               "1/4".format(name))

                def check(m):
                    return m.channel is ctx.channel and m.author is ctx.author

                while True:
                    try:
                        msg = await self.bot.wait_for('message', check=check, timeout=20)
                    except asyncio.TimeoutError:
                        await ctx.send('You took too long...')
                        break
                    if len(msg.content) > 16:

                        await ctx.send(
                            "Too long, please try again. You have 20 seconds and 15 Characters for this field.\n"
                            "When you like skip this setting type *skip*")
                        continue
                    elif msg.content == "skip":
                        await ctx.send("Language skipped")
                        break
                    else:
                        function_room(name, 'edit', 'lang', msg.content[0:15])
                        await ctx.send("The Language from **{}** has been set to **{}**.".format(name, msg.content))
                        break
                await ctx.send("───────────────────────────────────────────────────────────")
                await asyncio.sleep(3)
                await ctx.send("The next point of my list is the Chatroom-Topic.\n"
                               "You have 60 seconds and 50 Characters for this field.\n"
                               "When you don´t like set a topic, write: None")
                while True:
                    try:
                        msg = await self.bot.wait_for('message', check=check, timeout=60)
                    except asyncio.TimeoutError:
                        await ctx.send('You took too long...')
                        break
                    if len(msg.content) > 51:
                        await ctx.send("Too long, please try again.\n"
                                       "You have 60 seconds and 50 Characters for this field.\n"
                                       "When you don´t like set a topic, write: None")
                        continue
                    elif msg.content == "skip":
                        await ctx.send("Topic skipped")
                        break
                    else:
                        function_room(name, 'edit', 'topic', msg.content[0:50])
                        await ctx.send(
                            "The Chatroom-topic from **{}** has been set to **{}**.".format(name, msg.content))
                        break
                await ctx.send("───────────────────────────────────────────────────────────")
                await asyncio.sleep(3)
                await ctx.send(
                    "You like allow the Chatroom User to send Pictures in the Chat? Write **Yes** or Yeah and **No** "
                    "for No.\n "
                    "You have 20 seconds.\n"
                    "When you like skip this setting type *skip*\n"
                    "2/4")
                while True:
                    try:
                        msg = await self.bot.wait_for('message', check=check, timeout=20)
                    except asyncio.TimeoutError:
                        await ctx.send('You took too long...')
                        break
                    if "Yes" == msg.content:
                        function_room(name, 'edit', 'pictures', True)
                        await ctx.send("You allow the Chatroom User to send Pictures in the Chat.")
                        break
                    elif "skip" == msg.content:
                        await ctx.send("Media setting skipped.")
                        break
                    elif "No" == msg.content:
                        function_room(name, 'edit', 'pictures', False)
                        await ctx.send("You not allow the Chatroom User to send Pictures in the Chat.")
                        break
                    else:
                        await ctx.send(
                            "Ops, wrong input. Write **Yes** or Yeah and **No** for No.\n"
                            "You have 20 seconds.\n"
                            "When you like skip this setting type *skip*")
                        continue
                await ctx.send("───────────────────────────────────────────────────────────")
                await asyncio.sleep(3)
                await ctx.send(
                    "Please send now the description for your Chatroom.\n"
                    "You have 120 seconds time and 500 Characters for this field.\n"
                    "When you like skip this setting type *skip*\n"
                    "3/4")
                while True:
                    try:
                        msg = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        await ctx.send('You took too long...')
                        break
                    if len(msg.content) > 501:
                        await ctx.send(
                            "Too long, please try again. You have 120 seconds and 500 Characters for this "
                            "field.\nWhen you like skip this setting type *skip*")
                        continue
                    elif "skip" == msg.content:
                        await ctx.send("Description setting skipped.")
                        break
                    else:
                        function_room(name, 'edit', 'desc', msg.content[0:500])
                        await ctx.send("The Description from **{}** has been setted to:\n"
                                       "**{}**".format(name, msg.content[0:500]))
                        break
                await ctx.send("───────────────────────────────────────────────────────────")
                await asyncio.sleep(3)
                while True:
                    if len(function_room(name, 'request', 'cid')) > 10:
                        await ctx.send("Do you like set your Chatroom as public?\n"
                                       "Type *yes* for yeah or *no* for no\n"
                                       "You have 20 seconds\n"
                                       "When you like skip this setting type *skip* .4/4")
                        while True:
                            try:
                                msg = await self.bot.wait_for('message', check=check, timeout=20)
                            except asyncio.TimeoutError:
                                await ctx.send('You took too long...')
                                break
                            if "yes" == msg.content:
                                function_room(name, 'edit', 'open', True)
                                await ctx.send("Your Chatroom has been set as public. Gratulation.")
                                break
                            elif "no" == msg.content:
                                function_room(name, 'edit', 'open', False)
                                await ctx.send("You have remove the Public status from your Chatroom.")
                                break
                            elif "skip" == msg.content:
                                await ctx.send("Public setting skipped.")
                                break
                            else:
                                await ctx.send(
                                    "Ops! Invalid input, please write *yes* for yeah or *no* for no\n"
                                    "You have 20 seconds\n"
                                    "When you like skip this setting type *skip*")
                                continue
                        break
                    else:
                        break
            await ctx.send("Setup finish")
            topic = function_room(name, 'request', 'topic')
            cid = function_room(name, 'request', 'cid')
            if not topic == "None":
                for cid in cid:
                    channel = self.bot.get_channel(int(cid))
                    if channel:
                        try:
                            await channel.edit(topic="Chatgroup: {} | {}".format(name, topic))
                        except PermissionError:
                            pass


def setup(bot):
    bot.add_cog(RoomOwner(bot))
