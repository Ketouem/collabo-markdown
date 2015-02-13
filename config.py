class Config(object):
    SECRET_KEY = 'supersecretkey'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
