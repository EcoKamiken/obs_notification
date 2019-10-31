import obs_notification.mail

mail_object = obs_notification.mail.Email()


def test_noop():
    assert mail_object.noop() == (250, b'OK')
