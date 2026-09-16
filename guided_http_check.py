import argparse
import logging
import json
import csv
import requests
import os

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("--target", action="append", required=True)

args = parser.parse_args()

security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy"
]

for target in args.target:

    logging.info("Checking: %s", target)

    try:
        response = requests.get(target, timeout=5)

        logging.info("HTTP status: %s", response.status_code)

        header_results = {}

        for header in security_headers:

            if header in response.headers:
                header_results[header] = "Present"
                logging.info("Present: %s", header)

            else:
                header_results[header] = "Missing"
                logging.warning("Missing: %s", header)

        result = {
            "target": target,
            "status_code": response.status_code,
            "security_headers": header_results
        }

        print(json.dumps(result, indent=2))
     


    except requests.RequestException as error:

        logging.error("Request failed: %s", error)