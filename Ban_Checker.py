import requests
from colorama import Fore, init
import random
import threading
import time
import ctypes

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

def check(input):
    data = f'ign={input}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

    request = requests.request('POST', "https://donate.2b2t.org/category/738999", data=data, headers=headers)
    if 'not a valid' in request.text:
        print(Fore.LIGHTRED_EX + f"{input} is not a valid username")
    elif 'Unable' in request.text:
        print(Fore.LIGHTRED_EX + f"Unable to find a player with the username: {input}")
    elif 'banned' not in request.text:
        print(Fore.LIGHTRED_EX + f"{input} is not currently banned")
    else:
        print(Fore.LIGHTGREEN_EX + f"{input} is currently banned")

print(Fore.LIGHTWHITE_EX + title)
lines = [item.replace("\n", "") for item in open('usernames.txt', 'r').readlines()]
for i in range(len(lines)):
    check(lines[i])
input(Fore.RESET + 'Finished Checking!')