# Wing

Source: https://www.chessprogramming.org/Wing

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Wing**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Lift-force-en.svg/330px-Lift-force-en.svg.png)](/File:Lift-force-en.svg)

Forces acting on a wing [[1]](#cite_note-1)

**Wing**,  
a [WinBoard](/WinBoard "WinBoard") compliant chess engine by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)") written in [C++](/Cpp "Cpp"), first released in October 2004. Initially influenced by [Crafty](/Crafty "Crafty") [[2]](#cite_note-2), Wing was released as [open source](/Category:Open_Source "Category:Open Source") in December 2010 to demonstrate the basics of chess programming [[3]](#cite_note-3), shortly before Stef Luijten started his [Winglet](/Winglet "Winglet") tutorial *Writing a Chess Program in 99 Steps* [[4]](#cite_note-4).

# Description

## Board Representation

Wing is a [bitboard](/Bitboards "Bitboards") engine and determines [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") using [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards"). The [inner six bits](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks") optimization yields to four lookup tables of 64x64x8 bytes, that is 32-KiB each or 1/8 MiB in total for [ranks](/Ranks "Ranks"), [files](/Files "Files"), [diagonals](/Diagonals "Diagonals") and [anti-diagonals](/Anti-Diagonals "Anti-Diagonals"). Interestingly, this attack table layout was preserved in [Winglet](/Winglet "Winglet"), when line-wise occupied states were [rotated](/Flipping_Mirroring_and_Rotating#RankFileAndDiagonal "Flipping Mirroring and Rotating") on the fly by [magic multiplication](/Magic_Bitboards "Magic Bitboards") and shift right.

## Search

Wing performs a [negamax](/Negamax "Negamax") [alpha-beta](/Alpha-Beta "Alpha-Beta") [search](/Search "Search") with conditional compiled (default on) [PVS](/Principal_Variation_Search "Principal Variation Search") inside the [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework without [aspiration windows](/Aspiration_Windows "Aspiration Windows"). The recent version has a [always replace](/Transposition_Table#ReplacementStrategies "Transposition Table") [transposition table](/Transposition_Table "Transposition Table") using [Zobrist keys](/Zobrist_Hashing "Zobrist Hashing"), while earlier versions used an additional [depth-preferred replacement table](/Transposition_Table#ReplacementStrategies "Transposition Table") [[5]](#cite_note-5). As stated by its author in 2006, Wing has gained over 100 ELO points from adding [history pruning](/Late_Move_Reductions "Late Move Reductions") [[6]](#cite_note-6), while the published sources lack LMR.

### [Selectivity](/Selectivity "Selectivity")

- [Check Extensions](/Check_Extensions "Check Extensions")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Recapture Extensions](/Recapture_Extensions "Recapture Extensions")
- [Passed Pawn Extensions](/Passed_Pawn_Extensions "Passed Pawn Extensions")
- [Threat Extensions](/Mate_Threat_Extensions "Mate Threat Extensions")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Extended Futility Pruning](/Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
- [Razoring](/Razoring "Razoring")

### [Move Ordering](/Move_Ordering "Move Ordering")

- [Principal Variation Extraction from TT](/Principal_Variation "Principal Variation")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [History Heuristic](/History_Heuristic "History Heuristic")
- [MVV-LVA](/MVV-LVA "MVV-LVA")

## [Evaluation](/Evaluation "Evaluation")

- [Material Balance](/Material#Balance "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Development](/Development "Development")
- [Mobility](/Mobility "Mobility")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")

:   [Backward Pawn](/Backward_Pawn "Backward Pawn")
:   [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
:   [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
:   [Passed Pawn](/Passed_Pawn "Passed Pawn")
:   [Connected Passed Pawns](/Connected_Passed_Pawns "Connected Passed Pawns")

- [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
- [Bishop Pair](/Bishop_Pair "Bishop Pair")
- [Rook on Open File](/Rook_on_Open_File "Rook on Open File")
- [King Safety](/King_Safety "King Safety") in [Opening](/Opening "Opening"), [Middlegame](/Middlegame "Middlegame")

:   [Pawn Shield](/King_Safety#PawnShield "King Safety")
:   [King Tropism](/King_Safety#KingTropism "King Safety")

- [King Centralization](/King_Centralization "King Centralization") in [Endgame](/Endgame "Endgame")

# See also

- [Crafty](/Crafty "Crafty")
- [Little Wing](/Little_Wing "Little Wing")
- [Winglet](/Winglet "Winglet")

# Forum Posts

- [Wing exit from Winboard!](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=378) by Pablo, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), October 25, 2004
- [wing engine files](https://www.stmintz.com/ccc/index.php?id=459128) by Adam Wilks, [CCC](/CCC "CCC")], November 01, 2005
- [Hash table hit rate](http://www.open-aurec.com/wbforum/viewtopic.php?t=3838) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 16, 2005 » [Transposition Table](/Transposition_Table "Transposition Table")
- [Re: history pruning/ late move pruning](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4435&p=23032#p23032) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 02, 2006

# External Links

## Chess Engine

- [Wing](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Wing&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) from [CCRL 40/4](/CCRL "CCRL")
- [Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Index of /chess/engines/Jim Ablett/WING](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/WING/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")

## Chess

- [Wing Gambit from Wikipedia](https://en.wikipedia.org/wiki/Wing_Gambit)

## Misc

- [Wing from Wikipedia](https://en.wikipedia.org/wiki/Wing)
- [Wing (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Wing_%28disambiguation%29)
- [Wing (building) from Wikipedia](https://en.wikipedia.org/wiki/Wing_%28building%29)
- [Focus](/Category:Focus "Category:Focus") - [Angle Wings](http://www.focustheband.com/focusdisc.htm), Live at [Old Grey Whistle Test](https://en.wikipedia.org/wiki/The_Old_Grey_Whistle_Test) 1976, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   Line-up: [Thijs van Leer](https://en.wikipedia.org/wiki/Thijs_van_Leer), [Philip Catherine](/Category:Philip_Catherine "Category:Philip Catherine"), [Bert Ruiter](https://en.wikipedia.org/wiki/Bert_Ruiter), [David Kemper](https://en.wikipedia.org/wiki/David_Kemper)

# References

1. [↑](#cite_ref-1) [Forces](https://en.wikipedia.org/wiki/Force) acting on a [wing](https://en.wikipedia.org/wiki/Wing), [thrust](https://en.wikipedia.org/wiki/Thrust), [lift](https://en.wikipedia.org/wiki/Lift_%28force%29), [drag](https://en.wikipedia.org/wiki/Drag_%28physics%29), and [weight](https://en.wikipedia.org/wiki/Weight), Image by Bartosz Kosiorek, [Bird flight from Wikipedia](https://en.wikipedia.org/wiki/Bird_flight), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Chess Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:chess_engine_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
3. [↑](#cite_ref-3) [Index of /chess/engines/Jim Ablett/WING](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/WING/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
4. [↑](#cite_ref-4) [Winglet, Writing a Chess Program in 99 Steps](http://web.archive.org/web/20120621100214/http://www.sluijten.com/winglet/) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), hosted by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
5. [↑](#cite_ref-5) [Hash table hit rate](http://www.open-aurec.com/wbforum/viewtopic.php?t=3838) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 16, 2005
6. [↑](#cite_ref-6) [Re: history pruning/ late move pruning](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4435&p=23032#p23032) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 02, 2006

**[Up one Level](/Engines "Engines")**