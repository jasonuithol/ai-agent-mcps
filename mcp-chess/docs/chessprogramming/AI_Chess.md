# AI Chess

Source: https://www.chessprogramming.org/AI_Chess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* AI Chess**

**AI Chess**, (A.I. Chess)  
a chess program by [Marty Hirsch](/Marty_Hirsch "Marty Hirsch") and predecessor of [MChess](/MChess "MChess"). AI Chess was written in [8086](/8086 "8086") [assembly language](/Assembly "Assembly") to ran on an [IBM PC](/IBM_PC "IBM PC") under [DOS](/MS-DOS "MS-DOS") [[1]](#cite_note-1). It played the [ACM 1988](/ACM_1988 "ACM 1988") in [Orlando](https://en.wikipedia.org/wiki/Orlando%2C_Florida), the [WCCC 1989](/WCCC_1989 "WCCC 1989") in [Edmonton](https://en.wikipedia.org/wiki/Edmonton) and the [WMCCC 1989](/WMCCC_1989 "WMCCC 1989") in [Portorož](https://en.wikipedia.org/wiki/Portoro%C5%BE) [[2]](#cite_note-2).

# Description

given in the [WCCC 1989](/WCCC_1989 "WCCC 1989") booklet [[3]](#cite_note-3) :

```
A.I. Chess uses a fairly complicated algorithm combining full-width search, selective search, and a "layered" quiescence search which behaves differently at different levels in the search tree. The program performs an iterative full-width search using a modified form of the Principal-Variation-Search (PVS) algorithm. On top of this, it does a combined selective/quiscence analysis. A.I. Chess has the unusual feature of sometimes re-searching a "quiscence node" with a full-width investigation.
```

```
The quiescence search incorporates a detailed "threat analysis" and therefore, the program spots may combinations long before a contrasting "brute force" approach would find them. The gain (from needing less full-width plies) seems to exceed the loss in speed by a significant amount.
```

```
Position evaluation starts by considering if the side to move is threatened with pawn promotion, check, or double attack, or has trapped, pinned, or skewered pieces. Penalties similar to swap-off scores are imposed if the position is too deep to merit a re-search. Scores are then added for other tactical patterns, pressure on pieces and pawns, development, King safety, passed pawns, pawn structure, outposts, and mobility.
```

```
Some types of endgame positions are scored differently, by pattern recognition processing. The program is alert to simplifications, and to tactics involving passed pawns.
```

# See also

- [MChess](/MChess "MChess")

# External Links

- [AI Chess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=352)

# References

1. [↑](#cite_ref-1) [Monty Newborn](/Monroe_Newborn "Monroe Newborn"), [Danny Kopec](/Danny_Kopec "Danny Kopec") (**1989**). *Results of The Nineteenth ACM North American Computer Chess Championship*. [Communications of the ACM](/ACM#Communications "ACM"), Vol. 32, No. 10, [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_23_C.pdf)
2. [↑](#cite_ref-2) [AI Chess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=352)
3. [↑](#cite_ref-3) [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](/Peter_Jennings "Peter Jennings"), from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)

**[Up one level](/Engines "Engines")**