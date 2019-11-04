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
        logger.info('Create Email object')
        # Load config
        self.config = AppConfig()

        # SMTP Settings
        self.smtp_host = self.config.settings['smtp'].get('host')
        self.smtp_user = os.environ.get('SMTP_USER')
        self.smtp_pass = os.environ.get('SMTP_PASS')

    def create_mime(self, subject, body):
        logger.info('Create MIME')
        self.charset = self.config.settings['mail'].get('charset')
        self.body = body
        self.msg = MIMEText(self.body, "plain", self.charset)
        self.msg['Subject'] = subject
        self.msg['From'] = self.config.settings['mail'].get('from')
        self.msg['To'] = self.config.settings['mail'].get('to')
        self.msg['Cc'] = self.config.settings['mail'].get('cc')
        self.msg['Bcc'] = self.config.settings['mail'].get('bcc')
        self.msg['Date'] = None

    def send(self):
        logger.info('Send')
        with SMTP_SSL(self.smtp_host, 465) as smtps:
            smtps.login(self.smtp_user, self.smtp_pass)
            smtps.send_message(self.msg)

    def noop(self):
        logger.info('noop')
        with SMTP_SSL(self.smtp_host, 465) as smtps:
            return smtps.noop()
