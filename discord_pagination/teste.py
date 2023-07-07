import discord
import os
import asyncio
import traceback
from discord.ext import commands
from discord_pagination import PaginatedView

TOKEN = os.getenv("DISCORD_BOSONS_TESTS")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents, command_prefix: str):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Cliente logado como {self.user} (ID: {self.user.id})')

bot = MyBot(intents=intents, command_prefix="!")

@bot.command()
async def paginate(ctx):
	try:
		embeds = [discord.Embed(title=f"Page {i}") for i in range(1, 1000)]
		view = PaginatedView(ctx, embeds, use_buttons=True, owner_only=True)
		await ctx.send(embed=embeds[0], view=view)
	except Exception as e:
		print(f"An error occurred: {e}")
		tb = traceback.format_exc()
		print(tb)
                
async def main():
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())
