import os,league_client.shortcuts
os.system("title League Of Legends Automatic Login  ^|  t.me/violanesfan")
accounts={}
user = os.environ['USERPROFILE'][9:]
n=0
riot_exe = 'C:\\Riot Games\\Riot Client\\RiotClientServices.exe'
league_lockfile = 'C:\\Riot Games\\League of Legends\\lockfile'
riot_lockfile = 'C:\\Users\\'+user+'\\AppData\\Local\\Riot Games\\Riot Client\\Config\\lockfile'
with open('accs.txt','r') as file:
    for line in file:
        login,password = line.strip().split(',')
        accounts[login] = password
print("Select an account:")
for login in accounts:
    n+=1 
    print("["+str(n)+"] "+login)
logins = list(accounts.keys())
while True:
    selected_acc = input("")
    try:
        selected_acc = int(selected_acc)
        if selected_acc > n or selected_acc < 1:
            continue
        else:
            break
    except Exception:
        continue
login = logins[int(selected_acc) -1]
password = accounts[login]
league_client.shortcuts.login(login,password,riot_exe,riot_lockfile,league_lockfile)