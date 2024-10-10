import time


def timer(func):

    def wrapper():
        time1 = time.time()
        func()
        time2 = time.time()-time1
        return time2
    return wrapper

def timer_log(func):

    def wrapper():
        time1 = time.time()
        var = func()
        time2 = time.time()-time1
        print(f"{time2} seconds to execute!")
        return var

    return wrapper




