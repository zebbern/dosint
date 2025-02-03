import os
import time
import random
import sys
from googlesearch import search
from termcolor import colored, cprint
from http import cookiejar  

# One-time definition of the custom cookie policy
class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = (lambda self, *args, **kwargs: False)
    netscape = True
    rfc2965 = hide_cookie2 = False

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

BANNER = f""""
{RED}███████╗███╗   ███╗ ██████╗ ██████╗ ███████╗
{RED}██╔════╝████╗ ████║██╔═══██╗██╔══██╗██╔════╝
{RED}███████╗██╔████╔██║██║   ██║██║  ██║█████╗  
{RED}╚════██║██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
{RED}███████║██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
{RED}╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
github.com/zebbern for more! 
{WHITE}
 Find online PLCs 
 Note: This may take some time...
"""

TLD_LIST = ["com","co.in","be","de","co.uk","ru"]

SCADA_QUERIES = [
    # (query, approximate_stop, label_for_progress)
    ('intitle:"Rockwell Automation" "Device Name" "Uptime"', 50, '20%'),
    ('inurl:dtm.html intitle:1747-L551', 50, '40%'),
    ('intitle:"Miniweb Start Page"', 50, '60%'),
    ('inurl:"Portal/Portal.mwsl"', 50, '80%'),
    ('inurl:/Portal0000.htm', 50, '100%')
]

def spinning_cursor(iterations=40, delay=0.1):
    """
    Simple text spinner for visual feedback.
    iterations: how many spins to do
    delay: time in seconds per spin
    """
    for _ in range(iterations):
        for cursor in "|/-\\":
            sys.stdout.write(cursor)
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write('\b')

print(BANNER)
print(colored('[+] Searching SCADA targets...\n', 'green'))

for query, stop_count, progress_label in SCADA_QUERIES:
    # Show spinner to simulate "in-progress"
    spinning_cursor(30, 0.05)  # You can adjust as you like

    tld = random.choice(TLD_LIST)
    print(colored(f'[+] Using TLD: {tld}', 'cyan'))
    for result in search(query, tld=tld, num=10, stop=stop_count, pause=2):
        print(colored('[+] Found > ', 'yellow') + result)

    print(colored(f'[+] {progress_label} done', 'green'))
    print(colored('[+] Sleeping for 3 seconds...', 'blue'))
    time.sleep(3)

print(colored('[+] All queries complete.', 'green'))
print(colored('[! >] Remember to delete any .google-cookie file if it exists.', 'red'))
