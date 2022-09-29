import json
import gspread
import requests
from zipfile import ZipFile
import pandas as pd

def update(CLIENT_ID, CLIENT_SECRET, CLASS_ID):
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    response = requests.post('https://stepik.org/oauth2/token/',
                            data={'grant_type': 'client_credentials'},
                            auth=auth)
    token = response.json().get('access_token', None)
    if not token:
        print('Unable to authorize with provided credentials')
        exit(1)

    gc  = gspread.service_account('account.json')
    info_plusnik = gc.open('Плюсник инфо 2021-22')
    test_page = info_plusnik.worksheet('Test')

    responce_ = requests.post(f'https://stepik.org/api/long-tasks?klass={CLASS_ID}&type="class_download_grade_book"', headers={'Authorization': 'Bearer ' + token})
    value = requests.get(f'https://stepik.org/api/long-task-templates?kind=report&klass={CLASS_ID}', headers={'Authorization': 'Bearer ' + token}).json()["long-task-templates"][0]["recent_tasks"][0]#['long-task-templates'][0]['recent-tasks']['0']
    download = requests.get(f'https://stepik.org/api/long-tasks/{value}', headers={'Authorization': 'Bearer ' + token}).json()['long-tasks'][0]['result']['files'][0]['url']
    file = requests.get(download)

    with open('table.zip', 'wb') as f:
        f.write(file.content)

    with ZipFile('table.zip') as arc:
        arc.extractall()

    data = pd.read_csv(f'class-{CLASS_ID}-grade-book.csv')
    data = data.fillna('NaN')
    test_page.update([len(data.columns.values.tolist()) * ['', ]] * 70)
    test_page.update([data.columns.values.tolist()] + data.values.tolist())