# Fidelity

Source: https://www.chessprogramming.org/Fidelity

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Fidelity**

[![](/images/thumb/d/d2/Fidelity-chess-machine.wccc.edmonton.1989.102645423.newborn.jpg/300px-Fidelity-chess-machine.wccc.edmonton.1989.102645423.newborn.jpg)](http://www.computerhistory.org/chess/full_record.php?iid=stl-431f4cc194e20)

Fidelity X at [WCCC 1989](/WCCC_1989 "WCCC 1989") [[1]](#cite_note-1)

**Fidelity**,  
was a family of [dedicated Chess Computers](/Dedicated_Chess_Computers "Dedicated Chess Computers"), manufactured by [Sidney Samole's](/Sidney_Samole "Sidney Samole") company [Fidelity Electronics](/Fidelity_Electronics "Fidelity Electronics") [[2]](#cite_note-2). The early programs were written by [Ron Nelson](/Ron_Nelson "Ron Nelson"), since 1980/1981 most programs were based on [Dan](/Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen's](/Kathe_Spracklen "Kathe Spracklen") [Sargon](/Sargon "Sargon") programs. Fidelity chess computers with Spracklen programs, the commercial available [Chess Challenger](/Chess_Challenger "Chess Challenger"), [Elite](/Elite "Elite"), [Sensory](/Sensory_9 "Sensory 9"), [Elegance](/Elegance "Elegance"), [Private Line](/Private_Line "Private Line") and the experimental versions coined *Fidelity X* as covered on this page, participated in many tournaments with great success and won many world as well as national titles.

# Fidelity X

## 1981-1984

Fidelity X, which won the [WMCCC 1981](/WMCCC_1981 "WMCCC 1981"), was later market as [Fidelity Elite Champion](/Elite "Elite") [[3]](#cite_note-3) [[4]](#cite_note-4) . It was based on a [6502](/6502 "6502") [Sargon](/Sargon "Sargon") program by [Dan](/Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen's](/Kathe_Spracklen "Kathe Spracklen"). Same or slightly improved hardware played the [ACM 1982](/ACM_1982 "ACM 1982"), the [WCCC 1983](/WCCC_1983 "WCCC 1983") and [ACM 1984](/ACM_1984 "ACM 1984").

## 1986

In 1986, at the [17th ACM North American Computer Chess Championship](/ACM_1986 "ACM 1986") in [Dallas](https://en.wikipedia.org/wiki/Dallas), Fidelity showed up with two experimental machines. Fidelity Experimental with [Danny Kopec](/Danny_Kopec "Danny Kopec") as [Book author](/Category:Opening_Book_Author "Category:Opening Book Author") had one [68020](/68020 "68020") CPU, where three models also played the [WMCCC 1986](/WMCCC_1986 "WMCCC 1986") some streets farther with compatible time schedule. [Chess Challenger X](/Chess_Challenger "Chess Challenger") was a parallel system with a [Z80](/Z80 "Z80") controller, and 16 or more [68000](/68000 "68000") CPUs, co-authored by [Ron Nelson](/Ron_Nelson "Ron Nelson"), with a Kopec book as well.

## Description 1989

Fidelity X, alias *Fidelity/Motorola Challenger*, which played the [WCCC 1989](/WCCC_1989 "WCCC 1989") was a 32 bit program, targeting [Motorola's](/index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") [68030](/68030 "68030") processor [[5]](#cite_note-5). Description from the WCCC booklet [[6]](#cite_note-6) :

The Fidelity/Motorola Challenger relies for its strength on a combination of state-of-the-art microcomputer hardware and a chess algorithm that has undergone continuous full-time development for over ten years.

The central feature of the hardware is a [Motorola](/index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") [68030](/68030 "68030") processor, hand-selected by Motorola engineers to run at the fastest possible clock speed. The exact speed will not be known until just prior to tournament time. The system is completed by 32K of program [ROM](/Memory#ROM "Memory"), 64K of [opening book](/Opening_Book "Opening Book") ROM, 16K of program [RAM](/Memory#RAM "Memory"), one megabyte of dynamic RAM for [transposition tables](/Transposition_Table "Transposition Table"), and a special 16K of non-volatile RAM that supports the [learning](/Learning "Learning") feature.

The learning feature is just one facet of a multi-faceted chess algorithm. The program is basically [brute force](/Brute-Force "Brute-Force") in origin with evolution to incorporate extensive positional analysis and [selective extensions](/Extensions "Extensions") during the [quiescence search](/Quiescence_Search "Quiescence Search"). The positional analysis incorporates extensive heuristics for [king safety](/King_Safety "King Safety") and [pawn structure](/Pawn_Structure "Pawn Structure"). Numerous end-game specific routines are incorporated, icluding [mate with bishop and knight](/KBNK_Endgame "KBNK Endgame"), complete evaluation of [king and pawn vs. king](/KPK "KPK"), probably outcome of a [pawn race](/Pawn_Race "Pawn Race"), [square of the pawn](/Rule_of_the_Square "Rule of the Square"), [bishop and rook pawn of the opposite color](/Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn"), the [Philidor](/index.php?title=Philidor_Position&action=edit&redlink=1 "Philidor Position (page does not exist)") and [Lucena positions](/index.php?title=Lucena_Position&action=edit&redlink=1 "Lucena Position (page does not exist)") and others. Dynamic recognition of minimum mating material, [fifty move rule](/Fifty-move_Rule "Fifty-move Rule"), and [repetition of position](/Repetitions#RepetitionOfPositions "Repetitions") assist in forestalling heartbreaking draws in otherwise won positions. The search algorithm uses a [depth first](/Depth-First "Depth-First"), [alpha-beta](/Alpha-Beta "Alpha-Beta") search with the [zero width window](/Null_Window "Null Window") technique ([PVS](/Principal_Variation_Search "Principal Variation Search")). The search proceeds [iteratively](/Iterative_Deepening "Iterative Deepening") with a quiescence search incorporating [captures](/Captures "Captures") and certain threats appended beyond the [nominal depth](/Depth "Depth"). The program will not perform an [evaluation](/Evaluation "Evaluation") on a position where either king is [in check](/Check "Check"). The check must first be resolved by showing the existence of an escape move or [mate](/Checkmate "Checkmate"). Iterations are finally halted under the direction of a [time control algorithm](/Time_Management "Time Management") which is dynamically incorporated for up to 40 moves in the root position. Two [killer moves](/Killer_Move "Killer Move") are stored at every [ply](/Ply "Ply"). The program performs a preliminary sort on the ply above the quiescence search. The search is supported by extensive [transposition tables](/Transposition_Table "Transposition Table") incorporating random numbers selected using [BCH theory](/BCH_Hashing "BCH Hashing").

# See also

- [Book Issues in Cray Blitz - Fidelity X @ ACM 1984](/Boris_Baczynskyj#CrayBlitzFidelity "Boris Baczynskyj")
- [Fidelity Electronics](/Fidelity_Electronics "Fidelity Electronics")
- [Excalibur Electronics](/Excalibur_Electronics "Excalibur Electronics")
- [Hegener & Glaser](/Hegener_%26_Glaser "Hegener & Glaser")
- [Sidney Samole](/Sidney_Samole "Sidney Samole")
- [Sargon](/Sargon "Sargon")
- [Dan Spracklen](/Dan_Spracklen "Dan Spracklen")
- [Kathe Spracklen](/Kathe_Spracklen "Kathe Spracklen")

# Fidelity Computers

- [Chess Challenger](/Chess_Challenger "Chess Challenger")
- [Elegance](/Elegance "Elegance")
- [Elite](/Elite "Elite")
- [Excel](/Excel "Excel")
- [Excellence](/Excellence "Excellence")
- Fidelity
- [Fidelity Phantom](/Fidelity_Phantom "Fidelity Phantom")
- [Par Excellence](/Par_Excellence "Par Excellence")
- [Private Line](/Private_Line "Private Line")

# External Links

## Chess Computers

- [Fidelity's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=312)
- [Fidelity | Photo collection](http://www.flickr.com/photos/10261668@N05/sets/72157600922170604/) by [Chewbanta](/Steve_Blincoe "Steve Blincoe")

## Misc

- [Fidelity from Wikipedia](https://en.wikipedia.org/wiki/Fidelity)
- [Fidelity (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Fidelity_(disambiguation))

# References

1. [↑](#cite_ref-1) [Fidelity X chess computer at the 6th World Chess Championship in Edmonton, Alberta](http://www.computerhistory.org/chess/full_record.php?iid=stl-431f4cc194e20), [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), Photo courtesy: [Monty Newborn](/Monroe_Newborn "Monroe Newborn")
2. [↑](#cite_ref-2) [Fidelity Electronics](http://www.ismenio.com/fidelity.html) from [chesscomputers.org](http://www.ismenio.com/chess_computers.html)
3. [↑](#cite_ref-3) [Fidelity Elite Champion Sensory Chess Challenger](http://www.schach-computer.info/wiki/index.php/Fidelity_CC_Elite_Champion) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
4. [↑](#cite_ref-4) [Fidelity Elite Champion](http://www.chesscomputeruk.com/html/fidelity_elite_champion.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
5. [↑](#cite_ref-5) [Fidelity](https://www.game-ai-forum.org/icga-tournaments/program.php?id=312)
6. [↑](#cite_ref-6) [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](/Peter_Jennings "Peter Jennings"), from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)

**[Up one level](/Engines "Engines")**