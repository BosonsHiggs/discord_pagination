import discord
from discord.ext import commands
from discord_pagination import PaginatedView

bot = commands.Bot(command_prefix="!")

@bot.command()
async def paginate(ctx):
    embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 11)]
    
    async def my_callback():
        await ctx.send("The callback function was called!")

    view = PaginatedView(ctx, embeds, timeout=60, on_timeout_callback=my_callback)
    await ctx.send(embed=embeds[0], view=view)

bot.run("token")