# ZChess

Source: https://www.chessprogramming.org/ZChess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* ZChess**

**ZChess**,  
a [WinBoard](/WinBoard "WinBoard") compatible chess engine by [Franck Zibi](/Franck_Zibi "Franck Zibi"), written in [C++](/Cpp "Cpp"), in April 2001 renamed to [Pharaon](/Pharaon "Pharaon"). ZChess evolved from a [C](/C "C") port of [HpChess](/HpChess "HpChess") incorporating [object oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) paradigms, and using a [bitboard](/Bitboards "Bitboards") board representation [[1]](#cite_note-1) and in particular [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") to generate sliding piece attacks.
ZChess applies [PVS](/Principal_Variation_Search "Principal Variation Search") with [iterative deepening](/Iterative_Deepening "Iterative Deepening") and [aspiration windows](/Aspiration_Windows "Aspiration Windows"), using a [transposition table](/Transposition_Table "Transposition Table") with multiple probes, [pawn-](/Pawn_Hash_Table "Pawn Hash Table") and [king safety](/King_Safety "King Safety") [hash tables](/Hash_Table "Hash Table"), [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") for [move ordering](/Move_Ordering "Move Ordering") and [pruning](/Pruning "Pruning"), [adaptive null move pruning](/Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") with [R](/Depth_Reduction_R "Depth Reduction R") = 2, 3, and heavily prunes not only in [quiescence search](/Quiescence_Search "Quiescence Search"). Move ordering considers [hash-table move](/Hash_Move "Hash Move"), winning [captures](/Captures "Captures") by SEE, [killer heuristic](/Killer_Heuristic "Killer Heuristic"), [counter move heuristic](/Countermove_Heuristic "Countermove Heuristic"), and [history heuristic](/History_Heuristic "History Heuristic") [[2]](#cite_note-2).

# Tournaments

ZChess had its debut at the [FCCC 1997](/FCCC_1997 "FCCC 1997") and became runner up behind [Chess Wizard](/Chess_Wizard "Chess Wizard") at the [FCCC 1998](/FCCC_1998 "FCCC 1998"). It further participated at the [WMCCC 2000](/WMCCC_2000 "WMCCC 2000") in London, the [IPCCC 2001](/IPCCC_2001 "IPCCC 2001") and [CCT2](/CCT2 "CCT2") online tournament, before it was renamed to [Pharaon](/Pharaon "Pharaon"). Against humans, ZChess 1.2 played the [1999 Aubervilliers Tournament](/Aubervilliers_Rapid_Open#1999 "Aubervilliers Rapid Open"), scoring 9½/12 (one loss) with a [TPR](https://en.wikipedia.org/wiki/Performance_rating_%28chess%29#Performance_rating) of 2300 [Elo](https://en.wikipedia.org/wiki/Elo_rating_system) [[3]](#cite_note-3).

# Selected Games

## FCCC 1998

[FCCC 1998](/FCCC_1998 "FCCC 1998"), round 10, ZChess - [Chess Guru](/Chess_Guru "Chess Guru")

```
[Event "6th French CCC"]
[Site "Clichy, FRA"]
[Date "1998.09.27"]
[Round "10"]
[White "ZChess"]
[Black "Chess Guru"]
[Result "1-0"]
[ECO "B81"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.g4 h6 7.Rg1 Be7 8.Be3
Nc6 9.Qf3 Bd7 10.O-O-O Nxd4 11.Rxd4 Qa5 12.Rd1 Bc6 13.g5 hxg5 14.Rxg5 
d5 15.Rxg7 dxe4 16.Qf4 Kf8 17.Rg2 Nh5 18.Qg4 Bb4 19.Nb1 Nf6 20.Qg7+ 
Ke7 21.Rg5 Bd5 22.Rg6 Nh7 23.Rh6 Rag8 24.Bg5+ Ke8 25.Qe5 f6 26.Bxf6 
Nxf6 27.Rxf6 Ke7 28.a3 Bc4 29.Qf4 Qh5 30.axb4 e5 31.Qxe4 Kxf6 32.Bxc4 
Rd8 33.Nd2 Rd7 34.f4 Ke7 35.Bb5 Rdd8 36.Qxb7+ Kf8 37.Qc7 Qh4 38.fxe5
Rh7 39.Qc5+ Kg8 40.Rg1+ Kh8 41.e6 Qf6 42.Ne4 Qf4+ 43.Kb1 Qxe4 44.Qc3+ 
Qd4 45.Rd1 1-0
```

## WMCCC 2000

[WMCCC 2000](/WMCCC_2000 "WMCCC 2000"), round 6, [Junior](/Junior "Junior") - ZChess [[4]](#cite_note-4) [[5]](#cite_note-5)

```
[Event "WMCCC 2000"]
[Site "London, UK"]
[Date "2000.08.24"]
[Round "6"]
[White "Junior"]
[Black "ZChess"]
[Result "1/2-1/2"]

1.e4 c6 2.d4 d5 3.Nd2 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 Bd6 
8.Qe2 h6 9.Ne4 Nxe4 10.Qxe4 Qc7 11.Qg4 Kf8 12.O-O c5 13.Re1 b6 14.c3 
Bb7 15.h4 Rd8 16.Qh3 Bf4 17.a4 Bxc1 18.Raxc1 Qf4 19.Qg3 Qxg3 20.fxg3 
Ke7 21.Bb5 a5 22.Rcd1 g5 23.d5 Nf6 24.c4 Rhg8 25.Rd2 Rd6 26.b3 Rg7 
27.Rde2 Ng4 28.Nd2 Nf6 29.hxg5 hxg5 30.Nf3 Ng4 31.Re4 Nh6 32.g4 Kd8 
33.R4e2 Rg6 34.Ne5 Rf6 35.Re3 exd5 36.cxd5 Rxd5 37.Nc4 Kc8 38.Re8+ Rd8 
39.Rxd8+ Kxd8 40.Rd1+ Kc7 41.Rd7+ Kb8 42.Rd8+ Kc7 43.Rd7+ Kb8 1/2-1/2
```

# See also

- [Pharaon](/Pharaon "Pharaon")
- [Z-Chess](/Z-Chess "Z-Chess")

# Forum Posts

- [ANN : ZChess 2.0 (London) Released](https://www.stmintz.com/ccc/index.php?id=127888) by [Franck Zibi](/Franck_Zibi "Franck Zibi"), [CCC](/CCC "CCC"), September 02, 2000
- [ZChess 2.0 running the gauntlet](https://www.stmintz.com/ccc/index.php?id=127895) by CLiebert, [CCC](/CCC "CCC"), September 02, 2000
- [ZChess getting much stronger...](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=32639) by CLiebert, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 10, 2000
- [ZChess 2.00 (London) in concerto !](http://www.talkchess.com/forum/viewtopic.php?t=46037) by [Ruxy Sylwyka](http://www.talkchess.com/forum/profile.php?mode=viewprofile&u=881), [CCC](/CCC "CCC"), November 17, 2012

# External Links

- [ZChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=124) (includes [Pharaon](/Pharaon "Pharaon"))
- [Pharaon History](http://www.fzibi.com/pharaon/history.htm)
- [ZChess at the 1999 Aubervilliers Tournament](http://www.fzibi.com/pharaon/auber99.htm) » [Aubervilliers Rapid Open 1999](/Aubervilliers_Rapid_Open#1999 "Aubervilliers Rapid Open")
- [Meet the Authors](http://www.rebel.nl/authors.htm) by [Ed Schröder](/Ed_Schroder "Ed Schroder")
- [Comp ZChess 1.2 chess games - 365Chess.com](http://www.365chess.com/players/Comp_ZChess_1.2)

# References

1. [↑](#cite_ref-1) [Introduction to Bitboards](http://www.fzibi.com/cchess/bitboards.htm) by [Franck Zibi](/Franck_Zibi "Franck Zibi")
2. [↑](#cite_ref-2) [Pharaon History](http://www.fzibi.com/pharaon/history.htm)
3. [↑](#cite_ref-3) [ZChess at the 1999 Aubervilliers Tournament](http://www.fzibi.com/pharaon/auber99.htm)
4. [↑](#cite_ref-4) [London 2000 - Chess - Round 6 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=31&round=6&id=5)
5. [↑](#cite_ref-5) [Junior-zchess is going to be a draw](https://www.stmintz.com/ccc/index.php?id=125984) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), August, 24, 2000

**[Up one level](/Engines "Engines")**