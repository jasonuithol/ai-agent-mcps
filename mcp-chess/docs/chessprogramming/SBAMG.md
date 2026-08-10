# SBAMG

Source: https://www.chessprogramming.org/SBAMG

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* SBAMG**

**SBAMG**, (Subtraction based Attack Mask Generation)  
a subtraction based approach proposed by [Syed Fahad](/Syed_Fahad "Syed Fahad") [[1]](#cite_note-1) which combines techniques used in [Subtracting a Rook from a Blocking Piece](/Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece") aka o^(o-2r) and [Obstruction Difference](/Obstruction_Difference "Obstruction Difference"). The idea is to subtract three times the closest blocker in [negative ray](/On_an_empty_Board#NegativeRays "On an empty Board") [direction](/Direction "Direction") ([most significant one bit](/General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations") of lower ray [occupancy](/Occupancy "Occupancy")) from the line [occupancy](/Occupancy "Occupancy"), to [exclusive or](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations") that difference with the line occupancy again: **o^(o-3cbn)**. Three times is necessary, since we need not only to subtract the next highest neigbouring square of the closest blocker for the borrow propagation, but the blocker square itself. The line occupancy excludes the sliding piece itself, and equivalently the final result is again restricted by the line-mask excluding the square of the attacker. Outer squares of the line occupancy, which don't affect resulting line attacks, are always set to avoid conditional code.

# Sample

A two [nibble](/Nibble "Nibble") sample calculating the [rank](/Ranks "Ranks") aka [byte](/Byte "Byte") attacks of a rook illustrates the technique:

```
                   binary     hex  dez
bit-index          7654 3210  
blockers and rook  .b.. r.bb
occ (without rook) 0100 0011  0x43  67
cbn                0000 0010  0x02   2 
occ-3cbn           0011 1101  0x3d  61
occ^(occ-3cbn)     0111 1110  0x7e 126
attacks (/rook)    0111 0110  0x76 118
```

# C Code

The routine works for all lines, [ranks](/Ranks "Ranks"), [files](/Files "Files"), [diagonals](/Diagonals "Diagonals") and [anti-diagonals](/Anti-Diagonals "Anti-Diagonals") by applying appropriate line-masks, and could therefor used as a generalized routine with a line-direction parameter. Signature and [BitScanReverse](/BitScan#Bitscanreverse "BitScan") (bsr64) similar to [Obstruction Difference](/Obstruction_Difference "Obstruction Difference").

|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](/Square_Mapping_Considerations "Square Mapping Considerations") | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*. |

```
/*
 * @author Syed Fahad, Gerd Isenberg
 * @param  U64 occ occupancy of the board
 * @param  SMasks* a mask structure by square and line
 * @return line attacks from that square
 */
U64 lineAttacks(U64 occ, const SMasks *pMask) {
   occ &= pMask->lineEx;
   occ |= pMask->outer;
   int bsq = bsr64(occ & pMask->lower);
   U64 cbnx3 = C64(3) << bsq; // or lookup
   occ = occ ^ (occ - cbnx3);
   return occ & pMask->lineEx;
}
```

To use it that way:

```
struct SMasks
{
   U64 lower;  // 1 for sq 0, otherwise (1 << sq) - 1
   U64 lineEx; // excluding (1 << sq)
   U64 outer;  // outer & 1 must be 1 to avoid calling bsr(0)
} masks[64][4]; // needs initialization

U64 rookAttacks(U64 occ, enumSquare sq) {
   return lineAttacks(occ, masks[sq] + 0) | lineAttacks(occ, masks[sq] + 1);
}
U64 bishopAttacks(U64 occ, enumSquare sq) {
   return lineAttacks(occ, masks[sq] + 2) | lineAttacks(occ, masks[sq] + 3);
}
```

# See also

- [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence")
- [Obstruction Difference](/Obstruction_Difference "Obstruction Difference")
- [Subtracting a Rook from a Blocking Piece](/Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece")

# Forum Posts

- [Slider attack mask generation without table lookup](http://www.talkchess.com/forum/viewtopic.php?t=56468) by [Syed Fahad](/Syed_Fahad "Syed Fahad"), [CCC](/CCC "CCC"), May 24, 2015
- [SBAMG - Competing Hyperbola Quintessence](http://www.talkchess.com/forum/viewtopic.php?t=59845) by [Syed Fahad](/Syed_Fahad "Syed Fahad"), [CCC](/CCC "CCC"), April 10, 2016 » [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence")
- [Subtraction based Attack Mask Generation](http://www.talkchess.com/forum/viewtopic.php?t=62159) by [Syed Fahad](/Syed_Fahad "Syed Fahad"), [CCC](/CCC "CCC"), November 16, 2016

# References

1. [↑](#cite_ref-1) [SBAMG - Completing Hyperbola Quintessence](http://www.talkchess.com/forum/viewtopic.php?t=59845) by [Syed Fahad](/Syed_Fahad "Syed Fahad"), [CCC](/CCC "CCC"), April 10, 2016

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**