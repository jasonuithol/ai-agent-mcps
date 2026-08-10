# Unfree Pawns (Bitboards)

Source: https://www.chessprogramming.org/Unfree_Pawns_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Unfree Pawns**

**Unfree Pawns**, (Closed Pawns)
are pawns with a mechanical obstruction of an opponent pawn in front. Being an unfree pawn is therefore a mutual property for both white and black pawns on a **closed** file. Even if weak, like isolated or backward, **unfree** pawns are considered less vulnerable than open pawns on a halfopen file. Thus, in the [initial position](/Initial_Position "Initial Position") all pawns are unfree.

# Unfree Single Pawn

Working in the *square centric* world of the board, thus using a square index of **one** particular pawn, likely from [bitboard traversal](/Bitboard_Serialization "Bitboard Serialization"), to lookup pre-calculated pattern.

For a single pawn we need to access a lookup-table to get all squares on the same file in front of the pawn. If the intersection of the frontspan with the set of opponent pawns is not empty, it is an unfree or closed pawn.

```
U64 arrFrontSpans[2][64];

if ( (arrFrontSpans[white][sqOfWhitePawn] & pawnBB[black]) != 0 ) -> pawn unfree
```

```
arrFrontSpan[white][d4]
. . . 1 . . . .
. . . 1 . . . .
. . . 1 . . . .
. . . 1 . . . .
. . . p . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
```

# Unfree Pawns set-wise

Working in the *bitboard centric* world to determine pawn related pattern *set-wise*.

Unfree (or closed) Pawns have a mechanical obstruction in front - an opponent pawn as member of the own [frontfill](/Pawn_Fills "Pawn Fills") or [frontspan](/Pawn_Spans "Pawn Spans"). An intersection with opponents frontspans is sufficient to determine unfree pawns:

```
U64 wUnfreePawns(U64 wpawns, U64 bpawns) {
   return wpawns & bFrontSpan(bpawns);
}

U64 bUnfreePawns(U64 bpawns, U64 wpawns) {
   return bpawns & wFrontSpan(wpawns);
}
```

# External Links

- [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)") [[1]](#cite_note-1)
- [The Game of Chess: Pawns and Their Related Terms](http://www.justchess.biz/chesspawns.htm) from [Just Chess .biz](http://www.justchess.biz/)

# See also

- [Open Pawns](/Open_Pawns_(Bitboards) "Open Pawns (Bitboards)")
- [Passed Pawns](/Passed_Pawns_(Bitboards) "Passed Pawns (Bitboards)")
- [Candidates](/Candidates_(Bitboards) "Candidates (Bitboards)")

# References

1. [↑](#cite_ref-1) [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**