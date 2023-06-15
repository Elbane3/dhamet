import socket
from essai_31 import Connection
from essai_31 import initialize_game_state
from essai_31 import update_game_state

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []
    
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"New connection from {address}")
            connection = Connection(client_socket)
            self.connections.append(connection)
            self.handle_client(connection)
    
    def handle_client(self, connection):
        # Initialize the game state
        game_state = initialize_game_state()

        while True:
            try:
                # Receive the client's move and update the game state
                move = connection.receive_move()
                game_state = update_game_state(game_state, move)

                # Send the updated game state to all clients
                for other_connection in self.connections:
                    if other_connection != connection:
                        other_connection.send_game_state(game_state)

            except:
                print(f"Client disconnected")
                self.connections.remove(connection)
                connection.close()
                break
   
server = Server('10.55.123.179',8888)
server.start()
