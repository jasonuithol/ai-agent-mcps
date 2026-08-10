# Sungorus

Source: https://www.chessprogramming.org/Sungorus

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Sungorus**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Djungarian_hamster_%C5%9Awir_eating_pumpkin_seed.JPG/330px-Djungarian_hamster_%C5%9Awir_eating_pumpkin_seed.JPG)](/File:Djungarian_hamster_%C5%9Awir_eating_pumpkin_seed.JPG)

Phodopus Sungorus [[1]](#cite_note-1)

**Sungorus**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Pablo Vazquez](/Pablo_Vazquez "Pablo Vazquez"),
first released in June 2009 [[2]](#cite_note-2).
Last recent version is Sungorus 1.4 from June 2010, which was base of further development by [Pawel Koziol](/Pawel_Koziol "Pawel Koziol") and his [Rodent](/Rodent "Rodent") engine [[3]](#cite_note-3).

# Features

## [Board Representation](/Board_Representation "Board Representation")

- [6+2 Bitboard Board Definition](/Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition")
- [8x8 Board](/8x8_Board "8x8 Board")
- [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards")
- [BitScan by De Bruijn Multiplication](/BitScan#DeBruijnMultiplation "BitScan")
- [SWAR-Popcount](/Population_Count#SWARPopcount "Population Count")

## [Search](/Search "Search")

- [Fail Soft](/Fail-Soft "Fail-Soft") [Alpha-Beta](/Alpha-Beta "Alpha-Beta") with [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Quiescence Search](/Quiescence_Search "Quiescence Search") at [depth](/Depth "Depth") <= 0
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [PV-Table on Stack](/Triangular_PV-Table "Triangular PV-Table")
- [MVV/LVA](/MVV-LVA "MVV-LVA") for sorting [captures](/Captures "Captures")
- [History Heuristic](/History_Heuristic "History Heuristic")

## [Evaluation](/Evaluation "Evaluation")

- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")

# See also

- [Hamsters](/Hamsters "Hamsters")
- [Rodent](/Rodent "Rodent")

# Forum Posts

- [Sungorus 1.0](http://www.talkchess.com/forum/viewtopic.php?t=28490) by [Pablo Vazquez](/Pablo_Vazquez "Pablo Vazquez"), [CCC](/CCC "CCC"), June 18, 2009
- [Sungorus 1.0.1 : 1856](http://www.talkchess.com/forum/viewtopic.php?t=28550) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), June 21, 2009
- [Sungorus 1.1](http://www.talkchess.com/forum/viewtopic.php?t=28795) by [Pablo Vazquez](/Pablo_Vazquez "Pablo Vazquez"), [CCC](/CCC "CCC"), July 05, 2009
- [Sungorus 1.1 : 2167](http://www.talkchess.com/forum/viewtopic.php?t=28887) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), July 10, 2009
- [Sungorus 1.2](http://www.talkchess.com/forum/viewtopic.php?t=29271) by [Pablo Vazquez](/Pablo_Vazquez "Pablo Vazquez"), [CCC](/CCC "CCC"), August 06, 2009
- [Sungorus 1.2 : 2157](http://www.talkchess.com/forum/viewtopic.php?t=29302) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), August 08, 2009
- [Sungorus 1.3](http://www.talkchess.com/forum/viewtopic.php?t=32579) by [Pablo Vazquez](/Pablo_Vazquez "Pablo Vazquez"), [CCC](/CCC "CCC"), February 13, 2010
- [Sungorus 1.4](http://www.talkchess.com/forum/viewtopic.php?t=35217) by [Pablo Vazquez](/Pablo_Vazquez "Pablo Vazquez"), [CCC](/CCC "CCC"), June 30, 2010

# External Links

## Chess Engine

- [Sungorus 1.4 - download](https://sites.google.com/site/sungorus/)
- [Sungorus 1.4 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Sungorus%201.4%2064-bit) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Djungarian hamster (Phodopus sungorus) from Wikipedia](https://en.wikipedia.org/wiki/Djungarian_hamster)
- [Mongolian three-toed jerboa (Stylodipus sungorus) from Wikipedia](https://en.wikipedia.org/wiki/Mongolian_three-toed_jerboa)
- [Phodopus sungorus - Wikispecies](http://species.wikimedia.org/wiki/Phodopus_sungorus)

# References

1. [↑](#cite_ref-1) Djungarian hamster (Phodopus sungorus) named Świr eating [pumpkin (Cucurbita) seed](https://en.wikipedia.org/wiki/Pepita), Photo by Mar lena, April 09, 2012, [Djungarian hamster (Phodopus sungorus) from Wikipedia](https://en.wikipedia.org/wiki/Djungarian_hamster)
2. [↑](#cite_ref-2) [Sungorus 1.0](http://www.talkchess.com/forum/viewtopic.php?t=28490) by [Pablo Vazquez](/Pablo_Vazquez "Pablo Vazquez"), [CCC](/CCC "CCC"), June 18, 2009
3. [↑](#cite_ref-3) [open source gift for Christmas](http://www.talkchess.com/forum/viewtopic.php?t=41590) by [Pawel Koziol](/Pawel_Koziol "Pawel Koziol"), [CCC](/CCC "CCC"), December 25, 2011

**[Up one Level](/Engines "Engines")**