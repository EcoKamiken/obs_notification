#!/usr/bin/env python
"""mail.py
"""

from smtplib import SMTP_SSL
from logzero import logger

from obs_notification.settings import AppConfig


class Email():
    def __init__(self):
        config = AppConfig()
        self.smtp_host = config.settings['smtp'].get('host')
        self.subject = ''
        self.body = ''
        self.from_addr = config.settings['mail'].get('from')
        self.to_addr = config.settings['mail'].get('to')
        self.cc_addr = config.settings['mail'].get('cc')

    def show_vars(self):
        print(self.smtp_host)
        print(self.subject)
        print(self.body)
        print(self.from_addr)
        print(self.to_addr)
        print(self.cc_addr)

    def send(self):
        # TODO: do something
        logger.info('send')
        pass

    def noop(self):
        with SMTP_SSL(self.smtp_host, 465) as smtps:
            return smtps.noop()


if __name__ == '__main__':
    em = Email()
    em.show_vars()
