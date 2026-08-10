# Chiron

Source: https://www.chessprogramming.org/Chiron

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Chiron**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Palais_Bourbon%2C_Malerei_in_der_Kuppel_der_Poesie%2C_Szene-_Erziehung_des_Achill_%28Eug%C3%A8ne_Delacroix%29.jpg/330px-Palais_Bourbon%2C_Malerei_in_der_Kuppel_der_Poesie%2C_Szene-_Erziehung_des_Achill_%28Eug%C3%A8ne_Delacroix%29.jpg)](/File:Palais_Bourbon,_Malerei_in_der_Kuppel_der_Poesie,_Szene-_Erziehung_des_Achill_(Eug%C3%A8ne_Delacroix).jpg)

[Eugène Delacroix](/Category:Eug%C3%A8ne_Delacroix "Category:Eugène Delacroix") - [Chiron](https://en.wikipedia.org/wiki/Chiron) instructing [Achilles](https://en.wikipedia.org/wiki/Achilles) [[1]](#cite_note-1)

**Chiron**,  
a commercial chess engine by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), supporting both the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](/UCI "UCI"), the [PolyGlot](/PolyGlot "PolyGlot") and [CTG](/CTG "CTG") [[2]](#cite_note-2) [opening book formats](/Opening_Book#Formats "Opening Book"), various [endgame tablebase](/Endgame_Tablebases "Endgame Tablebases") and [bitbase](/Endgame_Bitbases "Endgame Bitbases") formats, and able to play [Chess960](/Chess960 "Chess960"). The development started in 2002 and it has been under continuous development, underwent a major rewrite in 2009 using [bitboards](/Bitboards "Bitboards"), and has been commercially released in October 2011 [[3]](#cite_note-3) . Chiron applies [parallel search](/Parallel_Search "Parallel Search") on [multiprocessor](https://en.wikipedia.org/wiki/Multiprocessor) systems, and has implemented [pawn blockage detection](/Blockage_Detection "Blockage Detection") function [[4]](#cite_note-4) [[5]](#cite_note-5), improved to detect blockages not only in [pawn endgame](/Pawn_Endgame "Pawn Endgame") but also when there are a few pieces on the board [[6]](#cite_note-6) [[7]](#cite_note-7) [[8]](#cite_note-8). Chiron is available as [Windows](/Windows "Windows") and [Android](/Android "Android") version.

# Further Versions

## Chiron 2

Chiron **2**, released in December 2013 is about 40 Elo points stronger than Chiron 1.5 thanks to improvements in both [search](/Search "Search") and [evaluation](/Evaluation "Evaluation") [[9]](#cite_note-9).

## Chiron 3

The next major release in May 2016, Chiron **3**, is about 60 Elo stronger than 2, due to further search and evaluation enhancements and tuning, and also supports [Syzygy Bases](/Syzygy_Bases "Syzygy Bases") and is able to probe of 6-men [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases") [[10]](#cite_note-10).

## Chiron 4

On January 10, 2017, Chiron **4** was released, again a considerable improvement of about 70 Elo over its predecessor, Chiron 4 improved in a further [tuned](/Automated_Tuning "Automated Tuning") [evaluation](/Evaluation "Evaluation"), specially considering [passed pawns](/Passed_Pawn "Passed Pawn") and [mobility](/Mobility "Mobility"), and various [search](/Search "Search") enhacements, such as better [forward pruning](/Pruning "Pruning"), [Lazy SMP](/Lazy_SMP "Lazy SMP") and [NUMA](/NUMA "NUMA") awareness [[11]](#cite_note-11).

## Chiron 5

Chiron **5** was released on June 21, 2021. It is about 110/120 points stronger than Chiron 4. Most of the gains come from improvements in [search](/Search "Search") and [move ordering](/Move_Ordering "Move Ordering") but also the [evaluation](/Evaluation "Evaluation") has been improved and [tuned](/Automated_Tuning "Automated Tuning") by playing several million games [[12]](#cite_note-12).

# Tournament Play

Chiron played various [Italian Computer Chess Championships](/Italian_Computer_Chess_Championship "Italian Computer Chess Championship"), was best Italian entry at the [CCC 2009](/CCC_2009 "CCC 2009") and the [IOCSC 2010](/IOCSC_2010 "IOCSC 2010") [[13]](#cite_note-13) respectively, and further won the [IGWT 2013](/IGWT_2013 "IGWT 2013"), [IGWT 2014](/IGWT_2014 "IGWT 2014") and [IGWT III](/IGWT_III "IGWT III") online, and the [IGT 2016](/IGT_2016 "IGT 2016") and [IGT 2017](/IGT_2017 "IGT 2017") over the board. Chiron played the [WCCC 2006](/WCCC_2006 "WCCC 2006") in [Turin](https://en.wikipedia.org/wiki/Turin), the [IPCCC 2006](/IPCCC_2006 "IPCCC 2006"), and four [CCT Tournaments](/CCT_Tournaments "CCT Tournaments"), winning the [CCT14](/CCT14 "CCT14") in 2012 [[14]](#cite_note-14)

# Photos & Games

## WCCC 2006

[![ItalianChessProgrammers.jpg](/images/e/ed/ItalianChessProgrammers.jpg)](/File:ItalianChessProgrammers.jpg)

[Ubaldo](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [Nietta](/Antonia_Jeanrenaud "Antonia Jeanrenaud"), [Stefano](/Stefano_Malloggi "Stefano Malloggi") and [Eros](/Eros_Riccio "Eros Riccio"), [WCCC 2006](/WCCC_2006 "WCCC 2006"), Chiron vs. [Diep](/Diep "Diep") [[15]](#cite_note-15)

```
[Event "WCCC 2006"]
[Site "Turin, Italy"]
[Date "2006.06.01"]
[Round "11"]
[White "Chiron"]
[Black "Diep"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be2 e5 7.Nb3 Be7 8.O-O O-O
9.a4 Nc6 10.a5 Be6 11.Be3 Nb412.f4 exf4 13.Rxf4 d5 14.e5 Nd7 15.Nc5 Qc7 16.Rxb4
Bxc5 17.Bxc5 Qxc5+ 18.Qd4 Qxd4+ 19.Rxd4 Rac8 20.Bf3 Nxe5 21.Bxd5 Bxd5 22.Rxd5 f6
23.Rad1 Nc4 24.Rd7 Nxb2 25.Rb1 Rxc3 26.Rxb2 Rb8 27.Rb4 h5 28.Re4 Rc5 29.Ree7 Rg5
30.h4 Rg4 31.Rxb7 Rxb7 32.Rxb7 Ra4 33.Kf2 Rxa5 34.Rc7 Ra2 35.Kf3 Ra3+ 36.Ke4 Rg3
37.c4 Rxg2 38.c5 Rc2 39.Kf5 Re2 40.Kg6 Rg2+ 41.Kf5 Rc2 42.Kg6 Kf8 43.Kxh5 Kg8
44.Kg6 Rg2+ 45.Kf5 Kh7 46.Ke6 Re2+ 47.Kd6 Rd2+ 48.Ke7 Re2+ 49.Kd8 Rc2 50.c6 a5
51.Rc8 Rd2+ 52.Kc7 Rc2 53.Ra8 g5 54.hxg5 fxg5 55.Kb7 Kg6 56.Rxa5 Kh5 57.c7 1/2-1/2
```

## CCT14

[CCT14](/CCT14 "CCT14"), round 5, Chiron - [Komodo](/Komodo "Komodo") [[16]](#cite_note-16)

```
[Event "CCT14"]
[Site "Internet Chess Club"]
[Date "2012.02.26"]
[Round "5"]
[White "Chiron"]
[Black "Komodo"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8. c3 O-O 9.h3 Na5
10.Bc2 c5 11.d4 Qc7 12.d5 Bd7 13.Qe2 Rfe8 14.b3 g6 15.Bh6 Nh5 16.Qe3 Bf8 17.Nbd2 Nb7
18.g4 Nf4 19.Bxf4 exf4 20.Qxf4 Bg7 21.Rad1 Nd8 22.Qg3 f6 23.e5 dxe5 24.Ne4 Nf7 25.d6
Qc8 26.c4 Ra7 27.Rd5 Be6 28.Rxc5 Qb8 29.Nfd2 Nxd6 30.Rc6 Nf7 31.c5 Qd8 32.Nd6 Nxd6
33.Rxd6 Rd7 34.Rxd7 Qxd7 35.Ne4 Qd4 36.Rd1 Qb4 37.c6 Qf8 38.b4 Rc8 39.Nc5 Bc4 40.Qg2
Qe8 41.Be4 f5 42.gxf5 gxf5 43.Bxf5 Rxc6 44.Rd7 Qg6 45.Bxg6 Rxg6 46.Qxg6 hxg6 47.a3 Bh6
48.Rd6 Kf7 49.Rxa6 Bc1 50.Kg2 Bb2 51.Kf3 Bd5+ 52.Kg4 Bc4 53.Ra7+ Ke8 54.Kg5 Bd4 55.Kxg6
Bxf2 56.Kf6 Bh4+ 57.Kxe5 Bg3+ 58.Kf5 Bf2 59.Rb7 Bf1 60.Ne4 Be1 61.Rh7 Bd3 1-0
```

# Acknowledgment

by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), 2011 [[17]](#cite_note-17) [[18]](#cite_note-18)

```
In these nine years Chiron has improved a lot thanks also to ideas found in strong |open source engines, in computer chess forums and websites, etc. In particular I would like to thank Fabien Letouzey, Tord Romstad, Robert Hyatt, the Ippolit guys, Ed Schröder, Bruce Moreland, Ernst Heinz and many others. Thanks to Miguel Ballicora, Eugene Nalimov and Daniel Shawul for the probing code of their tablebases/bitbases, to Pradu Kannan, Gerd Isenberg and Lasse Hansen for the magic bitboards, to Sesse and Stephan Vermeire for the CTG specifications, to Ilari Pihlajisto for cutechess-cli that I've been using since 2009 for testing Chiron with very fast games. Thanks to all the people that tested Chiron in the past, among them Ciro Vignotto, Leo Dijksman, Olivier Deville, Günther Simon, Lars Hallerström, the testers of CEGT and CCRL and many others. Thanks to Wilhelm Hudetz for the Chiron logo. Finally, thanks to Salvo Spitaleri who has been the opening book author of Chiron since 2006.
```

# See also

- [Achilles](/Achilles "Achilles")
- [Centaur](/Centaur "Centaur")
- [Cheiron](/Cheiron "Cheiron")

# Publications

- [Arno Nickel](/Arno_Nickel "Arno Nickel") (**2012**). *[Die schöne neue Welt der Schachengines](http://www.edition-marco-shop.de/epages/64079634.sf/de_DE/?ObjectPath=/Shops/64079634/Categories/Schachgeschehen/Computerschach)*. [SCHACH](http://www.zeitschriftschach.de/) 2,3,5,6 2012, [pdf](http://www.edition-marco-shop.de/WebRoot/Store14/Shops/64079634/5177/F0A3/C389/D0DD/3A71/C0A8/2935/25F6/Die_schoene_neue_Welt_der_Schachengines.pdf) (German) [[19]](#cite_note-19)

# Forum Posts

- [Chiron 1.0 available for preorder](http://www.talkchess.com/forum/viewtopic.php?t=40529) by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [CCC](/CCC "CCC"), September 26, 2011
- [Code of Chiron for Detection of Pawn Blockages](http://www.talkchess.com/forum/viewtopic.php?t=40748) by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [CCC](/CCC "CCC"), October 13, 2011
- [Chiron 1.1 bug?](http://www.talkchess.com/forum/viewtopic.php?t=41569) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), December 24, 2011
- [CCT 14: Chiron is the Champion!](http://www.talkchess.com/forum/viewtopic.php?t=42638) by [Peter Skinner](/Peter_Skinner "Peter Skinner"), [CCC](/CCC "CCC"), February 26, 2012
- [Chiron 1.5](http://www.talkchess.com/forum/viewtopic.php?t=45813) by Cliff Sears, [CCC](/CCC "CCC"), November 01, 2012
- [Re: Chiron chess a finished project?](http://www.talkchess.com/forum/viewtopic.php?t=48915&start=2) by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [CCC](/CCC "CCC"), August 10, 2013
- [Chiron 2 Released](http://www.talkchess.com/forum/viewtopic.php?t=50475) by mike hurd, [CCC](/CCC "CCC"), December 13, 2013
- [Chiron 3 released](http://www.talkchess.com/forum/viewtopic.php?t=60017) by Christian Goralski, [CCC](/CCC "CCC"), May 01, 2016
- [Chiron 5 Released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77534) by Damir, [CCC](/CCC "CCC"), June 22, 2021

# External Links

## Chess Engine

- [Chiron's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=83)
- [Chiron Chess Engine](https://www.chironchess.com/)

:   [Chiron 3 released](https://www.chironchess.com/chiron-3-released/), May 01, 2016
:   [Chiron 4 released](https://www.chironchess.com/chiron-4-released/), January 10, 2017
:   [Chiron 5 released](https://www.chironchess.com/chiron-5-released/), June 21, 2021

- [Chiron 4 Chess Engine – Google Play](https://play.google.com/store/apps/details?id=com.chironchess.chiron4)

## Misc

- [Chiron (Mythology) from Wikipedia](https://en.wikipedia.org/wiki/Chiron)
- [2060 Chiron from Wikipedia](https://en.wikipedia.org/wiki/2060_Chiron)

:   [Chiron - Centaurs in astrology from Wikipedia](https://en.wikipedia.org/wiki/Centaurs_in_astrology#Chiron)
:   [Chiron - Asteroid in astrology from Wikipedia](https://en.wikipedia.org/wiki/Asteroids_in_astrology#Chiron)

# References

1. [↑](#cite_ref-1) [Chiron](https://en.wikipedia.org/wiki/Chiron), half man, half horse: instructing [Achilles](https://en.wikipedia.org/wiki/Achilles), The Education of Achilles, by [Eugène Delacroix](/Category:Eug%C3%A8ne_Delacroix "Category:Eugène Delacroix"), 2nd third of 19th century, [Palais Bourbon](https://en.wikipedia.org/wiki/Palais_Bourbon), [Liminal being from Wikipedia](https://en.wikipedia.org/wiki/Liminal_being)
2. [↑](#cite_ref-2) [CTG specification](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=2319) by [Sesse](/Steinar_H._Gunderson "Steinar H. Gunderson"), [Rybka Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 30, 2007
3. [↑](#cite_ref-3) [Chiron 1.0 available for preorder](http://www.talkchess.com/forum/viewtopic.php?t=40529) by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [CCC](/CCC "CCC"), September 26, 2011
4. [↑](#cite_ref-4) [Omid David](/Eli_David "Eli David"), [Ariel Felner](/Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](/Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *Blockage Detection in Pawn Endgames*. [ICGA Journal, Vol. 27, No. 3](/ICGA_Journal#27_3 "ICGA Journal")
5. [↑](#cite_ref-5) [Omid David](/Eli_David "Eli David"), [Ariel Felner](/Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](/Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *[Blockage Detection in Pawn Endings](http://link.springer.com/chapter/10.1007/11674399_13)*. [CG 2004](/CG_2004 "CG 2004")
6. [↑](#cite_ref-6) [Chiron Chess Engine | Pawn Blockages](https://web.archive.org/web/20120122012655/http://www.chironchess.com/index.php/component/content/article/69) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), January 22, 2012)
7. [↑](#cite_ref-7) [Code of Chiron for Detection of Pawn Blockages](http://www.talkchess.com/forum/viewtopic.php?t=40748) by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [CCC](/CCC "CCC"), October 13, 2011
8. [↑](#cite_ref-8) [Chiron 1.1 bug?](http://www.talkchess.com/forum/viewtopic.php?t=41569) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), December 24, 2011
9. [↑](#cite_ref-9) [Chiron 2 released](https://www.chironchess.com/chiron-2-released/)
10. [↑](#cite_ref-10) [Chiron 3 released](https://www.chironchess.com/chiron-3-released/)
11. [↑](#cite_ref-11) [Chiron 4 released](https://www.chironchess.com/chiron-4-released/), January 10, 2017
12. [↑](#cite_ref-12) [Chiron 5 released](https://www.chironchess.com/chiron-5-released/)
13. [↑](#cite_ref-13) [I have seen parts of the source](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=428176&t=40669) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), October 11, 2011
14. [↑](#cite_ref-14) [CCT 14: Chiron is the Champion!](http://www.talkchess.com/forum/viewtopic.php?t=42638) by [Peter Skinner](/Peter_Skinner "Peter Skinner"), [CCC](/CCC "CCC"), February 26, 2012
15. [↑](#cite_ref-15) [Turin 2006 - Chess - Round 11 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=16&round=11&id=5)
16. [↑](#cite_ref-16) [Re: CCT 14: Chiron is the Champion!](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=452443&t=42638) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), February 26, 2012
17. [↑](#cite_ref-17) [Chiron Chess Engine | About](https://www.chironchess.com/about/)
18. [↑](#cite_ref-18) Thank you! ([Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), April 22, 2012) My own contribution to [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") was the line-wise forerunner, dubbed [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards"), also tried with "random" factors, while [Lasse Hansen](/Lasse_Hansen "Lasse Hansen") had the idea to hash both lines simultaneously. I was initially skeptical whether the huge tables pay off.
19. [↑](#cite_ref-19) Part 1 covers [Houdini](/Houdini "Houdini"), [Rybka](/Rybka "Rybka"), [Komodo](/Komodo "Komodo"), [Stockfish](/Stockfish "Stockfish"), [Critter](/Critter "Critter"), [Naum](/Naum "Naum"), Chiron and [Spike](/Spike "Spike")

**[Up one Level](/Engines "Engines")**