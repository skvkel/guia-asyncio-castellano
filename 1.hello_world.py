import asyncio


async def hello_world():
    print('Hello World!')

# Produces a warning, because is not awaited
#my_coroutine = hello_world()
#print(type(my_coroutine))

asyncio.run(hello_world())
