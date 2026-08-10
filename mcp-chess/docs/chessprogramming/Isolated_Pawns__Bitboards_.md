# Isolated Pawns (Bitboards)

Source: https://www.chessprogramming.org/Isolated_Pawns_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Isolated Pawns**

An **Isolated Pawn** or **Isolani** has no friendly pawns on adjacent [files](/Files "Files"). Isolanis may be determined inside the *square centric world* as well in *set-wise world* of Bitboards considering the whole board.

# Isolani by Square

To determine whether a pawn is isolated, we simply lookup an [array](/Array "Array") with neighboring file-masks. If the [intersection](/General_Setwise_Operations#Intersection "General Setwise Operations") of neighbored files with own pawns is empty, the pawn is isolated. This symmetrical property appears to be equal for white and black pawns.

```
if ( (arrNeighborFiles[sqOfWhitePawn] & pawnBB[white]) == 0 ) -> pawn is isolated
```

```
arrNeighborFiles[d*]
. . 1 . 1 . . .
. . 1 . 1 . . .
. . 1 . 1 . . .
. . 1 . 1 . . .
. . 1 . 1 . . .
. . 1 . 1 . . .
. . 1 . 1 . . .
. . 1 . 1 . . .
```

The arrNeighborFiles might be condensed to eight bitboards only, instead of 64 - if we index by

```
file(sq) == sq & 7
```

instead of square.

# Isolanis and Half-isolanis set-wise

Isolated pawns are the [relative complement](/General_Setwise_Operations#RelativeComplement "General Setwise Operations") of pawns with the union of their own [attack fills](/Attack_Spans "Attack Spans") over the whole file. To keep disjoint pawns with no neighbor on either east or west adjacent files has the advantage of greater versatility. Isolanis are the intersection of them, half-isolanis the exclusive or:

```
U64 noNeighborOnEastFile (U64 pawns) {
    return pawns & ~westAttackFileFill(pawns);
}

U64 noNeighborOnWestFile (U64 pawns) {
    return pawns & ~eastAttackFileFill(pawns);
}

U64 isolanis(U64 pawns) {
   return  noNeighborOnEastFile(pawns)
         & noNeighborOnWestFile(pawns);
}

U64 halfIsolanis(U64 pawns) {
   return  noNeighborOnEastFile(pawns)
         ^ noNeighborOnWestFile(pawns);
}
```

# Hanging pawns

[Hanging pawns](/Hanging_Pawns "Hanging Pawns") are a [duo](/Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)") of [open](/Open_Pawns_(Bitboards) "Open Pawns (Bitboards)") and half-isolated pawns.

```
U64 wHangingPawns(U64 wpawns, U64 bpawns) {
   return wOpenPawns(wpawns, bpawns)
        & halfIsolanis(wpawns) & duo(wpawns);
}
```

# See also

- [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
- [Dispersion and Distortion](/Dispersion_and_Distortion "Dispersion and Distortion")
- [Pawn Islands](/Pawn_Islands "Pawn Islands")

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**