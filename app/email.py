from flask import Flask, render_template, url_for
from flask_mail import Mail, Message
from . import mail
import os

def send_verification_email(to_email, token):
    verify_url = url_for('auth.confirm', token=token, _external=True)
    sender_name = "软件工程第四组"
    sender_email = os.getenv('MAIL_USERNAME')
    sender = (sender_name, sender_email)
    subject = 'AI 教学双端邮箱验证'
    message = Message(subject, sender=sender, recipients=[to_email])
    message.body = f'点击这里验证你的邮箱:{verify_url}'
    mail.send(message)



