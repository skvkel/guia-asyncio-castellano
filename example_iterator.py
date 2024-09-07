import asyncio


class AsyncContador:

    def __init__(self, limite):
        self.limite = limite
        self.actual = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.actual < self.limite:
            self.actual += 1
            await asyncio.sleep(1)
            return self.actual
        else:
            # Here the iterator will stop
            raise StopAsyncIteration


async def main():
    async for numero in AsyncContador(5):
        print(numero)


asyncio.run(main())
