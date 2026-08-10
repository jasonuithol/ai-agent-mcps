# Searcher

Source: https://www.chessprogramming.org/Searcher

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Searcher**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Searcher_ronquil.jpg/330px-Searcher_ronquil.jpg)](/File:Searcher_ronquil.jpg)

[Searcher (Bathymaster signatus)](https://en.wikipedia.org/wiki/Bathymaster_signatus) [[1]](#cite_note-1)

**Searcher**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant, private [[2]](#cite_note-2) chess engine written by [Frank Phillips](/Frank_Phillips "Frank Phillips"). It is a [bitboard](/Bitboards "Bitboards") engine, although it didn't used [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards") for [move generation](/Move_Generation "Move Generation") [[3]](#cite_note-3). In 2008, Frank implemented [Magic Bitboards](/Magic_Bitboards "Magic Bitboards"), and started to rewrite and improve his "ancient code" [[4]](#cite_note-4).

# Tournament Play

Searcher played four consecutive, strong [CCT Tournaments](/CCT_Tournaments "CCT Tournaments"), the [CCT3](/CCT3 "CCT3") (5th/32), [CCT4](/CCT4 "CCT4") (6th/46), [CCT5](/CCT5 "CCT5") (15th/45), and the [CCT6](/CCT6 "CCT6") (12th/54).

# Quotes

[Frank Phillips](/Frank_Phillips "Frank Phillips") in his [CCT3](/CCT3 "CCT3") report on Searcher [[5]](#cite_note-5):

```
My chess program (before then there was a knight tour, connect4, simple othello and others to learn recursion and search etc) started as my expanded interpretation of TSCP, helped by articles on the internet (particularly Marsland's excellent summary of the anatomy of a chess program) [6] and of course by members of CCC and particulalry Bob Hyatt. Now its origins are unrecognisable, although mailbox is still used to precompute move tables - simply because I had already written that code.  The last major rewrite, two years or so ago introduced bitboards (because they looked interesting and Bob is always talking about them) to use mainly in evaluation. Move generation, king attacks, is a square attacked, SEE etc is a mixture of bitboards for the easy cases (knights, pawns, king) and offset precomputed arrays for the sliders. Like Dan Newman (I think), I also use bitboards to screen for _potential_ slider attacks etc to reduce work, but do not precompute the rank, file or diagonal states to give an index to a bitboard of the first square attacked.  Full and rotated bitboards implementation next time.  Maybe after an IQ transplant, or to get cheap mobility.  Move generation is not a massive drain in my program, so bitboards are more valuable for their other benefits.  Search is pretty standard Crafty type approach.  Tried and discarded Dark Thought type pruning.  But will try again after listening to Bruce on CCT3.  Extensions as recommended by Bob and limited as recommend by Bruce, although I still have recapture extension because it seems to help me and do a bit extra for passed pawns. Tested other and other variations of extensions without much impact.  All sorts of daft ideas. Trans/ref hash and hashing of basic pawn structure elements. Nalimov EGTBs (3 years to generate all 5 man on and off, on a variety of machines.  Thanks Eugene), primitive book learning and positional learning. The evaluation has become increasingly sophisticated (voluminous anyway) with time. Playing on the chess servers, even for a brief time, has certainly caused me to add stuff.
```

# Selected Games

[CCT4](/CCT4 "CCT4"), round 11, Searcher - [Goliath-Blitz](/Goliath "Goliath") [[7]](#cite_note-7)

```
[Event "CCT4"]
[Site "Internet Chess Club"]
[Date "2002.01.27"]
[Round "11"]
[White "SearcherX"]
[Black "Goliath-Blitz"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be2 e5 7.Nb3 Be7 
8.O-O O-O 9.Be3 Be6 10.Nd5 Nxd5 11.exd5 Bf5 12.f4 e4 13.c3 Re8 14.Nd2 
h6 15.Bg4 Qc8 16.Bxf5 Qxf5 17.Qb3 Nd7 18.Qxb7 Reb8 19.Qc6 Rc8 20.Qa4 Nf6 
21.Bd4 Nxd5 22.Rae1 Bh4 23.g3 e3 24.Bxe3 Nxe3 25.Rxe3 Bf6 26.Ne4 Be7 
27.Nf2 Bf6 28.Rd1 Rab8 29.Re2 Rb6 30.Rdd2 g6 31.Qe4 Qd7 32.Qd5 Bg7 33.Ne4 
Rcc6 34.a4 Kh7 35.Rf2 f5 36.Nc5 Qc8 37.Ne6 Rb8 38.Rfe2 Qb7 39.Nxg7 Kxg7 
40.Re6 Rf8 41.Rxd6 Qb6+ 42.Kg2 Rxd6 43.Qxd6 Rf6 44.Qxb6 Rxb6 45.b4 Kf6 
46.Rd4 Ke6 47.Kf3 Rb7 48.Ke3 Rb8 49.Rc4 Kd6 50.Kd4 h5 51.Rc5 Kd7 52.Ra5 
Rb6 53.c4 Rxb4 54.Rxa6 Rb2 55.h4 Ra2 56.Rxg6 Ke7 57.Rg5 Ke6 58.Rxh5 Rxa4 
59.Rh6+ Ke7 60.h5 Ra3 61.Rg6 Ra2 1-0
```

# Forum Posts

- [CCT3 Day 1 reflections](https://www.stmintz.com/ccc/index.php?id=171919) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), May 27, 2001 » [CCT3](/CCT3 "CCT3")
- [CCT3 day2](https://www.stmintz.com/ccc/index.php?id=172027) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), May 28, 2001
- [A fun game between Searcher and PostModernist](https://www.stmintz.com/ccc/index.php?id=179706) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), July 14, 2001 » [PostModernist](/PostModernist "PostModernist")
- [3 fold repetiton (Seacher v Postmodernist)](https://www.stmintz.com/ccc/index.php?id=216120) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), March 02, 2002 » [Repetitions](/Repetitions "Repetitions")
- [Re: Simple questions about bitboards](https://www.stmintz.com/ccc/index.php?id=317184) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), September 22, 2003 » [BitScan](/BitScan "BitScan")
- [Re: Speedup with bitboards on 64-bit CPUs](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=114674&t=13426) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), April 28, 2007
- [magic move - bitboard orientation](http://www.talkchess.com/forum/viewtopic.php?t=21543) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), June 01, 2008 » [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")
- [xboard and engine match using remote machine](http://www.talkchess.com/forum/viewtopic.php?t=40448) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), September 18, 2011 » [XBoard](/XBoard "XBoard")

# External Links

- [SearcherX](http://www6.chessclub.com/finger/SearcherX) at [ICC](/index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")
- [Searcher (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Searcher)
- [The Searchers (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/The_Searchers)

:   [The Searchers (film) from Wikipedia](https://en.wikipedia.org/wiki/The_Searchers_%28film%29)

- [The Searchers](/Category:The_Searchers "Category:The Searchers") - [Sweets For My Sweet](https://en.wikipedia.org/wiki/Sweets_for_My_Sweet) (1963), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Photo by Jan Haaga, from [NOAA's](https://en.wikipedia.org/wiki/National_Oceanic_and_Atmospheric_Administration) [Alaska Fisheries Science Center](http://www.afsc.noaa.gov/kodiak/photo/fishsearcher.htm), [Bathymaster signatus from Wikipedia](https://en.wikipedia.org/wiki/Bathymaster_signatus)
2. [↑](#cite_ref-2) [Private Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:private_engine_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
3. [↑](#cite_ref-3) [Re: Simple questions about bitboards](https://www.stmintz.com/ccc/index.php?id=317184) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), September 22, 2003
4. [↑](#cite_ref-4) [magic move - bitboard orientation](http://www.talkchess.com/forum/viewtopic.php?t=21543) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), June 01, 2008
5. [↑](#cite_ref-5) [CCT3 day2](https://www.stmintz.com/ccc/index.php?id=172027) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), May 28, 2001
6. [↑](#cite_ref-6)  [Tony Marsland](/Tony_Marsland "Tony Marsland") (**1995**). *[The Anatomy of Chess Programs](http://ilk.uvt.nl/icga/games/chess/anatomy.php)*. [8th World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cd6ed) pp. 4-6, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1995_WCCC/1995%20WCCC.062303014.sm.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), Courtesy of [Monroe Newborn](/Monroe_Newborn "Monroe Newborn")
7. [↑](#cite_ref-7) PGN download from [CCT4](http://www.vrichey.de/cct4/) hosted by [Volker Richey](/index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")

**[Up one level](/Engines "Engines")**