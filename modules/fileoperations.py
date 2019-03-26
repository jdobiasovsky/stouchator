from collections import deque
import logging
import os


class OcrFile:
    def __init__(self, initname, initpath):
        self.name = initname
        self.path = initpath

    def fullpath(self):
        return os.path.join(self.path, self.name)


class FileQueue:
    def __init__(self):
        self.queue = deque(maxlen=None)
        logging.info('Started a new queue')

    def getqueue(self):
        return self.queue

    def enqueue(self, item):
        # insert at the end of queue
        if item in self.queue:
            logging.warning('Already in queue: {}'.format(item))
            return
        self.queue.append(item)

    def dequeue(self):
        # remove item from the front queue
        self.queue.popleft()

    def getfront(self):
        return self.queue[0]

    def getrear(self):
        return self.queue[-1]

    def remove(self, item):
        try:
            self.queue.remove(item)
        except ValueError:
            logging.warning('Failed to remove: {} not in queue'.format(item))

    def isempty(self):
        if self.queue:
            return False
        return True
