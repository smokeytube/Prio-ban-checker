import os.path
import requests
import threading
import random
import time
import ctypes

lines = open('usernames.txt').read().splitlines()

title = """
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
 ██████╗ ██████╗ ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
 ██╔══██╗██╔══██╗██║██╔═══██╗    ██╔══██╗██╔══██╗████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
 ██████╔╝██████╔╝██║██║   ██║    ██████╔╝███████║██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
 ██╔═══╝ ██╔══██╗██║██║   ██║    ██╔══██╗██╔══██║██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
 ██║     ██║  ██║██║╚██████╔╝    ██████╔╝██║  ██║██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

Banned = 0
Unbanned = 0
Finished = 0
LastTotal = 0

def random_line():
    return random.choice(lines)

def check(input):
    global Banned
    global Unbanned
    if len(input) < 3:
        print(f'\nUnable to find {input}')
    else:
        data = f'ign={input}'
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
            }

        request = requests.request('POST', "https://donate.2b2t.org/category/738999", data=data, headers=headers)
        if 'banned' in request.text:
            print((f"{input} is currently banned").center(119))
            line = f'{input}\n'
            open('checked_usernames.txt', 'a').write(line)
            Banned += 1
        else:
            print((f"{input} is not currently banned").center(119))
            Unbanned += 1

def start():
    while 0 == 0:
        usernames = open('usernames.txt').read()
        if usernames == '':
            break
        else:
            username = random_line()
            open('usernames.txt', 'w').write(usernames.replace(f"\n{username}", '').replace(username, ''))
            check(username)

def name():
    global Finished
    global LastTotal
    while Finished == 0:
        Speed = (((Banned + Unbanned) - LastTotal) / 3).__round__(2)
        ctypes.windll.kernel32.SetConsoleTitleW(f"BGP's Prio Ban Checker | Banned: {Banned} | Unbanned: {Unbanned} | Speed: {Speed}/s")
        LastTotal = Banned + Unbanned
        time.sleep(3)

print(title)
print(('By BGP#0419\n'.center(119)))

threads = []
open('checked_usernames.txt', 'w').write('')
numberofthreads = int(input('Enter amount of threads: '))
print('Loading threads...')
threading.Thread(target=name).start()
for i in range(numberofthreads):
    t = threading.Thread(target=start)
    threads.append(t)
    t.start()
    time.sleep(.1)
print(('\nFinished loading all threads.\n').center(119))
for x in threads:
    x.join()
Finished = 1
input(('Finished Checking! Press enter to close.').center(119))