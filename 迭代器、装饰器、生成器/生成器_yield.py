# 生成器对象就是一个迭代器


from re import S


def demo01():
    print('!!!!start!!!! 第1次循环')
    for i in range(2):
        c = yield i
        print('c ---->', c)
        print('!!!!end!!!! 第%d次循环' % (i + 1))


def demo02(flag):
    print('hi')
    if flag:
        print('yield')
        yield '触发'
        print('back')
    print('bye')
    return 'result'


class DowCounte:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        while self.start > 0:
            self.start -= 1  # 自减
            yield self.start
        # else:
        #     raise StopIteration


def async_task(ta):
    print(f'当前响应 {ta}')
    yield
    print(f'再次响应 {ta}')
    yield
    print('====end====')
    yield


def async_run_task():
    for ta in task_list:
        next(ta)


if __name__ == '__main__':
    # pass
    # gun = demo02(False)  # StopIteration: result
    # gun = demo02(True)
    # c2 = next(gun)
    # print(c2)

    # for x in DowCounte(5):
    #     print(x)

    # 创建任务队列
    task_list = []
    # 创建任务
    task1 = async_task('task1')
    task2 = async_task('task2')
    task_list.append(task2)
    task_list.append(task1)
    for i in range(3):
        async_run_task()

# TypeError: can't send non-None value to a just-started generator
