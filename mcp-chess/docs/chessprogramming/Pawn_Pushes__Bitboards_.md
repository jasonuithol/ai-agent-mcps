# Pawn Pushes (Bitboards)

Source: https://www.chessprogramming.org/Pawn_Pushes_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Pawn Pushes**

[![](/images/e/e9/Chimpanzee1d4.jpg)](http://alchessmist.blogspot.de/2008/12/animal-cognition-theory-of-mind-and.html)

[Chimpanzee](https://en.wikipedia.org/wiki/Chimpanzee) pushing 1. d4 [[1]](#cite_note-1) [[2]](#cite_note-2)

Bitboards allow to determine [pawn push](/Pawn_Push "Pawn Push") target squares, or equivalently their [stop squares](/Stop_Square "Stop Square") set-wise, while pawn pushes of a single pawn are the domain of [mailbox](/Mailbox "Mailbox")-approaches. To generate the single-step targets for all pawns requires vertical shift by one [rank](/Ranks "Ranks") and [intersection](/General_Setwise_Operations#Intersection "General Setwise Operations") with the set of empty squares. The resulting set might be shifted one more time for the double pushes by further intersection with empty squares on the fourth (white) or fifth (black) double push target ranks. Since double pushing triggers determination of [en passant](/En_passant "En passant") target square, it makes sense to [serialize](/Bitboard_Serialization "Bitboard Serialization") both sets separately for different [move encoding](/Encoding_Moves "Encoding Moves").

# Push per Side

Keeping different but most efficient code for both white and black pawns. The code snippets rely on [shifting bitboards](/General_Setwise_Operations#ShiftingBitboards "General Setwise Operations"), specially by [one step only](/General_Setwise_Operations#OneStepOnly "General Setwise Operations").

```
U64 wSinglePushTargets(U64 wpawns, U64 empty) {
   return nortOne(wpawns) & empty;
}

U64 wDblPushTargets(U64 wpawns, U64 empty) {
   const U64 rank4 = C64(0x00000000FF000000);
   U64 singlePushs = wSinglePushTargets(wpawns, empty);
   return nortOne(singlePushs) & empty & rank4;
}

U64 bSinglePushTargets(U64 bpawns, U64 empty) {
   return soutOne(bpawns) & empty;
}

U64 bDoublePushTargets(U64 bpawns, U64 empty) {
   const U64 rank5 = C64(0x000000FF00000000);
   U64 singlePushs = bSinglePushTargets(bpawns, empty);
   return soutOne(singlePushs) & empty & rank5;
}
```

# Pawns able to Push

To get the set of source squares of pawns able to push is about intersection of pawns with the shifted empty squares in opposite [direction](/Direction "Direction"):

```
U64 wPawnsAble2Push(U64 wpawns, U64 empty) {
   return soutOne(empty) & wpawns;
}

U64 wPawnsAble2DblPush(U64 wpawns, U64 empty) {
   const U64 rank4 = C64(0x00000000FF000000);
   U64 emptyRank3 = soutOne(empty & rank4) & empty;
   return wPawnsAble2Push(wpawns, emptyRank3);
}
```

and similar for black.

# Generalized Push

One may rely on the [generalized shift](/General_Setwise_Operations#GeneralizedShift "General Setwise Operations") for one [color](/Color "Color") parametrized pawn push routine. Since pawns don't occur on the first or eighth rank, one may either safe the wrap-ands ...

```
enum { white, black };

U64 singlePushTargets(U64 pawns, U64 empty, int color) {
    return rotateLeft( pawns, 8 - (color << 4) ) & empty;;
}
```

... or make the "white" north-shift unconditionally but to conditionally shift back south two ranks by color\*16:

```
U64 singlePushTargets(U64 pawns, U64 empty, int color) {
    return ( (pawns << 8) >> (color << 4) ) & empty;
}
```

# Forum Posts

- [How to Shift Left (by) a Negative Number??](http://www.talkchess.com/forum/viewtopic.php?t=47710) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), April 05, 2013

# References

1. [↑](#cite_ref-1) [Animal Cognition - "Theory Of Mind" and "Chimp Chess"](http://alchessmist.blogspot.com/2008/12/animal-cognition-theory-of-mind-and.html) from [ALCHEssMIST](http://alchessmist.blogspot.com/)
2. [↑](#cite_ref-2) [Chimpanzee - Worth1000 Contests](http://www.worth1000.com/entries/396884/) by [minouz](http://www.worth1000.com/artists/minouz)

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**