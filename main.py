
import logging
import base.log
import base.ads
import base.dc as bot
from modules.loading import *

_logger = logging.getLogger(__name__)

# Load extension modules
load_modules = get_auto_install_extension()
_logger.debug(f'load_modules= {load_modules}')
for module in load_modules:
    bot.bot.load_extension(f'{ADDONS_PATH}.{module}')
bot.run()
