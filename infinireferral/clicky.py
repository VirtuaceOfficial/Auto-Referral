import html
import http
import urllib
import pysocks
import socket
import requests
import urllib.request

from dotenv import load_dotenv
load_dotenv()

import os
token = os.environ.get("api-token")

#Set number of times to loop program
#num = input("Enter desired amount of requests: \n")
num = 20
for x in range(num):
    from bs4 import BeautifulSoup
    from stem import Signal
    from stem.control import Controller
    from urllib.request import urlopen

    #Create Tor proxychain session
    def get_tor_session():
        session = requests.session()
        session.proxies = {'http': 'socks5://127.0.0.1:9050',
                            'https': 'socks5://127.0.0.1:9050'}
        return session
    session = get_tor_session() 
    print("\nYour IP: \n")
    print(session.get('https://api.ipify.org/').text)
    print(requests.get('https://api.ipify.org/').text) 

    #Test URL Response
    try:
        r = requests.get("https://genfanad.com/refer/98954c19")
        print("\nStatus Request Code: ")
        print(r.status_code)
        print("\n---------------")
    except requests.ConnectionError:
        print("\nFailed To Connect")
    
    
    def renew_connection():
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password="password")
            controller.signal(Signal.NEWNYM)
        session = get_tor_session()
        print(session.get('https://api.ipify.org/').text)
