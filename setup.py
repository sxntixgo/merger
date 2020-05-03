#!/bin/python3

import getopt
import secrets
import string
import sys

def usage():
    print('Usage: %s [-d | -v]')
    print('Options')
    print('-d\t: generate .env file for docker setup. Default.')
    print('-v\t: gemerate .env file for venv setup.')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'dhv', ['--help'])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)
        usage()
        sys.exit(2)
    

    for o, a in opts:
        if o in ('-d', '-v'):
            dictionary = string.ascii_letters + string.digits + string.punctuation
            db_pass = ''.join(secrets.choice(dictionary) for i in range(64))
            web_pass = ''.join(secrets.choice(dictionary) for i in range(64))
            with open('.env', 'w') as f:
                f.write('DB_PASSWORD=' + db_pass + '\n')
                f.write('WEB_PASSWORD=' + web_pass + '\n')
                if o == '-v':
                    f.write('DB_ADDRESS=localhost' + '\n')
                else:
                    f.write('DB_ADDRESS=db' + '\n')
            print('.env file created')
            if o == '-v':
                print('Execute "for i in `cat .env`; do export $i; done"')
        elif o in ('-h', '--help'):
            usage()
            sys.exit()
        else:
            assert False, 'unhandled option'

if __name__ == "__main__":
    main()