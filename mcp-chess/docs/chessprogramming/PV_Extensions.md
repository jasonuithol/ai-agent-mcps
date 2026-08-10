# PV Extensions

Source: https://www.chessprogramming.org/PV_Extensions

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Extensions](/Extensions "Extensions") \* PV Extensions**

**PV Extensions**, (PVS Extensions)
a technique to extend along the [principal variation](/Principal_Variation "Principal Variation") (PV) to achieve higher [search depths](/Depth "Depth") in the critical part of the [tree](/Search_Tree "Search Tree"). In [Rebel](/Rebel "Rebel"), [Ed Schröder](/Ed_Schroder "Ed Schroder") incremented a counter each time two consecutive [PV-moves](/PV-Move "PV-Move") were retrieved from the [transposition table](/Transposition_Table "Transposition Table"), to extend by one [ply](/Ply "Ply") each time the counter is divisible by four [[1]](#cite_note-1). Influenced by observing the principal variations of [Junior](/Junior "Junior") during the [Kasparov versus Deep Junior 2003](/Kasparov_versus_Deep_Junior_2003 "Kasparov versus Deep Junior 2003") match, [David Levy](/David_Levy "David Levy") proposed multiple extensions to treat the often early stable part of a PV as a single ply in 2003 [[2]](#cite_note-2). To determine the length of the PV, Levy expresses a threshold as a percentage of the total number of nodes searched with the common PV during the previous iteration of the [iterative deepening](/Iterative_Deepening "Iterative Deepening").

# See also

- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [SEX Algorithm](/SEX_Algorithm "SEX Algorithm")
- [Singular Extensions](/Singular_Extensions "Singular Extensions")

# Publications

- [David Levy](/David_Levy "David Levy") (**2003**). *The State of the Art in Man vs. “Machine” Chess*. [ICGA Journal](/ICGA_Journal "ICGA Journal"), Vol. 26, No. 1

# Forum Posts

- [PV verification heuristic](https://www.stmintz.com/ccc/index.php?id=74) by Peter Jacobi, [CCC](/CCC "CCC"), July 05, 1998
- [Re: PV verification heuristic](https://www.stmintz.com/ccc/index.php?id=21808) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), July 06, 1998
- [@Ed about PV extension](http://www.talkchess.com/forum/viewtopic.php?t=15216) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [CCC](/CCC "CCC"), July 19, 2007

# External Links

- [Extension Techniques in REBEL (PVS extensions)](http://www.top-5000.nl/authors/rebel/chess840.htm#PVS) from [Programmer Corner](http://www.top-5000.nl/authors/rebel/chess840.htm) by [Ed Schröder](/Ed_Schroder "Ed Schroder") [[3]](#cite_note-3)

# References

1. [↑](#cite_ref-1) [Extension Techniques in REBEL (PVS extensions)](http://www.top-5000.nl/authors/rebel/chess840.htm#PVS) from [Programmer Corner](http://www.top-5000.nl/authors/rebel/chess840.htm) by [Ed Schröder](/Ed_Schroder "Ed Schroder")
2. [↑](#cite_ref-2) [David Levy](/David_Levy "David Levy") (**2003**). *The State of the Art in Man vs. “Machine” Chess*. [ICGA Journal](/ICGA_Journal "ICGA Journal"), Vol. 26, No. 1
3. [↑](#cite_ref-3) How Rebel Plays Chess as [pdf reprint](http://members.home.nl/matador/Inside%20Rebel.pdf)

**[Up one level](/Extensions "Extensions")**