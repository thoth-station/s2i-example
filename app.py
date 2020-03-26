#!/usr/bin/env python3

import time
import logging
import daiquiri

def main():
    """Log hello thoth every 10 seconds."""
    daiquiri.setup(level=logging.INFO)
    while True:
        logger = daiquiri.getLogger(__name__)
        logger.info("Hello Thoth ;)")
        time.sleep(10)


__name__ == "__main__" and main()
