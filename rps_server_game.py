import socket
import threading
from collections import deque

# Rules of the game
GAME_RULES = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

# Players waiting to play
waiting_players = deque(maxlen=6)


class Player:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.choice = None

def handle_client(player):
    """Handle client connection"""
    while True:
        try:
            msg = player.conn.recv(1024).decode('utf-8').strip()
            if msg in GAME_RULES.keys():
                player.choice = msg
                play_game(player)
            elif msg == 'quit':
                player.conn.close()
                waiting_players.remove(player)
                broadcast_waiting_list()
                break
        except:
            print('Connection closed')
            waiting_players.remove(player)
            broadcast_waiting_list()
            break

def play_game(player):
    """Handle game logic"""
    if len(waiting_players) < 2:
        waiting_players.append(player)
        broadcast_waiting_list(waiting_players)
    else:
        player1 = waiting_players.popleft()
        player2 = waiting_players.popleft() if waiting_players else player

        winner = determine_winner(player1, player2)
        for p in (player1, player2):
            p.conn.send(f'Winner is {winner.addr}\n'.encode('utf-8'))

def determine_winner(player1, player2):
    """Determine game winner"""
    if GAME_RULES[player1.choice] == player2.choice:
        return player1
    elif GAME_RULES[player2.choice] == player1.choice:
        return player2
    else:
        return None

def broadcast_waiting_list(waiting_players):
    """Broadcast waiting list to all clients"""
    for player in waiting_players:
        player.conn.send(f'Waiting players: {[p.addr for p in waiting_players]}\n'.encode('utf-8'))

def start_server(host = '127.0.0.1', port = 55555):
    """Start server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(6)

    print(f'Server started on {host}:{port}')

    while True:
        conn, addr = server.accept()
        player = Player(conn, addr)
        thread = threading.Thread(target=handle_client, args=(player,))
        thread.start()

        print(f'Connection from {addr}')

if __name__ == "__main__":
    start_server()
