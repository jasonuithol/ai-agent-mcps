# Vapor

Source: https://www.chessprogramming.org/Vapor

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Vapor**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Phase-diag2.svg/330px-Phase-diag2.svg.png)](/File:Phase-diag2.svg)

Pressure-Temperature Phase Diagram [[1]](#cite_note-1)

**Vapor**, (Vapor Chess)  
an [UCI](/UCI "UCI") compliant chess engine by [Mike Leany](/Mike_Leany "Mike Leany"), written in [C](/C "C"), since October 2010 no longer [vaporware](https://en.wikipedia.org/wiki/Vaporware) [[2]](#cite_note-2), and since November 2019 published as [open source](/Category:Open_Source "Category:Open Source") on [GitHub](https://en.wikipedia.org/wiki/GitHub) [[3]](#cite_note-3).

# Description

Vapor is a rudimentary, didactic engine and lacks state of the art [search](/Search "Search") techniques and [evaluation](/Evaluation "Evaluation") terms.
It [represents the board](/Board_Representation "Board Representation") with a [little-endian file-rank mapped](/Square_Mapping_Considerations#LittleEndianFileRankMapping "Square Mapping Considerations") [bitboard definition](/Bitboard_Board-Definition "Bitboard Board-Definition"),
and applies [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") [[4]](#cite_note-4).
Search is plain [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table"), [check extension](/Check_Extensions "Check Extensions") and [quiescence](/Quiescence_Search "Quiescence Search") inside the [iterative deepening](/Iterative_Deepening "Iterative Deepening") loop [[5]](#cite_note-5),
considering [material](/Material "Material") and [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") for [pawns](/Pawn "Pawn") and [knights](/Knight "Knight") as [evaluation](/Evaluation "Evaluation") terms at the [leaves](/Leaf_Node "Leaf Node") [[6]](#cite_note-6).

# See also

- [Zilch](/Zilch "Zilch")
- [Tinman](/Tinman "Tinman")

# Postings

- [Vaporware No More - Vapor Chess](http://vapor.mikeleany.com/home/vaporwarenomore) by [Mike Leany](/Mike_Leany "Mike Leany"), October 11, 2010
- [Vapor Chess v0.02 Release for Linux](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=44755) by [Mike Leany](/Mike_Leany "Mike Leany"), [CCC](/CCC "CCC"), August 10, 2012
- [Source Code Released](http://vapor.mikeleany.com/home/sourcecodereleased) by [Mike Leany](/Mike_Leany "Mike Leany"), November 09, 2019

# External Links

## Chess Engine

- [GitHub - mikeleany/vapor: My old chess engine written in C](https://github.com/mikeleany/vapor)
- [Vapor Chess](http://vapor.mikeleany.com/)
- [Vapor](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Vapor%200.01r12#Vapor_0_01r12) in [CCRL Blitz](/CCRL "CCRL")

## Misc

- [vapor - Wiktionary](https://en.wiktionary.org/wiki/vapor)
- [Vapor from Wikipedia](https://en.wikipedia.org/wiki/Vapor)
- [Vapor (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Vapor_(disambiguation))
- [U-Foes, Vapor (Marvel Comics) from Wikipedia](https://en.wikipedia.org/wiki/U-Foes)
- [from Wikipedia](https://en.wikipedia.org/wiki/Vaporware)
- [Soulive](https://en.wikipedia.org/wiki/Soulive) - [Vapor](https://en.wikipedia.org/wiki/Break_Out_(Soulive_album)), [Brooklyn Bowl](https://en.wikipedia.org/wiki/Brooklyn_Bowl), March 19, 2014, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) The [vapor-liquid critical point](https://en.wikipedia.org/wiki/Critical_point_(thermodynamics)) in a [pressure](https://en.wikipedia.org/wiki/Pressure)-[temperature](https://en.wikipedia.org/wiki/Temperature) [phase diagram](https://en.wikipedia.org/wiki/Phase_diagram) is at the high-temperature extreme of the [liquid–gas phase boundary](https://en.wikipedia.org/wiki/Supercritical_liquid%E2%80%93gas_boundaries) (The dotted green line gives the [anomalous behaviour of water](https://en.wikipedia.org/wiki/Superheated_water#Explanation_of_anomalous_behaviour)). Image by Matthieumarechal, January 28, 2008, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Vaporware No More - Vapor Chess](http://vapor.mikeleany.com/home/vaporwarenomore) by [Mike Leany](/Mike_Leany "Mike Leany"), October 11, 2010
3. [↑](#cite_ref-3) [Source Code Released](http://vapor.mikeleany.com/home/sourcecodereleased) by [Mike Leany](/Mike_Leany "Mike Leany"), November 09, 2019
4. [↑](#cite_ref-4) [vapor/moves.h at master · mikeleany/vapor · GitHub](https://github.com/mikeleany/vapor/blob/master/src/moves.h)
5. [↑](#cite_ref-5) [vapor/search.c at master · mikeleany/vapor · GitHub](https://github.com/mikeleany/vapor/blob/master/src/search.c)
6. [↑](#cite_ref-6) [vapor/eval.c at master · mikeleany/vapor · GitHub](https://github.com/mikeleany/vapor/blob/master/src/eval.c)

**[Up one level](/Engines "Engines")**