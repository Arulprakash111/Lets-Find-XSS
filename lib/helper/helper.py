'''
Lets-Find-XSS - 2024
This project was created by Arul Prakash R with Cyber Security team. 
Copyright under the MIT license
'''
import requests, json
##### Warna ####### 
N = '\033[0m'
W = '\033[1;37m' 
B = '\033[1;34m' 
M = '\033[1;35m' 
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m' 
##### Styling ######
underline = "\033[4m"
##### Default ######
agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
line="—————————————————" 
#####################
def session(proxies,headers,cookie):
	r=requests.Session()
	r.proxies=proxies
	r.headers=headers
	r.cookies.update(json.loads(cookie))
	return r

logo=G+"""
__  ______ ____        _   _ _   _ _   _ _____ _____ ____  
\ \/ / ___/ ___|      | | | | | | | \ | |_   _| ____|  _ \%s
 \  /\___ \___ \ _____| |_| | | | |  \| | | | |  _| | |_) |
 /  \ ___) |__) |_____|  _  | |_| | |\  | | | | |___|  _ < 
/_/\_\____/____/      |_| |_|\___/|_| \_| |_| |_____|_| \_\%s
<<<<<<< CREATED BY ARUL PRAKASH R
"""%(R+"{v0.5 Final}"+G,underline+C+"https://github.com/Arulprakash111/Lets-Find-XSS"+N+G)
	
##=======
"""%(R+"{v0.5 Final}"+G,underline+C+"https://github.com/Arulprakash111/Lets-Find-XSS"+N+G)
	
>>>>>>> branch 'master' of https://github.com/Arulprakash111/Lets-Find-XSS
"""
