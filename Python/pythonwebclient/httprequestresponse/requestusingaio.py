import asyncio
import aiohttp

data = {'name': 'john kennedy'}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', json=data) as response:
            print(await response.json())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
