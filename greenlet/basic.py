from gevent import Greenlet
import time


class BaseService(Greenlet):
    def __init__(self, message):
        Greenlet.__init__(self)
        self.start(message)

    def start(self, message):
        while True:
            print(message)
            time.sleep(2)


a = BaseService('a')
b = BaseService('b')

a.run()
b.run()

time.sleep(100)

