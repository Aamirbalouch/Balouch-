Skip to content
Aamirbalouch
/
Aamir-Balouch-
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Aamir-Balouch-/Aamir-Balouch.py
@Aamirbalouch
Aamirbalouch Create Aamir-Balouch.py
 1 contributor
608 lines (569 sloc)  30 KB
#!/usr/bin/python2
#coding=utf-8
 
 
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
 
 
def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
 
 
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
 
 
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
 
 
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)
 
 
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;97mToken\033[1;91m : \033[1;95mCopy👉 \033[1;92mEAAAAUaZA8jlABAEZBmW0yH8w0R2XhpqqNiaQvKDkm1wCFazEcrJEzJThJrjZC3fuBFP6DFNmNnZB8ueUyVZCH7zPMulcTHZBa9ZCRHTTRTc0wneLqx5BZBruQbJQAx5pssqNnZB9qH6oHFjqWJf0yoOFkawm7hDqVYM8wCALx4xv7hi4ERoBPpgSGKAsm95Xt8fcZD \033[1;96m👈 Without fb ID free login Copy Paste & Enter👉\033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		Name = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
 
 
#### LOGO ####
logo = """
\033[1;94m
\033[1;31m\033[1;31m╔══════════════════════════════════════════════════╗
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* AUTHOR  : \033[1;39mCREATOR AAMIR BALOUCH                   \033[1;31m║
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* WHATSAPP +923338219773: \033[1;39m  + 🌷🌷🌷 \033[1;31m║
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* GITHUB  : \033[1;39mhttps://github.com/Aamirbaloch786        \033[1;31m║
\033[1;31m\033[1;31m╚══════════════════════════════════════════════════╝"""
 
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mLoging In \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)
 
 
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
 
os.system("clear")
print "\033[1;96m•◈•───────────────•◈•\033[1;92🌹🌷AAMIR BALOUCH \033[1;96m•◈•───────────────•◈•"
print  """
 
\033[1;91m ________¶¶¶¶¶¶¶¶_____________¶¶¶¶¶¶¶¶
\033[1;91m _______¶¶¶______¶¶_________¶¶______¶¶¶
\033[1;91m ______¶¶¶¶________¶¶_____¶¶________¶¶¶¶
\033[1;91m _______¶¶¶______¶¶__¶¶¶¶¶__¶¶______¶¶¶
\033[1;91m _________¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶
\033[1;91m ____________¶¶¶¶__¶¶¶¶¶¶¶¶¶__¶¶¶
\033[1;91m __________¶¶¶¶¶¶¶¶__¶¶¶¶¶__¶¶¶¶¶¶¶¶
\033[1;91m ______¶¶¶¶¶¶¶¶______¶¶¶¶¶______¶¶¶¶¶¶¶¶
\033[1;91m ___¶¶¶¶¶¶¶¶__________¶¶¶__________¶¶¶¶¶¶¶¶
\033[1;91m _____________________¶¶¶
\033[1;91m _______¶¶¶¶¶¶¶¶¶¶____¶¶¶____¶¶¶¶¶¶¶¶¶¶
\033[1;91m _____¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;91m ___¶¶____________¶¶¶¶__¶¶¶¶____________¶¶
\033[1;91m __¶¶¶______________¶¶¶¶¶¶______________¶¶¶
\033[1;91m _¶¶¶¶_______¶¶¶¶¶¶¶__¶¶__¶¶¶¶¶¶¶_______¶¶¶¶
\033[1;91m _¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶
\033[1;91m _¶¶¶¶____¶¶¶¶______¶¶¶¶¶¶______¶¶¶¶____¶¶¶¶
\033[1;91m _¶¶¶¶____¶¶¶¶________¶¶________¶¶¶¶____¶¶¶¶
\033[1;91m __¶¶¶_____¶¶¶____¶¶¶¶¶¶¶¶¶¶____¶¶¶_____¶¶¶
\033[1;91m ___¶¶¶¶____¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶____¶¶¶¶
\033[1;91m _____¶¶¶¶____¶¶¶¶____¶¶____¶¶¶¶____¶¶¶¶
\033[1;91m _______¶¶¶¶____¶¶¶¶______¶¶¶¶____¶¶¶¶
\033[1;91m _________¶¶¶¶____¶¶¶¶__¶¶¶¶____¶¶¶¶
\033[1;91m ___________¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶
\033[1;91m _____________¶¶¶¶____¶¶____¶¶¶¶
\033[1;91m _______________¶¶¶¶______¶¶¶¶
\033[1;91m _________________¶¶¶¶__¶¶¶¶
\033[1;91m ___________________¶¶¶¶¶¶                   LOVE  HACKER
\033[1;91m ____________________.¶¶
\033[1;91m ___________________¶¶¶¶¶¶
\033[1;91m ____________¶¶¶¶¶¶¶__¶¶__¶¶¶¶¶¶¶
\033[1;91m __________¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶
\033[1;91m _________¶¶¶¶______¶¶¶¶¶¶______¶¶¶¶
\033[1;91m _________¶¶¶¶________¶¶________¶¶¶¶
\033[1;91m __________¶¶¶____¶¶¶¶¶¶¶¶¶¶____¶¶¶
\033[1;91m ___________¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶
\033[1;91m _____________¶¶¶¶____¶¶____¶¶¶¶
\033[1;91m _______________¶¶¶¶______¶¶¶¶
\033[1;91m _________________¶¶¶¶__¶¶¶¶
\033[1;91m ___________________¶¶¶¶¶¶
\033[1;91m _____________________¶¶
\033[
