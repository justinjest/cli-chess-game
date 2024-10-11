# A command line chess game tool

Currently the board is rendered after each turn in your cli
Moves are accepted in a modified version of algebraic notation. All moves must be presented in format [piece][destination column][destination row]. Ie Re7
- If two pieces can move to the square you will be prompted to clarifiy it's location in the form of the grid square it is on
- If a capture is to be performed there is no need to add X. Currently you can not do so
- Pawns require their piece to be called as well.

## Known limitations
- Nothing prevents you from not blocking checks, although you will lose the game if you don't
- Pawns only promote to queens
- En Pasant is not implemented
- Draw rules are not currently in place (Both on the board and long move strings)

