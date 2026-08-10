# Bison

Source: https://www.chessprogramming.org/Bison

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Bison**

[![](https://upload.wikimedia.org/wikipedia/commons/2/24/Muybridge_Buffalo_galloping.gif)](/File:Muybridge_Buffalo_galloping.gif)

American Bison [[1]](#cite_note-1)

**Bison**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Ivan Bonkin](/Ivan_Bonkin "Ivan Bonkin"),
written in [C++](/Cpp "Cpp") and licensed under [GPLv3](/Free_Software_Foundation#GPL "Free Software Foundation").
Bison played the [CCCCISC 2008](/CCCCISC_2008 "CCCCISC 2008") over the board.
Whether Bison is merely a rewrite of the [Fruit](/Fruit "Fruit") concepts, using [bitboards](/Bitboards "Bitboards") instead of [vector attack arrays](/Vector_Attacks "Vector Attacks"),
as suggested by [Dann Corbit](/Dann_Corbit "Dann Corbit") [[2]](#cite_note-2),
might be subject of scientific research - opposed to the [Rybka Controversy](/Rybka_Controversy "Rybka Controversy"), both sources are freely availably
[[3]](#cite_note-3)
[[4]](#cite_note-4).

# Description

## Board Representation

Bison is a [bitboard](/Bitboards "Bitboards") engine and uses [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks").
It performs the 2x32-bit [SWAR-implementation](/Population_Count#SWARPopcount "Population Count") to [count populations](/Population_Count "Population Count"), and [De Bruijn multiplication](/BitScan#DeBruijnMultiplation "BitScan") to [scan bits forward](/BitScan#Bitscanforward "BitScan") in [bitboard serialization](/Bitboard_Serialization "Bitboard Serialization").

## Search

Bison applies [PVS](/Principal_Variation_Search "Principal Variation Search") [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table"), [null move pruning](/Null_Move_Pruning "Null Move Pruning") with [zugzwang verification search](/Null_Move_Pruning#ZugzwangVerification "Null Move Pruning"),
[razoring](/Razoring "Razoring"), [IID](/Internal_Iterative_Deepening "Internal Iterative Deepening"), [futility pruning](/Futility_Pruning "Futility Pruning"), [history pruning](/History_Leaf_Pruning "History Leaf Pruning"), [delta pruning](/Delta_Pruning "Delta Pruning") and [mate distance pruning](/Mate_Distance_Pruning "Mate Distance Pruning"), [LMR](/Late_Move_Reductions "Late Move Reductions") and various [extensions](/Extensions "Extensions") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](/Aspiration_Windows "Aspiration Windows") and [floating point](/Float "Float") [fractional ply depths](/Depth#FractionalPlies "Depth").
[SEE](/SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm") is used in [move ordering](/Move_Ordering "Move Ordering") and to determine winning [tactical moves](/Tactical_Moves "Tactical Moves") in [quiescence](/Quiescence_Search "Quiescence Search").

## Evaluation

[Evaluation](/Evaluation "Evaluation") is sped up by pre-initialized [material-tables](/Material_Tables "Material Tables") indexed à la [Strelka](/Strelka "Strelka") and a [pawn hash table](/Pawn_Hash_Table "Pawn Hash Table") and might be [lazy](/Lazy_Evaluation "Lazy Evaluation").
It otherwise takes [pawn structure](/Pawn_Structure "Pawn Structure"), [mobility](/Mobility "Mobility") considering [pinned pieces](/Pin "Pin") and [king piece tropism](/King_Safety#KingTropism "King Safety") and various [pattern and attacks](/Bitboards#Pattern "Bitboards") under account with focus on [king safety](/King_Safety "King Safety") and [passed pawns](/Passed_Pawn "Passed Pawn"),
speculatively aggregating [middlegame](/Middlegame "Middlegame") and [endgame](/Endgame "Endgame") scores, which were [tapered](/Tapered_Eval "Tapered Eval") by a range of 24 [game phases](/Game_Phases "Game Phases").

# Selected Games

[CCCCISC 2008](/CCCCISC_2008 "CCCCISC 2008"), round 3, Bison - [Counter](/Counter "Counter") [[5]](#cite_note-5)

```
[Event "CIS 2008"]
[Site "Moscow SDCHESS RGSU"]
[Date "2008.03.01"]
[Round "3"]
[White "Bison 8.2.4r"]
[Black "Counter 0.8"]
[Result "1/2-1/2"]

1.Nf3 d5 2.d4 Nf6 3.c4 e6 4.Nc3 Be7 5.Bg5 h6 6.Bh4 O-O 7.e3 b6 8.Rb1 c6 9.cxd5 exd5 
10.Bd3 Bg4 11.O-O Ne4 12.Bxe7 Qxe7 13.Qc2 Bxf3 14.gxf3 Nxc3 15.Qxc3 a5 16.Rbc1 Rc8 
17.Kh1 Qf6 18.Be2 Nd7 19.Qb3 a4 20.Qa3 c5 21.dxc5 Rxc5 22.b4 Rxc1 23.Qxc1 Qe6 24.Qc2 
Ne5 25.Rc1 a3 26.Qd2 Nc6 27.b5 Ne7 28.Rc3 Qd6 29.Qd4 Rc8 30.Rxc8+ Nxc8 31.Bd3 Qc5 
32.Qh4 Ne7 33.Kg2 f6 34.Qa4 Kf7 35.Be2 Qc3 36.Bd1 g6 37.Qa7 Qc4 38.Bb3 Qxb5 39.e4 Qc5
40.Bxd5+ Kg7 41.Qd7 h5 42.Be6 Qg5+ 43.Kh3 Qc5 44.f4 g5 45.fxg5 fxg5 46.Bd5 g4+ 47.Kg2
Kh6 48.Qe6+ Ng6 49.Qf6 h4 50.h3 gxh3+ 51.Kxh3 Qc1 52.Qf3 Qg5 53.Bb3 Nf4+ 54.Kh2 b5 
55.Kh1 Kg6 56.Bc2 Kf6 57.Qc3+ 1/2-1/2
```

# Forum Posts

## 2008 ...

- [Is Bison kosher ?](http://www.talkchess.com/forum/viewtopic.php?t=19419) by [Olivier Deville](/Olivier_Deville "Olivier Deville"), [CCC](/CCC "CCC"), February 05, 2008
- [Bison 8.2.4r : 2152](http://www.talkchess.com/forum/viewtopic.php?t=19464) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), February 07, 2008
- [Bison 9.6 is released...](http://www.talkchess.com/forum/viewtopic.php?t=28335) by [Dr.Wael Deeb](/index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](/CCC "CCC"), June 10, 2009
- [Bison 9.6 : 2507](http://www.talkchess.com/forum/viewtopic.php?t=28371) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), June 12, 2009
- [Bison Info](http://www.talkchess.com/forum/viewtopic.php?t=28510) by [Ted Summers](http://www.talkchess.com/forum/profile.php?mode=viewprofile&u=608), [CCC](/CCC "CCC"), June 19, 2009
- [Bison 9.8 : 2528](http://www.talkchess.com/forum/viewtopic.php?t=29215) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), August 02, 2009
- [Bison 9.11 is released...](http://www.talkchess.com/forum/viewtopic.php?t=30749) by [Dr.Wael Deeb](/index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](/CCC "CCC"), November 22, 2009
- [Bison 9.11 : 2585](http://www.talkchess.com/forum/viewtopic.php?t=30762) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), November 23, 2009

## 2010 ...

- [Bison](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50838&p=193088) by [Graham Banks](/Graham_Banks "Graham Banks"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 04, 2010
- [About derivatives](http://www.open-chess.org/viewtopic.php?f=5&t=1546) by [Olivier Deville](/Olivier_Deville "Olivier Deville"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 11, 2011

# External Links

## Chess Engine

- [Bison at SourceForge.net](https://sourceforge.net/projects/bison/)
- [Bison by Иван Бонькин (Ivan Bonkin), Russia!](http://www.sdchess.ru/Bison.html) from [sdchess.ru](http://www.sdchess.ru/)
- [Bison](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Bison&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [Bison from Wikipedia](https://en.wikipedia.org/wiki/Bison)
- [Bison (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Bison_%28disambiguation%29)
- [Bison - Wikispecies](https://species.wikimedia.org/wiki/Bison)
- [GNU bison from Wikipedia](https://en.wikipedia.org/wiki/GNU_bison)
- [Bison - GNU parser generator](http://www.gnu.org/software/bison/)
- [Bison B.C.](https://en.wikipedia.org/wiki/Bison_B.C.) - Medication, [The Milestone](https://themilestone.club/), [Charlotte, NC](https://en.wikipedia.org/wiki/Charlotte,_North_Carolina), September 19, 2009, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

### Extant Bison

- [American bison from Wikipedia](https://en.wikipedia.org/wiki/American_bison)

:   [Plains bison from Wikipedia](https://en.wikipedia.org/wiki/Plains_bison)
:   [Wood bison from Wikipedia](https://en.wikipedia.org/wiki/Wood_bison)

- [European bison from Wikipedia](https://en.wikipedia.org/wiki/European_bison)

### Extinct Bison

- [Bison antiquus from Wikipedia](https://en.wikipedia.org/wiki/Bison_antiquus)
- [Bison latifrons from Wikipedia](https://en.wikipedia.org/wiki/Bison_latifrons)
- [Bison occidentalis from Wikipedia](https://en.wikipedia.org/wiki/Bison_occidentalis)
- [Steppe bison from Wikipedia](https://en.wikipedia.org/wiki/Steppe_bison)

# References

1. [↑](#cite_ref-1) [Animated sequence of a buffalo (American bison)](https://commons.wikimedia.org/wiki/File:Muybridge_Buffalo_galloping.gif) galloping. Photos taken by [Eadweard Muybridge](https://en.wikipedia.org/wiki/Eadweard_Muybridge) (died 1904), first published in 1887 at [Philadelphia](https://en.wikipedia.org/wiki/Philadelphia) (Animal Locomotion). Animation by [Waugsberg](http://commons.wikimedia.org/wiki/User:Waugsberg), July 16, 2006, [American bison from Wikipedia](https://en.wikipedia.org/wiki/American_bison)
2. [↑](#cite_ref-2) [Re: Bison](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50838&p=193088) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 04, 2010
3. [↑](#cite_ref-3) [Bison at SourceForge.net](https://sourceforge.net/projects/bison/)
4. [↑](#cite_ref-4) [Fruit Chess Engine by Fabien Letouzey - Fruit 2.1 source](http://arctrix.com/nas/chess/fruit/)
5. [↑](#cite_ref-5) [The The First championship of the CIS (Первый официальный чемпионат СНГ)](http://www.sdchess.ru/Tournaments/Cis_official_1.htm) from [sdchess.ru](http://www.sdchess.ru/)

**[Up one Level](/Engines "Engines")**