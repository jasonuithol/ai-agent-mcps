# Ant

Source: https://www.chessprogramming.org/Ant

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Ant**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Scheme_ant_worker_anatomy-en.svg/330px-Scheme_ant_worker_anatomy-en.svg.png)](/File:Scheme_ant_worker_anatomy-en.svg)

Basic morphology of a worker ant [[1]](#cite_note-1)

**Ant**,  
a [WinBoard](/WinBoard "WinBoard") compatible chess engine by [Tom Vijlbrief](/Tom_Vijlbrief "Tom Vijlbrief"), written in [C++](/Cpp "Cpp"), at times supported by [Hans Secelle](/Hans_Secelle "Hans Secelle") [[2]](#cite_note-2) and [Albrecht Heeffer](/Albrecht_Heeffer "Albrecht Heeffer"). Ant regularly participates at [Dutch Open Computer Chess Championships](/Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship") and [International CSVN Tournaments](/International_CSVN_Tournament "International CSVN Tournament") and had its debut at the [DOCCC 1995](/DOCCC_1995 "DOCCC 1995"). It further played the [Aegon 1996](/Aegon_1996 "Aegon 1996") and [Aegon 1997](/Aegon_1997 "Aegon 1997") human machine tournaments, the [IPCCC 1998](/IPCCC_1998 "IPCCC 1998"), and the [Livingston Chess960 Computer World Championships](/Livingston_Chess960_Computer_World_Championship "Livingston Chess960 Computer World Championship") in [2005](/Chess960CWC_2005 "Chess960CWC 2005") and [2006](/Chess960CWC_2006 "Chess960CWC 2006").

# Photos & Games

## Ant beats Tiger

[![Leiden02ict2002.jpg](/images/b/b3/Leiden02ict2002.jpg)](http://en.chessbase.com/post/a-black-day-for-france/30)

[ICT 2002](/ICT_2002 "ICT 2002"): round 2, Ant - [Chess Tiger](/Chess_Tiger "Chess Tiger"), [Hans Secelle](/Hans_Secelle "Hans Secelle") and [Hans van der Zijden](/Hans_van_der_Zijden "Hans van der Zijden") [[3]](#cite_note-3) [[4]](#cite_note-4)

```
[Event "ICT 2002"]
[Site "Leiden NED"]
[Date "2002.05.31"]
[Round "02"]
[White "Ant"]
[Black "Chess Tiger"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.c3 Nf6 4.d4 Nxe4 5.d5 Ne7 6.Nxe5 Ng6 7.Nxg6 hxg6 8.Qe2 Qe7 
9.Bf4 d6 10.Na3 Bf5 11.f3 Nf6 12.Qxe7+ Bxe7 13.Bb5+ Nd7 14.g4 g5 15.Be3 Bg6 16.O-O 
a6 17.Bxd7+ Kxd7 18.Rf2 Bf6 19.Rd1 Rae8 20.Bc1 Rh3 21.Nc4 Reh8 22.Ne3 Be5 23.Nf1 f6 
24.Be3 Re8 25.Kg2 Rh7 26.c4 b5 27.c5 dxc5 28.Bxc5 Reh8 29.Kg1 Bf7 30.b3 Rh3 31.Rd3 
R8h4 32.Rd1 Bg8 33.Kh1 Rh6 34.Rd3 Bf7 35.a4 R6h4 36.axb5 axb5 37.Rg2 Bg6 38.Re3 Kc8 
39.b4 Bf7 40.Rd3 c6 41.Ra2 Bxd5 42.Ra8+ Kd7 43.Ra7+ Ke8 44.Re7+ Kd8 45.Kg2 Bb2
46.Rxg7 Rh6 47.Re3 Rh8 48.Ree7 Bxf3+ 49.Kg1 Bxg4 50.Rb7 Be5 51.Ra7 Bd7 52.Raxd7+ Kc8 
53.Ra7 Kb8 54.Rgb7+ Kc8 55.Rb6 R8h7 56.Rxc6+ Kb8 57.Ra5 Kb7 58.Rb6+ Kc8 59.Kg2 Kd7 
60.Ra7+ Kc8 61.Rc6+ Kb8 62.Ra5 Rb3 63.Rxb5+ Rb7 64.Bd6+ Bxd6 65.Rxb7+ Kxb7 66.Rxd6 
Rb2+ 67.Kf3 f5 68.Rd5 Rb3+ 69.Ke2 Rb2+ 70.Nd2 Rxb4 71.Rxf5 g4 72.Ke3 Ra4 73.Ne4 Kb6 
74.Rf6+ Kc7 75.Nf2 Kd7 76.Rg6 Ra3+ 77.Ke4 Ra4+ 78.Kf5 Ra5+ 79.Kxg4 Ra2 80.Kf3 Ra3+
81.Kf4 Ke7 82.h4 Ra5 83.Rg5 Ra4+ 84.Ne4 Ra2 85.h5 Rh2 86.Rg7+ Kf8 87.Rh7 Kg8 88.Ra7 
Rh4+ 89.Kf5 Kf8 90.Kf6 Rf4+ 91.Kg6 Rxe4 92.Ra8+ 1-0
```

## Ant draws Shredder

[ICT 2005](/ICT_2005 "ICT 2005"), round 9, Ant - [Shredder](/Shredder "Shredder") [[5]](#cite_note-5)

```
[Event "ICT 2005"]
[Site "Leiden NED"]
[Date "2005.06.05"]
[Round "9"]
[White "Ant"]
[Black "Shredder"]
[Result "1/2-1/2"]

1.d4 d5 2.c4 dxc4 3.e3 Nf6 4.Bxc4 e6 5.Nf3 a6 6.O-O c5 7.Bd3 Nbd7 8.Re1 b6 9.e4 cxd4 
10.e5 Nd5 11.Nxd4 Bb7 12.Nxe6 fxe6 13.Qh5 Ke7 14.Bxh7 Qc7 15.Bg5 N5f6 16.exf6 gxf6 
17.Bd2 Qc5 18.Qxc5 Nxc5 19.Bc2 Rd8 20.Be3 Bh6 21.f4 Nd3 22.Bxd3 Rxd3 23.g3 Bg7 24.Nc3 
Bf3 25.h4 f5 26.Bxb6 Rb8 27.Bc5 Kf7 28.Rab1 Bxc3 29.bxc3 Rxb1 30.Rxb1 Bd5 31.Bf2 Rxc3 
32.Ra1 Ra3 33.Kf1 Kg6 34.Ke2 a5 35.Kd2 1/2-1/2
```

# When Ants Play Chess

- [Alexis Drogoul](/index.php?title=Alexis_Drogoul&action=edit&redlink=1 "Alexis Drogoul (page does not exist)") (**1993, 1995**). *When Ants Play Chess (Or Can Strategies Emerge From Tactical Behaviors?)* [MAAMAW ’93](http://www.informatik.uni-trier.de/~ley/db/conf/maamaw/maamaw1993.html#Drogoul93), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.50.4902) [pdf](http://www2.hawaii.edu/~nreed/ics606/papers/drogoul95when.pdf)

# See also

- [Jaglavak](/Jaglavak "Jaglavak")
- [Matant](/Matant "Matant")

# Forum Posts

- [Ant 4.13 (Dutch-ch 99 Leiden) !](https://www.stmintz.com/ccc/index.php?id=76858) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), November, 08, 1999
- [Dutch Championship : Nimzo 8 - Ant](https://www.stmintz.com/ccc/index.php?id=133006) by [Johan Havegheer](/Johan_Havegheer "Johan Havegheer"), [CCC](/CCC "CCC"), October, 14, 2000
- [Trapper Ant](https://www.stmintz.com/ccc/index.php?id=297022) by [Ulrich Türke](/Ulrich_T%C3%BCrke "Ulrich Türke"), [CCC](/CCC "CCC"), May 18, 2003

# External Links

## Chess Engine

- [Index of /chess/engines/Norbert's collection/ANT aka GI-ANT (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/ANT%20aka%20GI-ANT%20%28Compilation%29/) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [The chess games of Ant (Computer)](http://www.chessgames.com/perl/chessplayer?pid=103281) from [chessgames.com](http://www.chessgames.com/index.html)

## Misc

- [Ant's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=645), [Connect6](/Connect6 "Connect6") program
- [Ant from Wikipedia](https://en.wikipedia.org/wiki/Ant)
- [Ant (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Ant_%28disambiguation%29)
- [Netherlands Antilles from Wikipedia](https://en.wikipedia.org/wiki/Netherlands_Antilles)
- [Apache Ant from Wikipedia](https://en.wikipedia.org/wiki/Apache_Ant)
- [Langton's ant from Wikipedia](https://en.wikipedia.org/wiki/Langton%27s_ant)

:   [![LangtonsAntAnimated.gif](https://upload.wikimedia.org/wikipedia/commons/0/09/LangtonsAntAnimated.gif)](http://en.wikipedia.org/wiki/Langton%27s_ant)

- [Albert Mangelsdorff](/Category:Albert_Mangelsdorff "Category:Albert Mangelsdorff"), [Jaco Pastorius](/Category:Jaco_Pastorius "Category:Jaco Pastorius"), [Alphonse Mouzon](/Category:Alphonse_Mouzon "Category:Alphonse Mouzon") - Ant Steps On An Elephant's Toe, [Trilogue](https://en.wikipedia.org/wiki/Albert_Mangelsdorff#Discography), [Berlin Jazz Festival](https://en.wikipedia.org/wiki/JazzFest_Berlin), November 06, 1976, [Berliner Philharmonie](https://en.wikipedia.org/wiki/Berliner_Philharmonie), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Diagram showing the morphology of a worker [ant](https://en.wikipedia.org/wiki/Ant) (Pachycondyla verenae), by [Mariana Ruiz](https://commons.wikimedia.org/wiki/User:LadyofHats) with data from [Bert Hölldobler](https://en.wikipedia.org/wiki/Bert_H%C3%B6lldobler) and [Edward O. Wilson](https://en.wikipedia.org/wiki/E._O._Wilson), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Some news about H. Secelle (author of Bionic)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30320) by [Johan Havegheer](/Johan_Havegheer "Johan Havegheer"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 08, 1999
3. [↑](#cite_ref-3) [A black day for France](http://en.chessbase.com/post/a-black-day-for-france/30) by [Eric van Reem](/Eric_van_Reem "Eric van Reem"), [ChessBase News](/ChessBase "ChessBase"), June 01, 2002
4. [↑](#cite_ref-4) [Ant vs Chess Tiger 14.0 48...Bxf3](https://www.stmintz.com/ccc/index.php?id=233413) by K. Burcham, [CCC](/CCC "CCC"), June 01, 2002
5. [↑](#cite_ref-5) [Leiden(9) surprise: Ant-Shredder 1/2-1/2](https://www.stmintz.com/ccc/index.php?id=429826) by [Theo van der Storm](/Theo_van_der_Storm "Theo van der Storm"), [CCC](/CCC "CCC"), June 05, 2005

**[Up one Level](/Engines "Engines")**