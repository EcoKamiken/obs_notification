import obs_notification.settings
import obs_notification.mail

config = obs_notification.settings.AppConfig()
em = obs_notification.mail.Email()
em.show_vars()
