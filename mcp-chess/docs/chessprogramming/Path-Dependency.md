# Path-Dependency

Source: https://www.chessprogramming.org/Path-Dependency

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* Path-Dependency**

**Path-Dependency** describes a situation when the same [position](/Chess_Position "Chess Position") gets a different value depending on a sequence of [moves](/Moves "Moves") by which it has been reached. Whilst a few programs do this by design [[1]](#cite_note-1), within the standard [alpha-beta](/Alpha-Beta "Alpha-Beta") framework path-dependency is considered undesirable, if impossible to avoid.

# Typical Cases

- The position can be treated differently if there is a chance of [repetition](/Repetitions "Repetitions") or hitting into a [fifty-move rule](/Fifty-move_Rule "Fifty-move Rule").
- Different [move ordering](/Move_Ordering "Move Ordering") can cause different result (different moves causing a cutoff), when it comes from the [hash table](/Transposition_Table "Transposition Table") [[2]](#cite_note-2)
- Hf a program uses [search extensions](/Extensions "Extensions"), search depth may be different (i.e. 1. d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Nf3 vs 1.d4 Nf6 2.c4 e6 3.Nf3 Bb4+ 4.Nc3, where only the latter triggers a [check extension](/Check_Extensions "Check Extensions"))
- History-dependent heuristics, like some versions of [LMR](/index.php?title=Late_move_reductions&action=edit&redlink=1 "Late move reductions (page does not exist)") may prune different sub-trees.

# See also

- [Graph History Interaction](/Graph_History_Interaction "Graph History Interaction") (GHI)
- [Transposition](/Transposition "Transposition")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Repetitions](/Repetitions "Repetitions")
- [Fifty-move Rule](/Fifty-move_Rule "Fifty-move Rule")

# Forum Posts

## 2000 ...

- ["Don't trust draw score" <=Is it true?](https://www.stmintz.com/ccc/index.php?id=182927) by [Teerapong Tovirat](/Teerapong_Tovirat "Teerapong Tovirat"), [CCC](/CCC "CCC"), August 08, 2001 » [Repetitions](/Repetitions "Repetitions"), [Graph History Interaction](/Graph_History_Interaction "Graph History Interaction")

## 2005 ...

- [path dependent evaluation](http://www.open-aurec.com/wbforum/viewtopic.php?t=2320) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 20, 2005
- [Re: And a still unsolved test position](https://www.stmintz.com/ccc/index.php?id=430487) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), June 09, 2005 » [Movei](/Movei "Movei")
- [Semi-Path Dependent Hashing: a semi-useless idea](http://talkchess.com/forum/viewtopic.php?t=21343) by [Zach Wegner](/Zach_Wegner "Zach Wegner"), [CCC](/CCC "CCC"), May 24, 2008 » [Transposition Table](/Transposition_Table "Transposition Table")

## 2010 ...

- [Repetitions/50 moves and TT](http://www.talkchess.com/forum/viewtopic.php?t=40388) by [Sergei Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), September 13, 2011
- [Texel recipe to fix TT draws scores](http://www.talkchess.com/forum/viewtopic.php?t=44167) by [Marco Costalba](/Marco_Costalba "Marco Costalba"), [CCC](/CCC "CCC"), June 23, 2012 » [Texel](/Texel "Texel")

# External Links

- [Path dependence from Wikipedia](https://en.wikipedia.org/wiki/Path_dependence)

# References

1. [↑](#cite_ref-1) [Re: Methods to stably evaluate nodes?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=115849&t=13559) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), May 05, 2007
2. [↑](#cite_ref-2) [Tony Warnock](/Tony_Warnock "Tony Warnock"), [Burton Wendroff](/Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal](/ICGA_Journal "ICGA Journal"), Vol. 11, No. 1, pp. 10-13.

**[Up one Level](/Search "Search")**