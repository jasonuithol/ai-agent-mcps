# Moby

Source: https://www.chessprogramming.org/Moby

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Moby**

[![](/images/thumb/f/f7/Meiko_inside.jpg/300px-Meiko_inside.jpg)](http://www.computermuseum.org.uk/fixed_pages/meiko_computing_surface.html)

[Meiko Computing Surface](https://en.wikipedia.org/wiki/Meiko_Scientific#Computing_Surface)[[1]](#cite_note-1)

**Moby**,  
a [multiprocessor](https://en.wikipedia.org/wiki/Multiprocessing) chess program participating at the [WCCC 1989](/WCCC_1989 "WCCC 1989"), running on a large [Meiko Computing Surface](https://en.wikipedia.org/wiki/Meiko_Scientific#Computing_Surface), based on [Inmos](https://en.wikipedia.org/wiki/Inmos) [T800 Transputer](/Transputer "Transputer") chips [[2]](#cite_note-2), installed at [University of Edinburgh](/University_of_Edinburgh "University of Edinburgh") as part of the [Edinburgh Concurrent Supercomputer Project](https://en.wikipedia.org/wiki/Edinburgh_Concurrent_Supercomputer). Moby was a descendant of [Cyrus 68K](/Cyrus_68K "Cyrus 68K"), whose development begun by [Mark Taylor](/Mark_Taylor "Mark Taylor") and [David Levy](/David_Levy "David Levy") in 1985, the parallel implementation was done by [Greg Wilson](/Greg_Wilson "Greg Wilson").

# Authors

- [David Levy](/David_Levy "David Levy")
- [Mark Taylor](/Mark_Taylor "Mark Taylor")
- [Greg Wilson](/Greg_Wilson "Greg Wilson")

# Description

based on [WCCC 1989](/WCCC_1989 "WCCC 1989") booklet [[3]](#cite_note-3)

```
Moby was a conventional searcher, but distributed the search across the available processors in a homogeneous fashion, that is all processors are carrying out the same type of operations, rather than some processors doing deep scout searches while others do more complete searches guided by the information returned by the scouts. Load balancing is archived by processor overloading - each processor supports a hash table manager responsible for part of the global transposition table. One distinguished processor acts as system master, interacting with the user and handling file i/o when the opening books are consulted.
```

# Selected Games

[WCCC 1989](/WCCC_1989 "WCCC 1989"), round 1, Moby - [Deep Thought](/Deep_Thought "Deep Thought") [[4]](#cite_note-4)

```
[Event "WCCC 1989"]
[Site "Edmonton, Canada"]
[Date "1989.05.28"]
[Round "1"]
[White "Moby"]
[Black "Deep Thought"]
[Result "0-1"]

1.d4 d5 2.Nc3 Nf6 3.Bg5 Nbd7 4.Qd3 h6 5.Bh4 c6 6.Nf3 g6 7.h3 Bg7 8.g4 Qa5 9.a3 Nf8 
10.Qe3 h5 11.gxh5 Rxh5 12.O-O-O Bf5 13.Bg5 Ne4 14.Bf4 Ne6 15.Nxe4 Bxe4 16.Qb3 Nxf4 
17.Qxb7 Qd8 18.Qxc6+ Kf8 19.Qa6 Qc7 20.Rd2 Bh6 21.Kd1 Rb8 22.c3 Qxc3 23.Rg1 Nxh3 
24.Qxa7 Rxb2 25.Qa5 Rb1# 0-1
```

# External Links

## Chess Program

- [Moby's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=363)

## Misc

- [moby - Wiktionary](https://en.wiktionary.org/wiki/moby)
- [Moby (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Moby_(disambiguation))
- [Moby Dick (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Moby_Dick_(disambiguation))
- [Moby-Dick from Wikipedia](https://en.wikipedia.org/wiki/Moby-Dick)
- [Voeltzkowia mobydick from Wikipedia](https://en.wikipedia.org/wiki/Voeltzkowia_mobydick)
- [Moby Dick (Rhine) from Wikipedia](https://en.wikipedia.org/wiki/Moby_Dick_%28Rhine%29)
- [Led Zeppelin](/Category:Led_Zeppelin "Category:Led Zeppelin") - [Moby Dick](https://en.wikipedia.org/wiki/Moby_Dick_(instrumental)), Live at the [Royal Albert Hall](https://en.wikipedia.org/wiki/Royal_Albert_Hall) 1970, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Meiko Computing Surface CS1](http://www.computermuseum.org.uk/fixed_pages/meiko_computing_surface.html) from [The Jim Austin Computer Collection](http://www.computermuseum.org.uk/)
2. [↑](#cite_ref-2) [The Meiko Computing Surface](http://www.new-npac.org/projects/cdroms/cewes-1999-06-vol1/nhse/hpccsurvey/orgs/meiko/meiko.html#CS)
3. [↑](#cite_ref-3) [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](/Peter_Jennings "Peter Jennings"), from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)
4. [↑](#cite_ref-4) [Edmonton 1989 - Chess - Round 1 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=14&round=1&id=1)

**[Up one Level](/Engines "Engines")**