# Cheiron

Source: https://www.chessprogramming.org/Cheiron

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Cheiron**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Chiron_instructs_young_Achilles_-_Ancient_Roman_fresco.jpg/250px-Chiron_instructs_young_Achilles_-_Ancient_Roman_fresco.jpg)](/File:Chiron_instructs_young_Achilles_-_Ancient_Roman_fresco.jpg)

[Cheiron](https://de.wikipedia.org/wiki/Cheiron) and [Achilles](https://en.wikipedia.org/wiki/Achilles) [[1]](#cite_note-1)

**Cheiron**,  
a chess program by [Ulf Lorenz](/Ulf_Lorenz "Ulf Lorenz"). [Cheiron](https://de.wikipedia.org/wiki/Cheiron) is the German spelling of [Chiron](https://en.wikipedia.org/wiki/Chiron), a [centaur](https://en.wikipedia.org/wiki/Centaur) creature of the [Greek mythology](https://en.wikipedia.org/wiki/Greek_mythology). The program played the [8th World Computer Chess Championship 1995](/WCCC_1995 "WCCC 1995") in [Shatin](https://en.wikipedia.org/wiki/Sha_Tin), [Hong Kong](https://en.wikipedia.org/wiki/Hong_Kong) and the [13th World Microcomputer Chess Championship 1995](/WMCCC_1995 "WMCCC 1995") in [Paderborn](https://en.wikipedia.org/wiki/Paderborn), the [IPCCC 1994](/IPCCC_1994 "IPCCC 1994") and [IPCCC 1997](/IPCCC_1997 "IPCCC 1997"), and the [Aegon 1996](/Aegon_1996 "Aegon 1996") and [Aegon 1997](/Aegon_1997 "Aegon 1997") man-machine tournaments.

# Description

from the [ICGA](/ICGA "ICGA")-site [[2]](#cite_note-2):

```
In Greek mythology, Cheiron was the wisest of all centaurs and the teacher of many heroes. The program Cheiron is written in C. It is an alpha-beta program using most of the known state-of-the-art heuristics including killer heuristics, transposition table, aspiration search, plausible move ordering, iterative deepening, selective deepening etc. Null moves, however, are not used. The quiescence search is quite large and examines some tactical motifs, particularly mating and promotion threats.
```

```
Apart from the move generator, the evaluation function is the most expensive part of the program. It examines the pawn structure, king's security, static positions of the pieces, everlasting knights etc. as well as special situations in the endgame (e.g. there are positions when two pawns are more worth than a rook).
```

```
On a Pentium 90MHz the program will search about 10,000 nodes per second. Cheiron is more a positional playing than a tactical playing program. Cheiron uses an opening book containing about 12,000 positions to get a good start into the game. Using the Bednorz-Toennissen test, Cheiron has an estimated rating of 2100 ELO on a 50MHz PC. Tournament results against humans supports this number. Originally, the program was developed for Unix boxes, but a version has been developed with a graphical interface using Turbo C in a DOS-Windows 3.1 environment.
```

# Selected Games

## WCCC 1995

[WCCC 1995](/WCCC_1995 "WCCC 1995"), round 1, [Gandalf](/Gandalf "Gandalf") - Cheiron [[3]](#cite_note-3)

```
[Event "WCCC 1995"]
[Site "Shatin, Hong Kong"]
[Date "1995.05.25"]
[Round "1"]
[White "Gandalf"]
[Black "Cheiron"]
[Result "0-1"]

1.e4 e6 2.d4 c5 3.Nf3 cxd4 4.Nxd4 Nf6 5.Bd3 Be7 6.O-O Nc6 7.Be3 O-O 8.Nc3 d6 9.Nxc6 bxc6 10.f3 d5 
11.e5 d4 12.exf6 Bxf6 13.Bxd4 Qxd4+ 14.Kh1 Rb8 15.Rb1 Rd8 16.Qe2 Bb7 17.a3 Be5 18.Rfe1 Bc7 19.Qe4 
Qxe4 20.Nxe4 Rd5 21.g3 c5 22.Kg2 Rbd8 23.h3 Bb6 24.b3 Rd4 25.Re3 R4d7 26.Re2 Rd5 27.Bc4 Rd1 28.Rxd1 
Rxd1 29.h4 g6 30.Kf2 Kf8 31.Re1 Rxe1 32.Kxe1 Ke7 33.g4 f5 34.Ng5 h6 35.Nxe6 Bxf3 36.gxf5 gxf5 37.c3 
Kd6 38.Kd2 Bd5 39.Bxd5 Kxd5 40.Nf4+ Ke4 41.Nd3 f4 42.h5 c4 43.bxc4 Be3+ 44.Kc2 f3 45.a4 f2 46.Nxf2+ 
Bxf2 47.a5 0-1
```

## Aegon 1996

[Aegon 1996](/Aegon_1996 "Aegon 1996"), round 4, Cheiron - [Sofia Polgár](https://en.wikipedia.org/wiki/Sofia_Polg%C3%A1r) [[4]](#cite_note-4)

```
[Event "AEGON 1996"]
[Site "The Hague NED"]
[Date "1996.04.15"]
[Round "4"]
[White "Cheiron"]
[Black "Sofia Polgar"]
[Result "1/2-1/2"]

1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 Bg4 6.Be2 e6 7.O-O Nc6 8.Be3 cxd4 9.cxd4 Bb4 10.Nc3 Qd6 
11.a3 Ba5 12.Nb5 Qb8 13.h3 Bh5 14.g4 Bg6 15.Qc1 Nd5 16.Nh4 Bd8 17.g5 Nce7 18.Nc3 O-O 19.Nxg6 hxg6 
20.Nxd5 Nxd5 21.Bf3 Qd6 22.Qc5 Qd7 23.Rac1 Bb6 24.Qc4 Qd6 25.Bxd5 exd5 26.Qb5 Rfe8 27.Rfd1 Bc7 28.Kf1 
Bb6 29.Re1 Re4 30.Kg2 Qe6 31.Rh1 Re8 32.Qd3 Qf5 33.Qd2 Kh7 34.a4 Rh4 35.f4 f6 36.gxf6 Qxf6 37.Qf2 Re4 
38.Rhd1 Bd8 39.Rd3 Qf5 40.Qg3 g5 41.fxg5 Reg4 42.hxg4 Rxg4 43.Qxg4 Qxg4+ 44.Kf2 Qh4+ 45.Ke2 Qh2+ 
46.Bf2 Qh5+ 47.Kf1 Qh1+ 48.Bg1 Kg6 49.Rg3 Qe4 50.Re1 Qf5+ 51.Bf2 Bc7 52.Rge3 1/2-1/2
```

# See also

- [Achilles](/Achilles "Achilles")
- [Centaur](/Centaur "Centaur")
- [Chiron](/Chiron "Chiron")

# Forum Posts

- [AEGON 1997 breakdown of opponents from their webpage](https://groups.google.com/d/msg/rec.games.chess.misc/7fcqu7_2Rr4/WR5IijMqDF0J) by Lonnie, [rgcm](/Computer_Chess_Forums "Computer Chess Forums"), April 11, 1997 » [Aegon 1997](/Aegon_1997 "Aegon 1997")

# External Links

## Chess Program

- [Cheiron's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=188)
- [Comp Cheiron chess games - 365Chess.com](https://www.365chess.com/players/Comp_Cheiron)

## Misc

- [Cheiron – Wikipedia.de](https://de.wikipedia.org/wiki/Cheiron) (German)
- [Chiron (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Chiron_(disambiguation))
- [Chiron from Wikipedia](https://en.wikipedia.org/wiki/Chiron)
- [Category:Chiron - Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Chiron?uselang=en)
- [Corvus Corax](https://en.wikipedia.org/wiki/Corvus_Corax_(band)) - [Cheiron](https://www.discogs.com/de/composition/3ea755eb-36be-4fcb-aee8-dd4714e85497-Cheiron), April 14, 2019 at [Moscow](https://en.wikipedia.org/wiki/Moscow) [Station Hall](https://station-hall.ru/), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) The [fresco](https://en.wikipedia.org/wiki/Fresco) shows the [centaur](https://en.wikipedia.org/wiki/Centaur) [Chiron](https://en.wikipedia.org/wiki/Chiron), pedagogue of [Achilles](https://en.wikipedia.org/wiki/Achilles), who teaches the still young man the use of the [cithara](https://en.wikipedia.org/wiki/Cithara). The prototype for this fresco was not another painting but a statue that [Pliny the Elder](https://en.wikipedia.org/wiki/Pliny_the_Elder) remembered was exhibited in [Rome](https://en.wikipedia.org/wiki/Rome) in [Saepta Julia](https://en.wikipedia.org/wiki/Saepta_Julia). [National Archaeological Museum, Naples (inv. Nr. 9109)](https://en.wikipedia.org/wiki/National_Archaeological_Museum,_Naples), from [Herculaneum](https://en.wikipedia.org/wiki/Herculaneum), [Augusteum](https://en.wikipedia.org/wiki/Augusteum) - [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Cheiron's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=188)
3. [↑](#cite_ref-3) [Shatin 1995 - Chess - Round 1 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=29&round=1&id=5)
4. [↑](#cite_ref-4) [Aegon round 4](https://groups.google.com/d/msg/rec.games.chess.misc/X06MxKpsLJ4/0wuwy6054VEJ) by Alastair Scott, [rgcm](/Computer_Chess_Forums "Computer Chess Forums"), April 16, 1996

**[Up one Level](/Engines "Engines")**