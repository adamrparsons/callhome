import requests
import os

from settings import *
from version import *
from models import ServerReport

PAYLOAD_URL = SERVER_ADDRESS + "api/servers-reports/"

def main():
    
    version_needed = requests.get(SERVER_ADDRESS + "servers/callhome-version-required/").json()['CALLHOME_VERSION_REQUIRED']
    if VERSION < version_needed:
        print("Updating callhome to latest version...")
        os.system("git pull")
        print("Please re-run callhome")
        os.exit()
    
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