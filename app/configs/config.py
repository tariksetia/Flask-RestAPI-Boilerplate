class Configuration:
    data = {
        'development':{
            'DEBUG': True,
            'IGNORE_AUTH': True,
            'SECRET_KEY': 'top-secret!',
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///dev.db'
        },
        'testing':{
            'DEBUG': False,
            'TESTING': True,
            'SECRET_KEY': 'top-secret!',
            'SERVER_NAME': 'example.com',
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'
        },
        'production':{
            'DEBUG': False,
            'SECRET_KEY': 'top-secret!',
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///prod.db'
        }
    }



