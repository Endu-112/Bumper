from typing import Literal
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix= "B!")
client.remove_command("help")

@client.event
async def on_ready():
    print("online")


@client.command()
async def test(ctx):
   await ctx.channel.send("działa")
   await asyncio.sleep(5)
   await ctx.channel.purge(limit = 2)

@client.command()
async def bump(ctx):
    while(True):
        await ctx.channel.send("!d bump")
        await asyncio.sleep(7200)


client.run("ODcyMTA5NTI5ODAwNzgxODc0.YQlFSg.TSeuP7F_SR-3QATEVNSZPIg3UhQ")