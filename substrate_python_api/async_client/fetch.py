import asyncio
from datetime import datetime
from threading import Thread
from typing import Optional, Tuple, Sequence

import aiohttp
import bs4

URLS = [
    "http://pypi.org",
    "http://python.org",
    "http://stackoverflow.com",
    "http://ubuntu.com",
]

def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()


def get_title(html: str) -> Optional[str]:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup.title.string


async def fetch(url: str, session: aiohttp.ClientSession = None) -> Tuple[str, str]:
    async def _fetch(url: str, session: aiohttp.ClientSession):
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            return url, get_title(html)

    if session:
        return await _fetch(url, session)
    else:
        async with aiohttp.ClientSession() as session:
            return await _fetch(url, session)

async def fetch_urls(loop: asyncio.AbstractEventLoop) -> Sequence[Tuple[str, str]]:
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(fetch(url, session)) for url in URLS]
        results = await asyncio.gather(*tasks)
        return results

def main() -> None:
    loop = asyncio.new_event_loop()
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    start_time = datetime.now()
    # Commented part shows an example where we create all tasks from the main thread
    # But then we can't use one instance of aiohttp.ClientSession
    # as it requires "async with", which is available only within a coroutine

    # tasks = [
    #     asyncio.run_coroutine_threadsafe(fetch(url), loop)
    #     for url in URLS
    # ]
    # for task in tasks:
    #     url, title = task.result()
    #     print(f'{url} -> {title}')


    task = asyncio.run_coroutine_threadsafe(fetch_urls(loop), loop)
    for url, title in task.result():
        print(f'{url} -> {title}')

    exec_time = (datetime.now() - start_time).total_seconds()
    print(f"It took {exec_time:,.2f} seconds to run", flush=True)


if __name__ == '__main__':
    main()


