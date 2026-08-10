# Vertical Flipping

Source: https://www.chessprogramming.org/Vertical_Flipping

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Position](/Chess_Position "Chess Position") \* Vertical Flipping**

[![](https://upload.wikimedia.org/wikipedia/commons/4/4f/FrontAerial.gif)](/File:FrontAerial.gif)

Acrobatic Flip [[1]](#cite_note-1)

**Vertical Flipping** mirrors all [pieces](/Pieces "Pieces") along the horizontal axis between the 4th and 5th [rank](/Ranks "Ranks"). Opposed to [color flipping](/Color_Flipping "Color Flipping") it does not swap the piece colors and [side to move](/Side_to_move "Side to move"), and therefor with respect to the [front span](/Pawn_Spans "Pawn Spans") of [pawns](/Pawn "Pawn"), is only applicable in pawn-less [endgames](/Endgame "Endgame") with [castling](/Castling "Castling") no longer possible, and results in an equivalent position with identical [evaluation](/Evaluation "Evaluation") and same number of attacks and moves. Along with [horizontal](/Horizontal_Mirroring "Horizontal Mirroring") and/or [diagonal mirroring](/Diagonal_Mirroring "Diagonal Mirroring"), vertical flipping is used in pawn-less [endgame tablebases](/Endgame_Tablebases "Endgame Tablebases") to restrict a white king to the 10 squares of the a1-d4-d1 triangle of the board.

# Sample Position

| Original | Vertical Flip | Color Flip |
| --- | --- | --- |
| |  | | --- | |                                                             ♚                 ♘♔  ♗ | | |  | | --- | |                                                         ♘♔  ♗             ♚ | | |  | | --- | |                                                         ♞♚  ♝             ♔ | |
| k7/8/NK2B3/8/8/8/8/8 w - - | 8/8/8/8/8/NK2B3/8/k7 w - - | 8/8/8/8/8/nk2b3/8/K7 b - - |

# Flipping an 8x8 Board

An [8x8 Board](/8x8_Board "8x8 Board") with a [rank-file mapping](/Squares "Squares"), needs to perform an [exclusive or](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with 56 (A8 in [LERF](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")) to vertically flip square coordinates. A pure 8x8 Board may be vertically flipped that way in [C](/C "C"):

```
int board[64], sq, s, f;

for (sq = 0; sq < 32; ++sq) {
  s = board[sq];
  board[sq] = board[sq^56];
  board[sq^56] = s;
}
```

# See also

- [Color Flipping](/Color_Flipping "Color Flipping")
- [Diagonal Mirroring](/Diagonal_Mirroring "Diagonal Mirroring")
- [Flipping, Mirroring and Rotating](/Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating") of [Bitboards](/Bitboards "Bitboards")
- [Horizontal Mirroring](/Horizontal_Mirroring "Horizontal Mirroring")

# External Links

- [flip - Wiktionary](http://en.wiktionary.org/wiki/flip)

:   [ausflippen - Wiktionary](http://en.wiktionary.org/wiki/ausflippen)

- [Flip from Wikipedia](https://en.wikipedia.org/wiki/Flip)
- [Flip (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Flip_%28mathematics%29)
- [Reflection (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28mathematics%29)
- [Reflection (physics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28physics%29)
- [Reflection symmetry from Wikipedia](https://en.wikipedia.org/wiki/Reflection_symmetry)

# References

1. [↑](#cite_ref-1) A [front aerial](https://en.wikipedia.org/wiki/Front_aerial) performed as part of an [acro dance](https://en.wikipedia.org/wiki/Acro_dance) routine, image by [User: Lambtron](https://en.wikipedia.org/wiki/User:Lambtron), April 29, 2008, [Flip (acrobatic) from Wikipedia](https://en.wikipedia.org/wiki/Flip_%28acrobatic%29)

**[Up one Level](/Chess_Position "Chess Position")**