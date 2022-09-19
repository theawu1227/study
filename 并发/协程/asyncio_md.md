**运行本质**

event loop 在面对多个任务时，决定去执行哪一个任务；

在asyncio中，同时执行的任务只能有一个

与线程不同，asyncio没有上下文的切换

# 概念
## coroutine

coroutine无法被直接运行，需要将coroutine 转变为task
event loop 不会直接运行coroutine

*协程函数* --
**coroutine function**
   1. 所有 async def 开头的函数都叫coroutine function
   2. 无法直接返回函数里面的程序，返回的是一个coroutine object
   ```python 
   import asyncio

   async def func():
       print('hi')
       await asyncio.sleep(1)
       print('bye')
   
   coro = func()
   print(coro)
   
   # <coroutine object func at 0x0000023713E796C0>
   # sys:1: RuntimeWarning: coroutine 'func' was never awaited
   ```

*协程对象* --
**coroutine object**

## task

## await

当await 一个 coroutine