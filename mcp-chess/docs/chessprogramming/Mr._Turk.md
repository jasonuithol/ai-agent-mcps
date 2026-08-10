# Mr. Turk

Source: https://www.chessprogramming.org/Mr._Turk

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Mr. Turk**

[![](https://upload.wikimedia.org/wikipedia/commons/1/1d/TurkSColes.jpg)](/File:TurkSColes.jpg)

The Turk [[1]](#cite_note-1)

**Mr. Turk**,  
an early chess program by primary authors [Gary Boos](/Gary_Boos "Gary Boos") and [James Mundstock](/James_Mundstock "James Mundstock") at [University of Minnesota](/University_of_Minnesota "University of Minnesota"), written in [Fortran](/Fortran "Fortran") to run on a [CDC 6600](/CDC_6600 "CDC 6600"). Mr. Turk participated in the [ACM's Second North American Computer-Chess Championship](/ACM_1971 "ACM 1971") 1971. It did not use [alpha-beta](/Alpha-Beta "Alpha-Beta"), but a search based on a *Multipurpose, Theorem-Proving Heuristic Program* as described by [James R. Slagle](/James_R._Slagle "James R. Slagle") and [Philip Bursky](/Philip_Bursky "Philip Bursky") in 1968 [[2]](#cite_note-2) .

# Description

by [Gary Boos](/Gary_Boos "Gary Boos") from [Ben Mittman's](/Ben_Mittman "Ben Mittman") 1971 Panel [[3]](#cite_note-3) :

```
Since late 1967 James Mundstock, myself, and others, have been working on our chess program, Mr. Turk. Mr. Turk was developed at the University of Minnesota on a CDC 6600. At almost all times everyone working on the program was both a chess player and a reasonably good FORTRAN programmer. Our main goal has been to produce a program that could win as many chess games as possible. The methods used in striving for this goal have varied from group to group.
```

```
Based upon our chess experience (Mundstock is a class B player, and I am an experienced, class A player), we knew that to obtain a winning position, one normally has to outplay the opponent in both the opening and the middle game. Consequently, we concentrated our initial efforts on writing good evaluation routines for the opening and middlegame, plus producing routines that supplied legal moves, location of pinned pieces, which squares are attacked by which pieces, etc. The result was a program that would produce reasonable moves 80 to 90% of the time, with (in effect) a 1-ply level lookahead.
```

```
The next major task was to write a lookahead routine and incorporate it into the rest of the program. Existing lookahead routines were not impressive. They tended to have a vast number of limbs in their move tree, and very little evaluation was spent on the positions examined. An experienced human chess player selects variations with an efficiency at least 10 times greater than any pre-1970 program. Mundstock and I felt that any attempt to approach a master's thought process should help in shaping and improving the move tree. The most noticeable difference in previous lookahead routines and a master's analysis is that the master analyzes one and only one line at a time. He seems to try to insure that that line is the best for both sides, and he attempts to analyze it as deeply as his vision and time permit.
```

```
Mundstock noticed an article by Slagle and Bursky in the Journal of the ACM, that pointed toward an algorithm that seemed better than alpha-beta pruning. Based upon this article, and guided by Mundstock, I wrote a lookahead routine whose main theme is that the best line is analyzed until it is shown that it is no longer the best line.
```

```
This process eliminates many common problems that accompany a fixed depth search, one of which is the Ostrich Effect which existed in even Northwestern University's  Chess 3.0. Tests showed that in a small set of positions, Mr. Turk could find the main variation on the first try. We believe that the basic theme of our lookahead routine is better than alpha-beta pruning.
```

```
Full scale tests of the program revealed serious shortcomings. Mr. Turk had only a fixed width (5 moves) move tree, and when all of the top 5 moves were bad (often twice a game), the program was forced to play the best of those 5. That is to say, we had no fall-back routine; no panic button to push.
```

```
Other weaknesses were: a) the inability to include sacrificial moves in the move tree, b) little endgame capability, and c) only a small opening book. Nevertheless, we challenged five other programs to postal matches. Only Northwestern University was capable of playing. The match was started in late 1970, and Chess 3.2 is presently winning the two game match. Our team has been working on the above weaknesses since September 1970, and also performing a major overhaul on the existing code. We hope to be able to include tactical moves in the move tree, provide a fall-back algorithm, enlarge and improve our opening book and still keep the necessary storage at under 54k.
```

```
It is our opinion that existing chess programs have many weaknesses, and that their play is far too often superficial. Almost all programs find it very difficult to win an endgame if positional play is of the essence. Most programs have opening books, but I seriously doubt that any can handle transpositions. I have never seen a program sacrifice material unless either checkmate or a net win of material was within its view. Also (and this is probably the hardest task of all) no program has been able to develop a logical plan of play in a general position. With the aid of other chess players in Minnesota, we have developed a secret weapon for the Second ACM tournament, and will attempt to exploit one of these weaknesses.
```

```
The Second ACM tournament will be far stronger than the 1970 championship (how much stronger will be indicated by where Chess 3.5 finishes). The tournament will provide very interesting games, and the panel discussions between chess programmers from across the nation will bring forth new ideas. We must learn all the lessons we can, for next year, the Russians are coming.
```

# See also

- [Iron Fish](/Iron_Fish "Iron Fish")
- [Kempelen](/Kempelen "Kempelen")
- [The Baron](/The_Baron "The Baron")
- [The Turk](/The_Turk "The Turk")

# External Links

- [The Turk from Wikipedia](https://en.wikipedia.org/wiki/The_Turk), the historic fake chess-playing machine
- [Ein Türke in Paderborn](https://de.chessbase.com/post/ein-trke-in-paderborn) from [ChessBase Nachrichten](/ChessBase "ChessBase") (German)

# References

1. [↑](#cite_ref-1) [Gaughan's](https://en.wikipedia.org/wiki/John_Gaughan) reconstructed Turk, [Source image](http://www.grg.org/images/TurkSColes.jpg) with [L. Stephen Coles](/L._Stephen_Coles "L. Stephen Coles"): This is a derivative, released under the [GFDL](https://en.wikipedia.org/wiki/GNU_Free_Documentation_License) and [CC](https://en.wikipedia.org/wiki/Creative_Commons), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [James R. Slagle](/James_R._Slagle "James R. Slagle"), [Philip Bursky](/Philip_Bursky "Philip Bursky") (**1968**). *Experiments With a Multipurpose, Theorem-Proving Heuristic Program*. [Journal of the ACM](/ACM#Journal "ACM"), Vol. 15, No. 1
3. [↑](#cite_ref-3) [Ben Mittman](/Ben_Mittman "Ben Mittman") (**1971**). *[Computer Chess Programs (Panel)](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d1ee8)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-3.computer_chess_panel.mittman/3-1%20and%203-3.computer_chess_panel.mittman_etc.1971.ACM.062303021.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")

**[Up one level](/Engines "Engines")**