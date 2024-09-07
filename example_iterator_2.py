import asyncio


def do_something():
    return 'a'


class AsyncContador:

    def __init__(self, limite):
        self.limite = limite
        self.actual = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.actual < self.limite:
            self.actual += 1
            awaitable = asyncio.to_thread(do_something)

            return awaitable
        else:
            # Here the iterator will stop
            raise StopAsyncIteration


async def main():
    a = [numero async for numero in AsyncContador(5)]
    print('Started every task in a new thread')

    # Wait for all new created threads and capture results
    result_in_order = await asyncio.gather(*a)

    # Print the returned result by tasks
    print(result_in_order)


asyncio.run(main())
