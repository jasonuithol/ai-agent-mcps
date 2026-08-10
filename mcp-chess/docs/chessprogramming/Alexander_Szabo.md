# Alexander Szabo

Source: https://www.chessprogramming.org/Alexander_Szabo

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Alexander Szabo**

**Alexander (Alex) Szabo**,  
an American computer scientist, physicist, chess player, at times professional computer chess programmer, in the 80s, along with [Barbara Szabo](/Barbara_Szabo "Barbara Szabo"),
active in computer chess business and research. [Szabo Software](/Szabo_Software "Szabo Software") located in [Borrego Springs, California](https://en.wikipedia.org/wiki/Borrego_Springs,_California), distributed their commercial chess program [TechMate](/TechMate "TechMate") for the [Atari ST](/Atari_ST "Atari ST").
Alex Szabo defended his M.Sc. in physics in 1980, and his M.Sc. in CS in 1984, both from [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia), [Vancouver](https://en.wikipedia.org/wiki/Vancouver), [British Columbia](https://en.wikipedia.org/wiki/British_Columbia), [Canada](https://en.wikipedia.org/wiki/Canada).

# Tech 3

In his 1984 thesis *Computer-Chess Tactics and Strategy*, Alex Szabo elaborates on [tactics](/Tactics "Tactics") and [strategy](/Strategy "Strategy") exemplified by his thesis chess program [Tech 3](/Tech#Tech3 "Tech").
In the spirit of the original [Tech](/Tech "Tech") program by [James Gillogly](/James_Gillogly "James Gillogly"), he claimed that [knowledge](/Knowledge "Knowledge") is best applied at the top of the [search tree](/Search_Tree "Search Tree") as positional presort rather than at the [leaf nodes](/Leaf_Node "Leaf Node") using complex [evaluation](/Evaluation "Evaluation").

# The Technology Curve

[![](/images/thumb/5/51/TechnologyCurve.jpg/300px-TechnologyCurve.jpg)](/File:TechnologyCurve.jpg)

The Technology Curve [[1]](#cite_note-1)

Tech3's performance on [Reinfeld's](https://en.wikipedia.org/wiki/Fred_Reinfeld) [Win at Chess](/Win_at_Chess "Win at Chess") (WAC) problem set is 274/300,
which compares favourable with [Belle's](/Belle "Belle"), considering machine power. Alex Szabo used the **Technology Curve** as introduced by [James Gillogly](/James_Gillogly "James Gillogly") [[2]](#cite_note-2), a graph of [playing strength](/Playing_Strength "Playing Strength") versus machine power aka [binary logarithm](https://en.wikipedia.org/wiki/Binary_logarithm) of [nodes per second](/Nodes_per_Second "Nodes per Second"), as a tool for measuring the effectiveness of [knowledge](/Knowledge "Knowledge") encoding, and found in this respect [Nuchess](/Nuchess "Nuchess") as the best chess program of that time [[3]](#cite_note-3).

# TechMate

During the mid 80s, Alex Szabo developed [TechMate](/TechMate "TechMate") for the [Atari ST](/Atari_ST "Atari ST"). It was derived from [Tech 3](/Tech#Tech3 "Tech") with the addition of a simple strategic component, a more profound [evaluation function](/Evaluation_Function "Evaluation Function"). TechMate was commercially market by [Szabo Software](/Szabo_Software "Szabo Software") [[4]](#cite_note-4).

# The Technology Curve Revisted

As published in their 1988 [ICCA Journal](/ICGA_Journal "ICGA Journal") paper [[5]](#cite_note-5), Alex and Barbara Szabo revisited the [Technology Curve](#TechnologyCurve) by playing 6882 games between copies of TechMate set at different time rates, with the conclusion that the advantage of improved technology rapidly decreases when [machines](/Hardware "Hardware") and [algorithms](/Algorithms "Algorithms") become more powerful. [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") in his self-play memo on the experiment of the Szabos [[6]](#cite_note-6):

```
The Szabos determined the technology curve of their chess program TechMate that self-played 6,882 games on two Atari ST computers. The number of games per match between longer and shorter searching versions of the program varied strongly from a minimum of 32 to a maximum of 1367. The gain in playing strength averaged at 156 rating points per doubling of available search time (computing power). 

The experimental data indicated slight diminishing returns at longer search times. However, the Szabos simply did not play enough games at long times to draw reliable conclusions.
```

# WAC 230

In a 2001 [CCC](/CCC "CCC") forum post, Alex Szabo proposed several corrections on [Win at Chess](/Win_at_Chess "Win at Chess"), in particular that in WAC 230, a position from [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") vs [Aron Nimzowitsch](https://en.wikipedia.org/wiki/Aron_Nimzowitsch) [[7]](#cite_note-7), [Bad Niendorf](http://de.wikipedia.org/wiki/Niendorf_%28Ostsee%29), [1927](https://en.wikipedia.org/wiki/List_of_strong_chess_tournaments#1920.E2.80.931929) [[8]](#cite_note-8), 50... Rb4 does not win [[9]](#cite_note-9):

:   |  |
    | --- |
    |                                                                                   ♝       ♜         ♚♗♟ ♟  ♟  ♟♙ ♙    ♟♙      ♟♙   ♔   ♖   ♙ |

```
2b5/1r6/2kBp1p1/p2pP1P1/2pP4/1pP3K1/1R3P2/8 b - -
```

```
#230    [Rb4 does not win.  The main line is,  1... Rb4!? 2.cxb4 a4
        3.b5+ Kxb5 4.Ba3 c3 5.Re2! Kc4 6.f4 Kxd4 7.f5 exf5 8.e6 Kd3
        9.e7 Bd7 10.Kf3 d4 11.Rh2 Kc4 12.Rh8 b2 13.Rb8 d3
        14.Bxb2 cxb2 15.Rxb2 a3 16.Rb7 Be8 17.Ra7 Kb3 18.Ke3 a2
        19.Kxd3 Kb2 20.Rb7+ Kc1 21.Ra7 =]

        Ra7, Rb6, Rb5, Rd7, Rf7, Rg7, Rh7, Bd7, Kd7, Kb6, Kb5, a4, and Rc7
        are just as good as the book solution Rb4 -- they all hold the game.
```

In August 2010, [Dann Corbit](/Dann_Corbit "Dann Corbit") posted an allegedly refutation of Szabo's refutation found by [Stockfish 1.8](/Stockfish "Stockfish") [[10]](#cite_note-10).

# Selected Publications

[[11]](#cite_note-11)

- Alexander Szabo (**1980**). *The Co Distribution Around l=30°, b=0°*. M.Sc. Thesis, [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia), [pdf](https://circle.ubc.ca/bitstream/handle/2429/22558/UBC_1980_A6_7%20S93.pdf?sequence=1)
- Alexander Szabo (**1984**). *[Computer-Chess Tactics and Strategy](https://open.library.ubc.ca/cIRcle/collections/ubctheses/831/items/1.0051870)*. M.Sc. Thesis, [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia), [pdf](https://circle.ubc.ca/bitstream/handle/2429/24780/UBC_1984_A6_7%20S98.pdf?sequence=1)
- Alexander Szabo, [Barbara Szabo](/Barbara_Szabo "Barbara Szabo") (**1988**). *The Technology Curve Revisited*. [ICCA Journal, Vol. 11, No. 1](/ICGA_Journal#11_1 "ICGA Journal")

# Forum Posts

- [WAC Corrections](https://www.stmintz.com/ccc/index.php?id=163035) by Alex Szabo, [CCC](/CCC "CCC"), April 12, 2001
- [WAC 230 and Alexander Szabo's refutation revisted](https://www.stmintz.com/ccc/index.php?id=439525) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), August 01, 2005
- [WAC.230 revisited yet again](http://www.talkchess.com/forum/viewtopic.php?t=28900) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), July 11, 2009
- [Stockfish 1.8 demolishes WAC.230](http://www.talkchess.com/forum/viewtopic.php?t=35669) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), August 02, 2010

# External Links

- [Alexander Szabo chess games - 365Chess.com](http://www.365chess.com/players/Alexander_Szabo)

# References

1. [↑](#cite_ref-1) Image from Alexander Szabo (**1984**). *[Computer-Chess Tactics and Strategy](https://circle.ubc.ca/handle/2429/24780)*. M.Sc. Thesis, [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia), pg. 37
2. [↑](#cite_ref-2) [James Gillogly](/James_Gillogly "James Gillogly") (**1978**). *Performance Analysis of the Technology Chess Program*. Ph.D. Thesis. Tech. Report CMU-CS-78-189, [Carnegie Mellon University](/Carnegie_Mellon_University "Carnegie Mellon University"), [CMU-CS-77 pdf](http://reports-archive.adm.cs.cmu.edu/anon/anon/usr/ftp/scan/CMU-CS-77-gillogly.pdf)
3. [↑](#cite_ref-3) Alexander Szabo (**1984**). *[Computer-Chess Tactics and Strategy](https://circle.ubc.ca/handle/2429/24780)*. M.Sc. Thesis, [University of British Columbia](https://en.wikipedia.org/wiki/University_of_British_Columbia)
4. [↑](#cite_ref-4) [Gregg Pearlman](http://www.linkedin.com/in/greggpearlman) (**1986**). *[ST New Products](http://www.atarimagazines.com/v5n8/STNewProducts.html)*. [Antic Vol. 5, No. 8](http://www.atarimagazines.com/index/?issue=v5n8)
5. [↑](#cite_ref-5) Alexander Szabo, [Barbara Szabo](/Barbara_Szabo "Barbara Szabo") (**1988**). *The Technology Curve Revisited*. [ICCA Journal, Vol. 11, No. 1](/ICGA_Journal#11_1 "ICGA Journal")
6. [↑](#cite_ref-6) [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") (**2000**). *A New Self-Play Experiment in Computer Chess*. [Massachusetts Institute of Technology](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), Laboratory of Computer Science, Technical Memo No. 608, [zipped ps](http://supertech.lcs.mit.edu/~heinz/ps/new_exp.ps.gz), [pdf](http://bitsavers.trailing-edge.com/pdf/mit/lcs/tm/MIT-LCS-TM-608.pdf)
7. [↑](#cite_ref-7) [Hans Kmoch vs Aron Nimzowitsch (1927)](http://www.chessgames.com/perl/chessgame?gid=1102423) from [chessgames.com](http://www.chessgames.com/index.html)
8. [↑](#cite_ref-8) [Bad Niendorf 1927 - 365Chess.com Tournaments](http://www.365chess.com/tournaments/Bad_Niendorf_1927)
9. [↑](#cite_ref-9) [WAC Corrections](https://www.stmintz.com/ccc/index.php?id=163035) by Alex Szabo, [CCC](/CCC "CCC"), April 12, 2001
10. [↑](#cite_ref-10) [Stockfish 1.8 demolishes WAC.230](http://www.talkchess.com/forum/viewtopic.php?t=35669) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), August 02, 2010
11. [↑](#cite_ref-11) [ICGA Reference Database](/ICGA_Journal#RefDB "ICGA Journal")

**[Up one level](/People "People")**