import requests
from termcolor import colored
from bs4 import BeautifulSoup
import re

BANNER = r"""
████████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   ██║   ██║██████╔╝
   ██║   ██║   ██║██╔══██╗
   ██║   ╚██████╔╝██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
   github.com/zebbern for more!
"""

print(BANNER)
print(colored('[!] Tor proxy must be on port 9050 ', 'yellow'))
print(colored('[+] Checking TOR... ', 'green'))

session = requests.session()
session.proxies = {
    'http':  'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}
# Verify Tor IP
try:
    ip_info = session.get('http://httpbin.org/ip', timeout=10)
    print(ip_info.text)
    print(colored('[+] Got session... ', 'green'))
except requests.RequestException:
    print(colored('[!] Could not connect via Tor. Check that Tor is running on port 9050.', 'red'))
    exit()

################################################################################
xquery = input("Please set your query : ")

def fetch_links(url):
    """ Fetch onion links from a given page. """
    try:
        page = session.get(url, timeout=15)
        soup = BeautifulSoup(page.text, 'html.parser')
        tags = soup.find_all('a', attrs={'href': re.compile("^http://")})
        for tag in tags:
            print(tag.get('href'))
    except requests.RequestException:
        print(colored(f"[!] Failed to retrieve {url}", "red"))

print()
# Example for Phobos
phobos = "http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion"
print(colored(f'[+] Searching in "Phobos" {phobos} ...', 'green'))

# Instead of manually calling pages 1..14, do it in a loop:
for p in range(1, 15):
    url = f"{phobos}/search?query={xquery}&p={p}"
    fetch_links(url)

print(colored('[+] Done from Phobos', 'yellow'))

# Similarly for TOR66, Tordex, etc.
# ...
