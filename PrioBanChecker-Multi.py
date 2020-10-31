import os.path
import requests

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

def check(input):
    if len(input) < 3:
        print('\nUnable to find a player with that username')
    else:
        data = f'ign={input}'
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
            }

        request = requests.request('POST', "https://donate.2b2t.org/category/738999", data=data, headers=headers)
        if 'banned' in request.text:
            print((f"{input} is currently banned").center(119))
            open('checked_usernames.txt', 'a').write(input)
        else:
            print((f"{input} is not currently banned").center(119))

if os.path.exists('usernames.txt'):
    open('checked_usernames.txt', 'w').close()
    print(title)
    print(('By BGP#0419\n'.center(119)))
    file = open('usernames.txt', 'r')
    while 0 == 0:
        username = file.readline().replace('\n', '')
        if username == '':
            print(('Checked all usernames!').center(119))
            break
        else:
            check(username)
    input('Press enter to close')
else:
    open('usernames.txt', 'a')
    print('Put a list of usernames in "usernames.txt", then run the program again')
    input('Press enter to close')