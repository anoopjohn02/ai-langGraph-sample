
"""
The stream module
"""
from queue import Queue
from threading import Thread

from app.ai.handlers import StreamingHandler


class Streamable:
    """
    Streamable chain
    """
    def stream(self, input):
        """
        Stream function
        Args:
            input(Any): the user input
        """
        queue = Queue()
        handler = StreamingHandler(queue)

        def task():
            self(input, callbacks=[handler])

        Thread(target=task).start()
        while True:
            token = queue.get()
            if token is None:
                break
            yield token.replace('\n', '<br>')