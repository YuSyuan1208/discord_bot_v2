PREFIX = '*'
LOGGING_CONFIG_DEFAULT = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': {
            '()': 'coloredlogs.ColoredFormatter',  
            # 'format': '%(asctime)s [%(levelname)s] %(name)s[%(lineno)s]: %(message)s' # %(funcName)s,%(filename)s,%(pathname)s
            'format': '%(asctime)s [%(levelname)s] %(pathname)s[%(lineno)s]: %(message)s'
        },
    },
    'handlers': { 
        'default': { 
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': { 
        '': {  # root logger
            'handlers': ['default'],
            'level':  'DEBUG',
            'propagate': False
        },
         'discord': { 
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'modules': { 
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'react': { 
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}