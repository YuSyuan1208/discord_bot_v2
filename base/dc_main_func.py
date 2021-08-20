import logging
import sys
from modules.loading import *
from base.ads import ModuleManage

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
        if await self._module_action(module, 'load'):
            await ctx.send(f'Loaded {module}')

    async def unload(self, ctx, module):
        if await self._module_action(module, 'unload'):
            await ctx.send(f'Unloaded {module}')

    async def reload(self, ctx, module):
        if await self._module_action(module, 'reload'):
            await ctx.send(f'Reloaded {module}')

    async def _module_action(self, module, type):
        try:
            installable = module in get_installable_list()
            installed = module in ModuleManage.get_module_installed()
            _logger.debug(f'installable: {installable}, installed: {installed}')

            flag = False
            if type == 'load':
                if installable and not installed:
                    self.bot.load_extension(f'{ADDONS_PATH}.{module}')
                    ModuleManage.module_load(module)
                    await self.bot.get_cog(module).on_ready()
                    flag = True
            elif type == 'unload':
                if installed:
                    self.bot.unload_extension(f'{ADDONS_PATH}.{module}')
                    ModuleManage.module_unload(module)
                    flag = True
            elif type == 'reload':
                if installed and installable:
                    self.bot.reload_extension(f'{ADDONS_PATH}.{module}')
                    ModuleManage.module_reload(module)
                    await self.bot.get_cog(module).on_ready()
                    flag = True
            if not flag:
                _logger.error(f'{module} {type} failed.')
                return False
        except:
            _logger.error(f'Extension {module} action error. {sys.exc_info()}')
            return False
        _logger.debug(f'installed_modules= {ModuleManage.get_module_installed()}')
        return True
