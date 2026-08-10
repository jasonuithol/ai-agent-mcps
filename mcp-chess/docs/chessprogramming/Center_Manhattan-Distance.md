# Center Manhattan-Distance

Source: https://www.chessprogramming.org/Center_Manhattan-Distance

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Squares](/Squares "Squares") \* Center Manhattan-Distance**

The **Center Manhattan-Distance** is the [Manhattan-Distance](/Manhattan-Distance "Manhattan-Distance") or number of orthogonal [King](/King "King") moves on the otherwise empty board from any square to the four squares {d4, d5, e4, e5} in the center of the board. In conjunction with [Center Distance](/Center_Distance "Center Distance") a constant [array](/Array "Array") might be considered as the base of [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables"). Center Manhattan-Distance is used in various evaluation terms, for instance to encourage the king to centralize in the ending, as well in [Mop-up Evaluation](/Mop-up_Evaluation "Mop-up Evaluation").

# Lookup

Rather than to calculate the Center Manhattan-Distance from square coordinates, taking the sum from the file- and rank- Center Distance each, a lookup of a small array is appropriate. This is how the Center Manhattan-Distance might be defined in [C](/C "C") or [C++](/Cpp "Cpp"):

```
const int arrCenterManhattanDistance[64] = { // char is sufficient as well, also unsigned
  6, 5, 4, 3, 3, 4, 5, 6,
  5, 4, 3, 2, 2, 3, 4, 5,
  4, 3, 2, 1, 1, 2, 3, 4,
  3, 2, 1, 0, 0, 1, 2, 3,
  3, 2, 1, 0, 0, 1, 2, 3,
  4, 3, 2, 1, 1, 2, 3, 4,
  5, 4, 3, 2, 2, 3, 4, 5,
  6, 5, 4, 3, 3, 4, 5, 6
};
```

# Calculation

Avoid Memory lookup purists may use following calculation. The routine first extracts file and rank. If either is less than 4, its ones' complement is used, to get the file or rank wise Manhattan Center Distance from the two lower bits each (while the third lowest bit 2, is always set).

```
file = sq  & 7;             //  0  1  2  3  4  5  6  7
if (file < 4) file = ~file; // -1 -2 -3 -4  4  5  6  7  bit 2 is always set
file &= 3;                  //  3  2  1  0  0  1  2  3
```

The file and rank distances are added for the final Manhattan Center Distance. The slight optimization considers each summand has bit 2 set, to perform the 'add' with a final post-mask 7, rather than to add two pre-masks with 3.

```
/**
 * manhattanCenterDistance
 * @author Gerd Isenberg
 * @param sq square 0..63
 * @return Manhattan Center Distance
 */
int manhattanCenterDistance(int sq) {
   int file, rank;
   file  = sq  & 7;
   rank  = sq >> 3;
   file ^= (file-4) >> 8;
   rank ^= (rank-4) >> 8;
   return (file + rank) & 7;
}
```

with following generated [x86](/X86 "X86") [Assembly](/Assembly "Assembly"):

```
?manhattanCenterDistance PROC NEAR
; _sq$ = ecx
  00000	8b d1       mov  edx, ecx
  00002	c1 f9 03    sar  ecx, 3
  00005	8d 41 fc    lea  eax, DWORD PTR [ecx-4]
  00008	c1 f8 08    sar  eax, 8
  0000b	33 c1       xor  eax, ecx
  0000d	83 e2 07    and  edx, 7
  00010	8d 4a fc    lea  ecx, DWORD PTR [edx-4]
  00013	c1 f9 08    sar  ecx, 8
  00016	33 ca       xor  ecx, edx
  00018	03 c1       add  eax, ecx
  0001a	83 e0 07    and  eax, 7
  0001d	c3          ret  0
```

# See also

- [Avoiding Branches](/Avoiding_Branches "Avoiding Branches")
- [Center Distance](/Center_Distance "Center Distance")
- [Corner-Distance](/KBNK_Endgame#CornerDistance "KBNK Endgame") in [KBNK Endgame](/KBNK_Endgame "KBNK Endgame")
- [Manhattan-Distance](/Manhattan-Distance "Manhattan-Distance")
- [Mop-up Evaluation](/Mop-up_Evaluation "Mop-up Evaluation")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")

# Forum Posts

- [Simple method for simple mates for programs without TBs](http://www.talkchess.com/forum/viewtopic.php?t=62257) by [J. Wesley Cleveland](/index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](/CCC "CCC"), November 25, 2016 » [Mop-up Evaluation](/Mop-up_Evaluation "Mop-up Evaluation"), [KBNK Endgame](/KBNK_Endgame "KBNK Endgame")

# External Links

- [CAB](/Category:CAB "Category:CAB") - Wah Wah, [Tony MacAlpine](https://en.wikipedia.org/wiki/Tony_MacAlpine), [Bunny Brunel](https://en.wikipedia.org/wiki/Bunny_Brunel), [Dennis Chambers](/Category:Dennis_Chambers "Category:Dennis Chambers"), [Brian Auger](/Category:Brian_Auger "Category:Brian Auger"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

**[Up one Level](/Squares "Squares")**