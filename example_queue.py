import asyncio
import random

buffer = asyncio.Queue(maxsize=10)


async def producer():
    while True:
        item = random.randint(1, 100)
        await buffer.put(item)
        print(f'Produced: {item}')
        await asyncio.sleep(random.uniform(0.1, 1))


async def consumer():
    while True:
        item = await buffer.get()
        print(f'Consumed: {item}')
        await asyncio.sleep(random.uniform(0.2, 1.5))


async def main():

    productor_task = asyncio.create_task(producer())
    consumidor_task = asyncio.create_task(consumer())

    await asyncio.gather(productor_task, consumidor_task)

# Ejecutar el programa
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("FInished.")
