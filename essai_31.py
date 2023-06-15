import pygame
from pygame import WINDOWRESIZED
import pieces
from view import View
from controller import Controller
import json
import socket
import sys

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("DHAMET_essai_3")

def initialize_game_state():
    board = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
    ]
    state = {
        'board': board,
        'player_turn': 1,
        'winner': None,
    }
    return state

def update_game_state(game_state, move):
    """Updates the game state with the given move."""
    # Update the game board with the new move
    game_state['board'][move['to_row']][move['to_col']] = game_state['board'][move['from_row']][move['from_col']]
    game_state['board'][move['from_row']][move['from_col']] = 0

    # Return the updated game state
    return game_state


# screen resolution
res = (800, 700)

# opens up a window
screen = pygame.display.set_mode(res)

bo = pygame.image.load("imgs/screen.png")
# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 75)
buttonFont = pygame.font.SysFont('Arial', 40)

# rendering a text written in
# this font
Welcome = smallfont.render('Soyez le bienvenue', True, color)
Jouer = buttonFont.render('JOUER', True, color)



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
   
server = Server('10.45.16.164', 5595)
server.start()



class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.socket.connect((self.host, self.port))
    
    def send_move(self, move):
        move_str = json.dumps(move)
        self.socket.sendall(move_str.encode())
    
    def receive_move(self):
        data = b''
        while b'\n' not in data:
            packet = self.socket.recv(2048)
            if not packet:
                break
            data += packet
        move_str = data.decode().strip()
        move = json.loads(move_str)
        return move
    
    def close(self):
        self.socket.close()
            
def play():
    V = View()
    C = Controller()
    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == WINDOWRESIZED:
                V.size = (V.board.get_width(), V.board.get_height())
            if event.type == pygame.MOUSEBUTTONDOWN:
                C.action()
        if pieces.whiteCount == 40 or pieces.blackCount == 40:
            print("Le match est terminé")
            break

        V.redrawGame()


while True:
    screen.blit(bo, (0, 0))
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            quit()
        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            # button the game is terminated
            if 233 <= mouse[0] <= 467 and height / 2 <= mouse[1] <= height / 2 + 60:
                play()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if 233 <= mouse[0] <= 566 and height / 2 <= mouse[1] <= height / 2 + 60:
        pygame.draw.rect(screen, color_light, [233, height / 2, 333, 60])

    else:
        pygame.draw.rect(screen, color_dark, [233, height / 2, 333, 60])
    # superimposing the text onto our button
    screen.blit(Jouer, (340, height / 2 + 7))
    # updates the frames of the game
    pygame.display.update()
