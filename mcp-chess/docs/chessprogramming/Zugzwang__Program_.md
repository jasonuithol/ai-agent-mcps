# Zugzwang (Program)

Source: https://www.chessprogramming.org/Zugzwang_(Program)

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Zugzwang**

**Zugzwang** was a massive parallel chess program by [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann") and [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz") from the [Paderborn University](/Paderborn_University "Paderborn University"), Germany. It won the bronze medal at the [2nd Computer Chess Olympiad, London 1990](/2nd_Computer_Olympiad#Chess "2nd Computer Olympiad"), and was runner up with three wins and two draws at the [WCCC 1992](/WCCC_1992 "WCCC 1992"), and won three times the International Paderborn Computer Chess Championships [IPCCC](/IPCCC "IPCCC"). The Zugzwang team was completed by chess player and [opening book author](/Category:Opening_Book_Author "Category:Opening Book Author") [Heiner Matthias](/Heiner_Matthias "Heiner Matthias"). Zugzwang was first based on [Transputer](/Transputer "Transputer") technology with a grid of up to 1024 [Inmos](https://en.wikipedia.org/wiki/Inmos) T800 and later T805 processors. Software was developed in the [Occam](https://en.wikipedia.org/wiki/Occam_%28programming_language%29) programming language. Later it was also ported to the [C-programming language](/C "C"), to run on other hardware architectures such as the [Cray T3E](/Cray_T3E "Cray T3E") supercomputer in 1999. The [Young Brothers Wait Concept](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept") was elaborated exhaustingly by Feldmann et al. [[1]](#cite_note-1)[[2]](#cite_note-2). Zugzwang didn't use [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning"), but Feldmann's [Fail-High Reductions](/Fail-High_Reductions "Fail-High Reductions") as well based on the [Null Move Observation](/Null_Move_Observation "Null Move Observation") [[3]](#cite_note-3). Zugzwang's [evaluation](/Evaluation "Evaluation") was [tuned](/Automated_Tuning "Automated Tuning") by [simulated annealing](/Simulated_Annealing "Simulated Annealing") as described in Mysliwietz' Ph.D. thesis [[4]](#cite_note-4).

# Photos & Games

[![RainerAegon1997.gif](/images/e/ec/RainerAegon1997.gif)](http://www.thorstenczub.de/aegon.html)

[Aegon 1997](/Aegon_1997 "Aegon 1997"), [Ye Rongguang](https://en.wikipedia.org/wiki/Ye_Rongguang) vs. Zugzwang operated by [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann")

```
[Event "12th AEGON Man-Mach"]
[Site "The Hague NED"]
[Date "1997.04.22"]
[Round "05"]
[White "Ye Rongguang"]
[Black "ZUGZWANG"]
[Result "1/2-1/2"]

1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 d6 6.e3 a5 7.Nge2 Nf6 8.a3 O-O
9.Rb1 Bg4 10.b4 axb4 11.axb4 e4 12.dxe4 Ne5 13.h3 Be6 14.f4 Nxc4 15.O-O Re8
16.Nd4 c6 17.Qd3 d5 18.e5 Nd7 19.g4 Qb6 20.Kh1 Rad8 21.Nxe6 fxe6 22.h4 Ra8
23.g5 Qc7 24.Bh3 Ndb6 25.Qc2 Qe7 26.Qb3 h5 27.Ne2 Qc7 28.Nd4 Qf7 29.Re1 Bf8
30.Nf3 Ra4 31.Qc3 Ra2 32.e4 Bg7 33.exd5 cxd5 34.Ra1 Rxa1 35.Qxa1 Bf8
36.Qb1 Nd7 37.Nd4 Nb8 38.Bf1 Nc6 39.Nxc6 bxc6 40.Bd3 Kh7 41.Bxc4 dxc4
42.Rd1 Qb7 43.Qe4 c3 44.Rd4 Rb8 45.Kh2 c5 46.Qxb7+ Rxb7 47.bxc5 Bxc5
48.Rc4 Rc7 49.Kg2 Bb6 50.Rb4 Rc6 51.Kf1 c2 52.Ke2 Ba5 53.Rb5 Bc7 54.Rb7 Kg8
55.Ra7 Bb6 56.Rd7 Bc7 57.Kd3 Ba5 58.Ke2 Bc7 59.Rd3 Kf8 60.Ra3 Bb6
61.Ra8+ Kg7 62.Ra2 Kf7 63.Ra1 Bc5 64.Ra4 Bg1 65.Ra3 Rc7 66.Rf3 Bd4
67.Kd2 Bb6 68.Ke2 Ba5 69.Ra3 Bb4 70.Rb3 Bc3 71.Ra3 Kf8 72.Ra2 Bd4
73.Ra4 Ba7 74.Ra6 Kf7 75.Rd6 Bc5 76.Rd8 Rc6 77.Rd7+ Kf8 78.Rd3 Be7
79.Rb3 Bd8 80.Rb8 Ke7 81.Rb7+ Kf8 82.Ra7 Be7 83.Kd3 Bc5 84.Ra8+ Kf7
85.Ke2 Kg7 86.Ra4 Bg1 87.Ra3 Rc8 88.Rg3 Bd4 89.Rd3 Bc3 90.Rd7+ Kf8
91.Rd6 Ke7 92.Ra6 Rc7 93.Ra8 Bd4 94.Ra4 Bb6 95.Rb4 Rc6 96.Rb3 Kd7
97.Ra3 Rc5 98.Rd3+ Ke7 99.Rd6 Ba5 100.Ra6 Kf7 101.Ra7+ Bc7 102.Kd3 Rc6
103.Ra2 Bb6 104.Ra6 Ke7 105.Ke2 Kd8 106.Ra8+ Rc8 1/2-1/2
```

# Descriptions

given from the [ICGA](/ICGA "ICGA") tournament site [[5]](#cite_note-5):

## 1995

```
Zugzwang made its first moves in 1989. It won the bronze medal in the 1990 Computer Olympiad, and won the Paderborn (human) Championships in 1991. In the last Computer World Championships in Madrid 1992, Zugzwang, running on a system consisting of 1023 T800 transputers, finished second and was undefeated without playing the eventual Champion, ChessMachine Schroeder. In 1993 Zugzwang had its first victory over a grandmaster. In 1994 Zugzwang was completely rewritten from OCCAM to C (about 20,000 lines of code) and is now portable to a large spectrum of machines including SPARC, SGI, DEC Alpha, i860, 486 and PowerPC. In this year's Championships, Zugzwang will run on a GC-Powerplus distributed system (based on the PowerPC) with at least 96 processors. The opening book contains about 130,000 moves and 1MB transposition tables are used per processor. Zugzwang uses brute-force alpha-beta  search with history tables and killer heuristics. The program searches about 3000 nodes per second per processor on a PowerPC. The search is performed by distributed processors using a distributed algorithm based on the Young Brothers Wait Concept, which gives good results even if as many as 1000 processors are used. In this case the system calculates moves more than 400 times faster than a sequential system.
```

## 1999

```
Zugzwang has been written by Rainer Feldmann and Peter Mysliwietz (until 1996). Rainer Feldmann is a member, Peter Mysliwietz a former member of the research group of Prof. Dr. Burkhard Monien at the University of Paderborn. Zugzwang is a product of an ongoing research in the field of efficient parallel algorithms for optimization problems. In the course of this research we developed a parallel game tree search algorithm which runs efficiently even on massively parallel systems without any shared memory.
```

```
The program started as an OCCAM program for Transputers. In 1992 it played the WCCC in Madrid running on a system with 1024 processors. From 1995 the program was rewritten to C. It now runs efficiently on various hardware platforms as e.g. PowerPC based parallel computers or the Cray T3E.
```

```
The opening book of Zugzwang is handwritten. No automatic opening book compilation is used. The search algorithm used is the Fail-High Reductions algorithm. The program has access to the endgame databases of Ken Thompson.
```

```
The most recent tournament played was the Lippstadt Grandmaster Tournament in August 1998, where the program finished second and played at a rate of about 2600 ELO points. The program ran on a Cray T3E with 512 processors (300 MHz) at the John von Neumann Institute for Computing [6] in Juelich, Germany.
```

# See also

- [Alpha I](/Alpha_I "Alpha I")
- [Zugzwang](/Zugzwang "Zugzwang")

# Publications

- [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](/Burkhard_Monien "Burkhard Monien"), [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](/Oliver_Vornberger "Oliver Vornberger") (**1989**). *Distributed Game-Tree Search*. [ICCA Journal, Vol. 12, No. 2](/ICGA_Journal#12_2 "ICGA Journal") [[7]](#cite_note-7)
- [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](/Burkhard_Monien "Burkhard Monien") (**1991**). *A Fully Distributed Chess Program*. [Advances in Computer Chess 6](/Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.top-5000.nl/ps/A%20fully%20distribuited%20chess%20program.pdf)
- [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](/Burkhard_Monien "Burkhard Monien") (**1992**). *Experiments with a Fully Distributed Chess Program*. [Heuristic Programming in AI 3](/3rd_Computer_Olympiad#Workshop "3rd Computer Olympiad")
- [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Phd-Thesis, [pdf](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
- [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](/Burkhard_Monien "Burkhard Monien") (**1994**). *Game-Tree Search on a Massively Parallel System*. [Advances in Computer Chess 7](/Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
- [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. thesis (German)
- [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](/Burkhard_Monien "Burkhard Monien") (**1998**). *Selective Game Tree Search on a Cray T3E*. [ps](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/FM_T3E.ps.Z) [[8]](#cite_note-8)

# Forum Posts

- [Re: Playing for position (mobility)](http://groups.google.com/group/rec.games.chess.computer/msg/6d07c745072dc611) by [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 02, 1995 » [Mobility](/Mobility "Mobility")
- [Zugzwang with GM-like perfomance in Lippstadt tournament](https://www.stmintz.com/ccc/index.php?id=25061) by [Dirk Frickenschmidt](/Dirk_Frickenschmidt "Dirk Frickenschmidt"), [CCC](/CCC "CCC"), August 19, 1998
- [What went wrong with P.Conners and Zugzwang in WCCC?](https://www.stmintz.com/ccc/index.php?id=58557) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), June 29, 1999 » [WCCC 1999](/WCCC_1999 "WCCC 1999")

# External Links

- [Zugzwang's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=54)
- [Zugzwang's games at chessgames.com](http://www.chessgames.com/perl/ezsearch.pl?search=Zugzwang)
- [Parallele Suche in Spielbäumen](http://www.faui01.de/brettspiele/parallel.pdf) (pdf) by Stefan Büttcher (german)

# References

1. [↑](#cite_ref-1) [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](/Burkhard_Monien "Burkhard Monien") (**1991**). *A Fully Distributed Chess Program*. [Advances in Computer Chess 6](/Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.top-5000.nl/ps/A%20fully%20distribuited%20chess%20program.pdf)
2. [↑](#cite_ref-2) [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems* Phd-Thesis, [pdf](http://wwwcs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
3. [↑](#cite_ref-3) [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann") (**1997**). *Fail-High Reductions.* [Advances in Computer Chess 8](/Advances_in_Computer_Chess_8 "Advances in Computer Chess 8"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=4399933A9FAE32A9C855DED714120C66?doi=10.1.1.51.4897&rep=rep1&type=pdf) from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.51.4897)
4. [↑](#cite_ref-4)  [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. thesis (German)
5. [↑](#cite_ref-5) [Zugzwang's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=54)
6. [↑](#cite_ref-6) [John von Neumann Institute for Computing](http://fzj.helmholtz.de/nic/nic-e.html)
7. [↑](#cite_ref-7) [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Comment on 'Distributed Game-Tree Search'* . [ICCA Journal, Vol. 12, No. 4](/ICGA_Journal#12_4 "ICGA Journal")
8. [↑](#cite_ref-8) [Forschungszentrum Jülich schickt Cray T-3 zur Schachweltmeisterschaft](https://www.computerwoche.de/a/forschungszentrum-juelich-schickt-cray-t-3-zur-schachweltmeisterschaft,508177), June 09, 1999, [Computerwoche](/Computerworld#Woche "Computerworld") (German) » [WCCC 1999](/WCCC_1999 "WCCC 1999")

**[Up one Level](/Engines "Engines")**