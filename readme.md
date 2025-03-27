# 🔥 基于 RAG 检索的 DeepSeek 智能教学双端系统

[](https://img.shields.io/badge/Flask-3.1.0-000000?style=flat&logo=flask)

[](https://img.shields.io/badge/React-18.2.0-61DAFB?style=flat&logo=react)

[](https://img.shields.io/badge/Python-3.12.9-3776AB?style=flat&logo=python)

[](https://img.shields.io/badge/SQLAlchemy-3.1.1-000000?style=flat&logo=sqlalchemy)

## 🚀 项目介绍

本项目是一个基于 **RAG (Retrieval-Augmented Generation)** 检索技术的智能教学系统，采用 **Flask** + **React** 双端架构。系统利用 **DeepSeek** 的强大语言模型能力，结合教学知识库检索，为学生提供智能化的学习辅导体验。

## 🏗️ 项目结构

```
├── app/                      # Flask 应用核心
│   ├── __init__.py           # 应用工厂
│   ├── models.py             # 数据库模型
│   ├── extensions.py         # Flask扩展初始化
│   ├── email.py              # 邮件功能
│   ├── static/               # 静态文件
│   ├── templates/            # Jinja2模板
│   │   ├── auth/             # 认证相关模板
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── email/        # 邮件模板
│   │   ├── base.html         # 基础模板
│   │   ├── index.html        # 首页
│   │   └── user.html         # 用户页面
│   └── blueprints/           # 蓝图模块
│       ├── auth/             # 认证蓝图
│       │   ├── __init__.py
│       │   ├── forms.py      # 表单定义
│       │   └── views.py      # 视图函数
│       └── main/             # 主蓝图
│           ├── __init__.py
│           ├── errors.py     # 错误处理
│           └── views.py      # 主视图
├── migrations/               # 数据库迁移
│   ├── versions/            # 迁移脚本
│   ├── env.py               # 迁移环境
│   └── alembic.ini          # 迁移配置
├── tests/                   # 测试代码
│   ├── test_send_email.py   # 邮件测试
│   └── test_user_model.py   # 用户模型测试
├── config.py                # 应用配置
├── app.py                   # 应用入口
├── requirements.txt         # Python依赖
├── test.py                  # 测试入口
└── README.md                # 项目文档

```

## 🛠️ 技术栈

- **后端框架**: Flask 3.1.0
- **前端框架**: React 18.2.0 (前端项目应单独存放)
- **数据库**: SQLAlchemy 3.1.1
- **认证系统**: Flask-Login
- **表单处理**: Flask-WTF
- **邮件支持**: Flask-Mail
- **数据库迁移**: Flask-Migrate + Alembic
- **测试框架**: pytest (可选)

## 🏗️ 环境配置

### 1. 克隆仓库

```bash
git clone https://github.com/BlueMAX111/-RAG-DeepSeek-.git
cd -RAG-DeepSeek-
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate    # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

创建`.env`文件(参考`.env.example`):

```python
FLASK_CONFIG=developmen
SECRET_KEY=your-secret-key-here
DEV_DATABASE_URL=sqlite:///dev.db
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-email-password
```

### 5. 初始化数据库

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 6. 运行开发服务器

```bash
flask run --debug
```

## 🧪 运行测试

```bash
python test.py
# 或运行单个测试模块
python -m pytest tests/test_user_model.py
```

## 🔧 开发指南

### 创建新蓝图

1. 在`app/blueprints`下创建新目录
2. 创建`__init__.py`、`views.py`等必要文件
3. 在`app/__init__.py`中注册蓝图

### 添加新模型

1. 在`app/models.py`中定义新模型
2. 生成迁移脚本:

```bash
flask db migrate -m "add new model"
flask db upgrade
```

### 邮件系统使用

参考`app/email.py`和`app/templates/auth/email/`中的模板

## 🤝 贡献指南

1. Fork 项目仓库
2. 创建特性分支 (`git checkout -b feature/NewFeature`)
3. 提交更改 (`git commit -m 'Add NewFeature'`)
4. 推送到分支 (`git push origin feature/NewFeature`)
5. 创建 Pull Request