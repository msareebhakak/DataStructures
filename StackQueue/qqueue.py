#
# Author: Sareeb Hakak
# Purpose: Learn Queue DS
# Date: 25 Feb 24
# Queue has 2 main operations: push and pop
# It follows FIFO (First In First Out)
# For python, use list or collections.deque from collections, in C++ std::queue
#
from collections import deque
import threading
import time


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0


if __name__ == '__main__':
    stock_price = []
    stock_price.insert(0, 130)
    stock_price.insert(0, 132)
    stock_price.insert(0, 133)
    stock_price.insert(0, 136)
    print(stock_price)
    stock_price.pop()
    print(stock_price)
    stock_price.pop()
    print(stock_price)

    q = deque()
    q.appendleft(130)
    q.appendleft(132)
    q.appendleft(133)
    q.appendleft(136)
    print(q)
    q.pop()
    print(q)
    q.pop()
    print(q)

    # food ordering system with queue
    qq = Queue()
    global done

    def place_order():
        orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
        for order in orders:
            qq.enqueue(order)
            print(f'At {time.time()} order for {order} placed')
            time.sleep(0.5)

    def serve_order():
        global done
        while True:
            if qq.is_empty():
                done = True
                break
            serve = qq.dequeue()
            print(f'At {time.time()} order for {serve} served')
            time.sleep(2)

    t1 = threading.Thread(target=place_order())
    t2 = threading.Thread(target=serve_order())

    t1.start()
    time.sleep(1)
    t2.start()

    if done:
        print('Dinner Done')
    # print binary numbers from 1 to 10 using Queue
