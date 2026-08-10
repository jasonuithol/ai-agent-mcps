# Backward Pawns (Bitboards)

Source: https://www.chessprogramming.org/Backward_Pawns_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Backward Pawns**

[Kmoch's](/Hans_Kmoch "Hans Kmoch") definition of a [backward pawn](/Backward_Pawn "Backward Pawn") or Straggler: A half-free pawn on the second or third rank whose stop square lacks pawn protection but is controlled by a [sentry](/Sentry "Sentry"). The definition of a backward pawn seems a bit ambiguous. May an [isolated pawn](/Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)") also be a backward one? Or an pawn on a [closed file](/Pawns_and_Files_(Bitboards)#ClosedFiles "Pawns and Files (Bitboards)")? What about a backward [ram](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)") or [faked candidates](/Candidates_(Bitboards) "Candidates (Bitboards)") or even [levers](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)")?

# Backward

We may use a more general definition of backwardness, or better a pre-condition for backwardness, to consider certain subsets in further processing. All pawns, which [stop](/Pawn_Spans#StopandDistantStop "Pawn Spans") is not member of own [front-attackspans](/Attack_Spans "Attack Spans") but controlled by a sentry are considered **backward** here, no matter if they are member of a ram or lever or more advanced mutually backward [[1]](#cite_note-1):

```
U64 wBackward(U64 wpawns, U64 bpawns) {
   U64 stops = wpawns << 8;
   U64 wAttackSpans = wEastAttackFrontSpans(wpawns)
                    | wWestAttackFrontSpans(wpawns);
   U64 bAttacks     = bPawnEastAttacks(bpawns)
                    | bPawnWestAttacks(bpawns);
   return (stops & bAttacks & ~wAttackSpans) >> 8;
}
```

# Straggler

Stragglers are the intersection of above backward pawns with [open pawns](/Open_Pawns_(Bitboards)#OpenPawnsSetwise "Open Pawns (Bitboards)") and the second or third rank:

```
U64 wStraggler(U64 wpawns, U64 bpawns) {
   return wBackward (wpawns, bpawns)
        & wOpenPawns(wpawns, bpawns)
        & 0xffff00; // rank 2,3
}
```

In the strict sense, we still need to exclude [levers](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)"). On the other hand, levers are subject of [quiescence search](/Quiescence_Search "Quiescence Search") anyway.

# Telestop Weakness

As pointed out by [Sam Hamilton](/Sam_Hamilton "Sam Hamilton") [[2]](#cite_note-2) considering stop squares might be insufficient for pawns which may actually push, but have a permanent weakened [telestop](/Pawn_Spans#StopandDistantStop "Pawn Spans"), f.i.:

|  |
| --- |
|                                                                           ♟         ♟  ♟ ♟   ♙  ♙ ♙             ♙  ♙ |

8/5p2/6p1/p1p3P1/P1P5/7P/1P6/8 w - -
On the other hand, such a backward prospective pawn has a vital [tempo](/Tempo "Tempo"), which is often decisive in certain [pawn endings](/Pawn_Endgame "Pawn Endgame"), so one should be careful to don't make the penalty too worse. Anyway, one may either apply the above [wBackward](/Backward_Pawns_(Bitboards)#Backward "Backward Pawns (Bitboards)") algorithm with so far movable pawns shifted one rank up, or alternatively determine a *backward square area*, which is the black [attack span](/Attack_Spans "Attack Spans") of all black attacks which are outside the white [front attack spans](/Attack_Spans "Attack Spans"):

```
white pawns         black pawns
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . 1 . .
. . . . . . . .     . . . . . . 1 .
. . . . . . 1 .     1 . 1 . . . . .
1 . 1 . . . . .     . . . . . . . .
. . . . . . . 1     . . . . . . . .
. 1 . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .

~white front     &  black attacks    -> stop squares
attackspans                             dominated by black 
. . . . 1 . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . 1 . 1 .     . . . . 1 . . .
. . . . 1 1 . 1     . . . . . 1 . 1     . . . . . 1 . 1
. 1 . 1 1 1 . 1  &  . 1 . 1 . . . .     . 1 . 1 . . . .
. 1 . 1 1 1 1 1     . . . . . . . .     . . . . . . . .
1 1 1 1 1 1 1 1     . . . . . . . .     . . . . . . . .
1 1 1 1 1 1 1 1     . . . . . . . .     . . . . . . . .
stop squares
dominated by black
filled down
-> white         &  white pawns      -> backward pawns
backward area
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . . . . .     . . . . . . . .
. . . . 1 1 . 1     . . . . . . 1 .     . . . . . . . .
. 1 . 1 1 1 . 1  &  1 . 1 . . . . .     . . . . . . . .
. 1 . 1 1 1 . 1     . . . . . . . 1     . . . . . . . 1
. 1 . 1 1 1 . 1     . 1 . . . . . .     . 1 . . . . . .
. 1 . 1 1 1 . 1     . . . . . . . .     . . . . . . . .
```

# Dynamic Backwardness

## A further Pass

Another issue is that some pawns or their stop squares are statically member of their own [attack spans](/Attack_Spans "Attack Spans"), but those spans could not be realized, since their pawns are either backward or [rammed](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)") (or both). Those pawns (f.i. white pawn c4, and mutually black pawn a4 in the diagram) may determined in a second pass, only considering attack spans of movable pawns.

|  |
| --- |
|                                                                         ♟                ♟ ♙ ♟       ♟♙     ♙ ♙ |

8/8/1p6/8/p1P1p3/3pP3/1P1P4/8 w - -

## Stops with negative SEE

A more sophisticated definition of backwardness was given by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen") [[3]](#cite_note-3), even a member of a [pawn duo](/Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)") may be backward, if its stop square has a negative [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") score, also considering pieces. Here b7 is considered backward, no matter whether the other friendly pawn is on c7 or c6, since it's stop square b6 has a negative SEE in both cases.

|  |
| --- |
|                                                                                             ♟♟                 ♙                                  ♖ |

8/1pp5/8/2P5/8/8/8/1R6 w - -

# See also

- [Backward Pawn](/Backward_Pawn "Backward Pawn")
- [Open Pawns](/Open_Pawns_(Bitboards) "Open Pawns (Bitboards)")
- [Sentry](/Sentry "Sentry")
- [Attack Spans](/Attack_Spans "Attack Spans")
- [Sneaker](/Candidates_(Bitboards)#Sneaker "Candidates (Bitboards)") from [Candidates (Bitboards)](/Candidates_(Bitboards) "Candidates (Bitboards)")
- [Hidden Passed Pawn](/Hidden_Passed_Pawn "Hidden Passed Pawn")
- [Faker](/Faker "Faker")
- [Hans Kmoch](/Hans_Kmoch "Hans Kmoch")

# Publications

- [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6

# Forum Posts

## 1999

- [Detecting backward pawns](https://www.stmintz.com/ccc/index.php?id=56328) by [James Robertson](/James_Robertson "James Robertson"), [CCC](/CCC "CCC"), June 17, 1999

:   [Re: Detecting backward pawns](https://www.stmintz.com/ccc/index.php?id=56431) by [Edward Screven](/index.php?title=Edward_Screven&action=edit&redlink=1 "Edward Screven (page does not exist)"), [CCC](/CCC "CCC"), June 17, 1999

## 2000 ...

- [WHAT is the definition of a backward pawn?](https://www.stmintz.com/ccc/index.php?id=272739) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), December 23, 2002
- [Backward Pawns](http://www.talkchess.com/forum/viewtopic.php?t=20320) by [Mark Lefler](/Mark_Lefler "Mark Lefler"), [CCC](/CCC "CCC"), March 24, 2008
- [Doubled and Backward Pawn Engine "Definitions"](http://www.talkchess.com/forum/viewtopic.php?t=29689) by [Brian Richardson](/Brian_Richardson "Brian Richardson"), [CCC](/CCC "CCC"), September 07, 2009

## 2010 ...

- [What is a backward pawn?](http://www.talkchess.com/forum/viewtopic.php?t=52300) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), May 12, 2014
- [Some questions about backward pawns](https://groups.google.com/d/msg/fishcooking/7v29HZhwDsk/DFesjUyZAAAJ) by [Stephane Nicolet](/Stephane_Nicolet "Stephane Nicolet"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), November 20, 2016 » [Stockfish](/Stockfish "Stockfish")
- [backward pawn](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71205) by [Vivien Clauzon](/Vivien_Clauzon "Vivien Clauzon"), [CCC](/CCC "CCC"), July 06, 2019

# External Links

- [Backward pawn from Wikipedia](https://en.wikipedia.org/wiki/Backward_pawn)

# References

1. [↑](#cite_ref-1) [backward pawn](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71205) by [Vivien Clauzon](/Vivien_Clauzon "Vivien Clauzon"), [CCC](/CCC "CCC"), July 06, 2019
2. [↑](#cite_ref-2) [Re: Doubled and Backward Pawn Engine "Definitions"](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=290991&t=29689) by [Sam Hamilton](/Sam_Hamilton "Sam Hamilton"), [CCC](/CCC "CCC"), September 13, 2009
3. [↑](#cite_ref-3) [Re: WHAT is the definition of a backward pawn?](https://www.stmintz.com/ccc/index.php?id=272903) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), December 24, 2002

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**