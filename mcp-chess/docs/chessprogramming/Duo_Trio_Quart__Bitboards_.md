# Duo Trio Quart (Bitboards)

Source: https://www.chessprogramming.org/Duo_Trio_Quart_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Duo Trio Quart**

[![](/images/3/3e/SamuelBakWhiteAndBlue.jpg)](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bba)

[Samuel Bak](/Category:Samuel_Bak "Category:Samuel Bak") - White and Blue [[1]](#cite_note-1)

**Pawn-Duo**, (Phalanx) [[2]](#cite_note-2)   
two adjacent [pawns](/Pawn "Pawn") of the same [color](/Color "Color") on the same [rank](/Ranks "Ranks") that mutually cover the other's [stop square](/Stop_Square "Stop Square"). A **Trio** are three horizontal friendly pawns, a **Quart** four horizontal friendly pawns.

*Working in the bitboard centric world to determine pawn related pattern set-wise*.

*The code snippets rely on [shifting bitboards](/General_Setwise_Operations#ShiftingBitboards "General Setwise Operations"), specially by [one step only](/General_Setwise_Operations#OneStepOnly "General Setwise Operations").*

# Neighbors

To get pawns with east or west neighbors is simple:

```
U64 pawnsWithEastNeighbors(U64 pawns) {
   return pawns & westOne (pawns);
}

U64 pawnsWithWestNeighbors(U64 pawns) {
   return pawnsWithEastNeighbors(pawns) << 1; // * 2
}
```

or

```
U64 pawnsWithWestNeighbors(U64 pawns) {
   return pawns & eastOne (pawns);
}

U64 pawnsWithEastNeighbors(U64 pawns) {
   return pawnsWithWestNeighbors(pawns) >> 1;
}
```

|  |
| --- |
|                                                              ♙♙♙                    ♙♙ |

```
pawns               pawns with east     pawns with west     pawns with east
                    neighbors           neighbors           and west neighbors
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
1 1 1 . . . . .     1 1 . . . . . .     . 1 1 . . . . .     . 1 . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . 1 1 .     . . . . . 1 . .     . . . . . . 1 .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
```

# Neighbor Algebra

Pawns with east or west neighbors are at least member of a duo. Pawns with east and west neighbors at least member of a trio. If two neighbors have both east and west neighbors, it is at least a quart.

An exclusive pawn duo is therefor a pawn with one neighbor, while this neighbor has no other neighbor as well.

```
U64 duo (U64 pawns) {
   U64 withWestNeighbors = pawnsWithWestNeighbors(pawns);
   U64 withEastNeighbors = withWestNeighbors >> 1;

   U64 withOneExclusiveNeighbor  = withWestNeighbors ^ withEastNeighbors;
   U64 withExclusiveWestNeighbor = withWestNeighbors & withOneExclusiveNeighbor;
   U64 withExclusiveEastNeighbor = withEastNeighbors & withOneExclusiveNeighbor;

   U64 duoWestOne = withEclusiveEastNeighbor & (withEclusiveWestNeighbor >> 1);
   U64 duoEastOne = duoWestOne << 1;
   return duoWestOne | duoEastOne;
}
```

```
pawns               pawns with excl.    pawns with excl.    duo
                    east neighbor       west neighbor
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
1 1 1 . . . . .     1 . . . . . . .     . . 1 . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . 1 1 .     . . . . . 1 . .     . . . . . . 1 .     . . . . . 1 1 .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
```

# See also

- [Stop Square](/Stop_Square "Stop Square")
- [Hanging Pawns](/Hanging_Pawns "Hanging Pawns")
- [Pawn Islands (Bitboards)](/Pawn_Islands_(Bitboards) "Pawn Islands (Bitboards)")
- [Phalanx](/Phalanx "Phalanx") (Engine)

# Forum Posts

- [The phalanx concept](http://www.talkchess.com/forum/viewtopic.php?t=52382) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), May 21, 2014

# External Links

- [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")
- [Duet from Wikipedia](https://en.wikipedia.org/wiki/Duet)
- [Phalanx from Wikipedia](https://en.wikipedia.org/wiki/Phalanx)
- [Trio from Wikipedia](https://en.wikipedia.org/wiki/Trio)
- [Kinga Głyk Trio](http://kingaglyk.pl) - Walking Baby, [VisionInMusica](http://www.visioninmusica.com/), [Terni](https://en.wikipedia.org/wiki/Terni), March 10, 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Kinga Głyk](/Category:Kinga_G%C5%82yk "Category:Kinga Głyk"), [Irek Głyk](http://glyk.pl/), [Rafal Stepien](http://www.visioninmusica.com/kinga-glyk-happy-birthday/)

- [Quart (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Quart_%28disambiguation%29)
- [Panta Rhei](/Category:Panta_Rhei "Category:Panta Rhei") plays [Bartók's](https://en.wikipedia.org/wiki/B%C3%A9la_Bart%C3%B3k) Quarts, 1977, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) 
   [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bba), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](/University_of_Minnesota "University of Minnesota")
2. [↑](#cite_ref-2) [Pawn Structure (General) | Page 5 of 5 | Phalanx Formation](http://www.chess-game-strategies.com/pawn-structure_general_page-5_phalanx-formation.html)

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**