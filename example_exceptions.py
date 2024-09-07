import asyncio
import time


async def coro_exception():
    try:
        1/0
    except ZeroDivisionError:
        return 'ZeroDivisionError'


async def start_coro_exception():
    a = await coro_exception()
    print(a)


async def start_coro_exception_task():
    task = asyncio.create_task(coro_exception())

    await task
    # If we receive InvalidStateError, this exception is raised when the task
    # is not yet done. We need to wait it previously
    if task.exception():
        print('La excepcion:')
        print(task.exception())

asyncio.run(start_coro_exception_task())

