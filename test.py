from timer import timer,timer_log
import time
@timer
def start():
    time.sleep(2)
@timer_log
def start_log():

    time.sleep(3)
    return 0
c = start()
print(f"{c} seconds to execute!")

d = start_log()
print(f"returned {d}")