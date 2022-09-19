import asyncio
import time
import datetime


class demo01:
    async def run(self, delay, file):
        await asyncio.sleep(delay)  # 等待回复
        print(file)

    async def func(self):
        task1 = asyncio.create_task(self.run(1, 'my name is thea'))
        task2 = asyncio.create_task(self.run(2, 'age 18'))
        print(time.strftime('%X'))
        # await asyncio.sleep(1)
        # await run(1, 'my name is thea')
        # await run(2, 'age 18')

        await asyncio.gather(task1, task2)

        print(time.strftime('%X'))


# de = demo01()
# coro = de.func()
# asyncio.run(coro)

# class YieldFrom:
async def first_task():
    print('begin task')
    print('\t begin big_step',time.strftime('%H:%M:%S', time.localtime()))
    big_result = await big_step()
    # big_coro = self.big_step()
    # while True:
    #     try:
    #         x = big_coro.send(None)
    #     except StopIteration as e:
    #         big_result = e.value
    #         break
    #     else:
    #         func, arg = x  # 调用sleep阻塞
    #         func(arg)
    # yield x
    print(f'\t end big_step with {big_result}')
    print(f'end task')


async def big_step():
    # pass
    print('\t\t begin small_step',time.strftime('%H:%M:%S', time.localtime()))
    # print('\t\t 阻塞')
    # time.sleep(2)
    # await asyncio.gather(self.small_step())
    small_result = await small_step()
    # small_result1 = self.small_step()
    # while True:
    #     try:
    #         x = small_result1.send(None)
    #     except StopIteration as e:
    #         small_result = e.value
    #         break
    #     else:
    #         # pass
    #         yield x  # 抛给first
    print(f'\t\t end small_step {small_result}')
    return time.strftime('%H:%M:%S', time.localtime())


async def small_step():
    # pass
    print('\t\t\t 阻塞')
    t1 = time.time()
    await YieldFromIter((time.sleep, 2))  # gen
    # assert time.time() - t1 > 2, 'passss'
    print('\t\t\t /(ㄒoㄒ)/~~搬砖中')
    return time.strftime('%H:%M:%S', time.localtime())


class YieldFromIter:
    def __init__(self, obj):
        self.value = obj

    def __await__(self):
        yield self


class Task:
    def __init__(self, coro):
        self.coro1 = coro
        self._done = False
        self._result = None

    def run(self):
        print('----------------')
        # while True:
        if not self._done:
            try:
                x = self.coro1.send(None)
            except StopIteration as e:
                self._result = e.value
                self._done = True
                # break
            else:
                assert isinstance(x,YieldFromIter)
                # func, arg = x.value  # 调用sleep阻塞
                # func(arg)
        else:
            print('Done')
        print('----------------')


# yf = YieldFrom()
t = Task(first_task())
t.run()
for i in range(5):
    print('do somethings-----')
    time.sleep(0.2)

t.run()