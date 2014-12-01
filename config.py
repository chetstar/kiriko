CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'chetmeinzersf'
# MAIL_PASSWORD = str(os.environ.get('cpw'))
MAIL_PASSWORD = 'sensitive'

# administrator list
# ADMINS = ['chetstar@gmail.com']