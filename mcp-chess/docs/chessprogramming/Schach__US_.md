# Schach (US)

Source: https://www.chessprogramming.org/Schach_(US)

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Schach**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/KnightsTemplarPlayingChess1283.jpg/330px-KnightsTemplarPlayingChess1283.jpg)](/File:KnightsTemplarPlayingChess1283.jpg)

Knights Templar playing Chess [[1]](#cite_note-1) [[2]](#cite_note-2)

**Schach**,  
an early chess program by [Rolf C. Smith](/Rolf_C._Smith "Rolf C. Smith") and [Franklin D. Ceruti](/Franklin_D._Ceruti "Franklin D. Ceruti"), competing the first three [ACM North American Computer Chess Championships](/ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), the [ACM 1970](/ACM_1970 "ACM 1970"), [ACM 1971](/ACM_1971 "ACM 1971") and the [ACM 1972](/ACM_1972 "ACM 1972"). Schach was originally developed in 1968 as part of the requirements for the degree of Master of Computer Science at [Texas A&M University](https://en.wikipedia.org/wiki/Texas_A%26M_University) under advisor [Dan D. Drew](/Dan_D._Drew "Dan D. Drew") [[3]](#cite_note-3), was written in [Fortran](/Fortran "Fortran") and had an implementation of a [SOMA](/SOMA "SOMA") like algorithm instead of [quiescence search](/Quiescence_Search "Quiescence Search"). [Static exchange evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation") was further used at [interior nodes](/Interior_Node "Interior Node") for [move ordering](/Move_Ordering "Move Ordering") and [pruning](/Pruning "Pruning") aka reducing the width of a [Shannon Type B](/Type_B_Strategy "Type B Strategy") program.

# Description

[Rolf C. Smith's](/Rolf_C._Smith "Rolf C. Smith") description from the [ACM 1971](/ACM_1971 "ACM 1971") panel session [[4]](#cite_note-4):

SCHACH was originally developed in 1968 as part of the requirements for the degree of Master of Computing Science at Texas A&M University. Basic FORTRAN was chosen as the language which would lend itself best to the programming and the degree of machine independence and availability desired by its authors. It was initially programmed via the [RAX terminal system](https://en.wikipedia.org/wiki/MUSIC/SP) on an [IBM 360/40](/IBM_360 "IBM 360") belonging to LTV on loan to the University. In late 1968 it was switched over to A&M's new IBM 360/65; in 1969 it ran on IBM 360/50's in [Saigon](https://en.wikipedia.org/wiki/Ho_Chi_Minh_City), [RVN](https://en.wikipedia.org/wiki/South_Vietnam) and in [Sadahip](https://en.wikipedia.org/wiki/Sattahip_District), [Thailand](https://en.wikipedia.org/wiki/Thailand), when the authors were transferred overseas with the [U.S. Air Force](https://en.wikipedia.org/wiki/United_States_Air_Force). It has most recently run on an [IBM 1410](https://en.wikipedia.org/wiki/IBM_1410) and is now in residence on a [UNIVAC 418 III](/UNIVAC_418 "UNIVAC 418").

The backbone of SCHACH is the concept of [piece board control](/Square_Control "Square Control"), defined as all squares on which a piece exerts direct or indirect influence (can move to in a capture mode). Utilizing this concept we have found that a pseudo-dynamic position projection can be effected in a static environment on a local scale. Significant is that this is accomplished through the control concept without actual [move regeneration](/Move_Generation "Move Generation") in depth. Coupled with a heuristic method developed for examination of multiple piece exchanges (SWAP), it is theoretically possible to predict/project move sequences up to 36 [plys](/Ply "Ply") in depth with substantial accuracy. This is used in lieu of [alpha-beta pruning](/Alpha-Beta "Alpha-Beta") or dynamic [move-generation ordering](/Move_Ordering "Move Ordering"), permitting [pre-pruning](/Pruning "Pruning") of move-group subsets prior to recursive evaluation and deeper ply explorations.

The following items are considered significant enough to warrant discussion during the panel session:

1. Piece board control methods, theory, tabling and application.
2. Dynamic piece reweighting system.
3. Approaches to minimax criteria and systems of treeing used to date.
4. Table of interrelated values/weights for the overall static evaluation "polynomial" and positionality criteria. In support of this are some sample sequences which demonstrate the effect of some of the major criteria in a stand-alone use for static evaluation.
5. Coding optimization and considerations in logic optimization for elimination of repetitive and recursive portions in favor of progressive deepening and reevaluation compression and retention.
6. Book opening considerations.
7. Macro flow of program logic and micro explanation of basic table design.
8. Statistics accrued in game play.

[Captain](https://en.wikipedia.org/wiki/Captain_%28United_States_O-3%29) Smith collaborated with Captain Franklin D. Ceruti, [USAF](https://en.wikipedia.org/wiki/United_States_Air_Force), in the development of SCHACH.

# Selected Games

[ACM 1972](/ACM_1972 "ACM 1972"), round 2, [Leverett CP](/Leverett_CP "Leverett CP") - Schach [[5]](#cite_note-5)

```
[Event "ACM 1972"]
[Site "Boston USA"]
[Date "1972.08.14"]
[Round "2"]
[White "Leverett CP"]
[Black "Schach"]
[Result "0-1"]

1.Nc3 d5 2.e4 dxe4 3.Nxe4 e5 4.Qh5 Nc6 5.Nf3 Nf6 6.Nxf6+ gxf6 7.Bc4
Qd7 8.Qxf7+ Qxf7 9.Bxf7+ Kxf7 10.O-O Rg8 11.d3 Bc5 12.Be3 Nd4 13.Nxd4
exd4 14.Bf4 Bd6 15.Bg3 Be6 16.a4 Rg5 17.h4 Rg4 18.b4 Bxg3 19.fxg3
Rxg3 20.Rf4 Rd8 0-1
```

# Continuation

*see main article [Schach 2](/Schach "Schach")*

According to the [Chessgames.com](https://en.wikipedia.org/wiki/Chessgames.com) description [[6]](#cite_note-6), a 1970 version of Schach was extended in 1978 to become [Schach 2](/Schach "Schach"), ported to [Algol](/Algol "Algol") by [Matthias Engelbach](/Matthias_Engelbach "Matthias Engelbach"), at that time [German military](https://en.wikipedia.org/wiki/Bundeswehr) officer and student at [Bundeswehr University Munich](https://en.wikipedia.org/wiki/Bundeswehr_University_Munich). In the early 90s, along with co-author [Thomas Kreitmair](/Thomas_Kreitmair "Thomas Kreitmair"), Schach 3.0 was a complete re-write in [x86](/X86 "X86") (486) [assembly language](/Assembly "Assembly") for [PCs](/IBM_PC "IBM PC"), to become one of the fastest programs of its time [[7]](#cite_note-7).

# See also

- [Schach 2](/Schach "Schach") by [Matthias Engelbach](/Matthias_Engelbach "Matthias Engelbach"), 3.0 with [Thomas Kreitmair](/Thomas_Kreitmair "Thomas Kreitmair")
- [Schach MV 5,6](/Schach_MV_5,6 "Schach MV 5,6") by [Helmut Richter](/Helmut_Richter "Helmut Richter")

# Publications

- [Rolf C. Smith](/Rolf_C._Smith "Rolf C. Smith") (**1969**). *The SCHACH Chess program*. [ACM SIGART](/ACM#SIGART "ACM"), Vol. 15
- [Ben Mittman](/Ben_Mittman "Ben Mittman"), [Rolf C. Smith](/Rolf_C._Smith "Rolf C. Smith") et al. (**1971**) *[Computer Chess Programs (Panel)](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d1ee8)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-3.computer_chess_panel.mittman/3-1%20and%203-3.computer_chess_panel.mittman_etc.1971.ACM.062303021.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")

# External Links

- [Schach from Wikipedia](https://en.wikipedia.org/wiki/Schach)
- [Schach from Wikipedia.de](http://de.wikipedia.org/wiki/Schach) (German) = [Chess](/Chess "Chess")
- [Schach (Zeitschrift) from Wikipedia.de](http://de.wikipedia.org/wiki/Schach_%28Zeitschrift%29) (German [Chess periodical](https://en.wikipedia.org/wiki/List_of_chess_periodicals))

# References

1. [↑](#cite_ref-1) [Knights Templar](https://en.wikipedia.org/wiki/Knights_Templar) playing Chess, [Libro de los juegos](https://en.wikipedia.org/wiki/Libro_de_los_juegos) commissioned by [Alfonso X of Castile](https://en.wikipedia.org/wiki/Alfonso_X_of_Castile), 1283
2. [↑](#cite_ref-2) [Chess from Wikipedia](https://en.wikipedia.org/wiki/Chess)
3. [↑](#cite_ref-3) [ACM 1970 - Special Events for Association for Computing Machinery, 25th National Conference](http://archive.computerhistory.org/projects/chess/related_materials/text/3-0%20and%203-1%20and%203-2%20and%203-3%20and%205-2.1970_ACM_70/1970_ACM.062303010.pdf) (pdf), hosted by [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
4. [↑](#cite_ref-4) [Ben Mittman](/Ben_Mittman "Ben Mittman"), [Rolf C. Smith](/Rolf_C._Smith "Rolf C. Smith") et al. (**1971**) *[Computer Chess Programs (Panel)](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d1ee8)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-3.computer_chess_panel.mittman/3-1%20and%203-3.computer_chess_panel.mittman_etc.1971.ACM.062303021.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
5. [↑](#cite_ref-5) [PGN Download NACCC](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=60&Itemid=26&lang=en) from [Computerschaak/Downloads/Games](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=13&Itemid=26&lang=en), [CSVN](/CSVN "CSVN") site
6. [↑](#cite_ref-6) [The chess games of Schach 2 3](http://www.chessgames.com/perl/chessplayer?pid=64934) from [Chessgames.com](https://en.wikipedia.org/wiki/Chessgames.com)
7. [↑](#cite_ref-7) [Schach 3.0](https://www.stmintz.com/ccc/index.php?id=222098) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), April 08, 2002

**[Up one level](/Engines "Engines")**