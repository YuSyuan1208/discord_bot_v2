import logging
import os

_logger = logging.getLogger(__name__)


class dc_main_func():

    def __init__(self, bot) -> None:
        self.bot = bot

    async def on_ready(self):
        _logger.info('------')
        _logger.info('Logged in as')
        _logger.info(self.bot.user.name)
        _logger.info(self.bot.user.id)
        _logger.info('------')

    async def load(self, ctx, file_path):
        if os.path.isfile(file_path):
            self.bot.load_extension(file_path)
            await ctx.send(f'Loaded {file_path}')
        else:
            _logger.warning(f'Extension {file_path} could not be loaded.')

    async def unload(self, ctx, file_path):
        if os.path.isfile(file_path):
            self.bot.unload_extension(file_path)
            await ctx.send(f'Unloaded {file_path}')
        else:
            _logger.warning(f'Extension {file_path} has not been loaded')

    async def reload(self, ctx, file_path):
        author_id = ctx.author.id
        if os.path.isfile(file_path):
            self.bot.reload_extension(file_path)
            await ctx.send(f'Reloaded {file_path}')
        else:
            _logger.warning(f'Extension {file_path} has not been loaded')
