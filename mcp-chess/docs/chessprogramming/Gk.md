# Gk

Source: https://www.chessprogramming.org/Gk

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Gk**

**Gk**, (GKJunior)  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") under the [GNU General Public License](/Free_Software_Foundation#GPL "Free Software Foundation"), written by [Tijs van Dam](/index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)") in [C++](/Cpp "Cpp"), first released in May 2003, while its private forerunner GKJunior already played at [Internet Chess Club](/index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)") in the late 90s [[1]](#cite_note-1) [[2]](#cite_note-2).

# Description

## Bitboard Infrastructure

As [bitboard](/Bitboards "Bitboards") engine, Gk [generates moves](/Move_Generation "Move Generation") with the typical [serialization loops](/Bitboard_Serialization "Bitboard Serialization") on move target sets, and uses [Brian Kernighan's population count](/Population_Count#BrianKernighansway "Population Count") to determine the cardinality of sets.

### Rotated Indices

Gk applies [rotated indices](/Rotated_Indices "Rotated Indices") with 1/2 MiB pre-initialized lookup tables to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks"), indexed by square and [8-bit line occupancy](/Occupancy_of_any_Line "Occupancy of any Line") [[3]](#cite_note-3):

```
BitBoard diag_h1_attack[64][256];
BitBoard diag_a1_attack[64][256];
BitBoard diag_file_attack[64][256];
BitBoard diag_rank_attack[64][256];
```

Rather than keeping the [rotated](/Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating") [occupancies](/Occupancy "Occupancy") inside [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards"), a deconcentrated data structure of unsigned integer arrays is used keeping 8-bit occupancies for each enumerated line of either 8 [ranks](/Ranks "Ranks") / [files](/Files "Files") or 15 [diagonals](/Diagonals "Diagonals") / [anti-diagonals](/Anti-Diagonals "Anti-Diagonals"), [incrementally updated](/Incremental_Updates "Incremental Updates") during [make](/Make_Move "Make Move") and [unmake move](/Unmake_Move "Unmake Move") [[4]](#cite_note-4):

```
unsigned diag_h1_occ[15];
unsigned diag_a1_occ[15];
unsigned diag_file_occ[8];
unsigned diag_rank_occ[8];

INLINE BitBoard AttacksDiagA1(int square) {
  return diag_a1_attack[square][diag_a1_occ[DiagA1DiagNum(square)]];
}

INLINE int DiagA1DiagNum(int square) {
  return 7-Rank(square)+File(square);
}
```

### BitScan

[BitScan](/BitScan "BitScan") is either implemented in 32-bit [x86](/X86 "X86") [Assembly](/Assembly "Assembly"), or with 16-bit indexed, 64K int lookup tables of 1/2 MiB and conditions for other architectures. FirstOne scans reverse, LastOne forward [[5]](#cite_note-5):

```
int first_ones[65536];
int last_ones[65536];

INLINE int FirstOne(BitBoard b) {
#ifdef USE_ASM
ASM {
   bsr     edx, dword ptr b+4 // is there a 1 in the high word?
   mov     eax, 32
   jnz     l1                 // return FirstOne(hiword(b))+32
   bsr     edx, dword ptr b   // else return FirstOne(loword(b))
   xor     eax, eax
l1:add     eax, edx
  }
#else
  register U16 *x=(U16 *)(&b);
  if(x[3]) return first_ones[x[3]]+48;
  if(x[2]) return first_ones[x[2]]+32;
  if(x[1]) return first_ones[x[1]]+16;
  return first_ones[x[0]];
#endif
}

INLINE int LastOne(BitBoard b) {
#ifdef USE_ASM
__asm {
   bsf    eax, dword ptr b   // is there a 1 in the low word
   jnz    l1                 // then return LastOne(loword(b))
   bsf    eax, dword ptr b+4 // else return LastOne(hiword(b))+32
   add    eax,32
l1:
   }
#else
  register U16 *x=(U16 *)(&b);
  if(x[0]) return last_ones[x[0]];
  if(x[1]) return last_ones[x[1]]+16;
  if(x[2]) return last_ones[x[2]]+32;
  return last_ones[x[3]]+48;
#endif
}
```

## Search

The [search](/Search "Search") is [PVS](/Principal_Variation_Search "Principal Variation Search") [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework without [aspiration](/Aspiration_Windows "Aspiration Windows"), maintaining the [principal variations](/Principal_Variation "Principal Variation") inside a "quadratic" [PV-table](/Triangular_PV-Table "Triangular PV-Table"). [Selectivity](/Selectivity "Selectivity") is realized by [null move Pruning](/Null_Move_Pruning "Null Move Pruning"), [check extensions](/Check_Extensions "Check Extensions"), and [delta pruning](/Delta_Pruning "Delta Pruning") in [quiescence search](/Quiescence_Search "Quiescence Search"). [History heuristic](/History_Heuristic "History Heuristic"), [IID](/Internal_Iterative_Deepening "Internal Iterative Deepening"), [MVV-LVA](/MVV-LVA "MVV-LVA") in conjunction with a [SEE swap routine](/SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm") improve [move ordering](/Move_Ordering "Move Ordering") and delta pruning.

## Evaluation

Gk's [evaluation](/Evaluation "Evaluation") is rudimentary and restricts positional [scores](/Score "Score") in the range of plus-minus one [pawn](/Pawn "Pawn") [value](/Point_Value "Point Value") - at least it is very [lazy](/Lazy_Evaluation "Lazy Evaluation") if the [material balance](/Material#Balance "Material") is outside the [alpha-beta window](/Window "Window") by that margin. It considers [center control](/Center_Control "Center Control"), [mobility](/Mobility "Mobility"), [development](/Development "Development") and [too early queen](/Evaluation_of_Pieces#Queen "Evaluation of Pieces"), and some [pawn shield](/King_Safety#PawnShield "King Safety") and [castling right](/Castling_Rights "Castling Rights") related [king safety](/King_Safety "King Safety") stuff. The [cached](/Pawn_Hash_Table "Pawn Hash Table") [pawn structure](/Pawn_Structure "Pawn Structure") evaluation takes [passers](/Passed_Pawn "Passed Pawn"), [doubled](/Doubled_Pawn "Doubled Pawn") and [isolated pawns](/Isolated_Pawn "Isolated Pawn"), and [pawns protecting each other](/Defended_Pawns_(Bitboards) "Defended Pawns (Bitboards)") into account.

# See also

- [Fortress](/Fortress_(Engine) "Fortress (Engine)")
- [GK 2100](/GK_2100 "GK 2100")
- [PK](/PK "PK")

# Forum Posts

- [Re: ICC Green List - Jan 3](https://www.stmintz.com/ccc/index.php?id=85839) by [Tijs van Dam](/index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)"), [CCC](/CCC "CCC"), January 04, 2000
- [Re: Can we use hash table at root?](https://www.stmintz.com/ccc/index.php?id=93810) by [Tijs van Dam](/index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)"), [CCC](/CCC "CCC"), February 01, 2000 » [Transposition Table](/Transposition_Table "Transposition Table"), [Root](/Root "Root")
- [Re: More programs added to my tournament](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45776#p173920) by Sergio Martinez, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 27, 2003

# External Links

## Chess Engine

- [Tijs van Dam - Software](http://tijsvd.home.xs4all.nl/old_software/)

## Misc

- [GK (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/GK)
- [Garry Kasparov from Wikipedia](https://en.wikipedia.org/wiki/Garry_Kasparov)

# References

1. [↑](#cite_ref-1) [ICC Green List - Nov 29](https://www.stmintz.com/ccc/index.php?id=79887) by [Will Singleton](/Will_Singleton "Will Singleton"), [CCC](/CCC "CCC"), November 29, 1999
2. [↑](#cite_ref-2) [ICC Green List - Jan 3](https://www.stmintz.com/ccc/index.php?id=85701) by [Will Singleton](/Will_Singleton "Will Singleton"), [CCC](/CCC "CCC"), January 03, 2000
3. [↑](#cite_ref-3) [Tijs van Dam - Software](http://tijsvd.home.xs4all.nl/old_software/), gk-0.90.tar.gz / global.cpp
4. [↑](#cite_ref-4) [Tijs van Dam - Software](http://tijsvd.home.xs4all.nl/old_software/), gk-0.90.tar.gz / position.h
5. [↑](#cite_ref-5) [Tijs van Dam - Software](http://tijsvd.home.xs4all.nl/old_software/), gk-0.90.tar.gz / bitboard.h

**[Up one level](/Engines "Engines")**