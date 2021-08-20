
import logging
import base.log
import base.ads
import base.dc as bot
from modules.loading import *

_logger = logging.getLogger(__name__)

# Load extension modules
load_modules = get_auto_install_extension()
for module in load_modules:
    bot.bot.load_extension(f'{ADDONS_PATH}.{module}')
    base.ads.ModuleManage.set_module_installed(module, True)
_logger.info(f'installed_modules= {base.ads.ModuleManage.get_module_installed()}')
bot.run()
