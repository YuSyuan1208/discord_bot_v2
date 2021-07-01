import logging
import os
from modules.loading import *

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

    async def load(self, ctx, module):
        if module in get_installable_list():
            try:
                self.bot.load_extension(f'{ADDONS_PATH}.{module}')
                AddonsModuleImport.modules_load(module)
                await self.bot.get_cog(module).on_ready()
                await ctx.send(f'Loaded {module}')
            except:
                _logger.warning(f'Extension {module} could not be loaded.')
        else:
            _logger.warning(f'Extension {module} installable is False.')

    async def unload(self, ctx, module):
        try:
            self.bot.unload_extension(f'{ADDONS_PATH}.{module}')
            AddonsModuleImport.module_unload(module)
            await ctx.send(f'Unloaded {module}')
        except:
            _logger.warning(f'Extension {module} has not been loaded')

    async def reload(self, ctx, module):
        try:
            self.bot.reload_extension(f'{ADDONS_PATH}.{module}')
            AddonsModuleImport.module_reload(module)
            await self.bot.get_cog(module).on_ready()
            await ctx.send(f'Reloaded {module}')
        except:
            _logger.warning(f'Extension {module} has not been loaded')
