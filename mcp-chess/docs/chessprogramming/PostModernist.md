# PostModernist

Source: https://www.chessprogramming.org/PostModernist

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* PostModernist**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/WeinerText.JPG/330px-WeinerText.JPG)](/File:WeinerText.JPG)

[Lawrence Weiner](/index.php?title=Category:Lawrence_Weiner&action=edit&redlink=1 "Category:Lawrence Weiner (page does not exist)"), Bits & Pieces ... [[1]](#cite_note-1) [[2]](#cite_note-2)

**PostModernist**,  
a chess program by [Andrew Williams](/Andrew_Williams "Andrew Williams"), supporting the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") [[3]](#cite_note-3) to run under [Linux](/Linux "Linux") and [Windows](/Windows "Windows") platforms [[4]](#cite_note-4). PostModernist uses [MTD(f)](/MTD(f) "MTD(f)") to drive its [search](/Search "Search") [[5]](#cite_note-5), its [transposition table](/Transposition_Table "Transposition Table") entries contain [upper](/Upper_Bound "Upper Bound") and a [lower bound](/Lower_Bound "Lower Bound") scores. As the search progresses, the gap between the bounds is narrowed until they meet, being the [exact score](/Exact_Score "Exact Score") for the position. It further applies [iterative deepening](/Iterative_Deepening "Iterative Deepening"), [null move pruning](/Null_Move_Pruning "Null Move Pruning"), [ETC](/Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff") and [extended futility pruning](/Futility_Pruning#Extendedfutilityprunning "Futility Pruning"), and uses separate [evaluation hash table](/Evaluation_Hash_Table "Evaluation Hash Table") and [pawn evaluation hash table](/Pawn_Hash_Table "Pawn Hash Table"), and probes [Nalimov endgame tablebases](/Nalimov_Tablebases "Nalimov Tablebases") [[6]](#cite_note-6). PostModernist played the [WCCC 2002](/WCCC_2002 "WCCC 2002"), and various [CCT Tournaments](/CCT_Tournaments "CCT Tournaments").

# Selected Games

[WCCC 2002](/WCCC_2002 "WCCC 2002"), round 9, PostModernist - [Insomniac](/Insomniac "Insomniac") [[7]](#cite_note-7)

```
[Event "WCCC 2002"]
[Site "Maastricht, The Netherlands"]
[Date "2002.07.11"]
[Round "9"]
[White "PostModernist"]
[Black "Insomniac"]
[Result "1/2-1/2"]

1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.Nc3 c6 5.Bg5 h6 6.Bxf6 Qxf6 7.e3 Nd7 8.Bd3 dxc4 9.Bxc4 g6 
10.O-O Bg7 11.Rc1 O-O 12.Qe2 Rd8 13.Rfd1 Qe7 14.e4 Nb6 15.e5 Nxc4 16.Qxc4 f5 17.exf6 
Qxf6 18.Ne4 Qf5 19.Ng3 Qa5 20.Qc2 Kf7 21.b3 a6 22.a4 Rd5 23.Nh4 Rg5 24.Ne4 Rg4 25.Nd6+ 
Kg8 26.Nxc8 Qd8 27.Nf3 Rxc8 28.h3 Rf4 29.Qxg6 Qe7 30.Re1 Re8 31.Qg3 Qf6 32.a5 Kh7 
33.Rc3 Rg8 34.Qh2 Qf7 35.Rd3 Rd8 36.Rde3 Bxd4 37.Nxd4 Rdxd4 38.Qg3 Rf6 39.R3e2 Rg6 
40.Qc3 Rd5 41.b4 Rdg5 42.g3 Rd5 43.Re4 Qd7 44.Qc2 Rd2 45.Qb3 Rd3 46.Qb1 Kg7 47.Qb2+ 
Kh7 48.Rf4 Qd6 49.Kf1 Rd2 50.Qb3 Kg8 51.Qf3 Qd3+ 52.Qxd3 Rxd3 53.Kg2 Kg7 54.Rfe4 Kf7 
55.g4 h5 56.f3 Rf6 57.f4 hxg4 58.hxg4 Rh6 59.R1e3 Rd2+ 60.Re2 Rd3 61.f5 exf5 62.Re7+ 
Kf8 63.gxf5 Rd2 64.Re8+ Kf7 65.Rxd2 Kxe8 66.Kg3 Ke7 67.Kg4 Rh1 68.Rd4 Kf6 69.Rd6+ Ke7 
70.Rd3 Rb1 71.Re3+ Kf7 72.Re4 Kf6 73.Re6+ Kf7 74.Rh6 Rxb4+ 75.Kg5 Kg8 76.Rd6 Kf7 
77.Rd7+ Ke8 78.Rc7 Rb2 79.f6 Kf8 80.Rh7 Kg8 81.Re7 Rb1 82.Kg6 Rg1+ 83.Kf5 Rb1 84.Ke6 
Re1+ 85.Kd7 Rf1 86.Ke6 Re1+ 87.Kd6 Rb1 88.Rc7 Kf8 89.Ke5 Re1+ 90.Kf5 Rf1+ 91.Kg5 Rg1+ 
92.Kh6 Rh1+ 93.Kg6 Rg1+ 94.Kf5 Rf1+ 95.Ke4 Re1+ 
1/2-1/2
```

# Forum Posts

- [Building the Principal Variation in MTD(f) searches](https://www.stmintz.com/ccc/index.php?id=60833) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), July 18, 1999 » [Principal Variation](/Principal_Variation "Principal Variation"), [MTD(f)](/MTD(f) "MTD(f)")
- [Re: Green List, PostModernist??](https://www.stmintz.com/ccc/index.php?id=70677) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), September 27, 1999
- [PostModernist in CCT3](https://www.stmintz.com/ccc/index.php?id=172094) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), May 28, 2001
- [A fun game between Searcher and PostModernist](https://www.stmintz.com/ccc/index.php?id=179706) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), July 14, 2001 » [Searcher](/Searcher "Searcher")
- [PostModernist in CCT5](https://www.stmintz.com/ccc/index.php?id=278729) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), January 21, 2003
- [PostModernist (v1003) available for download](https://www.stmintz.com/ccc/index.php?id=307830) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), July 24, 2003
- [PostModernist vs Amateur](https://www.stmintz.com/ccc/index.php?id=315949) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), September 15, 2003 » [Amateur](/Amateur "Amateur")

# External Links

## Chess Engine

- [PostModernist's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=76)
- [PostModernist 1016](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=PostModernist%201016) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Post (Disambiguation page) from Wikipedia](https://en.wikipedia.org/wiki/Post)
- [What does the prefix post mean?](http://wiki.answers.com/Q/What_does_the_prefix_post_mean) from [Answers.com](http://www.answers.com/)
- [Modernism from Wikipedia](https://en.wikipedia.org/wiki/Modernism)
- [Postmodernism from Wikipedia](https://en.wikipedia.org/wiki/Postmodernism)
- [Postmodernity from Wikipedia](https://en.wikipedia.org/wiki/Postmodernity)
- [Postmodern philosophy from Wikipedia](https://en.wikipedia.org/wiki/Postmodern_philosophy)
- [Postmodernist school from Wikipedia](https://en.wikipedia.org/wiki/Postmodernist_school)
- [Postmodern art from Wikipedia](https://en.wikipedia.org/wiki/Postmodern_art)
- [Postmodern architecture from Wikipedia](https://en.wikipedia.org/wiki/Postmodern_architecture)
- [Postmodern literature from Wikipedia](https://en.wikipedia.org/wiki/Postmodern_literature)
- [Postmodern music from Wikipedia](https://en.wikipedia.org/wiki/Postmodern_music)
- [Postmodernist film from Wikipedia](https://en.wikipedia.org/wiki/Postmodernist_film)

# References

1. [↑](#cite_ref-1) [Lawrence Weiner](/index.php?title=Category:Lawrence_Weiner&action=edit&redlink=1 "Category:Lawrence Weiner (page does not exist)"), Bits & Pieces Put Together to Present a Semblance of a Whole, [Walker Art Center](https://en.wikipedia.org/wiki/Walker_Art_Center), [Minneapolis](https://en.wikipedia.org/wiki/Minneapolis), 2005
2. [↑](#cite_ref-2) [Postmodern art from Wikipedia](https://en.wikipedia.org/wiki/Postmodern_art)
3. [↑](#cite_ref-3) [Re: Green List, PostModernist??](https://www.stmintz.com/ccc/index.php?id=70677) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), September 27, 1999
4. [↑](#cite_ref-4) [PostModernist (v1003) available for download](https://www.stmintz.com/ccc/index.php?id=307830) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), July 24, 2003
5. [↑](#cite_ref-5) [Building the Principal Variation in MTD(f) searches](https://www.stmintz.com/ccc/index.php?id=60833) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), July 18, 1999
6. [↑](#cite_ref-6) README file for PostModernist, June 28, 2006
7. [↑](#cite_ref-7) [Maastricht 2002 - Chess - Round 9 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=20&round=9&id=5)

**[Up one Level](/Engines "Engines")**