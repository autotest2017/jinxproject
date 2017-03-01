#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue, threading,time,random

class consumer(threading.Thread):

    def __init__(self,que):
        threading.Thread.__init__(self)
        self.daemon = False
        self.queue = que

    def run(self):
        while True:
            if self.queue.empty():
                break
            item = self.queue.get()
            time.sleep(item)
            print self.name, item
            self.queue.task_done()
        return

que = Queue.Queue()
for x in range (10):
    que.put(random.random())

print  que
consumers = [consumer(que) for x in range(5)]

for c in consumers:
    c.start()

for c in consumers:
    c.join()
