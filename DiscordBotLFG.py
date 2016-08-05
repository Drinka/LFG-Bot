import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.channel.is_private == True:
        if message.author != client.user:
            await client.send_message(message.author, "I'm sorry, but I do not work in private messages.")
            return
        else:
            return
    if "!LFG".lower() == message.content.lower():
        LFG = [x.name for x in message.author.roles]
        RLFG = discord.utils.get(message.server.roles, name='LFG')
        if message.author == client.user:
            return
        elif "LFG" in LFG:
            await client.remove_roles(message.author, RLFG)
            await client.send_message(message.channel, "%s is no longer looking for a group." % message.author.mention)

        elif "LFG" not in LFG:
            await client.add_roles(message.author, RLFG)
            await client.send_message(message.channel, "%s is now looking for a group." % message.author.mention)
        else:
            await client.send_message(message.channel, "An error has occured. If this error continues, please contact the owner of this server.")
            #If this error occurs trying restarting the bot. If it continues to occur please contact me on Reddit at "DrinkaKZ".
    if "!LFG list".lower() == message.content.lower():
        RLFG = discord.utils.get(message.server.roles, name='LFG')
        list = []
        for mem in message.server.members:
            LFGList = [y.name for y in mem.roles]
            if "LFG" in LFGList:
                list.append(mem.name)
            else:
                return
    if "!LFG create".lower() == message.content.lower():
        if message.author.permissions.administrator == True
            if message.author == client.user:
                return
            elif "LFG" in message.server.roles:
                client.send_message(message.channel, "The LFG role already exists.")
            else:
                client.create_role(message.server, name = "LFG", permissions.none)
                client.send_message(message.channel, "LFG Role created.")
        else:
            print("Error.")
        if len(list) != 0:
            await client.send_message(message.channel, "**Current users looking for a group:\n**" + "\n".join(["{0}. {1}".format(n, i) for (n, i) in enumerate(list, start=1)]))
    if ("!LFG help".lower() == message.content.lower()) or ("!LFG ?".lower() == message.content.lower()):
        await client.send_message(message.channel, "**Commands:**" + """```None of these commands are case sensitive.\n
!LFG - If you are not in the LFG group, it will add you to it. If you are already in the LFG group it will remove you from it. Note: You are automatically removed from the LFG group when you go offline.\n
!LFG list - Brings up a list of users currently in the LFG group.\n
!LFG help or !LFG ? - Brings up the help menu.```""")

@client.event
async def on_member_update(before,after):
    RLFG = discord.utils.get(before.server.roles, name='LFG')
    if after.status.offline == after.status:
        await client.remove_roles(message.author, RLFG)
    else:
        return









client.run('BOT TOKEN')
