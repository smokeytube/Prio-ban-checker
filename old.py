import requests
import threading
import random
import time
import ctypes
import asyncio

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
Limited = 0
# Settings
UseProxies = 0

def random_proxy():
    lines = open('proxies.txt').read().splitlines()
    p = random.choice(lines)
    return p

def random_line():
    lines = open('usernames.txt').read().splitlines()
    return random.choice(lines)

def check(input):
    global Banned
    global Unbanned
    global Limited
    if len(input) < 3:
        print(f'\nUnable to find {input}')
    else:
        data = f'ign={input}'
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }

        if UseProxies == 0:
            request = requests.request('POST', "https://donate.2b2t.org/category/738999", data=data, headers=headers)
        else:
            proxy = {
                'https': f'{random_proxy()}'
            }
            try:
                request = requests.request('POST', "https://donate.2b2t.org/category/738999", proxies=proxy, timeout=10, data=data, headers=headers)
            except requests.exceptions.ProxyError:
                request = requests.request('POST', "https://donate.2b2t.org/category/738999", proxies=proxy, timeout=10, data=data, headers=headers)
        if 'banned' in request.text:
            print((f"{input} is currently banned").center(119))
            line = f'{input}\n'
            open('checked_usernames.txt', 'a').write(line)
            Banned += 1
        else:
            print((f"{input} is not currently banned").center(119))
            Unbanned += 1
        if request.status_code != 200:
            print('IP has been rate limited', request.status_code)
            if UseProxies == 1:
                proxylist = open('proxies.txt').read()
                open('proxies.txt', 'w').write(proxylist.replace(f'{proxy}',''))
            else:
                Limited += 1

def start():
    global Limited
    while Limited == 0:
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
if UseProxies == 1:
    print('You are using proxies. Change UseProxies to 0 to turn it off.')
elif UseProxies == 0:
    print('You are not using proxies. Change UseProxies to 1 to turn it on.')
else:
    print('Error loading proxy config. UseProxies must be "0" or "1".')

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