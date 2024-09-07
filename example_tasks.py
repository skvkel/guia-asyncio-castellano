import asyncio
import random


async def my_task():
    for number in range(5):
        print(number)
        # Resume the next task
        await asyncio.sleep(0)
    return 'Terminada'


async def my_second_task():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for _ in range(5):
        print(random.choice(my_list))
        await asyncio.sleep(0)


async def my_coro():
    my_task_scheduled = asyncio.create_task(my_task(),
                                            name='first_task')
    my_second_task_scheduled = asyncio.create_task(my_second_task(),
                                                   name='second_task')
    print('Scheduled tasks')
    # With get_name() we can get the name of task
    print(my_task_scheduled.get_name())

    # If we don't wait tasks, this example will print just two values and
    # .result() will fail. T
    await my_task_scheduled
    await my_second_task_scheduled

    # We can check if task finished
    if my_second_task_scheduled.done():
        print('Second task finished')

    # With result() we can get the result of coroutine
    print(my_task_scheduled.result())

asyncio.run(my_coro())
