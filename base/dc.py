# =========================================================================
# Discord
# =========================================================================
import logging
from discord.ext import commands
from tools.data import DataImport
from tools import config
from .dc_main_func import dc_main_func

# CONFIG_SETTING_PATH = './config/setting.json'

_logger = logging.getLogger(__name__)

# setting_data = DataImport(CONFIG_SETTING_PATH).get_file_data()
# _logger.debug(setting_data)
# if not setting_data:
#     _logger.error(""" Bot starting fail!! Please check file. (path= %s)
#     The content must be like:
#     {
#         "BOT_PREFIX": ["*"],
#         "TOKEN": {Your bot TOKEN}
#     }
#     """ % CONFIG_SETTING_PATH)

bot = commands.Bot(
    command_prefix=config['prefix'].split(','), case_insensitive=True)

# base robot command 
func = dc_main_func(bot)
bot.add_listener(func.on_ready)
bot.add_command(commands.Command(func.load))
bot.add_command(commands.Command(func.unload))
bot.add_command(commands.Command(func.reload))


# help ending note
""" bot.help_command.get_ending_note """


def run():
    if not config['token']:
        _logger.error(f'Discord robot TOKEN not setting. Please set in {config.rcfile}')
    else:
        bot.run(config['token'])
