# Pawn Levers (Bitboards)

Source: https://www.chessprogramming.org/Pawn_Levers_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Pawn Levers**

[![](/images/thumb/f/f6/TotheRight.jpg/200px-TotheRight.jpg)](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bbf)

[Samuel Bak](/Category:Samuel_Bak "Category:Samuel Bak") - To The Right [[1]](#cite_note-1)

**Pawn Lever**,  
opposing [pawns](/Pawn "Pawn") in contact that can [capture](/Captures "Captures") each other. In chess the term lever is also used as **option** to attack an opposing pawn by a [push](/Pawn_Push "Pawn Push") or [double push](/Pawn_Push#DoublePush "Pawn Push"). In *Pawn Power in Chess* [[2]](#cite_note-2), [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") classified levers in the following way [[3]](#cite_note-3):

# Lever Classification

- **Center lever** - A lever wholly within the two center files.
- **Chain lever** - Adjacent levers in a diagonal formation, where the respective headpawns attack the base of the opposing chain, e.g., f5, g4 vs. g6, h5. Produces passed pawns.
- **Fork lever** - A lever attacking two units at once (can include a piece).
- **Inner Lever** - A lever where the capture would move toward the center.
- **Loose lever** - A lever where each side has the option of capturing or bypassing.
- **Mute chain lever** - A chain lever in which the bases of the opposing pawn chains are not attacked, e.g., a5, b4, c3 vs. a7, b6, c5. Doesn't produce passers.
- **Outer lever** - A lever where the capture would move away from the center.
- **Tight lever** - A lever including a ram, that offers only one side the option of both capture and bypass, e.g., c4, d4 vs. d5, e6.

*Working in the bitboard centric world to determine pawn related pattern set-wise*.

## East and West Levers

We define lever direction by the two horizontal [attack](/Pawn_Attacks_(Bitboards)#PawnAttacks "Pawn Attacks (Bitboards)") directions of the pawn, not where it comes from if capturing. Whites east lever implies blacks west lever and vice versa:

```
whites east lever   whites west lever
is blacks west      is blacks east
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . b . . . .     . . . b . . . .
. . w . . . . .     . . . . w . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
```

Keeping disjoint west- or east levers...

*Code is based on [Pawn Attacks (Bitboards)](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)") and [Pawn Pushes (Bitboards)](/Pawn_Pushes_(Bitboards) "Pawn Pushes (Bitboards)").*

```
U64 wEastLever(U64 wpawns, U64 bpawns) {
   return wpawns & bPawnWestAttacks(bpawns);
}

U64 wWestLever(U64 wpawns, U64 bpawns) {
   return wpawns & bPawnEastAttacks(bpawns);
}

U64 wAnyLever(U64 wpawns, U64 bpawns) {
   return wEastLever(wpawns, bpawns)
        | wWestLever(wpawns, bpawns);
}
```

... makes it easier to decide about inner or outer levers.

If it is about black levers, we can calculate them accordantly. On the other hand, if we already calculated white levers, we may simply shift them back since wraps are already considered:

```
bEastLever = wWestLever << 7;
bWestLever = wEastLever << 9
```

## Inner, Outer and Center Levers

Whites inner levers imply black outer levers and vice versa. Inner levers are usually more advantageous than outer levers.

```
whites inner lever  whites outer lever
is blacks outer     is blacks inner
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . b . . . b .     . b . . . . . b
. w . . . . . w     . . w . . . w .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
```

```
U64 wInnerLever(U64 wpawns, U64 bpawns) {
   const U64 abcFiles = C64(0x0707070707070707);
   const U64 fghFiles = C64(0xE0E0E0E0E0E0E0E0);
   return ( wEastLever(wpawns, bpawns) & abcFiles )
        | ( wWestLever(wpawns, bpawns) & fghFiles );
}

U64 wOuterLever(U64 wpawns, U64 bpawns) {
   const U64 bcdFiles = C64(0x0E0E0E0E0E0E0E0E);
   const U64 efgFiles = C64(0x7070707070707070);
   return ( wEastLever(wpawns, bpawns) & efgFiles )
        | ( wWestLever(wpawns, bpawns) & bcdFiles );
}

U64 wCenterLever(U64 wpawns, U64 bpawns) {
   const U64 dFile = C64(0x0808080808080808);
   const U64 eFile = C64(0x1010101010101010);
   return ( wEastLever(wpawns, bpawns) & dFile )
        | ( wWestLever(wpawns, bpawns) & eFile );
}
```

with similar code for black levers.

# See also

- [Defended Pawns (Bitboards)](/Defended_Pawns_(Bitboards) "Defended Pawns (Bitboards)")
- [Pawn Attacks (Bitboards)](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)")
- [Pawn Rams (Bitboards)](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)")

# External Links

- [Lever from Wikipedia](https://en.wikipedia.org/wiki/Lever)
- [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")

# References

1. [↑](#cite_ref-1) [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bbf), , [Center for Holocaust & Genocide Studies](http://chgs.elevator.umn.edu/), [University of Minnesota](/University_of_Minnesota "University of Minnesota")
2. [↑](#cite_ref-2) [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6
3. [↑](#cite_ref-3) [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**