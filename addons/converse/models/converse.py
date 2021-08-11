import logging

from discord.ext import commands
from addons import model, reaction

_logger = logging.getLogger(__name__)


class converse(model.Cog_Extension):

    _name = 'converse'

    reaction_list = []

    start_reaction_list = []
    
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
        re.header = 're'
        self.reaction_list.append(re)
        self.start_reaction_list.append(re)
        async def t(t):
            async def a(ctx):
                print(t)
                await ctx.send(t)
            return a
        re.add_reaction_list('模組列表', await t('test11'), emoji='🧡')
        re.add_reaction_list('美美管理員', await t('test12'), emoji='💛')
        re.add_reaction_list('問題回報', await t('test13'), emoji='💚')
        re.add_reaction_list('清空反應', re.clear_reactions, emoji='💙')
        # re.add_reaction_list('re2', re.clear_reactions)
        print('re:',re)

        re2 = reaction.Reaction()
        self.reaction_list.append(re2)
        re2.header = 're2'
        re2.add_reaction_list('test21', await t('test21'))
        re2.add_reaction_list('test22', await t('test22'))
        re2.add_reaction_list('test23', await t('test23'))
        print('re2:',re2)

        # re.add_reaction_list('test14', re2.send_react_list)
        re.add_reaction_list('re2', await re2.edit_reaction_list(re))
        re2.add_reaction_list('re', await re.edit_reaction_list(re2))
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        mes_id = payload.message_id
        user_id = payload.user_id
        emoji = payload.emoji
        channel_id = payload.channel_id
        channel = self.bot.get_channel(channel_id)

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
                        method = react.get('method')
                        await method(channel)
                        _logger.debug(f'react: {react}')
                            


    @commands.command()
    async def start(self, ctx):
        for reaction in self.start_reaction_list:
            await reaction.send_react_list(ctx)