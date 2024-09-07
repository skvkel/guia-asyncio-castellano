import asyncio


async def process_file(file):
    await asyncio.sleep(1)
    print(f'File {file} proccessed')
    return f'File content: {file}'


async def main():
    # List files
    files = [f'fichero_{i}.txt' for i in range(100)]

    # Create 100 task (one for every file)
    tasks = [asyncio.create_task(process_file(file)) for file in files]

    # Wait all of them
    results = await asyncio.gather(*tasks)

    print("All files are processed.")
    print(results)

asyncio.run(main())
