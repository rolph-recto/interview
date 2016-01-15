#!/usr/bin/env python
# threads.py
# example of multithreading in python

import sys
from time import time
import threading
import Queue

TOTAL = 0
TOTAL_LOCK = threading.Lock()

class CountThread(threading.Thread):
    def __init__(self, name):
        super(CountThread, self).__init__()
        self.name = name

    def run(self):
        global TOTAL
        TOTAL_LOCK.acquire()
        for i in range(100000):
            TOTAL += 1

        print 'THREAD {} : {}'.format(self.name, TOTAL)
        sys.stdout.flush()
        TOTAL_LOCK.release()

def count():
    a = CountThread('a')
    b = CountThread('b')
    a.start()
    b.start()


# processes print jobs
class Printer(threading.Thread):
    def __init__(self, print_queue):
        super(Printer, self).__init__()
        self.queue = print_queue
        self.job_count = 0
        self.quit = threading.Event()

    def run(self):
        while not self.quit.is_set():
            try:
                job = self.queue.get(block=False, timeout=0.5)
                self.job_count += 1
                print 'JOB #{}: {}'.format(self.job_count, job)
            except Queue.Empty:
                continue

# print the time every once in a while
class TimePrinter(threading.Thread):
    def __init__(self, print_queue):
        super(TimePrinter, self).__init__()
        self.queue = print_queue
        self.quit = threading.Event()

    def run(self):
        if not self.quit.set():
            self.queue.put('NUMBER OF SECONDS AFTER EPOCH {}'.format(time()))
            repeat = threading.Timer(3.0, self.run)
            repeat.daemon = True
            repeat.start()

def print_queue():
    jobs = Queue.Queue()
    scheduler = TimePrinter(jobs)
    scheduler.start()
    printer = Printer(jobs)
    printer.start()
    while True:
        job = raw_input()

        if job == 'quit':
            scheduler.quit.set()
            printer.quit.set()
            break
        else:
            jobs.put(job)
    
def main():
    # count()
    print_queue()

if __name__ == '__main__':
    main()
