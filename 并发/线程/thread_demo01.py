import re
import os
import urllib.request
import threading
import time

headers ={

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Referer': 'https://www.doutula.com/zz/list/',
}
'''
-----单线程爬取
'''

# start = time.time()
#1.生成网页列表
url_list =[]
http = "https://www.doutula.com/zz/list/?page="
for i in range(1,13):
    url = http + str(i)
    url_list.append(url)
#
# #3.下载图片到本地
# def download(url):
#     #修改文件名
#     split_list = url.split("/")
#     filename = split_list.pop()
#     path=os.path.join("doutu",filename)
#     #下载图片
#     urllib.request.urlretrieve(url,filename=path)
#
# for url in url_list:
#     # print(url)
# #2.爬取图片网址
#     res = urllib.request.Request(url,headers=headers)
#     res2 = urllib.request.urlopen(res).read().decode("UTF-8")
#     result = re.findall(re.compile(r'<img referrerpolicy="no-referrer".*?data-original="(.*?)"',re.S),res2)
#     print(result)
#     try:
#         for relt in result:
#             print(relt)
#             download(relt)
#     except:
#         pass
#
# end = time.time()
# need = end-start
# print("Need time :%d"%need)

'''
-----多线程
'''
#加锁，多线程再运行时，会出现同时访问某元素的情况，避免数据变动后出现错误
glock = threading.Lock()
#1.获取图片网址
pic_list=[]
def get_pic_url():
    while True:
        glock.acquire()#加锁
        if len(url_list) ==0:
            glock.release()#释放锁
            break
        else:
            page_url =url_list.pop()
            glock.release()
            res = urllib.request.Request(page_url,headers=headers)
            res2 = urllib.request.urlopen(res).read().decode("UTF-8")
            result = re.findall(re.compile(r'<img referrerpolicy="no-referrer".*?data-original="(.*?)"', re.S), res2)
            glock.acquire()
            for rel in result:
                pic_list.append(rel)
            glock.release()
def download_pic():
    while True:
        glock.acquire()
        if len(pic_list) == 0:
            glock.release()
            continue
        else:
            try:
                url = pic_list.pop()
                glock.release()
                #修改文件名
                split_list = url.split("/")
                filename = split_list.pop()
                path = os.path.join("../doutu", filename)
                #下载
                urllib.request.urlretrieve(url,filename=path)
            except Exception as e:
                print(e)

def main():
    #创建两个线程生产图片地址
    for x in range(2):
        product = threading.Thread(target=get_pic_url)
        product.start()

    #创建三个线程下载图片地址
    for x in range(3):
        consumer = threading.Thread(target=download_pic)
        consumer.start()

if __name__ == '__main__':
    d=time.time()
    main()
    d = time.time()-d
    print(d)