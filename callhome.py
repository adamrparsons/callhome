import requests
import os

from settings import *
from models import ServerReport

def main():
    report = ServerReport()
    report.fill_data()
    report_obj = {
        'managed_server': IDENTITY_URL,
        'response': report.to_dict(),
        'uptime': report.uptime,
    }
    headers = {'Api-Token': API_TOKEN, 'Api-Secret-Key': API_SECRET}
    post = requests.post(PAYLOAD_URL, json=report_obj, headers=headers)


if __name__ == "__main__":
    main()