# SOS

Source: https://www.chessprogramming.org/SOS

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* SOS**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Silicon_on_Sapphire_-_gate_stack_DE.svg/330px-Silicon_on_Sapphire_-_gate_stack_DE.svg.png)](/File:Silicon_on_Sapphire_-_gate_stack_DE.svg)

[Silicon on Sapphire](https://en.wikipedia.org/wiki/Silicon_on_sapphire) [[1]](#cite_note-1)

**SOS**,  
a chess program developed and written by [Rudolf Huber](/Rudolf_Huber "Rudolf Huber") in [C](/C "C"). In its early times in the mid 90s, SOS running on various platforms and operating systems had an own futuristic [graphical user interface](/GUI "GUI"). SOS supported the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") [[2]](#cite_note-2) , was available as [Young Talent](/ChessBase#YoungTalents "ChessBase") by [ChessBase](/ChessBase "ChessBase") running under the [Fritz6 GUI](/Fritz#FritzGUI "Fritz"), and since Rudolf is co-designer of the protocol, it finally changed to [UCI](/UCI "UCI") [[3]](#cite_note-3) , and is a *Partner Chess Engine* of [Arena](/Arena "Arena") [[4]](#cite_note-4) [[5]](#cite_note-5) . SOS evolved from [PVS](/Principal_Variation_Search "Principal Variation Search") to [MTD(f)](/MTD(f) "MTD(f)") and further as [ParSOS](/ParSOS "ParSOS") to [parallel](/Parallel_Search "Parallel Search") MTD(f).

# Tournaments

SOS has its debut at [Don Beal's](/Don_Beal "Don Beal") [1993 QMW Uniform-Platform Computer Chess Championship](/UPCCC_1993 "UPCCC 1993"). It further played various [World Microcomputer Chess](/World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship") and [World Computer Chess Championships](/World_Computer_Chess_Championship "World Computer Chess Championship"), the [WMCCC 1993](/WMCCC_1993 "WMCCC 1993"), [WCCC 1995](/WCCC_1995 "WCCC 1995"), [WMCCC 1997](/WMCCC_1997 "WMCCC 1997"), [WCCC 1999](/WCCC_1999 "WCCC 1999"), and the [WMCCC 2000](/WMCCC_2000 "WMCCC 2000"), where SOS won the title of the Amateur World Microcomputer Chess Champion. [ParSOS](/ParSOS "ParSOS") continued playing the [WMCCC 2001](/WMCCC_2001 "WMCCC 2001"), [WCCC 2002](/WCCC_2002 "WCCC 2002"), [WCCC 2003](/WCCC_2003 "WCCC 2003"), [WCCC 2004](/WCCC_2004 "WCCC 2004") and the [WCCC 2006](/WCCC_2006 "WCCC 2006"). SOS played most [IPCCCs](/IPCCC "IPCCC"), and also competed at [International CSVN Tournaments](/International_CSVN_Tournament "International CSVN Tournament").

# Descriptions

[[6]](#cite_note-6)

## 1995

```
SOS is a conventional chess program. It uses depth first minimax tree search with quiescence search, alpha-beta enhancement, minimal window search and null-move pruning. To improve the search efficiency, the history heuristic and a transpositional table is used. The search is extended to deeper plies on those move sequences which have a high probability of being part of the principal variation. For SOS, those sequences are recaptures and check evasions. Leaf node evaluation considers only material, piece placement and pawn structure and only about 10% of the CPU time is spent on this (not including the quiescence search which is capture only, but extends on "losing" captures which are checks and on checking sequences). The evaluation parameters are dynamic and continuously updated during tree search. SOS's weakest part is probably endgame knowledge. SOS actively plays a wide range of openings, but most of those lines are not very deep. With autoplay games against itself, the opening book is tuned to favor those lines which harmonize with SOS's style of play.
```

## 1999

```
SOS is an amateur program which was started in 1993 and has since then competed in a number of tournaments. The newest version runs on multiprocessor systems with a parallelized version of mtd(f) as its minimax search algorithm. SOS used to be a relatively fast searcher and relied on outsearching the opponent. This has changed now and more knowledge and special cases have been implemented which slow it down. Little effort is spent on the opening book. It plays a very broad range of openings. However it learns to avoid unsuccessful lines and tries not to repeat lost games. It uses publicly available endgame databases.
```

# Forum Posts

- [New Winboard engine, SOS by Rudolf Huber, Germany !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30441) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), 27 October 1999
- [Chess knowledge (eg: SOS)](https://www.stmintz.com/ccc/index.php?id=103948) by ujecrh, [CCC](/CCC "CCC"), March 30, 2000
- [Testing SOS (Chessbase engine) = Extremely strong!!](https://www.stmintz.com/ccc/index.php?id=114918) by Tomas Casanovas Martinez, [CCC](/CCC "CCC"), June 18, 2000
- [Re: Question about SOS](https://www.stmintz.com/ccc/index.php?id=115077) by [Andrew Williams](/Andrew_Williams "Andrew Williams"), [CCC](/CCC "CCC"), June 19, 2000
- [SSDF(Crafty 17.07 - SOS)AMD K6-2 450, 1-5.](https://www.stmintz.com/ccc/index.php?id=125163) by [Tony Hedlund](/Tony_Hedlund "Tony Hedlund"), [CCC](/CCC "CCC"), August 19, 2000
- [SOS is amateur WMCC 2000 with 5.5 point out of 9](https://www.stmintz.com/ccc/index.php?id=126539) by Jorge Pichard, [CCC](/CCC "CCC"), August 26, 2000
- [Goliath Light, Gromit, Patzer, SOS, etc. commercially sold](https://www.stmintz.com/ccc/index.php?id=186009) by [Theo van der Storm](/Theo_van_der_Storm "Theo van der Storm"), [CCC](/CCC "CCC"), August 28, 2001
- [Stalemate trap(SOS-Delfi)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35352) by [George Lyapko](/George_Lyapko "George Lyapko"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 18, 2001 » [Stalemate](/Stalemate "Stalemate"), [Test-Positions](/Test-Positions "Test-Positions"), [Delfi](/Delfi "Delfi")
- [The new UCI / WB GUI Arena is available with UCI Arena SOS ..](https://www.stmintz.com/ccc/index.php?id=208295) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), January 18, 2002
- [After ELChinito 3.25 on Christmas now SOS.4 on New Years day!](https://www.stmintz.com/ccc/index.php?id=339663) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), January 01, 2004 » [Chinito](/Chinito "Chinito")

# External Links

## Chess Engine

- [SOS' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=21)
- [Arena Chess GUI 3.0 - SOS](https://web.archive.org/web/20120106001947/http://www.playwitharena.com/?Partner_Chess_Engines:SOS%26nbsp%3B) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Interview with SOS programmer Rudolf Huber in German language!](https://web.archive.org/web/20120106031235/http://www.playwitharena.com/?Newsticker:Archive_9) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Arena Chess GUI 3.0](/Arena "Arena") - Archive 9, 132, May 10, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Young Talents, Teil 2](http://scleinzell.schachvereine.de/p_spielprogramme/youngtal_b.shtml) by [Peter Schreiner](/Peter_Schreiner "Peter Schreiner"), Mai 2000, hosted by [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml) (German)

## Misc

- [Buchholz system - SOS: Sum of Opponent Scores from Wikipedia](https://en.wikipedia.org/wiki/Buchholz_system)
- [SOS - Wiktionary](https://en.wiktionary.org/wiki/SOS)
- [SOS from Wikipedia](https://en.wikipedia.org/wiki/SOS) (· · · — — — · · ·)
- [SOS (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/SOS_%28disambiguation%29)
- [Apple SOS from Wikipedia](https://en.wikipedia.org/wiki/Apple_SOS)
- [SOS (game) from Wikipedia](https://en.wikipedia.org/wiki/SOS_%28game%29)
- [Wes Montgomery](/Category:Wes_Montgomery "Category:Wes Montgomery") - S.O.S. (take 3), [Full House](https://en.wikipedia.org/wiki/Full_House_(Wes_Montgomery_album)), recorded at [Tsubo](https://en.wikipedia.org/wiki/The_Jabberwock_(club)), [Berkeley, California](https://en.wikipedia.org/wiki/Berkeley,_California), June 25, 1962, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   feat. [Johnny Griffin](https://en.wikipedia.org/wiki/Johnny_Griffin), [Wynton Kelly](https://en.wikipedia.org/wiki/Wynton_Kelly), [Paul Chambers](https://en.wikipedia.org/wiki/Paul_Chambers), [Jimmy Cobb](https://en.wikipedia.org/wiki/Jimmy_Cobb)

# References

1. [↑](#cite_ref-1) [Silicon on sapphire from Wikipedia.de](http://de.wikipedia.org/wiki/Silicon_on_Sapphire)
2. [↑](#cite_ref-2) [New Winboard engine, SOS by Rudolf Huber, Germany !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30441) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), 27 October 1999
3. [↑](#cite_ref-3) [The new UCI / WB GUI Arena is available with UCI Arena SOS ..](https://www.stmintz.com/ccc/index.php?id=208295) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), January 18, 2002
4. [↑](#cite_ref-4) [Arena Chess GUI 3.0 - Partner Chess Engines](https://web.archive.org/web/20120103164848/http://www.playwitharena.com/?Partner_Chess_Engines) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
5. [↑](#cite_ref-5) [Arena Chess GUI 3.0 - SOS](https://web.archive.org/web/20120106001947/http://www.playwitharena.com/?Partner_Chess_Engines:SOS%26nbsp%3B) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
6. [↑](#cite_ref-6) [SOS' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=21)

**[Up one level](/Engines "Engines")**