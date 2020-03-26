#!/usr/bin/env python3

#import cowsay
import time
import logging
import daiquiri

def main():
    """Say hello to Thoth."""
    daiquiri.setup(level=logging.INFO)
    while True:
        logger = daiquiri.getLogger(__name__)
        logger.info("It works and log to stderr by default with color! Every 10 seconds ;)")
        time.sleep(10)
        # for character in cowsay.chars:
        #     character("Hello, Thoth!")
        #     time.sleep(5)


__name__ == "__main__" and main()
