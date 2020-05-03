#!/bin/python3

import secrets
import string

dictionary = string.ascii_letters + string.digits + string.punctuation

db_pass = ''.join(secrets.choice(dictionary) for i in range(64))
web_pass = ''.join(secrets.choice(dictionary) for i in range(64))

with open('.env', 'w') as f:
    f.write('DB_PASSWORD=' + db_pass + '\n')
    f.write('WEB_PASSWORD=' + web_pass + '\n')