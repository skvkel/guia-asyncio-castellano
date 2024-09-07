import asyncio
import time


async def coro1():
    time.sleep(0.5)

    return 'OK1'


async def coro2():
    time.sleep(0.5)

    return 'OK2'


async def coro3():
    time.sleep(0.5)
    try:
        raise Exception('exception_coro_4')
    except Exception as exception_4:
        return exception_4


async def main():

    tasks = [coro1(), coro2(), coro3()]

    future = await asyncio.gather(*tasks)

    # The coro3 will raise a handled exception and the execution will not be
    # stopped
    print(future)

asyncio.run(main())
