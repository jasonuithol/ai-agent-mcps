# Spark

Source: https://www.chessprogramming.org/Spark

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Spark**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Franklin_lightning_engraving.jpg/330px-Franklin_lightning_engraving.jpg)](/File:Franklin_lightning_engraving.jpg)

[Benjamin Franklin](https://en.wikipedia.org/wiki/Benjamin_Franklin) drawing a [spark](https://en.wikipedia.org/wiki/Electric_spark) [[1]](#cite_note-1)

**Spark**,  
an [UCI](/UCI "UCI") compatible chess engine by [Allard Siemelink](/Allard_Siemelink "Allard Siemelink"), written in [C++](/Cpp "Cpp").
During 2008, Allard Siemelink found that it became increasingly hard to improve his [0x88](/0x88 "0x88") engine [Bright](/Bright "Bright") much further, and started to create a [bitboard](/Bitboards "Bitboards") framework along with a [Perft](/Perft "Perft") benchmark which evolved to Spark with [search](/Search "Search") and [evaluation](/Evaluation "Evaluation") developed from scratch to try as much as possible alternative search strategies and evaluation terms for the ones that are found in Bright.
Spark's evaluation is [data mined](https://en.wikipedia.org/wiki/Data_mining) from a [database](/Databases "Databases") of 700,000 high quality games [[2]](#cite_note-2). Spark can be compiled to run under [Windows](/Windows "Windows"), [Linux](/Linux "Linux") and [Mac OS](/Mac_OS "Mac OS").

# Parallel Search

Like its earlier [0x88](/0x88 "0x88") relative [Bright](/Bright "Bright"), Spark is able to [search in parallel](/Parallel_Search "Parallel Search") supporting up to 16 [CPU cores](https://en.wikipedia.org/wiki/Multi-core_processor), basically applying the [Young Brothers Wait Concept](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept").
Since splitting is a cheap operation in Spark, avoiding an expensive copy of the board and associated data, the [search tree](/Search_Tree "Search Tree") can be split at any [depth](/Depth "Depth"), maximizing the use of the otherwise idle cores.

# LMR

[Late Move Reductions](/Late_Move_Reductions "Late Move Reductions") as popularized by [Fruit](/Fruit "Fruit") and [Glaurung](/Glaurung "Glaurung") are used in Spark with different implementation details. The reductions are not [history](/History_Heuristic "History Heuristic") based, and all moves, except the first one, can be reduced by up to two [plies](/Ply "Ply") depending on static criteria [[3]](#cite_note-3).

# Tournament Play

Spark played the [WCRCC 2009](/WCRCC_2009 "WCRCC 2009") [[4]](#cite_note-4),
[CCT12](/CCT12 "CCT12"), [ICT 2010](/ICT_2010 "ICT 2010"), [DOCCC 2010](/DOCCC_2010 "DOCCC 2010"), [DOCCC 2011](/DOCCC_2011 "DOCCC 2011") and [ICT 2012](/ICT_2012 "ICT 2012").

# Selected Games

## Rybka

[DOCCC 2010](/DOCCC_2010 "DOCCC 2010"), Round 6, Spark - [Rybka](/Rybka "Rybka")

```
[Event "DOCCC 2010"]
[Site "Leiden NED"]
[Date "2010.11.27"]
[Round "6"]
[White "Spark"]
[Black "Rybka"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 Qc7 6.Be3 a6 7.Be2 b5 8.Nxc6 Qxc6 9.O-O Bb7 10.Bf3 Qc7 
11.e5 Rc8 12.Bxb7 Qxb7 13.Qd3 Ne7 14.a4 bxa4 15.Rxa4 Nc6 16.f4 Nb4 17.Qe4 Qxe4 18.Nxe4 Rxc2 19.Rc1 
Rxc1+ 20.Bxc1 Be7 21.Bd2 Nd5 22.Nd6+ Bxd6 23.exd6 f5 24.Rxa6 Kf7 25.Ra7 Nf6 26.Bc3 Rb8 27.g3 Rb6 
28.Bxf6 Kxf6 29.Rxd7 Rxb2 30.h4 Rd2 31.Rd8 Kg6 32.Kf1 h5 33.Ke1 Rd5 34.Rd7 Rd4 35.Rd8 Kh7 36.Ke2 
Kh6 37.Ke3 Rd1 38.d7 Kg6 39.Re8 Rxd7 40.Rxe6+ 1/2-1/2
```

## HIARCS

[DOCCC 2010](/DOCCC_2010 "DOCCC 2010"), Round 7, [HIARCS](/HIARCS "HIARCS") - Spark

```
[Event "DOCCC 2010"]
[Site "Leiden NED"]
[Date "2010.11.28"]
[Round "7"]
[White "HIARCS"]
[Black "Spark"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e5 7.Nb3 Be6 8.f3 Be7 9.Qd2 O-O 10.O-O-O Nbd7 
11.g4 b5 12.g5 Nh5 13.Kb1 Nb6 14.Na5 Qc7 15.Nd5 Nxd5 16.exd5 Bxd5 17.Qxd5 Qxa5 18.Bd3 Qd8 19.Rhg1 
Rb8 20.Be4 Qc7 21.Rg4 g6 22.Qd3 Kh8 23.Bd5 f5 24.Rgg1 a5 25.a3 Qd7 26.f4 Rfc8 27.Bb3 a4 28.Ba2 Qc7 
29.c3 Bf8 30.Rgf1 Rd8 31.h4 Bg7 32.Bd5 Re8 33.Ka2 Re7 34.Kb1 Qc8 35.Ba2 exf4 36.Bxf4 Be5 37.Be3 f4 
38.Bf2 Ng3 39.Bxg3 fxg3 40.Rde1 Qh3 41.Qf3 Qf5+ 42.Qxf5 gxf5 43.Rxf5 Bxc3 44.Rxe7 g2 45.Rxh7+ Kxh7 
46.g6+ Kg7 47.Rg5 Bf6 48.Rxg2 b4 49.axb4 Rxb4 1/2-1/2
```

# See also

- [Bright](/Bright "Bright")
- [Chispa](/Chispa "Chispa")
- [Delphil's Desperado versus Spark](/Stalemate#SparkDelphil "Stalemate")

# Forum Posts

## 2009

- [2009 WCRCC: Bright/Spark issue](http://www.talkchess.com/forum/viewtopic.php?t=29385) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), August 13, 2009
- [Spark released](http://www.talkchess.com/forum/viewtopic.php?t=30432) by [Allard Siemelink](/Allard_Siemelink "Allard Siemelink"), [CCC](/CCC "CCC"), November 01, 2009

## 2010 ...

- [Spark 0.3a (mp) released](http://www.talkchess.com/forum/viewtopic.php?t=31617) by [Allard Siemelink](/Allard_Siemelink "Allard Siemelink"), [CCC](/CCC "CCC"), January 11, 2010
- [Spark 0.4 released](http://www.talkchess.com/forum/viewtopic.php?t=34476) by [Allard Siemelink](/Allard_Siemelink "Allard Siemelink"), [CCC](/CCC "CCC"), May 23, 2010
- [Spark node count](http://www.talkchess.com/forum/viewtopic.php?t=34555) by Peter C, [CCC](/CCC "CCC"), May 27, 2010
- [Spark 0.4 for Mac OSX released](http://www.talkchess.com/forum/viewtopic.php?t=34942) by [Allard Siemelink](/Allard_Siemelink "Allard Siemelink"), [CCC](/CCC "CCC"), June 14, 2010
- [Spark 1.0 released](http://www.talkchess.com/forum/viewtopic.php?t=37020) by [Allard Siemelink](/Allard_Siemelink "Allard Siemelink"), [CCC](/CCC "CCC"), December 10, 2010
- [Spark 2.0 Leiden 2011 ?](http://www.talkchess.com/forum/viewtopic.php?t=40788) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), October 16, 2011

## 2020 ...

- [Spark by Allard Siemelink ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74662) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), August 02, 2020

# External Links

## Chess Engine

- [Spark Chess](https://web.archive.org/web/20120302103748/http://members.ziggo.nl/allard.siemelink/spark/) by [Allard Siemelink](/Allard_Siemelink "Allard Siemelink") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Mac Chess Engines Repository](http://julien.marcel.free.fr/macchess/Chess_on_Mac/Engines.html) by [Julien Marcel](/Julien_Marcel "Julien Marcel")
- [Spark](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Spark&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Spark (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Spark)
- [Spark (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Spark_%28mathematics%29)
- [SPARK (programming language) from Wikipedia](https://en.wikipedia.org/wiki/SPARK_%28programming_language%29)
- [Spark (cellular automaton) from Wikipedia](https://en.wikipedia.org/wiki/Spark_%28cellular_automaton%29)
- [Electric spark from Wikipedia](https://en.wikipedia.org/wiki/Electric_spark)
- [Spark-gap transmitter from Wikipedia](https://en.wikipedia.org/wiki/Spark-gap_transmitter)
- [Spark (fire) from Wikipedia](https://en.wikipedia.org/wiki/Spark_%28fire%29)
- [Spark of Life from Wikipedia](https://en.wikipedia.org/wiki/Spark_of_Life)
- [Spark (Transformers) from Wikipedia](https://en.wikipedia.org/wiki/Spark_%28Transformers%29)
- [Spark (U.S. organization) from Wikipedia](https://en.wikipedia.org/wiki/Spark_%28U.S._organization%29)
- [Iskra (Spark) from Wikipedia](https://en.wikipedia.org/wiki/Iskra)
- [Sparks (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Sparks)
- [Hiromi Uehara](/Category:Hiromi_Uehara "Category:Hiromi Uehara"), [The Trio Project](https://en.wikipedia.org/wiki/Hiromi_Uehara#Trio), feat. [Anthony Jackson](/Category:Anthony_Jackson "Category:Anthony Jackson") & [Simon Phillips](/Category:Simon_Phillips "Category:Simon Phillips") - [Spark](https://en.wikipedia.org/wiki/Spark_(Hiromi_album)), (2016), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) An engraving of [Benjamin Franklin's](https://en.wikipedia.org/wiki/Benjamin_Franklin) [kite experiment](https://en.wikipedia.org/wiki/Kite_experiment), from page 159 (Fig. 82) of [Le Roy Clark Cooley](http://en.wikisource.org/wiki/Author:Le_Roy_C._Cooley) (**1881**). *Natural Philosophy for Common and High Schools*.
2. [↑](#cite_ref-2) [Spark Chess](https://web.archive.org/web/20120302103748/http://members.ziggo.nl/allard.siemelink/spark/) by [Allard Siemelink](/Allard_Siemelink "Allard Siemelink") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
3. [↑](#cite_ref-3) [Interview with Allard Siemelink](https://www.schach-welt.de/schach/computerschach/interviews/allard-siemelink-deng) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Schachwelt](https://www.schach-welt.de/), January 10, 2010
4. [↑](#cite_ref-4) [2009 WCRCC: Bright/Spark issue](http://www.talkchess.com/forum/viewtopic.php?t=29385) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), August 13, 2009

**[Up one Level](/Engines "Engines")**