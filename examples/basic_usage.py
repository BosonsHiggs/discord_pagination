import discord
from discord.ext import commands
from discord_pagination import PaginatedView

bot = commands.Bot(command_prefix="!")

@bot.command()
async def paginate(ctx):
    embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 11)]
    view = PaginatedView(ctx, embeds)
    await ctx.send(embed=embeds[0], view=view)

bot.run("token")