import discord
import os
import asyncio
import traceback
from discord.ext import commands
from discord_pagination import PaginatedView, HelpCommand
from discord import ButtonStyle

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')
bot.help_command = HelpCommand()

@bot.command()
async def paginate(ctx):
	"""Organize the embeds with a paginator"""
	embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 1000)]
	view = PaginatedView(ctx, embeds, use_buttons=True, owner_only=True)
	await ctx.send(embed=embeds[0], view=view)

@bot.command()
async def help_command(ctx):
	"""Custom Help command"""
	mapping = {cog: cog.get_commands() for cog in bot.cogs.values()}
	mapping[None] = [cmd for cmd in bot.commands if cmd.cog is None]


	# Invoke the help command
	custom_labels = ["First", "Previous", "Next", "Last", "Close"]
	custom_emojis = ["⏮️", "⏪", "⏩", "⏭️", "🚫"]
	custom_styles = [ButtonStyle.primary] * 4 + [ButtonStyle.secondary]

	await bot.help_command.send_bot_help(mapping, ctx, title="BOT COMMANDS", 
											custom_labels=custom_labels, 
											custom_emojis=custom_emojis, custom_styles=custom_styles
											)
bot.run(TOKEN)
