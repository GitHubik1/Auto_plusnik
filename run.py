import time
import sys
import plusnik.Console
import config
from plusnik.Plusnik import update

start_time = time.time_ns()

def get_time():
    return time.time_ns() - start_time

MILLESECOND = 1000000
SECOND = 1000000000
MINUTE = 60000000000

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
CLASS_ID = config.CLASS_ID

class App:
    def run_server(self):
        plusnik.Console.log('Server started')
        last_update = -config.UPDATE_TIME
        while True:
            if get_time() - last_update >= config.UPDATE_TIME:
                last_update = get_time()
                try:
                    if update(CLIENT_ID, CLIENT_SECRET, CLASS_ID) == 0:
                        plusnik.Console.log('updated', message_color=plusnik.Console.GREEN)
                except KeyError as e:
                    plusnik.Console.log(f'Excepted KeyError "{e}"', message_color=plusnik.Console.RED)

if __name__ == '__main__':
    app = App()
    if len(sys.argv) < 2:
        plusnik.Console.log('Error: not enough arguments', message_color=plusnik.Console.RED)
    elif sys.argv[1] == 'runserver':
        app.run_server()
    else:
        plusnik.Console.log(f'Error: invalid option "{sys.argv[1]}"', message_color=plusnik.Console.RED)