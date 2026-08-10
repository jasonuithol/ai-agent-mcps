# Gibbon

Source: https://www.chessprogramming.org/Gibbon

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Gibbon**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Zhu-Zhanji-Gibbons-at-Play.jpg/330px-Zhu-Zhanji-Gibbons-at-Play.jpg)](/File:Zhu-Zhanji-Gibbons-at-Play.jpg)

Gibbons at Play [[1]](#cite_note-1)

**Gibbon**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Eric Marathée](/Eric_Marath%C3%A9e "Eric Marathée") written in [C++](/Cpp "Cpp"). Gibbon originated from [Small-C](/Small-C "Small-C") in 2005, playing [Massy 2006](/Massy_2006 "Massy 2006") and improving since then. While featuring some [bitboards](/Bitboards "Bitboards"), it has no annoying [magic bitboard stuff](/Magic_Bitboards "Magic Bitboards"), and is a counter approach of a [Fruit](/Fruit "Fruit") like programming style, full of [gotos](https://en.wikipedia.org/wiki/Goto), and difficult to follow [control flow](https://en.wikipedia.org/wiki/Control_flow) due to [indent style](https://en.wikipedia.org/wiki/Indent_style) and preprocessor switches for [conditional compilation](https://en.wikipedia.org/wiki/Conditional_compilation). Gibbon computes a few [nodes](/Node "Node"), but is an attempt to compute the right ones [[2]](#cite_note-2).

# Features

[[3]](#cite_note-3)

## [Search](/Search "Search")

- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search") (PVS) with [Iterative Deepening](/Iterative_Deepening "Iterative Deepening") and [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Two-tier Transposition Table](/Transposition_Table#TwoTier "Transposition Table"), [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
- [Move Ordering](/Move_Ordering "Move Ordering") with [Hash Move](/Hash_Move "Hash Move") and [Killer Moves](/Killer_Move "Killer Move")
- [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Enhanced Transposition Cutoff](/Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff") (conditional compiled)

### [Selectivity](/Selectivity "Selectivity")

- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning") with [R](/Depth_Reduction_R "Depth Reduction R") = 4
- [Non-PV nodes](/Node_Types "Node Types") [pruning](/Pruning "Pruning") ([Late Move Reductions](/Late_Move_Reductions "Late Move Reductions") [Fail-Low](/Fail-Low "Fail-Low")/[Fail-High](/Fail-High "Fail-High") [History](/History_Heuristic "History Heuristic"))
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Extended Futility Pruning](/Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
- [Extensions](/Extensions "Extensions") ([Check Extensions](/Check_Extensions "Check Extensions"), [Recapture Extensions](/Recapture_Extensions "Recapture Extensions"), [Passed Pawn Extensions](/Passed_Pawn_Extensions "Passed Pawn Extensions"))

### [Quiescence Search](/Quiescence_Search "Quiescence Search")

- One [check](/Check "Check") allowed at the [horizon](/Horizon_Node "Horizon Node")
- Quiescence [heuristic for checks](/Double_Attack "Double Attack") winning [hanging pieces](/Hanging_Piece "Hanging Piece")
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation") (SEE)
- [One Reply Extensions](/One_Reply_Extensions "One Reply Extensions") in quiescence

### [Mate at a Glance](/Mate_at_a_Glance "Mate at a Glance")

- [Mate in one](/Checkmate "Checkmate") recognition for queen moves
- Heuristic to identify moves threatening mate with queen and piece

## [Evaluation](/Evaluation "Evaluation")

- [Lazy Evaluation](/Lazy_Evaluation "Lazy Evaluation")
- [Mobility](/Mobility "Mobility")
- [Pawn Structure](/Pawn_Structure "Pawn Structure") considering king placement
- [Passed Pawns](/Passed_Pawn "Passed Pawn")
- [Trade down bonus](/Material "Material") that encourages the winning side to trade pieces but no pawns
- Incentive to keep the [queen](/Queen "Queen") in case of material down
- Incentive to keep at least one [pawn](/Pawn "Pawn")
- [Bishop Pair](/Bishop_Pair "Bishop Pair")

### [Opening](/Opening "Opening")

- [Development](/Development "Development")

### [Middlegame](/Middlegame "Middlegame")

- [King Safety](/King_Safety "King Safety") considering [castling rights](/Castling_Rights "Castling Rights")
- [Outposts](/Outposts "Outposts")

### [Endgame](/Endgame "Endgame")

- [Bishops of Opposite Colors](/Bishops_of_Opposite_Colors "Bishops of Opposite Colors")
- [Rule of the Square](/Rule_of_the_Square "Rule of the Square")
- [King Pawn Tropism](/King_Pawn_Tropism "King Pawn Tropism")
- [King Centralization](/King_Centralization "King Centralization")
- [Draw Evaluation](/Draw_Evaluation "Draw Evaluation")
- [Pawn Endgame](/Pawn_Endgame "Pawn Endgame")

## [Interior Node Recognizer](/Interior_Node_Recognizer "Interior Node Recognizer")

- [KPK](/KPK "KPK")
- [KRPKR](/Rook_Endgame#KRPKR "Rook Endgame")
- KQKQ
- [Wrong Color Bishop and Rook Pawn](/Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")
- KNKP
- KBKP
- KRKP

## Misc

- [Incremental](/Incremental_Updates "Incremental Updates") [Move Generation](/Move_Generation "Move Generation") (few [bitboards](/Bitboards "Bitboards"))

:   => Gibbon knows all [legal moves](/Legal_Move "Legal Move"), [material](/Material "Material"), [mobility](/Mobility "Mobility"), and check-giving squares

- [Opening Book](/Opening_Book "Opening Book")

# BitScan with Reset

In [serializing bitboards](/Bitboard_Serialization "Bitboard Serialization"), Gibbon applies a [bitscan with reset](/BitScan#BitscanwithReset "BitScan") based on the [De Bruijn multiplication](/BitScan#DeBruijnMultiplation "BitScan") approach published by [Charles Leiserson](/Charles_Leiserson "Charles Leiserson"), [Harald Prokop](/Harald_Prokop "Harald Prokop") and [Keith H. Randall](/Keith_H._Randall "Keith H. Randall") in 1998 [[4]](#cite_note-4). The [De Bruijn sequence](/De_Bruijn_Sequence "De Bruijn Sequence") chosen is even, which implies five leading zeros [[5]](#cite_note-5):

```
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
const char xindex64[64] = {
   63,  0, 58,  1, 59, 47, 53,  2,
   60, 39, 48, 27, 54, 33, 42,  3,
   61, 51, 37, 40, 49, 18, 28, 20,
   55, 30, 34, 11, 43, 14, 22,  4,
   62, 57, 46, 52, 38, 26, 32, 41,
   50, 36, 17, 19, 29, 10, 13, 21,
   56, 45, 25, 31, 35, 16,  9, 12,
   44, 24, 15,  8, 23,  7,  6,  5
};

#define set_bit_to_0(x64,xr)     (x64) &= ~((unsigned __int64)1<<(xr)) 

char SEARCH::bitScanForward_Clear(unsigned __int64 &bb) 
{
   char index;
   unsigned __int64  debruijn64 =(unsigned __int64)(0x07EDD5E59A4E28C2);
   ASSERT (bb != 0);
   // Ignorer le warning de compilation
   index=xindex64[((bb & -bb) * debruijn64) >> 58];
   set_bit_to_0(bb, index);
   return index;
}
```

# See also

- [Small-C](/Small-C "Small-C")

# Forum Posts

- [Gibbon 2.32a : 2219](http://www.talkchess.com/forum/viewtopic.php?t=13171) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), April 16, 2007
- [Gibbon 2.41a : 2258](http://www.talkchess.com/forum/viewtopic.php?t=14559) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), June 19, 2007
- [Gibbon 2.42c : 2200](http://www.talkchess.com/forum/viewtopic.php?t=16825) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), October 01, 2007
- [Gibbon 2.51a : 2249](http://www.talkchess.com/forum/viewtopic.php?t=26533) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), February 12, 2009
- [Gibbon 2.52a : 2208](http://www.talkchess.com/forum/viewtopic.php?t=26839) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), March 03, 2009

# External Links

## Chess Engine

- [gibbon home page](http://perso.numericable.com/monique.marathee/gibbon_home_page.html)
- [Gibbon](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Gibbon&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](/CCRL "CCRL")

## Misc

- [Gibbon from Wikipedia](https://en.wikipedia.org/wiki/Gibbon)
- [Gibbon (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Gibbon_%28disambiguation%29)

# References

1. [↑](#cite_ref-1) Gibbons at Play - [Chinese painting](https://en.wikipedia.org/wiki/Chinese_painting) 15th century, Hanging scroll, ink and colors on paper, Current location: [National Palace Museum](https://en.wikipedia.org/wiki/National_Palace_Museum), [Taipei](https://en.wikipedia.org/wiki/Taipei), [Taiwan](https://en.wikipedia.org/wiki/Taiwan), [Gibbons Wikipedia.de](https://de.wikipedia.org/wiki/Gibbons) (German)
2. [↑](#cite_ref-2) [gibbon home page](http://perso.numericable.com/monique.marathee/gibbon_home_page.html)
3. [↑](#cite_ref-3) Features based on the [gibbon home page](http://perso.numericable.com/monique.marathee/gibbon_home_page.html)
4. [↑](#cite_ref-4) [Charles E. Leiserson](/Charles_Leiserson "Charles Leiserson"), [Harald Prokop](/Harald_Prokop "Harald Prokop"), [Keith H. Randall](/Keith_H._Randall "Keith H. Randall") (**1998**). *Using de Bruijn Sequences to Index a 1 in a Computer Word*. [pdf](http://supertech.csail.mit.edu/papers/debruijn.pdf)
5. [↑](#cite_ref-5) [gibbon home page](http://perso.numericable.com/monique.marathee/gibbon_home_page.html), Gibbon 2.57.a - uci - Cchess\_2.h, Cchess\_4.h, maj.cpp

**[Up one level](/Engines "Engines")**