"""settings.py
config/settings.iniが存在しない場合自動生成する。
"""

import os

from configparser import ConfigParser


class AppConfig():
    def __init__(self):
        self.CURRENT_DIR = os.getcwd()
        self.DEFAULT_INI = os.path.join(
            self.CURRENT_DIR, 'obs_notification', 'config', 'default.ini')
        self.SETTINGS_INI = os.path.join(
            self.CURRENT_DIR, 'obs_notification', 'config', 'settings.ini')

        # default.ini
        self.default = ConfigParser()
        self.default.read(self.DEFAULT_INI)

        # settings.ini
        self.settings = ConfigParser()
        if os.path.isfile(self.SETTINGS_INI):
            self.settings.read(self.SETTINGS_INI)
        else:
            self.generate_settings()
            self.settings.read(self.SETTINGS_INI)

    def generate_settings(self):
        with open(self.SETTINGS_INI, 'w') as configfile:
            self.default.write(configfile)
