import threading
import time

glock = threading.Lock()
li = [i for i in range(10)]
# print(li)
def num(thr):
    # print(thr)
    while True:
        glock.acquire()
        if len(li) != 0:
            d = li.pop()
            glock.release()
            print(thr+'-'+str(d))
            time.sleep(2)
        else:
            glock.release()
            break

if __name__ == "__main__":
    for n in range(3):
        nu = n+1
        thr = "Thread-%d"%nu
        pro = threading.Thread(target=num,args=(thr,))
        pro.start()