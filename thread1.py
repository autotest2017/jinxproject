#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue

q=Queue.Queue(5)
print (q.maxsize)
q.put(123)

print (q.get())
