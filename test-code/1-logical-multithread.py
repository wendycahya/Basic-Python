#Robot library
import math
import threading
#from goto import label, goto

#GUI
import pygame

loopTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0
x = 0
class Job(threading.Thread):
    global x
    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True

    def run(self):
        while self.__running.isSet():
            print("reading condition")
            while(True):
                self.__flag.wait()
                if x == 1:
                    print("nilai x yang keluar 1")
                    goto .end
                elif x == 2:
                    print("nilai x yang keluar 2")
                elif x == 3:
                    print("nilai 3 lets break the program")
                    break
                else:
                    print("Nilai input selain 1 2 dan 3")

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False


if __name__ == '__main__':
    server = Job()
    x = int(input("cek input python: "))
    if x == 1:
        print("nilai masukan 1")
        server.start()