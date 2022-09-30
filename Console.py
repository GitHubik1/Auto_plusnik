import datetime

GREEN = '\u001b[92m'
WHITE = '\u001b[0m'
RED = '\u001b[31m'

def write_log_to_file(log: str, file='log.txt'):
    with open(file, 'a') as f:
        f.write(log)

def log(*args, sep=' ', message_color=WHITE, date=None):
    str_ = f'[{datetime.datetime.now() if date == None else date}]: '
    str_c = str_ + message_color
    for i in args:
        a = i + sep
        str_ += a
        str_c += a
    str_c += WHITE
    print(str_c)
    write_log_to_file(str_ + '\n')