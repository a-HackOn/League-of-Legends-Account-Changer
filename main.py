import os,shutil,psutil
from pathlib import Path
os.makedirs("logs", exist_ok=True)
os.system("type nul > logs\\t.me-violanesfan.txt")
import time
import logging
import league_client.shortcuts

os.system("title League Of Legends Auto Login  ^|  t.me/violanesfan")

accounts = {}
user = os.environ['USERPROFILE'][9:]
riot_exe = 'C:\\Riot Games\\Riot Client\\RiotClientServices.exe'
league_lockfile = 'C:\\Riot Games\\League of Legends\\lockfile'
riot_lockfile = f'C:\\Users\\{user}\\AppData\\Local\\Riot Games\\Riot Client\\Config\\lockfile'
riot_process = ["LeagueCrashHandler.exe","League of Legends.exe","LeagueClientUxRender.exe","LeagueClientUx.exe","LeagueClient.exe","RiotClientServices.exe"]
def close_riot():
    for process_name in riot_process:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                try:
                    psutil.Process(process.info['pid']).terminate()
                    print(f"    Process '{process_name}' terminated successfully.")
                except Exception as ec:
                    print(f"    Error terminating process '{process_name}': {ec}")
file_to_remove = [R"C:\ProgramData\Riot Games",
		R"C:\ProgramData\Riot Games\machine.cfg",
		R"C:\Riot Games\League of Legends\Logs",
		R"C:\Riot Games\League of Legends\debug.log",
		R"C:\Riot Games\Riot Client\UX\natives_blob.bin",
		R"C:\Riot Games\Riot Client\UX\snapshot_blob.bin",
		R"C:\Riot Games\Riot Client\UX\v8_context_snapshot.bin",
		R"C:\Riot Games\Riot Client\UX\icudtl.dat"]
appdata = Path.home() / "AppData" / "Local" / "Temp" / "Riot Games"
file_to_remove.append(appdata)
def rm_logs():
    for path in file_to_remove:
        if os.path.isfile(path):
            os.remove(path)
            print(f'    Removed file: {path}')
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f'    Removed directory and its contents: {path}')
        else:
            print(f'    Error: {path} does not exist or is not a file or directory.')
try:
    with open('accs.txt', 'r') as file:
        for line in file:
            login, password = line.strip().split(',')
            accounts[login] = password
except FileNotFoundError:
    print("accs.txt File not found! Please make one :)")
    input()
    exit()

print("Select an account:")
logins = list(accounts.keys())

for i, login in enumerate(logins, 1):
    print(f"[{i}] {login}")

while True:
    selected_acc = input("")
    try:
        selected_acc = int(selected_acc)
        print("account selected, removing logs first")
        print("  Closing riot processes first :)")
        close_riot()
        print("  Done!\n  Removing Riot logs now :) (ignore errors)")
        time.sleep(2)
        rm_logs()
        print("  done, recommended to open riot client if it doesnt open by itself")
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
print("all done)\nhf!")
