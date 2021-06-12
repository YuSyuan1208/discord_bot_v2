import ast
import sys
import os
import json
import logging

_logger = logging.getLogger(__name__)

class DataImport():

    _file_data = {}
    _file_path = ''
    _file_type = 'json'
    _file_encoding = 'utf8'

    def __init__(self, path, rw_type='json', encoding='utf8') -> None:
        if path:
            self._file_path = path
        self._file_type = rw_type
        self._file_encoding = encoding
        # pass

    def get_file_data(self, auto_create=False):
        rs = self.json_file(self._file_path, 'r',)
        if not rs and auto_create:
            rs = self.write_file_data()
        return rs
    
    def write_file_data(self, data=False):
        if data:
            self._file_data = data
        rs = self.json_file(self._file_path, 'w')
        return rs

    def _check_json_file(self, keys=[]):
        not_find_keys = []
        if keys:
            not_find_keys = [key for key in keys if key not in self._file_data]
        _logger.debug(f'file= {self._file_path}, keys= {keys}, not_find_keys= {not_find_keys}')
        if not_find_keys:
            _logger.warning(f'keys not in file.(not_find_keys= {not_find_keys}, file= {self._file_path})')
            return False
        else:
            return True

    def json_file(self, file_path, action_type):
        """ file control """
        if action_type == 'r':
            if os.path.isfile(file_path):
                _logger.info(file_path + ' file getting.')
                try:
                    if os.stat(file_path).st_size != 0:
                        with open(file_path, 'r', encoding=self._file_encoding) as ofile:
                            if self._file_type == 'json':
                                self._file_data = json.load(ofile)
                            elif self._file_type == 'eval':
                                self._file_data = ast.literal_eval(ofile.read())
                        return self._file_data
                    else:
                        _logger.warning(f'file empty. (path={file_path})')
                        return False
                except Exception as e:
                    raise ValueError(f'file getting error.(message= {sys.exc_info()})')
            else:
                _logger.warning(file_path + ' file not find.')
                return False
        elif action_type == 'w':
            _logger.info(file_path + ' file saving.')
            with open(file_path, 'w') as ofile:
                if self._file_type == 'json':
                    json.dump(self._file_data, ofile)
                elif self._file_type == 'eval':
                    ofile.write(self._file_data)
            return self._file_data
        else:
            raise ValueError(f'action_type not find.(type={action_type})')
