
import logging

_logging = logging.getLogger(__name__)

REACTION_DEFAULT_EMOJI = '🆖'
REACTION_DEFAULT_SIMPLE = ' - '


class Reaction():

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

    def add_reaction_list(self, method_name, method, emoji=REACTION_DEFAULT_EMOJI):
        if self._check_method_name():
            self.react_list.append({
                'name': method_name,
                'method': method,
                'emoji': emoji,
            })
            return True
        logging.wran('method_name empty or not string.')
        return False

    async def send_react_list(self, ctx, sample=REACTION_DEFAULT_SIMPLE):

        channel_id = self._get_channel_id(ctx)
        if not channel_id:
            logging.wran('reaction channel id get fail.')
            return False
        content = ''
        if self.header:
            content += self.header+'\n'
        content = '\n'.join([react.get('method_name')+sample+react.get('emoji') for react in self.react_list])
        if self.footer:
            content += self.footer+'\n'
        emoji_list = [react.get('emoji')for react in self.react_list]
        self.channel_id = channel_id
        message = await ctx.send(content)
        self.message_id = message.id
        for emoji in emoji_list:
            message.add_reaction(emoji)
        return True
