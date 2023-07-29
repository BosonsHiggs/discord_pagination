import discord
import os
import asyncio
import traceback
from discord.ext import commands
from discord_pagination import PaginatedView, HelpCommand

TOKEN = os.getenv("BOT_LIA_TESTES")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
#self.remove_command('help')
bot.help_command = HelpCommand()

@bot.command()
async def paginate(ctx):
	"""Organize the embeds with a paginator"""
	embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 1000)]
	view = PaginatedView(ctx, embeds, use_buttons=True, owner_only=True)
	await ctx.send(embed=embeds[0], view=view)

bot.run(TOKEN)
