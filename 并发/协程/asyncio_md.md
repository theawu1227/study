协程，又被称为微线程，他是实现多任务的一种方式，势必线程更小的执行单元。

不是计算机中真实存在的
通过一个线程实现在代码块之间的切换

在一个线程中如果遇到IO等待时间，线程不会等待，利用此空间的时间取做一些其他的

通俗的理解： 在一个线程中的某个函数中，
我们可以在任何地方保存当前函数的一些临时变量等信息，
然后切换到另外一个函数中执行，注意不是通过调用函数的方式做到的 ，
并且切换的次数以及什么时候   再切换到原来的函数都由开发者自己确定。

实现协程的方法
greenlet
yield 关键字
asyncio 装饰器 py3.4
async await 关键字（python3.5）

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