import ast
import logging
from os.path import join as opj
from tools.command import CommandObjectImport
from discord.ext import commands
from tools import data
from modules.loading import addons_list

_logger = logging.getLogger(__name__)

MODEL_DATA_PATH = 'data'
MODEL_SETTING_FILE = 'setting.json'
MODEL_SETTING_KEYS = ['msg_id', 'channel_id']


class Cog_Extension(commands.Cog):

    _name = None
    _setting_file = None
    _data = {}

    async def on_ready(self):
        _logger.info(self._name + ' on_ready.')
        await self._load_setting()

    async def _load_setting(self):
        await self._get_message_setting()

    def __init__(self, bot):
        """  """
        self.bot = bot
        if self._name:
            _logger.info(self._name + ' init')
            _logger.debug(addons_list.get(self._name))
            addons_module_data_path = opj(addons_list.get(self._name).get('addons_module_path'), MODEL_DATA_PATH)
            addons_module_setting_file = opj(addons_module_data_path, MODEL_SETTING_FILE)
            self._setting_file = data.DataImport(addons_module_setting_file)
            self._setting_file.get_file_data(True)
        else:
            _logger.error('_name not setting.')
            raise NameError('model _name not setting.')

    def _str_to_list(self, str):
        """ covert message object content to list """
        ast_content = ast.literal_eval(str)
        return ast_content

    async def _get_message_obj(self, channel_id=0, msg_ids=[], history=True, setting={}):
        """ Get message object.

            return message object array (msg_objs)
        """
        limit = setting.get('limit', 100)

        if channel_id:
            # channel_id = self._setting_file._file_data['channel_id']  # 750943234691432510
            # msg_ids = [self._setting_file._file_data['msg_id']]  # 750946905751814224
            channel = self.bot.get_channel(channel_id)
            if not channel:
                _logger.warning(self._name + f' channel not find.(channel_id={channel_id})')
                return False

            msg_objs = []
            com_msg_ids = []
            if history:
                _logger.info(self._name + ' channel history content getting.')
                async for message in channel.history(limit=int(limit)):
                    if not msg_ids or message.id in msg_ids:
                        msg_objs.append(message)
                        com_msg_ids.append(message.id)
                        _logger.debug(self._name + f' message.id: {message.id}')

                com_msg_ids = set(msg_ids) - set(com_msg_ids)
                if com_msg_ids:
                    _logger.warning(self._name + f' message not find.(msg_id={com_msg_ids})')
            else:
                _logger.info(self._name + ' channel fetch_message content getting.')
                for msg_id in msg_ids:
                    try:
                        message = await channel.fetch_message(msg_id)
                        msg_objs.append(message)
                    except:
                        _logger.warning(self._name + f' message not find.(msg_id={msg_id})')

            _logger.info(self._name + ' message object get.')
            if not msg_objs:
                _logger.warning(self._name + ' no message object data.')
                return False
            else:
                return msg_objs
        else:
            _logger.warning(self._name + ' no message object data.')
            return False

    def _check_setting_file(self):
        """ check MODEL_SETTING_FILE. """
        if self._setting_file and self._setting_file._check_json_file(MODEL_SETTING_KEYS):
            return True
        else:
            return False

    async def _get_message_setting(self):
        """ 依據檔案的channel、message id 取得message object 

            self._set_default = self._str_to_list(msg_objs[0].content)
        """
        if not self._check_setting_file():
            return False
        msg_ids = [self._setting_file._file_data['msg_id']]
        channel_id = self._setting_file._file_data['channel_id']
        msg_objs = await self._get_message_obj(channel_id=channel_id, msg_ids=msg_ids)
        if msg_objs:
            self._set_default = self._str_to_list(msg_objs[0].content)
            _logger.debug(self._name + f' _set_default: {self._set_default}')
            if self._set_default:
                _logger.info(self._name + ' _set_default get.')
                return True
            else:
                _logger.warning(self._name + ' _set_default not get.')
        else:
            _logger.warning(self._name + f' _set_default msg_objs not get.')
        return False

    def _set_command(self, msg_obj, name, setting={}, init_flag=False):
        """ 設定指令 """
        if name:
            cmd_obj = self.bot.get_command(name)
            if cmd_obj:
                _logger.debug(self._name + f' ins_com: {name},{setting}')
                obj = cmd_obj.callback.__self__
                if obj.id == msg_obj.id or not init_flag:
                    obj.content = setting['content']
                else:
                    _logger.warning(self._name + f' command name repeat.')
            else:
                _logger.debug(self._name + f' add_com: {name},{setting}')
                obj = CommandObjectImport()
                obj.msg_obj = msg_obj
                obj.msg_content = setting['content']
                obj.obj_type = self._name
                self.bot.add_command(commands.Command(obj.add_cmd, name=name))
            _logger.info(self._name + ' cmds complete.')
            return True
        else:
            _logger.warning(self._name + ' name not set.')
            return False
