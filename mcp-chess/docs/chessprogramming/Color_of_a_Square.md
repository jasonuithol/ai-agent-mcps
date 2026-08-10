# Color of a Square

Source: https://www.chessprogramming.org/Color_of_a_Square

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Squares](/Squares "Squares") \* Color of a Square**

[![](/images/thumb/6/69/Study_for_Homage_to_the_Square.jpg/300px-Study_for_Homage_to_the_Square.jpg)](/File:Study_for_Homage_to_the_Square.jpg)

[Josef Albers](/index.php?title=Category:Josef_Albers&action=edit&redlink=1 "Category:Josef Albers (page does not exist)") - [Homage to the Square](https://en.wikipedia.org/wiki/Josef_Albers#Homage_to_the_Square) [[1]](#cite_note-1)

The **Color of a Square** of a [8x8 board](/8x8_Board "8x8 Board") may be determined by several approaches. Since the number of files (and ranks) is even, and black and white colors alternate on consecutive ranks (and files), one can not use the simple [parity](https://en.wikipedia.org/wiki/Parity_%28mathematics%29) of the combined square index in the 0..63 range. Applications are mostly related square color bounded [bishops](/Bishop "Bishop"), for instance to find the right corners in [KBNK Endgame](/KBNK_Endgame "KBNK Endgame").

# By Lookup

The obvious approach is a memory lookup of a pre-calculated 64 byte [array](/Array "Array"), containing the color of each square index. Alternatively one may use an In-Register Lookup, using a constant [Bitboard](/Bitboards "Bitboards") representing all dark squares.

```
0xAA55AA55AA55AA55
 . 1 . 1 . 1 . 1
 1 . 1 . 1 . 1 .
 . 1 . 1 . 1 . 1
 1 . 1 . 1 . 1 .
 . 1 . 1 . 1 . 1
 1 . 1 . 1 . 1 .
 . 1 . 1 . 1 . 1
 1 . 1 . 1 . 1 .
```

Shifting right this bitboard by square index, and masking off the least significant bit, leaves the square color:

```
enumColor colorOfSquare (enumSquare square) {
   U64 dark = C64(0xAA55AA55AA55AA55);
   return (dark >> square) & 1;
}
```

On [x86](/X86 "X86") one may use a shorter 32-bit constant and 32-bit shift, since the 32-bit shift is implicitly modulo 32 ... [[2]](#cite_note-2)

```
enumColor colorOfSquare (enumSquare square) {
   return (0xAA55AA55 >> square) & 1; // return (0xAA55AA55 >> (square & 31 )) & 1; 
}
```

... which also works for [0x88](/0x88 "0x88") coordinates, since the In-Register lookup covers one even and odd 16-bit rank.

```
enumColor colorOfSquare (int x88square) {
   return (0x00AA0055 >> x88square) & 1;
}
```

# By Anti-Diagonal Index

Another approach is based on whether the [anti-diagonal](/Anti-Diagonals "Anti-Diagonals") index (sum of [rank](/Ranks "Ranks") and [files](/Files "Files")) is odd or even. An even index (bit 0 clear) implies a black or dark square, an odd index light or white squares. Since we need to mask off the least significant bit only, we can save masking off the file from square, because upper bits have no influence on bit zero anyway. To be conform with the arbitrary [color definition](/Color#Definition "Color") (black == 1 rather than 0), one additional toggleColor, aka xor with '1' is necessary:

```
enumColor colorOfSquare (enumSquare square) {
   return toggleColor( ((square >> 3) + square) & 1); // +-^
}
```

Same applies for the [diagonal](/Diagonals "Diagonals") index as well (difference of [rank](/Ranks "Ranks") and [files](/Files "Files")), thus one can replace 'plus' by 'minus' or ['exclusive or'](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations"), as shown in [bitwise arithmetic](/Bit#BitwiseArithmetic "Bit").

A small transformation may save one register ...

```
enumColor colorOfSquare (enumSquare square) {
   return (( 9 * square + 8 ) >> 3) & 1;
}
```

... with following [x86](/X86 "X86") assembly in mind:

```
  lea  eax, [8*eax + eax + 8]
  shr  eax, 3
  and  eax, 1
```

A boolean condition even saves the shift, but tests bit 3:

```
bool isDark (enumSquare square) {
   //return (( 9 * square + 8) & 8) != 0;
   return (( 9 * square) & 8) == 0;
}
```

... with this assembly in mind:

```
  lea  eax, [8*eax + eax]
  test eax, 8
  jz   isDark
```

# Same color

The same tricks might be applied to determine two squares have the same color or not. If the sum of both [anti-diagonal](/Anti-Diagonals "Anti-Diagonals") indices is odd, the color is different. Using xor (sq1 ^= sq2) to 'add' ranks and files simultaneously or [SWAR-wise](/SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques") without possible overflows saves one instruction.

```
bool differentColor (enumSquare sq1, enumSquare sq2) {
   sq1 ^= sq2;
   return ( (sq1 >> 3) ^ sq1) & 1;
}
```

The mentioned lea-transformation saves one register and shift, if one jumps conditionally anyway...

```
bool differentColor (enumSquare sq1, enumSquare sq2) {
   return (( 9 * (sq1 ^ sq2)) & 8) != 0;
}
```

... also for the complement expression:

```
bool sameColor (enumSquare sq1, enumSquare sq2) {
   return (( 9 * (sq1 ^ sq2)) & 8) == 0;
}
```

Alternatively, if one has a [Knight-Distance](/Knight-Distance "Knight-Distance") 64 x 64 [array](/Array "Array"), one may use the least significant bit, since all even Knight-Distances between squares imply same square color.

# See also

- [Anti-Diagonals](/Anti-Diagonals "Anti-Diagonals")
- [Bishops of Opposite Colors](/Bishops_of_Opposite_Colors "Bishops of Opposite Colors")
- [Color](/Color "Color")
- [Diagonals](/Diagonals "Diagonals")
- [KBNK Endgame](/KBNK_Endgame "KBNK Endgame")
- [Knight-Distance](/Knight-Distance "Knight-Distance")
- [Wrong Color Bishop and Rook Pawn](/Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")

# References

1. [↑](#cite_ref-1) [Josef Albers](/index.php?title=Category:Josef_Albers&action=edit&redlink=1 "Category:Josef Albers (page does not exist)") - One Study for the [Homage to the Square](https://en.wikipedia.org/wiki/Josef_Albers#Homage_to_the_Square) Series, Exhibition in [Josef Albers Museum Quadrat](https://de.wikipedia.org/wiki/Quadrat_Bottrop), [Bottrop](https://en.wikipedia.org/wiki/Bottrop), Photo by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), September 16, 2018
2. [↑](#cite_ref-2) [Two small in-register-lookups](http://www.talkchess.com/forum/viewtopic.php?t=13344) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), April 23, 2007

**[Up one Level](/Squares "Squares")**