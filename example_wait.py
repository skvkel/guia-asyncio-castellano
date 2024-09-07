import asyncio


async def task1():
    await asyncio.sleep(1)
    return "Task 1 completed"


async def task2():
    await asyncio.sleep(3)  # Expire timeout
    return "Task 2 completed"


async def main():
    task1_future = asyncio.create_task(task1())
    task2_future = asyncio.create_task(task2())

    tasks = [task1_future, task2_future]
    done, pending = await asyncio.wait(tasks, timeout=2)

    print("Done tasks:")
    for task in done:
        print(task.result())

    print("Pending tasks:")
    for task in pending:
        print(task)


asyncio.run(main())
