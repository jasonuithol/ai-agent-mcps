# Advances in Computer Chess 1

Source: https://www.chessprogramming.org/Advances_in_Computer_Chess_1

**[Home](/Main_Page "Main Page") \* [Conferences](/Conferences "Conferences") \* Advances in Computer Chess 1**

**[Next >](/Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Oxford_-_Balliol_College_-_geograph.org.uk_-_1329613.jpg/330px-Oxford_-_Balliol_College_-_geograph.org.uk_-_1329613.jpg)](/File:Oxford_-_Balliol_College_-_geograph.org.uk_-_1329613.jpg)

[Balliol College, Oxford](https://en.wikipedia.org/wiki/Balliol_College,_Oxford) [[1]](#cite_note-1)

The **Advances in Computer Chess 1** conference was held in March [1975](/Timeline#1975 "Timeline") at [Balliol College, Oxford](https://en.wikipedia.org/wiki/Balliol_College,_Oxford), [England](https://en.wikipedia.org/wiki/England), and was organized by the [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory") and the [Society for the Study of Artificial Intelligence and Simulation of Behaviour](http://www.aisb.org.uk/) (SSAISB). [Proceedings](https://en.wikipedia.org/wiki/Proceedings) were published in 1977, edited by [Mike Clarke](/Mike_Clarke "Mike Clarke"). It was already the second conference on computer chess, after a conference meeting on chess playing by computer in May 1973 at [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory") [[2]](#cite_note-2).

# Proceedings

- **Advances in Computer Chess 1**

:   [M.R.B. Clarke](/Mike_Clarke "Mike Clarke"), Editor, 1977
:   Edinburgh University Press, Edinburgh.
:   ISBN 0-852-24292-1, [amazom](http://www.amazon.de/Advances-in-Computer-Chess/dp/0852242921/ref=sr_11_1?ie=UTF8&qid=1245489640&sr=11-1)

# Papers

1. [Georgy Adelson-Velsky](/Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](/Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](/Mikhail_Donskoy "Mikhail Donskoy") (**1977**). *On the Structure of an Important Class of Exhaustive Problems and Methods of Search Reduction for them*.
2. [Hans Berliner](/Hans_Berliner "Hans Berliner") (**1977**). *A Representation and Some Mechanisms for a Problem-Solving Chess Program.*
3. [Ron Atkin](/Ron_Atkin "Ron Atkin") (**1977**). *Positional Play in Chess by Computer*. [[3]](#cite_note-3)
4. [Donald Michie](/Donald_Michie "Donald Michie") (**1977**). *King and Rook Against King: Historical Background and a Problem on the Infinite Board*.
5. [Soei T. Tan](/Soei_Tan "Soei Tan") (**1977**). *Describing Pawn Structures.*
6. [John Birmingham](/John_Birmingham "John Birmingham"), [Peter Kent](/Peter_Kent "Peter Kent") (**1977**). *Tree-searching and tree-pruning techniques*.
7. [Mike Clarke](/Mike_Clarke "Mike Clarke") (**1977**). *A quantitative study of KPK*.

# Reviews

- [Alex Bell](/Alex_Bell "Alex Bell") (**1975**).*[Techniques for playing the end game](http://www.chilton-computing.org.uk/acl/literature/news/1975.htm)*. [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
- [Jack Good](/Jack_Good "Jack Good") (**1978**). *[Review of "Advances in Computer Chess, Volume 1. by M.R.B. Clarke"; University Press, 1977](http://dl.acm.org/citation.cfm?id=1045416.1045430)*. [ACM SIGART Bulletin](/ACM#SIG "ACM"), Issue 66

# The Forerunner

The first conference meeting on computer chess took place at the [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory") May 1973. It was the forerunner of the later *Advances in Computer Chess* conferences. [Alex Bell](/Alex_Bell "Alex Bell") about the arisen of the conference [[4]](#cite_note-4) :

```
In 1972 I was back in England again and met John Scott, who was doing a PhD, and his tutor Dr. Alan Bond. Naturally we talked about chess programs and the recent happenings in the American ACM tournaments. As we talked it became fairly obvious that in the intervening 4 years a number of new ideas had appeared on the scene. One idea was called refutation, a technique which (like alpha-beta) could vastly speed up the tree searching without any loss of information (see Chapter 9 - Machine Technique).
```

```
Even more mysterious was a paper Multi Dimensional Structure in the Game of Chess by Ron Atkin [5] , a maths lecturer at Essex University. Up to this point all chess programs had evaluation functions which were decidedly ad hoc, the programmers had a feeling in their water that certain features, material, mobility, control of the centre, king safety, pawn structure, etc., were the most important and accordingly stuck them in the program with very little idea of their precise effect. Now here was a mathematician who, with lots of squiggly things, appeared to have a precise mathematical evaluation function. Unfortunately neither John nor I could understand the paper - so why not get Atkin to talk about it. There were a few other new ideas I did not understand - a new, knowledge approach to solving end games and some psychological theories about how chess players think - so why not have a conference? If nothing else I might get some idea of what was going on.
```

```
The first Computer Chess Conference took place at the Atlas Computer Laboratory in May 1973. Apart from inviting the speakers it was also obvious that the conference would have to demonstrate a chess program in some form and it is at this point in time that MASTER really got started.
--
From then on the operators played more carefully and revealed that the program, because it still only had a shallow search, still suffered badly from horizon effect. Nevertheless it did win a few more games and it was decided to use it as the demonstration program at the conference.
```

```
Well it didn't win a game, hardly surprising since it was up against much stronger players. Nevertheless several people noticed that the program was usually achieving its main aim of controlling the centre squares; in other words, it was quite successful in doing what little it had been told to do but, from then on, it had no further direction other than a vague idea of advancing its own pawns and blocking its opponent's. Peter improved its sense of purpose by making the program, as the game progressed, put less emphasis on controlling the fixed centre squares and more and more emphasis on controlling the squares around the enemy king, wherever he may be. Because of mini-max this also caused the program to protect the squares around its own king far more effectively.
```

# ACC1

The conference on computer chess took place at [Balliol College, Oxford](https://en.wikipedia.org/wiki/Balliol_College,_Oxford) in March 1975. It was organized by [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory") and the [Society for the Study of Artificial Intelligence and Simulation of Behaviour](http://www.aisb.org.uk/) (SSAISB), and was later declared as *Advances in Computer Chess 1* conference. Proceedings were published by [Mike Clarke](/Mike_Clarke "Mike Clarke") from [Queen Mary College](/Queen_Mary,_University_of_London "Queen Mary, University of London"). Some excerpt from co-organizer, [Alex Bell's](/Alex_Bell "Alex Bell") report in [Computer Weekly](https://en.wikipedia.org/wiki/Computer_Weekly), April 10, 1975, *Techniques for playing the end game* [[6]](#cite_note-6) :

```
AFICIONADOS of the arts of chess and computing gathered at Balliol College, Oxford, last month for the second conference on computer chess organised by the Atlas Computer Laboratory and the Artificial Intelligence and Simulation of Behaviour study group.
```

```
A number of experts were invited to give papers. on their work, including Dr Mikhail Donskoy of the USSR, one of the authors of the world champion program, KAISSA. Unfortunately Donskoy was unable to attend, a disappointment only mitigated by the presence from the US of Dr Hans Berliner, of Carnegie-Mellon. Berliner is the world correspondence chess champion and has also spent the last eight or nine years programming computers to play the game. To most people in the practical, model building side of the subject, ie making a program play the computer game, Berliner is THE expert. Although full of good, implementable ideas he has no illusions as to the limitations of such chess programs.
--
The conference itself lasted one and a half days and the papers (depending on the listener) ranged from the profound to the puerile. I have no desire to repeat my own personal views, indeed as one of the organisers I helped to provide a platform for speakers whose views I found astonishing. What did seem evident to me was that the majority of the audience fell into one of three categories. One group is the artificial intelligentsia. They fully understand the difficulties of the problem and are still thinking about how to solve it. The second group are the let's get on and program something crunchers, the model makers, the people who can make big computers float round the room whistling God save the Queen. These people absolutely refuse to put anything remotely resembling knowledge, chess or otherwise, into their programs if they can avoid it, believing that if the result plays good chess then it can be more easily adapted to attempt other, more useful, decision making problems. The third group is the most important, these are the people who are new to the subject, the people who say, It sounds like a fascinating problem and I'd like to know what's going on.
```

```
Hans Berliner fits into two of these categories, his talk covered the AI approach and the crunchers, but he is hardly a newcomer. He was the first speaker and the domain of his talk was chess tactics with emphasis on recognising situations and dealing with them explicitly. He is full of good ideas and techniques which are relevant to the problem of selecting the right move in a game of chess and, more important, showed clearly how each idea and technique could be implemented in a computer.
```

```
The next paper by Ron Atkin, of Essex University, was more profound. Atkin has developed a mathematically valid approach to positional play in chess and also described a method of simulating the hierarchical method used by the chess master. His ideas have an intuitive appeal; one feels he must be right but the problem of implementing the ideas in a computer, are enormous and, as yet, unsolved. Another problem was that not a single person in the audience was sufficiently competent to stand up and say, "This is all very well but your approach will not handle this situation in a chess game, a tactic which often shoots down the simple minded crunch programs".
```

```
The final talk on the first day was given by Professor Donald Michie of the Machine Intelligence Research Unit, Edinburgh, who dealt with mechanisation of the King, Rook versus King end game. The first machine to play this end game was built by Torres y Quevado c. 1900. Hardly anything was published about it and Michie made an interesting reconstruction of the machine, and I have to admit that Michie had got most of it right.
```

```
The next day the speakers included Dr Soei Tan, also of Edinburgh, who dealt with pawn structures; John Birmingham and Peter Kent partially described how MASTER operates; and Mike Clarke, of Queen Mary College, talked about the King, Pawn versus King ending. Clarke's approach is much more scientific than the crunch programs; he has enumerated all possible positions of the K, P v K end game (there are 906,545,760 of them) and discovered which are wins and which are draws. He has done a similar enumeration for the King, Rook v King ending and should, with a little more effort. be able to scientifically work backwards to the 16 pawns, 16 pieces end game.
```

```
As can be seen a great deal of time was spent on this King, Rook v King ending. This is interesting because if this ending can cause such difficulty then it is intuitively obvious that the full game must be at least an order of magnitude more difficult. This is intuitively obvious but difficult to prove, nevertheless it appears to be true in the real world. I certainly have great difficulty obtaining a draw with the lone King. Finally, Max Bramer has offered to demonstrate his K,R v K and K,P v K programs to anyone who is interested. He can be contacted at the Open University.
```

# Forum Posts

- [Computer chess books](https://groups.google.com/g/rec.games.chess.computer/c/kecoM_YlyAM/m/NiCnP8wRgnQJ) by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), February 05, 1997
- [Re: Whatever happened to Neural Network Chess programs?](https://groups.google.com/d/msg/rec.games.chess.computer/xthKCFRJkeM/ZgORiY9-gF0J) by [Andy Walker](/Andy_Walker "Andy Walker"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 28, 2000 » [Ron Atkin](/Ron_Atkin "Ron Atkin")

# External Links

- [Small Faces](/Category:Small_Faces "Category:Small Faces") - [Itchycoo Park](https://en.wikipedia.org/wiki/Itchycoo_Park), [Beat-Club](https://en.wikipedia.org/wiki/Beat-Club), September 23, 1967, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Oxford - Balliol College](https://en.wikipedia.org/wiki/Balliol_College,_Oxford), One of my favourite views, across the appropriately-named Broad Street, May 30 2009, Photographer [Peter Trimming](http://www.geograph.org.uk/profile/34298), source [geograph.org.uk](http://www.geograph.org.uk/photo/1329613)
2. [↑](#cite_ref-2) [Alex Bell](/Alex_Bell "Alex Bell") (ed.) (**1973**). *Computer Chess*. Proceedings May 1973 Meeting on chess playing by computer. Science Research Council, [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory")
3. [↑](#cite_ref-3)  [Re: Whatever happened to Neural Network Chess programs?](https://groups.google.com/d/msg/rec.games.chess.computer/xthKCFRJkeM/ZgORiY9-gF0J) by [Andy Walker](/Andy_Walker "Andy Walker"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 28, 2000
4. [↑](#cite_ref-4) [Alex Bell](/Alex_Bell "Alex Bell") (**1978**). *[MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm)*. Excerpt from: The Machine Plays Chess? [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
5. [↑](#cite_ref-5) [Ron Atkin](/Ron_Atkin "Ron Atkin") (**1972**). *Multi-Dimensional Structure in the Game of Chess*. In [International Journal of Man-Machine Studies, 4](http://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies_volume_4.html) pp. 341-362
6. [↑](#cite_ref-6) [Alex Bell](/Alex_Bell "Alex Bell") (**1975**).*[Techniques for playing the end game](http://www.chilton-computing.org.uk/acl/literature/news/1975.htm)*. [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)

**[Up one Level](/Conferences "Conferences")**