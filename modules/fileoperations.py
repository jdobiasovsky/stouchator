"""Classes and modules for specific file operations and queuing."""
from collections import deque
import logging
import os


class OcrFile:
    """Handles documents and their paths."""

    def __init__(self, initname, initpath):
        """Save path and filename."""
        self.name = initname
        self.path = initpath
        self.status = "Waiting"

    def fullpath(self):
        """Join paths together to get full."""
        return os.path.join(self.path, self.name)

    def getstatus(self):
        """Return status variable."""
        return self.status

    def setstatus(self, setto):
        """Set status to str."""
        self.status = setto


class FileQueue:
    """Queuing and queue related operations."""

    def __init__(self):
        """Create new queue on instance."""
        self.queue = deque(maxlen=None)

    def getqueue(self):
        """Get queue object."""
        return self.queue

    def enqueue(self, item):
        """Insert item at the end of queue."""
        if item in self.queue:
            logging.warning('Already in queue: %s', item)
            return
        self.queue.append(item)

    def dequeue(self):
        """Remove item from the front queue."""
        self.queue.popleft()

    def getfront(self):
        """Return front of the queue."""
        return self.queue[0]

    def getrear(self):
        """Return last item added (rear)."""
        return self.queue[-1]

    def remove(self, item):
        """Remove item from queue without regard to position."""
        try:
            self.queue.remove(item)
        except ValueError:
            logging.warning('Failed to remove: %s not in queue', item)

    def isempty(self):
        """Check if queue is empty."""
        if self.queue:
            return False
        return True
