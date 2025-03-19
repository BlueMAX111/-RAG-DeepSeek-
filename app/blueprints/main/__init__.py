from flask import Blueprint
main = Blueprint('main', __name__)      # 实例化Blueprint类
from . import views, errors           

# 应用路由保存在包里的 app/blueprints/views.py里，错误处理保存在app/blueprints/errors.py里