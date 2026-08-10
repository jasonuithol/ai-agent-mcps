# Plisk

Source: https://www.chessprogramming.org/Plisk

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Plisk**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Egg-rmh.jpg/330px-Egg-rmh.jpg)](/File:Egg-rmh.jpg)

A broken wild bird eggshell [[1]](#cite_note-1)

**Plisk**, (PliskChess)  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](/UCI "UCI") compliant chess engine by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"),
written in [C++](/Cpp "Cpp"), first released in June 2009 [[2]](#cite_note-2).
Its development started in January 2009, when Plisk evolved from Vlad's earlier engine **fastthink** with a completely re-written [search](/Search "Search") [[3]](#cite_note-3).
Plisk played the [ACCA 2010](/ACCA_2010 "ACCA 2010"), [ACCA 2011](/ACCA_2011 "ACCA 2011"), and the [WCRCC 2010](/WCRCC_2010 "WCRCC 2010"). Since version 0.2.4o, binaries are available for [Windows](/Windows "Windows"), [Linux](/Linux "Linux") and [Mac OS](/Mac_OS "Mac OS").

# Features

[[4]](#cite_note-4)

- [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards")
- [Parallel Search](/Parallel_Search "Parallel Search")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta") [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Delta Pruning](/Delta_Pruning "Delta Pruning") in QS
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Check Extensions](/Check_Extensions "Check Extensions")
- [Opening Book](/Opening_Book "Opening Book") (own format)
- [Perft](/Perft "Perft")
- [Pondering](/Pondering "Pondering")

# Acknowledgments

[[5]](#cite_note-5)

- Detecting if there is a key press in the pipe - from [Glaurung](/Glaurung "Glaurung"), from [Beowulf](/Beowulf "Beowulf"), from [OliThink](/OliThink "OliThink")
- Idea of doing a [futility check](/Futility_Pruning "Futility Pruning") for each move that is accepted in QS (rather than once per QS node) - from [Stockfish](/Stockfish "Stockfish")
- Non-constant [LMR](/Late_Move_Reductions "Late Move Reductions") [depth reduction](/Depth_Reduction_R "Depth Reduction R"), but use either linear or logarithmical - from [Stockfish](/Stockfish "Stockfish")
- [Rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") for [move generation](/Move_Generation "Move Generation") (and other tasks) - from [Crafty](/Crafty "Crafty") and [Robert Hyatt](/Robert_Hyatt "Robert Hyatt")
- [Material imbalance ideas](/Material_Tables "Material Tables") - from [Larry Kaufman](/Larry_Kaufman "Larry Kaufman")
- [Evaluate](/Evaluation "Evaluation") [King Safety](/King_Safety "King Safety") with identifying what squares in kings' vicinity are attacked but not defended, or only defended by the king itself - from [Stockfish](/Stockfish "Stockfish")
- [SplitMP](/Parallel_Search "Parallel Search") and other MP related ideas (where to synch, lock, the fact that in split nodes you do not need to do [null move](/Null_Move_Pruning "Null Move Pruning"), [razoring](/Razoring "Razoring"), etc.) - from [Viper](/Viper "Viper"), from [Stockfish](/Stockfish "Stockfish")

# Selected Games

[WCRCC 2010](/WCRCC_2010 "WCRCC 2010"), round 8, Plisk - [Telepath](/Telepath "Telepath") [[6]](#cite_note-6)

```
[Event "WCRCC 2010"]
[Site "Internet Chess Club"]
[Date "2010.07.18"]
[Round "8"]
[White "Plisk"]
[Black "Telepath"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e5 7.Nf3 Be7 8.Bc4 O-O 9.O-O Be6 
10.Bxe6 fxe6 11.Qd2 Nc6 12.Rad1 Ng4 13.Qe2 Nxe3 14.Qxe3 b5 15.Rd2 Qe8 16.Rfd1 Rb8 
17.Ne2 Qf7 18.Ng3 Rfc8 19.h3 b4 20.Qe2 a5 21.Qd3 Nd8 22.a3 bxa3 23.Qxa3 Rc5 24.c3 Nc6 
25.Re1 Rcb5 26.Qa4 R8b6 27.Ra1 d5 28.Qa2 Rb3 29.Rad1 Bf6 30.Qa4 d4 31.Rc1 g6 32.cxd4
R3b4 33.Rxc6 Rxa4 34.Rxb6 exd4 35.e5 Qc7 36.Rxe6 Be7 37.Ne4 d3 38.Rxe7 Qxe7 39.Nf6+ 
Kf7 40.Rxd3 Ke6 41.Nxh7 Qb4 42.Kh2 Qc4 43.Rd6+ Ke7 44.Rf6 Qa2 45.Nf8 Qxb2 46.Nxg6+ Kd8 
47.Ng5 Kc7 48.Rf7+ Kc6 49.e6 Ra1 50.Nf3 Qb8+ 51.Nfe5+ Kd5 52.e7 Qe8 53.Rf8 Qxe7 54.Nxe7+ 
Kxe5 55.Ng6+ Ke6 56.Nf4+ Ke7 57.Ra8 Ra2 58.Kg3 Kf6 59.h4 Ra3+ 60.Kg4 Ra1 61.Ra6+ Ke5 
62.h5 Rb1 63.Rxa5+ Kd6 64.Ra7 Rb8 65.h6 Rg8+ 66.Rg7 Rh8 67.h7 Ke5 68.Rf7 Kd6 69.Ng6 Ra8 
70.Nf8 Rb8 71.h8=Q Rb7 72.Rxb7 Kc6 73.Rb5 Kxb5 74.Qc3 Ka6 75.Qb3 Ka5 76.Nd7 Ka6 77.Qb6# 
1-0
```

# Forum Posts

## 2009

- [New winboard engine: Plisk](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50232) by [Olivier Deville](/Olivier_Deville "Olivier Deville"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), June 26, 2009
- [Plisk 0.0.6](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50251) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 09, 2009
- [Plisk](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50347) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 20, 2009

## 2010 ...

- [Plisk 0.2.1](http://www.talkchess.com/forum/viewtopic.php?t=33621) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), April 05, 2010
- [New release: Plisk 022](http://www.talkchess.com/forum/viewtopic.php?t=34135) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), May 03, 2010
- [Plisk 023h](http://www.talkchess.com/forum/viewtopic.php?t=34310) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), May 15, 2010
- [Plisk 024 release](http://www.talkchess.com/forum/viewtopic.php?t=35006) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), June 17, 2010
- [WCRCC 2010 - Plisk games](http://www.talkchess.com/forum/viewtopic.php?t=35471) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), July 17, 2010 » [WCRCC 2010](/WCRCC_2010 "WCRCC 2010")
- [Plisk 025 released](http://www.talkchess.com/forum/viewtopic.php?t=35557) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), July 23, 2010
- [Plisk 025](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=51102) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 23, 2010
- [Plisk 0.2.5n 64-bit - CCRL 40/4 Results](http://www.talkchess.com/forum/viewtopic.php?t=35732) by [Adam Hair](/Adam_Hair "Adam Hair"), [CCC](/CCC "CCC"), August 08, 2010
- [New Plisk 027d](http://www.talkchess.com/forum/viewtopic.php?t=36685) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), November 13, 2010
- [2011 ACCA Pan American CCC - Plisk games](http://www.talkchess.com/forum/viewtopic.php?t=41058) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), November 12, 2011 » [ACCA 2011](/ACCA_2011 "ACCA 2011")

# External Links

## Chess Engine

- [PliskChess](https://sites.google.com/site/pliskchess/)
- [Plisk 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Plisk&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")

## Misc

- [plisk - Wiktionary](https://en.wiktionary.org/wiki/plisk)
- [Urban Dictionary: Plisk](https://www.urbandictionary.com/define.php?term=plisk)

# References

1. [↑](#cite_ref-1) A broken wild bird [eggshell](https://en.wikipedia.org/wiki/Eggshell), [Photo](https://commons.wikimedia.org/wiki/File:Egg-rmh.jpg) by [Kim Pardi](https://www.flickr.com/photos/rockymountainhigh/), June 21, 2005, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [New winboard engine: Plisk](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50232) by [Olivier Deville](/Olivier_Deville "Olivier Deville"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), June 26, 2009
3. [↑](#cite_ref-3) [PliskChess - History](https://sites.google.com/site/pliskchess/)
4. [↑](#cite_ref-4) [PliskChess - Features](https://sites.google.com/site/pliskchess/)
5. [↑](#cite_ref-5) The creation of Plisk could not have been possible without the help of other people, ideas and programs. Below is a list of some influences... plisk\_027\_d\_linux.zip/thanks.txt
6. [↑](#cite_ref-6) [Re: WCRCC 2010 - Plisk games](http://www.talkchess.com/forum/viewtopic.php?t=35471&start=6) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), July 18, 2010

**[Up one level](/Engines "Engines")**