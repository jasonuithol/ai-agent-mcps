# Attack Spans

Source: https://www.chessprogramming.org/Attack_Spans

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Attack Spans**

The admittedly arbitrary definition of **front attackspans** includes the attacked squares itself, thus it is like a **fill** of [attacked squares](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)") in the appropriate direction. The **rear attackspan** is the **complement** set on the **same file**, so that the union of both spans covers the **whole file**. As always, we keep disjoint east-west sets for separate applications, despite illustrated as union with one single pawn:

*Set-wise pattern, based on attackspans are for instance [isolated pawns](/Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)"), [passers](/Passed_Pawns_(Bitboards) "Passed Pawns (Bitboards)") and [candidates](/Candidates_(Bitboards) "Candidates (Bitboards)")*.

```
white attack        white attack     attack filefill with least one
frontspan           rearspan         square attacked by white
. . 1 . 1 . . .     . . . . . . . .     . . 1 . 1 . . .
. . 1 . 1 . . .     . . . . . . . .     . . 1 . 1 . . .
. . 1 . 1 . . .     . . . . . . . .     . . 1 . 1 . . .
. . 1 . 1 . . .     . . . . . . . .     . . 1 . 1 . . .
. . . w . . . .     . . 1 w 1 . . .     . . 1 w 1 . . .
. . . . . . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. . . . . . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. . . . . . . .     . . 1 . 1 . . .     . . 1 . 1 . . .

black attack        black attack     attack filefill with least one
frontspan           rearspan         square attacked by black
. . . . . . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. . . . . . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. . . . . . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. . . . . . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. . . b . . . .     . . 1 b 1 . . .     . . 1 b 1 . . .
. . 1 . 1 . . .     . . . . . . . .     . . 1 . 1 . . .
. . 1 . 1 . . .     . . . . . . . .     . . 1 . 1 . . .
. . 1 . 1 . . .     . . . . . . . .     . . 1 . 1 . . .
```

The routines based on [one step only](/General_Setwise_Operations#OneStepOnly "General Setwise Operations"), [vertical fills](/Pawn_Fills "Pawn Fills") and [pawn spans](/Pawn_Spans "Pawn Spans") :

```
U64 wEastAttackFrontSpans (U64 wpawns) {return eastOne(wFrontSpans(wpawns));}
U64 wWestAttackFrontSpans (U64 wpawns) {return westOne(wFrontSpans(wpawns));}
U64 bEastAttackFrontSpans (U64 bpawns) {return eastOne(bFrontSpans(bpawns));}
U64 bWestAttackFrontSpans (U64 bpawns) {return westOne(bFrontSpans(bpawns));}

U64 wEastAttackRearSpans (U64 wpawns)  {return eastOne(wRearFill(wpawns));}
U64 wWestAttackRearSpans (U64 wpawns)  {return westOne(wRearFill(wpawns));}
U64 bEastAttackRearSpans (U64 bpawns)  {return eastOne(bRearFill(bpawns));}
U64 bWestAttackRearSpans (U64 bpawns)  {return westOne(bRearFill(bpawns));}
```

The filefills are independent on color

```
U64 eastAttackFileFill (U64 pawns) {return eastOne(fileFill(pawns));}
U64 westAttackFileFill (U64 pawns) {return westOne(fileFill(pawns));}
```

- If a pawn is not member of own west or east attack filefills, the pawn is [half-isolated](/Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)").
- If a pawn is not member of the union of own east and west attack filefills, the pawn is [isolated](/Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)").
- If a pawn is not member of the union of all opponent front pawn- and attack-spans, it is a [passed pawn](/Passed_Pawns_(Bitboards) "Passed Pawns (Bitboards)").

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**