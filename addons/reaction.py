
import logging

_logging = logging.getLogger(__name__)

REACTION_DEFAULT_EMOJI = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
REACTION_DEFAULT_SIMPLE = ' - '
REACTION_DEFAULT_BACK_FORMAT = '**`Back`**'

class Reaction():

    message = None
    channel_id = 0
    message_id = 0
    header = ''
    footer = ''

    def __init__(self, header='', footer='') -> None:
        self.header = header
        self.footer = footer
        self.react_list = []

    def _check_method_name(self, method_name):
        if method_name and type(method_name).__name__ == 'str':
            return True
        return False

    def _get_channel_id(self, ctx):
        if str(type(ctx)) == "<class 'discord.channel.TextChannel'>":
            return ctx.id
        else:
            try:
                return ctx.channel.id
            except:
                return False

    def add_reaction_list(self, name, method, emoji=False):
        if self._check_method_name(name):
            if not emoji:
                if len(self.react_list) > 10:
                    _logging.warning('emoji must be give.')
                    return False
                emoji = REACTION_DEFAULT_EMOJI[len(self.react_list)]
            self.react_list.append({
                'name': name,
                'method': method,
                'emoji': emoji,
            })
            return True
        _logging.warning('method_name empty or not string.')
        return False

    async def add_emoji_list(self):
        emoji_list = [react.get('emoji')for react in self.react_list]
        for emoji in emoji_list:
            await self.message.add_reaction(emoji)

    async def send_react_list(self, ctx):

        channel_id = self._get_channel_id(ctx)
        if not channel_id:
            _logging.warning('reaction channel id get fail.')
            return False
        _logging.debug(f'self.react_list: {self.react_list}')
        content = self.get_reaction_content()
        message = await ctx.send(content)
        self.message = message
        self.channel_id = channel_id
        self.message_id = message.id
        await self.add_emoji_list()
        return True

    async def clear_reactions(self, ctx):
        """  """
        await self.message.clear_reactions()

    async def edit_reaction_list(self, re, add_return_flag=False):
        """  """
        _logging.debug(f're: {re}')
        re2 = self
        async def edit(ctx):
            message = re.message
            channel_id = re2._get_channel_id(ctx)
            if not channel_id:
                _logging.warning('reaction channel id get fail.')
                return False
            content = re2.get_reaction_content()
            await re.clear_reactions(ctx)
            await message.edit(content=content)
            re2.message = message
            re2.channel_id = channel_id
            re2.message_id = message.id
            re.message = None
            re.channel_id = 0
            re.message_id = 0
            await re2.add_emoji_list()
        if add_return_flag:
            self.add_reaction_list(REACTION_DEFAULT_BACK_FORMAT, await re.edit_reaction_list(re2), emoji='⬅️')
        return edit

    def get_reaction_content(self, front_sample='', mid_sample=REACTION_DEFAULT_SIMPLE, back_sample=''):
        """  """
        content = ''
        if self.header:
            content += self.header+'\n'
        content += '\n'.join([front_sample+react.get('emoji')+mid_sample+react.get('name')+back_sample for react in self.react_list])
        if self.footer:
            content += self.footer+'\n'
        _logging.debug(f'content: {content}')
        return content