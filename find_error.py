#!/usr/bin/env python3

import sys
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
# log_file = BASE_DIR / "logs" / "fishy.log"
output_file = BASE_DIR / "output" / "error_found.log"

def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []

    with open(log_file, "r", encoding="UTF-8") as file:
        for line in file:
            if "error" in line.lower() and error.lower() in line.lower():
                returned_errors.append(line)

    return returned_errors

def file_output(returned_errors):
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w", encoding="UTF-8") as file:
        for line in returned_errors:
            file.write(line)

# Type 1 - instrukcja uruchomienia programu
# returned_errors = error_search(log_file)
# file_output(returned_errors)

# Type 2 - instrukcja uruchomienia programu
if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)