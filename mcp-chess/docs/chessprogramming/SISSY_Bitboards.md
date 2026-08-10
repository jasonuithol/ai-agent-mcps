# SISSY Bitboards

Source: https://www.chessprogramming.org/SISSY_Bitboards

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* SISSY Bitboards**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Paul_Klee%2C_Hauptweg_und_Nebenwege%2C_1929%2C_%C3%96l_auf_Leinwand%2C_83%2C7_x_67%2C5_cm%2C_Museum_Ludwig_1976.jpg/330px-Paul_Klee%2C_Hauptweg_und_Nebenwege%2C_1929%2C_%C3%96l_auf_Leinwand%2C_83%2C7_x_67%2C5_cm%2C_Museum_Ludwig_1976.jpg)](/File:Paul_Klee,_Hauptweg_und_Nebenwege,_1929,_%C3%96l_auf_Leinwand,_83,7_x_67,5_cm,_Museum_Ludwig_1976.jpg)

[Paul Klee](/Category:Paul_Klee "Category:Paul Klee") - Hauptweg und Nebenwege, 1929 [[1]](#cite_note-1)

**SISSY Bitboards** (Split Index Super Set Yielding),  
a new and interesting approach to determine sliding piece attacks devised by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), introduced and discussed in [CCC](/CCC "CCC") in February 2020 [[2]](#cite_note-2) as an improvement of his [Sherwin Bitboards](/Sherwin_Bitboards "Sherwin Bitboards").
SISSY bitboards apply the occupancy lookup [rank](/Ranks "Ranks") by rank to [intersect](/General_Setwise_Operations#Intersection "General Setwise Operations") supersets of the attack bitboards from the same square considering blocking pieces on that particular rank only.
While using eight lookups to intersect sounds expensive on the first glance, SISSY Bitboards yields up to eight [ray-directions](/Direction#RayDirections "Direction") of a queen in one run with cheap instructions and high [IPC](https://en.wikipedia.org/wiki/Instructions_per_cycle) potential, and thus may be an alternative for [magic bitboards](/Magic_Bitboards "Magic Bitboards") on architectures with slow 64-bit multiplication, in particular for the queen.

|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](/Square_Mapping_Considerations "Square Mapping Considerations") | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*. |

# Queen Attacks

The general SISSY attack getter requires a 3-dimensional 1MByte lookup table, with pre-initialized attack bitboards indexed by 3-bit rank index, 6-bit square, 8-bit rank occupancy.

```
U64 qss[8][64][256]; 

U64 queenAttacks(U64 occ, enumSquare sq) {  
  return                             
    qss[0][sq][ occ        & 255] &  
    qss[1][sq][(occ >>  8) & 255] &  
    qss[2][sq][(occ >> 16) & 255] &  
    qss[3][sq][(occ >> 24) & 255] &  
    qss[4][sq][(occ >> 32) & 255] &  
    qss[5][sq][(occ >> 40) & 255] &  
    qss[6][sq][(occ >> 48) & 255] &  
    qss[7][sq][(occ >> 56) & 255] ;  
}
```

The following sample demonstrates how to determine queen attacks. The intersection of the eight split index addressed attack bitboards yields the desired queen attack bitboard (red squares attacked by queen, blue reset due to blocker):

[![](/images/5/59/Queen%27s_Star.jpg)](http://www.carinajorgensen.com/Chess/queensstar.php)

[Carina Jørgensen](/Category:Carina_J%C3%B8rgensen "Category:Carina Jørgensen"), Queen's Star [[3]](#cite_note-3)

|  |  |  |
| --- | --- | --- |
|  | abcdefgh |  |
| 8 7 6 5 4 3 2 1 |                                                                                  ♚ ♛     ♟   ♟   ♟ ♟   ♞         ♕ ♘   ♙ ♙       ♙ ♔  ♙ | 8 7 6 5 4 3 2 1 |
|  | abcdefgh |  |

```
7k/q5p1/1p3p1p/2n5/3Q1N2/P1P5/1P1K2P1/8 w - - 
occ = 0x8041A20428054A00
```

```
    [7][d4][0x80]     [6][d4][0x41]     [5][d4][0xA2]     [4][d4][0x04]  
   . . . 1 . . . 1*  . . . 1 . . . 0   . . . 1 . . . 0   . . . 1 . . . 1
   1 . . 1 . . 1 .   1 . . 1 . . 1 .*  0 . . 1 . . 0 .   0 . . 1 . . 1 .
   . 1 . 1 . 1 . .   . 1 . 1 . 1 . .   . 1 . 1 . 1 . .*  . 0 . 1 . 1 . .
   . . 1 1 1 . . . & . . 1 1 1 . . . & . . 1 1 1 . . . & . . 1 1 1 . . .* 
   1 1 1 Q 1 1 1 1   1 1 1 Q 1 1 1 1   1 1 1 Q 1 1 1 1   1 1 1 Q 1 1 1 1
   . . 1 1 1 . . .   . . 1 1 1 . . .   . . 1 1 1 . . .   . . 1 1 1 . . .
   . 1 . 1 . 1 . .   . 1 . 1 . 1 . .   . 1 . 1 . 1 . .   . 1 . 1 . 1 . .
   1 . . 1 . . 1 .   1 . . 1 . . 1 .   1 . . 1 . . 1 .   1 . . 1 . . 1 .

    [3][d4][0x28]     [2][d4][0x05]     [1][d4][0x4a]     [0][d4][0x00] 
   . . . 1 . . . 1   . . . 1 . . . 1   . . . 1 . . . 1   . . . 1 . . . 1
   1 . . 1 . . 1 .   1 . . 1 . . 1 .   1 . . 1 . . 1 .   1 . . 1 . . 1 .
   . 1 . 1 . 1 . .   . 1 . 1 . 1 . .   . 1 . 1 . 1 . .   . 1 . 1 . 1 . .
 & . . 1 1 1 . . . & . . 1 1 1 . . . & . . 1 1 1 . . . & . . 1 1 1 . . .
   1 1 1 Q 1 1 0 0*  1 1 1 Q 1 1 1 1   1 1 1 Q 1 1 1 1   1 1 1 Q 1 1 1 1
   . . 1 1 1 . . .   . . 1 1 1 . . .*  . . 1 1 1 . . .   . . 1 1 1 . . .
   . 1 . 1 . 1 . .   . 0 . 1 . 1 . .   . 1 . 1 . 1 . .*  . 1 . 1 . 1 . .
   1 . . 1 . . 1 .   0 . . 1 . . 1 .   0 . . 0 . . 1 .   1 . . 1 . . 1 .*
  
   . . . 1 . . . 0 
   0 . . 1 . . 0 . 
   . 0 . 1 . 1 . . 
 = . . 1 1 1 . . . 
   1 1 1 Q 1 1 0 0 
   . . 1 1 1 . . . 
   . 0 . 1 . 1 . . 
   0 . . 0 . . 1 .
```

Since queens may appear on file A and H with attacks on that outer files, a reduction of the occupancy index range due to the [inner six bits](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks") is not possible for queens.
We will elaborate on reducing occupancy index range possibilities for bishops and rooks later. However, for queens, one may skip the outer ranks if combined with
a [general rank lookup](/First_Rank_Attacks#AttacksOnAllRanks "First Rank Attacks").

# Union Bitboard

Rather then using shift/and instructions to get the rank-wise occupancies, and similar to [Sherwin Bitboards](/Sherwin_Bitboards "Sherwin Bitboards"), one may use a [union](/C#Union "C") of a bitboard and a struct or array of eight [bytes](/Byte "Byte") (Portability concerning [endianness](/Endianness "Endianness") is an issue), to appear the code looking simpler.

```
typedef unsigned char U08;
struct bb8 {U08 r1; U08 r2; U08 r3; U08 r4; U08 r5; U08 r6; U08 r7; U08 r8;};
union bbu {U64 b64; bb8 b08;};

U64 qss[8][64][256]; // 1M

U64 queenAttacks(U64 occ, enumSquare sq) {
  bbu o; o.b64 = occ;
  return 
    qss[0][sq][o.b08.r1] &
    qss[1][sq][o.b08.r2] &
    qss[2][sq][o.b08.r3] &
    qss[3][sq][o.b08.r4] &
    qss[4][sq][o.b08.r5] &
    qss[5][sq][o.b08.r6] &
    qss[6][sq][o.b08.r7] &
    qss[7][sq][o.b08.r8];
}
```

Targeting [X86-64](/X86-64 "X86-64"), the generated [assembly](/Assembly "Assembly") is likely similar to the above shift/and255 code [[4]](#cite_note-4).

```
queenAttacks(unsigned long long, int):                     # @queenAttacks(unsigned long long, int)
        mov     rdx, rdi
        mov     rcx, rdi
        shr     rcx, 56
        movsxd  rsi, esi
        movzx   edi, dl
        shl     rsi, 11
        movzx   eax, dh
        mov     rax, qword ptr [rsi + 8*rax + qss+131072]
        and     rax, qword ptr [rsi + 8*rdi + qss]
        mov     rdi, rdx
        shr     rdi, 13
        and     edi, 2040
        and     rax, qword ptr [rsi + rdi + qss+262144]
        mov     rdi, rdx
        shr     rdi, 21
        and     edi, 2040
        and     rax, qword ptr [rsi + rdi + qss+393216]
        mov     rdi, rdx
        shr     rdi, 29
        and     edi, 2040
        and     rax, qword ptr [rsi + rdi + qss+524288]
        mov     rdi, rdx
        shr     rdi, 37
        and     edi, 2040
        and     rax, qword ptr [rsi + rdi + qss+655360]
        shr     rdx, 45
        and     edx, 2040
        and     rax, qword ptr [rsi + rdx + qss+786432]
        and     rax, qword ptr [rsi + 8*rcx + qss+917504]
        ret
```

# Bishop Attacks

Taking advantage of the [inner six bits](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks") optimization for SISSY bishop attacks, but still much memory and computation compared to other techniques:

```
U64 bss[6][64][64]; // 192 K

U64 bishopAttacks(U64 occ, enumSquare sq) {
  return
    bss[0][sq][(occ >>  9) & 63] &  // 2nd rank
    bss[1][sq][(occ >> 17) & 63] &  
    bss[2][sq][(occ >> 25) & 63] &  
    bss[3][sq][(occ >> 33) & 63] &  
    bss[4][sq][(occ >> 41) & 63] &  
    bss[5][sq][(occ >> 49) & 63] ;  // 7th rank
}
```

There is a more recent attempt to half the number of lookups by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak") but using much larger tables [[5]](#cite_note-5).

# Rook Attacks

If combined with the [rank lookup](/First_Rank_Attacks#AttacksOnAllRanks "First Rank Attacks") for SISSY fileAttacks only, one can dense the occupy index range to 2, considering only blockers on the same file.

```
U64 rss[6][64][2];  // 6K

U64 fileAttacks(U64 occ, enumSquare sq) { 
  occ >>= (sq & 7); // shift occupancy to A file
  return
    rss[0][sq][(occ >>  8) & 1] &  // 2nd rank
    rss[1][sq][(occ >> 16) & 1] &  
    rss[2][sq][(occ >> 24) & 1] &  
    rss[3][sq][(occ >> 32) & 1] &  
    rss[4][sq][(occ >> 40) & 1] &  
    rss[5][sq][(occ >> 48) & 1] ;  // 7th rank
}
```

One may try some more index trickery for instance considering 3 ranks each, for an upper and lower half,

```
U64 rss[2][64][8];  // 8K

U64 fileAttacks(U64 occ, enumSquare sq) { 
  occ >>= (sq & 7); // shift occupancy to A file
  return
    rss[0][sq][((occ>>22)&4) | ((occ>>15)&2) | ((occ>> 8)&1)] &  // rank 4,3,2
    rss[1][sq][((occ>>46)&4) | ((occ>>39)&2) | ((occ>>32)&1)];   // rank 7,6,5
}
```

One step further, to combine the occupancy to one six-bit index is already quite similar to [Kindergarten File Attacks](/Kindergarten_Bitboards#FileAttacks "Kindergarten Bitboards"), in particular [Zach Wegner's](/Zach_Wegner "Zach Wegner") [32-bit Version](/Kindergarten_Bitboards#32-bit_Versions "Kindergarten Bitboards") [[6]](#cite_note-6)

# Forum Posts

- [New RookAttacks() - possibly](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73063) by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), [CCC](/CCC "CCC"), February 12, 2020
- [Split Index Super Set Yielding (SISSY) Bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73083) by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), [CCC](/CCC "CCC"), February 13, 2020

:   [Re: Split Index Super Set Yielding (SISSY) Bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73083&start=46) by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), [CCC](/CCC "CCC"), February 13, 2021
:   [Re: Split Index Super Set Yielding (SISSY) Bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73083&start=55) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), February 14, 2021

# References

1. [↑](#cite_ref-1) [Paul Klee](/Category:Paul_Klee "Category:Paul Klee") - [Hauptweg und Nebenwege](https://commons.wikimedia.org/wiki/File:Paul_Klee,_Hauptweg_und_Nebenwege,_1929,_%C3%96l_auf_Leinwand,_83,7_x_67,5_cm,_Museum_Ludwig_1976.jpg), 1929, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Museum Ludwig](https://en.wikipedia.org/wiki/Museum_Ludwig)
2. [↑](#cite_ref-2) [Split Index Super Set Yielding (SISSY) Bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73083) by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), [CCC](/CCC "CCC"), February 13, 2020
3. [↑](#cite_ref-3) [Queen's Star](http://www.carinajorgensen.com/Chess/queensstar.php) 2009 by [Carina Jørgensen](/Category:Carina_J%C3%B8rgensen "Category:Carina Jørgensen")
4. [↑](#cite_ref-4) [Compiler Explorer](https://godbolt.org/) with x86-64 clang (experimental - Wlifetime), -O3
5. [↑](#cite_ref-5) [Re: Split Index Super Set Yielding (SISSY) Bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73083&start=55) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), February 14, 2021
6. [↑](#cite_ref-6) [Zach's tricky 32-bit approach](http://www.open-aurec.com/wbforum/viewtopic.php?topic_view=threads&p=26851&t=4523) by [Zach Wegner](/Zach_Wegner "Zach Wegner"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 22, 2006

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**