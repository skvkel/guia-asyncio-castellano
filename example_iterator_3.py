import asyncio
import random
from collections.abc import Awaitable


class AsyncAPIClient:
    def __init__(self, total_pages):
        self.total_pages = total_pages
        self.current_page = 0

    def __aiter__(self):
        return self

    async def __anext__(self) -> Awaitable:
        if self.current_page < self.total_pages:
            self.current_page += 1
            # Simula una llamada a una API con un retraso asíncrono
            future_new_thread = asyncio.to_thread(random.uniform, 0.5, 1.5)

            return future_new_thread

        else:
            raise StopAsyncIteration


async def main():

    # We will set 3 "calls"
    api_client = AsyncAPIClient(total_pages=3)

    # We get the list of awaitables, executing concurrently
    tasks = [task async for task in api_client]

    # Wait for all finished tasks
    values_returned = await asyncio.gather(*tasks)

    print(values_returned)

asyncio.run(main())
