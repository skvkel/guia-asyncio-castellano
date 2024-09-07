import asyncio
from typing import NoReturn


async def coro_1(can_start: asyncio.Event) -> NoReturn:

    print('coro_1 is waiting for the event.')
    await can_start.wait()

    print('coro_1 now is executing. ')
    await asyncio.sleep(1)


async def coro_2(can_start: asyncio.Event) -> NoReturn:

    print('coro_2 is waiting for the event.')
    await can_start.wait()

    print('coro_2 now is executing. ')
    await asyncio.sleep(1)


async def coro_3(can_start: asyncio.Event) -> NoReturn:

    print('coro_3 is waiting for the event.')
    await can_start.wait()

    print('coro_3 now is executing. ')
    await asyncio.sleep(1)


async def main():

    can_start = asyncio.Event()

    task_1 = asyncio.create_task(coro_1(can_start))
    task_2 = asyncio.create_task(coro_2(can_start))
    task_3 = asyncio.create_task(coro_3(can_start))

    await asyncio.sleep(2)
    can_start.set()

    await asyncio.gather(
        task_1,
        task_2,
        task_3
    )

asyncio.run(main())

