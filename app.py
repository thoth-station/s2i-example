#!/usr/bin/env python3

import cowsay
import time

def main():
    """Say hello to Thoth."""
    while True:
        for character in cowsay.chars:
            character("Hello, Thoth!")
            time.sleep(5)


__name__ == "__main__" and main()
