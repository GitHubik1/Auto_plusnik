import time
import sys
import Console
from Plusnik import update

start_time = time.time_ns()

def get_time():
    return time.time_ns() - start_time

MILLESECOND = 1000000
SECOND = 1000000000
MINUTE = 60000000000

CLIENT_ID = ...
CLIENT_SECRET = ...
CLASS_ID = ...

class App:
    def run_server(self):
        Console.log('Server started')
        last_update = get_time()
        while True:
            if get_time() - last_update >= MINUTE:
                last_update = get_time()
                update(CLIENT_ID, CLIENT_SECRET, CLASS_ID)
                Console.log('updated', message_color=Console.GREEN)

if __name__ == '__main__':
    app = App()
    if len(sys.argv) < 2:
        Console.log('Error: not enough arguments', message_color=Console.RED)
    elif sys.argv[1] == 'runserver':
        app.run_server()
    else:
        Console.log(f'Error: invalid option "{sys.argv[1]}"', message_color=Console.RED)