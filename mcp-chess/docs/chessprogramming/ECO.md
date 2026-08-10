# ECO

Source: https://www.chessprogramming.org/ECO

**[Home](/Main_Page "Main Page") \* [Knowledge](/Knowledge "Knowledge") \* [Opening Book](/Opening_Book "Opening Book") \* ECO**

**Encyclopaedia of Chess Openings**, (ECO)  
a de facto standard of a classification system for chess openings, established by [Chess Informant](https://en.wikipedia.org/wiki/Chess_Informant) since 1966, using a coding system that has been widely-used and adopted by other chess publications, chess programs, [databases](/Databases "Databases") and [GUIs](/GUI "GUI"). There are five main categories, "A" to "E", which are divided into one hundred subcategories each, in total 500 from A00 to E99. ECO code is a registered trademark of Chess Informant [[1]](#cite_note-1) .

# Main Classifications

- A - [Flank openings](https://en.wikipedia.org/wiki/Flank_opening)
- B - [Semi-Open Games](https://en.wikipedia.org/wiki/Semi-Open_Game) other than the [French Defence](https://en.wikipedia.org/wiki/French_Defence)
- C - [Open Games](https://en.wikipedia.org/wiki/Open_Game) and the [French Defence](https://en.wikipedia.org/wiki/French_Defence)
- D - [Closed Games](https://en.wikipedia.org/wiki/Closed_Game) and [Semi-Closed Games](https://en.wikipedia.org/wiki/Semi-Closed_Game)
- E - [Indian Defences](https://en.wikipedia.org/wiki/Indian_Defence)

# Ambiguity

ECO codes are defined by halfmove sequences from the [initial position](/Initial_Position "Initial Position") with non-uniform length or depth of one to 28 [plies](/Ply "Ply") [[2]](#cite_note-2) . The position reached after that move sequence associates the ECO code. Depending on the particular opening and its classification granulation and depth, the ECO assignment may change during the course of the opening from halfmove to halfmove to more specific classified ECO codes until it sticks with the final assessment. However, due to [transpositions](/Transposition "Transposition"), even into [color flipped positions](/Color_Flipping "Color Flipping"), ambiguity manifests in different implementations of chess engines, [databases](/Databases "Databases") and [GUIs](/GUI "GUI"). As pointed out by [Gregor Cramer](/index.php?title=Gregor_Cramer&action=edit&redlink=1 "Gregor Cramer (page does not exist)"), [ChessBase](/ChessBase_(Database) "ChessBase (Database)") assigns "1.f4 e5 2.d4" to A02, and "1.d4 e5 2.f4" to A40, but [Scidb](/Scidb "Scidb") assigns both lines to A02 [[3]](#cite_note-3) . Since there are zillions of transpositions f.i. between Scandinavian gambit B01, Caro Kann B13, B14, Symmetrical English A35, and Queens Gambit D26, D40, ..., the following position has ambiguous ECO assignments. How should it be classified? Depending on the sequence of moves reaching it?

|  |
| --- |
|                                                                                     ♜ ♝♛♚♝ ♜ ♟♟   ♟♟♟   ♞ ♟       ♞        ♙       ♘  ♘   ♙♙   ♙♙♙ ♖ ♗♕♔♗ ♖ |

r1bqkb1r/pp3ppp/2n1p3/3n4/3P4/2N2N2/PP3PPP/R1BQKB1R w KQkq -   
Four of many possible move sequences to reach the same position:

```
1.e4 d5 2.exd5 Nf6 3.c4 c6 4.d4 cxd5 5.Nc3 Nc6 6.Nf3 e6 7.cxd5 Nxd5
1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 e6 5.Nf3 Nf6 6.cxd5 Nxd5 7.Nc3 Nc6
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.cxd5 Nxd5 6.e3 cxd4 7.exd4 Nc6
1.c4 c5 2.Nc3 Nf6 3.Nf3 Nc6 4.e3 e6 5.d4 cxd4 6.exd4 d5 7.cxd5 Nxd5
```

# Sample Implementation

The book identification code of the [opening book](/Opening_Book "Opening Book") in [IsiChess](/IsiChess "IsiChess") (commercial [DOS](/MS-DOS "MS-DOS") version) had all book lines defined in a [PGN](/Portable_Game_Notation "Portable Game Notation")-like textfile with a descriptive name and ECO code associated, much more than the 500 determinative ECO lines and full of transpositions, merged into an opening tree similar to a persistent [transposition table](/Transposition_Table "Transposition Table") indexed by the [Zobrist key](/Zobrist_Hashing "Zobrist Hashing"), keeping not only a list of possible moves from the current position, but also a list of different predecessor moves aka indices to the different opening lines. Its [book editor](/IsiChess#Book_Editor "IsiChess") has not only an opening tree view, but also a list view of opening lines where multiple lines with different last moves and possibly ECO codes may appear, leading to the current position.

[![IsiChessBook.jpg](/images/9/9e/IsiChessBook.jpg)](/File:IsiChessBook.jpg)

# See also

- [NIC-Key](/NIC-Key "NIC-Key")

# Forum Posts

## 1995 ...

- [Opening taxonomy](https://groups.google.com/d/msg/rec.games.chess.computer/twuuIKTUqRw/bCN6Jn9zGOcJ) by [Hugh S. Myers](/Hugh_S._Myers "Hugh S. Myers"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), September 12, 1995
- [Electronic ECO](https://www.stmintz.com/ccc/index.php?id=33684) by C.M.A., [CCC](/CCC "CCC"), November 23, 1998
- [Mercilous Attack? What is it? What is the ECO on it?](https://www.stmintz.com/ccc/index.php?id=59677) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), July 07, 1999

## 2000 ...

- [ECO question](https://www.stmintz.com/ccc/index.php?id=100213) by [Robert Pope](/Robert_Pope "Robert Pope"), [CCC](/CCC "CCC"), March 04, 2000
- [implement program to identify eco code](https://www.stmintz.com/ccc/index.php?id=229375) by Sylvain Eche, [CCC](/CCC "CCC"), May 13, 2002
- [ECO-Browser in Scid 3.6.1 (under WinXP)](https://www.stmintz.com/ccc/index.php?id=388737) by [Daniel Clausen](/index.php?title=Daniel_Clausen&action=edit&redlink=1 "Daniel Clausen (page does not exist)"), [CCC](/CCC "CCC"), September 23, 2004
- [ECO Codes as PGN 1.16 available for download](https://www.stmintz.com/ccc/index.php?id=426462) by [Michael Diosi](/index.php?title=Michael_Diosi&action=edit&redlink=1 "Michael Diosi (page does not exist)"), [CCC](/CCC "CCC"), May 17, 2005

## 2010 ...

- [Scid.eco](https://www.mail-archive.com/scid-users@lists.sourceforge.net/msg06639.html) by [Gregor Cramer](/index.php?title=Gregor_Cramer&action=edit&redlink=1 "Gregor Cramer (page does not exist)"), [scid-users](https://www.mail-archive.com/scid-users@lists.sourceforge.net/), April 19, 2014
- [code method to get ECO code/opening name](http://www.talkchess.com/forum/viewtopic.php?t=52141) by [Mike Adams](/index.php?title=Mike_Adams&action=edit&redlink=1 "Mike Adams (page does not exist)"), [CCC](/CCC "CCC"), April 27, 2014
- [Hint for ChessGUI users](http://www.talkchess.com/forum/viewtopic.php?t=59970) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), April 26, 2016 » [ChessGUI](/ChessGUI "ChessGUI")
- [Tool to ECO classify EPD positions?](http://www.talkchess.com/forum/viewtopic.php?t=64744) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), July 28, 2017

## 2020 ...

- [Chess opening database with names](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75878) by Peperoni, [CCC](/CCC "CCC"), November 20, 2020

# External Links

- [Encyclopaedia of Chess Openings (ECO) from Wikipedia](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings)
- [List of chess openings from Wikipedia](https://en.wikipedia.org/wiki/List_of_chess_openings)
- [ECO Codes - 365Chess.com](https://www.365chess.com/eco.php)
- [ECO Listing - chessgames.com](https://www.chessgames.com/chessecohelp.html)
- [ECO Opening Classification (11)](https://web.archive.org/web/20180821064736/http://www.playwitharena.com/?User_Files%2C_Engines:ECO_Opening_Classification_%2811%29) from [Arena Chess GUI](/Arena "Arena") developed by [Christopher Conkie](/index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [eco.pgn](https://www.cs.kent.ac.uk/~djb/pgn-extract/eco.pgn) from [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/) by [David J. Barnes](/David_J._Barnes "David J. Barnes") » [pgn-extract](/Pgn-extract "Pgn-extract")
- [Encyclopaedia of Chess Openings file](https://raw.githubusercontent.com/BookOwl/scid-vs-pc/master/scid.eco) for [Scid vs. PC](/Scid_vs._PC "Scid vs. PC")
- [arasan-chess/book/eco at master · jdart1/arasan-chess · GitHub](https://github.com/jdart1/arasan-chess/blob/master/book/eco) by [Jon Dart](/Jon_Dart "Jon Dart")
- [icsbot/eco.txt at master · seberg/icsbot · GitHub](https://github.com/seberg/icsbot/blob/master/misc/eco.txt) by [Sebastian Berg](/index.php?title=Sebastian_Berg&action=edit&redlink=1 "Sebastian Berg (page does not exist)")
- [Chess Programming - CleanPGN](http://www.sdragons.org/Software/chess_programming.html) by [Hugh S. Myers](/Hugh_S._Myers "Hugh S. Myers")
- [OPEX - Chess Openings Explorer](https://opex.ebemunk.com/) by [Buğra Fırat](/index.php?title=Bu%C4%9Fra_F%C4%B1rat&action=edit&redlink=1 "Buğra Fırat (page does not exist)")
- [Opening statistics](https://www.computerchess.org.uk/ccrl/4040/eco_report_by_eco.html) from [CCRL 40/15](/CCRL "CCRL")
- [Opening statistics](https://www.computerchess.org.uk/ccrl/404/eco_report_by_eco.html) from [CCRL Blitz](/CCRL "CCRL")

# References

1. [↑](#cite_ref-1) [List of chess openings from Wikipedia](https://en.wikipedia.org/wiki/List_of_chess_openings)
2. [↑](#cite_ref-2) [D69: Queen's Gambit Declined, Orthodox defence, classical, 13.en - 365Chess.com](http://www.365chess.com/eco/D69_Queen%27s_Gambit_Declined_Orthodox_defence_classical_13.en)
3. [↑](#cite_ref-3) [Scid.eco](https://www.mail-archive.com/scid-users@lists.sourceforge.net/msg06639.html) by [Gregor Cramer](/index.php?title=Gregor_Cramer&action=edit&redlink=1 "Gregor Cramer (page does not exist)"), [scid-users](https://www.mail-archive.com/scid-users@lists.sourceforge.net/), April 19, 2014

**[Up one level](/Opening_Book "Opening Book")**