import asyncio


async def my_async_function():
    await asyncio.sleep(2)
    return "Completed"


async def main():
    result = await asyncio.wait_for(my_async_function(), timeout=1)
    print(result)

asyncio.run(main())
