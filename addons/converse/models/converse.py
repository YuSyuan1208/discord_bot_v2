import logging

from discord.ext import commands
from addons import model, reaction

_logger = logging.getLogger(__name__)


class converse(model.Cog_Extension):

    _name = 'converse'

    reaction_list = []
    
    user_list = []

    selection_list = []

    def _check_user_id(self, user_id):
        if user_id in self.user_list:
            return True

    def _get_message(self, ctx):
        return

    @commands.Cog.listener()
    async def on_ready(self):
        await super().on_ready()
        re = reaction
        self.reaction_list.append(re)
        re.add_reaction_list('test', 'test')
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        mes_id = payload.message_id
        user_id = payload.user_id
        channel_id = payload.channel_id

        message = [re.message for re in self.reaction_list if re.message_id == mes_id]
        message = message[0] if message else False
        

    @commands.command()
    async def start(self, ctx):
        await self.reaction.send_react_list(ctx)