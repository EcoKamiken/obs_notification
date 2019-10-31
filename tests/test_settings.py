import obs_notification.settings


def test_config():
    config = obs_notification.settings.AppConfig()
    assert config.default['test']['value'] == 'test'
