# Passed Pawns (Bitboards)

Source: https://www.chessprogramming.org/Passed_Pawns_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Passed Pawns**

[![](/images/6/64/Pawn%27s_Dream.jpg)](http://www.carinajorgensen.com/Chess/pawnsdream.php)

[Carina Jørgensen](/Category:Carina_J%C3%B8rgensen "Category:Carina Jørgensen") - Pawn's Dream [[1]](#cite_note-1)

A **Passed Pawn**, also called **Passer**, has no opponent pawns in front on the same or adjacent files. In Bitboards, passers may be determined square- or set-wise.

# Single Passer

Working in the *square centric* world of the board, thus using a square index of **one** particular pawn, likely from [bitboard traversal](/Bitboard_Serialization "Bitboard Serialization"), to lookup pre-calculated pattern.

For a single pawn we need to access a lookup-table to get all squares on the same file and adjacent file in front of the pawn. This is what we call front-span and attack spans. If the intersection of those span-union with the set of opponent pawns is empty, it is a passed pawn.

```
U64 arrFrontSpans[2][64];

if ( (arrFrontSpans[white][sqOfWhitePawn] & pawnBB[black]) == 0 ) -> pawn is a passer
```

```
arrFrontSpans[white][d4]
. . 1 1 1 . . .
. . 1 1 1 . . .
. . 1 1 1 . . .
. . 1 1 1 . . .
. . . p . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
```

Pawns ready to promote don't need above condition, the appearance on the 7th (or 2nd) rank is already sufficient to be a passer:

```
if ( sqOfWhitePawn >= a7 ) -> white pawn may promote
if ( sqOfBlackPawn <= h2 ) -> black pawn may promote
```

# Passers set-wise

Working in the *bitboard centric* world to determine pawn related pattern *set-wise*.

Passers are the pawns [outside](/General_Setwise_Operations#RelativeComplement "General Setwise Operations") the union of all opponent [frontspans](/Pawn_Spans "Pawn Spans") and [attack-frontspans](/Attack_Spans "Attack Spans").

```
U64 wPassedPawns(U64 wpawns, U64 bpawns) {
   U64 allFrontSpans = bFrontSpans(bpawns);
   allFrontSpans |= eastOne(allFrontSpans)
                 |  westOne(allFrontSpans);
   return wpawns & ~allFrontSpans;
}

U64 bPassedPawns(U64 bpawns, U64 wpawns) {
   U64 allFrontSpans = wFrontSpans(wpawns);
   allFrontSpans |= eastOne(allFrontSpans)
                 |  westOne(allFrontSpans);
   return bpawns & ~allFrontSpans;
}
```

# See also

- [Candidate Passed Pawn](/Candidate_Passed_Pawn "Candidate Passed Pawn")
- [Candidates (Bitboards)](/Candidates_(Bitboards) "Candidates (Bitboards)")
- [Hidden Passed Pawn](/Hidden_Passed_Pawn "Hidden Passed Pawn")
- [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [Passed Pawn Extensions](/Passed_Pawn_Extensions "Passed Pawn Extensions")
- [Set-wise Rule of Squares](/King_Pattern#SetwiseRuleoftheSquare "King Pattern")

# External Links

- [Passed pawn from Wikipedia](https://en.wikipedia.org/wiki/Passed_pawn)

# References

1. [↑](#cite_ref-1) [Pawn's Dream](http://www.carinajorgensen.com/Chess/pawnsdream.php) 2009 by [Carina Jørgensen](/Category:Carina_J%C3%B8rgensen "Category:Carina Jørgensen")

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**