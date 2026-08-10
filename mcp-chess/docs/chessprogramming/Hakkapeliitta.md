# Hakkapeliitta

Source: https://www.chessprogramming.org/Hakkapeliitta

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Hakkapeliitta**

[![](https://upload.wikimedia.org/wikipedia/commons/c/c8/Hakkapeliitta-1940.jpg)](/File:Hakkapeliitta-1940.jpg)

Hakkapeliitta [[1]](#cite_note-1)

**Hakkapeliitta**,  
an [UCI](/UCI "UCI") compatible [open source chess engine](/Category:Open_Source "Category:Open Source") by [Mikko Aarnos](/Mikko_Aarnos "Mikko Aarnos"), written in [C++11/14](/Cpp "Cpp") and licensed under the [GNU General Public License](/Free_Software_Foundation#GPL "Free Software Foundation"), Version 3. Hakkapeliitta is a state of the art [bitboard](/Bitboards "Bitboards") engine, and performs [Magic bitboards](/Magic_Bitboards "Magic Bitboards") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks"). Despite using conditional compiled [x86-64](/X86-64 "X86-64") processer instructions for [bitscan](/BitScan "BitScan"), Hakkapeliitta uses [Kim Walisch's](/Kim_Walisch "Kim Walisch") [forward](/BitScan#KimWalisch "BitScan") and [reverse bitscans](/BitScan#FillDeBruijn "BitScan") [[2]](#cite_note-2). If the processor does not support hardware [popcount](/Population_Count "Population Count"), Hakkapeliitta falls back to [SWAR-popcount](/Population_Count#SWARPopcount "Population Count"). The [search](/Search "Search") uses [function templates](https://en.wikipedia.org/wiki/Template_%28C%2B%2B%29#Function_templates) to distinguish between [PV-nodes](/Node_Types#PV "Node Types") and none PV-nodes at compile time [[3]](#cite_note-3). Similar, hardware popcount support is boolean template parameter of [evaluation](/Evaluation "Evaluation") routines [[4]](#cite_note-4).

# Etymology

The term is probably based on the [Finnish](https://en.wikipedia.org/wiki/Finnish_language) [battle cry](https://en.wikipedia.org/wiki/Battle_cry) "Hakkaa päälle" [[5]](#cite_note-5), commonly translated as "Cut them down!". The Finnish [cavalryman](https://en.wikipedia.org/wiki/Cavalry) in the service of [King](https://en.wikipedia.org/wiki/Monarchy_of_Sweden) [Gustavus Adolphus](https://en.wikipedia.org/wiki/Gustavus_Adolphus_of_Sweden) of [Sweden](https://en.wikipedia.org/wiki/Swedish_Empire) during the [Thirty Years' War](https://en.wikipedia.org/wiki/Thirty_Years%27_War) (1618 to 1648) were called Hackapelit, Hackapelite, Hackapell, Haccapelit, or Haccapelite in the [Holy Roman Empire](https://en.wikipedia.org/wiki/Holy_Roman_Empire), in the [19th-century](https://en.wikipedia.org/wiki/19th_century) modified to Finnish **Hakkapeliitta** [[6]](#cite_note-6) [[7]](#cite_note-7).

# Features

[[8]](#cite_note-8)

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Move Count Based Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
- [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
- [Razoring](/Razoring "Razoring")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [Relative History Heuristic](/Relative_History_Heuristic "Relative History Heuristic")
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](/Evaluation "Evaluation")

- [Material](/Material "Material")
- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
- [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")

:   [Backward Pawn](/Backward_Pawn "Backward Pawn")
:   [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
:   [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
:   [Passed Pawn](/Passed_Pawn "Passed Pawn")

- [King Safety](/King_Safety "King Safety")

:   [Pawn Shelter](/King_Safety#PawnShield "King Safety")

## Misc

- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")
- [Perft](/Perft "Perft")
- [Pondering](/Pondering "Pondering") (since 3.0)
- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")

# Acknowledgements

Thanks from the author to following [people](/People "People") or [organizations](/Organizations "Organizations") [[9]](#cite_note-9)

- [CPW](/Main_Page "Main Page") (Thanks as well)
- [Talkchess](/CCC "CCC")
- [Tord Romstad](/Tord_Romstad "Tord Romstad") of [Glaurung](/Glaurung "Glaurung")
- [Ronald de Man](/Ronald_de_Man "Ronald de Man")
- [Tord Romstad](/Tord_Romstad "Tord Romstad"), [Marco Costalba](/Marco_Costalba "Marco Costalba"), and [Joona Kiiski](/Joona_Kiiski "Joona Kiiski") of [Stockfish](/Stockfish "Stockfish")
- [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") of [Crafty](/Crafty "Crafty")
- [Peter Österlund](/Peter_%C3%96sterlund "Peter Österlund") of [Texel](/Texel "Texel")
- Authors of [IvanHoe](/IvanHoe "IvanHoe")
- [Ed Schröder](/Ed_Schroder "Ed Schroder") of [Rebel](/Rebel "Rebel") and [ProDeo](/ProDeo "ProDeo") [[10]](#cite_note-10)
- [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)") of [Winglet](/Winglet "Winglet") [[11]](#cite_note-11)
- [Steve Maughan](/Steve_Maughan "Steve Maughan") of [Maverick](/Maverick "Maverick")
- [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan") of [TSCP](/TSCP "TSCP")

# Forum Posts

## 2014

- [Hakkapeliitta dev 63.7 by Mikko Aarnos](http://www.talkchess.com/forum/viewtopic.php?t=51406) by [Jose Mº Velasco](/Jose_Maria_Velasco "Jose Maria Velasco"), [CCC](/CCC "CCC"), February 25, 2014
- [Hakkapeliitta 1.0 release](http://www.talkchess.com/forum/viewtopic.php?t=52725) by [Mikko Aarnos](/Mikko_Aarnos "Mikko Aarnos"), [CCC](/CCC "CCC"), June 22, 2014
- [Hakkapeliitta 2.0 release](http://www.talkchess.com/forum/viewtopic.php?t=54749) by [Mikko Aarnos](/Mikko_Aarnos "Mikko Aarnos"), [CCC](/CCC "CCC"), December 25, 2014

## 2015 ...

- [Hakkapeliitta 3.0 release](http://www.talkchess.com/forum/viewtopic.php?t=56790) by [Mikko Aarnos](/Mikko_Aarnos "Mikko Aarnos"), [CCC](/CCC "CCC"), June 27, 2015
- [Hakkapeliitta the "STRONGEST" in tactic, new Nr1](http://www.talkchess.com/forum/viewtopic.php?t=57029) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), July 19, 2015
- [Hakkapeliitta TCEC, dev relase](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=59924) by [velmarin](/index.php?title=Jose_M%C2%BA_Velasco&action=edit&redlink=1 "Jose Mº Velasco (page does not exist)"), [CCC](/CCC "CCC"), April 21, 2016

# External Links

## Chess Engine

- [mAarnos/Hakkapeliitta · GitHub](https://github.com/mAarnos/Hakkapeliitta)
- [Hakkapeliitta](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Hakkapeliitta&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](/CCRL "CCRL")

## Misc

- [Hakkapeliitta - Wiktionary](https://en.wiktionary.org/wiki/Hakkapeliitta)
- [Hakkapeliitta from Wikipedia](https://en.wikipedia.org/wiki/Hakkapeliitta)
- [Hakkapeliittain Marssi from Wikipedia](https://en.wikipedia.org/wiki/Hakkapeliittain_Marssi)
- [Hakkapeliitta (lehti) Wikipedia](https://fi.wikipedia.org/wiki/Hakkapeliitta_%28lehti%29) (Finnish, Paramilitary Journal 1926 - 1944)
- [Mossy Rocks](http://www.mossyrocks.ca/) - Cut Em Down, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Hakkapeliitta](https://commons.wikimedia.org/wiki/File:Hakkapeliitta-1940.jpg) featured on a 1940 Finnish stamp, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Hakkapeliitta/bitboard.hpp at master · mAarnos/Hakkapeliitta · GitHub](https://github.com/mAarnos/Hakkapeliitta/blob/master/src/bitboards.hpp)
3. [↑](#cite_ref-3) [Hakkapeliitta/search.cpp at master · mAarnos/Hakkapeliitta · GitHub](https://github.com/mAarnos/Hakkapeliitta/blob/master/src/search.cpp) - template <bool pvNode> int Search::search
4. [↑](#cite_ref-4) [Hakkapeliitta/evaluation.cpp at master · mAarnos/Hakkapeliitta · GitHub](https://github.com/mAarnos/Hakkapeliitta/blob/master/src/evaluation.cpp)
5. [↑](#cite_ref-5) [Hakkapeliitta - Wiktionary](https://en.wiktionary.org/wiki/Hakkapeliitta)
6. [↑](#cite_ref-6) [Hakkapeliitta from Wikipedia](https://en.wikipedia.org/wiki/Hakkapeliitta)
7. [↑](#cite_ref-7) [Military of the Swedish Empire - Wikipedia](https://en.wikipedia.org/wiki/Military_of_the_Swedish_Empire)
8. [↑](#cite_ref-8) based on sources of [Hakkapeliitta 2.0](https://github.com/mAarnos/Hakkapeliitta/tree/master/src)
9. [↑](#cite_ref-9) [mAarnos/Hakkapeliitta · GitHub - Acknowledgements](https://github.com/mAarnos/Hakkapeliitta)
10. [↑](#cite_ref-10) [Inside Rebel/Prodeo](http://www.top-5000.nl/authors/rebel/chess840.htm) by [Ed Schröder](/Ed_Schroder "Ed Schroder")
11. [↑](#cite_ref-11) [Winglet, Writing a Chess Program in 99 Steps](http://web.archive.org/web/20120621100214/http://www.sluijten.com/winglet/) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)

**[Up one level](/Engines "Engines")**