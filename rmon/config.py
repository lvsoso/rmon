#coding=utf-8

class BaseConfig(object):
    """ 配置基类 """
    SECRET_KEY = "OQR!YuiIZ0K5!NmqI1zy@S7x&ac5zJ9DAQhb"
    TEMPLATES_AUTO_RELOAD = True

class DevelopmentConfig(BaseConfig):
    """ 开发环境 """
    DEBUG = True
    # mysql
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/simpledu"
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    WX_TOKEN = 'wuqilv'
    # 替换微信公众号  app id
    WX_APP_ID = 'wx4f6a176ebb8183ac'
    # 替换成微信公众号 app secret
    WX_SECRET = 'faf7c0bba4dc1e6ca02da0bdc0feb537'


class ProductionConfig(BaseConfig):
    """ 生产环境配置 """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/rmon"

    WX_TOKEN = 'wuqilv'
    # 替换微信公众号  app id
    WX_APP_ID = 'wx4f6a176ebb8183ac'
    # 替换成微信公众号 app secret
    WX_SECRET = 'faf7c0bba4dc1e6ca02da0bdc0feb537'


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    pass



configs = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
