# Rock-Paper-Scissors Game Server in Python

This project contains a simple multiplayer Rock-Paper-Scissors game server implemented in Python using sockets and threading. 

## Features

- **Accept Connections**: The server accepts connections from clients and adds them to a waiting list.
- **Waiting List**: The server maintains a waiting list of players who are waiting for a match.
- **Matchmaking**: Once two clients have connected, the server matches them and initiates the game.
- **Game Logic**: The server handles the logic for determining the winner of the game and broadcasts the result to both players.
- **Broadcast Waiting List**: The server broadcasts the waiting list to all clients.
- **Multiplayer Support**: The server can handle multiple games simultaneously, with each game being played by two clients.

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the directory where you saved "rps_server.py" using the `cd` command.
   ```bash
   cd /path/to/directory
   ```
3. Run the Python file using the Python command.
   ```bash
   python rps_server.py
   ```

## Testing

Unit testing is done using Python's built-in `unittest` module. To run the tests, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you saved "test_rps.py" using the `cd` command.
   ```bash
   cd /path/to/directory
   ```
3. Run the Python test file using the Python command.
   ```bash
   python -m unittest test_rps.py
   ```

**Note**: Due to the nature of socket programming and threading, it's challenging to write tests for all parts of the code. Therefore, some parts of the code are not covered by unit tests.

## Client Side

Clients can connect to the server using a socket connection. They send their choice of "rock", "paper", or "scissors" as a message to the server. The server responds with the game results once enough players have connected and made their choices. 

## Additional Notes

This server is a simple example and may not handle all edge cases or potential errors. More robust error handling and additional features (such as handling clients that disconnect unexpectedly or send invalid moves) would need to be added for a production-level server.
```

This markdown file includes information about the project, its features, how to run the server, how to run the tests, and additional notes.
