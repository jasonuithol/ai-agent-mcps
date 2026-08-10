# Obstruction Difference

Source: https://www.chessprogramming.org/Obstruction_Difference

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Obstruction Difference**

[![](/images/thumb/3/3e/ManRayObstruction.jpg/300px-ManRayObstruction.jpg)](http://www.imj.org.il/en/collections/194569?itemNum=194569)

[Man Ray](/Category:Man_Ray "Category:Man Ray") - Obstruction, 1947 [[1]](#cite_note-1)

**Obstruction Difference**,  
a subtraction approach to determine sliding piece attacks with bitboards, proposed by [Michael Hoffmann](/Michael_Hoffmann "Michael Hoffmann") [[2]](#cite_note-2). The idea is to get disjoint [positive](/On_an_empty_Board#PositiveRays "On an empty Board") and [negative ray masks](/On_an_empty_Board#NegativeRays "On an empty Board") of the [occupancy](/Occupancy "Occupancy"), and to subtract the [most significant one bit](/General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations") of the negative ray from the doubled [least significant one bit](/General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") (LS1B) of the positive ray. The difference is finally intersected with the linemask, excluding the [sliding piece](/Sliding_Pieces "Sliding Pieces") itself from the attack set. However, in 2022, [Daniel Infuehr](/index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)") found a faster solution to calculate the obstruction difference: subtract the most significant one bit of the negative ray from the the positive ray obstruction, followed by the [symmetric difference](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations") to flip all positive ray obstruction bits for the proper result [[3]](#cite_note-3).

# Empty Sets

If there is no obstruction inside the positive ray, we simply subtract from zero, aka borrow from the hidden 2^64 bit, same if doubling results in an empty set. If there is no obstruction inside the negative ray, we need at least to subtract one. With neither blocker available, the difference is the universal set -1 (~0), and we end up with the linemask, excluding the sliding piece, which are all [attacks on the otherwise empty board](/On_an_empty_Board "On an empty Board"). Therefor, to subtract at least '1', oring '1' is required if the negative ray occupancy is empty. Since setting the least significant bit does not affect any MS1B extraction, it can be done unconditionally on the negative ray.

# Isolation

While [isolation of the LS1B](/General_Setwise_Operations#LS1BIsolation "General Setwise Operations") is the intersection of a bitboard with its [two's complement](/General_Setwise_Operations#TheTwosComplement "General Setwise Operations"), the [MS1B](/General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations") is not that simple to extract, and requires a fast 64-bit [BitScanReverse](/BitScan#Bitscanreverse "BitScan"), f.i. [x86-64](/X86-64 "X86-64") [bsr](/X86-64#gpinstructions "X86-64") with throughput in the [one cycle range](/BitScan#x86Timing "BitScan"), as with [Intel's](/Intel "Intel") [Core 2](https://en.wikipedia.org/wiki/Intel_Core_2) or [Nehalem architecture](https://en.wikipedia.org/wiki/Nehalem_%28microarchitecture%29), or [Leading Zero Count](/BitScan#LeadingZeroCount "BitScan"), f.i. [x86-64](/X86-64 "X86-64") [lzcnt](/X86-64#gpinstructions "X86-64") on [AMD](/AMD "AMD") [K10](https://en.wikipedia.org/wiki/AMD_K10) or [Intel](/Intel "Intel") Nehalem CPUs.

# C Code

The routine works for all lines, [ranks](/Ranks "Ranks"), [files](/Files "Files"), [diagonals](/Diagonals "Diagonals") and [anti-diagonals](/Anti-Diagonals "Anti-Diagonals") by applying appropriate line-masks, and could therefor used as a generalized routine with a line-direction parameter, or in [C](/C "C") even passing a pointer to a structure with three (or multiples for several lines in parallel) bitboards per square and line, upper- and lower rays and the union of both.

|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](/Square_Mapping_Considerations "Square Mapping Considerations") | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*. |

```
/*
 * @author Michael Hoffmann, Daniel Infuehr
 * @param  U64 occ occupancy of the board
 * @param  SMasks* a mask structure by square and line
 * @return line attacks from that square
 */
U64 lineAttacks(U64 occ, const SMasks *pMask) {
   U64 lower, upper, ms1B, odiff;
   lower = pMask->lower & occ;
   upper = pMask->upper & occ;
   ms1B = C64(0x8000000000000000) >> lzcnt(lower | 1); // ms1b of lower (at least bit zero)
   // ls1b  = upper & -upper;
   // odiff = 2 * ls1b - ms1B; 
   odiff = upper ^ (upper - ms1B); // Daniel Infuehr's improvement
   return pMask->lineEx & odiff; // (pMask->lower | pMask->upper) & odiff;
}
```

To use it that way:

```
struct SMasks
{
   U64 lower;
   U64 upper;
   U64 lineEx; // lower | upper
} masks[64][4]; // 6 (4) KByte, needs initialization

U64 rookAttacks(U64 occ, enumSquare sq) {
   return lineAttacks(occ, masks[sq] + 0) | lineAttacks(occ, masks[sq] + 1);
}
U64 bishopAttacks(U64 occ, enumSquare sq) {
   return lineAttacks(occ, masks[sq] + 2) | lineAttacks(occ, masks[sq] + 3);
}
```

The routine looks competitive for CPUs with fast [lzcnt](/X86-64#gpinstructions "X86-64") but has problems on processors with slow bitScan or 32-bit processors. Register usage is moderate and should suffice all x88-64 scratch registers for two lines.

# Java

[Java](/Java "Java") programmers may rely on [Long.numberOfLeadingZeros](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html#numberOfLeadingZeros%28long%29), where the 64-bit [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine) may use appropriate machine instructions.

```
/*
 * @author Michael Hoffmann, Daniel Infuehr
 * @param  long occ occupancy of the board
 * @param  int sq  0..63
 * @param  int line  0..3 for rank, file, dia, antidia
 * @return line attacks from that square
 */
long lineAttacks(long occ, int sq, int line) {
   long lower = longMasks[sq][line][0] & occ;
   long upper = longMasks[sq][line][1] & occ;
   long mMs1b = 0x8000000000000000 >>> Long.numberOfLeadingZeros (lower | 1);
   long odiff = upper ^ (upper - mMs1b);
   return longMasks[sq][line][2] & odiff;
}
```

# See also

- [SBAMG](/SBAMG "SBAMG")

# Forum Posts

- [DIRECT BITBOARD MOVEGENERATION](http://www.talkchess.com/forum/viewtopic.php?t=29087) by [Michael Hoffmann](/Michael_Hoffmann "Michael Hoffmann"), [CCC](/CCC "CCC"), July 23, 2009
- [Re: Sliding Piece Algorithm by Abstract Syntax Tree Sifting [RELEASE]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79701&start=2) by [Daniel Infuehr](/index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](/CCC "CCC"), April 17, 2022
- [Re: Comparison of all known Sliding lookup algorithms [CUDA]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79078&start=56) by [Daniel Infuehr](/index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](/CCC "CCC"), April 24, 2022

# References

1. [↑](#cite_ref-1) [Man Ray - Obstruction, 1947](http://www.imj.org.il/en/collections/194569?itemNum=194569), [The Israel Museum](https://en.wikipedia.org/wiki/Israel_Museum)
2. [↑](#cite_ref-2) [DIRECT BITBOARD MOVEGENERATION](http://www.talkchess.com/forum/viewtopic.php?t=29087) by [Michael Hoffmann](/Michael_Hoffmann "Michael Hoffmann"), [CCC](/CCC "CCC"), July 23, 2009
3. [↑](#cite_ref-3) [Re: Sliding Piece Algorithm by Abstract Syntax Tree Sifting [RELEASE]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79701&start=2) by [Daniel Infuehr](/index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](/CCC "CCC"), April 17, 2022

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**