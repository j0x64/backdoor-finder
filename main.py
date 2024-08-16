# Backdoor Finder created by JordanIsADev
# https://github.com/jordanisadev

# Import necessary libraries
from os import system as command
import os
import sys
from time import sleep
import subprocess

# Function to install the package if not found
def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Check if a library is already installed or not
try:
    import colorama
    colorama.init()  # Initialize colorama if needed
except ImportError:
    print("Colorama not found. Installing...")
    install_package('colorama')
    import colorama
    colorama.init()
    print("Colorama has been installed and initialized.")


# Initialize command line color
resetStyle = colorama.Style.RESET_ALL
foreGreen = colorama.Fore.GREEN
foreRed = colorama.Fore.RED
foreYellow = colorama.Fore.YELLOW
foreWhite = colorama.Fore.WHITE

# Define some variables
banner = r'''
  _         _  __ _           _           
 | |       | |/ _(_)         | |          
 | |__   __| | |_ _ _ __   __| | ___ _ __ 
 | '_ \ / _` |  _| | '_ \ / _` |/ _ \ '__|
 | |_) | (_| | | | | | | | (_| |  __/ |   
 |_.__/ \__,_|_| |_|_| |_|\__,_|\___|_|   
                                          
Backdoor Finder (C) Artemis
Github: https://github.com/jordanisadev
'''

# Create console loggings
class Logs:
    def info(message : str):
        print(f'{resetStyle}[{foreGreen}INFO{resetStyle}] {message}')
    def warning(message : str):
        print(f'{resetStyle}[{foreYellow}WARNING{resetStyle}] {message}')
    def error(message : str):
        print(f'{resetStyle}[{foreRed}ERROR{resetStyle}] {message}')

# Create the function to search for all the possible words
def searchForPossibilities(file_input : str):
    search_word = ['shutdown', 'system(', 'net user']
    exceptions = ['COLOR', 'TITLE', 'CLS', 'PAUSE']
    log_file_path = "logs/logs.txt"
    if os.path.isfile(file_input):
        if not os.path.isfile(log_file_path):
            Logs.error(f"Log file '{log_file_path} does not exists")
        else:
            found_count = 0
            found_lines = []
            with open(file_input, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line_number, line in enumerate(lines, start=1):
                    for word in search_word:
                        if word in line:
                            if word == 'system(':
                                if any(exception in line.upper() for exception in exceptions):
                                    continue
                            found_count += 1
                            found_lines.append(line_number)
                            with open(log_file_path, 'a', encoding='utf-8') as log_file:
                                log_file.write(f"[LOGS] '{word}' possibilities found at line: {line_number} -> {line.strip()}\n")
                            Logs.info(f"Found '{foreYellow}{word}{resetStyle}' in line {line_number}: {foreYellow}{line.strip()}{resetStyle}")
            if found_count > 0:
                line_str = ", ".join(map(str, found_lines))
                Logs.info(f'Logs has been saved at -> {log_file_path}')
                Logs.info(f"{found_count} 'backdoor' possibilities found at line(s): {line_str}")
            else:
                Logs.warning("No 'backdoor' possibilities found")
    else:
        Logs.error('The selected file is not a valid file')

# Create the main function to handle all the related functions
def main():
    command('cls')
    print(banner)
    while True:
        file_input = input('Drag and drop selected file: ')
        searchForPossibilities(file_input)

# Run all the main functions
if __name__ == '__main__':
    main()