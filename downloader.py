import asyncio
import concurrent.futures
import math
import os

import requests

total = 0
size = 0


async def get_size(url):
    response = requests.head(url)
    size = int(response.headers['Content-Length'])
    return size


def download_range(url, start, end, output, seg):
    global total

    headers = {'Range': f'bytes={start}-{end}'}
    response = requests.get(url, headers=headers, stream=True)
    with open(output, 'wb') as f:
        for part in response.iter_content(512 * 1024):
            f.write(part)
            total += 512 * 1024
            print("{}%".format(round(total * 100 / size, 2)))


async def download(executor, url, output):
    global size
    loop = asyncio.get_event_loop()
    file_size = await get_size(url)
    size = file_size
    chunk_size = math.ceil(file_size / 10)
    chunks = range(0, file_size, chunk_size)

    tasks = [
        loop.run_in_executor(
            executor,
            download_range,
            url,
            start,
            start + chunk_size - 1,
            f'{output}.part{i}',
            i
        )
        for i, start in enumerate(chunks)
    ]
    await asyncio.wait(tasks)
    print("Integrating")
    with open(output, 'wb') as o:
        for i in range(len(chunks)):
            chunk_path = f'{output}.part{i}'
            with open(chunk_path, 'rb') as s:
                o.write(s.read())
            os.remove(chunk_path)
        o.close()


def downloader(url, output):
    global total
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    loop = asyncio.new_event_loop()
    try:
        print("Starting download")
        loop.run_until_complete(
            download(executor, url, output)
        )
    finally:
        print(output)
        loop.close()
        total = 0
