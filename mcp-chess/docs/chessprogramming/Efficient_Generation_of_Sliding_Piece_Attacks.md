# Efficient Generation of Sliding Piece Attacks

Source: https://www.chessprogramming.org/Efficient_Generation_of_Sliding_Piece_Attacks

**[Home](/Main_Page "Main Page") \* [Conferences](/Conferences "Conferences") \* [Workshop Chess and Mathematics](/Workshop_Chess_and_Mathematics "Workshop Chess and Mathematics") \* Efficient Generation of Sliding Piece Attacks**

[File:Logo TU Dresden.svg](/index.php?title=Special:Upload&wpDestFile=Logo_TU_Dresden.svg "File:Logo TU Dresden.svg")

:   Fakultät Mathematik und Naturwissenschaften Institut für Numerische Mathematik

:   **Workshop Chess and Mathematics** [[1]](#cite_note-1)
:   [Dresden](https://en.wikipedia.org/wiki/Dresden), November 21st and 22nd, 2008

---

[Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), Hattingen

**Efficient generation of Moves and Controls of Sliding Pieces**

Sa., 16:00, TU Dresden, WIL C207  
Attack-Sets as Base for Bitboard Move-generation: Opposed to “None-sliding” pieces, Knight, King and Pawn, whose attacks are determined by its origin square only, sliding piece attacks like Rook-, Bishop- and Queen-attacks are dependend on other pieces as well, which may block the attacking ray in one particular ray-direction. In [Quiescence Search](/Quiescence_Search "Quiescence Search") the performance of generating (winning) capture moves is crucial. Opposed to classical square-centric board-representations, which require loops over squares, bitboards permit more efficient algorithms in generating sliding attacks.

---

# Bitboard Basics

Bitboards are 64-bit integers and represent a [finite set](https://en.wikipedia.org/wiki/Finite_set) of up to 64 elements - all the [squares](/Squares "Squares") of a [chessboard](/Chessboard "Chessboard") with specific boolean properties of those squares. For instance whether squares are empty or occupied, or occupied by a specific kind of piece - or which is the main topic of this talk, whether a square is controlled or attacked (defended) by a specific kind of piece, especially attacked by sliding pieces.

## Squares and Bitindex

*see main article [Square Mapping Considerations](/Square_Mapping_Considerations "Square Mapping Considerations")*

There is a [bijective](https://en.wikipedia.org/wiki/Bijection) one-to-one correspondence between bits of a bitboard and the squares of a board. There are 64! different mappings, but most commonly bits are enumerated "in order" along ranks or files (orthogonal). Some programs ([Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards")) keep redundant mappings and also enumerate consecutive bits along the diagonals or anti-diagonals.

*If not stated otherwise, we further rely on Little-Endian Rank-File Mapping.*

[![BBUniverse.jpg](/images/0/0d/BBUniverse.jpg)](/File:BBUniverse.jpg)

with following relations:

```
squareIndex {0..63} = 8*rankIndex + fileIndex;
rankIndex   {0..7}  = squareIndex div 8; // squareIndex >> 3;
fileIndex   {0..7}  = squareIndex mod 8; // squareIndex & 7;
```

Diagonals may be enumerated in various ways determined by the difference of rankIndex and fileIndex:

```
DiagonalIndex {0..15} = (rankIndex - fileIndex) & 15;
\f  0  1  2  3  4  5  6  7
r_________________________
7 | 7  6  5  4  3  2  1  0
6 | 6  5  4  3  2  1  0 15
5 | 5  4  3  2  1  0 15 14
4 | 4  3  2  1  0 15 14 13
3 | 3  2  1  0 15 14 13 12
2 | 2  1  0 15 14 13 12 11
1 | 1  0 15 14 13 12 11 10
0 | 0 15 14 13 12 11 10  9
```

Anti-Diagonals may be enumerated in various ways determined by the sum of rankIndex and fileIndex:

```
AntiDiagonalIndex {0..15} = (rankIndex + fileIndex) ^ 7; // xor
\f  0  1  2  3  4  5  6  7
r_________________________
7 | 0 15 14 13 12 11 10  9
6 | 1  0 15 14 13 12 11 10
5 | 2  1  0 15 14 13 12 11
4 | 3  2  1  0 15 14 13 12
3 | 4  3  2  1  0 15 14 13
2 | 5  4  3  2  1  0 15 14
1 | 6  5  4  3  2  1  0 15
0 | 7  6  5  4  3  2  1  0
```

## Empty and Universe

- The [empty set](https://en.wikipedia.org/wiki/Empty_set) is represented by all bits zero.
- The [universal set](https://en.wikipedia.org/wiki/Universal_set) contains all elements by setting all bits to binary one.

The numerical values and set-wise representations of those sets, and how the appear as a board:

```
empty set E = 0      universal set U   = 2^64 - 1 or ~0
 set-wise   = {}      set-wise         = {a1, b1, c1, d1, ....., e8, f8, g8, h8}
                      hexadecimal      = 0xffffffffffffffff
                      unsigned decimal = 18,446,744,073,709,551,615
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
```

## Bitboard Board-Definition

*see main article [Bitboard Board-Definition](/Bitboard_Board-Definition "Bitboard Board-Definition")*

To represent the board we typically need one bitboard for each [piece-type](/Pieces "Pieces") and [color](/Color "Color") - likely encapsulated inside a class or structure, or as an array of bitboards as part of a [position](/Chess_Position "Chess Position") object. A one-bit inside a bitboard implies the existence of a piece of this piece-type on a certain [square](/Squares "Squares") - one to one associated by the bit-position.

```
               pieces
   white                  black            occupied               empty
. . . . . . . .     1 . 1 1 . 1 1 .     1 . 1 1 . 1 1 .     . 1 . . 1 . . 1
. . . . . . . .     . . 1 . 1 1 1 1     . . 1 . 1 1 1 1     1 1 . 1 . . . .
. . . . . . . .     1 . . . . . . .     1 . . . . . . .     . 1 1 1 1 1 1 1
. . . . . . . .     . 1 . 1 1 . . .     . 1 . 1 1 . . .     1 . 1 . . 1 1 1
. . . . . . . .     . . . . . . . .     . . . . . . . .     1 1 1 1 1 1 1 1
. 1 1 . . . . .     . . . . . . . .     . 1 1 . . . . .     1 . . 1 1 1 1 1
1 1 . 1 . 1 1 1     . . . . . . . .     1 1 . 1 . 1 1 1     . . 1 . 1 . . .
1 1 1 1 1 . 1 .     . . . . . . . .     1 1 1 1 1 . 1 .     . . . . . 1 . 1
```

:   :   |  |
        | --- |
        |                                                                                    ♜ ♝♛ ♜♚    ♟ ♝♟♟♟ ♟         ♟ ♞♟              ♗♙      ♙♙ ♙ ♙♙♙ ♖♘♗♕♖ ♔ |

```
               pawns                                  knights
   white                  black            white                  black
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . 1 . . 1 1 1     . . . . . . . .     . . . . . . . .
. . . . . . . .     1 . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . 1 . . 1 . . .     . . . . . . . .     . . . 1 . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . 1 . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
1 1 . 1 . 1 1 1     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . 1 . . . . . .     . . . . . . . .
              bishops                                  rooks
   white                   black           white                  black
. . . . . . . .     . . 1 . . . . .     . . . . . . . .     1 . . . . 1 . .
. . . . . . . .     . . . . 1 . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. 1 . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . 1 . . . . .     . . . . . . . .     1 . . . 1 . . .     . . . . . . . .
               queens                                  kings
   white                   black           white                  black
. . . . . . . .     . . . 1 . . . .     . . . . . . . .     . . . . . . 1 .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . 1 . . . .     . . . . . . . .     . . . . . . 1 .     . . . . . . . .
```

## Setwise Operations

*see main article [General Setwise Operations](/General_Setwise_Operations "General Setwise Operations")*

[Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra) is an algebraic structure that captures essential properties of both set operations and logic operations. Specifically, it deals with the set operations of **intersection**, **union**, **complement** - and the bitwise boolean operations of **AND, OR, NOT**. Bitwise boolean operations on 64-bit words are in fact 64 parallel operations on each bit.

Assume we have an attack set of a [queen](/Queen "Queen"), and like to know whether the queen attacks opponent [pieces](/Pieces "Pieces") it may [capture](/Captures "Captures"), we need to 'and' the queen-attacks with the set of opponent pieces.

```
queen attacks    &  opponent pieces  =  attacked pieces
. . . . . . . .     1 . . 1 1 . . 1     . . . . . . . .
. . . 1 . . 1 .     1 . 1 1 1 1 1 .     . . . 1 . . 1 .
. 1 . 1 . 1 . .     . 1 . . . . . 1     . 1 . . . . . .
. . 1 1 1 . . .     . . . . . . . .     . . . . . . . .
1 1 1 * 1 1 1 .  &  . . . * . . 1 .  =  . . . * . . 1 .
. . 1 1 1 . . .     . . . . . . . .     . . . . . . . .
. . . 1 . 1 . .     . . . . . . . .     . . . . . . . .
. . . 1 . . . .     . . . . . . . .     . . . . . . . .
```

## Shifts

Shift acts like a multiplication (shift left) or division (shift right) by a power of two.
With orthogonal square mapping, shift with appropriate ray directions amounts of {1,7,8,9} are used to "move" the pieces one step in that direction, or to generate their square controls set-wise.

In the 8\*8 board centric world with one scalar square-coordinate 0..63, each of the max eight neighboring squares can be determined by adding an offset for each direction. For border squares one has to care about overflows and wraps from a-file to h-file or vice versa. Some conditional code is needed to avoid that. Such code is usually part of move generation for particular pieces.

The mentioned square mapping implies following eight ray-directions as a compass-rose:

```
  northwest    north   northeast
  noWe         nort         noEa
          +7    +8    +9
              \  |  /
  west    -1 <-  0 -> +1    east
              /  |  \
          -9    -8    -7
  soWe         sout         soEa
  southwest    south   southeast
```

In the set-wise world of bitboards, where a square as member of a set is determined by an appropriate one-bit 2^square, the operation to apply such movements is shifting.

One has to consider wraps, which requires one further intersection.

*To be aware of their scalar 64-bit origin, we use so far a type defined unsigned integer U64 in our [C](/C "C") or [C++](/Cpp "Cpp") source snippets, the scalar 64-bit long in [Java](/Java "Java"). Feel free to define a distinct type or wrap U64 into classes for better abstraction and type-safety during compile time. The macro C64 will append a suffix to 64-bit constants as required by some compilers*:

```
typedef unsigned __int64 U64;    // for the old microsoft compilers
typedef unsigned long long  U64; // supported by MSC 13.00+ and C99
#define C64(constantU64) constantU64##ULL
```

### One Step Only

The advantage with bitboards is, that the shift applies to all set bits in parallel, e.g. with all pawns. Vertical shifts by +-8 don't need any under- or overflow conditions since bits simply fall out and disappear.

```
U64 soutOne (U64 b) {return  b >> 8;}
U64 nortOne (U64 b) {return  b << 8;}
```

Wraps from a-file to h-file or vice versa may be considered by only shifting subsets which may not wrap. Thus we can mask off the a- or h-file before or after a +-1,7,9 shift:

```
const U64 notAFile = 0xfefefefefefefefe; // ~0x0101010101010101
const U64 notHFile = 0x7f7f7f7f7f7f7f7f; // ~0x8080808080808080
```

Post-shift masks, ...

```
U64 eastOne (U64 b) {return (b << 1) & notAFile;}
U64 noEaOne (U64 b) {return (b << 9) & notAFile;}
U64 soEaOne (U64 b) {return (b >> 7) & notAFile;}
U64 westOne (U64 b) {return (b >> 1) & notHFile;}
U64 soWeOne (U64 b) {return (b >> 9) & notHFile;}
U64 noWeOne (U64 b) {return (b << 7) & notHFile;}
```

### Pawn Attacks

*see main article [Pawn Attacks (Bitboards)](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)")*

Pawn Attacks set-wise as application of One Step Only.

```
 white pawns       white pawns << 9  &       notAFile     ==      noEaOne
. . . . . . . .     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . .
. . . . . . . .     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . .
. . . . . . . .     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . .
. . . . . . . .     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . .
. . . . . . . .     h . . c . . . .      . 1 1 1 1 1 1 1      . . . c . . . .
. . c . . . . .     . a b . d . f g      . 1 1 1 1 1 1 1      . a b . d . f g
a b . d . f g h     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . .
. . . . . . . .     / . . . . . . .      . 1 1 1 1 1 1 1      / . . . . . . .

 white pawns       white pawns << 7  &       notHFile     ==     noWeOne
. . . . . . . .     . . . . . . . .      1 1 1 1 1 1 1 .      . . . . . . . .
. . . . . . . .     . . . . . . . .      1 1 1 1 1 1 1 .      . . . . . . . .
. . . . . . . .     . . . . . . . .      1 1 1 1 1 1 1 .      . . . . . . . .
. . . . . . . .     . . . . . . . .      1 1 1 1 1 1 1 .      . . . . . . . .
. . . . . . . .     . c . . . . . .      1 1 1 1 1 1 1 .      . c . . . . . .
. . c . . . . .     b . d . f g h .      1 1 1 1 1 1 1 .      b . d . f g h .
a b . d . f g h     . . . . . . . a      1 1 1 1 1 1 1 .      . . . . . . . .
. . . . . . . .     . . . . . . . \      1 1 1 1 1 1 1 .      . . . . . . . \

 white pawns                                                 Union (1 == double attacks)
. . . . . . . .                                               . . . . . . . .
. . . . . . . .                                               . . . . . . . .
. . . . . . . .                                               . . . . . . . .
. . . . . . . .                                               . . . . . . . .
. . . . . . . .                                               . c . c . . . .
. . c . . . . .                                               b a 1 . 1 g 1 g
a b . d . f g h                                               . . . . . . . .
. . . . . . . .                                               . . . . . . . .
```

## Bit-Twiddling relying on the Two's Complement

### LS-Bit-Isolation

Intersection with its Two's Complement isolates the least significant one bit:

```
With some arbitrary sample set:
      x          &        -x         =     LS1B_of_x
. . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .
. . 1 . 1 . . .     1 1 . 1 . 1 1 1     . . . . . . . .
. 1 . . . 1 . .     1 . 1 1 1 . 1 1     . . . . . . . .
. . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .
. 1 . . . 1 . .  &  1 . 1 1 1 . 1 1  =  . . . . . . . .
. . 1 . 1 . . .     . . 1 1 . 1 1 1     . . 1 . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
```

### LS-Bit-Reset

Intersection with its Ones' Decrement resets the least significant one bit:

```
      x          &      (x-1)        =  x_with_reset_LS1B
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . 1 . 1 . . .     . . 1 . 1 . . .     . . 1 . 1 . . .
. 1 . . . 1 . .     . 1 . . . 1 . .     . 1 . . . 1 . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. 1 . . . 1 . .  &  . 1 . . . 1 . .  =  . 1 . . . 1 . .
. . 1 . 1 . . .     1 1 . . 1 . . .     . . . . 1 . . .
. . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .
. . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .
```

... since two's complement (-x) and ones' decrement (x-1) are complement sets.

## Converting Bitboards to Lists

*see main article [Bitboard Serialization](/Bitboard_Serialization "Bitboard Serialization") and [Traversing Subsets of a Set](/Traversing_Subsets_of_a_Set "Traversing Subsets of a Set")*

At some point bitboards require serialization - for instance if we need to process move-target sets to generate moves. Thanks to the Two's Complement, isolation and reset is cheap. To determine the bit- or square-index in the 0..63 range is tad more work ...

```
while ( x ) {
   *list++  = log2OfPowerOfTwo (x & -x); // determine bit index, also referred as BitScan
   x &= x-1; // reset LS1B
}
```

or alternatively

```
while ( x ) {
   *list++  = bitScanForward(x); // determine bit index of least significant one bit
   x &= x-1; // reset LS1B
}
```

## BitScan

*see main article [BitScan](/BitScan "BitScan")*

Despite recent processors have hardware instruction for bitScan, two hashing methods are mentioned to determine the base two logarithm of a single populated Bitboard. One hash-index is based on multiplication and shift, while the second one is determined by modulo. As we will see, both techniques also appear in hashing of multiple bits of a line.

### De Bruijn Multiplication

The classical **De Bruijn** bitscan, as described by [Leiserson et al.](/Charles_Leiserson "Charles Leiserson") [[2]](#cite_note-2), to determine the [LS1B](/General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") index by [minimal perfect hashing](/Hash_Table#MinimalPerfectHashing "Hash Table"). So called [De Bruijn sequences](https://en.wikipedia.org/wiki/De_Bruijn_sequence) were invented by the Dutch mathematician [Nicolaas de Bruijn](/Nicolaas_de_Bruijn "Nicolaas de Bruijn"). A 64-bit De Bruijn sequence contains 64-overlapping unique 6-bit sequences, thus a ring of 64+5 bits. The five hidden "trailing" zeros are in fact common with the five leading zeros. There are 2^26 = 67108864 odd sequences with 6 leading binary zeros and 2^26 even sequences with 5 leading binary zeros, which may be calculated from the odd ones by shifting left one.

A multiplication with a power of two value (the isolated [LS1B](/General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations")) acts like a left shift by it's exponent. Thus, if we multiply a 64-bit De Bruijn sequence with the isolated [LS1B](/General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations"), we get a unique six bit sequence in the most significant bits. To obtain the bit-index we need to extract these upper six bits by shifting right the product, to lookup an array.

See also [generating your "private" De Bruijn Bitscan routine](/De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator").

```
const int index64[64] = {
   63,  0, 58,  1, 59, 47, 53,  2,
   60, 39, 48, 27, 54, 33, 42,  3,
   61, 51, 37, 40, 49, 18, 28, 20,
   55, 30, 34, 11, 43, 14, 22,  4,
   62, 57, 46, 52, 38, 26, 32, 41,
   50, 36, 17, 19, 29, 10, 13, 21,
   56, 45, 25, 31, 35, 16,  9, 12,
   44, 24, 15,  8, 23,  7,  6,  5
};

/**
* bitScanForward
* @author Charles E. Leiserson
*         Harald Prokop
*         Keith H. Randall
* "Using de Bruijn Sequences to Index a 1 in a Computer Word"
* @param bb bitboard to scan
* @precondition bb != 0
* @return index (0..63) of least significant one bit
*/
int bitScanForward(U64 bb) {
   const U64 debruijn64 = C64(0x07EDD5E59A4E28C2);
   return index64[((bb & -bb) * debruijn64) >> 58];
}
```

### Bitscan by Modulo

Another idea is to apply a modulo operation of the isolated LS1B by the prime number 67 [[3]](#cite_note-3) [[4]](#cite_note-4)[[5]](#cite_note-5). The remainder 0..66 can be used to [perfectly hash](/Hash_Table#PerfectHashing "Hash Table") the bit-index table. Three gaps are 0, 17, and 34, so the mod 67 can make a branchless trailing zero count.

```
const int lookup67[67+1] = {
   64,  0,  1, 39,  2, 15, 40, 23,
    3, 12, 16, 59, 41, 19, 24, 54,
    4, -1, 13, 10, 17, 62, 60, 28,
   42, 30, 20, 51, 25, 44, 55, 47,
    5, 32, -1, 38, 14, 22, 11, 58,
   18, 53, 63,  9, 61, 27, 29, 50,
   43, 46, 31, 37, 21, 57, 52,  8,
   26, 49, 45, 36, 56,  7, 48, 35,
    6, 34, 33, -1
};

/**
* trailingZeroCount
* @param bb bitboard to scan
* @return index (0..63) of least significant one bit, 64 if bb is zero
*/
int trailingZeroCount(U64 bb) {
   return lookup67[(bb & -bb) % 67];
}
```

Since div/mod is an expensive instruction, a modulo by constant is likely replaced by reciprocal fixed point multiplication to get the quotient and a second multiplication and difference to get the remainder. Compared with De Bruijn multiplication it is still to slow.

## Kindergarten Multiplication

*see main article [Flipping Mirroring and Rotating](/Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")*

Multiplication with **disjoint** intermediate results was nominated as Kindergarten Multiplication.

Multiplying the masked A-file with the main-diagonal, maps the file-bits to the 8th rank, similar to a flip about the anti-diagonal A8-H1. Shifting down to the 1st rank, leaves the bits like a 90-degree anti clockwise rotation.

```
masked bits                             mapped to 8th rank
bits on A-file   *  main-diagonal    =  with garbage     -> 1st rank
A . . . . . . .     . . . . . . . 1     A B C D E F G H     . . . . . . . .
B . . . . . . .     . . . . . . 1 .     B C D E F G H .     . . . . . . . .
C . . . . . . .     . . . . . 1 . .     C D E F G H . .     . . . . . . . .
D . . . . . . .     . . . . 1 . . .     D E F G H . . .  >> . . . . . . . .
E . . . . . . .  *  . . . 1 . . . .  =  E F G H . . . .  56 . . . . . . . .
F . . . . . . .     . . 1 . . . . .     F G H . . . . .     . . . . . . . .
G . . . . . . .     . 1 . . . . . .     G H . . . . . .     . . . . . . . .
H . . . . . . .     1 . . . . . . .     H . . . . . . .     A B C D E F G H
```

That is straight forward multiplication of a masked diagonal or anti-diagonal with the A-file.
To mask the garbage off, we further shift down by 7 ranks.

```
masked diagonal  *  A-file              mapped
to 8th rank      ->  1st rank
. . . . . . . H     1 . . . . . . .     A B C D E F G H     . . . . . . . .
. . . . . . G .     1 . . . . . . .     A B C D E F G .     . . . . . . . .
. . . . . F . .     1 . . . . . . .     A B C D E F . .  >> . . . . . . . .
. . . . E . . .     1 . . . . . . .     A B C D E . . .  56 . . . . . . . .
. . . D . . . .  *  1 . . . . . . .  =  A B C D . . . .     . . . . . . . .
. . C . . . . .     1 . . . . . . .     A B C . . . . .     . . . . . . . .
. B . . . . . .     1 . . . . . . .     A B . . . . . .     . . . . . . . .
A . . . . . . .     1 . . . . . . .     A . . . . . . .     A B C D E F G H
```

---

# Attack-Sets as Base for Bitboard Move-generation

Opposed to "None-sliding" pieces, Knight, King and Pawn, whose **controls** or **attacks** are determined by its origin **square** only, sliding piece attacks like Rook-, Bishop- and Queen-attacks are dependent on other pieces as well, which may **block** the attacking ray in one particular ray-direction.

In Quiescence Search the performance of generating (winning) capture moves is crucial. Opposed to classical square-centric board-representations, which require loops over squares, bitboards permit more efficient algorithms in generating sliding attacks.

## Sliding piece Attacks on the otherwise empty board

*see main article [On an empty Board](/On_an_empty_Board "On an empty Board")*

Attacks of single sliding pieces on the otherwise empty board or their disjoint subsets on lines or rays are that simple than none sliding pieces. We simply use pre-calculated tables for each piece-type, line or ray, indexed by square-index.

### Ray Attacks

The mentioned square mapping implies following eight ray-directions as a compass-rose:

```
  northwest    north   northeast
  noWe         nort         noEa
          +7    +8    +9
              \  |  /
  west    -1 <-  0 -> +1    east
              /  |  \
          -9    -8    -7
  soWe         sout         soEa
  southwest    south   southeast
```

Positive Rays:

```
East (+1)           Nort (+8)            NoEa (+9)           NoWe (+7)
. . . . . . . .     . . . 1 . . . .      . . . . . . . 1     . . . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . . . 1 .     1 . . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . . 1 . .     . 1 . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . 1 . . .     . . 1 . . . . .
. . . R 1 1 1 1     . . . R . . . .      . . . B . . . .     . . . B . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
```

Negative Rays:

```
West (-1)           Sout (-8)            SoWe (-9)           SoEa (-7)
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
1 1 1 R . . . .     . . . R . . . .      . . . B . . . .     . . . B . . . .
. . . . . . . .     . . . 1 . . . .      . . 1 . . . . .     . . . . 1 . . .
. . . . . . . .     . . . 1 . . . .      . 1 . . . . . .     . . . . . 1 . .
. . . . . . . .     . . . 1 . . . .      1 . . . . . . .     . . . . . . 1 .
```

### Line Attacks

```
Rank                File                 Diagonal            Anti-Diagonal
. . . . . . . .     . . . 1 . . . .      . . . . . . . 1     . . . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . . . 1 .     1 . . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . . 1 . .     . 1 . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . 1 . . .     . . 1 . . . . .
1 1 1 R 1 1 1 1     . . . R . . . .      . . . B . . . .     . . . B . . . .
. . . . . . . .     . . . 1 . . . .      . . 1 . . . . .     . . . . 1 . . .
. . . . . . . .     . . . 1 . . . .      . 1 . . . . . .     . . . . . 1 . .
. . . . . . . .     . . . 1 . . . .      1 . . . . . . .     . . . . . . 1 .
```

### Piece attacks

Piece attacks are the union of either orthogonal or diagonal lines. Queen attacks are the union of rook- and bishop attacks.

```
                                   Queen
                               . . . 1 . . . 1
                               1 . . 1 . . 1 .
                               . 1 . 1 . 1 . .
               Rook            . . 1 1 1 . . .         Bishop
           . . . 1 . . . .     1 1 1 Q 1 1 1 1     . . . . . . . 1
           . . . 1 . . . .     . . 1 1 1 . . .     1 . . . . . 1 .
           . . . 1 . . . .     . 1 . 1 . 1 . .     . 1 . . . 1 . .
           . . . 1 . . . .     1 . . 1 . . 1 .     . . 1 . 1 . . .
           1 1 1 R 1 1 1 1                         . . . B . . . .
           . . . 1 . . . .                         . . 1 . 1 . . .
           . . . 1 . . . .                         . 1 . . . 1 . .
           . . . 1 . . . .                         1 . . . . . 1 .
```

# Sliding Attacks by Calculation

For one single sliding piece, one may consider subtraction from the set of blockers, to determine attack sets. Zeros, that are empty squares, between the nearest blocker and the sliding pieces became "ones", the nearest blocker becomes zero. In fact all flipped bits are the attacked squares in positive ray direction.

```
 occupied  11000101
 slider    00000100 subset of occupied
 o-s       11000001 resets the slider in occupied
 o-2s      10111101 borrows the one from nearest blocker
 occupied  11000101
 o^(o-2s)  01111000 all flipped bits are the attacks in most significant bit direction
```

To restrict the operations to a certain line, rank file or diagonal, a leading intersection with the line mask is necessary, same for the final result.

## Subtraction and Reverse Subtraction of rooks from blockers

*see main article [Subtracting a Rook from a Blocking Piece](/Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece") and [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence")*

With s (sliding piece) single element set and subset of o (occupied):

```
positiveRayAttacks = o  ^ (o - 2s);
```

The first subtraction resets the siding-piece-bit in occupied.
The second subtraction borrows a one from nearest blocker (if any), and sets all intermediate zero bits (empty squares). The exclusive or gains all flipped bits, which turnes out to be the rook attacks in "positive" attacking direction.

For negative directions one needs "reverse" arithmetic (2 + 2 == 1).

```
with o' = reverse (o)
and  s' = reverse (s)
negativeRayAttacks = reverse (o' ^ (o' - 2s'));
```

Since bit-reversal or any mirroring or flipping is distributive over xor:

```
reverse(a ^ b) == reverse (a) ^ reverse(b)
```

One can reformulate negative rays

```
negativeRayAttacks = o  ^  reverse (o' - 2s');
```

which leads to a simplification in the line-attacks, since positiveRayAttacks and negativeRayAttacks are disjoint sets for one particular sliding piece and may be combined by "xor", and o ^ o == 0.

```
lineAttacks = positiveRayAttacks ^ negativeRayAttacks;
lineAttacks =         o ^ (o-2s) ^ reverse( o'-2s') ^ o
lineAttacks =             (o-2s) ^ reverse( o'-2s')
```

Diagonal or vertical line occupancies need leading and trailing intersection with line-masks. Thanks to the little-endian versus big-endian war, recent processors have appropriate instructions to swap bytes (ranks) inside a 64-bit word for the reverse arithmetic, note that masked files or diagonals have only max one bit per rank:

```
U64 diagonalAttacks(U64 occ, int sqOfSlider) {
   U64 forward, reverse, slider, lineMask;

   lineMask = diagonalMaskEx[sqOfSlider]; // excludes square of slider
   slider   = singleBitboard[sqOfSlider]; // single bit 1 << sq, 2^sq

   forward  = occ & lineMask; // also performs the first subtraction by clearing the s in o
   reverse  = byteswap( forward ); // o'-s'
   forward -=         ( slider  ); // o -2s
   reverse -= byteswap( slider  ); // o'-2s'
   forward ^= byteswap( reverse );
   return forward & lineMask;      // mask the line again
}
```

## Flood Fill Techniques with multiple sliders

Fill approaches determine attacks set-wise for multiple pieces (i.e. rooks and queen(s)) in one particular ray-direction. The flood stops on each particular ray (either 8 ranks or files, or 15 diagonals or anti-diagonals), if a square is not empty.

### Occluded Fill

*see main article [Dumb7Fill](/Dumb7Fill "Dumb7Fill")*
For sliding piece-attacks one direction step can be repeated seven times, after each shift, intersecting with empty squares accumulating all intermediate results to a union set, which results in an occluded fill set, including the sliding piece but excluding the blocker.

```
U64 eastOccluded (U64 rooks, U64 empty) {
   empty  = empty & notAFile; // make A-File all occupied, to consider H-A-wraps after shift
   rooks |= empty & (rooks << 1); // 1. fill
   rooks |= empty & (rooks << 1); // 2. fill
   rooks |= empty & (rooks << 1); // 3. fill
   rooks |= empty & (rooks << 1); // 4. fill
   rooks |= empty & (rooks << 1); // 5. fill
   rooks |= empty & (rooks << 1); // 6. fill
   rooks |= empty & (rooks << 1); // 7. fill // not necessary for further attack generation
   return rooks;
}
```

### Kogge-Stone Parallel Prefix Algorithm

*see main article [Kogge-Stone Algorithm](/Kogge-Stone_Algorithm "Kogge-Stone Algorithm") and [Parallel Prefix Algorithms](/Parallel_Prefix_Algorithms "Parallel Prefix Algorithms")*
Occluded fill might be done more efficiently parallel prefix wise by Kogge-Stone Algorithms:

```
U64 eastOccluded(U64 rooks, U64 empty) {
   empty  = empty & notAFile; // make A-File all occupied, to consider H-A-wraps after shift
   rooks |= empty & (rooks << 1);
   empty  = empty & (empty << 1);
   rooks |= empty & (rooks << 2);
   empty  = empty & (empty << 2);
   rooks |= empty & (rooks << 4);
   return rooks;
}
```

The Kogge-Stone [parallel prefix algorithm](/Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") for sliding piece attack generation was first introduced by [Steffan Westcott](/Steffan_Westcott "Steffan Westcott") in [CCC](/CCC "CCC") [[6]](#cite_note-6). It is a parallel prefix approach of a occluded [dumb7](/Dumb7Fill "Dumb7Fill") [flood-fill](https://en.wikipedia.org/wiki/Flood_fill), propagating sliding piece attacks in software like carries of a kogge-stone [hardware adder](https://en.wikipedia.org/wiki/Carry_look-ahead_adder) [[7]](#cite_note-7). We need to pass sliders as generator set and the set of empty squares as propagator set. For appropriate attacks we need to shift [one step](/General_Setwise_Operations#OneStepOnly "General Setwise Operations") further, considering wraps.

### Ray-wise Attacks in one Direction

For square attack sets, occluded fill sets need to be shifted one more step. Thus, the occluded fill needs one fill cycle less.

```
U64 eastAttacks (U64 rooks, U64 empty) {
   empty  = empty & notAFile; // make A-File all occupied, to consider H-A-wraps after shift
   rooks |= empty & (rooks << 1); // 1. fill
   rooks |= empty & (rooks << 1); // 2. fill
   rooks |= empty & (rooks << 1); // 3. fill
   rooks |= empty & (rooks << 1); // 4. fill
   rooks |= empty & (rooks << 1); // 5. fill
   rooks |= empty & (rooks << 1); // 6. fill
   return notAFile& (rooks << 1);
}
```

Because fill-approaches keep distinct ray-directions, there is still a unique source-target square relation. Fill approaches with pure calculation are Cpu-intensive, but require no memory reads. They are a domain of SIMD instruction sets like SSE2 with sixteen 128-bit registers, to process two or four distinct sets (e.g. white and black, sliders and king as queen like meta-slider) per register and several ray-directions simultaneously - e.g. three 128-bit instructions per cycle for core2duo.

Keeping distinct ray-directions has some advantages, for instance in determining pinned pieces or discovered checks. Fill-Algorithms are great to feed in line-wise attack sets of single sliders, to determine a progressive mobility on the orthogonal rays, i.e. move targets in two moves, or trajectories against important squares or areas.

```
 . . . . . . . .
 . . . . \ . . .
 . . . \ . 1 . .
 . . \ . 1 . \ .
 . \ . 1 . \ . .
 . . 1 . \ . . .
 . B . \ . . . .
 . . . . . . . .
```

---

# Lookup Techniques

Lookup Techniques are used to hash pre-calculated attack-sets of a single pieces by square-index and occupancy of the affected lines.

## Rook Attacks on the first Rank - as a base of occupancy lookup

*see main article [First Rank Attacks](/First_Rank_Attacks "First Rank Attacks")*
The first [rank](/Ranks "Ranks") is the ideal line to introduce occupancy lookups.

### One Byte Only

Assume we (temporary) reduce the chess-board to one [rank](/Ranks "Ranks"). Occupancy bitboard is one [byte](/Byte "Byte") with up to 256 states. A [rook](/Rook "Rook") attack-set from one of the eight [squares](/Squares "Squares") ([file](/Files "Files")) on this single rank is also only one byte. Thus we can construct an array of bytes[256][8], indexed by all 256 occupancies and 8 files, to lookup the pre-calculated rank-attack bytes.

|  |
| --- |
| [FirstRank.JPG](/File:FirstRank.JPG) |
| Occupancy of the first rank = 01001010B |
| [FirstRankA.JPG](/File:FirstRankA.JPG) |
| Rank-attacks ::= f (e-file, Occupancy) = 01110110B |

```
BYTE arrFirstRankAttacks256x8[256][8]; // 2048 Bytes = 2KByte

firstRankAttack = arrFirstRankAttacks256x8[rankOccupancy][squareOnRank];
```

### The Outer Squares

If we think about to the occupancy lookup, we may recognize that the outer squares don't matter. There are no more squares behind. The outer squares are either attacked or not - independent from their occupancy state. We can use the **six inner bits** only as lookup-index with two additional cheap instruction. This reduces the lookup-table by factor of **four**.

```
BYTE arrFirstRankAttacks64x8[64][8]; // 512 Bytes = 1/2KByte

firstRankAttack = arrFirstRankAttacks64x8[(rankOccupancy >> 1)& 63][squareOnRank];
```

### Other ranks

It is simple to shift other ranks to the first rank, and to shift back the attack set.

## Rotated Bitboards

*see main article [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards")*

**Rotated Bitboards** are a bitboard move generation technique invented independently by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") [[8]](#cite_note-8) and by [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") [[9]](#cite_note-9) with [Peter Gillgasch](/Peter_Gillgasch "Peter Gillgasch") from the [DarkThought](/DarkThought "DarkThought") team. This variation uses rotated copies of the occupancy in order to place bits along a [file](/Files "Files") or [diagonal](/Diagonals "Diagonals") in adjacent bits. Because of this, these bits can be easily extracted to obtain an occupancy map for a [rank](/Ranks "Ranks"), file, or diagonal. This is used, along with the square of a slider, to lookup a bitboard containing attacks in an array.

Rotated bitboards are fast to extract the occupancy index and require 32 KByte for each line direction (rank, file, diagonal and anti-diagonal) for the lookup-tables, considering the inner six bits. However, there is more work in updating four occupied bitboards while making or unmaking moves, instead of one. The fast 64-bit multiplication of recent x64 processors (~4-cycles) with a throughput of up to one cycle, makes on the fly calculations of occupied states on files and diagonals more attractive.

## Kindergarten Bitboards

*see main article [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards")*
Kindergarten Bitboards perform a fill-multiplication and uses a shared lookup table for ranks and diagonals.

### Ranks and Diagonals

Ranks and diagonals - that is their appropriate line-mask by square-index - are first intersected by the occupancy of the whole board. Doesn't matter whether the slider itself is cleared or not - it is redundant anyway, considered by the pre-calculated lookup-table. Since there is only up to one bit per file, the [north-fill multiplication](/General_Setwise_Operations#Multiplication "General Setwise Operations") by the A-file maps the diagonal to the 8th rank. Or - since we only need the inner six bits, we combine the required shift left one by multiplying with the B-file. Shifting right the product by 58 (64-6) leaves the six-bit occupancy-index in the 0..63 range.

For instance the diagonal-attacks of a bishop on d4. 'A'-'H' represent the masked occupied bits along this diagonal, which are either zero or one. We need 'B'-'G' as six bit number:

```
masked line      *  B-File           =  B-G upper six       occupancy 6 bit
. . . . . . . H     . 1 . . . . . .     . A[B C . E F G]    . . . . . . . .
. . . . . . G .     . 1 . . . . . .     . A B C . E F G     . . . . . . . .
. . . . . F . .     . 1 . . . . . .     . A B C . E F .     . . . . . . . .
. . . . E . . .     . 1 . . . . . .     . A B C . E . .  >> . . . . . . . .
. . . . . . . .  *  . 1 . . . . . .  =  . A B C . . . .  58 . . . . . . . .
. . C . . . . .     . 1 . . . . . .     . A B C . . . .     . . . . . . . .
. B . . . . . .     . 1 . . . . . .     . A B . . . . .     . . . . . . . .
A . . . . . . .     . 1 . . . . . .     . A . . . . . .    [B C . E F G]. .
```

The pre-calculated lookup-table contains the attacks of the first rank - but eight copies in each rank or byte. It is indexed by the six bit occupied-state ('B'-'G') and the file of the slider's square. It needs to be intersected with the same line-mask as formerly the occupancy - to map the first rank attack bits to the appropriate line - that's all. Appropriate pre-calculated attack bits are represented by 'a'-'h':

```
fillUpAttacks[file == 3][B C . E F G]:

8 copies of rank      the attack set
attacks & l-mask  ->  of this line
a b c . e f g h       . . . . . . . h
a b c . e f g h       . . . . . . g .
a b c . e f g h       . . . . . f . .
a b c . e f g h       . . . . e . . .
a b c . e f g h       . . . . . . . .
a b c . e f g h       . . c . . . . .
a b c . e f g h       . b . . . . . .
a b c . e f g h       a . . . . . . .
```

Code spippets.

```
U64 fillUpAttacks[8][64];  // 4 KByte pre-calculated Lookup table
const U64 bFile = C64(0x0202020202020202);

U64 diagonalAttacks(U64 occ, enumSquare sq) {
   occ = (diagonalMaskEx[sq] & occ) * bFile >> 58;
   return diagonalMaskEx[sq] & fillUpAttacks[sq&7][occ];
}

U64 antiDiagAttacks(U64 occ, enumSquare sq) {
   occ = (antidiagMaskEx[sq] & occ) * bFile >> 58;
   return antidiagMaskEx[sq] & fillUpAttacks[sq&7][occ];
}

U64 rankAttacks(U64 occ, enumSquare sq) {
   occ = (rankMaskEx[sq] & occ) * bFile >> 58;
   return rankMaskEx[sq] & fillUpAttacks[sq&7][occ];
}
```

### Files

File attacks need tad more work:

```
U64 aFileAttacks [8][64];  // 4 KByte
const U64 aFile   = C64(0x0101010101010101);
const U64 diac2h7 = C64(0x0080402010080400);

U64 fileAttacks(U64 occ, enumSquare sq) {
   occ = aFile  & (occ >> (sq&7));
   occ = (diac2h7 *  occ ) >> 58;
   return aFileAttacksx[sq>>3][occ] << (sq&7);
}
```

## Congruent Modulo Bitboards

*see main article [Congruent Modulo Bitboards](/Congruent_Modulo_Bitboards "Congruent Modulo Bitboards")*

**Congruent Modulo Bitboards** was introduced by [Trevor Fenner](/Trevor_Fenner "Trevor Fenner") and [Mark Levene](/Mark_Levene "Mark Levene") in the [ICGA Journal](/ICGA_Journal "ICGA Journal") Vol. 31, No. 1 in 2008 [[10]](#cite_note-10). While their [Perfect Hashing](/Hash_Table "Hash Table") approach provides great mathematical insights in [Congruent Modulo](https://en.wikipedia.org/wiki/Modulo) arithmetic, their final conclusion in comparison with [Hashing Dictionaries](/Hashing_Dictionaries "Hashing Dictionaries"), [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards") and [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") was criticized by the obvious comparison with [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards") [[11]](#cite_note-11).

Fenner and Levene use masked line modulo 514 for the diagonals, modulo 257 for the anti-diagonals and mod 258 for files, to calculate the occupied index, but they didn't consider the [inner six bits](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks") for a denser lookup. Of course, tables could made denser by storing indices, but that would require a second indirection. While Fenner and Levene used a [Matlab](https://en.wikipedia.org/wiki/MATLAB) 32-bit implementation to conclude their approach might be competitive, this is how it may be implemented in [C](/C "C") by looking up pre-calculated attack-bitboards:

```
U64 arrCmodDiaAttacks [514][64];  // 257 K
U64 arrCmodAntiAttacks[257][64];
U64 arrCmodFileAttacks[258][64];

U64 diagonalAttacks(U64 occ, enumSquare sq) {
   occ = (diagonalMask[sq] & occ) % 514;
   return arrCmodDiaAttacks[occ][sq];
}

U64 antiDiagAttacks(U64 occ, enumSquare sq) {
   occ = (antiDiagMask[sq] & occ) % 257;
   return arrCmodAntiAttacks[occ][sq];
}

U64 fileAttacks(U64 occ, enumSquare sq) {
   occ = (fileMask[sq] & occ) % 258;
   return arrCmodFileAttacks[occ][sq];
}
```

## Magic Bitboards

*see main article [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")*

Magic bitboards uses a multiply-right-shift [perfect hashing](/Hash_Table#PerfectHashing "Hash Table") algorithm to index a attack bitboard database - which leaves both line-attacks of a bishop or rook in one run.

The magic bitboard approach was introduced by [Lasse Hansen](/Lasse_Hansen "Lasse Hansen") in the [Winboard programming forum](/Computer_Chess_Forums "Computer Chess Forums"). He had the idea to hash the up to twelve relevant occupied bits of **both directions** of a rook- or bishop movement simultaneously [[12]](#cite_note-12).

[Pradu Kannan's](/Pradu_Kannan "Pradu Kannan") improvements to Lasse Hansen's initial approach was to introduce a [Java](/Java "Java")-like, two-dimensional array with individual size for each square and all it's relevant occupancies [[13]](#cite_note-13). Big savings in table-size - since many squares on either orthogonals or diagonals require less bits than others, especially considering the [inner six bits](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks"). While center squares are more dense for rooks, it is the opposite for bishops [[14]](#cite_note-14).

### How it works

A magic move-bitboard generation technique consists of four key steps:

1. Mask the relevant occupancy bits to form a key. For example if you had a rook on a1, the relevant occupancy bits will be from a2-a7 and b1-g1.
2. Multiply the key by a "magic number" to obtain an index mapping. This magic number can be generated by brute-force trial and error quite easily although it isn't 100% certain that the magic number is the best possible (see step 3).
3. Right shift the index mapping by 64-n bits to create an index, where n is the number of bits in the index. A better magic number will have less bits required in the index.
4. Use the index to reference a preinitialized move database.

```
any consecutive
relevant occupancy                      combination of
bishop b1, 5 bits                       the masked bits
. . . . . . . .     . . . . . . . .     . . .[C D E F G]
. . . . . . . .     . 1 . . . . . .     . . . . . . . .
. . . . . . G .     . 1 . . . . . .     . . . . . . . .
. . . . . F . .     . 1 . . . . . .     . . . . . . . .
. . . . E . . .  *  . 1 . . . . . .  =  . .garbadge . .    >> (64- 5)
. . . D . . . .     . 1 . . . . . .     . . . . . . . .
. . C . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

any consecutive
relevant occupancy                      combination of
bishop d4, 9 bits                       the masked bits
. . . . . . . .     . . . . . . . .     2 4 5 B C E F G]
. . . . . . G .     . . .some . . .     . . . . . . .[1
. 5 . . . F . .     . . . . . . . .     . . . . . . . .
. . 4 . E . . .     . . .magic. . .     . . . . . . . .
. . . . . . . .  *  . . . . . . . .  =  . .garbadge . .    >> (64- 9)
. . C . 2 . . .     . . .bits . . .     . . . . . . . .
. B . . . 1 . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

any consecutive
relevant occupancy                      combination of
rook d4, 10 bits                        the masked bits
. . . . . . . .     . . . . . . . .     4 5 6 B C E F G]
. . . 6 . . . .     . . .some . . .     . . . . . .[1 2
. . . 5 . . . .     . . . . . . . .     . . . . . . . .
. . . 4 . . . .     . . .magic. . .     . . . . . . . .
. B C . E F G .  *  . . . . . . . .  =  . .garbadge . .    >> (64-10)
. . . 2 . . . .     . . .bits . . .     . . . . . . . .
. . . 1 . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

any consecutive
relevant occupancy                      combination of
rook a1, 12 bits                        the masked bits
. . . . . . . .     . . . . . . . .     5 6 B C D E F G]
6 . . . . . . .     . . .some . . .     . . . .[1 2 3 4
5 . . . . . . .     . . . . . . . .     . . . . . . . .
4 . . . . . . .     . . .magic. . .     . . . . . . . .
3 . . . . . . .  *  . . . . . . . .  =  . .garbadge . .    >> (64-12)
2 . . . . . . .     . . .bits . . .     . . . . . . . .
1 . . . . . . .     . . . . . . . .     . . . . . . . .
. B C D E F G .     . . . . . . . .     . . . . . . . .
```

The above illustration is correct for the b1 bishop, since it has only one ray and one bit per file and works kindergarten like. In general a one to one mapping of N scattered occupied bits to N consecutive bits is not always possible due to possible overflows. A perfect mapping of N scattered bits to N consecutive bits is likely not minimal for most squares. It requires one or two gaps inside the consecutive N bits, to avoid collisions, blowing up the table size.

But the purpose is to perfectly hash attack-sets rather than consecutive occupied bits.

The number of distinct attack-sets is much smaller than the relevant occupancies. Thus, with the help of constructive collisions, some initial guess how to map the bits, and/or trial and error, using exactly N bits is always possible. If we try hard enough to maximize constructive collisions - even less.

### Perfect Hashing

Magic bitboards applies [perfect hashing](/Hash_Table#PerfectHashing "Hash Table"). A [surjective function](https://en.wikipedia.org/wiki/Surjection), to map the vector of all relevant occupancies to a range of attack-sets per square. The less bits the attack-set - the closer the blockers, the more those attack-sets are shared by occupancies with different, but redundant outer squares.

- The **cardinality** of all **relevant occupancies** is determined by the number of bits to map, varying from five to twelve - thus, the cardinality is the power of two the number of bits, varying from 32 to 4096.
- The **cardinality** of **distinct attack-sets** is determined by the product of the length of each of the max four direction rays greater than zero (or one). The rook on d4 has 3\*4\*3\*4 = 144 distinct attack-sets, a bishop on a8 has only 7.

The **ratio** of both cardinalities, that is all **relevant occupancies** versus the all **distinct attack-sets** is illustrated below: As a quarter of a board - due to the symmetry, the other squares may deduced by flipping and mirroring. Noticeable is the huge 4096/49 ratio of 2^12 occupied states versus 7 times 7 attack-sets of the edge rooks - 12 bits instead of 6. Those "expensive" squares make constructive collisions very desirable. To become more "minimal" by saving an index bit - to halve down the table for one square or the other.

| bishop on square | | | | | #occs/ #attset | rook on square | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | A | B | C | D |  | A | B | C | D |
| 8 | 64/7 | 32/6 | 32/10 | 32/12 |  | 8 | 4096/49 | 2048/42 | 2048/70 | 2048/84 |
| 7 | 32/6 | 32/6 | 32/10 | 32/ 12 | 7 | 2048/42 | 1024/36 | 1024/ 60 | 1024/ 72 |
| 6 | 32/10 | 32/10 | 128/40 | 128/ 48 | 6 | 2048/70 | 1024/60 | 1024/100 | 1024/120 |
| 5 | 32/12 | 32/12 | 128/48 | 512/108 | 5 | 2048/84 | 1024/72 | 1024/120 | 1024/144 |
|  | | | | | | | | | | |
| bishop on square | | | | | rook on square | | | | |
|  | A | B | C | D |  | A | B | C | D |
| 8 | 9.14 | 5.33 | 3.20 | 2.67 | 8 | 83.59 | 48.76 | 29.26 | 24.38 |
| 7 | 5.33 | 5.33 | 3.20 | 2.67 | 7 | 48.76 | 28.44 | 17.07 | 14.22 |
| 6 | 3.20 | 3.20 | 3.20 | 2.67 | 6 | 29.26 | 17.07 | 10.24 | 8.53 |
| 5 | 2.67 | 2.67 | 2.67 | 4.74 | 5 | 24.38 | 14.22 | 8.53 | 7.11 |

The idea to implement minimal perfect hashing by an additional 16-bit indirection turned out to be slower.

Recent table sizes were about **38 KByte** for the bishop attacks, but still about **800 KByte** for rook attacks. That sounds huge, considering L1 and L2 (L3) cache-sizes and number of cachelines and pages needed - we likely fetch distinct cachelines for each different square or occupancy. On the other hand caches and pages become larger in future processors. And occupancy and squares of the lookups don't change that randomly inside a search that we can still expect a lot of L1-hits. Unfortunately changes in occupancy outside the blockers and therefor not affecting the attack-set will introduce some more cache misses.

### Sample Code

Anyway, register usage and code size are important issues as well - and here **magic bitboards** are unbeatable - specially bishopAttacks, with respect to the relative small table.

```
U64 attacks_table[...]; // ~840K Byte all rook and bishop attacks

struct SMagic {
   U64* ptr;  // pointer to the attack-table for one particular square
   U64 mask;  // to mask of both lines
   U64 magic; // magic 64-bit factor
   int shift; // shift right 
};

SMagic mBishopTbl[64];
SMagic mRookTbl[64];

U64 bishopAttacks(U64 occ, enumSquare sq) {
   U64* aptr = mBishopTbl[sq].ptr;
   occ      &= mBishopTbl[sq].mask;
   occ      *= mBishopTbl[sq].magic;
   occ     >>= mBishopTbl[sq].shift;
   return aptr[occ];
}

U64 rookAttacks(U64 occ, enumSquare sq) {
   U64* aptr = mRookTbl[sq].ptr;
   occ      &= mRookTbl[sq].mask;
   occ      *= mRookTbl[sq].magic;
   occ     >>= mRookTbl[sq].shift;
   return aptr[occ];
}
```

# Summary

The bitboard method for holding a board game appears to have been invented in the mid 1950's, by [Arthur Samuel](/Arthur_Samuel "Arthur Samuel") and was used in his checkers program. In computer chess bitboards were first described by [Georgy Adelson-Velsky](/Georgy_Adelson-Velsky "Georgy Adelson-Velsky") et al. in 1967 [[15]](#cite_note-15), reprinted 1970 [[16]](#cite_note-16). Bitboards were used both in [Kaissa](/Kaissa "Kaissa") and independently in [Chess](/Chess_(Program) "Chess (Program)"). The invention and publication of [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards") by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") and [Peter Gillgasch](/Peter_Gillgasch "Peter Gillgasch") with [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") in the 90s was another milestone in the history of bitboards. While rotated bitboards was the mainstream in bitboard chess programs, [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") become more populated nowadays. Finally, [Steffan Westcott's](/Steffan_Westcott "Steffan Westcott") innovations, too expensive with 32-bit [x86](/X86 "X86") architectures, should be revisited with [x86-64](/X86-64 "X86-64") and [SIMD instructions](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") in mind.

---

# References

1. [↑](#cite_ref-1) [Workshop Chess and Mathematics](http://www.math.tu-dresden.de/num/chess2008/abstracts.pdf) (pdf) agenda and abstracts
2. [↑](#cite_ref-2) [Charles E. Leiserson](/Charles_Leiserson "Charles Leiserson"), [Harald Prokop](/Harald_Prokop "Harald Prokop"), [Keith H. Randall](/Keith_H._Randall "Keith H. Randall") (**1998**) [Using de Bruijn Sequences to Index a 1 in a Computer Word](http://supertech.csail.mit.edu/papers/debruijn.pdf) (pdf)
3. [↑](#cite_ref-3) [bitboard 2^i mod 67 is unique](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d5dbf08c66e83517#) by [Stefan Plenkner](/Stefan_Plenkner "Stefan Plenkner"), [rec.games.chess.computer](/Computer_Chess_Forums "Computer Chess Forums"), August 6, 1996
4. [↑](#cite_ref-4) [bitboard 2^i mod 67 is unique](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/871851f83e2c429f#) by [Joël Rivat](/Jo%C3%ABl_Rivat "Joël Rivat"), [rec.games.chess.computer](/Computer_Chess_Forums "Computer Chess Forums"), September 2, 1996
5. [↑](#cite_ref-5) [bitboard 2^i mod 67 is unique](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/9658009e315021fe#) by [Stefan Plenkner](/Stefan_Plenkner "Stefan Plenkner"), [rec.games.chess.computer](/Computer_Chess_Forums "Computer Chess Forums"), August 7, 1996
6. [↑](#cite_ref-6) [Re: flood fill attack bitboards](https://www.stmintz.com/ccc/index.php?id=252289) by [Steffan Westcott](/Steffan_Westcott "Steffan Westcott"), [CCC](/CCC "CCC"), September 15, 2002
7. [↑](#cite_ref-7) [Hardware algorithms for arithmetic modules](http://www.aoki.ecei.tohoku.ac.jp/arith/mg/algorithm.html#fsa_pfx) from the ARITH research group, Aoki lab., Tohoku University
8. [↑](#cite_ref-8) [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.craftychess.com/hyatt/bitmaps.html)*. [ICCA Journal](/ICGA_Journal "ICGA Journal"), [Vol. 22, No. 4](http://www.cs.unimaas.nl/icga/journal/contents/content22-4.htm), pp. 213–222.
9. [↑](#cite_ref-9) [Rotated Bitboards by Ernst A. Heinz](http://people.csail.mit.edu/heinz/dt/node8.html)
10. [↑](#cite_ref-10) [Trevor Fenner](/Trevor_Fenner "Trevor Fenner"), [Mark Levene](/Mark_Levene "Mark Levene") (**2008**). *Move Generation with Perfect Hashing Functions.* [ICGA Journal](/ICGA_Journal "ICGA Journal"), Vol. 31, No. 1, pp. 3-12. ISSN 1389-6911.
11. [↑](#cite_ref-11) [Nice Math - Strange Conclusions](http://www.talkchess.com/forum/viewtopic.php?t=20913) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC")
12. [↑](#cite_ref-12) [Lasse Hansen's](/Lasse_Hansen "Lasse Hansen") [Initial idea](http://www.open-aurec.com/wbforum/viewtopic.php?t=5015) from [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), June 14, 2006
13. [↑](#cite_ref-13) [Magic Move-Bitboard Generation in Computer Chess](http://www.pradu.us/old/Nov27_2008/Buzz/research/magic/Bitboards.pdf) (pdf) by [Pradu Kannan](/Pradu_Kannan "Pradu Kannan")
14. [↑](#cite_ref-14) [List of magics for bitboard move generation](http://www.open-aurec.com/wbforum/viewtopic.php?t=5441) thread started by [Pradu Kannan](/Pradu_Kannan "Pradu Kannan") from [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), Aug 23, 2006
15. [↑](#cite_ref-15) [Early Reference on Bit-Boards](http://groups.google.com/group/rec.games.chess/browse_frm/thread/0e3a93f45ff07d31#) by [Tony Warnock](/Tony_Warnock "Tony Warnock"), October 29, 1994 [rec.games.chess archive](http://groups.google.com/group/rec.games.chess/topics)
16. [↑](#cite_ref-16) [Georgy Adelson-Velsky](/Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](/Vladimir_Arlazarov "Vladimir Arlazarov"), [Alexander Bitman](/Alexander_Bitman "Alexander Bitman"), [Alexander Zhivotovsky](/Alexander_Zhivotovsky "Alexander Zhivotovsky") and [Anatoly Uskov](/Anatoly_Uskov "Anatoly Uskov") (**1970**). *Programming a Computer to Play Chess*. Russian Mathematical Surveys, Vol. 25, pp. 221-262

**[Up one Level](/Workshop_Chess_and_Mathematics "Workshop Chess and Mathematics")**