import datetime

GREEN = '\u001b[92m'
WHITE = '\u001b[0m'
RED = '\u001b[31m'

def log(*args, sep=' ', message_color=WHITE, date=None):
    print(f'[{datetime.datetime.now() if date == None else date}]: {message_color}', end='')
    for i in args:
        print(i, end=sep)
    print(WHITE)