import ast
import sys
import os
import json
import errno
import logging


class DataImport():

    _file_data = {}
    _file_path = ''
    _file_type = 'json'
    _file_encoding = 'utf8'
    _directory_create = True

    def __init__(self, path, rw_type='json', encoding='utf8', directory_create=True) -> None:
        if path:
            self._file_path = path
            self._file_directory = os.path.dirname(path)
        if rw_type in ['eval', 'str']:
            self._file_data = ''
        self._file_type = rw_type
        self._file_encoding = encoding
        self._directory_create = directory_create
        # pass

    def get_file_data(self, file_create=False):
        rs = self.json_file(self._file_path, 'r')
        if not rs and file_create:
            rs = self.write_file_data()
        return rs

    def write_file_data(self, data=False, indent=None):
        if data:
            self._file_data = data
        rs = self.json_file(self._file_path, 'w', indent=indent) if self._check_directory() else False
        return rs

    def _check_json_file(self, keys=[]):
        not_find_keys = []
        if keys:
            not_find_keys = [key for key in keys if key not in self._file_data]
        logging.debug(f'file= {self._file_path}, keys= {keys}, not_find_keys= {not_find_keys}')
        if not_find_keys:
            logging.warning(f'keys not in file.(not_find_keys= {not_find_keys}, file= {self._file_path})')
            return False
        else:
            return True

    def _check_directory(self):
        if not os.path.exists(self._file_directory):
            logging.warning(f'No such directory: {self._file_directory}')
            if self._directory_create:
                try:
                    os.makedirs(self._file_directory)
                    logging.info(f'{self._file_directory} created.')
                    return True
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
        else:
            return True
        return False

    def json_file(self, file_path, action_type, indent=None):
        """ file control """
        if action_type == 'r':
            if os.path.isfile(file_path):
                logging.info(file_path + ' file getting.')
                try:
                    if os.stat(file_path).st_size != 0:
                        with open(file_path, 'r', encoding=self._file_encoding) as ofile:
                            if self._file_type == 'json':
                                self._file_data = json.load(ofile)
                            elif self._file_type == 'eval':
                                self._file_data = ast.literal_eval(ofile.read())
                            elif self._file_type == 'str':
                                self._file_data = ofile.read()
                        return self._file_data
                    else:
                        logging.warning(f'file empty. (path={file_path})')
                        return False
                except Exception as e:
                    raise ValueError(f'file getting error.(message= {sys.exc_info()})')
            else:
                logging.warning(file_path + ' file not find.')
                return False
        elif action_type == 'w':
            logging.info(file_path + ' file saving.')
            with open(file_path, 'w') as ofile:
                if self._file_type == 'json':
                    json.dump(self._file_data, ofile, indent=indent)
                elif self._file_type in ['eval', 'str']:
                    ofile.write(self._file_data)
            return self._file_data
        else:
            raise ValueError(f'action_type not find.(type={action_type})')
