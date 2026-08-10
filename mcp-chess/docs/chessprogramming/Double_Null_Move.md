# Double Null Move

Source: https://www.chessprogramming.org/Double_Null_Move

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Pruning](/Pruning "Pruning") \* [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning") \* Double Null Move**

**Double Null Move**,  
a Null Move Pruning technique proposed by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen") in 1997 [[1]](#cite_note-1), that allows two consecutive [null moves](/Null_Move "Null Move") with common [depth reduction R](/Depth_Reduction_R "Depth Reduction R") in a row. Provided that the [depth](/Depth "Depth") or distance to the horizon is big enough to recognize a possible [zugzwang](/Zugzwang "Zugzwang") 2R+2 plies shallower, and the first null move is refuted by the second one, its aim is to make NMH zugzwang aware. Double Null Move is used in [Diep](/Diep "Diep") [[2]](#cite_note-2), and was widely discussed in [computer chess forums](/Computer_Chess_Forums "Computer Chess Forums") [[3]](#cite_note-3), and overall recognized as a great idea [[4]](#cite_note-4) . While likely too expensive in the [middlegame](/Middlegame "Middlegame") where zugzwang is rare, and still not recommend for [pawn endings](/Pawn_Endgame "Pawn Endgame") [[5]](#cite_note-5), it might be well applied in other [endgames](/Endgame "Endgame").

# See also

- [Fail-High Reductions](/Fail-High_Reductions "Fail-High Reductions")
- [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Null Move](/Null_Move "Null Move")
- [Null Move Observation](/Null_Move_Observation "Null Move Observation")
- [Null Move Reductions](/Null_Move_Reductions "Null Move Reductions")
- [Null Move Test-Positions](/Null_Move_Test-Positions "Null Move Test-Positions"), where Null Move may fail due to zugzwang
- [Zugzwang](/Zugzwang "Zugzwang")
- [Zugzwang Verification](/Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")

# Forum Posts

- [Re: Null move?](https://groups.google.com/d/msg/rec.games.chess.computer/PrN_AXwYV_4/UXU5x67UaoQJ) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 11, 1997
- [Searching correctly with the Nullmove ==> no zugzwang problems anymore](https://groups.google.com/d/msg/rec.games.chess.computer/i4NWIfd5CWc/InTKKFrT8YsJ) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 23, 1997
- [Pseudo C code for double nullmove + PVS](https://www.stmintz.com/ccc/index.php?id=123156) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), August 06, 2000
- [Double Nullmove](https://www.stmintz.com/ccc/index.php?id=160954) by [David Rasmussen](/David_Rasmussen "David Rasmussen"), [CCC](/CCC "CCC"), March 30, 2001
- [Double Null move?](https://www.stmintz.com/ccc/index.php?id=179604) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), July 13, 2001
- [Double Nullmove](https://www.stmintz.com/ccc/index.php?id=225990) by [Andreas Herrmann](/Andreas_Herrmann "Andreas Herrmann"), [CCC](/CCC "CCC"), April 25, 2002
- [double null move help](https://www.stmintz.com/ccc/index.php?id=373804) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), July 04, 2004
- [Re: Search-algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=283903&t=29176) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), August 01, 2009

:   [Re: Search-algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=283906&t=29176) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), August 01, 2009

- [Why not two consecutive null moves ?](http://www.talkchess.com/forum/viewtopic.php?t=56272) by [Henk van den Belt](/index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](/CCC "CCC"), May 07, 2015

# References

1. [↑](#cite_ref-1) [Re: Null move?](https://groups.google.com/d/msg/rec.games.chess.computer/PrN_AXwYV_4/UXU5x67UaoQJ) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 11, 1997
2. [↑](#cite_ref-2) [Pseudo C code for double nullmove + PVS](https://www.stmintz.com/ccc/index.php?id=123156) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), August 06, 2000
3. [↑](#cite_ref-3) [Searching correctly with the Nullmove ==> no zugzwang problems anymore](https://groups.google.com/d/msg/rec.games.chess.computer/i4NWIfd5CWc/InTKKFrT8YsJ) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 23, 1997
4. [↑](#cite_ref-4) [Re: Double Nullmove](https://www.stmintz.com/ccc/index.php?id=161000) by [James Swafford](/James_Swafford "James Swafford"), [CCC](/CCC "CCC"), March 30, 2001
5. [↑](#cite_ref-5) [Re: double nullmove??](https://www.stmintz.com/ccc/index.php?id=123223) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), August 06, 2000

**[Up one level](/Null_Move_Pruning "Null Move Pruning")**