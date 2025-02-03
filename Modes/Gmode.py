import urllib.request
import ssl
import certifi
import socket

# Save original urlopen
_old_urlopen = urllib.request.urlopen

def urlopen_with_certifi(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, context=None):
    """
    Custom urlopen that enforces the use of certifi's CA bundle for SSL verification.
    """
    if context is None:
        context = ssl.create_default_context(cafile=certifi.where())
    return _old_urlopen(url, data=data, timeout=timeout, context=context)

# Monkey-patch urllib.request.urlopen with our custom version.
urllib.request.urlopen = urlopen_with_certifi
# === End SSL Context Patch ===

import os
import random
import warnings
from termcolor import colored
from http import cookiejar
import requests
from googlesearch import search

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = (lambda self, *args, **kwargs: False)
    netscape = True
    rfc2965 = hide_cookie2 = False

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
UNDERLINE = "\033[4m"

BANNER = f"""
{RED} ██████╗ ███╗   ███╗ ██████╗ ██████╗ ███████╗
{RED}██╔════╝ ████╗ ████║██╔═══██╗██╔══██╗██╔════╝
{RED}██║  ███╗██╔████╔██║██║   ██║██║  ██║█████╗  
{RED}██║   ██║██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
{RED}╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
{RED} ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
github.com/zebbern for more!
"""
print(BANNER)

# 1) Prompt for single dork or file with multiple dorks
dork_input = input(colored('[>] Enter a single dork OR dorks.txt for multiple dorks: ', 'green'))

if os.path.exists(dork_input):
    # The user provided a file path; read it for multiple dorks
    with open(dork_input, "r", encoding="utf-8") as f:
        queries = [line.strip() for line in f if line.strip()]
    print(colored(f"[+] Loaded {len(queries)} dorks from '{dork_input}'.", "cyan"))
else:
    # The user provided a single dork
    queries = [dork_input]

# 2) Prompt for how many links to fetch per dork
try:
    limit_str = input(colored('[>] How many links to fetch per dork? ', 'green'))
    limit = int(limit_str)
except ValueError:
    print(colored("[!] Invalid input, defaulting to 20 links.", "red"))
    limit = 20

TLD = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]

# Create a requests session that blocks cookies.
s = requests.Session()
s.cookies.set_policy(BlockAll())

# Process each dork in turn.
for query in queries:
    print("\n" + colored(f"[DORK] {query}", "yellow"))
    tld_choice = random.choice(TLD)
    print(colored(f"Using random TLD: {tld_choice}", "cyan"))

    # 'num=10' is how many results per page, 'stop=limit' is total results,
    # 'pause=2' is the delay in seconds between requests to avoid being blocked.
    for idx, result in enumerate(search(query, tld=tld_choice, num=10, stop=limit, pause=2), start=1):
        print(colored(f'[{idx}] ', 'yellow') + result)

print(colored('\n[+] All searches complete.', 'green'))
print(colored('[! >] Delete .google-cookie file in dosint DIR if present', 'red'))