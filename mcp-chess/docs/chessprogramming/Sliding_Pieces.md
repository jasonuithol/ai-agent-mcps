# Sliding Pieces

Source: https://www.chessprogramming.org/Sliding_Pieces

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Pieces](/Pieces "Pieces") \* Sliding Pieces**

**Sliding Pieces** can move an indefinite number of [squares](/Squares "Squares") along a [horizontal](/Ranks "Ranks"), [vertical](/Files "Files"), or [diagonal](/Diagonals "Diagonals") line until the edge of the board or another piece obstructs the [ray](/Rays "Rays") of a line. This applies for [bishops](/Bishop "Bishop"), [rooks](/Rook "Rook") and [queen](/Queen "Queen"). Sliding piece [move generation](/Move_Generation "Move Generation") is more extensive than generation of none sliding [knight](/Knight "Knight"), [pawn](/Pawn "Pawn") or [king](/King "King") moves. With board arrays it requires a loop along the ray, scanning each square for emptiness to continue, or [occupancy](/Occupancy "Occupancy") by own or opponent piece to break, combined with an off the board test to terminate the ray loop as well. However, such a loop may be designed in an efficient way generalized for all pieces as broached in [Table-driven Move Generation](/Table-driven_Move_Generation "Table-driven Move Generation") and in [Bruce Moreland's](/Bruce_Moreland "Bruce Moreland") *Programming Topics* [[1]](#cite_note-1). With [bitboards](/Bitboards "Bitboards") one relies on the various techniques to [generate attack sets](/Sliding_Piece_Attacks "Sliding Piece Attacks"), which further requires [serialization](/Bitboard_Serialization "Bitboard Serialization") to finally [encode moves](/Encoding_Moves "Encoding Moves") in move generation.

The advantage of the bitboard method seems the cheaper generation of moves to certain subsets of squares, for instance [captures](/Captures "Captures") in [quiescence search](/Quiescence_Search "Quiescence Search"). Despite [Fritz Reul](/Fritz_Reul "Fritz Reul") demonstrated dense and efficient [blocking loops](/Vector_Attacks#NewArchitecture "Vector Attacks") in [mailbox](/Mailbox "Mailbox") based [board representations](/Board_Representation "Board Representation"), and in conjunction with [disjoint piece flags](/Pieces#DisjointPieceFlags "Pieces") and [piece-lists](/Piece-Lists "Piece-Lists") [[2]](#cite_note-2).

# See also

- [Bishop](/Bishop "Bishop")
- [Blocking Loop](/Vector_Attacks#NewArchitecture "Vector Attacks")
- [Discovered Attack](/Discovered_Attack "Discovered Attack")
- [Discovered Check](/Discovered_Check "Discovered Check")
- [Move Generation](/Move_Generation "Move Generation")
- [Pin](/Pin "Pin")
- [Rook](/Rook "Rook")
- [Queen](/Queen "Queen")
- [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") with [Bitboards](/Bitboards "Bitboards")
- [Table-driven Move Generation](/Table-driven_Move_Generation "Table-driven Move Generation")
- [Vector Attacks](/Vector_Attacks "Vector Attacks")
- [Vulnerable on Distant Checks](/King_Pattern#VulnerableOnDistantChecks "King Pattern") from [King Pattern](/King_Pattern "King Pattern") in [Bitboards](/Bitboards "Bitboards")
- [X-ray](/X-ray "X-ray")
- [X-ray Attacks (Bitboards)](/X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)")

# References

1. [↑](#cite_ref-1) [Move Table move generation](http://web.archive.org/web/20070715002634/www.brucemo.com/compchess/programming/movetable.htm) from [Bruce Moreland's](/Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
2. [↑](#cite_ref-2) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. Thesis, *Chapter 2 Non-Bitboard Architectures*

**[Up one Level](/Pieces "Pieces")**