import discord
from discord.ext import commands
from .pagination import PaginatedView

class HelpCommand(commands.DefaultHelpCommand):
    async def send_bot_help(self, mapping, context:commands.Context=None, title:str='HELP', prefix:str="\\"):
        ctx = context if context is not None else self.context 
        embeds = []

        for cog, commands in mapping.items():
            title = cog.qualified_name if cog is not None else "No Cog"

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
            custom_labels = ["First", "Previous", "Next", "Last", "Close"]
            view = PaginatedView(ctx, embeds, labels=custom_labels)
            await ctx.send(embed=embeds[0], view=view)