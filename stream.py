import discord
from discord.ext import commands

intents = discord.Intents.default()

client = commands.Bot(command_prefix='!', intents=intents) # this is the prefix u can change it whenever u want(u can change the client too)

@client.command()
async def stream(ctx, *, stream_name: str):
    await client_multi_line_spam.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=stream_name, url=""))
    await ctx.send(f"# <@{ctx.author.id}> you re streaming now:  {stream_name}")
