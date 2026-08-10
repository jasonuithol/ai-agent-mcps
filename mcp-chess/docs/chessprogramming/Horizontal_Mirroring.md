# Horizontal Mirroring

Source: https://www.chessprogramming.org/Horizontal_Mirroring

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Position](/Chess_Position "Chess Position") \* Horizontal Mirroring**

[![](/images/a/a0/Cheating-cheat-chess-mirror-best-demotivational-posters.jpg)](http://bestdemotivationalposters.com/delusion/)

Mirroring [[1]](#cite_note-1)

**Horizontal Mirroring** mirrors all [pieces](/Pieces "Pieces") along the vertical axis between the D- and E-[File](/Files "Files"). Applicable if both sides have lost their [castling rights](/Castling_Rights "Castling Rights"), horizontal mirroring should result in equal static [evaluation](/Evaluation "Evaluation") [score](/Score "Score"), but not necessarily equal [search](/Search "Search") result if [pieces](/Pieces "Pieces") and [squares](/Squares "Squares") are traversed in different order. Along with [vertical flipping](/Vertical_Flipping "Vertical Flipping") and/or [diagonal mirroring](/Diagonal_Mirroring "Diagonal Mirroring"), horizontal mirroring is used in pawn-less [endgame tablebases](/Endgame_Tablebases "Endgame Tablebases") to restrict a white king to the 10 squares of the a1-d4-d1 triangle of the board.

# Sample Position

## Horizontal Mirroring

| Original | Horizontal Mirroring |
| --- | --- |
| |  | | --- | |                                                             ♚                 ♘♔  ♗ | | |  | | --- | |                                                         ♚             ♗  ♔♘ | |
| k7/8/NK2B3/8/8/8/8/8 w - - | 7k/8/3B2KN/8/8/8/8/8 w - - |

## Flipping & Rotation

[Vertical flipping](/Vertical_Flipping "Vertical Flipping") and horizontal mirroring (or vice versa) results in [rotation](https://en.wikipedia.org/wiki/Rotation_%28mathematics%29) by 180 degrees.

| Vertical Flipping | 180° Rotation |
| --- | --- |
| |  | | --- | |                                                         ♘♔  ♗             ♚ | | |  | | --- | |                                                             ♗  ♔♘                 ♚ | |
| 8/8/8/8/8/NK2B3/8/k7 w - - | 8/8/8/8/8/3B2KN/8/7k w - - |

# Mirroring an 8x8 Board

An [8x8 Board](/8x8_Board "8x8 Board") with a [rank-file mapping](/Squares "Squares") needs to perform an [exclusive or](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with 7 (h1 in [LERF](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")) to horizontally mirror square coordinates. A pure 8x8 Board may be mirrored that way in [C](/C "C"):

```
int board[64], sq, s;

for (sq = 0; sq < 64; sq += ++sq & 4)  {
  s = board[sq];
  board[sq] = board[sq^7];
  board[sq^7] = s;
}
```

# See also

- [Color Flipping](/Color_Flipping "Color Flipping")
- [Diagonal Mirroring](/Diagonal_Mirroring "Diagonal Mirroring")
- [Flipping, Mirroring and Rotating](/Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating") of [Bitboards](/Bitboards "Bitboards")
- [Vertical Flipping](/Vertical_Flipping "Vertical Flipping")

# External Links

- [Mirror from Wikipedia](https://en.wikipedia.org/wiki/Mirror)
- [Mirroring (psychology) from Wikipedia](https://en.wikipedia.org/wiki/Mirroring_%28psychology%29)
- [Reflection (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28mathematics%29)
- [Reflection (physics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28physics%29)
- [Reflection symmetry from Wikipedia](https://en.wikipedia.org/wiki/Reflection_symmetry)
- [Why do Mirrors Reverse Left and Right?](http://math.ucr.edu/home/baez/physics/General/mirrors.html)
- [Venus effect from Wikipedia](https://en.wikipedia.org/wiki/Venus_effect)
- [Shocking Blue](/Category:Shocking_Blue "Category:Shocking Blue") - [Venus](https://en.wikipedia.org/wiki/Venus_(Shocking_Blue_song)) (1970), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Chess Demotivational Posters & Images](http://bestdemotivationalposters.com/tag/chess/)

**[Up one Level](/Chess_Position "Chess Position")**