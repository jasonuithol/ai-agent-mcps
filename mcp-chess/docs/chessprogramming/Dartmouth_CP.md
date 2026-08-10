# Dartmouth CP

Source: https://www.chessprogramming.org/Dartmouth_CP

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Dartmouth CP**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Keggy_the_Keg.JPG/250px-Keggy_the_Keg.JPG)](/File:Keggy_the_Keg.JPG)

[Keggy the Keg](https://en.wikipedia.org/wiki/Keggy_the_Keg) [[1]](#cite_note-1)

**Dartmouth CP**,  
a chess program developed in the early 70s at [Dartmouth College](/Dartmouth_College "Dartmouth College") by a team lead by professor [Larry Harris](/Larry_Harris "Larry Harris"). Primary author was [Warren Montgomery](/Warren_Montgomery "Warren Montgomery") [[2]](#cite_note-2), supported by co-authors [Danny Kopec](/Danny_Kopec "Danny Kopec"), [Hal Terrie](/Hal_Terrie "Hal Terrie"), [David Levner](/index.php?title=David_Levner&action=edit&redlink=1 "David Levner (page does not exist)") and others [[3]](#cite_note-3). Dartmouth CP was written in [GCOS](https://en.wikipedia.org/wiki/General_Comprehensive_Operating_System) [assembly](/Assembly "Assembly"), the language for the [GE-635](/Honeywell_6000 "Honeywell 6000"), to run under the [Dartmouth Time Sharing System](https://en.wikipedia.org/wiki/Dartmouth_Time_Sharing_System). In his 1973 paper on [Bandwidth Search](/index.php?title=Bandwidth_Search&action=edit&redlink=1 "Bandwidth Search (page does not exist)") [[4]](#cite_note-4), which was applied successfully to chess and therefor likely to Dartmouth CP, [Larry Harris](/Larry_Harris "Larry Harris") acknowledged professor [Steve Garland](/index.php?title=Steve_Garland&action=edit&redlink=1 "Steve Garland (page does not exist)") and the undergraduates [Warren Montgomery](/Warren_Montgomery "Warren Montgomery"), [Dave Chenerow](/index.php?title=Dave_Chenerow&action=edit&redlink=1 "Dave Chenerow (page does not exist)"), [Dexter Kozen](/index.php?title=Dexter_Kozen&action=edit&redlink=1 "Dexter Kozen (page does not exist)"), and [Steve Poulsen](/index.php?title=Steve_Poulsen&action=edit&redlink=1 "Steve Poulsen (page does not exist)") for their work on that topic [[5]](#cite_note-5).

# Challenging Chess

Excerpt from [Danny Kopec's](/Danny_Kopec "Danny Kopec") *Recent developments in computer chess* [[6]](#cite_note-6):

```
Dartmouth's program was the first program to challenge Northwestern's ascendancy in the ACM tournaments. In the ACM U.S. Computer Chess Championship, held in Atlanta, Northwestern's program was lucky to draw against Dartmouth. It only did so because the latter had no repetition check. Particularly encouraging was the fact that in a game of more than 50 moves, Dartmouth was never in a losing position.
```

```
[Event "ACM 1973"]
[Site "Atlanta USA"]
[Date "1973.08.26"]
[Round "2"]
[White "Dartmouth CP"]
[Black "Chess 4.0"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 d6 6.Be3 Nxd4 7.Bxd4 e5 8.Be3 Be7 
9.Bb5+ Bd7 10.Qd3 O-O 11.O-O-O Ng4 12.Bxd7 Qxd7 13.Nd5 Bh4 14.f3 Nf2 15.Bxf2 Bxf2 
16.Rd2 Bc5 17.b4 Bd4 18.c3 Bb6 19.Nxb6 axb6 20.b5 Kh8 21.Qd5 Rfc8 22.Kb2 Rc5 
23.Qxd6 Rxb5+ 24.Ka1 Qc8 25.Qd3 Rba5 26.Rb1 Qc7 27.Rb4 Ra3 28.Rc4 Qe7 29.Rb4 Qf6 
30.Rb5 R3a4 31.Qd5 Qh4 32.Rxb6 R4a5 33.Qd6 Qe1+ 34.Rb1 Qh4 35.Qd7 b5 36.Qxf7 Qxh2 
37.Qd7 Qf4 38.Qd8+ Qf8 39.Qxf8+ Rxf8 40.Kb2 Rfa8 41.Ra1 R5a6 42.Rd5 Rg6 43.g4 Rf6
44.Rxb5 Rxf3 45.Rxe5 Rb8+ 46.Kc2 Rc8 47.Kb3 Rfxc3+ 48.Kb4 Rc2 49.Re7 Rb2+ 50.Ka3 
Rg2 51.e5 Rxg4 52.e6 Rg2 53.Ka4 Rb2 54.Ra7 h5 55.a3 Rc4+ 56.Ka5 Rc5+ 57.Ka4 g5 
58.e7 Rc4+ 59.Ka5 Rb8 60.Re1 Rc5+ 61.Ka4 Rcc8 62.Re5 Ra8 63.Rxa8 Rxa8+ 64.Kb5 Re8 
65.Rxg5 Rxe7 66.Rxh5+ Kg7 67.Kb6 Re6+ 68.Kb5 Re7 69.Kb6 Re6+ 70.Kb5 Re7 71.Kb6 
1/2-1/2
```

# Evaluation

[Danny Kopec](/Danny_Kopec "Danny Kopec") in *Recent developments in computer chess* on the [Evaluation](/Evaluation "Evaluation") of Dartmouth CP [[7]](#cite_note-7):

```
The program is divided into two major evaluation functions, ĥ and đ. ĥ is concerned with the "soft", positional features of a given board position, while đ is concerned with the "hard" tactical features of a position. The specific chess concepts which comprise đ and ĥ are called "Detectors". A set of related detectors are assigned various values (weights) and are put into a table. ĥ includes tables such as Centre Control, Piece Mobility, Pawn Structure, King Safety, etc., while đ includes tables such as Pins, Forks, Discovered Attacks, Levers. The program is also divided into modules (Opening, Middle Game, and Endings) which allow greater flexibility in the assignment of weights. For example, in the opening, Piece-development, Centre control and King safety are stressed. A persistent problem which many programs still have is the too early development of the queen, because of its tremendous square control, mobility, and ability to produce threats. By assigning a value of -300 (where 100 = pawn) to every minor piece (B or N) still on the back rank, piece development is given prominence, since the program tries to get rid of these initial negative values. Other examples of tables which employ modular flexibility are Occupation of the Centre, and Rook on 7th. Greater weights are assigned to these in the middle game and ending than in the opening, to avoid moving the same pieces too often, before others have moved at all.
```

```
An idea which was never fully implemented was that of an "Attack-Defence Ratio". This is a measure of the difference between the sum of the forces attacking the quarter of the board where the enemy king is located and the sum of those forces which defend the same squares. If this difference in force is greater than a certain threshold value, an "alarm" is set off which results in a higher đ value and an increase in the depth of search. In this manner, long sacrificial variations are more carefully investigated. A benchmark of sacrificial positions would be a good test for its effectiveness.
```

```
Dartmouth's most "informed" table was the one on pawn formations, called "PFORM". Among its standard detectors were Isolated Pawns, Backward Pawns, Doubled Pawns, Passed Pawns, and Duos. Detectors such as Chains, Mini-chains, Shielded Backward Pawns, Potential Passed Pawns, and the table, "Levers", were among the more esoteric concepts which were added later. Many of these definitions were taken directly from Hans Kmoch's classic work Pawn Power [8]. The concept, Levers, using a modified definition of my own "pawn mover wich improve our formation and hurt our opponent's" - proved useful in the recognition of critical pawn moves. In addition, the levers concept helps to guide the placement of pieces especially in the opening and middle game. It could also help toward plan formation. Some further pawn formational concepts from Pawn Power which were never programmed were Outpost and Weak Square Complexes. The Dartmouth program is probably, in theory, capable of more sophisticated pawn formational evaluations than any other program; however the implementation is rudimentary. The program had at one time approximately 50 detectors in various tables and many others were planned.
```

# See also

- [Dart](/Dart "Dart")

# Publications

- [Larry Harris](/Larry_Harris "Larry Harris") (**1973**). *The bandwidth heuristic search*. [3. IJCAI 1973](/Conferences#IJCAI1973 "Conferences"), [pdf](http://www.ijcai.org/Past%20Proceedings/IJCAI-73/PDF/004.pdf)
- [Larry Harris](/Larry_Harris "Larry Harris") (**1974**). *Heuristic Search under Conditions of Error*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 5, No. 3, also as (**1977**). *The heuristic search: An alternative to the alpha-beta minimax procedure.* [Chess Skill in Man and Machine](/Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
- [Larry Harris](/Larry_Harris "Larry Harris") (**1975**). *The Heuristic Search And The Game Of Chess - A Study Of Quiescence, Sacrifices, And Plan Oriented Play*. [4. IJCAI 1975](/Conferences#IJCAI1975 "Conferences"), reprinted (**1988**) in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
- [Larry Harris](/Larry_Harris "Larry Harris") (**1977**). *The heuristic search: An alternative to the alpha-beta minimax procedure.* [Chess Skill in Man and Machine](/Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
- [Danny Kopec](/Danny_Kopec "Danny Kopec") (**1977**). *Recent developments in computer chess*. Firbush News 7 Edinburgh: Machine Intelligence Research Unit, [University of Edinburgh](/University_of_Edinburgh "University of Edinburgh") (ed. [Donald Michie](/Donald_Michie "Donald Michie")), [pdf](http://www.sci.brooklyn.cuny.edu/~kopec/Publications/Publications/O_45_C.pdf)

# External Links

- [The Dartmouth Computing Timeline - The 1970s - 1973 - Chess Program in Tournament](https://www.dartmouth.edu/its-tools/archive/history/timeline/1970s.html#1973)

# References

1. [↑](#cite_ref-1) [Dartmouth College from Wikipedia](https://en.wikipedia.org/wiki/Dartmouth_College)
2. [↑](#cite_ref-2) [The Dartmouth Computing Timeline - The 1970s - 1973 - Chess Program in Tournament](https://www.dartmouth.edu/its-tools/archive/history/timeline/1970s.html#1973)
3. [↑](#cite_ref-3) [Danny Kopec](/Danny_Kopec "Danny Kopec") (**1977**). *Recent developments in computer chess*. Firbush News 7 Edinburgh: Machine Intelligence Research Unit, [University of Edinburgh](/University_of_Edinburgh "University of Edinburgh") (ed. [Donald Michie](/Donald_Michie "Donald Michie")), [pdf](http://www.sci.brooklyn.cuny.edu/~kopec/Publications/Publications/O_45_C.pdf) - Work at Dartmouth College
4. [↑](#cite_ref-4) [Bandwidth search | Variants of A\*](http://theory.stanford.edu/~amitp/GameProgramming/Variations.html#bandwidth-search) from [Amit’s A\* Page](http://theory.stanford.edu/~amitp/GameProgramming/)
5. [↑](#cite_ref-5) [Larry Harris](/Larry_Harris "Larry Harris") (**1973**). *The bandwidth heuristic search*. [3. IJCAI 1973](/Conferences#IJCAI1973 "Conferences"), [pdf](http://www.ijcai.org/Past%20Proceedings/IJCAI-73/PDF/004.pdf)
6. [↑](#cite_ref-6) [Danny Kopec](/Danny_Kopec "Danny Kopec") (**1977**). *Recent developments in computer chess*. Firbush News 7 Edinburgh: Machine Intelligence Research Unit, [University of Edinburgh](/University_of_Edinburgh "University of Edinburgh") (ed. [Donald Michie](/Donald_Michie "Donald Michie")), [pdf](http://www.sci.brooklyn.cuny.edu/~kopec/Publications/Publications/O_45_C.pdf)
7. [↑](#cite_ref-7) [Danny Kopec](/Danny_Kopec "Danny Kopec") (**1977**). *Recent developments in computer chess*. Firbush News 7 Edinburgh: Machine Intelligence Research Unit, [University of Edinburgh](/University_of_Edinburgh "University of Edinburgh") (ed. [Donald Michie](/Donald_Michie "Donald Michie")), [pdf](http://www.sci.brooklyn.cuny.edu/~kopec/Publications/Publications/O_45_C.pdf)
8. [↑](#cite_ref-8) [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6, [Google Books](http://books.google.com/books?id=FT7hpAiec3EC&dq=Pawn+Power+in+Chess&pg=PP1&ots=q_yCx72Ms_&sig=sKrQzXouaweUYbwCjfTcaplUF4U&hl=de&sa=X&oi=book_result&resnum=1&ct=result#PPA1,M1), [amazon](http://www.amazon.com/Pawn-Power-Chess-Hans-Kmoch/dp/0486264866)

**[Up one Level](/Engines "Engines")**