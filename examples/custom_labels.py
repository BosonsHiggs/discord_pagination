import discord
from discord.ext import commands
from discord_pagination import PaginatedView

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def paginate(ctx):
    embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 11)]
    custom_labels = ["First", "Previous", "Next", "Last", "Close"]
    view = PaginatedView(ctx, embeds, labels=custom_labels)
    await ctx.send(embed=embeds[0], view=view)

bot.run("token")