# Created by Ericarthurc
# February 2/10/2020
# Version 0.0.2 (3/2/2020)

import sys
import os
import time

import paramiko
from colorama import Back, Fore, Style, init

from conf import conf

# If using .dev for env variables
# from dotenv import load_dotenv
# from pathlib import Path
# env_path = Path('config') / '.env'
# load_dotenv(dotenv_path=env_path, override=True)
init()


def print_slow(str, x):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(x)


def connect():
    print(Fore.WHITE, end="")
    print(Back.GREEN, end="")
    print('Live Stream Debugger 0.0.1 - Ericarthurc')
    print(Style.RESET_ALL, end="")
    print(Fore.CYAN, end="")
    print_slow('Connecting to server!', 0.04)
    print(Style.RESET_ALL, end="")
    time.sleep(1)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect("SEVRER IP", username="USERNAME",
                       password="PASSWORD")
    except:
        print(Fore.RED, end="")
        print()
        print_slow(
            'Connection to server failed? Contact System Manager...', 0.06)
        print(Style.RESET_ALL, end="")
        time.sleep(1)
        sys.exit(0)
    os.system('cls')
    menu(client)


def menu(client):
    while True:
        print(Fore.WHITE, end="")
        print(Back.GREEN, end="")
        print("Live Stream Debugger 0.0.1 - Ericarthurc")
        print(Style.RESET_ALL, end="")
        print(Fore.GREEN, end="")
        print("Main Menu:")
        print("1. Update stream keys")
        print("2. Restart streaming processes")
        print("3. Exit program")
        print(Style.RESET_ALL, end="")
        val = input("Select option [1, 2, 3]: ")

        if val == '1':
            youtube = input("Input YouTube stream key: ")
            facebook = input("Input Facebook stream key: ")
            sftp = client.open_sftp()
            sftp.chdir(path=r'/usr/local/nginx/conf')
            client.exec_command(
                'cp /usr/local/nginx/conf/nginx.conf /usr/local/nginx/conf/nginx.conf.BACKUP')
            file = sftp.file('nginx.conf', 'w', 1)
            file.write(conf(youtube, facebook))
            file.flush()
            print(Fore.CYAN, end="")
            print_slow(
                'Stream keys written to configuration file!', 0.06)
            client.exec_command('/usr/local/nginx/sbin/nginx -s stop')
            client.exec_command('/usr/local/nginx/sbin/nginx')
            print('')
            print_slow(
                'Processes restarted!', 0.06)
            print(Style.RESET_ALL, end="")
            time.sleep(1)
            os.system('cls')
        elif val == '2':
            client.exec_command('systemctl restart stunnel4')
            client.exec_command('systemctl restart nginx')
            client.exec_command('/usr/local/nginx/sbin/nginx -s stop')
            client.exec_command('/usr/local/nginx/sbin/nginx')
            print(Fore.CYAN, end="")
            print_slow(
                'Processes restarted!', 0.06)
            print(Style.RESET_ALL, end="")
            time.sleep(1)
            os.system('cls')
        elif val == '3':
            print(Fore.RED, end="")
            print_slow(
                'Program closing...', 0.04)
            print(Style.RESET_ALL, end="")
            time.sleep(1)
            sys.exit(0)


if __name__ == "__main__":
    connect()
