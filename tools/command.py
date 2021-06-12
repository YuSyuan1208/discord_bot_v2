import logging
import os
import random

_logger = logging.getLogger(__name__)


class CommandObjectImport:

    msg_obj = None  # message object
    msg_content = []  # message content
    obj_type = ''

    def __init__(self):
        pass
        # self.ctx = ctx
        # self.argv = argv
        # self.knews = knews

    async def add_cmd(self, ctx, *argv, **knews):
        content = self.random_str(ctx, argv, knews)
        await ctx.send(content)

    def random_str(self, ctx, argv, knews):
        return random.choice(self.msg_content).format(ctx=ctx, argv=argv, knews=knews)
