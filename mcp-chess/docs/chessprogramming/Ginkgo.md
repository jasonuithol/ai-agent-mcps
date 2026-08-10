# Ginkgo

Source: https://www.chessprogramming.org/Ginkgo

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Ginkgo**

[![](/images/thumb/4/4f/GinggoShirt.JPG/300px-GinggoShirt.JPG)](/WCCC_2015 "WCCC 2015")

[WCCC 2015](/WCCC_2015 "WCCC 2015") [Ginkgo leaf](https://en.wikipedia.org/wiki/Ginkgo_biloba#Leaves) [[1]](#cite_note-1)

**Ginkgo**,  
an [UCI](/UCI "UCI") compliant private chess engine written by [Frank Schneider](/Frank_Schneider "Frank Schneider") in [C++](/Cpp "Cpp"), the development started in fall 2014 after further improvements of Frank's earlier [0x88](/0x88 "0x88") engine [Anaconda](/Anaconda "Anaconda") were diminishing. Ginkgo was written from scratch using [bitboards](/Bitboards "Bitboards") as primary board representation, in particular [fancy magic bitboards](/Magic_Bitboards#Fancy "Magic Bitboards") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks"). The [parallel](/Parallel_Search "Parallel Search") [multi-threaded](/Thread "Thread") [search](/Search "Search") performs [PVS](/Principal_Variation_Search "Principal Variation Search") [alpha-beta](/Alpha-Beta "Alpha-Beta") with a [shared](/Shared_Hash_Table "Shared Hash Table") [transposition table](/Transposition_Table "Transposition Table") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](/Aspiration_Windows "Aspiration Windows"), [null move pruning](/Null_Move_Pruning "Null Move Pruning"), [late move reductions](/Late_Move_Reductions "Late Move Reductions"), and various [extensions](/Extensions "Extensions"), but no [singular](/Singular_Extensions "Singular Extensions"). The [automatically tuned](/Automated_Tuning "Automated Tuning") [evaluation](/Evaluation "Evaluation") features [material](/Material "Material"), [mobility](/Mobility "Mobility"), [pawn structure](/Pawn_Structure "Pawn Structure") and [king safety](/King_Safety "King Safety").

# Tournament Play

Ginkgo had its tournament debut at the [WCCC 2015](/WCCC_2015 "WCCC 2015") and [WCSC 2015](/WCSC_2015 "WCSC 2015") in [Leiden](/Leiden_University "Leiden University"), and was close winning the latter, finally losing from [Shredder](/Shredder "Shredder") in the blitz playoff. At the [WCCC 2016](/WCCC_2016 "WCCC 2016") and [WCCC 2018](/WCCC_2018 "WCCC 2018"), Ginkgo was incorporated in the [GridGinkgo](/GridGinkgo "GridGinkgo") [cluster](https://en.wikipedia.org/wiki/Computer_cluster) chess program by [Kai Himstedt](/Kai_Himstedt "Kai Himstedt") et al., while Ginkgo continued to play the [WCSC 2016](/WCSC_2016 "WCSC 2016"), [WCSC 2018](/WCSC_2018 "WCSC 2018"), the [WCSC 2019](/WCSC_2019 "WCSC 2019") and the [WCCC 2019](/WCCC_2019 "WCCC 2019").

# Photos & Games

## WCCC 2015

### Fridolin - Ginkgo

[![FridoGinkgoR2WCCC2015.JPG](/images/4/4f/FridoGinkgoR2WCCC2015.JPG)](/WCCC_2015 "WCCC 2015")

[WCCC 2015](/WCCC_2015 "WCCC 2015") round 2, [Fridolin](/Fridolin "Fridolin") vs. Ginkgo with some [ICCA Journals](/ICGA_Journal "ICGA Journal"), [Christian Sommerfeld](/Christian_Sommerfeld "Christian Sommerfeld") and [Ingo Bauer](/Ingo_Bauer "Ingo Bauer"),   
[Richard Pijl](/Richard_Pijl "Richard Pijl") on the right fighting the [Komodo](/Komodo "Komodo") with his [Baron](/The_Baron "The Baron") [[2]](#cite_note-2)

```
[Event "WCCC 2015"]
[Site "Leiden, The Netherlands"]
[Date "2015.06.29"]
[Round "2.4"]
[White "Fridolin"]
[Black "Ginkgo"]
[Result "0-1"]

1.c4 e5 2.Nc3 Nf6 3.g3 Bb4 4.Bg2 O-O 5.e4 Bxc3 6.dxc3 d6 7.Ne2 a6 8.O-O b5 9.cxb5 axb5 
10.Qc2 Bb7 11.Rd1 Nbd7 12.Bg5 h6 13.Bxf6 Nxf6 14.c4 b4 15.a4 bxa3 16.bxa3 Nd7 17.Re1 Nc5 
18.Nc3 Bc6 19.a4 Ra5 20.Nb5 Qd7 21.Ra3 Rfa8 22.Rea1 h5 23.Bf3 g6 24.Bg2 Kg7 25.f3 Qc8 
26.R3a2 Qb8 27.Bf1 Qb6 28.Kg2 Qb7 29.Kg1 Qb8 30.Kg2 Be8 31.Kg1 h4 32.gxh4 Qd8 33.Ra3 c6 
34.Nc3 Qxh4 35.Qf2 Qf6 36.Bg2 Ne6 37.Ne2 c5 38.Nc3 Nd4 39.Kh1 Bd7 40.Nd5 Qg5 41.Nb6 R8a7 
42.Nxd7 Rxd7 43.Qb2 Rda7 44.Bf1 Qf4 45.Bg2 Ra8 46.h3 Rh8 47.Kg1 Qg3 48.Kf1 Raa8 49.Qa2 
Rab8 50.Rd1 Rb4 51.Qf2 Qf4 52.Qd2 Qh2 53.a5 Rhb8 54.Ra2 Rb1 55.Qd3 R8b2 56.Rxb2 Rxb2 
57.Rd2 Rb3 58.Qxb3 Nxb3 59.Ra2 Qf4 60.a6 Qc1+ 61.Kf2 Qb1 62.Re2 Qa1 63.Bf1 Qxa6 64.Re1 
Nd4 65.h4 Qa2+ 66.Be2 Qd2 67.Kf1 Qf4 0-1
```

### Jonny - Ginkgo

[![Round8WCCC2015.JPG](/images/9/9e/Round8WCCC2015.JPG)](/WCCC_2015 "WCCC 2015")

[Jonny](/Jonny "Jonny") vs. Ginkgo, [Johannes Zwanzger](/Johannes_Zwanzger "Johannes Zwanzger") and [Frank Schneider](/Frank_Schneider "Frank Schneider") with Ginkgo shirt. [Komodo](/Komodo "Komodo") vs. [Fridolin](/Fridolin "Fridolin")   
in the background with [Christian Sommerfeld](/Christian_Sommerfeld "Christian Sommerfeld"), [Erdogan Günes](/Erdogan_G%C3%BCnes "Erdogan Günes") and [Mark Lefler](/Mark_Lefler "Mark Lefler")

```
[Event "WCCC 2015"]
[Site "Leiden, The Netherlands"]
[Date "2015.07.03"]
[Round "8.2"]
[White "Jonny"]
[Black "Ginkgo"]
[Result "1-0"]

1.d4 f5 2.g3 e6 3.Bg2 d5 4.Nf3 Nf6 5.c4 c6 6.O-O Bd6 7.Nc3 O-O 8.Qc2 Ne4 9.Be3 Nd7
10.Rac1 Qe8 11.Nxe4 dxe4 12.Nd2 e5 13.c5 exd4 14.Bxd4 Be5 15.Bxe5 Qxe5 16.b4 Nf6
17.Nc4 Qc7 18.f3 exf3 19.Rxf3 Be6 20.Nd6 g6 21.Re3 Bd5 22.Rd1 Rad8 23.a4 b6 24.Bxd5+
Nxd5 25.Qb3 a5 26.Rxd5 cxd5 27.Qxd5+ Kh8 28.Rd3 Rb8 29.Qd4+ Kg8 30.Qc4+ Kh8 31.Nb5
Qe7 32.Qd4+ Kg8 33.cxb6 Qxb4 34.Qxb4 axb4 35.a5 Rfe8 36.Nd4 Rec8 37.Kf2 Kf7 38.Rb3
Rc4 39.Nb5 Ke6 40.Nc7+ Kd6 41.Na6 Rb7 42.Nxb4 Re4 43.h4 Re5 44.Ra3 Re4 45.Nd3 Re8
46.Rb3 Ra8 47.Rb5 Kc6 48.Rc5+ Kd6 49.Kf3 Re7 50.Re5 Rd7 51.Kf4 Kc6 52.Nb4+ Kb7
53.Kg5 Rf7 54.Kh6 Rg8 55.Rb5 Ka8 56.a6 g5 1-0
```

## WCSC 2015

### Komodo - Ginkgo

[![KomodoGinkgoWCSC2015.JPG](/images/0/01/KomodoGinkgoWCSC2015.JPG)](/WCSC_2015 "WCSC 2015")

[Erdogan Günes](/Erdogan_G%C3%BCnes "Erdogan Günes") and [Frank Schneider](/Frank_Schneider "Frank Schneider") in [Komodo](/Komodo "Komodo") vs. Ginkgo, [WCSC 2015](/WCSC_2015 "WCSC 2015"), round 2

```
[Event "WCSC 2015"]
[Site "Leiden, The Netherlands"]
[Date "2015.07.04"]
[Round "2"]
[White "Komodo"]
[Black "Ginkgo"]
[Result "1/2-1/2"]

1.Nf3 Nf6 2.b3 g6 3.Bb2 Bg7 4.e3 O-O 5.Be2 d6 6.d4 c5 7.c4 cxd4 8.Nxd4 Nc6 9.O-O Nxd4 
10.exd4 d5 11.c5 b6 12.Nc3 Bd7 13.Rc1 Bc6 14.cxb6 axb6 15.a4 Qd7 16.Bb5 Rfc8 17.Qd3 Bh6 
18.Ba6 Bb7 19.Bxb7 Qxb7 20.Rc2 Ne4 21.Bc1 Bg7 22.Nb5 Rxc2 23.Qxc2 Rc8 24.Qb2 Rc6 25.Be3 
Nc5 26.Qb1 Ne6 27.Qd3 Bf6 28.h3 Ng7 29.Bh6 Nf5 30.Bf4 h5 31.g3 Qd7 32.Rc1 Rxc1+ 33.Bxc1 
Qe6 34.Bd2 Bg7 35.Kg2 Qf6 36.Bc3 Qc6 37.Kh2 Bh6 38.Bd2 Bxd2 39.Qxd2 f6 40.Kg2 Kf7 41.Qc3 
Qxc3 42.Nxc3 Ke6 43.Nb5 g5 44.Kf3 Ng7 45.b4 Kd7 46.a5 bxa5 47.bxa5 Ne6 48.a6 Kc6 49.a7 
Kb7 50.Ke3 Ka8 51.Ke2 Kb7 52.Kd3 Ka8 53.Ke3 Kb7 54.Kf3 Ka8 55.Kg2 Kb7 56.Kf1 Ka8 57.Ke2 
Kb7 58.Kd3 Ka8 59.Ke3 Kb7 60.Ke2 Ka8 61.Kf3 Kb7 62.Ke3 Ka8 63.Ke2 1/2-1/2
```

### Shredder - Ginkgo

[![ShredderGinkgoR5WCSC2015.JPG](/images/0/06/ShredderGinkgoR5WCSC2015.JPG)](/WCSC_2015 "WCSC 2015")

[Shredder](/Shredder "Shredder") by [Stefan Meyer-Kahlen](/Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") vs. Ginkgo operated by [Ingo Bauer](/Ingo_Bauer "Ingo Bauer"). Both programs meet four more times  
to finally decide the [championship](/WCSC_2015 "WCSC 2015"). This one was a tough game for the later champion [[3]](#cite_note-3)

```
[Event "WCSC 2015"]
[Site "Leiden, The Netherlands"]
[Date "2015.07.05"]
[Round "5.4"]
[White "Shredder"]
[Black "Ginkgo"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e6 7.f3 b5 8.g4 h6 9.Qd2 b4 
10.Nce2 e5 11.Nb3 a5 12.Ng3 a4 13.Nc1 d5 14.Bb5+ Bd7 15.Bxd7+ Qxd7 16.exd5 Nxd5 
17.Nd3 a3 18.b3 f6 19.Ne4 Na6 20.O-O-O Nac7 21.Rhe1 O-O-O 22.Qf2 Nxe3 23.Qxe3 Nd5 
24.Qf2 Qc7 25.Rd2 Be7 26.Nec5 Nc3 27.Ne6 Qc6 28.Nxg7 Bf8 29.Nf5 Rh7 30.Ne3 Rhd7 
31.Nf5 Nxa2+ 32.Kb1 Nc3+ 33.Ka1 a2 34.Qf1 Nb1 35.Rde2 Ra7 36.Nb2 Kc7 37.Qg1 Bc5
38.Qg2 Bd4 39.Nxd4 Rxd4 40.Qh1 Ra5 41.h4 Nd2 42.f4 e4 43.Qg1 Nf3 44.Qe3 Nxe1 
45.Rxe1 Qc5 46.g5 hxg5 47.hxg5 fxg5 48.fxg5 Qe5 49.g6 Rd6 50.Qg1 Rd7 51.Qe3 Rc5 
52.Rc1 Qg5 53.Qe1 e3 54.Kxa2 e2 55.Kb1 Re5 56.Nd3 Re4 57.Qh1 Qe3 58.Qh2+ Kb7 
59.g7 Rxg7 60.Qd6 Ka7 61.Kb2 Qd4+ 62.Qxd4+ Rxd4 63.Re1 Re4 64.Kc1 Kb6 65.Kd2 Rc7 
66.Nc1 Rd7+ 67.Nd3 Rde7 68.Nc1 Kb7 69.Rxe2 Rd7+ 70.Ke1 Rg4 71.Nd3 Rh7 72.Re5 Rh1+ 
73.Kd2 Kb6 74.Re2 Ka7 75.c3 bxc3+ 76.Kxc3 Rh3 77.b4 Rgg3 78.Ra2+ Kb6 79.Rd2 Kb5 
80.Kc2 Re3 81.Nc5 Rh4 82.Kc1 Re1+ 83.Rd1 Re8 84.Kd2 Rg4 85.Nd3 Rg2+ 86.Kc3 Rg3 
87.Rd2 Re7 88.Kd4 Rg4+ 89.Kc3 Rc4+ 90.Kb2 Rd4 91.Kc2 Rc7+ 92.Kb2 Ra7 93.Kc3 Rc4+ 
94.Kb3 Rd7 95.Rd1 Re4 96.Kb2 Re2+ 97.Kc3 Re3 98.Kc2 Rc7+ 99.Kb3 Rh7 100.Kb2 Kc4 
101.Nc1 Rh2+ 102.Kb1 Reh3 103.b5 Rh5 104.Rf1 Rxb5+ 105.Ka1 1/2-1/2
```

# See also

- [Anaconda](/Anaconda "Anaconda")
- [GridGinkgo](/GridGinkgo "GridGinkgo")

# Publications

- [Frank Schneider](/Frank_Schneider "Frank Schneider") (**2018**). *ICGA chess in Stockholm: A player perspective*. [ICGA Journal, Vol. 40, No. 3](/ICGA_Journal#40_3 "ICGA Journal")

# Forum Posts

- [Ginkgo's blunders against Shredder in WSCC](http://www.talkchess.com/forum/viewtopic.php?t=56892) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), July 07, 2015

# External Links

## Chess Engine

- [Ginkgo's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=790)

## Misc

- [Ginkgo from Wikipedia](https://en.wikipedia.org/wiki/Ginkgo)
- [Ginkgo biloba from Wikipedia](https://en.wikipedia.org/wiki/Ginkgo_biloba)
- [Ginkgoaceae from Wikipedia](https://en.wikipedia.org/wiki/Ginkgoaceae)
- [Ginkgo - Wikispecies](https://species.wikimedia.org/wiki/Ginkgo)
- [Ginkgo biloba - Wikispecies](https://species.wikimedia.org/wiki/Ginkgo_biloba)
- [Ginkgo biloba - Wikimedia Commons](https://commons.wikimedia.org/wiki/Ginkgo_biloba)
- [Gingo biloba (Goethe poem) from Wikipedia](https://en.wikipedia.org/wiki/Gingo_biloba)

# References

1. [↑](#cite_ref-1) The Ginkgo leaf from [Frank's](/Frank_Schneider "Frank Schneider") or [Ingo's](/Ingo_Bauer "Ingo Bauer") [WCCC 2015](/WCCC_2015 "WCCC 2015") shirt
2. [↑](#cite_ref-2) Photos by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg")
3. [↑](#cite_ref-3) [Ginkgo's blunders against Shredder in WSCC](http://www.talkchess.com/forum/viewtopic.php?t=56892) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), July 07, 2015

**[Up one Level](/Engines "Engines")**