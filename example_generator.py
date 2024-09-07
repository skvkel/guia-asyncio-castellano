import asyncio


async def generador_asincrono():
    for i in range(4):
        await asyncio.sleep(1)
        yield i


async def main():
    async for numero in generador_asincrono():
        print(numero)

asyncio.run(main())
