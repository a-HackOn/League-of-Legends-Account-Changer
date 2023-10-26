import os
os.makedirs("logs", exist_ok=True)
os.system("type nul > logs\\cześć.txt")
import time
import logging
import league_client.shortcuts

os.system("title League Of Legends Auto Login  ^|  t.me/violanesfan")

accounts = {}
user = os.environ['USERPROFILE'][9:]
riot_exe = 'C:\\Riot Games\\Riot Client\\RiotClientServices.exe'
league_lockfile = 'C:\\Riot Games\\League of Legends\\lockfile'
riot_lockfile = f'C:\\Users\\{user}\\AppData\\Local\\Riot Games\\Riot Client\\Config\\lockfile'

with open('accs.txt', 'r') as file:
    for line in file:
        login, password = line.strip().split(',')
        accounts[login] = password

print("Select an account:")
logins = list(accounts.keys())

for i, login in enumerate(logins, 1):
    print(f"[{i}] {login}")

while True:
    selected_acc = input("")
    try:
        selected_acc = int(selected_acc)
        if 1 <= selected_acc <= len(logins):
            break
    except ValueError:
        pass

login = logins[selected_acc - 1]
password = accounts[login]
league_client.shortcuts.login(login, password, riot_exe, riot_lockfile, league_lockfile)

print("Done, removing logs")

for handler in league_client.shortcuts.logger.handlers:
    if isinstance(handler, logging.handlers.RotatingFileHandler):
        handler.close()
        league_client.shortcuts.logger.removeHandler(handler)
os.system("rmdir /s /q logs")
