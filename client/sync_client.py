from threading import Thread
import asyncio
import time


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

print('started.')

new_loop.call_soon_threadsafe(more_work, 6)
new_loop.call_soon_threadsafe(more_work, 3)

