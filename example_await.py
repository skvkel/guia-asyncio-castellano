import asyncio
import time


# It's the same that asyncio.sleep(2)
async def my_second_coroutine():
    print('Starting my_second_coroutine')
    time.sleep(2)
    print('Finished seconds waited in second coro')


async def my_first_coroutine():
    print('started my first coroutine')
    await my_second_coroutine()
    print('Finished my first coroutine')


asyncio.run(my_first_coroutine())

