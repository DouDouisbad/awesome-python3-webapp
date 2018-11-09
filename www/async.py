# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:54:19 2018

@author: SAB
"""


# Python基础-异步IO的支持 async和await

# asyncio的编程模型就是一个消息循环
import threading
import asyncio

# 把 generator 标记为 coroutine 类型，便于执行 EventLoop
async def func(name):
    print('Start %s! (%s)' % (name, threading.currentThread()))
    # yield from语法可以让我们方便地调用另一个generator
    if name == "访问百度":
        print("%s 延迟 1秒" % name)
        await asyncio.sleep(1)
    elif name == "访问Google":
        print("%s 延迟 5秒" % name)
        await asyncio.sleep(5)
    else:
        print("%s 延迟 3秒" % name)
        await asyncio.sleep(3)

    print('\n End %s!! (%s)' % (name, threading.currentThread()))


# 获取 EventLoop
loop = asyncio.get_event_loop()

tasks = [func("访问百度"),func("访问Google"),func("访问Python")]

# 执行 coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()