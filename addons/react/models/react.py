import logging
import json
from tools import data
from discord.ext import commands
from addons import model

_logger = logging.getLogger(__name__)


class react(model.Cog_Extension):

    _name = 'react'
    _data = {}
    _set_default = {}

    def __init__(self, bot):
        # self._setting_file.get_file_data('addons/react/data/react.json')
        # _logger.debug(self._setting_file._file_data)
        super().__init__(bot)

    def _check(self, ctx):
        if self._setting_file._file_data and self._data:
            _logger.info(self._name + ' file already get.')
            return True
        else:
            _logger.warning(self._name + ' file not getting!')
            return False

    def _list_to_str(self, list):
        str = json.dumps(list, indent=4, ensure_ascii=False)
        return str

    @commands.Cog.listener()
    async def on_ready(self):
        await super().on_ready()
        # _logger.info(self._name + ' on_ready.')
        if await self._get_message_setting():
            await self.get_react_command_list()
        """ /* 752886850435416264-767615688755118091 */ """

    async def get_react_command_list(self):
        """ 獲取react指令 """
        if 'cmd_channel_id' in self._set_default:
            channel_id = self._set_default['cmd_channel_id']
            msg_objs = await self._get_message_obj(channel_id=channel_id)
            if msg_objs:
                for message in msg_objs:
                    content_ls = self._str_to_list(message.content)
                    if content_ls:
                        self._set_command(message, content_ls['name'], setting=content_ls, init_flag=True)
                    else:
                        _logger.warning(self._name + f' command obj _str_to_list fail.(msg_id={message.id})')
                return True
        else:
            _logger.warning(self._name + f' cmd_channel_id not get.')
            return False

    @commands.command()
    async def at(self, ctx, name, *msg):
        cmd_obj = self.bot.get_command(name)
        setting = {}
        content = ' '.join(msg)
        setting.update({'name': name, 'content': [content]})
        channel_id = self._set_default['cmd_channel_id']
        if not cmd_obj:
            msg_obj = await self._send_message_obj(channel_id, setting)
        else:
            if not hasattr(cmd_obj.callback, '__self__'):
                _logger.warning(self._name + f' name can not use in command.(name={name})')
                return False
            msg_obj = cmd_obj.callback.__self__
            if hasattr(msg_obj, 'obj_type'):
                obj_type = msg_obj.obj_type
                if obj_type != self._name:
                    _logger.warning(self._name + f' obj_type compare fail.(obj_type={obj_type})')
                    return False
            else:
                    _logger.warning(self._name + f' object has no attribute \obj_type\'.')
                    return False
            _logger.debug(self._name + f' at repeat. (setting.content={setting["content"]},msg_obj.content={msg_obj.content})')
            setting['content'] += msg_obj.content
            msg_objs = await self._get_message_obj(channel_id=channel_id, msg_ids=[msg_obj.id])
            msg_obj = msg_objs[0]
            if not await self._edit_message_obj(msg_obj, setting):
                return False
        if msg_obj:
            self._set_command(msg_obj, setting['name'], setting)
        else:
            return False

    async def _edit_message_obj(self, msg_obj, setting):
        if 'content' in setting:
            content = self._list_to_str(setting)
            if msg_obj.author == self.bot.user:
                await msg_obj.edit(content=content)
            else:
                await msg_obj.delete()
                await self._send_message_obj(msg_obj.channel.id,setting)
            return True
        return False


    async def _send_message_obj(self, channel_id, setting):
        channel = self.bot.get_channel(channel_id)
        content = self._list_to_str(setting)
        return await channel.send(content)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        pass




