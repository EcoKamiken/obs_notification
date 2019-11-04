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

email_object.create_mime(subject, body)
email_object.send()
