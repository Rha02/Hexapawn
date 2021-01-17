# Hexapawn
Hexapawn is a simple game  created by Martin Gardner that's used to demonstrate machine learning.
The game is a 3x3 grid, with 3 pawns on top and bottom. The pawns on top belong to the AI, while the pawns on the bottom belong to the player.

## The Game
The rules of the game are simple:
1. Each pawn acts like a pawn would do in a game of chess:
2. Go one tile forward if there is nothing ahead. Or take out opponent's piece if it is in a diagonally neighboring tile.
3. To win, you must either take out all your opponent's pawns, put your opponent at a stalemate, or have your pawn reach the opponent's side of the board.

In my app's scenario, the player's pawns are represented by the digit '1', the opponent's pawns are represented by the digin '2', and the empty tiles are represented by the digit '0'.

For the player to move their pawn, they must enter a two digit number. The first digit indicates which pawn the player wishes to move, and the second digit indicates where the player wants to move that pawn.

Each tile is represented by a digit in the following order:
<pre>
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
</pre>

This is what the board initially looks like:
<pre>
2 | 2 | 2
--+---+--
0 | 0 | 0
--+---+--
1 | 1 | 1
</pre>

The player moves first. A valid move for the player, would be for example move '74', in which case the digit '1' in tile '7' moves forward to the tile '4'. So the new board would look like this:
<pre>
2 | 2 | 2
--+---+--
1 | 0 | 0
--+---+--
0 | 1 | 1
</pre>

## Machine Learning
The AI is initially dumb, and it makes **random choices**. The AI looks at the current board, checks for possible moves, and using the Python's "random" module, it chooses a random move from the possible moves that it could make. **Once the AI loses to the player, AI's previous move is removed from the list of possible moves it could make**. In other words, the AI won't make the same mistake again, unless the player decides to exit the application. If the AI is victories, it doesn't anyhow impact its possible moves.

As the player continues playing and winning, the AI's moves become tougher and more challenging. It will be obvious to the player, as the AI becomes more proficient at the game.
