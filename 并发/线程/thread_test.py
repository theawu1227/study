import threading
import time


# exitFlag=0
# #自定义线程，继承threading.Thread来自定义线程类，本质是重构Thread类中的run方法
# class myThread (threading.Thread):
#     def __init__(self,threadID,name,counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name=name
#         self.counter=counter
#
#     def run(self):
#         print("start:"+self.name)
#         print_time(self.name,self.counter,5)
#         print("end:"+self.name)
#
# def print_time(threadName,delay,counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(1)
#         print("%s:%s"%(threadName,time.ctime(time.time())))
#         counter-=1

# def run(n):
#     print("task",n)
#     time.sleep(1)
#     print('3')
#     time.sleep(1)
#     print('2')
#     time.sleep(1)
#     print('1')
#
# def work1():
#     global exitFlag
#     exitFlag =10
#     print("work1 num is : %d"%exitFlag)
#
# def work2():
#     global exitFlag
#     for i in range(3):
#         exitFlag+=1
#     print("work2 num is :%d"%exitFlag)


#
# if __name__ == '__main__':
#     # 创建新线程
#     # thread1 = myThread(1,"Thread-1",1)
#     # thread2 = myThread(2,"Thread-2",2)
#
#     thread1 = threading.Thread(target=work1)
#     thread2 = threading.Thread(target=work2)
#
#     thread1.setDaemon(True)# 开启守护进程，必须在start之前完成
#     thread2.setDaemon(True)
#     #开启新线程
#     thread1.start()
#     thread2.start()
#     thread1.join()# 设置主进程等待子进程结束
#     thread2.join()
#     print("退出主线程")

event = threading.Event()


def lighter():
    count = 0
    event.set()     #初始值为绿灯
    while True:
        if 5 < count <=10 :
            event.clear()  # 红灯，清除标志位
            print("\33[41;1mred light is on...\033[0m")
        elif count > 10:
            event.set()  # 绿灯，设置标志位
            count = 0
        else:
            print("\33[42;1mgreen light is on...\033[0m")

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():      #判断是否设置了标志位
            print("[%s] running..."%name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..."%name)
            event.wait()
            print("[%s] green light is on,start going..."%name)

light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car,args=("MINI",))
car.start()