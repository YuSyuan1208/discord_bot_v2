
import logging

_logging = logging.getLogger(__name__)

REACTION_DEFAULT_EMOJI = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
REACTION_DEFAULT_SIMPLE = ' - '


class Reaction():

    message = None
    channel_id = 0
    message_id = 0
    react_list = []
    header = ''
    footer = ''

    def __init__(self, header='', footer='') -> None:
        self.header = header
        self.footer = footer

    def _check_method_name(self, method_name):
        if method_name and type(method_name).__name__ == 'str':
            return True
        return False

    def _get_channel_id(self, ctx):
        if type(ctx).__name__ == 'discord.channel.TextChannel':
            return ctx.id
        else:
            try:
                return ctx.channel.id
            except:
                return False

    def add_reaction_list(self, method_name, method, emoji=False):
        if self._check_method_name(method_name):
            if not emoji:
                if len(self.react_list) > 10:
                    _logging.warning('emoji must be give.')
                    return False
                emoji = REACTION_DEFAULT_EMOJI[len(self.react_list)]
            self.react_list.append({
                'name': method_name,
                'method': method,
                'emoji': emoji,
            })
            return True
        _logging.warning('method_name empty or not string.')
        return False

    async def send_react_list(self, ctx, sample=REACTION_DEFAULT_SIMPLE):

        channel_id = self._get_channel_id(ctx)
        if not channel_id:
            _logging.warning('reaction channel id get fail.')
            return False
        content = ''
        if self.header:
            content += self.header+'\n'
        _logging.debug(f'self.react_list: {self.react_list}')
        content = '\n'.join([react.get('emoji')+sample+react.get('name') for react in self.react_list])
        if self.footer:
            content += self.footer+'\n'
        emoji_list = [react.get('emoji')for react in self.react_list]
        self.channel_id = channel_id
        message = await ctx.send(content)
        self.message = message
        self.message_id = message.id
        for emoji in emoji_list:
            await message.add_reaction(emoji)
        return True