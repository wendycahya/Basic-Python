import time, threading

# Code executed by the new thread:
def loop():
    print("thread %s is running...".format(threading.current_thread().name))
    n = 0
    while n <5:
        n = n + 1
        print('thread {.2f} >>> {.2f}'.format(threading.current_thread().name, n))
        time.sleep(1)
    print('thread {.2f} ended.'.format(threading.current_thread().name))

print('thread {.2f} is running...'.format(threading.current_thread().name))
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread {.2f} ended.'.format(threading.current_thread().name))