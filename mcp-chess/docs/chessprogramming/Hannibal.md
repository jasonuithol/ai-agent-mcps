# Hannibal

Source: https://www.chessprogramming.org/Hannibal

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Hannibal**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/HannibalFrescoCapitolinec1510.jpg/330px-HannibalFrescoCapitolinec1510.jpg)](/File:HannibalFrescoCapitolinec1510.jpg)

Hannibal crossing the Alps [[1]](#cite_note-1)

**Hannibal**,  
an [UCI](/UCI "UCI") compliant chess engine developed by [Sam Hamilton](/Sam_Hamilton "Sam Hamilton") and [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), supported by [Audy Arandela](/index.php?title=Audy_Arandela&action=edit&redlink=1 "Audy Arandela (page does not exist)") in [testing](/Engine_Testing "Engine Testing") and maintaining the [opening book](/Opening_Book "Opening Book"). They share the common goal to make Hannibal as strong as possible. As of now, they are working on the [tactical](/Tactics "Tactics") weakness, due to Edsel's non-conventional aggressive [pruning](/Pruning "Pruning") methods, and the holes in the [evaluation function](/Evaluation_Function "Evaluation Function") [[2]](#cite_note-2). Edsel will be working on [SMP search](/Parallel_Search "Parallel Search") [[3]](#cite_note-3), while Sam will be in charge of writing code to [tune the parameters automatically](/Automated_Tuning "Automated Tuning").

Hannibal incorporates ideas from their authors earlier engines [LearningLemming](/LearningLemming "LearningLemming") and [Twisted Logic](/Twisted_Logic "Twisted Logic"). It uses [alpha-beta](/Alpha-Beta "Alpha-Beta"), enhanced with various chess specific heuristics, and relies on a very [selective search](/Selectivity "Selectivity"), [endgame](/Endgame "Endgame") [knowledge](/Knowledge "Knowledge"), and an understanding of [material](/Material "Material") imbalances [[4]](#cite_note-4). [Bitboards](/Bitboards "Bitboards") are the basic data structure used to represent the board and to [generate moves](/Move_Generation "Move Generation").

# Etymology

[Hannibal](https://en.wikipedia.org/wiki/Hannibal_%28disambiguation%29), from [Phoenician](https://en.wikipedia.org/wiki/Phoenician_language) hann - "grace" and baal - "master" or "lord", meaning “mercy of (the god) [Ba'al](https://en.wikipedia.org/wiki/Ba%27al)” [[5]](#cite_note-5), was a [Carthaginian](https://en.wikipedia.org/wiki/Carthage) general who fought the [Roman Republic](https://en.wikipedia.org/wiki/Roman_Republic) in the [Second Punic War](https://en.wikipedia.org/wiki/Second_Punic_War).

# Tournament Play

Hannibal played the [CCT12](/CCT12 "CCT12"), [WCRCC 2010](/WCRCC_2010 "WCRCC 2010"), [WCRCC 2011](/WCRCC_2011 "WCRCC 2011"), and the [ACCA 2011](/ACCA_2011 "ACCA 2011") [online tournaments](/Tournaments_and_Matches#online "Tournaments and Matches").

# Selected Games

[CCT12](/CCT12 "CCT12"), round 5, Hannibal - [Shredder](/Shredder "Shredder") [[6]](#cite_note-6)

```
[Event "CCT12"]
[Site "FICS"]
[Date "2010.02.20"]
[Round "5"]
[White "Hannibal"]
[Black "Shredder"]
[Result "1/2-1/2"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O d6 6.Re1 Be7 7.c3 Bd7 8.d4 O-O 
9.Nbd2 exd4 10.cxd4 Nb4 11.Bxd7 Qxd7 12.Qb3 a5 13.a3 Na6 14.Qc2 h6 15.Nc4 
a4 16.Bd2 d5 17.exd5 Nxd5 18.b3 c5 19.bxa4 cxd4 20.Nce5 Qc7 21.Qe4 Qd8 
22.Qg4 Nc5 23.Bxh6 Bf6 24.Rac1 Nc3 25.Bg5 Rxa4 26.Bxf6 Qxf6 27.Nxd4 Rd8 
28.Rxc3 Raxd4 29.Qh5 Re4 30.Rce3 Rxe3 31.Rxe3 Qf5 32.g4 Qxh5 33.gxh5 Rd5 
34.Nc4 Rg5+ 35.Kh1 Rxh5 36.Re8+ Kh7 37.Nd6 Kg6 38.Re7 Rh3 39.Rxf7 Rd3 40.Rc7 
Ne6 41.Rd7 Kh5 42.h4 Kg4 43.Nf7 Rxd7 44.Ne5+ Kxh4 45.Nxd7 Nf4 46.Nc5 b6 
47.Nb3 Nd3 48.Kg2 Kg4 49.a4 Kf4 50.a5 bxa5 51.Nxa5 Ke4 1/2-1/2
```

# See also

- [Elephant](/Elephant "Elephant")
- [LearningLemming](/LearningLemming "LearningLemming")
- [Twisted Logic](/Twisted_Logic "Twisted Logic")

# Forum Posts

## 2010 ...

- [Twisted Logic 20100131x](http://www.talkchess.com/forum/viewtopic.php?t=32288) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), February 02, 2010
- [Hannibal 1.0](http://www.talkchess.com/forum/viewtopic.php?t=35468) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), July 17, 2010
- [WCRCC 2010 - Hannibal games](http://www.talkchess.com/forum/viewtopic.php?t=35474) by [Sam Hamilton](/Sam_Hamilton "Sam Hamilton"), [CCC](/CCC "CCC"), July 17, 2010 » [WCRCC 2010](/WCRCC_2010 "WCRCC 2010")
- [To Ed: Hannibal 1.0a ... Twisted Logic!](http://www.talkchess.com/forum/viewtopic.php?t=35522) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), July 20, 2010
- [Hannibal opening book](http://www.talkchess.com/forum/viewtopic.php?t=35528) by [Audy Arandela](/index.php?title=Audy_Arandela&action=edit&redlink=1 "Audy Arandela (page does not exist)"), [CCC](/CCC "CCC"), July 21, 2010
- [Xmas SWCR gift: Booot won vs. Hannibal with 3 knights!](http://www.talkchess.com/forum/viewtopic.php?t=37216) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), December 21, 2010 » [Booot](/Booot "Booot")
- [Gaviota - Hannibal 5th round (great Hannibal game, watch it)](http://www.talkchess.com/forum/viewtopic.php?t=39823) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), July 23, 2011
- [Reducing/Pruning Bad Captures (SEE < 0)](http://www.talkchess.com/forum/viewtopic.php?t=40100) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), August 19, 2011 » [Pruning](/Pruning "Pruning"), [Reductions](/Reductions "Reductions"), [Captures](/Captures "Captures"), [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Hey Sam: Hannibal and obvious move heuristic](http://www.talkchess.com/forum/viewtopic.php?t=41254) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), November 29, 2011
- [SMP and questions](http://www.talkchess.com/forum/viewtopic.php?t=46124) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), November 23, 2012 » [Parallel Search](/Parallel_Search "Parallel Search")
- [Hannibal 1.3 SMP](http://www.talkchess.com/forum/viewtopic.php?t=46683) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), December 31, 2012

## 2015 ...

- [Hannibal 1.5 release](http://www.talkchess.com/forum/viewtopic.php?t=55127) by [Sam Hamilton](/Sam_Hamilton "Sam Hamilton"), [CCC](/CCC "CCC"), January 28, 2015
- [Hannibal 1.5 bug](http://www.talkchess.com/forum/viewtopic.php?t=57124) by Carl Langan, [CCC](/CCC "CCC"), July 31, 2015
- [Hannibal 1.7](http://www.talkchess.com/forum/viewtopic.php?t=61082) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), August 09, 2016

# External Links

## Chess Engine

- [Hannibal - Chess Engine Portal](https://sites.google.com/site/edapostol/hannibal)
- [Computerschach, Interview with Edsel Apostol](http://www.schach-welt.de/schach/computerschach/interviews/edsel-apostol) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), February 25, 2010
- [Hannibal 1.2 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details+%28text%29&eng=Hannibal%201.2%2064-bit) from [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Hannibal (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Hannibal_%28disambiguation%29)
- [Hannibal from Wikipedia](https://en.wikipedia.org/wiki/Hannibal)
- [2152 Hannibal from Wikipedia](https://en.wikipedia.org/wiki/2152_Hannibal)
- [Hannibal, Missouri from Wikipedia](https://en.wikipedia.org/wiki/Hannibal,_Missouri)
- [Hannibal, New York from Wikipedia](https://en.wikipedia.org/wiki/Hannibal,_New_York)
- [Hannibal Lecter from Wikipedia](https://en.wikipedia.org/wiki/Hannibal_Lecter)
- [Hannibal (high-rise building) from Wikipedia](https://en.wikipedia.org/wiki/Hannibal_%28high-rise_building%29)
- [Miles Davis](/Category:Miles_Davis "Category:Miles Davis") - Hannibal [[7]](#cite_note-7), 1988, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   feat. [Kenny Garrett](https://en.wikipedia.org/wiki/Kenny_Garrett), [Bobby Irving](https://en.wikipedia.org/wiki/Robert_Irving_III), [Adam Holzman](https://en.wikipedia.org/wiki/Adam_Holzman_%28keyboardist%29), [Benjamin Rietveld](http://www.discogs.com/artist/Benny+Rietveld?filter_anv=1&anv=Benjamin+Rietveld), [Joe "Foley" McCreary](https://en.wikipedia.org/wiki/Foley_%28musician%29), [Marilyn Mazur](/Category:Marilyn_Mazur "Category:Marilyn Mazur"), [Ricky Wellman](http://www.thelastmiles.com/interviews-ricky-wellman.php)

# References

1. [↑](#cite_ref-1) Hannibal's celebrated feat in crossing the [Alps](https://en.wikipedia.org/wiki/Alps) with [war elephants](https://en.wikipedia.org/wiki/War_elephant) passed into European legend: detail of a fresco by [Jacopo Ripanda](https://en.wikipedia.org/wiki/Jacopo_Ripanda), ca. 1510, [Capitoline Museums](https://en.wikipedia.org/wiki/Capitoline_Museums), [Rome](https://en.wikipedia.org/wiki/Rome), [Hannibal from Wikipedia](https://en.wikipedia.org/wiki/Hannibal)
2. [↑](#cite_ref-2) [Computerschach, Interview with Edsel Apostol](http://www.schach-welt.de/schach/computerschach/interviews/edsel-apostol) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), February 25, 2010
3. [↑](#cite_ref-3) [SMP and questions](http://www.talkchess.com/forum/viewtopic.php?t=46124) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), November 23, 2012
4. [↑](#cite_ref-4) [Hannibal - Chess Engine Portal](https://sites.google.com/site/edapostol/hannibal)
5. [↑](#cite_ref-5) [Hannibal - Wiktionary](https://en.wiktionary.org/wiki/Hannibal)
6. [↑](#cite_ref-6) [CCT-12-Hannibal games](http://www.schach-welt.de/images/download/computerschach/cct-12_hannibal.zip) hosted by [Schachwelt](http://www.schach-welt.de/index.php), [Computerschach, Interview with Edsel Apostol](http://www.schach-welt.de/schach/computerschach/interviews/edsel-apostol) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), February 25, 2010
7. [↑](#cite_ref-7) This is actually [The Senate / Me & You](http://www.youtube.com/watch?v=R4uytYyj1aA)

**[Up one Level](/Engines "Engines")**