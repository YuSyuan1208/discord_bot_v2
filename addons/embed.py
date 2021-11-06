from os import name
import discord


class Embed():
    """  """

    header = ''
    footer = ''
    field_list = []
    thumbnail_url = ''

    def add_field(self, data):
        self.field_list.append(data)
    
    def get_embed(self):
        embed=discord.Embed(title="", url="", description="", color=0xb82828)
        embed.set_author(name="", url="", icon_url="")
        embed.set_thumbnail(url="")
        for field in self.field_list:
            embed.add_field(name=field.get('name', ''), value=field.get('value', ''), inline=field.get('inline', False))
        embed

