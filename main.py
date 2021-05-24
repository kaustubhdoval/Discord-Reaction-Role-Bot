import discord
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 757898124319785002:
	#ENTER THE MESSAGE ID OF THE MESSAGE THAT HAS TO BE REACTED TO
	
        guild = client.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = guild.get_member(payload.user_id)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 757898124319785002:
        guild = client.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = guild.get_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role) 
                print("done")
            else:
                print("member not found")
        else:
            print("role not found")
			

client.run('TOKEN ID')
#ENTER YOUR OWN TOKEN ID
