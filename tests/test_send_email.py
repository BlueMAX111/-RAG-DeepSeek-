import unittest
import sys
from flask import url_for
from app import create_app, db
from app.models import User
from flask_mail import Mail
from unittest.mock import patch

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.mail = Mail(self.app)

        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        with self.app.app_context():
            user = User.query.filter_by(email="2331084642@qq.com")
            if user:
                db.session.delete(user)
                db.session.commit()
            db.session.remove()
            self.app_context.pop()
    
    @patch('app.email.mail.send')
    def test_register_user_sends_email(self, mock_mail_send):
        """测试注册用户时是否调用了邮件发送"""
        with self.app.test_request_context():
            url = url_for('auth.register')
        data = {
            "email": "2331084642@qq.com",
            "password": "TestPassword123",
            "confirm_password": "TestPassword123"
        }
        response = self.client.post(url_for("auth.register"), data=data)

        # 1. 确保请求成功
        self.assertEqual(response.status_code, 200)

        # 2. 检查数据库是否添加用户
        with self.app.app_context():
            user = User.query.filter_by(email="2331084642@qq.com").first()
            self.assertIsNotNone(user, "用户应该成功注册并添加到数据库")

            # 清理数据库
            db.session.delete(user)
            db.session.commit()

        # 3. 确保 `mail.send()` 被调用了一次
        mock_mail_send.assert_called_once()