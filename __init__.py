import re
import os, sys
import time

# Add the parent directory to the sys.path

from tqdm import tqdm
from rich import print as rprint
from termcolor import colored
from pyfiglet import Figlet

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def print_banner():
    f = Figlet(font='slant')
    print(colored(f.renderText('M-Scanner\n'), 'red'))

print_banner()

def summary():
    print(colored('M-Scanner is a simple tool to scan for malicious content in files.\n', 'green'))

summary()

# Path: scanner.py

def scan_for_malicious_content(directory):
    malicious_patterns = [
        r'malware',
        r'trojan',
        r'virus',
        # Add more malicious patterns as needed
    ]
    
    for i in tqdm(range(100), desc="Scanning for malicious content", ascii=False, colour='green'):
        time.sleep(0.01)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                try:
                    content = f.read()
                except UnicodeDecodeError:
                    # This will skip files that are not text files
                    continue

            for pattern in malicious_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)

                if file_path == './__init__.py':
                    continue

                if file_path == './test__init__.py':
                    continue

                if matches:
                    rprint(f"Potential malicious content found in {file_path}: {matches}")
                    delete_files = input("Do you want to delete the files with malicious content? (y/n): ")
                    if delete_files == 'y':
                        os.remove(file_path)
                        rprint(f"{file_path} has been deleted")
                        break
                    else:
                        rprint(f"{file_path} has not been deleted")
                        break
                if not matches:
                    rprint(f"{file_path} is clean")

if __name__ == '__main__':
    scan_for_malicious_content('.')