# Discord Pagination

`discord_pagination` is a Python library for creating dynamic paginated embeds in Discord bots using the discord.py library. This library extends discord.py's built-in features to provide a customizable, user-friendly pagination system. 

## Installation

To install `discord_pagination`, you need Python 3.6 or later. You can install the library directly from GitHub using pip:

```bash
pip install git+https://github.com/BosonsHiggs/discord_pagination.git
```

## Getting Started

Here's a simple example of how to use `discord_pagination` in your Discord bot:

```python
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
```

In this example, we're creating a set of embeds and displaying them with a PaginatedView. The user can navigate through the embeds using the buttons added by the PaginatedView.

## Customization

`discord_pagination` provides several customization options, allowing you to modify button labels, emojis, styles, and more. For more information on how to use these features, check out the [examples](https://github.com/BosonsHiggs/discord_pagination/tree/main/examples) in this repository.

# Contact

If you have any questions, feedback, or suggestions, feel free to reach out!

- Discord User: arilogai
- Discord Server: [https://discord.gg/GrDXnctrNM](https://discord.gg/GrDXnctrNM)

We appreciate your interest in `discord_pagination` and look forward to hearing from you!