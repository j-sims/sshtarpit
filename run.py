# Credits: https://nullprogram.com/blog/2019/03/22/
import asyncio
import random

async def handler(_reader, writer):
    try:
        while True:
            await asyncio.sleep(10)
            writer.write(b'%x\r\n' % random.randint(0, 2**32))
            await writer.drain()
    except ConnectionResetError:
        pass

async def main():
    server = await asyncio.start_server(handler, '0.0.0.0', 22)
    async with server:
        await server.serve_forever()

asyncio.run(main())

