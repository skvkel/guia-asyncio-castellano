import asyncio
from random import randint


async def task():
    time_to_wait = randint(1, 3)
    await asyncio.sleep(time_to_wait)

    return f"Task with {time_to_wait} completed"


async def main():
    tasks = [task(), task(), task()]
    completed_task = asyncio.as_completed(tasks)

    # Itera sobre las tareas a medida que se completan
    for awaitable in completed_task:
        # We must wait the awaitable
        result = await awaitable
        print(result)

asyncio.run(main())
