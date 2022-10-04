import json
import time
import gspread
import requests
import plusnik.Console
from zipfile import ZipFile
import pandas as pd
import config

def update(CLIENT_ID, CLIENT_SECRET, CLASS_ID):
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    response = requests.post('https://stepik.org/oauth2/token/',
                            data={'grant_type': 'client_credentials'},
                            auth=auth)
    token = response.json().get('access_token', None)
    if not token:
        plusnik.Console.log('Unable to authorize with provided credentials', message_color=plusnik.Console.RED)
        return -1

    gc  = gspread.service_account(config.PATH_TO_ACCOUNT_FILE)
    info_plusnik = gc.open(config.SHEET_NAME)
    test_page = info_plusnik.worksheet(config.WORKSHEET)
    plusnik.Console.log('Authorized in GoogleSheetsAPI', message_color=plusnik.Console.GREEN)

    # responce_ = requests.post(f'https://stepik.org/api/long-tasks', data={"longTask":{"finish_date":None,"queue_date":None,"start_date":None,"status":None,"type":"class_download_grade_book","course":None,"klass":"33791","lesson":None,"step":None,"user":None}}, headers={'Authorization': 'Bearer ' + token})
    responce_ = requests.post(f'https://stepik.org/api/long-tasks', data='{"longTask":{"type":"class_download_grade_book","klass":"' + str(CLASS_ID) + '"}}', headers={'Authorization': 'Bearer ' + token, "Content-Type": "application/json; charset=utf-8"})
    value = responce_.json()['long-tasks'][0]['id']
    time.sleep(10)
    download = requests.get(f'https://stepik.org/api/long-tasks/{value}', headers={'Authorization': 'Bearer ' + token}).json()['long-tasks'][0]['result']['files'][0]['url']

    file = requests.get(download)
    with open('table.zip', 'wb') as f:
        f.write(file.content)

    with ZipFile('table.zip') as arc_:
        arc_.extractall()
    plusnik.Console.log('Downloaded new report', message_color=plusnik.Console.GREEN)

    data = pd.read_csv(f'class-{CLASS_ID}-grade-book.csv')
    data = data.fillna(config.FILL_NAN)
    test_page.update([len(data.columns.values.tolist()) * ['', ]] * 70)
    test_page.update([data.columns.values.tolist()] + data.values.tolist())
    return 0