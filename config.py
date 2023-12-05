from decouple import config

class Config(object):
    SECRET_KEY = config('SECRET_KEY')
    TESTING = False
    # DB_SERVER = '192.168.1.56'


class DevelopmentConfig(Config):
    DEBUG = True

# class ProductionConfig(Config):
#     """Uses production database server."""
#     DB_SERVER = '192.168.19.32'

# class TestingConfig(Config):
#     DB_SERVER = 'localhost'
#     DATABASE_URI = 'sqlite:///:memory:'


config = {
    'development': DevelopmentConfig
}