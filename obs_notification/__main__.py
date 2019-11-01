import obs_notification.mail

email_object = obs_notification.mail.Email()

subject = 'title'
body = '''
testestestetestsetes
testestestetestsetes
testestestetestsetes
testestestetestsetes
testestestetestsetes
testestestetestsetes
'''

email_object.set_subject(subject)
email_object.set_body(msg)
email_object.send()
