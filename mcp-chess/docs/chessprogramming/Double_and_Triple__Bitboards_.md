# Double and Triple (Bitboards)

Source: https://www.chessprogramming.org/Double_and_Triple_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Double and Triple**

**Double and Triple** pawns may be determined in the *square centric world* as well in *set-wise world* of Bitboards considering the whole board.

# By Square

Working in the *square centric world* of the board implies using a square index of one particular pawn, likely from [bitboard traversal](/Bitboard_Serialization "Bitboard Serialization"). For [doubled](/Doubled_Pawn "Doubled Pawn") (twins) or multiple pawns on a file, we simply intersect the file-mask by own-pawns and perform a [population count](/Population_Count "Population Count"). This symmetrical property appears to be equal for white and black pawns, except for the before- and behind semantic.

```
wPawnsOnFile = arrFiles[sqOfWhitePawn] & pawnBB[white];
if ( wPawnsOnFile & (wPawnsOnFile-1) ) -> white pawn is a least double pawn
if ( wPawnsOnFile & arrNortRay[sqOfWhitePawns] ) -> white pawn has own pawn ahead
if ( wPawnsOnFile & arrSoutRay[sqOfWhitePawns] ) -> white pawn has own pawn behind
```

```
arrFiles[d*]
. . . 1 . . . .
. . . 1 . . . .
. . . 1 . . . .
. . . 1 . . . .
. . . 1 . . . .
. . . 1 . . . .
. . . 1 . . . .
. . . 1 . . . .
```

The arrFiles might be condensed to eight bitboards only, instead of 64 - if we index by

```
file(sq) == sq & 7
```

instead of square.

# Multiple Pawns

Working in the *bitboard centric world* to determine pawn related pattern set-wise.

All pawns that are member of the [rearspan](/Pawn_Spans "Pawn Spans") of all own pawns, have at least one pawn in front on the same file. All pawns that are member of the [frontspan](/Pawn_Spans "Pawn Spans") of all own pawns, have at least one pawn behind on the same file.

```
// pawns with at least one pawn in front on the same file
U64 wPawnsBehindOwn(U64 wpawns) {return wpawns & wRearSpans(wpawns);}

// pawns with at least one pawn behind on the same file
U64 wPawnsInfrontOwn (U64 wpawns) {return wpawns & wFrontSpans(wpawns);}
```

Obviously, since each pawn in front of a pawn implies this pawn behind, the number of pawns in front is equal the number of pawns behind.

```
popCount(wPawnsBehindOwn) == popCount(wPawnsInfrontOwn)
```

The intersection of both sets implies at least a triple, thus a pawn in front and behind.

```
U64 wPawnsInfrontAndBehindOwn (U64 wpawns) {
   return wPawnsInfrontOwn(wpawns) &  wPawnsBehindOwn(wpawns);
}
```

If the intersection is empty on a file, it is a double pawn or a twin.

```
fileWithAtLeastTriple = fileFill(infrontAndBehindOwn);
rearTwin  = behindOwn  & ~fileWithAtLeastTriple;
frontTwin = infrontOwn & ~fileWithAtLeastTriple;
```

# Forum Posts

- [Doubled and Backward Pawn Engine "Definitions"](http://www.talkchess.com/forum/viewtopic.php?t=29689) by [Brian Richardson](/Brian_Richardson "Brian Richardson"), [CCC](/CCC "CCC"), September 07, 2009
- [Doubled pawns](http://www.talkchess.com/forum/viewtopic.php?t=60133) by [Stefano Gemma](/Stefano_Gemma "Stefano Gemma"), [CCC](/CCC "CCC"), May 11, 2016

# External Links

- [Doubled pawns from Wikipedia](https://en.wikipedia.org/wiki/Doubled_pawns)

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**