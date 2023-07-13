from threading import Thread, Lock
import time

db_value = 0

def increase(lock):
    global db_value

    # lock is needed because when threads have same methods to execute,
    # they just copy executed value from the former thread that is already executed 
    lock.acquire()
    local_copy = db_value
    # processing
    local_copy += 1
    time.sleep(0.2)
    db_value = local_copy
    lock.release()

    # Second way to use lock
    # with lock:
    #   lock.acquire()
    #   local_copy = db_value
    #   local_copy += 1
    #   time.sleep(0.2)
    #   db_value = local_copy

if __name__ == "__main__":

    lock = Lock()
    print("start value > ", db_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value > ", db_value)
    print("end main")