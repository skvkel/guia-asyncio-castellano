import asyncio


async def coro_1(lock: asyncio.Lock):
    print('Coro 1 trying to acquire lock')
    async with lock:
        print('Coro1 acquired lock')
        await asyncio.sleep(1)

    return 'coro 1 finished'


async def coro_2(lock: asyncio.Lock):
    print('Coro 2 trying to acquire lock')
    async with lock:
        print('Coro2 acquired lock')
        await asyncio.sleep(1)

    return 'coro 2 finished'


async def main():
    my_lock = asyncio.Lock()

    task_1 = asyncio.create_task(coro_1(my_lock))
    task_2 = asyncio.create_task(coro_2(my_lock))

    results = await asyncio.gather(task_1, task_2)

    print(results)


asyncio.run(main())