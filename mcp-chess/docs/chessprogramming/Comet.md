# Comet

Source: https://www.chessprogramming.org/Comet

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Comet**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Histoire_d%27une_com%C3%A8te%2C_by_Luis_Ricardo_Falero.jpg/330px-Histoire_d%27une_com%C3%A8te%2C_by_Luis_Ricardo_Falero.jpg)](/File:Histoire_d%27une_com%C3%A8te,_by_Luis_Ricardo_Falero.jpg)

Story of a Comet [[1]](#cite_note-1)

**Comet**,   
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess program by [Ulrich Türke](/Ulrich_T%C3%BCrke "Ulrich Türke"). Comet is written in [C](/C "C") and therefor available for several platforms. Comet played various [over the board tournaments](/Tournaments_and_Matches "Tournaments and Matches"), [Aegon Tournaments](/Aegon_Tournaments "Aegon Tournaments"), three [World Microcomputer Chess Championships](/World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship"), [1995](/WMCCC_1995 "WMCCC 1995"), [1996](/WMCCC_1996 "WMCCC 1996") and [1997](/WMCCC_1997 "WMCCC 1997"), multiple [International Paderborn Computer Chess Championships](/IPCCC "IPCCC"), [CCT Tournaments](/CCT_Tournaments "CCT Tournaments"), and the [ICT 2002](/ICT_2002 "ICT 2002").

# Screenshot

[![CometDOSGUI.gif](/images/7/70/CometDOSGUI.gif)](http://www.septober.de/chess/index.htm)

Comet [DOS](/MS-DOS "MS-DOS") [GUI](/GUI "GUI") [[2]](#cite_note-2)

# Description

given in 1997 from the [ICGA](/ICGA "ICGA") site [[3]](#cite_note-3):

- Design and implementation in 1991 originally guided by [GNU Chess 3.0](/GNU_Chess "GNU Chess")
- Standard - [search algorithm](/Search "Search"): [Minimax](/Minimax "Minimax") + [Alpha-Beta](/Alpha-Beta "Alpha-Beta") including "[Aspiration-Window](/Aspiration_Windows "Aspiration Windows")"; no [minimal window search](/Principal_Variation_Search "Principal Variation Search").
- Good [tactical](/Tactics "Tactics") strength by conventional [extensions](/Extensions "Extensions") and threat detection by [null-move heuristic](/Null_Move_Pruning "Null Move Pruning")
- Use of a sophisticated, domain-dependent evaluation window technique
- Considerable [knowledge](/Knowledge "Knowledge") implemented in [evaluation](/Evaluation "Evaluation") modules evaluation in 3 passes:

:   1. scan and evaluation of [pawn structure](/Pawn_Structure "Pawn Structure")
:   2. piece and king evaluation depending on the results of pass 1
:   3. evaluation of global positional characteristics

- Implementation of various classes of [killer moves](/Killer_Heuristic "Killer Heuristic")
- [Selectivity](/Selectivity "Selectivity"):

:   a) [Razoring](/Razoring "Razoring"), modified [fail high reduction](/Fail-High_Reductions "Fail-High Reductions") at [depth 1](/Frontier_Nodes "Frontier Nodes")
:   b) [Null move search](/Null_Move_Pruning "Null Move Pruning"), partly with reduced search depth
:   c) [Quiescence](/Quiescence_Search "Quiescence Search") cut-offs as in [GNU-Chess](/GNU_Chess "GNU Chess")

- [Opening book](/Opening_Book "Opening Book") with 120000 positions

# Selected Games

[WMCCC 1997](/WMCCC_1997 "WMCCC 1997"), round 11, Comet - [The Crazy Bishop](/The_Crazy_Bishop "The Crazy Bishop") [[4]](#cite_note-4)

```
[Event "WMCCC 1997"]
[Site "Paris, France"]
[Date "1997.11.02"]
[Round "11"]
[White "Comet"]
[Black "The Crazy Bishop"]
[Result "1-0"]

1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e5 6.Ndb5 d6 7.Bg5 a6 8.Na3 Be7 
9.Bc4 O-O 10.Bxf6 Bxf6 11.Bd5 Rb8 12.O-O Nd4 13.Nc4 b5 14.Ne3 Bg5 15.Ne2 Bxe3 
16.fxe3 Ne6 17.Ng3 Qb6 18.Qd2 Nc7 19.Bb3 Be6 20.Nf5 Bxf5 21.Rxf5 Ne8 22.Raf1 
Nf6 23.Rxf6 gxf6 24.Rxf6 a5 25.Qf2 Kh8 26.Rh6 Rg8 27.Bxf7 Rg7 28.Bd5 Qd8 29.Rf6
Rc7 30.c3 b4 31.c4 a4 32.Qf5 Re7 33.Bf7 Qd7 34.Be6 Qd8 35.c5 Rg7 36.c6 a3 37.b3
Qe7 38.c7 Qxc7 39.Rf8+ Rg8 40.Bxg8 Rxf8 41.Qxf8 Qg7 42.Qxg7+ Kxg7 43.Bd5 1-0
```

# See also

- [Astronomy](/Category:Astronomy "Category:Astronomy")

# Forum Posts

## 1997 ...

- [Comet A.75 in test](https://www.stmintz.com/ccc/index.php?id=12531) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), November 30, 1997
- [Comet A 82](https://www.stmintz.com/ccc/index.php?id=14640) by [Fernando Villegas](/Fernando_Villegas "Fernando Villegas"), [CCC](/CCC "CCC"), January 25, 1998
- [Comet\_against\_Humans](https://www.stmintz.com/ccc/index.php?id=17984) by [Ulrich Türke](/Ulrich_T%C3%BCrke "Ulrich Türke"), [CCC](/CCC "CCC"), May 05, 1998
- [Comet A90](https://www.stmintz.com/ccc/index.php?id=18766) by [Thorsten Czub](/Thorsten_Czub "Thorsten Czub"), [CCC](/CCC "CCC"), May 16, 1998
- [Comet A.90 on Winboard](https://www.stmintz.com/ccc/index.php?id=24842) by Earl H. Castillo, [CCC](/CCC "CCC"), August 15, 1998
- [New Comet B02 Version!](https://www.stmintz.com/ccc/index.php?id=53613) by Christian Goralski, [CCC](/CCC "CCC"), May 30, 1999

## 2000 ...

- [Paderborn : A "human" pawn sac by Comet !](https://www.stmintz.com/ccc/index.php?id=96435) by Côme, [CCC](/CCC "CCC"), February 11, 2000 » [IPCCC 2000](/IPCCC_2000 "IPCCC 2000")
- [Re: Comet B18 Whats new?](https://www.stmintz.com/ccc/index.php?id=103170) by [Ulrich Türke](/Ulrich_T%C3%BCrke "Ulrich Türke"), [CCC](/CCC "CCC"), March 24, 2000 » [Passed Pawn](/Passed_Pawn "Passed Pawn"), [Bad Bishop](/Bad_Bishop "Bad Bishop")
- [Comet B.31 by Dr. Ulrich Türke is available !](https://www.stmintz.com/ccc/index.php?id=157816) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), March 10, 2001
- [Paderborn Comet](https://www.stmintz.com/ccc/index.php?id=216201) by Edward Seid, [CCC](/CCC "CCC"), March 02, 2002 » [IPCCC 2002](/IPCCC_2002 "IPCCC 2002")
- [xboard/Linux version of Comet B.46 available!](https://www.stmintz.com/ccc/index.php?id=234855) by [Leo Dijksman](/Leo_Dijksman "Leo Dijksman"), [CCC](/CCC "CCC"), June 10, 2002
- [Comet B48 under Chess Partner 5.2](https://www.stmintz.com/ccc/index.php?id=251938) by [Shaun Brewer](/index.php?title=Shaun_Brewer&action=edit&redlink=1 "Shaun Brewer (page does not exist)"), [CCC](/CCC "CCC"), September 13, 2002
- [Re: Comet 62b, where I look for it?](https://www.stmintz.com/ccc/index.php?id=322771) by [Ulrich Türke](/Ulrich_T%C3%BCrke "Ulrich Türke"), [CCC](/CCC "CCC"), October 21, 2003
- [Testposition from Comet-The Baron](https://www.stmintz.com/ccc/index.php?id=349322) by [Richard Pijl](/Richard_Pijl "Richard Pijl"), [CCC](/CCC "CCC"), February 15, 2004 » [The Baron](/The_Baron "The Baron"), [IPCCC 2004](/IPCCC_2004 "IPCCC 2004")
- [Re: Comet B68 a little question...](https://www.stmintz.com/ccc/index.php?id=355823) by [Ulrich Türke](/Ulrich_T%C3%BCrke "Ulrich Türke"), [CCC](/CCC "CCC"), March 21, 2004

## 2005 ...

- [What happened to Comet?](https://www.stmintz.com/ccc/index.php?id=470971) by [Fernando Villegas](/Fernando_Villegas "Fernando Villegas"), [CCC](/CCC "CCC"), December 16, 2005
- [OT - Comet 17P Holmes](http://www.talkchess.com/forum/viewtopic.php?t=17489) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), October 31, 2007 » [Holmes](/Holmes "Holmes") [[5]](#cite_note-5)
- [A Propos "Comet"](http://www.talkchess.com/forum/viewtopic.php?t=30127) by [Fernando Villegas](/Fernando_Villegas "Fernando Villegas"), [CCC](/CCC "CCC"), October 13, 2009

## 2010 ...

- [Comet B15, Amy 0.6 Green Light Chess 2.07a available ...](http://www.talkchess.com/forum/viewtopic.php?t=32361) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), February 04, 2010 » [Amy](/Amy "Amy"), [Green Light Chess](/Green_Light_Chess "Green Light Chess")
- [More about Comet B68](http://www.talkchess.com/forum/viewtopic.php?t=39968) by [Fernando Villegas](/Fernando_Villegas "Fernando Villegas"), [CCC](/CCC "CCC"), August 06, 2011

# External Links

## Chess Engine

- [Comet's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=14)
- [Index of /chess/engines/Norbert's collection/Comet (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Comet%20%28Compilation%29/) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Comet B68](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Comet%20B68#Comet_B68) in [CCRL 40/40](/CCRL "CCRL")

## Comet

- [Comet (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Comet_%28disambiguation%29)
- [Comet from Wikipedia](https://en.wikipedia.org/wiki/Comet)

:   [Great Comet from Wikipedia](https://en.wikipedia.org/wiki/Great_Comet)
:   [Comet nucleus from Wikipedia](https://en.wikipedia.org/wiki/Comet_nucleus)
:   [Coma (cometary) from Wikipedia](https://en.wikipedia.org/wiki/Coma_%28cometary%29)
:   [Comet tail from Wikipedia](https://en.wikipedia.org/wiki/Comet_tail)

- [Lists of comets from Wikipedia](https://en.wikipedia.org/wiki/Lists_of_comets)

:   [Comet Holmes from Wikipedia](https://en.wikipedia.org/wiki/Comet_Holmes)
:   [Halley's Comet from Wikipedia](https://en.wikipedia.org/wiki/Halley%27s_Comet)

- [Bill Haley & His Comets](https://en.wikipedia.org/wiki/Bill_Haley_%26_His_Comets) - [Hot Dog Buddy Buddy](https://en.wikipedia.org/wiki/Bill_Haley_%26_His_Comets_discography), from [Don't Knock the Rock](https://en.wikipedia.org/wiki/Don%27t_Knock_the_Rock) (1956), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Story of a Comet](http://commons.wikimedia.org/wiki/File:Histoire_d%27une_com%C3%A8te,_by_Luis_Ricardo_Falero.jpg) by [Luis Ricardo Falero](/Arts#Falero "Arts"), before 1897, [Oil on canvas](https://en.wikipedia.org/wiki/Oil_painting), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Septober - Computerschach](http://www.septober.de/chess/index.htm) by [Herbert Marquardt](/index.php?title=Herbert_Marquardt&action=edit&redlink=1 "Herbert Marquardt (page does not exist)")
3. [↑](#cite_ref-3) [Comet's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=14)
4. [↑](#cite_ref-4) [Paris 1997 - Chess - Round 11 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=5&round=11&id=6)
5. [↑](#cite_ref-5) [Comet Holmes from Wikipedia](https://en.wikipedia.org/wiki/Comet_Holmes)

**[Up one Level](/Engines "Engines")**