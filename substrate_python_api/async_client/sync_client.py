from threading import Thread
import asyncio
import time


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    while True:
        print('More work {}'.format(x))
        time.sleep(x)
        print('Finished more work {}'.format(x))


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

print('started.')

new_loop.call_soon_threadsafe(more_work, 2)

new_loop2 = asyncio.new_event_loop()
t2 = Thread(target=start_loop, args=(new_loop2,))
t2.start()
new_loop2.call_soon_threadsafe(more_work, 1)

print('over.')
time.sleep(10)
t2.join()
t.join()
new_loop2.close()
new_loop.close()


