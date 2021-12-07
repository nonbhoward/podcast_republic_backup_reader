import os
import pathlib
project_name = os.getcwd().split('/')[4]
log_filename = pathlib.Path(os.getenv('HOME'),
                            'logs',
                            f'{project_name}.log')
log_filemode = 'a'
log_format = '%(asctime)s ' \
             '%(levelname)s ' \
             '%(filename)s ' \
             '%(lineno)d ' \
             '%(message)s'
