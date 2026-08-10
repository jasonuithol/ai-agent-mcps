# Rival

Source: https://www.chessprogramming.org/Rival

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Rival**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Ye_Eifl_%40_sunset.jpg/330px-Ye_Eifl_%40_sunset.jpg)](/File:Ye_Eifl_@_sunset.jpg)

The Rivals [[1]](#cite_note-1)

**Rival**, (Rival Chess, NewRival)  
a chess engine by [Chris Moreton](/Chris_Moreton "Chris Moreton") and [Russell Newman](/Russell_Newman "Russell Newman"), written in [C++](/Cpp "Cpp"), starting in 1992 as [MS-DOS](/MS-DOS "MS-DOS") program with an own [GUI](/GUI "GUI"),
before being rewritten for [Windows](/Windows "Windows") as [WinBoard](/WinBoard "WinBoard") compatible engine (NewRival) a couple of years later
[[2]](#cite_note-2).
The [UCI](/UCI "UCI") protocol was implemented in 2006 as *Rival UCI 1.18 for Windows*, while the current Rival engine was ported to [Java](/Java "Java") as used in the [Android](/Android "Android") application.
DOS and Windows versions are available as source code [[3]](#cite_note-3).
Further, Rival is able to play various [chess variants](/Chess#Variants "Chess") like [Kinglet](/index.php?title=Kinglet&action=edit&redlink=1 "Kinglet (page does not exist)"), [Losing Chess](/Losing_Chess "Losing Chess"), and [Shatranj](/Shatranj "Shatranj")
[[4]](#cite_note-4).

# Description

Rival is described in detail on the *redhotpawn* sites [[5]](#cite_note-5).
Rival for Java uses [bitboards](/Bitboards "Bitboards") with [big-endian rank-file](/Bibob#BERF "Bibob") [mapping](/Square_Mapping_Considerations "Square Mapping Considerations").
It determines [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") with [magic bitboards](/Magic_Bitboards "Magic Bitboards") [[6]](#cite_note-6) [[7]](#cite_note-7).

## Search

Rival applies [PVS](/Principal_Variation_Search "Principal Variation Search") [negamax](/Negamax "Negamax") [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table"), [killer heuristic](/Killer_Heuristic "Killer Heuristic") and [quiescence](/Quiescence_Search "Quiescence Search") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework.

## Evaluation

The [evaluation function](/Evaluation "Evaluation") calculates [scores](/Score "Score") of both sides, and returns the score difference of the [side to move](/Side_to_move "Side to move") minus the side not on the move in [negamax](/Negamax "Negamax") manner,
considering [pawn structure](/Pawn_Structure "Pawn Structure"), various [piece terms](/Evaluation_of_Pieces "Evaluation of Pieces"), and [king safety](/King_Safety "King Safety").
A quote from Rival's *Static Board Evaluation* site [[8]](#cite_note-8):

```
The factors considered in the evaluation function have been chosen because they are relatively quick to calculate. Very few of the ideas are entirely original; many represent elementary chess knowledge and many have been used in other chess programs. Sources that have been of particular influence are Slate & Atkin (1977) [9], Newborn (1975) [10] and Hyatt et al (1985) [11]. Some of the factors have been added to overcome certain weaknesses that the program has shown, others have been left out in the hope that the gain in search speed would outweigh the loss in evaluation quality. The work of Berliner et al (1990) [12] suggests the opposite to the last assumption.
```

# Sreenshots

## DOS & Windows

[[13]](#cite_note-Rival-13)

|  |  |
| --- | --- |
| [Rivaldos.jpg](/File:Rivaldos.jpg) | [Rivalwin.jpg](/File:Rivalwin.jpg) |
| Rival for [DOS](/MS-DOS "MS-DOS") | Rival for [Windows](/Windows "Windows") |

## Android

[![RivalForAndroid.jpg](/images/0/03/RivalForAndroid.jpg)](/File:RivalForAndroid.jpg)

JavaRival, [UCI](/UCI "UCI") engine for [Android](/Android "Android") [[13]](#cite_note-Rival-13)

# Forum Posts

- [Rival Chess 1.5.041](https://groups.google.com/g/rec.games.chess.computer/c/3Xd8OM2Pwec/m/FTelUbCcPS4J) by [Chris Moreton](/Chris_Moreton "Chris Moreton"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), November 03, 1998
- [Rival Chess](https://groups.google.com/d/msg/rec.games.chess.computer/0iOoI8YNLXQ/t-xX9U1kiEgJ) by [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), November 04, 1998
- [History Heuristic on its own](https://www.stmintz.com/ccc/index.php?id=39692) by [Chris Moreton](/Chris_Moreton "Chris Moreton"), [CCC](/CCC "CCC"), January 16, 1999 » [History Heuristic](/History_Heuristic "History Heuristic")
- [Rival Chess advances to Winboard Championships!](https://www.stmintz.com/ccc/index.php?id=103229) by Daniel Chancey, [CCC](/CCC "CCC"), March 24, 2000
- [Rival Chess 1.0.1 and 1.0.3](http://www.talkchess.com/forum/viewtopic.php?t=64754) by [Tony Mokonen](/index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](/CCC "CCC"), July 29, 2017

# External Links

## Chess Engine

- [Rival Chess - Red Hot Pawn](https://www.redhotpawn.com/rival/)
- [GitHub - chris-moreton/rival-chess-android-engine](https://github.com/chris-moreton/rival-chess-android-engine)
- [GitHub - chris-moreton/rival-chess-dos](https://github.com/chris-moreton/rival-chess-dos)
- [Rival Chess Engine](http://web.archive.org/web/20160313201136/http://www.rivalchess.com/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Rival Chess Engine - Magic Bitboards](http://web.archive.org/web/20160304114223/http://www.rivalchess.com/magic-bitboards/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Rival Chess Free - Android Apps on Google Play](https://play.google.com/store/apps/details?id=com.netadapt.rivalchess&hl=en)
- [Rival](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Rival&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")
- [Defending Humanity's Honor](https://timkr.home.xs4all.nl/chess2/honor.htm) by [Tim Krabbé](https://en.wikipedia.org/wiki/Tim_Krabb%C3%A9), see game NewRival - [Faile](/Faile "Faile") with 493 moves, and playing 402 moves with bare kings!

## Chess Programming

- [Introduction](https://www.redhotpawn.com/rival/programming/index.php)

:   [Negamax](https://www.redhotpawn.com/rival/programming/negamax.php)
:   [Alpha-Beta Pruning](https://www.redhotpawn.com/rival/programming/alphabeta.php)
:   [Move Ordering](https://www.redhotpawn.com/rival/programming/moveorder.php)
:   [Quiescence](https://www.redhotpawn.com/rival/programming/quiescence.php)
:   [Transposition/Refutation Tables](https://www.redhotpawn.com/rival/programming/transref.php)
:   [Killer Heuristics](https://www.redhotpawn.com/rival/programming/killers.php)
:   [Minimal Window](https://www.redhotpawn.com/rival/programming/minwin.php)
:   [Timing Moves](https://www.redhotpawn.com/rival/programming/timing.php)
:   [Draw Scoring](https://www.redhotpawn.com/rival/programming/draws.php)
:   [Static Board Evaluation](https://www.redhotpawn.com/rival/programming/evaluation.php)
:   [Openings](https://www.redhotpawn.com/rival/programming/openings.php)

- [Understanding magic bitboards in chess programming](http://web.archive.org/web/20160314001240/http://www.afewmorelines.com/understanding-magic-bitboards-in-chess-programming/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)) by [Chris Moreton](/Chris_Moreton "Chris Moreton") in his programming blog, August 07, 2013

## Misc

- [rival - Wiktionary](https://en.wiktionary.org/wiki/rival)
- [Rival (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Rival)
- [Rivals (Star Trek: Deep Space Nine) from Wikipedia](https://en.wikipedia.org/wiki/Rivals_%28Star_Trek:_Deep_Space_Nine%29)
- [Yr Eifl - The Rivals from Wikipedia](https://en.wikipedia.org/wiki/Yr_Eifl)

# References

1. [↑](#cite_ref-1) [Yr Eifl](https://en.wikipedia.org/wiki/Yr_Eifl) from [Llandegfan](https://en.wikipedia.org/wiki/Llandegfan) at sunset, [Image](https://commons.wikimedia.org/wiki/File:Ye_Eifl_@_sunset.jpg) by Velela, February 21, 2005, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Rival Chess Engine - About](http://web.archive.org/web/20160313201136/http://www.rivalchess.com/about/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
3. [↑](#cite_ref-3) [Rival Chess - Red Hot Pawn](https://www.redhotpawn.com/rival/)
4. [↑](#cite_ref-4) [The Chess Variant Pages: Computer resources](https://www.chessvariants.com/icomputer.html)
5. [↑](#cite_ref-5) [Introduction](https://www.redhotpawn.com/rival/programming/index.php)
6. [↑](#cite_ref-6) [Rival Chess Engine - Magic Bitboards](http://web.archive.org/web/20160304114223/http://www.rivalchess.com/magic-bitboards/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
7. [↑](#cite_ref-7) [Understanding magic bitboards in chess programming](http://web.archive.org/web/20160314001240/http://www.afewmorelines.com/understanding-magic-bitboards-in-chess-programming/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)) by [Chris Moreton](/Chris_Moreton "Chris Moreton") in his programming blog, August 07, 2013
8. [↑](#cite_ref-8) [Rival Chess Engine - Static Board Evaluation](https://www.redhotpawn.com/rival/programming/evaluation.php)
9. [↑](#cite_ref-9) [David Slate](/David_Slate "David Slate"), [Larry Atkin](/Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](/Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium") » [Chess 4.5](/Chess_(Program) "Chess (Program)")
10. [↑](#cite_ref-10) [Monroe Newborn](/Monroe_Newborn "Monroe Newborn") (**1975**). *Computer Chess*. Academic Press » [Ostrich](/Ostrich "Ostrich")
11. [↑](#cite_ref-11) [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [Albert Gower](/Albert_Gower "Albert Gower"), [Harry Nelson](/Harry_Nelson "Harry Nelson") (**1985**). *Cray Blitz*. [Advances in Computer Chess 4](/Advances_in_Computer_Chess_4 "Advances in Computer Chess 4") » [Cray Blitz](/Cray_Blitz "Cray Blitz")
12. [↑](#cite_ref-12) [Hans Berliner](/Hans_Berliner "Hans Berliner"), [Gordon Goetsch](/Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](/Murray_Campbell "Murray Campbell"), [Carl Ebeling](/Carl_Ebeling "Carl Ebeling") (**1990**). *Measuring the Performance Potential of Chess Programs.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, pp. 7-21 » [HiTech](/HiTech "HiTech")
13. ↑ [13.0](#cite_ref-Rival_13-0) [13.1](#cite_ref-Rival_13-1) [Rival Chess](https://www.redhotpawn.com/rival/)

**[Up one level](/Engines "Engines")**