import discord
from discord.ext import commands
from .pagination import PaginatedView

class HelpCommand(commands.DefaultHelpCommand):
    async def send_bot_help(self, mapping, context:commands.Context=None, **kwargs):
        ctx = context if context is not None else self.context 
        title = kwargs.get("title")
        prefix = kwargs.get("prefix")
        custom_labels = kwargs.get("custom_labels")
        custom_emojis = kwargs.get("custom_emojis")
        custom_styles = kwargs.get("custom_styles")

        prefix = prefix if prefix is not None else '/'
        custom_labels = custom_labels if custom_labels is not None else None
        custom_emojis = custom_emojis if custom_emojis is not None else None
        custom_styles = custom_styles if custom_styles is not None else None

        embeds = []

        for cog, commands in mapping.items():
            if title is None:
                title = cog.qualified_name if cog is not None else "HELP COMMANDS"

            embed = discord.Embed(title=title)
            added = False  # Variável para rastrear se algum comando foi adicionado

            for command in commands:
                if command.hidden:
                    continue

                # Verificar se o membro pode executar o comando
                try:
                    can_run = await command.can_run(ctx)
                except:
                    can_run = False

                if not can_run:
                    continue  # Ignorar comandos que o membro não pode executar
                
                description = command.brief or command.short_doc
                embed.add_field(name=f'{prefix}{command.name}', value=f"```\n{description}\n```" or 'No description')
                added = True  # Se chegamos até aqui, um comando foi adicionado

            # Se nenhum comando foi adicionado, não adicionar o embed à lista
            if added:
                embeds.append(embed)

        # seu código de paginação
        if not embeds:
            await ctx.send("There are no available commands you can execute.")
        else:
            view = PaginatedView(ctx, embeds, labels=custom_labels, emojis=custom_emojis, styles=custom_styles)
            await ctx.send(embed=embeds[0], view=view)