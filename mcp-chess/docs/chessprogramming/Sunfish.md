# Sunfish

Source: https://www.chessprogramming.org/Sunfish

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Sunfish**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Elassoma_sp.jpg/330px-Elassoma_sp.jpg)](/File:Elassoma_sp.jpg)

[Pygmy sunfish](https://en.wikipedia.org/wiki/Pygmy_sunfish) [[1]](#cite_note-1)

**Sunfish**,  
a simple [open source chess engine](/Category:Open_Source "Category:Open Source") under the [GPL](/Free_Software_Foundation#GPL "Free Software Foundation") written by [Thomas Dybdahl Ahle](/Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle") in [Python](/Python "Python") for didactic purposes, inspired by [Harm Geert Muller's](/Harm_Geert_Muller "Harm Geert Muller") [Micro-Max](/Micro-Max "Micro-Max") [[2]](#cite_note-2).
Without the code lines of the [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") and its simple [command line interface](/CLI "CLI"), it takes up just 111 lines of code. Besides its command line interface featuring a [Unicode chess symbol board](/2D_Graphics_Board#Unicode "2D Graphics Board"), Sunfish supports the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") to play with a [graphical interface](/GUI "GUI") like [XBoard](/XBoard "XBoard") or [PyChess](/PyChess "PyChess").

# Description

Sunfish applies MTD-bi, the binary search version of [MTD(f)](/MTD(f) "MTD(f)") [[3]](#cite_note-3),
also known as [NegaC\*](/NegaC* "NegaC*") as proposed by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") in 1990 [[4]](#cite_note-4) [[5]](#cite_note-5), which is based on [C\*](/NegaC* "NegaC*"), introduced by [Kevin Coplan](/Kevin_Coplan "Kevin Coplan") in 1981 at [Advances in Computer Chess 3](/Advances_in_Computer_Chess_3 "Advances in Computer Chess 3") [[6]](#cite_note-6).
MTD-bi is embedded inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework. Its [fail-soft](/Fail-Soft "Fail-Soft") [scout](/Scout "Scout") originally lacked the [quiescence search](/Quiescence_Search "Quiescence Search"), which made it blunder pretty badly in some positions [[7]](#cite_note-7), but a version of this was later added [[8]](#cite_note-8).
The rudimentary [evaluation](/Evaluation "Evaluation") considers [point values](/Point_Value "Point Value") and [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") - an aggregated [score](/Score "Score") is [incremental updated](/Incremental_Updates "Incremental Updates") during [make move](/Make_Move "Make Move").

# Etymology

Sunfish is named after the [Pygmy Sunfish](https://en.wikipedia.org/wiki/Pygmy_sunfish), which is among the very few fish to start with the letters 'Py', and refers other famous [fish engines](/Category:Fish "Category:Fish") such as [Stockfish](/Stockfish "Stockfish") and [Rybka](/Rybka "Rybka") [[9]](#cite_note-9) .

# See also

- [FastChess](/FastChess "FastChess")
- [PyChess](/PyChess "PyChess")

# Publications

- [Jonni Bidwell](https://www.techradar.com/author/jonni-bidwell) (**2016**). *Python: Sunfish chess engine*. [Linux Format](https://en.wikipedia.org/wiki/Linux_Format), [pdf](http://www.itu.dk/people/thdy/papers/sunfish.pdf)

# Postings

- [Sunfish – A 111 line Chess Engine in Python](https://www.reddit.com/r/programming/comments/1xmj1a/sunfish_a_111_line_chess_engine_in_python/) by [Thomas Dybdahl Ahle](/Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [reddit](https://en.wikipedia.org/wiki/Reddit), February 16, 2014
- [SUNFISH - a new chess engine written in Python !](http://www.talkchess.com/forum/viewtopic.php?t=51430) by Ruxy Sylwyka, [CCC](/CCC "CCC"), February 27, 2014
- [New version of Sunfish](http://www.talkchess.com/forum/viewtopic.php?t=61182) by [Thomas Dybdahl Ahle](/Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](/CCC "CCC"), August 20, 2016
- [Sunfish (Python Engine)](http://www.talkchess.com/forum/viewtopic.php?t=66216) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](/CCC "CCC"), January 02, 2018

# External Links

## Chess Engine

- [thomasahle/sunfish · GitHub](https://github.com/thomasahle/sunfish)

## Misc

- [Sunfish from Wikipedia](https://en.wikipedia.org/wiki/Sunfish)
- [Sunfish Lake (Ontario) from Wikipedia](https://en.wikipedia.org/wiki/Sunfish_Lake_%28Ontario%29)
- [Basking shark from Wikipedia](https://en.wikipedia.org/wiki/Basking_shark)
- [Pygmy sunfish from Wikipedia](https://en.wikipedia.org/wiki/Pygmy_sunfish)

# References

1. [↑](#cite_ref-1) [Pygmy sunfish](https://en.wikipedia.org/wiki/Pygmy_sunfish) (Elassoma sp.). [Drawing](https://digitalmedia.fws.gov/digital/collection/natdiglib/id/4499) by Duane Raver for the [United States Fish and Wildlife Service](https://en.wikipedia.org/wiki/United_States_Fish_and_Wildlife_Service), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Sunfish – A 111 line Chess Engine in Python](https://www.reddit.com/r/programming/comments/1xmj1a/sunfish_a_111_line_chess_engine_in_python/) by [Thomas Dybdahl Ahle](/Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [reddit](https://en.wikipedia.org/wiki/Reddit), February 16, 2014
3. [↑](#cite_ref-3) [Aske Plaat](/Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](/Wim_Pijls "Wim Pijls"), [Arie de Bruin](/Arie_de_Bruin "Arie de Bruin") (**1995**). *A New Paradigm for Minimax Search*. Technical Report EUR-CS-95-03, [arXiv:1404.1515](https://arxiv.org/abs/1404.1515)
4. [↑](#cite_ref-4) [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") (**1991**). *Experiments With the NegaC\* Search - An Alternative for Othello Endgame Search.* [Heuristic Programming in AI 2](/2nd_Computer_Olympiad#Workshop "2nd Computer Olympiad")
5. [↑](#cite_ref-5) [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") (**1992**). *The NegaC\* Search.* [ICCA Journal, Vol. 15, No. 1](/ICGA_Journal#15_1 "ICGA Journal")
6. [↑](#cite_ref-6) [Kevin Coplan](/Kevin_Coplan "Kevin Coplan") (**1982**). *A special-purpose machine for an improved search algorithm for deep chess combinations.* [Advances in Computer Chess 3](/Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
7. [↑](#cite_ref-7) [Re: SUNFISH - a new chess engine written in Python !](http://www.talkchess.com/forum/viewtopic.php?t=51430&start=7) by [Thomas Dybdahl Ahle](/Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](/CCC "CCC"), February 28, 2014
8. [↑](#cite_ref-8) [Re: SUNFISH - a new chess engine written in Python !](http://www.talkchess.com/forum/viewtopic.php?t=51430&start=20) by [Thomas Dybdahl Ahle](/Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](/CCC "CCC"), February 28, 2014
9. [↑](#cite_ref-9) [thomasahle/sunfish · GitHub](https://github.com/thomasahle/sunfish)

**[Up one level](/Engines "Engines")**