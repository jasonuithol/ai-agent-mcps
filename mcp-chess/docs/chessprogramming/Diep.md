# Diep

Source: https://www.chessprogramming.org/Diep

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Diep**

[![](/images/thumb/1/13/Opccc07diepmajiecastelling.jpg/300px-Opccc07diepmajiecastelling.jpg)](http://oudzuylenutrecht.nl/opppc-2007/)

Diep [GUI](/GUI "GUI") [[1]](#cite_note-1)

**Diep**,  
a private chess engine by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), written in [C](/C "C"). The development started in 1994, and so far stopped in December 2012 [[2]](#cite_note-2). Since 1999 Diep performed a [parallel search](/Parallel_Search "Parallel Search") on [SMP](/SMP "SMP"), and later on [NUMA](/NUMA "NUMA") multi core systems, and occasionally on Super Computers but unfortunately without too much support for testing. Diep's most successful year was 2004, when Diep won the [Dutch Open Computer Chess Championship in 2004](/DOCCC_2004 "DOCCC 2004") [[3]](#cite_note-3), and won the Bronze Medal at the [WCCC in Ramat Gan](/WCCC_2004 "WCCC 2004") [[4]](#cite_note-4). Diep spawns [processes](/Process "Process") for its parallel search. Due to its enormous chess [knowledge](/Knowledge "Knowledge") implemented in its [evaluation](/Evaluation "Evaluation"), Diep was not a fast but knowledge based searcher.

# Deep Trouble

In 1997, [Vincent Diepeveen's](/Vincent_Diepeveen "Vincent Diepeveen") early claim caused some trouble and antagonism [[5]](#cite_note-5) [[6]](#cite_note-6) [[7]](#cite_note-7) :

```
Diep is without doubt the strongest chess analysis program in the world at infinite level (few hours a move). The longer you allow it to analyse the better the move it will produce, something which is uncommon for most other chessprograms, caused by the enormeous chessknowledge in Diep, which is at the time still considerably growing every month (and decreasing the Diep searchspeed).
```

# Tournament Play

Diep was one of the most active programs in official [tournaments](/Tournaments_and_Matches "Tournaments and Matches"). It played three [World Microcomputer Chess Championships](/World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship"), the [WMCCC 1997](/WMCCC_1997 "WMCCC 1997") [[8]](#cite_note-8) , [WMCCC 2000](/WMCCC_2000 "WMCCC 2000") and [WMCCC 2001](/WMCCC_2001 "WMCCC 2001"), seven [World Computer Chess Championships](/World_Computer_Chess_Championship "World Computer Chess Championship"), [WCCC 1999](/WCCC_1999 "WCCC 1999"), [WCCC 2002](/WCCC_2002 "WCCC 2002"), [WCCC 2003](/WCCC_2003 "WCCC 2003") [[9]](#cite_note-9) , [WCCC 2004](/WCCC_2004 "WCCC 2004"), [WCCC 2005](/WCCC_2005 "WCCC 2005"), [WCCC 2006](/WCCC_2006 "WCCC 2006") and the [WCCC 2007](/WCCC_2007 "WCCC 2007"), various [Dutch Open Computer Chess Championships](/Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"), [ICTs](/International_CSVN_Tournament "International CSVN Tournament") , [IPCCCs](/IPCCC "IPCCC"), the [IOPCCC 2007](/IOPCCC_2007 "IOPCCC 2007"), [CPTs](/The_Chess_Programmers_Tournament "The Chess Programmers Tournament") and [CCT Tournaments](/CCT_Tournaments "CCT Tournaments").

# Book Authors

Diep, while playing tournaments, had various book authors over the time, [Carlos Pesce](/Carlos_Pesce "Carlos Pesce") at the [WMCCC 2001](/WMCCC_2001 "WMCCC 2001"), [Eros Riccio](/Eros_Riccio "Eros Riccio") at the [WCCC 2006](/WCCC_2006 "WCCC 2006"), and [Arturo Ochoa](/Arturo_Ochoa "Arturo Ochoa") at most other tournaments.

# Descriptions

given from the [ICGA](/ICGA "ICGA") tournament site [[10]](#cite_note-10)

## 1997

```
Diep is a classical chess playing program with this exception that I try to incorporate as much chess knowledge as possible. This is hard work, but in the end I hope it will give Diep a lot.
```

## 1999

```
Started winter 1994 with DIEP. But now i'm busy with this experimental parallel program, it's called DIEP. Still using the same huge evaluation, from which as far as i know it's the most extensive chess evaluation that any chessprogram contains (although mainly middlegame/opening heuristics).
```

```
The search of DIEP is however very very selective currently. I plan to join Paderborn with a complete new search. Not only parallel, but it's closer to best first search than the depth limited alfabeta search, although it's still using the iteration to expand nodes.
```

# Features

- [Double Null Move](/Double_Null_Move "Double Null Move") [[11]](#cite_note-11)
- [Diep's Table-driven Move Generation](/Table-driven_Move_Generation#Diep "Table-driven Move Generation") [[12]](#cite_note-12) [[13]](#cite_note-13) [[14]](#cite_note-14)

# Selected Games

[WCCC 2004](/WCCC_2004 "WCCC 2004"), round 10, [Fritz](/Fritz "Fritz") - Diep [[15]](#cite_note-15) [[16]](#cite_note-16)

```
[Event "WCCC 2004"]
[Site "Ramat Gan, Israel"]
[Date "2004.07.12"]
[Round "10"]
[White "Fritz"]
[Black "Diep"]
[Result "0-1"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e5 7.Nb3 Be6 
8.f3 Nbd7 9.g4 b5 10.g5 b4 11.Ne2 Nh5 12.Qd2 a5 13.Ng3 Nxg3 14.hxg3 
a4 15.Nc1 Qa5 16.f4 Nc5 17.Bg2 a3 18.b3 Rc8 19.f5 Bd7 20.Nd3 Nxd3+ 
21.cxd3 Qb5 22.d4 Be7 23.d5 Bd8 24.Bf1 Qb7 25.Bc4 Rb8 26.O-O-O Bb6 
27.Kb1 Qa7 28.Bxb6 Qxb6 29.Rc1 Kf8 30.Rc2 Qd4 31.Qe2 Rc8 32.g6 h5 
33.g4 h4 34.Qf3 f6 35.Rd1 Qb6 36.Rh2 Ke7 37.g5 fxg5 38.Re2 Rh6 
39.Qg4 Kf6 40.Qg2 Bb5 41.Rg1 Rh5 42.Bxb5 h3 43.Qg4 Qxb5 44.Rd2 Qc5 
45.Rgd1 Rh4 46.Qg3 Qc3 47.Qh2 Qe3 48.Re2 Qf3 0-1
```

# Publications

- [Eric van Reem](/Eric_van_Reem "Eric van Reem") (**2004**). *Drei Gewinner in Leiden - Die Geschichte von Diep*. [Computerschach und Spiele](/Computerschach_und_Spiele "Computerschach und Spiele"), 6/2004 (German) » [DOCCC 2004](/DOCCC_2004 "DOCCC 2004")

# Forum Posts

## 1996 ...

- [Diep homepage](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/45a5e167338f5574/) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), November 19, 1996
- [Endgame Study Solving Competition](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/5649587638e5cd4) by [Harold van der Heijden](/Harold_van_der_Heijden "Harold van der Heijden"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), December 13, 1996
- [Unsubstantiated claim in the Diep homepage](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/11e70ee3cec6c75f) by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 17, 1997
- [The Diep Home page (more correction needed)](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d962cff95d967c3) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 21, 1997
- [The Diep Advanced Intelligence chess program](https://www.stmintz.com/ccc/index.php?id=17262) by Jan-Frode Myklebust, [CCC](/CCC "CCC"), April 20, 1998
- [DIEP parallel in Paderborn - technical and detailed story](https://www.stmintz.com/ccc/index.php?id=58505) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), June 28, 1999

## 2000 ...

- [DIEP in WMCCC2000 London - long story](https://www.stmintz.com/ccc/index.php?id=127249) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), August 29, 2000
- [DIEP would have won from Kasparov on the board](https://www.stmintz.com/ccc/index.php?id=156790) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), March 02, 2001
- [Vincent (Diep) chessbench makes the news again](https://www.stmintz.com/ccc/index.php?id=201246) by K. Burcham, [CCC](/CCC "CCC"), December 09, 2001
- [An interesting forward pruning experiment - with pseudo description](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/88409a96de93cee8) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), February 08, 2003
- [Diep as a strong sparring opponent (longish)?](https://www.stmintz.com/ccc/index.php?id=320856) by [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [CCC](/CCC "CCC"), October 13, 2003 » [Ruffian](/Ruffian "Ruffian")
- [64 bits report on diep](https://www.stmintz.com/ccc/index.php?id=373233) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), June 30, 2004
- [Diep move generator speeded up](https://www.stmintz.com/ccc/index.php?id=403656) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), January 01, 2005
- [diep's inferior evaluation](http://www.talkchess.com/forum/viewtopic.php?t=14448) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), June 12, 2007
- [Diep tested on latest AMD and Intel processors](http://www.talkchess.com/forum/viewtopic.php?t=20429) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/Computer_Chess_Forums "Computer Chess Forums"), March 31, 2008
- [Pretty move by Diep](http://www.talkchess.com/forum/viewtopic.php?t=27858) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), May 11, 2009 » [WCCC 2004, Fritz - Diep](/Diep#Fritz "Diep")

## 2010 ...

- [Diep?](http://www.talkchess.com/forum/viewtopic.php?t=32788) by [Zach Wegner](/Zach_Wegner "Zach Wegner"), [CCC](/CCC "CCC"), February 20, 2010 » [CCT12](/CCT12 "CCT12")
- [ICGA rule #2 / opening books / Diep-Crafty, Turino 2006](http://www.talkchess.com/forum/viewtopic.php?t=40853) by [Peter Berger](/Peter_Berger "Peter Berger"), [CCC](/CCC "CCC"), October 22, 2011 » [Opening Book](/Opening_Book "Opening Book"), [WCCC 2006](/WCCC_2006 "WCCC 2006")
- [Diepeveen's move generator](http://www.talkchess.com/forum/viewtopic.php?t=46056) by Hrvoje Horvatic, [CCC](/CCC "CCC"), November 18, 2012 » [Table-driven Move Generation](/Table-driven_Move_Generation "Table-driven Move Generation")
- [DIEP chess engine ever made public?](http://www.talkchess.com/forum/viewtopic.php?t=53887) by Cliff Sears, [CCC](/CCC "CCC"), September 30, 2014
- [Diep 2.0](http://www.talkchess.com/forum/viewtopic.php?t=66417) by [Brendan J. Norman](/index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](/CCC "CCC"), January 26, 2018

:   [Re: Diep 2.0](http://www.talkchess.com/forum/viewtopic.php?t=66417&start=23) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), January 26, 2018

# External Links

## Chess Program

- [Vincent Diepeveen en het schaakprogramma Diep](http://oudzuylenutrecht.nl/utrecht/diep/) from [Schaakclub Oud Zuylen Utrecht](http://oudzuylenutrecht.nl/) (Dutch)
- [Diep lachende derde in het NK en Kramnik versus de witte-boorden-maffia](http://oudzuylenutrecht.nl/nk-2002/) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [Schaakclub Oud Zuylen Utrecht](http://oudzuylenutrecht.nl/) (Dutch)
- [Super Diep](http://oudzuylenutrecht.nl/wk-2003/) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [Schaakclub Oud Zuylen Utrecht](http://oudzuylenutrecht.nl/) (Dutch)
- [Permission to use code](http://mridulm.blogspot.de/2004/06/permission-to-use-code-have-to-put-up.html) from [Random thoughts](http://mridulm.blogspot.de/) by [Mridul Muralidharan](/Mridul_Muralidharan "Mridul Muralidharan"), June 09, 2004 » [Diep's Table-driven Move Generation](/Table-driven_Move_Generation#Diep "Table-driven Move Generation")
- [Diep's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=26)
- [The chess games of Diep](http://www.chessgames.com/perl/chessplayer?pid=85687) from [chessgames.com](http://www.chessgames.com/index.html)
- [Diep](http://www.chessclub.com/finger/DIEP) from [Internet Chess Club](/index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")

## Misc

- [Hollands Diep from Wikipedia](https://en.wikipedia.org/wiki/Hollands_Diep)

# References

1. [↑](#cite_ref-1) [Diep in Polen](http://oudzuylenutrecht.nl/opppc-2007/) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [Schaakclub Oud Zuylen Utrecht](http://oudzuylenutrecht.nl/) (Dutch)
2. [↑](#cite_ref-2) [Re: Diep 2.0](http://www.talkchess.com/forum/viewtopic.php?t=66417&start=23) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), January 26, 2018
3. [↑](#cite_ref-3) [Diep Nederlands kampioen 2004!](http://oudzuylenutrecht.nl/diep-nederlands-kampioen-2004/) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [Schaakclub Oud Zuylen Utrecht](http://oudzuylenutrecht.nl/) (Dutch)
4. [↑](#cite_ref-4) [Diep derde op het WK 2004!](http://oudzuylenutrecht.nl/wk-2004/) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [Schaakclub Oud Zuylen Utrecht](http://oudzuylenutrecht.nl/) (Dutch)
5. [↑](#cite_ref-5) [Unsubstantiated claim in the Diep homepage](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/11e70ee3cec6c75f) by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 17, 1997
6. [↑](#cite_ref-6) [Let's stop wasting time on Vincent Diepeveen](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a20a25fbec56fd82) by [Dap Hartmann](/Dap_Hartmann "Dap Hartmann"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 23, 1997
7. [↑](#cite_ref-7) [Peter Kouwenhoven](/Peter_Kouwenhoven "Peter Kouwenhoven") (**1997**). *DIEP, Deep Trouble*. [ICCA Journal](/ICGA_Journal "ICGA Journal"), Vol. 20, No. 3, pp. 200-203
8. [↑](#cite_ref-8) [Diep in Parijs](http://oudzuylenutrecht.nl/wk-1997/) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [Schaakclub Oud Zuylen Utrecht](http://oudzuylenutrecht.nl/) (Dutch)
9. [↑](#cite_ref-9) [Super Diep](http://oudzuylenutrecht.nl/wk-2003/) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [Schaakclub Oud Zuylen Utrecht](http://oudzuylenutrecht.nl/) (Dutch)
10. [↑](#cite_ref-10) [Diep's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=26)
11. [↑](#cite_ref-11) [Re: Null move?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/3eb37f017c1857fe/) post 4 by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 11, 1997
12. [↑](#cite_ref-12) [Permission to use code](http://mridulm.blogspot.de/2004/06/permission-to-use-code-have-to-put-up.html) from [Random thoughts](http://mridulm.blogspot.de/) by [Mridul Muralidharan](/Mridul_Muralidharan "Mridul Muralidharan"), June 09, 2004
13. [↑](#cite_ref-13) [Diep move generator speeded up](https://www.stmintz.com/ccc/index.php?id=403656) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/Computer_Chess_Forums "Computer Chess Forums"), January 01, 2005
14. [↑](#cite_ref-14) [Re: What's the fastest move generator?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=480726&t=44939) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), August 30, 2012
15. [↑](#cite_ref-15) [Ramat-Gan 2004 - Chess - Round 10 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=24&round=10&id=3)
16. [↑](#cite_ref-16) [Pretty move by Diep](http://www.talkchess.com/forum/viewtopic.php?t=27858) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), May 11, 2009

**[Up one level](/Engines "Engines")**