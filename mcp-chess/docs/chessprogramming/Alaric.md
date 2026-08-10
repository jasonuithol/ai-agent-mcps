# Alaric

Source: https://www.chessprogramming.org/Alaric

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Alaric**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Alarich_steel_engraving.jpg/330px-Alarich_steel_engraving.jpg)](/File:Alarich_steel_engraving.jpg)

Alaric I [[1]](#cite_note-1)

**Alaric**, (TerraPi)  
a [WinBoard](/WinBoard "WinBoard") and [UCI](/UCI "UCI") compliant chess engine by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), written in [C++](/Cpp "Cpp"). Its development started in 2004, when Peter decided to stop with his previous engine [Terra](/Terra "Terra") and start all over with a new engine [[2]](#cite_note-2).

# Description

Alaric uses both [bitboards](/Bitboards "Bitboards") and other structures to [represent the board](/Board_Representation "Board Representation") and to [generate moves](/Move_Generation "Move Generation"),
and further utilizes [transposition table](/Transposition_Table "Transposition Table"), [pawn hash table](/Pawn_Hash_Table "Pawn Hash Table"), [history tables](/History_Heuristic "History Heuristic"), and two [killer slots](/Killer_Heuristic "Killer Heuristic") per [ply](/Ply "Ply").
Inside its [principal variation search](/Principal_Variation_Search "Principal Variation Search") with [null move pruning](/Null_Move_Pruning "Null Move Pruning"),
a precise prediction of [node types](/Node_Types "Node Types") takes place in order to guide the [search](/Search "Search") [[3]](#cite_note-3).

# Etymology

The chess engine Alaric is named after [Alaric I](https://en.wikipedia.org/wiki/Alaric_I) (around 370 – 410 [AD](https://en.wikipedia.org/wiki/Anno_Domini)), [King](https://en.wikipedia.org/wiki/Germanic_kingship) of the [Visigoths](https://en.wikipedia.org/wiki/Visigoths) from 395, who managed to walk with his forces right through the [Roman empire](https://en.wikipedia.org/wiki/Roman_Empire), invaded [Italy](https://en.wikipedia.org/wiki/Italy_%28Roman_Empire%29) and [sacked Rome](https://en.wikipedia.org/wiki/Sack_of_Rome_%28410%29) in 410. Before that in the year 394 he served as a leader of [Germanic](https://en.wikipedia.org/wiki/Gothic) troops under Roman command of [Theodosius I](https://en.wikipedia.org/wiki/Theodosius_I) but wasn't happy with how the [Goths](https://en.wikipedia.org/wiki/Goths) were treated [[4]](#cite_note-4).

# Tournament Play

Alaric played the [CCT9](/CCT9 "CCT9") with a result of 3½/7, and, under the handle **TerraPi**, a successful [WCRCC 2007](/WCRCC_2007 "WCRCC 2007"), becoming 6th with 8½/14 [[5]](#cite_note-5). One year later, at the [WCRCC 2008](/WCRCC_2008 "WCRCC 2008"), Alaric even became 4th with 9½/14 [[6]](#cite_note-6). Alaric's [opening book](/Opening_Book "Opening Book") was [cooked](/index.php?title=Opening_Book_Authors&action=edit&redlink=1 "Opening Book Authors (page does not exist)") by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon") [[7]](#cite_note-7).

# Selected Games

## CCT9

[CCT9](/CCT9 "CCT9"), [Buzz](/Buzz "Buzz") - Alaric [[8]](#cite_note-8)

```
[Event "CCT9"]
[Site "Internet Chess Club"]
[Date "2007.02.17"]
[Round "?"]
[White "Buzz"]
[Black "Alaric"]
[Result "0-1"]

1.c4 e6 2.d4 c5 3.d5 exd5 4.cxd5 Nf6 5.Nc3 d6 6.e4 Be7 7.Be2 Qa5 8.Kf1 O-O 
9.f4 Na6 10.e5 Ne8 11.a3 Qc7 12.Nf3 Bg4 13.Bxa6 bxa6 14.exd6 Nxd6 15.h3 Bd7 
16.g4 Bf6 17.Kg2 Rfe8 18.Re1 Rxe1 19.Nxe1 Re8 20.Nd3 Nc4 21.Qf3 Bd4 22.Kg3
h5 23.gxh5 Bf5 24.Kh2 Qb8 25.h6 Qb3 26.Ne5 Nxe5 27.fxe5 Bxe5+ 28.Kg2 Qc2+ 
29.Qe2 Be4+ 30.Kf2 Bd4+ 31.Kg3 Qb3 32.Kh4 Bf6+ 33.Bg5 Bxg5+ 34.Kxg5 f6+ 
35.Kh4 g5+ 36.Kh5 Kf7 37.Re1 Bg6+ 38.Kg4 Rxe2 39.Rxe2 Bd3 40.Rf2 Bf1 41.Rxf1 
Qxb2 42.Kg3 Qxc3+ 43.Rf3 Qe5+ 44.Kf2 Qxd5 45.Ke2 Kg6 46.h7 Kxh7 47.Rc3 Qd4 
48.Rd3 Qe5+ 49.Re3 Qb2+ 50.Kd3 Qd4+ 51.Ke2 c4 52.Re7+ Kh6 53.Kf1 Qd1+ 54.Re1 
Qf3+ 55.Kg1 c3 56.Rf1 Qg3+ 57.Kh1 c2 58.h4 Kh5 59.Rc1 Kxh4 60.Rxc2 Kh3 61.Re2 
Qf3+ 62.Kg1 Qxe2 63.a4 Qg2# 0-1
```

## WCRCC 2008

[WCRCC 2008](/WCRCC_2008 "WCRCC 2008"), round 2, Alaric (TerraPi) - [Arasan](/Arasan "Arasan") [[9]](#cite_note-9) [[10]](#cite_note-10)

```
[Event "WCRCC 2008"]
[Site "Internet Chess Club"]
[Date "2008.06.21"]
[Round "2"]
[White "TerraPi"]
[Black "Arasan"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5 
9.exd5 Nxd5 10.Nxe5 Nxe5 11.Rxe5 c6 12.d4 Bd6 13.Re1 Qh4 14.g3 Qh3 15.Re4 
g5 16.Qe1 Bf5 17.Nd2 Nf6 18.f3 Nxe4 19.Nxe4 Bxe4 20.fxe4 Be7 21.e5 Qg4 22.Qd1 
Qxd1+ 23.Bxd1 Rab8 24.Bf3 Rfc8 25.Be3 Kg7 26.Be4 h6 27.Rf1 a5 28.Kg2 Rc7 
29.Kf3 Rh8 30.h3 Rd8 31.Kg4 a4 32.Rd1 Rf8 33.Kf5 Rb8 34.Rh1 Rh8 35.h4 Rcc8 
36.b3 axb3 37.axb3 Rc7 38.hxg5 Bxg5 39.Bxg5 hxg5 40.Rxh8 Kxh8 41.Kxg5 Kg7 
42.c4 bxc4 43.bxc4 Rc8 44.g4 Rd8 45.d5 cxd5 46.cxd5 Rc8 47.d6 Rc1 48.Kf4 Rf1+ 
49.Ke3 Re1+ 50.Kf3 Kh6 51.Kf4 Kg7 52.g5 Rf1+ 53.Ke3 Rd1 54.Bd3 Kf8 55.g6 fxg6 
56.Bxg6 Rg1 57.Bd3 Re1+ 58.Kd4 Ke8 59.Bc4 Kd7 60.Kd5 Rd1+ 61.Kc5 Re1 62.e6+ 
Kd8 63.Kd4 Kc8 1-0
```

# See also

- [Terra](/Terra "Terra")

# Forum Posts

## 2005 ...

- [About the "final" Terra and Alaric](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1488&p=6838) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 28, 2005
- [Alaric new version](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6210&p=29635) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 12, 2007
- [New Alaric](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6349&p=30102) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 30, 2007
- [Alaric 704 : 2607](http://www.talkchess.com/forum/viewtopic.php?t=12899) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), April 06, 2007
- [Alaric test for Fritz users](http://www.talkchess.com/forum/viewtopic.php?t=14814) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [CCC](/CCC "CCC"), July 01, 2007
- [Alaric 707](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6655&p=31087) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 14, 2007
- [Alaric 707 : 2670](http://www.talkchess.com/forum/viewtopic.php?t=15131) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), July 15, 2007

## 2008 ...

- [Where is Alaric?](http://www.talkchess.com/forum/viewtopic.php?t=18805) by [Mike Scheidl](/index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](/CCC "CCC"), January 08, 2008
- [some notes re Arasan games in ACCA](http://www.talkchess.com/forum/viewtopic.php?t=21900) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), June 22, 2008 » [WCRCC 2008](/WCRCC_2008 "WCRCC 2008"), [Arasan](/Arasan "Arasan")
- [WCRCC: Sjeng-TerraPi sac](http://www.talkchess.com/forum/viewtopic.php?t=21964) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), June 25, 2008 » [WCRCC 2008](/WCRCC_2008 "WCRCC 2008"), [Deep Sjeng](/Deep_Sjeng "Deep Sjeng")
- [Operator for Alaric in World Comp Rapid Chess Championship](http://www.talkchess.com/forum/viewtopic.php?t=29361) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [CCC](/CCC "CCC"), August 12, 2009 » [WCRCC 2009](/WCRCC_2009 "WCRCC 2009")

# External Links

## Chess Engine

- [Alaric Home](http://alaric.fendrich.se/)

:   [Input thread, code](http://alaric.fendrich.se/Downloads.html#Topic7)

- [Alaric Blog](http://alaricblog.fendrich.se/#home)
- [The chess games of Alaric](http://www.chessgames.com/perl/chessplayer?pid=111079) from [chessgames.com](http://www.chessgames.com/index.html)
- [/Engines/Alaric - Lucas Chess - Google Project Hosting](https://github.com/lukasmonk/lucaschess/tree/master/Engines/Windows/alaric)
- [Alaric 707](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&eng=Alaric%20707) in [KCEC](/KCEC "KCEC")
- [Alaric 707](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Alaric%20707#Alaric_707) in [CCRL 40/4](/CCRL "CCRL")

## Misc

- [Alaric (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Alaric)
- [Alaric (name) from Wikipedia](https://en.wikipedia.org/wiki/Alaric_%28name%29)
- [Alaric and Eric from Wikipedia](https://en.wikipedia.org/wiki/Alaric_and_Eric)
- [Alaric I from Wikipedia](https://en.wikipedia.org/wiki/Alaric_I)
- [Alaric II from Wikipedia](https://en.wikipedia.org/wiki/Alaric_II)

# References

1. [↑](#cite_ref-1) Portrait of Alaric in [C. Strahlheim](https://de.wikipedia.org/wiki/Johann_Konrad_Friederich) (**1836**). *Das Welttheater oder die allgemeine Weltgeschichte*. Band 4, [Frankfurt a.M.](https://en.wikipedia.org/wiki/Frankfurt), [Alaric I from Wikipedia](https://en.wikipedia.org/wiki/Alaric_I)
2. [↑](#cite_ref-2) [Alaric - Archive](http://alaric.fendrich.se/Archive.html)
3. [↑](#cite_ref-3) [Alaric - About the engine](http://alaric.fendrich.se/Abouttheengine.html)
4. [↑](#cite_ref-4) [Alaric - About Alaric and the Goths](http://alaric.fendrich.se/AboutAlaricandtheGoths.html)
5. [↑](#cite_ref-5) [Alaric @ WCRCC tournament](http://alaricblog.fendrich.se/#post13) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), July 24, 2007
6. [↑](#cite_ref-6) [Alaric's results](http://alaricblog.fendrich.se/#post17) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), June 23, 2008
7. [↑](#cite_ref-7) [Alaric - Downloads](http://alaric.fendrich.se/Downloads.html)
8. [↑](#cite_ref-8) [Buzz (Computer) vs Alaric (Computer) (2007)](http://www.chessgames.com/perl/chessgame?gid=1464418) from [chessgames.com](http://www.chessgames.com/index.html)
9. [↑](#cite_ref-9) [2008 Second Annual ACCA World Computer Chess Championships - Results](http://compchess.org/ACCAWCRCC/2008ACCAWCRCC/2008WCRCCResults.html)
10. [↑](#cite_ref-10) [some notes re Arasan games in ACCA](http://www.talkchess.com/forum/viewtopic.php?t=21900) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), June 22, 2008

**[Up one Level](/Engines "Engines")**