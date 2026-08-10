# Enhanced Transposition Cutoff

Source: https://www.chessprogramming.org/Enhanced_Transposition_Cutoff

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Transposition Table](/Transposition_Table "Transposition Table") \* Enhanced Transposition Cutoff**

[![](/images/e/ea/ETC.JPG)](/File:ETC.JPG)

ETC at node N [[1]](#cite_note-1)

**Enhanced Transposition Cutoff** (ETC) [[2]](#cite_note-2),  
an attempt to get a [cutoff](/Beta-Cutoff "Beta-Cutoff") from the transposition table, even though an entry may not exist for the current position. Entries may exist for **children** of the current position and one of these could be used to produce a cutoff without having to expand the current node. This is done by looping over the legal moves calculating the [hash keys](/Zobrist_Hashing "Zobrist Hashing") and doing a transposition table lookup with them in the hopes that one of these will produce the desired cutoff. One enhancement of this idea is to try only the strongest moves, perhaps the first several that are deemed to have potential.

In cases where a cutoff cannot be found, a fairly substantial amount of time is wasted, so in general it should not be applied at shallow depths of the tree where the small sub-tree savings may not justify the extra work. Example code for Enhanced Transposition Cutoff is rather difficult to find. One possible source is [Fruit](/Fruit "Fruit") version 1.5. However, this technique is not used since version 2.0, as tests have shown that it hurts Fruit's strength.

# Maximizing Transpositions

Quote from [Aske Plaat](/Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](/Wim_Pijls "Wim Pijls") and [Arie de Bruin](/Arie_de_Bruin "Arie de Bruin") in *Nearly Optimal Minimax Tree Search?* [[3]](#cite_note-3):

```
The reduction in search tree size offered by ETC is, in part, offset by the increased computation per node. For chess and checkers, it appears the performing ETC at all interior nodes is too expensive. A compromise, performing ETC at all interior nodes that are more than 2 ply away from the leaves, results in most of the ETC benefits with only a small computational overhead. Thus, ETC is a practical enhancement to most Alpha-Beta search programs.
```

```
We also experimented with more elaborate lookahead schemes. For example, ETC transposes the right portion of the tree into the left. ETC can be enhanced to also transpose from left to right. At an interior node, look up all the children’s positions in the transposition table. If no cutoff occurs, then check to see if one of the children leads to a position with a cutoff score that has not been searched deep enough. If so, then use the move leading to this score as the first move to try in this position. Unfortunately, several variations on this idea failed to yield a tangible improvement.
```

# See also

- [Beta-Cutoff](/Beta-Cutoff "Beta-Cutoff")
- [Repetitions](/Repetitions "Repetitions")
- [Transposition](/Transposition "Transposition")

# Publications

- [Aske Plaat](/Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](/Wim_Pijls "Wim Pijls"), [Arie de Bruin](/Arie_de_Bruin "Arie de Bruin") (**1994, 2014**). *Nearly Optimal Minimax Tree Search?* Technical Report, [University of Alberta](/University_of_Alberta "University of Alberta"), [arXiv:1404.1518](https://arxiv.org/abs/1404.1518)
- [Aske Plaat](/Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](/Wim_Pijls "Wim Pijls"), [Arie de Bruin](/Arie_de_Bruin "Arie de Bruin") (**1996**). *Exploiting Graph Properties of Game Trees.* [AAAI-96](/Conferences#AAAI-96 "Conferences")

# Forum Posts

## 1995 ...

- [Hash Table test (re: move ordering)](https://groups.google.com/d/msg/rec.games.chess.computer/LNIjJWxKL4U/F5KgDJjQ698J) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), February 8, 1996
- [Trick Marsland](https://groups.google.com/d/msg/rec.games.chess.computer/P_odidE_noY/_2H_VymEUhIJ) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), February 15, 1996
- [Tree search issues!](https://groups.google.com/d/msg/rec.games.chess.computer/TkhrEajlMCs/r8BRbNjNCt8J) by [Magnus Heldestad](/index.php?title=Magnus_Heldestad&action=edit&redlink=1 "Magnus Heldestad (page does not exist)"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), May 26, 1997 » [MTD(f)](/MTD(f) "MTD(f)")

:   [Re: Tree search issues!](https://groups.google.com/d/msg/rec.games.chess.computer/TkhrEajlMCs/Cg3pBOLSzv0J) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), May 26, 1997
:   [Re: Tree search issues!](https://groups.google.com/d/msg/rec.games.chess.computer/TkhrEajlMCs/HgrYwdBcjnEJ) by [Aske Plaat](/Aske_Plaat "Aske Plaat"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), May 27, 1997

- [ETC hashing discussion](https://groups.google.com/d/msg/rec.games.chess.computer/cLAwsdoYWUs/Th9y0jRRc5kJ) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), May 28, 1997
- [Enhanced Transposition Table Cutoffs](https://groups.google.com/d/msg/rec.games.chess.computer/irT5FyNOsBY/5YQzCgeBFKQJ) by [Andrea Zinno](/index.php?title=Andrea_Zinno&action=edit&redlink=1 "Andrea Zinno (page does not exist)"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), July 30, 1997
- [Enhanced Transposition Cutoff](https://www.stmintz.com/ccc/index.php?id=18821) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [CCC](/CCC "CCC"), May 18, 1998
- [ETC](https://www.stmintz.com/ccc/index.php?id=65039) by [Daniel Homan](/Daniel_Homan "Daniel Homan"), [CCC](/CCC "CCC"), August 17, 1999

## 2000 ...

- [Programmers: ETC](https://www.stmintz.com/ccc/index.php?id=284050) by [Peter McKenzie](/Peter_McKenzie "Peter McKenzie"), [CCC](/CCC "CCC"), February 13, 2003
- [Enhanced Transposition Cutoff](https://www.stmintz.com/ccc/index.php?id=379495) by [Stuart Cracraft](/Stuart_Cracraft "Stuart Cracraft"), [CCC](/CCC "CCC"), July 28, 2004

## 2005 ...

- [Enhanced Transposition Cutoff](http://www.talkchess.com/forum/viewtopic.php?t=13005) by [kongsian](/Chua_Kong_Sian "Chua Kong Sian"), [CCC](/CCC "CCC"), April 10, 2007
- [Enhanced Transposition Cutoff](http://www.talkchess.com/forum/viewtopic.php?t=24835) by hcyrano, [CCC](/CCC "CCC"), November 11, 2008

## 2010 ...

- [Mult-cut, SE and ETC](http://www.talkchess.com/forum/viewtopic.php?t=35697) by Ricardo Gibert, [CCC](/CCC "CCC"), August 05, 2010 » [Multi-Cut](/Multi-Cut "Multi-Cut"), [Singular Extensions](/Singular_Extensions "Singular Extensions")

# External Links

- [ETC from Wikipedia](https://en.wikipedia.org/wiki/ETC)
- [Wolfgang Dauner's](/Category:Wolfgang_Dauner "Category:Wolfgang Dauner") [Et Cetera](http://www.longhairmusic.de/etceterasilberdeutsch.htm) - [Tuning Spread](https://en.wikipedia.org/wiki/Piano_tuning), [Yin](https://en.wikipedia.org/wiki/Yin) (22:47), [The Great Escape](https://en.wikipedia.org/wiki/The_Great_Escape) (46:12), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   13th [Jazzfestival](https://en.wikipedia.org/wiki/Deutsches_Jazzfestival), [Frankfurt](https://en.wikipedia.org/wiki/Frankfurt), [Jahrhunderthalle](https://en.wikipedia.org/wiki/Jahrhunderthalle) , March 25, 1972, [Hessischer Rundfunk](https://en.wikipedia.org/wiki/Hessischer_Rundfunk) [FM broadcast](https://en.wikipedia.org/wiki/FM_broadcasting)
:   lineup: [Wolfgang Dauner](/Category:Wolfgang_Dauner "Category:Wolfgang Dauner"), [Günter Lenz](https://en.wikipedia.org/wiki/G%C3%BCnter_Lenz), [Fred Braceful](https://en.wikipedia.org/wiki/Fred_Braceful), [Jon Hiseman](/Category:Jon_Hiseman "Category:Jon Hiseman"), [Larry Coryell](/Category:Larry_Coryell "Category:Larry Coryell")

# References

1. [↑](#cite_ref-1) [Aske Plaat](/Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](/Wim_Pijls "Wim Pijls"), [Arie de Bruin](/Arie_de_Bruin "Arie de Bruin") (**1994, 2014**). *Nearly Optimal Minimax Tree Search?* Technical Report, [University of Alberta](/University_of_Alberta "University of Alberta"), [arXiv:1404.1518](https://arxiv.org/abs/1404.1518), *4.1 Maximizing Transpositions* ETC Image pp. 9
2. [↑](#cite_ref-2) [original article](https://chessprogramming.wikispaces.com/page/diff/Enhanced+Transposition+Cutoff/24577949) by [Don Dailey](/Don_Dailey "Don Dailey"), May 18, 2008
3. [↑](#cite_ref-3) [Aske Plaat](/Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](/Wim_Pijls "Wim Pijls"), [Arie de Bruin](/Arie_de_Bruin "Arie de Bruin") (**1994, 2014**). *Nearly Optimal Minimax Tree Search?* Technical Report, [University of Alberta](/University_of_Alberta "University of Alberta"), [arXiv:1404.1518](https://arxiv.org/abs/1404.1518)

**[Up one Level](/Transposition_Table "Transposition Table")**