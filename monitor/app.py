from dotenv import load_dotenv

load_dotenv()

import logging
import time

from config import *
from monitor import check_service, print_report

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Monitoring Engine Started")

while True:

    results = []

    for service in SERVICES:

        results.append(
            check_service(service)
        )

    print_report(results)

    time.sleep(CHECK_INTERVAL)