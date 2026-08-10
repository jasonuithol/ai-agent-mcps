# Hiding the Implementation

Source: https://www.chessprogramming.org/Hiding_the_Implementation

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Hiding the Implementation**

None rotated approaches as mentioned in

- [Classical Approach](/Classical_Approach#Wrapper "Classical Approach")
- [Rank Attacks](/First_Rank_Attacks#AttacksOnAllRanks "First Rank Attacks")
- [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence")
- [Obstruction Difference](/Obstruction_Difference "Obstruction Difference")
- [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards")
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")
- [The Switch Approach](/The_Switch_Approach "The Switch Approach")
- [SIMD Techniques](/SIMD_Techniques "SIMD Techniques")

can hide the implementation details behind a stateless interface:

```
U64 diagonalAttacks(U64 occ, enumSquare sq);
U64 antiDiagAttacks(U64 occ, enumSquare sq);
U64 fileAttacks    (U64 occ, enumSquare sq);
U64 rankAttacks    (U64 occ, enumSquare sq);

U64 rookAttacks    (U64 occ, enumSquare sq);
U64 bishopAttacks  (U64 occ, enumSquare sq);

U64 queenAttacks   (U64 occ, enumSquare sq);
```

In [C](/C "C") / [C++](/Cpp "Cpp") one may use [header files](https://en.wikipedia.org/wiki/Header_file) with exclusive, conditional compiled inlined routines, as combinations and variations of the mentioned approaches. Initialization should be implemented by conditional compile switches in various implementation files (c, cpp). Favorite should be **bishopAttack** by [magic bitboards](/Magic_Bitboards "Magic Bitboards") due to the relative small table less than 38KByte, while magic **rookattacks** takes more than 20 times the space so far.

As always with [space-time tradeoff](/Space-Time_Tradeoff "Space-Time Tradeoff") - it depends on the cache- and [memory](/Memory "Memory") using and [footprint](https://en.wikipedia.org/wiki/Memory_footprint) of a individual chess program - on a particular hardware architecture - which solution is preferable and faster. [Perft](/Perft "Perft") frameworks likely prefer larger tables but less computation. So far L1 [Cache](https://en.wikipedia.org/wiki/Cache) is a rare resource, [Translation Lookaside Buffer](https://en.wikipedia.org/wiki/Translation_Lookaside_Buffer) als well.

# External Links

- [Information hiding from Wikipedia](https://en.wikipedia.org/wiki/Information_hiding)

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**