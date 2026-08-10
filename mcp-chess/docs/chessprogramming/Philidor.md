# Philidor

Source: https://www.chessprogramming.org/Philidor

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Philidor**

[![](https://upload.wikimedia.org/wikipedia/commons/8/80/Andr%C3%A9_Philidor.jpg)](/File:Andr%C3%A9_Philidor.jpg)

André Danican Philidor [[1]](#cite_note-1)

**Philidor**,  
a series of chess programs by [David Levy's](/David_Levy "David Levy") and [Kevin O’Connell's](/Kevin_O%E2%80%99Connell "Kevin O’Connell") software forge [Philidor Software](/Philidor_Software "Philidor Software"), with [David Broughton](/David_Broughton "David Broughton") and [Mark Taylor](/Mark_Taylor "Mark Taylor") as primary programmers. Philidor was intended as test-bed and development version for programs dedicated for [SciSys'](/Saitek "Saitek") and other manufacturers chess computers, but also to play tournaments with an own-brand.

# History

Philidor was initially written by Broughton in [Z80](/Z80 "Z80") [[2]](#cite_note-2) and subsequent versions in [8086](/8086 "8086") [assembly](/Assembly "Assembly") to either run on an [Osborne](https://en.wikipedia.org/wiki/Osborne_1) and later on an [IBM PC](/IBM_PC "IBM PC") [[3]](#cite_note-3), in 1983 commercialized as [Parker Chess](/Parker_Chess "Parker Chess"). Taylor was responsible to port it to [6502](/6502 "6502") assembly for the SciSys [Chess Champion Mark V](/Chess_Champion_Mark_V "Chess Champion Mark V") branch. Parker Chess and Mark V already applied the first version of [fractional ply deepening](/Depth#FractionalPlies "Depth")  with [extensions](/Extensions "Extensions") and [reductions](/Reductions "Reductions"), aka [SX Algorithm](/SEX_Algorithm "SEX Algorithm"), which was somehow an early implementation of what was later called [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions") [[4]](#cite_note-4). Philidor played the [ACM 1981](/ACM_1981 "ACM 1981") and [ACM 1982](/ACM_1982 "ACM 1982"), the [European MCC 1981](/European_MCC_1981 "European MCC 1981") and [European MCC 1982](/European_MCC_1982 "European MCC 1982"), and the [WMCCC 1981](/WMCCC_1981 "WMCCC 1981") in [Travemünde](https://en.wikipedia.org/wiki/Travem%C3%BCnde) and the [WCCC 1983](/WCCC_1983 "WCCC 1983") in [New York](https://en.wikipedia.org/wiki/New_York_City) [[5]](#cite_note-5).

# Photos & Games

## WMCCC 1981

[![Levy1981.JPG](/images/8/87/Levy1981.JPG)](/File:Levy1981.JPG)

[David Levy](/David_Levy "David Levy") operating Philidor at the [WMCCC 1981](/WMCCC_1981 "WMCCC 1981") [[6]](#cite_note-6) Round 1, [Fidelity X](/Fidelity "Fidelity") - Philidor X [[7]](#cite_note-7)

```
[Event "WMCCC 1981"]
[Site "Travemünde, Germany"]
[Date "1981.09.21"]
[Round "1"]
[White "Fidelity X"]
[Black "Philidor X"]
[Result "0-1"]

1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 e6 5.Nf3 Nc6 6.Na3 cxd4 7.Nb5 Qd7 
8.Bf4 e5 9.Bxe5 Nxe5 10.Nxe5 Qe7 11.Qe2 dxc3 12.Nc7+ Qxc7 13.Ng6+ Ne7 
14.Nxh8 cxb2 15.Qxb2 Qa5+ 16.Ke2 Qa6+ 17.Kd2 Qa5+ 18.Kd1 Bg4+ 19.f3 Rd8+ 
20.Ke2 Be6 21.g3 Nd5 22.Qc1 Bc5 23.Kd1 Nc3+ 24.Kc2 Bf5+ 25.Bd3 Bxd3+ 
26.Kd2 Ne4+ 27.Kd1 Nf2# 0-1
```

## ACM 1982

[![PhilidorFidelity1982.jpg](/images/thumb/c/cd/PhilidorFidelity1982.jpg/560px-PhilidorFidelity1982.jpg)](http://archive.computerhistory.org/resources/still-image/Chess_temporary/still-image/3-1.Game_Room.ACM_NACCC_13.Dallas.102645376.NEWBORN.jpg)

[ACM 1982](/ACM_1982 "ACM 1982"), round 4, Philidor - [Fidelity X](/Fidelity "Fidelity") [[8]](#cite_note-8), [David Levy](/David_Levy "David Levy"), [Dan](/Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen](/Kathe_Spracklen "Kathe Spracklen") [[9]](#cite_note-9)

```
[Event "ACM 1982"]
[Site "Dallas USA"]
[Date "1982.10.26"]
[Round "4"]
[White "Philidor"]
[Black "Fidelity X"]
[Result "0-1"]

1.e4 c5 2.Nf3 Nc6 3.Bb5 e6 4.Nc3 a6 5.Be2 d5 6.O-O d4 7.Nb1 Nf6 
8.d3 Bd6 9.Bg5 O-O 10.Na3 h6 11.Bd2 e5 12.Nc4 Bc7 13.a4 Be6 14.b3 
b5 15.axb5 axb5 16.Rxa8 Qxa8 17.Nb2 Ba5 18.Bxa5 Qxa5 19.Qa1 Ra8
20.Qxa5 Rxa5 21.Rc1 Ra2 22.Rb1 Nd7 23.Nh4 Nb4 24.Bd1 g6 25.h3 Kh7 
26.Nf3 f5 27.exf5 Bxf5 28.Nd2 Nd5 29.g4 Be6 30.Ne4 Nc3 31.Nxc3 dxc3 
32.Nc4 bxc4 33.bxc4 Kg7 34.Kg2 Rb2 35.Ra1 Kf6 36.Ra3 Kg5 37.Rxc3 Kh4 
38.Ra3 h5 39.Ra6 Nf8 40.Ra8 Nh7 41.Rh8 Nf6 42.Rf8 Nd7 43.Re8 Rb6 
44.Rh8 Nf6 45.Bf3 Rb2 46.c3 Rc2 47.Rh6 Kg5 48.Rh8 Rxc3 49.gxh5 
gxh5 50.Rd8 Bd7 51.Be2 Kh4 52.Rf8 Bxh3+ 53.Kh2 Rc2 54.Rxf6 Rxe2 
55.Kg1 Re1+ 56.Kh2 Bf1 57.Rd6 e4 58.d4 Be2 59.dxc5 Bf3 0-1
```

# See also

- [Chess Champion Mark V](/Chess_Champion_Mark_V "Chess Champion Mark V")
- [Intelligent Chess](/Intelligent_Chess "Intelligent Chess")
- [Intelligent Software](/Intelligent_Software "Intelligent Software")
- [Intelligent Chess Software](/Intelligent_Chess_Software "Intelligent Chess Software")
- [Parker Chess](/Parker_Chess "Parker Chess")
- [Philidor Software](/Philidor_Software "Philidor Software")
- [SEX Algorithm](/SEX_Algorithm "SEX Algorithm")
- [Vega](/Vega "Vega")

# Publications

- [David Levy](/David_Levy "David Levy"), [Kevin O’Connell](/Kevin_O%E2%80%99Connell "Kevin O’Connell") (**1981**). *The Best Chess Computer Yet?* [Chess](https://en.wikipedia.org/wiki/CHESS_magazine), July 1981 [[10]](#cite_note-10)
- [David Levy](/David_Levy "David Levy"), [David Broughton](/David_Broughton "David Broughton"), [Mark Taylor](/Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](/ICGA_Journal#12_1 "ICGA Journal")

# Forum Posts

- [Philidor/Parker Chess for PC (1983)](https://www.hiarcs.net/forums/viewtopic.php?t=9941) by Ben Redic Fy Fazan, [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 29, 2020
- [David Broughtons Philidor DOS Schachprogramm](https://www.schachcomputer.info/forum/showthread.php?t=6209) by [mclane](/Thorsten_Czub "Thorsten Czub"), [Schachcomputer.info Community](/Computer_Chess_Forums "Computer Chess Forums"), June 09, 2020 (German)
- [David Broughtons computer chess Engine Philidor / MKV / MK VI](https://prodeo.actieforum.com/t256-david-broughtons-computer-chess-engine-philidor-mkv-mk-vi) by [Mclane](/Thorsten_Czub "Thorsten Czub"), [ProDeo Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 12, 2021

# External Links

## Chess Program

- [Philidor's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=417)

## Philidor

- [Philidor from Wikipedia](https://en.wikipedia.org/wiki/Philidor)
- [François-André Danican Philidor from Wikipedia](https://en.wikipedia.org/wiki/Fran%C3%A7ois-Andr%C3%A9_Danican_Philidor)

# References

1. [↑](#cite_ref-1) Portrait from *L’analyze des échecs*. London, second edition, 1777, [François-André Danican Philidor from Wikipedia](https://en.wikipedia.org/wiki/Fran%C3%A7ois-Andr%C3%A9_Danican_Philidor)
2. [↑](#cite_ref-2) [The Twelfth ACM's North American Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6ce737), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.1981_ACM_NACCC/1981_ACM_NACCC.sm.062303017.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
3. [↑](#cite_ref-3) [The Fourth World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c8af8) (labeled 22nd ACM), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1983_WCCC/1983-%20WCCC.062303061.sm.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_36_C.pdf) from [Danny Kopec](/Danny_Kopec "Danny Kopec")
4. [↑](#cite_ref-4) [David Levy](/David_Levy "David Levy"), [David Broughton](/David_Broughton "David Broughton"), [Mark Taylor](/Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](/ICGA_Journal#12_1 "ICGA Journal")
5. [↑](#cite_ref-5) [Philidor's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=417)
6. [↑](#cite_ref-6) [László Lindner](/L%C3%A1szl%C3%B3_Lindner "László Lindner"), A SZÁMÍTÓGÉPES SAKK KÉPEKBEN című melléklete - The pictures of the Beginning of Chess Computers
7. [↑](#cite_ref-7) [Travemünde 1981 - Chess - Round 1 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=67&round=1&id=1)
8. [↑](#cite_ref-8) [PGN Download NACCC](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=60&Itemid=26&lang=en) from [Computerschaak/Downloads/Games](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=13&Itemid=26&lang=en) hosted by [CSVN](/CSVN "CSVN")
9. [↑](#cite_ref-9) [archive.computerhistory.org - /resources/still-image](http://archive.computerhistory.org/resources/still-image/Chess_temporary/still-image/) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
10. [↑](#cite_ref-10) *The Best Chess Computer Yet?* [part 1](http://www.flickr.com/photos/10261668@N05/5856426830/in/photostream), [part 2](http://www.flickr.com/photos/10261668@N05/5855873337/in/photostream), [part 3](http://www.flickr.com/photos/10261668@N05/5855873365/in/photostream) by [Chewbanta](/Steve_Blincoe "Steve Blincoe")

**[Up one Level](/Engines "Engines")**