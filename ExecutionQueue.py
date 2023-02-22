import threading
import concurrent.futures
import queue

class Task:
    def __init__(self,_client_socket):
        self.client_socket = _client_socket
        
    def do_task(self):
        self.client_socket.send("Hello, client".encode())

class ExecutionQueue:
    
    def __init__(self):
        self.max_workers = 4
        self.task_queue = queue.Queue()        

    def startExecutionQueueThread(self):
        
        def createPool(task_queue):
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                while True:
                    # Get the next task from the queue
                    task = task_queue.get(block=True)

                    # Submit the task to the thread pool
                    executor.submit(task.do_task)
        
        self.executionPoolThread = threading.Thread(target=createPool, args=(self.task_queue,))
        self.executionPoolThread.start()
    
    def pushTask(self, task: Task):
        self.task_queue.put(task)