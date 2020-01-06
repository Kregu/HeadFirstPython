from datetime import datetime
from random import randint
from time import sleep

odds = [x for x in range(1, 60, 2)]

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an add minute.")

    sleep(randint(1, 10))
