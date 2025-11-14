#!/usr/bin/env python3

import sys
import time
import signal
import argparse
from datetime import datetime

__version__ = "1.1.0"


def clear_screen():
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[H')
    sys.stdout.flush()


def get_terminal_size():
    try:
        import shutil
        size = shutil.get_terminal_size()
        return (size.columns, size.lines)
    except (AttributeError, OSError):
        return (80, 24)


def center_text(text, width):
    return text.center(width)


def display_clock():
    try:
        while True:
            clear_screen()
            cols, rows = get_terminal_size()
            
            now = datetime.now()
            time_str = now.strftime('%H:%M:%S')
            
            vertical_padding = (rows - 1) // 2
            centered_time = center_text(time_str, cols)
            
            for _ in range(vertical_padding):
                print()
            
            print(centered_time, end='', flush=True)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        clear_screen()
        sys.exit(0)


def signal_handler(sig, frame):
    clear_screen()
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Minimal terminal clock tool for Linux/WSL")
    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    if not sys.stdout.isatty():
        print("Error: This program must be run in a terminal.", file=sys.stderr)
        sys.exit(1)
    
    display_clock()


if __name__ == '__main__':
    main()
