import discord
import asyncio
from discord.ext import commands
from discord_pagination import PaginatedView

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents, command_prefix: str):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Customer logged in as {self.user} (ID: {self.user.id})')

bot = MyBot(intents=intents, command_prefix="!")

@bot.command()
async def paginate(ctx):
    embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 10)]
    view = PaginatedView(ctx, embeds, use_buttons=True, owner_only=True)
    await ctx.send(embed=embeds[0], view=view)
                
async def main():
    async with bot:
        await bot.start("token")

asyncio.run(main())
