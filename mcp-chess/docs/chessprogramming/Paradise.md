# Paradise

Source: https://www.chessprogramming.org/Paradise

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Paradise**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Jan_Bruegel_d._%C3%84._003.jpg/330px-Jan_Bruegel_d._%C3%84._003.jpg)](/File:Jan_Bruegel_d._%C3%84._003.jpg)

Paradise by [Jan Brueghel the Younger](https://en.wikipedia.org/wiki/Jan_Brueghel_the_Younger) [[1]](#cite_note-1)

**Paradise**, (**Pa**ttern **r**ecognition **a**pplied to **di**recting **se**arch)  
a [knowledge](/Knowledge "Knowledge") based chess program written at [Stanford University](/Stanford_University "Stanford University") in the late 70s by [David Wilkins](/David_Wilkins "David Wilkins"). Paradise was written in [MacLisp](https://en.wikipedia.org/wiki/Maclisp), a dialect of the [Lisp](/index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)") programming language developed at [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") within [Project MAC](https://en.wikipedia.org/wiki/MIT_Computer_Science_and_Artificial_Intelligence_Laboratory#Project_MAC). Paradise' goal was to find the [best move](/Best_Move "Best Move") in [tactically](/Tactics "Tactics") sharp [middlegame](/Middlegame "Middlegame") [positions](/Chess_Position "Chess Position") from the [game](/Chess_Game "Chess Game") of chess masters.

# Pattern and Plans

Like human players, the program had a large number of stored "patterns", and analyzing a position involved matching these patterns to suggest [plans](/Planning "Planning") for attack or defense. By communicating plans down the [tree](/Search_Tree "Search Tree"), the analysis was verified and possibly corrected by a small [search](/Search "Search") of the game tree (tens of positions) inluding specialized causality facility and [quiescence search](/Quiescence_Search "Quiescence Search") [[2]](#cite_note-2). There were production rules to produce plans, implementing such concepts as [checkmate](/Checkmate "Checkmate"), [fork](/Double_Attack "Double Attack"), [skewer](/Skewer "Skewer"), and [trapping](/Trapped_Pieces "Trapped Pieces") the piece, etc..

A plan generator produced tactical plans in a Plan Language. The program is capable of finding very deep [combinations](/Combination "Combination") because no limit is placed on its [search depth](/Depth "Depth"). It searches for moves as long as a plan is continuing to work [[3]](#cite_note-3).

# Win at Chess

While Paradise was able to solve most of 92 positions picked from the first 100 from [Win at Chess](/Win_at_Chess "Win at Chess"), with averaged three minutes thirty-three seconds for each solved position on a [PDP-10](/PDP-10 "PDP-10") [[4]](#cite_note-4), it was not able to play a complete reasonable game of chess due not further implemented knowledge employable in [strategic](/Strategy "Strategy"), none-tactical positions, especially during the [endgame](/Endgame "Endgame"). Controlling the search by [recognizers](/Pattern_Recognition "Pattern Recognition"), i.e. the amount to [extend](/Extensions "Extensions") or to [reduce](/Reductions "Reductions") if a move is accordant to a plan or not is still hot topic.

# See also

- [CAPS](/CAPS "CAPS")
- [Eden](/Eden "Eden")
- [Knowledge](/Knowledge "Knowledge")
- [Pattern Recognition](/Pattern_Recognition "Pattern Recognition")
- [Planner](/Planner "Planner")
- [Planning](/Planning "Planning")
- [Symbolic](/Symbolic "Symbolic")

# Publications

[[5]](#cite_note-5)

- [David Wilkins](/David_Wilkins "David Wilkins") (**1979**). *Using Patterns and Plans to Solve Problems and Control Search*. Ph.D. thesis, Computer Science Dept, [Stanford University](/Stanford_University "Stanford University"), AI Lab Memo AIM-329
- [David Wilkins](/David_Wilkins "David Wilkins") (**1980**). *Using patterns and plans in chess*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 14, reprinted (**1988**) in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
- [David Wilkins](/David_Wilkins "David Wilkins") (**1982**). *Using Knowledge to Control Tree Searching*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 18
- [David Wilkins](/David_Wilkins "David Wilkins") (**1983**). *Using chess knowledge to reduce search*. [Chess Skill in Man and Machine](/Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), Ch. 10, 2nd edition
- [Tony Marsland](/Tony_Marsland "Tony Marsland") (**1987**). *[Computer Chess Methods](https://www.semanticscholar.org/paper/Computer-Chess-and-Search-Marsland/8f28b87e78e860d77d2f9173ddbfda7133a5b2d1).* Encyclopedia of Artificial Intelligence, John Wiley & sons, mentions Paradise on pp. 27
- [David Wilkins](/David_Wilkins "David Wilkins") (**1991**). *Working notes on Paradise chess patterns*. Technical Note 509, AI Center, SRI International, [pdf](http://www.ai.sri.com/pubs/files/465.pdf)
- [Jussi Tella](http://fi.wikipedia.org/wiki/Jussi_Tella) (**1997**). *[Planning in Games](http://www.cs.hut.fi/~sto/planning-seminaari/tella/planning-in-games.htm#22)*. Seminar on Knowledge Engineering, Fall 1997, [Helsinki University of Technology](https://en.wikipedia.org/wiki/Helsinki_University_of_Technology)
- [Eric B. Baum](/Eric_B._Baum "Eric B. Baum") (**2004**). *[What is Thought?](http://www.whatisthought.com/)* Bradford Book, Paradise mentioned at pp. 193
- [Tristan Caulfield](/index.php?title=Tristan_Caulfield&action=edit&redlink=1 "Tristan Caulfield (page does not exist)") (**2004**). *Acquiring and Using Knowledge in Computer Chess*. B.Sc. Computer Science, [University of Bath](https://en.wikipedia.org/wiki/University_of_Bath), [pdf](http://www.cs.bath.ac.uk/~mdv/courses/CM30082/projects.bho/2003-4/TristanCaulfieldDissertation.pdf), 4.2.2 PARADISE, pp. 12
- [Diego Rasskin-Gutman](/index.php?title=Diego_Rasskin-Gutman&action=edit&redlink=1 "Diego Rasskin-Gutman (page does not exist)") (**2009**). *[Chess Metaphors - Artificial Intelligence and the Human Mind](https://mitpress.mit.edu/books/chess-metaphors)*. translated by Deborah Klosky, [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), 5 Chess Metaphors: Searches and Heuristics, pp. 125, Paradise pp. 136

# Forum Posts

- [Wilkins' PARADISE etc.](https://groups.google.com/d/msg/rec.games.chess/LyMZ49kd9-o/S3JpgaRTeKUJ) by [Nicolai Czempin](/Nicolai_Czempin "Nicolai Czempin"), [rgc](/Computer_Chess_Forums "Computer Chess Forums"), November 11, 1989
- [PARADISE 2](https://www.stmintz.com/ccc/index.php?id=51) by Trefor Deane, [CCC](/CCC "CCC"), July 04, 1998
- [Paradise performance](https://www.stmintz.com/ccc/index.php?id=312384) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), August 22, 2003
- [Comparison: Paradise and Symbolic](https://www.stmintz.com/ccc/index.php?id=348861) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), February 13, 2004 » [Symbolic](/Symbolic "Symbolic")

# External Links

- [Paradise (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Paradise_%28disambiguation%29)
- [Paradise from Wikipedia](https://en.wikipedia.org/wiki/Paradise)
- [Paradise garden from Wikipedia](https://en.wikipedia.org/wiki/Paradise_garden)
- [Garden of Eden from Wikipedia](https://en.wikipedia.org/wiki/Garden_of_Eden)
- [Paradiso (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Paradiso)
- [Paradise Lost from Wikipedia](https://en.wikipedia.org/wiki/Paradise_Lost)
- [Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa") And [The Mothers Of Invention](https://en.wikipedia.org/wiki/The_Mothers_of_Invention) - [Dupree's Paradise](https://www.discogs.com/de/composition/1ce68c4b-dd99-4819-ba51-7d84a126248d-Duprees-Paradise), August 21, 1973 at Solliden, [Skansen](https://en.wikipedia.org/wiki/Skansen), [Stockholm](https://en.wikipedia.org/wiki/Stockholm), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa"), [Jean-Luc Ponty](/Category:Jean-Luc_Ponty "Category:Jean-Luc Ponty"), [George Duke](/Category:George_Duke "Category:George Duke"), [Tom Fowler](https://en.wikipedia.org/wiki/Tom_Fowler_%28musician%29), [Bruce Fowler](https://en.wikipedia.org/wiki/Bruce_Fowler), [Ruth Underwood](https://en.wikipedia.org/wiki/Ruth_Underwood), [Ian Underwood](https://en.wikipedia.org/wiki/Ian_Underwood), [Ralph Humphrey](http://wiki.killuglyradio.com/wiki/Ralph_Humphrey)

# References

1. [↑](#cite_ref-1) Paradise by [Jan Brueghel the Younger](https://en.wikipedia.org/wiki/Jan_Brueghel_the_Younger) (c. 1620). Oil on oak. [Gemäldegalerie, Berlin](https://en.wikipedia.org/wiki/Gem%C3%A4ldegalerie,_Berlin), [Paradise from Wikipedia](https://en.wikipedia.org/wiki/Paradise)
2. [↑](#cite_ref-2) [Comparison: Paradise and Symbolic](https://www.stmintz.com/ccc/index.php?id=348861) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), February 13, 2004
3. [↑](#cite_ref-3) [Tristan Caulfield](/index.php?title=Tristan_Caulfield&action=edit&redlink=1 "Tristan Caulfield (page does not exist)") (**2004**). *Acquiring and Using Knowledge in Computer Chess*. B.Sc. Computer Science, [University of Bath](https://en.wikipedia.org/wiki/University_of_Bath), [pdf](http://www.cs.bath.ac.uk/~mdv/courses/CM30082/projects.bho/2003-4/TristanCaulfieldDissertation.pdf), 4.2.2 PARADISE, pp. 12
4. [↑](#cite_ref-4) [Re: Paradise performance](https://www.stmintz.com/ccc/index.php?id=312389) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), August 22, 2003
5. [↑](#cite_ref-5) [Papers on Chess by David E. Wilkins](http://www.ai.sri.com/~wilkins/bib-chess.html)

**[Up one Level](/Engines "Engines")**