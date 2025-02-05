import argparse
import sys
import os

def clear():
    # Clear the terminal screen (works for Windows, macOS, and Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the screen.
clear()

# ANSI escape sequences for colors and styles
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


# Your custom banner (which can also serve as your help message)
BANNER = f""" {BLUE}|- {YELLOW}{BOLD}Created by github.com/zebbern{GREEN}
 ╔═══════════════════════════════════════╗
 ║ {YELLOW}-g{BLUE} |{CYAN} Dorking via Google{GREEN}               ║
 ║                                       ║
 ║ {YELLOW}-p{BLUE} |{CYAN} Fetches and saves proxies.{GREEN}       ║
 ║                                       ║
 ║ {YELLOW}-s{BLUE} |{CYAN} Search for exposed SCADA systems{GREEN} ║
 ║                                       ║
 ║ {YELLOW}-t{BLUE} |{CYAN} Dorking via Tor (port 9050){GREEN}      ║
 ╚═══════════════════════════════════════╝
 
 {BLUE}|- python main.py -p -g
 {WHITE}To Use Proxies Meanwhile Dorking{RESET}"""

parser = argparse.ArgumentParser(
    prog="main.py",
    add_help=False,           # Do not add the default -h/--help.
    usage=argparse.SUPPRESS,  # Suppress the default usage string.
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument("-h", "--help", action="store_true", help=argparse.SUPPRESS)
# Add other arguments with their help texts suppressed.
parser.add_argument("-g", "--google", help=argparse.SUPPRESS, action='store_true')
parser.add_argument("-s", "--scada", help=argparse.SUPPRESS, action='store_true')
parser.add_argument("-t", "--tor", help=argparse.SUPPRESS, action='store_true')
parser.add_argument("-p", "--proxy", help=argparse.SUPPRESS, action='store_true')

args = parser.parse_args()

# If user requests help explicitly OR gave no arguments
if args.help or len(sys.argv) == 1:
    print(BANNER)
    parser.print_help()
    sys.exit(0)

# Otherwise, run whatever modes they asked for
if args.proxy:
    from Modes import Proxy

if args.google:
    from Modes import Gmode

if args.scada:
    from Modes import Scada

if args.tor:
    from Modes import Tor
