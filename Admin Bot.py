import os
import discord

messages = joined = 0


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


client = discord.Client()





@client.event
async def on_member_join(member):
    global joined
    joined += 1
    if joined == 1:
        await client.send_message(f"""Welcome to the server {discord.member.mention}""")


@client.event
async def on_message(message):
    id = client.get_guild(592447508219953163)
    if message.content.find("!hello") != -1:
        message.author == message.author
        await message.channel.send(f"Hello {message.author}")
        print(f" {message.author} Said Hello")
    elif message.content == "!users":
        await message.channel.send(f" Number of Members: {id.member_count}")
        print(f"""{message.author} Asked for users""")
    ...
    if message.content == "!help":
        embed = discord.Embed(title="Admin Bot", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)
    ...

print("Connected To Discord!")
client.run(client.run(os.environ['TOKEN']))
