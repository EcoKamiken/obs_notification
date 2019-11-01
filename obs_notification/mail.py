#!/usr/bin/env python
"""mail.py
"""

import os

from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from logzero import logger

from obs_notification.settings import AppConfig


class Email():
    def __init__(self):
        # Load config
        config = AppConfig()

        # SMTP Settings
        self.smtp_host = config.settings['smtp'].get('host')
        self.smtp_user = os.environ.get('SMTP_USER')
        self.smtp_pass = os.environ.get('SMTP_PASS')

        # MIMEText
        self.charset = config.settings['mail'].get('charset')
        self.body = None
        self.msg = MIMEText(self.body, "plain", self.charset)
        self.msg['Subject'] = ''
        self.msg['From'] = config.settings['mail'].get('from')
        self.msg['To'] = config.settings['mail'].get('to')
        self.msg['Cc'] = config.settings['mail'].get('cc')
        self.msg['Bcc'] = None
        self.msg['Date'] = None

    def send(self, msg):
        with SMTP_SSL(self.smtp_host, 465) as smtps:
            smtps.login(self.smtp_user, self.smtp_pass)
            smtps.send_message(self.msg, self.from_addr, self.to_addr)

    def set_subject(self, subject):
        self.msg['subject'] = subject

    def set_body(self, body):
        self.msg['body'] = body

    def noop(self):
        with SMTP_SSL(self.smtp_host, 465) as smtps:
            return smtps.noop()
