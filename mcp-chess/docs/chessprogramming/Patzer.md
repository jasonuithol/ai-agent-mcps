# Patzer

Source: https://www.chessprogramming.org/Patzer

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Patzer**

**Patzer**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess engine by [Roland Pfister](/Roland_Pfister "Roland Pfister"), later versions were [UCI](/UCI "UCI") compliant, featuring a [parallel search](/Parallel_Search "Parallel Search") and own [endgame bitbases](/Endgame_Bitbases "Endgame Bitbases"), and were able to play [Chess960](/Chess960 "Chess960") [[1]](#cite_note-1). Patzer is famous for solving the [Behting Study](/Behting_Study "Behting Study") [[2]](#cite_note-2) [[3]](#cite_note-3) and a special [draw heuristic](/Draw "Draw") for checking sequences. Patzer was available as [Young Talent](/ChessBase#YoungTalents "ChessBase") by [ChessBase](/ChessBase "ChessBase") running under the [Fritz6 GUI](/Fritz#FritzGUI "Fritz") [[4]](#cite_note-4).

# Tournament Play

Patzer played the [WMCCC 1996](/WMCCC_1996 "WMCCC 1996") in [Jakarta](https://en.wikipedia.org/wiki/Jakarta), the [WMCCC 1997](/WMCCC_1997 "WMCCC 1997") in [Paris](https://en.wikipedia.org/wiki/Paris), the [WCCC 1999](/WCCC_1999 "WCCC 1999") in [Paderborn](https://en.wikipedia.org/wiki/Paderborn), and the [Chess960CWC 2005](/Chess960CWC_2005 "Chess960CWC 2005") and [Chess960CWC 2006](/Chess960CWC_2006 "Chess960CWC 2006") in [Mainz](https://en.wikipedia.org/wiki/Mainz). Further, Patzer was active over the board at [IPCCCs](/IPCCC "IPCCC"), the [5th Spanish Open Computer Chess Championship](/SCCC_1998 "SCCC 1998"), [Dutch Open Computer Chess Championships](/Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"), [International CSVN Tournaments](/International_CSVN_Tournament "International CSVN Tournament"), and the [BELCT 2001](/BELCT_2001 "BELCT 2001").

# Descriptions

[[5]](#cite_note-5)

## 1997

```
Patzer uses state of the art methods as minimal window, hash tables, history table, static exchange evaluation with bitboards, various extensions, recursive nullmove . It has small databases for KPK and KPKP with blocked pawns to decide if it is a win or not. Additionally it can use Thompson's Endgame CDs at ply 0.
```

```
At the moment I am working on including endgame table base support. Patzer has a text interface a well as GUIs for DOS, Windows, OS/2 and X11. It can read/write PGN and EPD files. It has an Interface for Autoplayer232 and for XBoard/WinBoard. It has knowledge of the "wrong" bishop in endgames. A Hypertext User Online Manual is available in German for DOS, Windows, OS/2 and Unix.
```

## 1999

```
Patzer uses the standard alpha-beta PVS search, enhanced by hashtables (4 retries replacement scheme), recursive nullmove (R=2) with verification if only one piece present, special pruning heuristic for ALL-nodes, various extensions. It also uses a special material hash table to adjust the material balance values for certain endgames where the "usual" values do not apply. It values king safety and passed pawns rather high (too high?). It is a incremental bitboard program with attack tables that are also used during move generation and sorting.
```

# Photos

[![FrankRoland.jpg](/images/5/50/FrankRoland.jpg)](http://www.quarkchess.de/csvn2001/body_index.html)

Patzer team [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky") and [Roland Pfister](/Roland_Pfister "Roland Pfister") at [ICT 2001](/ICT_2001 "ICT 2001") [[6]](#cite_note-6)

# See also

- [Woodpusher](/Woodpusher "Woodpusher")

# Namesake

- [Patzer](/index.php?title=Patzer_(K)&action=edit&redlink=1 "Patzer (K) (page does not exist)") by [Werner Koch](/Werner_Koch "Werner Koch") and [Thomas Schäfer](/index.php?title=Thomas_Sch%C3%A4fer&action=edit&redlink=1 "Thomas Schäfer (page does not exist)")

# Forum Posts

## 1998 ...

- [Yes, Patzer really seem to be quite something...](https://www.stmintz.com/ccc/index.php?id=20150) by [Fernando Villegas](/Fernando_Villegas "Fernando Villegas"), [CCC](/CCC "CCC"), June 07, 1998
- [Diepeveen Attack !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30531&p=115980) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 11, 1999

## 2000 ...

- [Patzer](https://www.stmintz.com/ccc/index.php?id=165577) by [Ingo Bauer](/Ingo_Bauer "Ingo Bauer"), [CCC](/CCC "CCC"), April 23, 2001
- [Re: 1 Hour CCR Test by IM Larry Kaufmann / Patzer 3.51](https://www.stmintz.com/ccc/index.php?id=169171) by [Roland Pfister](/Roland_Pfister "Roland Pfister"), [CCC](/CCC "CCC"), May 11, 2001 » [CCR One Hour Test](/CCR_One_Hour_Test "CCR One Hour Test")
- [Goliath Light, Gromit, Patzer, SOS, etc. commercially sold](https://www.stmintz.com/ccc/index.php?id=186009) by [Theo van der Storm](/Theo_van_der_Storm "Theo van der Storm"), [CCC](/CCC "CCC"), August 28, 2001
- [Is there a Tournament book for Patzer?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35220&p=133316) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 05, 2001
- [Re: Position solved](https://www.stmintz.com/ccc/index.php?id=259020) by [Roland Pfister](/Roland_Pfister "Roland Pfister"), [CCC](/CCC "CCC"), October 14, 2002 » [Behting Study](/Behting_Study "Behting Study")
- [Patzer 3.61 UCI vs 3.11 CB = 23 - 15](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42137&p=160957) by Brice Boissel, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 08, 2003
- [Patzer\_299zt](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44653&p=170186) by Telmo Escobar, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), October 18, 2003
- [Any programs besides Yace and Patzer that can use bitbase files](https://www.stmintz.com/ccc/index.php?id=370997) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), June 17, 2004 » [Endgame Bitbases](/Endgame_Bitbases "Endgame Bitbases"), [Yace](/Yace "Yace")

## 2010 ...

- [STS [1-10] Patzer 3.80](http://www.talkchess.com/forum/viewtopic.php?t=35320) by [Swaminathan](/Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](/CCC "CCC"), July 06, 2010 » [Strategic Test Suite](/Strategic_Test_Suite "Strategic Test Suite")

## 2020 ...

- [Patzer 3.80](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74394) by [Dr.Wael Deeb](/index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](/CCC "CCC"), July 06, 2020

# External Links

## Chess Engine

- [Patzer's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=19)
- [Patzer 3.80](http://web.archive.org/web/20090430124900/http://www.superchessengine.com/patzer.htm), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Meet the Authors - PATZER, Roland Pfister](http://www.rebel.nl/authors.htm) hosted by [Ed Schröder](/Ed_Schroder "Ed Schroder")
- [Patzer 3.80](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&eng=Patzer%203.80) in [CCRL 40/40](/CCRL "CCRL")
- [Young Talents, Teil 2](http://scleinzell.schachvereine.de/p_spielprogramme/youngtal_b.shtml) by [Peter Schreiner](/Peter_Schreiner "Peter Schreiner"), Mai 2000, hosted by [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml) (German)

## Misc

- [Patzer - Wiktionary](https://en.wiktionary.org/wiki/Patzer)

:   [patzer - Wiktionary](https://en.wiktionary.org/wiki/patzer)

- [Glossary of chess - P, Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_chess#P)
- [Patzer Opening - Chess Opening Database](http://www.chessvideos.tv/chess-opening-database/search/Patzer-Opening)
- [Bobby Fischer - Wikiquote - Patzer sees a check, gives a check](https://en.wikiquote.org/wiki/Bobby_Fischer) [[7]](#cite_note-7)

# References

1. [↑](#cite_ref-1) [Patzer 3.80](http://web.archive.org/web/20090430124900/http://www.superchessengine.com/patzer.htm), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
2. [↑](#cite_ref-2) [Meet the Authors - PATZER, Roland Pfister](http://www.rebel.nl/authors.htm) hosted by [Ed Schröder](/Ed_Schroder "Ed Schroder")
3. [↑](#cite_ref-3) [Re: Position solved](https://www.stmintz.com/ccc/index.php?id=259020) by [Roland Pfister](/Roland_Pfister "Roland Pfister"), [CCC](/CCC "CCC"), October 14, 2002
4. [↑](#cite_ref-4) [Support - ChessBase, May 28th, 2000](http://www.chessbase.com/support/support.asp?pid=100) (dead link)
5. [↑](#cite_ref-5) [Patzer's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=19)
6. [↑](#cite_ref-6) [1st International CSVN-Tournament 2001](http://www.quarkchess.de/csvn2001/body_index.html) by [Thomas Mayer](/Thomas_Mayer "Thomas Mayer"), [ICT 2001](/ICT_2001 "ICT 2001")
7. [↑](#cite_ref-7) [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) (**1969**). *[My 60 Memorable Games](https://en.wikipedia.org/wiki/My_60_Memorable_Games)*. [Simon & Schuster](https://en.wikipedia.org/wiki/Simon_%26_Schuster)

**[Up one Level](/Engines "Engines")**