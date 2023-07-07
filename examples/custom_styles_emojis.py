import discord
from discord.ext import commands
from discord_pagination import PaginatedView
from discord import ButtonStyle

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def paginate(ctx):
    embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 11)]
    custom_emojis = ["🍎", "🍊", "🍋", "🍌", "🍉"]
    custom_styles = [ButtonStyle.secondary, ButtonStyle.success, ButtonStyle.danger, ButtonStyle.grey, ButtonStyle.primary]
    view = PaginatedView(ctx, embeds, emojis=custom_emojis, styles=custom_styles)
    await ctx.send(embed=embeds[0], view=view)

bot.run("token")