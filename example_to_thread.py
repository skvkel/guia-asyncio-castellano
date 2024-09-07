import asyncio
import time
from aiohttp import web


async def do_things():
    flag = 0
    while flag < 10:
        await asyncio.sleep(0.5)
        print('hello from do things')
        flag += 1
    return 'done'


async def handle_file_request_all(request):
    # Simula un procesamiento ligero para otras rutas
    large_coro = asyncio.to_thread(read_large_file, 'test')
    _ = asyncio.create_task(do_things())

    await large_coro

    return web.Response(text="Request handled quickly!")


# Función bloqueante que simula la lectura de un archivo grande
def read_large_file(filename):
    print(f"Starting to read {filename}...")
    time.sleep(10)  # Simula una operación bloqueante de I/O
    print(f"Finished reading {filename}")
    return f"Content of {filename}"


# Maneja peticiones HTTP de manera asíncrona
async def handle_request(request):
    # Simula un procesamiento ligero para otras rutas
    await asyncio.sleep(1)
    return web.Response(text="Request handled quickly!")


# Maneja peticiones para leer un archivo grande
async def handle_file_request(request):
    filename = "large_file.txt"
    # Usa asyncio.to_thread para leer el archivo en un thread separado
    content = await asyncio.to_thread(read_large_file, filename)
    return web.Response(text=content)


async def main():
    # Configura las rutas del servidor
    app = web.Application()
    app.router.add_get('/', handle_request)
    app.router.add_get('/read-file', handle_file_request)
    app.router.add_get('/read-file-in-request', handle_file_request_all)

    # Ejecuta el servidor web
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server running on http://localhost:8080")

    # Mantén el servidor corriendo
    await asyncio.Event().wait()


# Ejecutar el bucle principal de asyncio
asyncio.run(main())
