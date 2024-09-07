import time
from random import randint
import asyncio


def blockin_task():
    print('Task is running')
    time.sleep(2)
    print('Task is done')


async def background():
    while True:
        print('Task in is running')
        await asyncio.sleep(randint(1, 2))


async def main():
    # Si ponemos await, no terminará nunca. Si no ponemos nada, nos aconsejará
    # que esa task no es esperada
    _ = asyncio.create_task(background())
    coro = asyncio.to_thread(blockin_task)

    await coro


asyncio.run(main())
