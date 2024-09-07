import asyncio
from typing import NoReturn


async def coro_1(my_lock: asyncio.Lock) -> NoReturn:

    async with my_lock:
        print('coro_1 has acquired the lock. '
              'Manipulating critical section...')
        await asyncio.sleep(1)

    print('coro_1 has released the lock.')


async def coro_2(my_lock: asyncio.Lock) -> NoReturn:
    async with my_lock:
        print('coro_2 has acquired the lock. '
              'Manipulating critical section...')
        await asyncio.sleep(1)

    print('coro_2 has released the lock.')


async def coro_3(my_lock: asyncio.Lock) -> NoReturn:
    async with my_lock:
        print('coro_3 has acquired the lock. '
              'Manipulating critical section...')
        await asyncio.sleep(1)

    print('coro_3 has released the lock.')


async def main():

    my_lock = asyncio.Lock()

    await asyncio.gather(coro_1(my_lock),
                         coro_2(my_lock),
                         coro_3(my_lock)
                         )

asyncio.run(main())

