#!/bin/python3

import getopt
import secrets
import string
import sys
import os

def usage():
    print('Usage: %s [-v]' % sys.argv[0])
    print('%s generates .env file for docker setup' % sys.argv[0])
    print('Options')
    print('-v\t: generate .env file for venv setup instead.')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'v')
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)
        usage()
        sys.exit(2)

    dictionary = string.ascii_letters + string.digits + string.punctuation
    db_pass = ''.join(secrets.choice(dictionary) for i in range(64))
    web_pass = ''.join(secrets.choice(dictionary) for i in range(64))

    with open('.env', 'w') as f:
        f.write(f'DB_PASSWORD={db_pass}\n')
        f.write(f'WEB_PASSWORD={web_pass}\n')
        if opts:
            for o, a in opts:
                if o == '-v':
                    f.write('DB_ADDRESS=localhost\n')

        else:
            f.write('DB_ADDRESS=db\n')

    os.makedirs('merger/reports', exist_ok=True)
    os.makedirs('media/uploads', exist_ok=True)
    os.makedirs('static', exist_ok=True)
                    

if __name__ == "__main__":
    main()