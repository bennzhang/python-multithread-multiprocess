import Queue
import threading
import time
import os

exitFlag = 0
queueLock = threading.Lock()
workQueue = Queue.Queue()
nThreads = 16

class Worker (threading.Thread):
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q

    def run(self):
        print "Starting thread " + str(self.threadID)
        while not exitFlag:
           queueLock.acquire()
           if not self.q.empty():
               cmd = self.q.get()
               #print (cmd)
               queueLock.release()
               start_time = int(round(time.time() * 1000))
               os.system(cmd)
               total_time = int(round(time.time() * 1000)) - start_time
               print "command: %s, total_time....%s" % (cmd,str(total_time))
           else:
               queueLock.release()
        print "Exiting thread " + str(self.threadID)

# Create working queue
cmd_list=[
   'sleep 1',
   'sleep 2',
   'sleep 3',
   'sleep 4',
   'sleep 5',
   'sleep 6',
   'sleep 7',
   'sleep 8',
   'sleep 9',
   'sleep 10',
   'sleep 11',
   'sleep 12',
   'sleep 13',
   'sleep 14',
   'sleep 1',
   'sleep 2',
   'sleep 3',
   'sleep 4',
   'sleep 5',
   'sleep 6',
   'sleep 7',
   'sleep 8',
   'sleep 9',
   'sleep 10',
   'sleep 11',
   'sleep 12',
   'sleep 13',
   'sleep 14',
   'sleep 1',
   'sleep 2',
   'sleep 3',
   'sleep 4',
   'sleep 5',
   'sleep 6',
   'sleep 7',
   'sleep 8',
   'sleep 9',
   'sleep 10',
   'sleep 11',
   'sleep 12',
   'sleep 13',
   'sleep 14',
   'sleep 1',
   'sleep 2',
   'sleep 3',
   'sleep 4',
   'sleep 5',
   'sleep 6',
   'sleep 7',
   'sleep 8',
   'sleep 9',
   'sleep 10',
   'sleep 11',
   'sleep 12',
   'sleep 13',
   'sleep 14',
]

for cmd in cmd_list:
    workQueue.put(cmd)


# Create new threads and start them
threads = []
for i in range(nThreads):
    thread=Worker(i, workQueue)
    thread.start()
    threads.append(thread)


# Wait for working queue to empty
while not workQueue.empty():
    pass

# Notify threads to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()

print "Done"
