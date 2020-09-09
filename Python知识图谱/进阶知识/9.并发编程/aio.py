#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/9/9 09:28
@desc: asyncio
"""


import asyncio
import threading

from asyncio import AbstractEventLoop

event_loop = asyncio.get_event_loop()
print(event_loop)
assert isinstance(event_loop, AbstractEventLoop)
main_thread = threading.main_thread()

async def run_in_mainthread():
    print('run in mainthread')
    assert threading.current_thread() is main_thread
    await asyncio.sleep(1)
event_loop.run_until_complete(run_in_mainthread())


def task_thread():
    print(threading.current_thread().name)
    try:
        loop = asyncio.get_event_loop()
        print(loop)
    except RuntimeError as e:
        # There is no current event loop in thread 'thread:task_thread'.
        print(e)
    # so we needs create new event loop for task thread
    asyncio.set_event_loop(task_loop)
    task_loop.run_forever()

task_loop = asyncio.new_event_loop()
assert isinstance(task_loop, AbstractEventLoop)
thread = threading.Thread(target=task_thread, name='thread:task_thread')
thread.start()
# thread.join()
# try run async function in task thread
async def run_in_task_thread(num):
    print('run in task thread, num=%d' % num)
    assert threading.current_thread() is thread
    await asyncio.sleep(1)
    return num

# notice task loop not safe call
# try:
#     task_loop.run_until_complete(run_in_task_thread())
# except Exception as e:
#     # This event loop is already running
#     print(e)

# 我们期望在异步线程调用函数、并阻塞等待结果返回
future = asyncio.run_coroutine_threadsafe(run_in_task_thread(1), loop=task_loop)
print(future.result())
# 注意这里的 threadsafe 细节
# https://docs.python.org/3/library/queue.html
# collections.deque is an alternative implementation of unbounded queues with fast atomic
# append() and popleft() operations that do not require locking and also support indexing.


# 或者普通回调函数
def callback(num):
    assert threading.current_thread() is thread
    print('normal callback, num={}'.format(num))
    return num
task_loop.call_soon_threadsafe(callback, 1)
task_loop.call_later(0, callback, 1.1)


# 或者线程池
def callback2(num):
    print('thread name = %s' % threading.current_thread().name)
    print('normal callback2, num=%d' % num)
    return num
task_loop.run_in_executor(None, callback2, 2)

# 或者在保证线程安全的情况下，并不保证什么时候执行，需要看前面排队的任务
asyncio.ensure_future(run_in_task_thread(2), loop=task_loop)
# 理论上应该在 task thread 中执行 ensure_future


# 来测试一下
def call_ensure_future_from_executor():
    asyncio.ensure_future(run_in_task_thread(3), loop=task_loop)
task_loop.run_in_executor(None, call_ensure_future_from_executor)


# 注意 loop 函数调用在主线程
# 执行过程在 task thread
# 或者线程池
# 但是都可以调用 ensure_future
# ...
# 思考题：如何在非主线程，调用主线程的函数？


def call_main_func_from_task_thread():
    print('call_main_func_from_task_thread')
    asyncio.run_coroutine_threadsafe(run_in_mainthread(), loop=event_loop)
task_loop.run_in_executor(None, call_main_func_from_task_thread)

event_loop.run_forever()
