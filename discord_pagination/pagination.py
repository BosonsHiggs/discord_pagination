import discord
from discord import ButtonStyle, ui
from typing import List, Optional, Callable, Any

class PaginatedView(ui.View):
    def __init__(
        self,
        ctx: discord.ext.commands.Context,
        embeds: List[discord.Embed],
        use_buttons: bool = True,
        labels: Optional[List[str]] = None,
        emojis: Optional[List[str]] = None,
        styles: Optional[List[ButtonStyle]] = None,
        timeout: Optional[int] = None,
        timeout_message: Optional[str] = None,
        on_timeout_callback: Optional[Callable[..., Any]] = None,
        owner_only: bool = True,
    ):
        super().__init__(timeout=timeout)
        self.ctx = ctx
        self.embeds = embeds
        self.current = 0
        self.timeout_message = timeout_message
        self.on_timeout_callback = on_timeout_callback
        self.owner_only = owner_only

        labels = labels if labels and len(labels) == 5 else ["First", "Previous", "Next", "Last", "Close"]
        emojis = emojis if emojis and len(emojis) == 5 else ["⏮️", "⏪", "⏩", "⏭️", "🚫"]
        styles = styles if styles and len(styles) == 5 else [ButtonStyle.primary] * 4 + [ButtonStyle.secondary]

        if use_buttons:
            self.add_item(ui.Button(style=styles[0], label=labels[0], emoji=emojis[0], custom_id="first"))
            self.add_item(ui.Button(style=styles[1], label=labels[1], emoji=emojis[1], custom_id="prev"))
            self.add_item(ui.Button(style=styles[2], label=labels[2], emoji=emojis[2], custom_id="next"))
            self.add_item(ui.Button(style=styles[3], label=labels[3], emoji=emojis[3], custom_id="last"))
            self.add_item(ui.Button(style=styles[4], label=labels[4], emoji=emojis[4], custom_id="close"))
        else:
            options = [discord.SelectOption(label=f"Page {i+1}", value=str(i)) for i in range(len(embeds))]
            select_menu = discord.ui.Select(custom_id="go_to", placeholder="Go to page...", options=options)
            self.add_item(select_menu)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        await interaction.response.defer()
        if self.owner_only and interaction.user.id != self.ctx.author.id:
            return False

        if interaction.data["component_type"] == discord.ComponentType.button.value:
            if interaction.data["custom_id"] == "first":
                self.current = 0
            elif interaction.data["custom_id"] == "prev":
                self.current = self.current - 1 if self.current > 0 else 0
            elif interaction.data["custom_id"] == "next":
                self.current = self.current + 1 if self.current < (len(self.embeds) - 1) else len(self.embeds) - 1
            elif interaction.data["custom_id"] == "last":
                self.current = len(self.embeds) - 1
            elif interaction.data["custom_id"] == "close":
                return await interaction.message.delete()
        elif interaction.data["component_type"] == discord.ComponentType.select.value:
            self.current = int(interaction.data["values"][0])
        embed = self.embeds[self.current]
        await interaction.message.edit(embed=embed)
        return True

    async def on_timeout(self):
        if self.timeout_message:
            await self.ctx.send(self.timeout_message)
        if self.on_timeout_callback:
            await self.on_timeout_callback()
