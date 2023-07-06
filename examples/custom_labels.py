import discord
from discord.ext import commands
from discord_pagination import PaginatedView

bot = commands.Bot(command_prefix="!")

@bot.command()
async def paginate(ctx):
    embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 11)]
    custom_labels = ["Primeira", "Anterior", "Próxima", "Última", "Fechar"]
    view = PaginatedView(ctx, embeds, labels=custom_labels)
    await ctx.send(embed=embeds[0], view=view)

bot.run("token")