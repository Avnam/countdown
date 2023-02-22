import socket
from ExecutionQueue import ExecutionQueue, Task

class GameServer:

    def __init__(self):
        self.sessions = []
        self.executionQueue = ExecutionQueue()       
        self.executionQueue.startExecutionQueueThread()

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 12345))
        server_socket.listen(5)
        print("Server is listening...")
        while True:
            #client_socket, client_address = server_socket.accept()
            client_socket, _ = server_socket.accept()
            self.executionQueue.pushTask(Task(client_socket))
            #print("Accepted connection from ", client_address)
            #client_socket.close()
            
game_server = GameServer()
game_server.start()