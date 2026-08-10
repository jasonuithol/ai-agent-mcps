# Center Distance

Source: https://www.chessprogramming.org/Center_Distance

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Squares](/Squares "Squares") \* Center Distance**

The **Center Distance** is the [distance](/Distance "Distance") (also known as [Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance)) or number of [King](/King "King") moves on the otherwise empty board from any square to the four squares {d4, d5, e4, e5} in the [center](/Center "Center") of the board. In conjunction with [Center Manhattan-distance](/Center_Manhattan-Distance "Center Manhattan-Distance") a constant [array](/Array "Array") might be considered as the base of [Piece-square tables](/Piece-Square_Tables "Piece-Square Tables"). Center distance is used in various [evaluation](/Evaluation "Evaluation") terms, for instance to encourage the king to [centralize](/King_Centralization "King Centralization") in the [ending](/Endgame "Endgame"), as well in [Mop-up Evaluation](/Mop-up_Evaluation "Mop-up Evaluation").

# Lookup

Rather than to calculate the Center distance from square coordinates, taking the max from the file- and rank- Center distance each, a lookup to a small array is appropriate here.

This is how the Center distance might be defined in [C](/C "C") or [C++](/Cpp "Cpp"):

```
const int arrCenterDistance[64] = { // char is sufficient as well, also unsigned
  3, 3, 3, 3, 3, 3, 3, 3,
  3, 2, 2, 2, 2, 2, 2, 3,
  3, 2, 1, 1, 1, 1, 2, 3,
  3, 2, 1, 0, 0, 1, 2, 3,
  3, 2, 1, 0, 0, 1, 2, 3,
  3, 2, 1, 1, 1, 1, 2, 3,
  3, 2, 2, 2, 2, 2, 2, 3,
  3, 3, 3, 3, 3, 3, 3, 3
};
```

# In Register Lookup

The avoid memory lookup purists may use two 64-bit in register lookups instead [[1]](#cite_note-1), but most likely it don't pays off.

```
int centerDistance(enumSquare sq) {
   const U64 bit0 = C64(0xFF81BDA5A5BD81FF);
   const U64 bit1 = C64(0xFFFFC3C3C3C3FFFF);
   return 2 * ((bit1 >> sq) & 1) + ((bit0 >> sq) & 1); 
}
```

with

```
 bit 1              bit 0
 1 1 1 1 1 1 1 1    1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1    1 . . . . . . 1
 1 1 . . . . 1 1    1 . 1 1 1 1 . 1
 1 1 . . . . 1 1    1 . 1 . . 1 . 1
 1 1 . . . . 1 1    1 . 1 . . 1 . 1
 1 1 . . . . 1 1    1 . 1 1 1 1 . 1
 1 1 1 1 1 1 1 1    1 . . . . . . 1
 1 1 1 1 1 1 1 1    1 1 1 1 1 1 1 1
```

# See also

- [Center Manhattan-Distance](/Center_Manhattan-Distance "Center Manhattan-Distance")
- [Distance](/Distance "Distance")
- [King Centralization](/King_Centralization "King Centralization")

# References

1. [↑](#cite_ref-1) [Two small in-register-lookups](http://www.talkchess.com/forum/viewtopic.php?t=13344) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), April 23, 2007

**[Up one Level](/Squares "Squares")**