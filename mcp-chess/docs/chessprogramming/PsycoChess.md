# PsycoChess

Source: https://www.chessprogramming.org/PsycoChess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* PsycoChess**

**PsycoChess**, (Psyco Chess)  
an [open source chess engine](/Category:Open_Source "Category:Open Source") by [Massimo Zizi](/index.php?title=Massimo_Zizi&action=edit&redlink=1 "Massimo Zizi (page does not exist)"), written in [Java](/Java "Java") and released in June 2004 under the [GPL](/Free_Software_Foundation#GPL "Free Software Foundation").
PsycoChess applies [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards"), and a 4 [ply](/Ply "Ply") fixed [depth](/Depth "Depth") [alpha-beta](/Alpha-Beta "Alpha-Beta") without [iterative deepening](/Iterative_Deepening "Iterative Deepening") and [quiescence](/Quiescence_Search "Quiescence Search").
A [transposition table](/Transposition_Table "Transposition Table") is used a the [root](/Root "Root") only. Instead of [negamax](/Negamax "Negamax") or indirect [recursion](/Recursion "Recursion") via max and min-routines, a boolean parameter is passed to the direct recursive search whether it is a max or min player
[[1]](#cite_note-1).
The rudimentary [Evaluation](/Evaluation "Evaluation") considers [material](/Material "Material"), and [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") and some [pawn structure](/Pawn_Structure "Pawn Structure") terms
[[2]](#cite_note-2).

# See also

- [Psycho](/Psycho "Psycho")
- [Psycho-Chess](/index.php?title=Psycho-Chess&action=edit&redlink=1 "Psycho-Chess (page does not exist)")

# Forum Posts

- [Java xboard/winboard chess engine psychochess](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48185) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 14, 2004
- [Does somebody have a win compatible compile of PsycoChess](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=723) by [Dr. Axel Schumacher](/index.php?title=Dr._Axel_Schumacher&action=edit&redlink=1 "Dr. Axel Schumacher (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 25, 2004
- [New engines: PsycoChess and Tarrasch Toy Engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50114) by [Ron Murawski](/Ron_Murawski "Ron Murawski"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 25, 2009

# External Links

## Chess Program

- [Psyco Chess - A GNU Java Chess Engine download | SourceForge.net](https://sourceforge.net/projects/psycochess/) (PsycoChess 1.38)

## Misc

- [Psyco - Wikipedia.it](https://it.wikipedia.org/wiki/Psyco)

:   [Psycho (1960 film) from Wikipedia](https://en.wikipedia.org/wiki/Psycho_%281960_film%29)

- [Psyco from Wikipedia](https://en.wikipedia.org/wiki/Psyco) ([Python](/Python "Python"))
- [Achim Zepezauer](/Category:Achim_Zepezauer "Category:Achim Zepezauer") - Psycow, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Psyco Chess - A GNU Java Chess Engine download | SourceForge.net](https://sourceforge.net/projects/psycochess/), PsycoChess.tar.gz/BestMove.java
2. [↑](#cite_ref-2) [Psyco Chess - A GNU Java Chess Engine download | SourceForge.net](https://sourceforge.net/projects/psycochess/), PsycoChess.tar.gz/Scacchiera.java

**[Up one level](/Engines "Engines")**