# TSCP

Source: https://www.chessprogramming.org/TSCP

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* TSCP**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Simplicissimus_Cover_page1669.jpg/250px-Simplicissimus_Cover_page1669.jpg)](/File:Simplicissimus_Cover_page1669.jpg)

Simplicius Simplicissimus [[1]](#cite_note-1)

**TSCP**,  
Tom's Simple Chess Program has been written by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan") in 1997 as a device to show the basics of the chess programming. On its home page [[2]](#cite_note-2) one can find not only the program itself, but also a couple of derivatives, like a version with [null move pruning](/Null_Move_Pruning "Null Move Pruning") or with a [bitboard](/Bitboards "Bitboards") move generator. TSCP 1.81 was the test engne in [Mannen's](/Henk_Mannen "Henk Mannen") and [Wiering's](/Marco_Wiering "Marco Wiering") computer chess learning experiments, where they trained several different chess [evaluation](/Evaluation "Evaluation") functions ([neural networks](/Neural_Networks "Neural Networks")) by using [TD(λ) learning](/Temporal_Difference_Learning "Temporal Difference Learning") on a set of database games, published in 2004/05 [[3]](#cite_note-3) [[4]](#cite_note-4).

# Features

- [Board Representation](/Board_Representation "Board Representation") [[5]](#cite_note-5) [[6]](#cite_note-6)
  - [10x12 Mailbox](/10x12_Board "10x12 Board")
  - [Offset Move Generation](/10x12_Board#OffsetMG "10x12 Board")
- [Search](/Search "Search") [[7]](#cite_note-7)
  - [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
  - [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Triangular PV-Table](/Triangular_PV-Table "Triangular PV-Table")
  - [Repetition detection](/SCP#Repetitions "SCP") [[8]](#cite_note-8) [[9]](#cite_note-9) [[10]](#cite_note-10)
- [Evaluation](/Evaluation "Evaluation") [[11]](#cite_note-11)
  - [Material Balance](/Material#Balance "Material")
  - [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
  - [Pawn Structure](/Pawn_Structure "Pawn Structure")

# Licensing

TSCP is open source, but does not fall under [GPL](/Free_Software_Foundation#GPL "Free Software Foundation") or similar licenses, which means that any derivative work must be approved by the author and most likely should not become open source, as it would open the path for violating author's copyright.

# Legal derivatives

- [Caligula](/Caligula_PC "Caligula PC")
- [Capivara](/Capivara "Capivara")
- [CCCP](/CCCP "CCCP")
- [Delphil](/Delphil "Delphil")
- [Deuterium](/Deuterium "Deuterium")
- [FCP](/FCP "FCP")
- [Jester](/Jester_US "Jester US")
- [Popochin](/index.php?title=Popochin&action=edit&redlink=1 "Popochin (page does not exist)")
- [TRACE](/TRACE "TRACE")
- [TSCPGothic](/index.php?title=TSCPGothic&action=edit&redlink=1 "TSCPGothic (page does not exist)")

# Clones

(as listed by author) [[12]](#cite_note-12)

- KasparovX
- Squash
- Replicant
- Tuxedo

# See also

- [MSCP](/MSCP "MSCP")
- [PeSTO's Evaluation Function](/PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")
- [SCP](/SCP "SCP")

# Forum Posts

## 1997 ...

- [Tom Kerrigan's Simple Chess Program](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/f6d1e6096a06fa8) by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), August 13, 1997
- [New version of TSCP!](https://www.stmintz.com/ccc/index.php?id=23632) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), August 02, 1998
- [TSCP derivatives?](https://www.stmintz.com/ccc/index.php?id=24043) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), August 06, 1998
- [Even more simple chess program :-)](https://www.stmintz.com/ccc/index.php?id=58083) by [Eugene Nalimov](/Eugene_Nalimov "Eugene Nalimov"), [CCC](/CCC "CCC"), June 25, 1999
- [Other programs like TSCP, SCP, and MSCP?](https://www.stmintz.com/ccc/index.php?id=64315) by Pete Galati, [CCC](/CCC "CCC"), August 11, 1999
- [NEW VERSION OF TSCP (1.4)](https://www.stmintz.com/ccc/index.php?id=81053) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), December 06, 1999

## 2000 ...

- [NEW VERSION OF TSCP (1.5)](https://www.stmintz.com/ccc/index.php?id=97100) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), February 14, 2000
- [Detecting three-fold repetition?](https://www.stmintz.com/ccc/index.php?id=119867) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), July 17, 2000 » [Repetitions](/Repetitions "Repetitions")

:   [Re: Detecting three-fold repetition?](https://www.stmintz.com/ccc/index.php?id=119911) by [John Stanback](/John_Stanback "John Stanback"), [CCC](/CCC "CCC"), July 17, 2000 » [SCP Repetition detection](/SCP#Repetitions "SCP")

- [Finally, repetition detection! TSCP 1.6 is now available!](https://www.stmintz.com/ccc/index.php?id=120028) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), July 17, 2000
- [Delphi version of TSCP](https://www.stmintz.com/ccc/index.php?id=145411) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), December 18, 2000
- [TSCP enhancements (Re: Short chess programs)](https://www.stmintz.com/ccc/index.php?id=252881) by [Ian Osgood](/Ian_Osgood "Ian Osgood"), [CCC](/CCC "CCC"), September 19, 2002
- [New version of TSCP (1.8)--opening book and hash keys](https://www.stmintz.com/ccc/index.php?id=280383) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), January 30, 2003
- [Looking for tweaked TSCP](https://www.stmintz.com/ccc/index.php?id=298902) by [Jean Efpraxiadis](/index.php?title=Jean_Efpraxiadis&action=edit&redlink=1 "Jean Efpraxiadis (page does not exist)"), [CCC](/CCC "CCC"), June 01, 2003

:   [TSCP with bitboards](https://www.stmintz.com/ccc/index.php?id=298973) by [Russell Reagan](/Russell_Reagan "Russell Reagan"), [CCC](/CCC "CCC"), June 01, 2003

## 2010 ...

- [Movei, The Baron, and TSCP](http://www.talkchess.com/forum/viewtopic.php?t=51063) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), January 23, 2014 » [Movei](/Movei "Movei"), [The Baron](/The_Baron "The Baron")
- [The Baron and TSCP](http://www.talkchess.com/forum/viewtopic.php?t=51073) by [Richard Pijl](/Richard_Pijl "Richard Pijl"), [CCC](/CCC "CCC"), January 27, 2014
- [A bugfix for TSCP](http://www.talkchess.com/forum/viewtopic.php?t=57318) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), August 20, 2015
- [Editing tscp](http://www.talkchess.com/forum/viewtopic.php?t=57366) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), August 24, 2015
- [Symbolic vs tscp: 1,000 game match results](http://www.talkchess.com/forum/viewtopic.php?t=57730) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), September 23, 2015 » [Symbolic](/Symbolic "Symbolic")
- [Symbolic vs tscp: more match results](http://www.talkchess.com/forum/viewtopic.php?t=57776) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), September 28, 2015

## 2020 ...

- [little fun with TSCP](https://prodeo.actieforum.com/t252-little-fun-with-tscp) by [nescitus](/Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 12, 2021 » [PeSTO's Evaluation Function](/PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")

# External Links

- [TSCP - from Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/TSCP)
- [jim - Revision 5535: /vendor/microwindows/current/src/demos/tuxchess](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/)
- [Tom Kerrigan's Simple Chess Program (TSCP) README](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/README.chess) Copyright 1997 [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan")
- [Tscp 1.81](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Tscp%201.81#Tscp_1_81) in [CCRL 40/4](/CCRL "CCRL")

# References

1. [↑](#cite_ref-1) [Simplicius Simplicissimus](https://en.wikipedia.org/wiki/Simplicius_Simplicissimus) Cover page, 1669 by [Hans Jakob Christoffel von Grimmelshausen](https://en.wikipedia.org/wiki/Hans_Jakob_Christoffel_von_Grimmelshausen), [The adventurous Simplicissimus : being the description of the life of a strange vagabond named Melchior Sternfels von Fechshaim : Grimmelshausen, Hans Jakob Christoph von, 1625-1676](https://archive.org/details/adventuroussimpl00grimrich), [Free Download & Streaming : Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
2. [↑](#cite_ref-2) [TSCP - from Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/TSCP)
3. [↑](#cite_ref-3) [Henk Mannen](/Henk_Mannen "Henk Mannen"), [Marco Wiering](/Marco_Wiering "Marco Wiering") (**2004**). *[Learning to play chess using TD(λ)-learning with database games](https://www.semanticscholar.org/paper/Learning-to-Play-Chess-using-TD(lambda)-learning-Mannen-Wiering/00a6f81c8ebe8408c147841f26ed27eb13fb07f3)*. Cognitive Artiﬁcial Intelligence, [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), Benelearn’04, [pdf](https://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/learning-chess.pdf)
4. [↑](#cite_ref-4) [Marco Wiering](/Marco_Wiering "Marco Wiering"), [Jan Peter Patist](https://dblp.org/pid/20/4400.html), [Henk Mannen](/Henk_Mannen "Henk Mannen") (**2005**). *[Learning to Play Board Games using Temporal Difference Methods](https://www.semanticscholar.org/paper/Learning-to-Play-Board-Games-using-Temporal-Methods-Wiering-Patist/7410e2bf16ed184db89f0e3acbbfdad473623b7a)*. Technical Report, [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), UU-CS-2005-048, [pdf](http://webdoc.sub.gwdg.de/ebook/serien/ah/UU-CS/2005-048.pdf)
5. [↑](#cite_ref-5) [TSCP - data.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/data.c)
6. [↑](#cite_ref-6) [TSCP - board.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/board.c)
7. [↑](#cite_ref-7) [TSCP - search.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/search.c)
8. [↑](#cite_ref-8) detects false repetitions in case of exchanging two unequal pieces, also used in [Belzebub](/Belzebub "Belzebub"), credited to [SCP](/SCP "SCP") and [GNU Chess](/GNU_Chess "GNU Chess") by [John Stanback](/John_Stanback "John Stanback")
9. [↑](#cite_ref-9) [Re: Detecting three-fold repetition?](https://www.stmintz.com/ccc/index.php?id=119911) by [John Stanback](/John_Stanback "John Stanback"), [CCC](/CCC "CCC"), July 17, 2000
10. [↑](#cite_ref-10) [Re: Move Tables - explain as if I'm five](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=490672&t=45846) by [Karlo Bala Jr.](/Karlo_Balla "Karlo Balla"), [CCC](/CCC "CCC"), November 05, 2012
11. [↑](#cite_ref-11) [TSCP - eval.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/eval.c)
12. [↑](#cite_ref-12) [TSCP - from Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/TSCP) Hall of shame

**[Up one Level](/Engines "Engines")**