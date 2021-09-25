import requests
import random
proxylist = 'proxy.txt'

if proxylist:

    openfile = open(proxylist).read().splitlines()

    randomlin = random.choice(openfile)

    proxy = {'http': 'http://{0}'.format(randomlin)}

    print(proxy)

else:

    proxy = None


requests.get('http://fugu.co.il', proxies=proxy)

