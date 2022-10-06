# Auto plusnik
## CLI interface
If you want to run an application without a website, you can run _run.py_. First you need to activate the virtual enviroment:
```bash
$ source e_plusnik/bin/activate
```
If you want to update only one time, you can use the following command:
```bash
$ python3 run.py runonce <class_id>
```
If you want to loop previos command, you can use the following command:
```bash
$ python3 run.py runserver <class_id>
```

## How to run a website
First, you need to change directory:
```bash
$ cd pl_sit
```
Then, run a _main.py_ file:
```bash
$ python3 main.py
```

## How to edit a config.py
`config.py` is a configuration file. You can change it to customize your plusnik:
```python
import pl_sit

MILLESECOND = 1000000
SECOND = 1000000000
MINUTE = 60000000000

CLIENT_ID = ...
CLIENT_SECRET = ...
CLASS_ID = pl_sit.CLASS_ID

UPDATE_TIME = ...
PATH_TO_ACCOUNT_FILE = ...
SHEET_NAME = ...
WORKSHEET = ...
FILL_NAN = ...
```
CLIENT_ID and CLIENT_SECRET - your client from oauth - https://stepik.org/oauth2/applications/.

UPDATE_TIME - interval between each update. You can use a constants. For example:
```python3
UPDATE_TIME = MINUTE * 20
```

PATH_TO_ACCOUNT_FILE - path to the account file - './plusnik/account.json'

SHEET_NAME - name of the Google Sheet

WORKSHEET - name of the list on Google Sheet

FILL_NAN - string for filling 'NaN'