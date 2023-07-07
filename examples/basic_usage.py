import discord
import os
import asyncio
import traceback
from discord.ext import commands
from discord_pagination import PaginatedView

TOKEN = os.getenv("DISCORD_BOSONS_TESTS")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def paginate(ctx):
	embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 1000)]
	view = PaginatedView(ctx, embeds, use_buttons=True, owner_only=True)
	await ctx.send(embed=embeds[0], view=view)

bot.run(TOKEN)
