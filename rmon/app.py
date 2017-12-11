#coding=utf-8

import os
import json
from flask import Flask
from flask_migrate import Migrate
#from flask_login import LoginManager

from rmon.views import apps, api
from rmon.models import db, User
from rmon.config import configs
from rmon.wx import wx_dispatcher




def register_extensions(app):
    # 初始化微信消息处理器
    wx_dispatcher.init_app(app)
    db.init_app(app)
    Migrate(app, db)


def register_blueprints(app):
    app.register_blueprint(apps)
    app.register_blueprint(api)

def get_config_from_file(app):
    file = os.environ.get('RMON_CONFIG', "")
    content = ""
    if not file:
        return
    try:
        with open(file) as f:
            for l in f:
                l = l.strip()
                if l.startswith('#'):
                    continue
                else:
                    content += l
    except IOError:
        raise Exception("IOError")
    try:
        data = json.loads(content)
    except:
        raise Exception("Config File Parser Error!")

    for key in data:
        app.config[key.upper()] = data.get(key)

def create_app(config):
    app = Flask("rmon")
    app.config.from_object(configs.get(config,"development"))
    # 从环境变量 RMON_SETTINGS 指定的文件中加载配置
    app.config.from_envvar('RMON_SETTINGS', silent=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    get_config_from_file(app)
    register_extensions(app)
    register_blueprints(app)

    # 如果是开发环境则创建所有数据库表
    if app.debug and not app.testing:
        with app.app_context():
            db.create_all()
            name, password = User.create_administrator()
            app.logger.debug('create administrator name/password %s/%s', name, password)

    return app
    return app