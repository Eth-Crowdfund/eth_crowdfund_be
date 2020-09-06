import os


class Development(object):
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class Production(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class Testing(object):
  TESTING = True
  JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/eth_crowdfund_api_db_test"
  SQLALCHEMY_TRACK_MODIFICATIONS=False


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
