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
        re = reaction.Reaction()
        self.reaction_list.append(re)
        re.add_reaction_list('test', 'test')
        re.add_reaction_list('test1', 'test1')
        re.add_reaction_list('test2', 'test2')
        re.add_reaction_list('test3', 'test3')
        re.add_reaction_list('test4', 'test4')
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        mes_id = payload.message_id
        user_id = payload.user_id
        channel_id = payload.channel_id
        emoji = payload.emoji

        if user_id != self.bot.user.id:
            re = False
            for i in self.reaction_list:
                if i.message_id == mes_id:
                    re = i
                    break
            if re:
                message = re.message 
                _logger.debug(f'message: {message}')
                if message:
                    react = False
                    for i in re.react_list:
                        print(i.get('emoji'),emoji,i.get('emoji') == str(emoji))
                        if i.get('emoji') == str(emoji):
                            react = i
                            break
                    if react:
                        _logger.debug(f'react: {react}')
                            


    @commands.command()
    async def start(self, ctx):
        for reaction in self.reaction_list:
            await reaction.send_react_list(ctx)