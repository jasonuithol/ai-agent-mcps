# Congruent Modulo Bitboards

Source: https://www.chessprogramming.org/Congruent_Modulo_Bitboards

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Congruent Modulo Bitboards**

**Congruent Modulo Bitboards** was introduced by [Trevor Fenner](/Trevor_Fenner "Trevor Fenner") and [Mark Levene](/Mark_Levene "Mark Levene") in the [ICGA Journal, Vol. 31, No. 1](/ICGA_Journal#31_1 "ICGA Journal") in 2008 [[1]](#cite_note-1). While their [Perfect Hashing](/Hash_Table "Hash Table") approach provides great mathematical insights in [Congruent Modulo](https://en.wikipedia.org/wiki/Modulo) arithmetic, their final conclusion in comparison with [Hashing Dictionaries](/Hashing_Dictionaries "Hashing Dictionaries"), [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards") and [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") was criticized by the obvious comparison with [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards") [[2]](#cite_note-2).

# Modulo vs. Multiplication

[BitScan](/BitScan "BitScan") broaches the issue of [Perfect Hashing](/Hash_Table "Hash Table") with [Modulo](/General_Setwise_Operations#Modulo "General Setwise Operations") versus [Multiplication](/General_Setwise_Operations#Multiplication "General Setwise Operations") as well:

- [Bitscan by Modulo](/BitScan#BitscanByModulo "BitScan")
- [De Bruijn Multiplication](/BitScan#DeBruijnMultiplation "BitScan")

So does the [SWAR-Popcount](/Population_Count#SWARPopcount "Population Count"), when it is about to finally add byte-wise populations:

- [Casting out](/Population_Count#Castingout "Population Count")
- [Multiplication](/Population_Count#Multiplication "Population Count")

## Modulo

### Congruence relation

Fenner and Levene use masked lines (not necessarily excluding the sliding piece), that is bitboards with N=8 active bits with k={7,8,9} bits apart, starting with bit zero

```
AkN = {0, k, 2k, ...,(N-1)k}
```

Based on [Congruence relation](https://en.wikipedia.org/wiki/Congruence_relation)

```
b ≡ c (mod m)
```

or equivalently

```
b mod m = c mod m
```

they deduced two general perfect hashing functions. The case N <= k with

```
h1(a) = a mod (2k + 2)
```

and the case N <= k + 1

```
h2(a) = a mod (2k+1 + 1)
```

This results in modulo 514 for [diagonals](/Diagonals "Diagonals"), modulo 257 for [anti-diagonals](/Anti-Diagonals "Anti-Diagonals"), and modulo 258 for [files](/Files "Files"), to calculate the occupied index. Tables could made denser by storing indices, but that would require a second indirection. While Fenner and Levene used a [Matlab](https://en.wikipedia.org/wiki/MATLAB) 32-bit implementation to conclude their approach might be competitive, this is how it may be implemented in [C](/C "C") by looking up pre-calculated attack-bitboards:

```
U64 arrCmodDiaAttacks [514][64];  // 257 K
U64 arrCmodAntiAttacks[257][64];
U64 arrCmodFileAttacks[258][64];

U64 diagonalAttacks(U64 occ, enumSquare sq) {
   const U64 aDia = C64(0x8040201008040201);
   occ = ( (occ >> diashift[sq]) & aDia) % 514;
   return arrCmodDiaAttacks[occ][sq];
}

U64 antiDiagAttacks(U64 occ, enumSquare sq) {
   const U64 aAntiDiaShr7 = C64(0x0002040810204081);
   occ = ( (occ >> antishift[sq]) & aAntiDiaShr7 ) % 257;
   return arrCmodAntiAttacks[occ][sq];
}

U64 fileAttacks(U64 occ, enumSquare sq) {
   const U64 aFile = C64(0x0101010101010101);
   occ = ( (occ >> (sq&7)) & aFile) % 258;
   return arrCmodFileAttacks[occ][sq];
}
```

### Casting out 255

For ranks, diagonals or anti-diagonals, where the occupancy mask excludes the sliding piece, and the rank-or byte-wise sum of disjoint bits is therefor less than 255, [Casting out](/Population_Count#Castingout "Population Count") 256-1 works as well, without any shifts required, and with more space saving options for the lookup table, i. e. similar to Kindergarten Bitboards with shared multiples of first rank attacks and an trailing post-mask with the same line [[3]](#cite_note-3).

```
masked occupany  %  256-1            =  A-H    
. . . . . . . H     . . . . . . . .     . . . . . . . .
. . . . . . G .     . . . . . . . .     . . . . . . . . 
. . . . . F . .     . . . . . . . .     . . . . . . . . 
. . . . E . . .     . . . . . . . .     . . . . . . . . 
. . . . . . . .  %  . . . . . . . .  =  . . . . . . . . 
. . C . . . . .     . . . . . . . .     . . . . . . . . 
. B . . . . . .     . . . . . . . .     . . . . . . . . 
A . . . . . . .     1 1 1 1 1 1 1 1     A B C . E F G H
```

### Reciprocal Multiplication

The 64-bit modulo by a constant can be done most efficiently by [reciprocal fixed point multiplication](/General_Setwise_Operations#Modulo "General Setwise Operations"), this is how [Microsoft](/Microsoft "Microsoft") [Visual C++](https://en.wikipedia.org/wiki/Visual_C%2B%2B) 2005 compiler implements the mod constant for [x86-64](/X86-64 "X86-64") processors. One 64\*64=128 bit multiplication, one shift, one further 32-bit multiplication , one subtraction. Of course using 64-bit [division](/General_Setwise_Operations#Division "General Setwise Operations") to get the remainder burns even more cycles.

```
Code:
% 514
 mov    r11d, r10 ; masked diagonal
 mov    rax, ff00ff00ff00ff01H
 mul    r10
 shr    rdx, 9
 imul   edx, 514 ; 00000202H
 sub    r11d, edx

% 257
 mov    r11d, r10 ; masked diagonal
 mov    rax, ff00ff00ff00ff01H
 mul    r10
 shr    rdx, 8
 imul   edx, 257 ; 00000101H
 sub    r11d, edx
```

## Multiplication

A Kindergarten like approach might look like this (not considering [inner six bits](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks")):

```
U64 arrDiagonalAttacks[256][64];  // 128 K

U64 diagonalAttacks(U64 occ, enumSquare sq) {
   occ = (diagonalMask[sq] & occ) * C64(0x0101010101010101) >> 56;
   return arrDiagonalAttacks[occ][sq];
}
```

and uses one 64\*64=64-bit multiplication, with this [x86-64](/X86-64 "X86-64") assembly for calculating an eight-bit occupied index:

```
 mov    rax, 0101010101010101H
 imul   rdx, rax
 shr    rdx, 56
```

Even [Kindergarten File-Attacks](/Kindergarten_Bitboards#FileAttacks "Kindergarten Bitboards") are cheaper and faster, not to mention [Magic Bitboards](/Magic_Bitboards "Magic Bitboards"), which covers two lines of a rook or bishop in one run.

# Fenner's and Levene's conclusion

Quote from their paper, pp 11  
**3.5. Comparison with other Methods**

```
As reported in Hyatt (2007), the rotated and magic bitboard methods are of comparable performance, and Tannous (2007) claims just a small improvement of the direct lookup method over rotated bitboards. It is easy to see that, in terms of the number of computer operations, the efficiency of our method will be similar to that of direct lookup. Thus we are justified in claiming that the computational efficiency of our method is comparable to the others.
```

Their conclusion was based on following statement of [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") [[4]](#cite_note-4) **...**

```
I had reported this earlier. Magic was no faster than rotated. I switched because of two things...
```

```
1. Magic is simpler, and simpler is better as I get older.
2. Magic gives you the opportunity to update the occupied_squares and then generate moves easily.
```

```
To do this with rotated bitboards first requires that all rotated bitboards be updated in addition to the normal occupied_squares bitboard. This is faster, if you use the feature (I don't yet, but well might at times).
```

**...** and this claim of [Sam Tannous](/Sam_Tannous "Sam Tannous") [[5]](#cite_note-5):

```
The results shown indicate that directly looking up the attacking moves for sliding pieces in hash tables improves the move generation speeds from 10% to 15% depending on computer architecture. Further efficiencies can be expected in a full implementation where the overhead of maintaining rotated bitboards is eliminated. The implementation and test code is made available in an Open-Source, interactive, chess programming module called “Shatranj” (Tannous, 2006).
```

# Publications

- [Zbigniew J. Czech](http://sun.aei.polsl.pl/~zjc/), [George Havas](http://itee.uq.edu.au/~havas/), [Bohdan S. Majewski](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Majewski:Bohdan_S=.html) (**1997**). *Perfect Hashing*. Theoretical Computer Science, Vol. 182, Nos. 1-2, pp. 1-143
- [Trevor Fenner](/Trevor_Fenner "Trevor Fenner"), [Mark Levene](/Mark_Levene "Mark Levene") (**2008**). *Move Generation with Perfect Hashing Functions.* [ICGA Journal, Vol. 31, No. 1](/ICGA_Journal#31_1 "ICGA Journal"), pp. 3-12. [pdf](http://www.dcs.bbk.ac.uk/~mark/download/bitboard_sliding_icga_final.pdf)

# Forum Posts

- [Nice Math - Strange Conclusions](http://www.talkchess.com/forum/viewtopic.php?t=20913) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), April 29, 2008
- [Low memory usage attack bitboard generation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51996) by crystalclear, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), October 06, 2011

# External Links

- [Congruence relation from Wikipedia](https://en.wikipedia.org/wiki/Congruence_relation)
- [Linear congruence theorem from Wikipedia](https://en.wikipedia.org/wiki/Linear_congruence_theorem)
- [Modular arithmetic from Wikipedia](https://en.wikipedia.org/wiki/Modular_arithmetic)
- [Modulo operation from Wikipedia](https://en.wikipedia.org/wiki/Modulo_operation)

# References

1. [↑](#cite_ref-1) [Trevor Fenner](/Trevor_Fenner "Trevor Fenner"), [Mark Levene](/Mark_Levene "Mark Levene") (**2008**). *Move Generation with Perfect Hashing Functions.* [ICGA Journal, Vol. 31, No. 1](/ICGA_Journal#31_1 "ICGA Journal"), pp. 3-12. [pdf](http://www.dcs.bbk.ac.uk/~mark/download/bitboard_sliding_icga_final.pdf)
2. [↑](#cite_ref-2) [Nice Math - Strange Conclusions](http://www.talkchess.com/forum/viewtopic.php?t=20913) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), April 29, 2008
3. [↑](#cite_ref-3) [Low memory usage attack bitboard generation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51996) by crystalclear, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), October 06, 2011
4. [↑](#cite_ref-4) [Re: BitBoard Tests Magic v Non-Rotated 32 Bits v 64 Bits](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=140141&t=16002) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC") August 25, 2007
5. [↑](#cite_ref-5) [Sam Tannous](/Sam_Tannous "Sam Tannous") (**2007**). *Avoiding Rotated Bitboards with Direct Lookup*. [ICGA Journal, Vol. 30, No. 2](/ICGA_Journal#30_2 "ICGA Journal"), pp. 85-91, [pdf](http://arxiv.org/PS_cache/arxiv/pdf/0704/0704.3773v2.pdf)

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**