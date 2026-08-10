# Blockers and Beyond

Source: https://www.chessprogramming.org/Blockers_and_Beyond

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Blockers and Beyond**

**Blockers and Beyond**,  
a general bitboard technique to determine not only sliding piece attacks, but also [king](/King_Pattern#KingAttacks "King Pattern") and [knight attacks](/Knight_Pattern#KnightAttacks "Knight Pattern"). The technique was introduced by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey") within his first release of the [open source engine](/Category:Open_Source "Category:Open Source") [Senpai 1.0](/Senpai "Senpai") in March 2014 [[1]](#cite_note-1) [[2]](#cite_note-2), but already devised in the mid 2000s, and applied in Fabien's private bitboard engine [Chess-64](/Chess-64 "Chess-64") [[3]](#cite_note-3). He found it simple and elegant with the endgame in mind [[4]](#cite_note-4), and dubbed it "blocker loop", a term already coined by [Fritz Reul](/Fritz_Reul "Fritz Reul") in the context of his [non bitboard architecture](/Vector_Attacks#NewArchitecture "Vector Attacks") [[5]](#cite_note-5), thus the editor's proposal of "Blockers and Beyond" [[6]](#cite_note-6) .

# How it works

The routine gets the pre-calculated [attack-set on the otherwise empty board](/On_an_empty_Board "On an empty Board") by looking up a two-dimensional array indexed by [piece kind](/Pieces#PieceTypeCoding "Pieces") and [origin square](/Origin_Square "Origin Square"). Further, the [occupancy](/Occupancy "Occupancy") of the whole board is [intersected](/General_Setwise_Operations#Intersection "General Setwise Operations") by a piece-kind and origin square specific blocker and beyond (b&b) mask, which is always empty for none sliding pieces. For sliders, the b&b mask almost equals the attack-set, except that the redundant most outer squares with no more ray-squares behind are cleared. [Serializing](/Bitboard_Serialization "Bitboard Serialization") the intersection with clearing all bits on the [ray](/Rays "Rays") from the origin behind the potential blocker square finally determines the sliding attack set, whether it is a bishop, rook or queen.

Of course, if there are multiple pieces on a ray, the routine performs multiple ray-resets with different lengths, which are redundant for the outer pieces beyond the first blocker without affecting the result. Despite the loop and branch issues, the routine has a tiny loop body, skips empty rays, has no conditional code on the (sign of) the [ray-direction](/Rays#RayDirections "Rays"), and is quite competitive, specially in rook, bishop and queen endings with high mobility.

# Sample C Source

[[7]](#cite_note-7)

```
U64 arrPieceAttacks[6][64];
U64 arrBlockersAndBeyond[6][64];
U64 arrBehind[64][64];

U64 pieceAttacks(int pc, int f, U64 occupied) {
   assert(pc != piece::PAWN);

   U64 ts = arrPieceAttacks[pc][f];
   for (U64 b = occupied & arrBlockersAndBeyond[pc][f]; b != 0; b &= (b - 1)) {
      int sq = bitScanForward(b);
      ts &= ~arrBehind[f][sq];
   }
   return ts;
}
```

For a queen on d4, with up to 27 attacked squares, the blockers and beyond cardinality of all eight rays is 19:

```
 pieceAttacks[q][d4]   blockers&beyond[q][d4]
 . . . 1 . . . 1       . . . . . . . .
 1 . . 1 . . 1 .       . . . 1 . . 1 .
 . 1 . 1 . 1 . .       . 1 . 1 . 1 . .
 . . 1 1 1 . . .       . . 1 1 1 . . .
 1 1 1 Q 1 1 1 1       . 1 1 Q 1 1 1 .
 . . 1 1 1 . . .       . . 1 1 1 . . .
 . 1 . 1 . 1 . .       . 1 . 1 . 1 . .
 1 . . 1 . . 1 .       . . . . . . . .
```

# See also

- [Chess-64](/Chess-64 "Chess-64")
- [Classical Approach](/Classical_Approach "Classical Approach")
- [Senpai](/Senpai "Senpai")

# Forum Posts

- [Re: Senpai 1.0 (new engine)](http://www.talkchess.com/forum/viewtopic.php?t=51637&start=26) by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), [CCC](/CCC "CCC"), March 17, 2014
- [Small improve for Blockers and Beyond Bitboard](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67693) by [Tamás Kuzmics](/Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](/CCC "CCC"), June 10, 2018

# External Links

- [Blocker from Wikipedia](https://en.wikipedia.org/wiki/Blocker)
- [Alpha blocker from Wikipedia](https://en.wikipedia.org/wiki/Alpha_blocker)
- [Beta blocker from Wikipedia](https://en.wikipedia.org/wiki/Beta_blocker)
- [Beyond from Wikipedia](https://en.wikipedia.org/wiki/Beyond)
- [Mahavishnu Orchestra](/Category:Mahavishnu_Orchestra "Category:Mahavishnu Orchestra") - [Miles Beyond](https://en.wikipedia.org/wiki/Birds_of_Fire), [Music Inn](http://www.musicinn.org/), [Lenox, Ma](https://en.wikipedia.org/wiki/Lenox,_Massachusetts) - July 21, 1973, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [John McLaughlin](/Category:John_McLaughlin "Category:John McLaughlin"), [Billy Cobham](/Category:Billy_Cobham "Category:Billy Cobham"), [Rick Laird](/Category:Rick_Laird "Category:Rick Laird"), [Jan Hammer](/Category:Jan_Hammer "Category:Jan Hammer"), [Jerry Goodman](https://en.wikipedia.org/wiki/Jerry_Goodman)

# References

1. [↑](#cite_ref-1) [Senpai 1.0 (new engine)](http://www.talkchess.com/forum/viewtopic.php?t=51637) by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), [CCC](/CCC "CCC"), March 17, 2014
2. [↑](#cite_ref-2) [Senpai Chess Engine - Computer Chess Programming](http://www.chessprogramming.net/senpai/) hosted by [Steve Maughan](/Steve_Maughan "Steve Maughan")
3. [↑](#cite_ref-3) Personal communication with [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), March 20, 2014
4. [↑](#cite_ref-4) [Re: Senpai 1.0 (new engine)](http://www.talkchess.com/forum/viewtopic.php?t=51637&start=26) by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), [CCC](/CCC "CCC"), March 17, 2014
5. [↑](#cite_ref-5) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, *Chapter 2 Non-Bitboard Architectures*.
6. [↑](#cite_ref-6) [Re: Senpai 1.0 (new engine)](http://www.talkchess.com/forum/viewtopic.php?t=51637&start=39) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), March 17, 2014
7. [↑](#cite_ref-7) adapted to common CPW types and style from Senpai 1.0 source
   bit\_t piece\_attacks\_from(int pc, int f, const board::Board & bd), senpai\_10.cpp, line 1867

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**