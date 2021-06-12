# =========================================================================
# Logging
# =========================================================================
from tools import config
import logging.config
logging.config.dictConfig(config['logging_config'])
logger_discord = logging.getLogger('discord')


# import logging
# import coloredlogs
# from logging.config import fileConfig

# def log_start():
# CONFIG_LOGGING_PATH = './config/logging.ini'

# logging.basicConfig(filename=CONFIG_LOGGING_PATH, level=logging.INFO)
# fileConfig(CONFIG_LOGGING_PATH)
# coloredlogs.install(level='DEBUG')
# logger_discord = logging.getLogger('discord')
