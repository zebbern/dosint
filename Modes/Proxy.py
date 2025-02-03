import sys
import asyncio
import os

# Use the Windows SelectorEventLoop if on Windows (fixes aiodns error)
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from proxybroker import Broker
from termcolor import colored

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
{RED}██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
{RED}██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
{RED}██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ 
{RED}██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  
{RED}██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   
{RED}╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝
github.com/zebbern for more!{GREEN}

[+] Finding 25 working proxy servers saved results to proxies_cleaned.txt
[+] Starting...
----------------------------------------------------------------------------{WHITE}
"""
print(BANNER)

# Global set to hold cleaned proxy strings (to avoid duplicates)
cleaned_proxies = set()

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        # Build a clean string (e.g., "13.48.109.48:3128")
        cleaned = f"{proxy.host}:{proxy.port}"
        print("Found proxy: " + cleaned)
        cleaned_proxies.add(cleaned)

proxies = asyncio.Queue()
broker = Broker(proxies)

tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], limit=100),
    show(proxies)
)

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)

# Write the cleaned proxies to a text file.
with open("proxies_cleaned.txt", "w") as f:
    for cp in cleaned_proxies:
        f.write(cp + "\n")

print(colored('[+] Done. Cleaned proxies saved to proxies_cleaned.txt', 'green'))
