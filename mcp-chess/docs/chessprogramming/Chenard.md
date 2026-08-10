# Chenard

Source: https://www.chessprogramming.org/Chenard

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Chenard**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Bundesarchiv_Bild_183-2008-0516-500%2C_Fernschreibmaschine_mit_Telefonanschluss.jpg/330px-Bundesarchiv_Bild_183-2008-0516-500%2C_Fernschreibmaschine_mit_Telefonanschluss.jpg)](/File:Bundesarchiv_Bild_183-2008-0516-500,_Fernschreibmaschine_mit_Telefonanschluss.jpg)

Early Teletype [[1]](#cite_note-1)

**Chenard**,  
an [open source chess program](/Category:Open_Source "Category:Open Source") by [Don Cross](/Don_Cross "Don Cross"), written in [C++](/Cpp "Cpp"). Its development already started in 1993, and it is maintained and improved until the present.
The source code of the didactic program is well structured and documented, is in the [public domain](https://en.wikipedia.org/wiki/Public_domain) with attribution of author's name and web address required in distributed works [[2]](#cite_note-2).
A [Windows](/Windows "Windows") version comes with an own [GUI](/GUI "GUI"), other versions for [Windows](/Windows "Windows") and [Linux](/Linux "Linux") support the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](/WinBoard "WinBoard") or [XBoard](/XBoard "XBoard"), its own native [command line interface](/CLI "CLI"), or [teletype](https://en.wikipedia.org/wiki/Teleprinter) chess.

# Description

Chenard provides a [genetic algorithm](/Genetic_Programming#GeneticAlgorithm "Genetic Programming") framework for evolving [move ordering](/Move_Ordering "Move Ordering") and [evaluation](/Evaluation "Evaluation") heuristics.
The [board is represented](/Board_Representation "Board Representation") by a [12x12 mailbox](/Mailbox "Mailbox") with [disjoint piece flag encoding](/Pieces#DisjointPieceFlags "Pieces").
Since Chenard isn't [negamaxing](/Negamax "Negamax"), [search](/Search "Search"), evaluation as well as [move generation](/Move_Generation "Move Generation") routines are implemented separately for White and Black.

## Search

Chenard's [search](/Search "Search") is pure [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table"),
despite [quiescence search](/Quiescence_Search "Quiescence Search") and its top layer with [checks](/Quiescence_Search#Checks "Quiescence Search"),
without any [selectivity](/Selectivity "Selectivity") in form of [extensions](/Extensions "Extensions"), [forward pruning](/Pruning "Pruning") and [reductions](/Reductions "Reductions").
The [root](/Root "Root") search implements [iterative deepening](/Iterative_Deepening "Iterative Deepening") without [aspiration windows](/Aspiration_Windows "Aspiration Windows").
The [depth](/Depth "Depth") parameter, suited to index a [ply](/Ply "Ply") [stack](/Stack "Stack"), starts at the root with zero and is incremented through the indirect [recursive](/Recursion "Recursion") function calls until the the maximum depth, dubbed level, is reached and quiescence is called [[3]](#cite_note-3).

## Evaluation

The [evaluation](/Evaluation "Evaluation") looks sophisticated considering a bunch of features, many part of Chenard's genes.
Beside the aggregation of [material](/Material "Material"), imbalance terms and [piece-square tables](/Piece-Square_Tables "Piece-Square Tables"),
which decides on an early exit aka [lazy evaluation](/Lazy_Evaluation "Lazy Evaluation"), Chenard looks at [immobile](/Trapped_Pieces "Trapped Pieces") and [connected](/Connectivity "Connectivity") pieces,
along with various [piece specific evaluation features](/Evaluation_of_Pieces "Evaluation of Pieces"), and further takes [pawn structure](/Pawn_Structure "Pawn Structure") with focus on [passed pawns](/Passed_Pawn "Passed Pawn"), [king safety](/King_Safety "King Safety"), and even [tactical motives](/Tactics "Tactics") such as [pinned pieces](/Pin "Pin") and [forks](/Double_Attack "Double Attack") into account.
Beside, Chenard has a [mop-up evaluation](/index.php?title=Mop-up_evaluation&action=edit&redlink=1 "Mop-up evaluation (page does not exist)") for late endgames like [KBNK](/KBNK_Endgame "KBNK Endgame").

## EGDB

Chenard has its own [depth to mate](/Endgame_Tablebases#DTM "Endgame Tablebases") [endgame databases](/Endgame_Tablebases "Endgame Tablebases"), generator and probing code [[4]](#cite_note-4) [[5]](#cite_note-5) [[6]](#cite_note-6).

# Screen Shot

[![Chenard screen shot.jpg](/images/5/58/Chenard_screen_shot.jpg)](http://cosinekitty.com/chenard/)

Chenard's [Windows](/Windows "Windows") [GUI](/GUI "GUI") [[7]](#cite_note-7)

# See also

- [Flywheel](/index.php?title=Flywheel&action=edit&redlink=1 "Flywheel (page does not exist)")

# Forum Posts

- [Chenard 1.136 with Winboard support available](http://www.talkchess.com/forum/viewtopic.php?t=20846) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [CCC](/CCC "CCC"), April 26, 2008
- [Chenard 1.1.40 JA](http://www.talkchess.com/forum/viewtopic.php?t=21252) by [Harun Taner](/Harun_Taner "Harun Taner"), [CCC](/CCC "CCC"), May 20, 2008
- [Chenard](http://www.talkchess.com/forum/viewtopic.php?t=29749) by [Gabor Szots](/Gabor_Szots "Gabor Szots"), [CCC](/CCC "CCC"), September 14, 2009
- [an oldy but goody, Chenard for the Mac - xBoard with source](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=61386) by [MikeB](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), September 10, 2016

# External Links

## Chess Program

- [Chenard - a freeware chess program](http://cosinekitty.com/chenard/) by [Don Cross](/Don_Cross "Don Cross")
- [cosinekitty/chenard · GitHub](https://github.com/cosinekitty/chenard)
- [Chenard](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Chenard&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/4](/CCRL "CCRL")

## Misc

- [Chenard-Walcker from Wikipedia](https://en.wikipedia.org/wiki/Chenard-Walcker)
- [Louis Chenard from Wikipedia](https://en.wikipedia.org/wiki/Louis_Chenard)

# References

1. [↑](#cite_ref-1) [A Creed Model 7 teleprinter in 1930](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-2008-0516-500,_Fernschreibmaschine_mit_Telefonanschluss.jpg?uselang=en), Photo by Willi Illger, [Bundesarchiv](https://commons.wikimedia.org/wiki/Commons:Bundesarchiv), [Bild 183-2008-0516-500](https://www.bild.bundesarchiv.de/dba/de/search/?query=Bild+183-2008-0516-500), [CC BY-SA 3.0 DE](https://creativecommons.org/licenses/by-sa/3.0/de/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Fernschreiber - Wikipedia.de](https://de.wikipedia.org/wiki/Fernschreiber)
2. [↑](#cite_ref-2) [Chenard - a freeware chess program](http://cosinekitty.com/chenard/) by [Don Cross](/Don_Cross "Don Cross")
3. [↑](#cite_ref-3) [chenard/search.cpp at master · cosinekitty/chenard · GitHub](https://github.com/cosinekitty/chenard/blob/master/src/search.cpp)
4. [↑](#cite_ref-4) [GitHub - cosinekitty/endgame: Chess endgame database generator](https://github.com/cosinekitty/endgame)
5. [↑](#cite_ref-5) [chenard/egdbase.cpp at master · cosinekitty/chenard · GitHub](https://github.com/cosinekitty/chenard/blob/master/src/egdbase.cpp)
6. [↑](#cite_ref-6) [Build Your Own Chess Endgame Monster - Level Up Coding](https://levelup.gitconnected.com/build-your-own-chess-endgame-monster-a3fb23bb3ec1) by [Don Cross](/Don_Cross "Don Cross"), February 17, 2020
7. [↑](#cite_ref-7) [Chenard - a freeware chess program](http://cosinekitty.com/chenard/) by [Don Cross](/Don_Cross "Don Cross")

**[Up one Level](/Engines "Engines")**