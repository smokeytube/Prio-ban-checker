# Prio ban checker
 Checks if a player is banned from donate.2b2t.org

![picture of the multi](https://i.imgur.com/595WGOr.png)
![picture of the single](https://i.imgur.com/3OQhuw6.png)

## Installation

1. Install Python3 if you don't already have it
2. Install requests if you don't already have it
```
pip3 install requests
```
## Usage

### Single

1. Run PrioBanChecker-Single.py
2. Follow the instructions the program gives you

### Multi

WARNING: Proxies don't really work because of cloudflare. Once one ip has been banned, other ips take much less time to be banned.

1. Make a list of usernames and put it in usernames.txt
2. If using proxies, put a list off http proxies in proxies.txt
3. Run PrioBanChecker-Multi.py
4. Wait for the program to finish checking
5. Open checked_usernames.txt
