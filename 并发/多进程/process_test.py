import multiprocessing
import time
from multiprocessing import Process
import random
import json
import os
from multiprocessing import Lock
from multiprocessing import Pool

# ####定义两个间隔0.5执行3次的函数
# def fun_a(num,name):
#     for i in range(num):
#         print(name)
#         time.sleep(0.5)
#
# def fun_b(num):
#     for i in range(num):
#         print('f_b()')
#         time.sleep(0.5)
#
# #顺序执行：
# # if __name__ == '__main__':
# #     fun_a()
# #     fun_b()
# #两个函数按照先后顺序执行
#
# #多进程--使用Process开启多进程:target = 任务名,arge = 元组形式参数，kwargs=字典形式参数
# if __name__ == '__main__':
#     # 创建进程对象
'''A--多进程无参数'''
#     # fun_a_process = multiprocessing.Process(target=fun_a)
#     # fun_b_process = multiprocessing.Process(target=fun_b)
#
'''B--多进程带参数'''
#     #--arge
#     # fun_a_process = multiprocessing.Process(target=fun_a,args=(3,'fun_a()'))
#     # fun_b_process = multiprocessing.Process(target=fun_b,args=(3,))
#     #--kwargs
#     fun_a_process = multiprocessing.Process(target=fun_a,kwargs={"num":4,"name":'fun_a'})
#     fun_b_process = multiprocessing.Process(target=fun_b,kwargs={"num":3})
#
#     # #启动多进程
#     fun_a_process.start()
#     fun_b_process.start()

'''C--类继承，函数功能相近，避免重复定义'''
# #继承Process类
# class fun_(Process):
#     def __init__(self,name,num):
#         #继承父类init方法
#         super().__init__()
#         self.name = name
#         self.num = num
#     #重写run函数
#     def run(self):
#         for i in range(self.num):
#             print(self.name)
#             time.sleep(0.5)
#
# if __name__ == '__main__':
#     print('start')
#     for para in [["fun_a",3],['fun_b',4]]:
#         #para[0]===进程名，para[1]===重复数
#         fun_(para[0],para[1]).start()

'''---------进程锁----------'''
##ticket.json里写的{“count”: 4}，表示现在只有4张票，我会启动5个进程去买票，这就意味着第5个进程会买票失败
# def buy_ticket(file_name,lock):
#     #进程锁开启，同一时间只允许一个进程操作
#     lock.acquire()
#     with open(file_name,'r',encoding='utf-8') as f:
#         dic = json.loads(f.read())
#     if dic["count"]>0:
#         print('{}查询，还剩{}张票'.format(os.getpid(),dic["count"]))
#         dic["count"] -=1
#         time.sleep(random.randint(1,3))
#         with open(file_name,'w',encoding='utf-8') as f:
#             f.write(json.dumps(dic))
#         #获取当前进程编号：os.getpid()
#         #获取当前父进程编号：os.getppid()
#         print("{} successful".format(os.getpid()))
#     else:
#         print('{} defeat'.format(os.getpid()))
#
#     lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(5):
#         sub_process = multiprocessing.Process(target=buy_ticket,args=("ticket.json",lock))
#         sub_process.start()

'''---------进程池---------'''


def work(n):
    print("{} statrt".format(os.getpid()))
    time.sleep(1)
    print("{} end".format(os.getpid()))
    return n * 2
#
if __name__ == '__main__':

    pool = Pool(processes=3) #定义线程个数
    res_l = []
    # A.阻塞（同步）
#     for i in range(6):
#         res = pool.apply(work,(i,))#apply是阻塞方式
#         res_l.append(res)#直接获得结果
#     pool.close()#关闭pool,使其不再接收新任务
#     pool.join()#主进程阻塞，子进程结束，主进程才可以结束
#
#     print(res_l)

    #非阻塞（异步）
    for i in range(6):
        res = pool.apply_async(work,(i,))#非阻塞
        res_l.append(res)#非直接获得结果
    pool.close()
    pool.join()

    print([res.get() for res in res_l])#使用get方式获取结果










