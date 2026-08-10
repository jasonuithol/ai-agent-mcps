# Huberman

Source: https://www.chessprogramming.org/Huberman

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Huberman**

**Huberman**, (Huberman's program)  
the Ph.D. thesis program by [Barbara Liskov](/Barbara_Liskov "Barbara Liskov") (née Huberman) written in [1968](/Timeline#1968 "Timeline") at [Stanford University](/Stanford_University "Stanford University"), under supervision of [John McCarthy](/John_McCarthy "John McCarthy"), to play certain chess [endgames](/Endgame "Endgame") with pieces versus the lonesome king. Barbara Huberman used heuristics to drive the lonesome king away from the [center](/Center "Center") and for [K,B,N](/KBNK_Endgame "KBNK Endgame") into the right corner, and most notably already proposed the [Killer Heuristic](/Killer_Heuristic "Killer Heuristic") for early refutations of the [alpha-beta](/Alpha-Beta "Alpha-Beta") search [[1]](#cite_note-1). She further elaborated on the implications of these endings with different board sizes, even an [infinite board](/index.php?title=Infinite_Board&action=edit&redlink=1 "Infinite Board (page does not exist)").

# Quotes

[Alex Bell](/Alex_Bell "Alex Bell") in *Games Playing with Computers* on Huberman's program [[2]](#cite_note-2):

```
A philosophic program was written by Barbara Huberman to specifically play end games. It was a research project on translating book descriptions of problem solving methods into program heuristics. It is well known that the following minimum combinations of pieces have a certain win against a lone king:
```

- K,Q
- [K,R](/KRK "KRK")
- K,B,B
- [K,B,N](/KBNK_Endgame "KBNK Endgame")
- K,N,N,N

```
The K,Q can be considered equivalent to the K,R.
```

```
Huberman followed descriptions (by Capablanca and Fine) of how to execute all but the case of K,N,N,N. The cases of K,R and K,B,B are feasible using the minimax technique. This is not true for the K,B,N. The difficulty here is that bishops and rooks can force mate on any size of board but the knight has a limited mobility (from a centre square there are five squares which each require four moves to be reached by the knight).
```

```
Consequently the K,B,N mate is not possible on a board of side > 8. Even allowing for the black king being against a side there is no way in which the K,B,N can be arranged and played that will systematically force the black king along the edge of an infinite board. Because of this weakness the actual mating can take up to forty moves. Huberman's model for the problem was a forcing tree co-ordinated with two functions (better and worse) which were able to compare positions. Roughly speaking the program had two sub-goals (apart from not losing a piece, giving stalemate , etc). First drive the king away from the centre and second, when the king is at the edge, drive him towards a corner of the bishop's colour.
```

```
Huberman's program is the only one which can perform this mating sequence for any starting position. It would be a useful addition to Greenblatt's program, being easily extended to solve other end games and hence giving the more general program a selection of sub-goals equivalent to winning the game. The problem of K,N,N,N is unlikely to occur; nevertheless it is of interest to the theorists. One surprising fact is that the combination can systematically drive the black king along the edge of an infinite board, and therefore the mating sequence is much easier to program.
```

# Publications

- [Barbara J. Huberman](/Barbara_Liskov "Barbara Liskov") (**1968**). *A Program to Play Chess End Games*. Technical Report no. CS-106, Ph.D. thesis. [Stanford University](/Stanford_University "Stanford University"), Computer Science Department
- [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227, [Chess programs: Huberman](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p005.htm#index19)
- [John McCarthy](/John_McCarthy "John McCarthy") (**1990**). *Chess as the Drosophila of AI.* [Computers, Chess, and Cognition](/Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition"), pp. 227-237 [[3]](#cite_note-3)

# Forum Posts

- [evaluating KNNN-K](https://www.stmintz.com/ccc/index.php?id=197935) by [Rafael B. Andrist](/Rafael_B._Andrist "Rafael B. Andrist"), [CCC](/CCC "CCC"), November 18, 2001

# References

1. [↑](#cite_ref-1) [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal](/ICGA_Journal "ICGA Journal"), Vol. 15, No. 1, pp. 8, The killer heuristic
2. [↑](#cite_ref-2) [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227, [Chess programs: Huberman](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p005.htm#index19)
3. [↑](#cite_ref-3) [John McCarthy](/John_McCarthy "John McCarthy") (**1997**). *Chess as the Drosophila of AI*. Computer Science Department, [Stanford University](/Stanford_University "Stanford University"), condensed version of the 1990 paper, [pdf](http://innovation.it.uts.edu.au/projectjmc/articles/drosophila/drosophila.pdf)

**[Up one Level](/Engines "Engines")**