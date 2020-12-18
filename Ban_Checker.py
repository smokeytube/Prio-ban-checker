import requests
from colorama import Fore, init
import threading


title = """
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
 ██████╗ ██████╗ ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
 ██╔══██╗██╔══██╗██║██╔═══██╗    ██╔══██╗██╔══██╗████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
 ██████╔╝██████╔╝██║██║   ██║    ██████╔╝███████║██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
 ██╔═══╝ ██╔══██╗██║██║   ██║    ██╔══██╗██╔══██║██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
 ██║     ██║  ██║██║╚██████╔╝    ██████╔╝██║  ██║██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                                    by BGP#0419
"""

print(Fore.GREEN + title)

while True:
    usern = input(Fore.GREEN + "Username of 2b2t player: ")
    with open('usernames.txt', 'w') as usernamelist:
        usernamelist.write(usern)


    init(convert=True)
    lines = [item.replace("\n", "") for item in open('usernames.txt', 'r').readlines()]
    lines1 = lines[:len(lines)//2]
    lines2 = lines[len(lines)//2:]
    threads = []

    def check(input):
        data = f'ign={input}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

        request = requests.request('POST', "https://donate.2b2t.org/category/738999", data=data, headers=headers)
        if 'rate limited' in request.text:
            print(Fore.LIGHTMAGENTA_EX + f"YOU'VE BEEN RATELIMITED!! :(")
        elif 'not a valid' in request.text:
            print(Fore.LIGHTRED_EX + f"{input} is not a valid username")
        elif 'Unable' in request.text:
            print(Fore.LIGHTRED_EX + f"Unable to find a player with the username: {input}")
        elif 'banned' not in request.text:
            print(Fore.LIGHTRED_EX + f"{input} is not currently banned")
        else:
            print(Fore.LIGHTGREEN_EX + f"{input} is currently banned")


    def l1():
        for i in range(len(lines1)):
            check(lines1[i])
    def l2():
        for i in range(len(lines2)):
            check(lines2[i])

    t1 = threading.Thread(target=l1)
    t2 = threading.Thread(target=l2)
    threads.append(t1)
    threads.append(t2)
    t1.start()
    t2.start()

    for x in threads:
        x.join()
