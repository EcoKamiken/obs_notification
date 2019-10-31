#!/usr/bin/env python
"""mail.py
"""

from smtplib import SMTP_SSL
from logzero import logger


class Email():
    def __init__(self):
        self.body = ''

    def send(self):
        # TODO: do something
        logger.info('send')
        pass

    def noop(self):
        with SMTP_SSL("smtp.lolipop.jp", 465) as smtps:
            return smtps.noop()


if __name__ == '__main__':
    mail_object = Email()
