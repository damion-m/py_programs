import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed(os.urandom(1024))

url = ''

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects=False, data = {
        'pinf_uio_app%2Fstructure%2Fpublic%2Flogin_login__username_value': username,
        'pinf_uio_app%2Fstructure%2Fpublic%2Flogin_login__password_value': password

        })

    print ('sending username %s and password %s' % (username, password))
