import asyncio
from time import sleep


async def coro1():
    sleep(0.1)
    return 'Hello from coro1'


async def coro2():
    sleep(0.1)
    return 'Hello from coro2'


async def main():

    task_1 = asyncio.create_task(coro1())
    task_2 = asyncio.create_task(coro2())
    tasks = [task_1, task_2]

    # Will return a future with values
    future = await asyncio.gather(*tasks)

    print(future)

asyncio.run(main())
