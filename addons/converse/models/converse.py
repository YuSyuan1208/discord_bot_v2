import logging

from discord.ext import commands
from addons import model

_logger = logging.getLogger(__name__)


class converse(model.Cog_Extension):

    _name = 'converse'
    
    user_list = []

    selection_list = []

    def _check_user_id(self, user_id):
        if user_id in self.user_list:
            return True

    def _get_message(self, ctx):
        return