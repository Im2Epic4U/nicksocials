import discord
import json
import os
from discord import activity

client = discord.Client()
# with open('config.json') as cfg_file:
#     print(f"> config loaded")

#     cfg = json.load(cfg_file)
Clayton = 379400007410909186
Nick = 269946726918389770

@client.event
async def on_ready():
	await client.wait_until_ready()
	await client.change_presence(activity=discord.Activity(type=2, name='nicks spotify'))
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

	if "ns.list" == message.content.lower():
		embed = discord.Embed(title="Nick's Socials", description="A list of Nick's social media accounts are shown here.\n\n[🐦 Twitter](https://twitter.com/godhxtesnick)\n\n[🎵 Spotify](https://open.spotify.com/user/w7dshlsxyrhl2i6o5yk5chwwc?si=XsHbVTDiTHy8eNQ-97JKqw)\n\n[📺 Twitch](https://twitch.tv/kosymosy)", colour=discord.Colour.red())
		embed.set_footer(text='Contact real epic#0001 if there is a bug with this bot.', icon_url='https://cdn.discordapp.com/avatars/379400007410909186/a_264e49cb370914994eda22c49ed2aa96.gif')
		embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/269946726918389770/8ee2b0b5ffc97fd266f3d6c7074ebf14.png')
		embed.set_author(name='nick!#0003', icon_url='https://cdn.discordapp.com/avatars/269946726918389770/8ee2b0b5ffc97fd266f3d6c7074ebf14.png')
		await message.channel.send(content=None, embed=embed)

	elif "ns.logout" == message.content.lower():
		if message.author.id == Clayton or Nick:
			await message.channel.send(f"Logging out... :wave:")
			client.logout()
		else:
			await message.channel.send(f"You don't have permission to logout this bot!")

client.run(os.getenv('TOKEN'))