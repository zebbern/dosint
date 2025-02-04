# DOSINT

DOSINT is an efficient OSINT (Open-Source Intelligence) tool designed for conducting various forms of dorking and reconnaissance. 
It streamlines information discovery through Google, SCADA-focused queries, Tor searches, and proxy-based reconnaissance all within a single tool.

## Features

- **Google Dorking**: Automates Google search queries to uncover sensitive information.
- **SCADA Searches**: Targets industrial control systems using specialized dorks.
- **Tor Mode**: Uses onion search engines through a local Tor proxy for deep web exploration.
- **Proxy Finder**: Finds and tests public proxies, saving them in a clean format for easy use.

## Requirements

- **Python 3.8+**
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- *(Optional)* Tor must be running locally on port **9050** if using Tor mode.

## Usage

Run the following command to access help and usage examples:

```bash
python dosint.py -h
```

### Command-line Options

```
usage: dosint.py [-h] [-g] [-s] [-t] [-p]

optional arguments:
  -h, --help     Show this help message and exit.
  -g, --google   Enable Google dorking mode.
  -s, --scada    Enable SCADA/PLC-focused search mode.
  -t, --tor      Enable Tor-based search mode.
  -p, --proxy    Enable Proxy finder mode.
```

### Examples

- **Google Dorking:**  
  ```bash
  python dosint.py -g
  ```
  Runs Google dorking mode to execute a single or multiple dorks from a file.

- **Google Dorking with Proxy:**  
  ```bash
  python dosint.py -p -g
  ```
  Finds public proxies first, then automatically utilizes them for Google dorking.

- **SCADA Searches:**  
  ```bash
  python dosint.py -s
  ```
  Performs reconnaissance on SCADA/PLC systems using specific search queries.

- **Tor Mode:**  
  ```bash
  python dosint.py -t
  ```
  Searches the dark web via Tor onion search engines.

> [!WARNING]
This tool is provided for **educational and authorized security testing purposes only**.  
Users must **obtain proper authorization** before scanning or performing reconnaissance activities.  
Misuse of this tool may violate laws and regulations use responsibly.
