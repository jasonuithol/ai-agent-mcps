# Chess Wizard

Source: https://www.chessprogramming.org/Chess_Wizard

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Chess Wizard**

[![](/images/e/ee/WizardByIgorMorski.jpg)](http://yrnxt.com/2013/05/igor-morski/001-igor-morski/#main)

[Igor Morski](/Category:Igor_Morski "Category:Igor Morski") - Wizard [[1]](#cite_note-1) [[2]](#cite_note-2)

**Chess Wizard**,  
a [private](/Category:Private "Category:Private") chess engine by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), competing in various [French Computer Chess Championships](/French_Computer_Chess_Championship "French Computer Chess Championship") and [Massy Programmers Tournaments](/French_Programmers_Tournament "French Programmers Tournament"), winning the [FCCC 1998](/FCCC_1998 "FCCC 1998"), [FCCC 2002](/FCCC_2002 "FCCC 2002") and [FCCC 2003](/FCCC_2003 "FCCC 2003") [[3]](#cite_note-3), and [Massy 2004](/Massy_2004 "Massy 2004") [[4]](#cite_note-4).

# Photos

[![Fccc2002-06.jpg](/images/9/98/Fccc2002-06.jpg)](http://www.ludochess.com/fccc2002/tournoi.php3)

Chess Wizard vs [The Crazy Bishop](/The_Crazy_Bishop "The Crazy Bishop"), [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), [Rémi Coulom](/R%C3%A9mi_Coulom "Rémi Coulom"), [FCCC 2002](/FCCC_2002 "FCCC 2002") [[5]](#cite_note-5)

# Description

## 1996

from a [rgcc](/Computer_Chess_Forums "Computer Chess Forums") post by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet") in 1996 [[6]](#cite_note-6):

```
Chess Wizard is a highly selective program, with a lot of knowledge in the eval function. It uses the bitmap approach, like Crafty and Chess Guru. However, it is very speculative in its evaluation and has a lot of special algorithms regarding space control.
```

```
It is quite slow compared to a lot of other programs (6000-10000 n/s on Pentium Pro 200), but I think it is not too "stupid" (that is, for a chess program :) Chess Wizard is two years old now, but the French Championship was his first official tournament.  
...
Wizard uses different extensions at different time controls, and his eval parameters change also with the time control (more agressive in sudden death). It uses an alpha-beta, and heavily prune forward by evaluating the position at each node in the tree.  
...
Since Wizard plays reasonably well positionally, I will concentrate on its tactical abilities for a few months. I was wondering what recapture extensions is considered to be optimal by other programmers. This problem is not simple at all. I am considering for now recapture extensions of equal material on the same square, plus quality sacs, plus exchanges around either king. I do not use fractional depth extensions, since I have not seen great benefits from them.
```

## 2002

from a [CCC](/CCC "CCC") post by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet") in 2002 [[7]](#cite_note-7):

```
The first time Chess Wizard played a real game of chess was in 1994. I worked a lot in 1994/1995/1996, and in 1996 it won the french championship with Chess Guru. I read a lot of publications, studied some source code (Turbo Chess in Turbo Pascal, GNU, later Crafty), tried a thousand ideas that did not work, found a few that really worked...
```

```
I tried the bitboard approach very early (1995) because of the possibilities regarding evaluation. I always wanted Wizard to have a good evaluation, and a lot of complex things were easier to implement with bitboards. I learned some bitboard tricks from Crafty (in the 9.x to 10. versions I think) that I had not thought about before. But Chess Wizard is not entirely bitboard-based, it's more a hybrid approach.
```

```
I have two problems : my opening book is not very good, and I don't seem to find a way to make forward pruning really work. I tried 6723 ideas, a few times I thought I had found the solution, but everytime it was a false impression. Maybe I am forward-pruning challenged. I use null move (R=4 very far, then R=3, then R=2), I recently removed all checks from the quiescence search. The strength of Chess Wizard is based on two things : good evaluation, and search extensions. I use many threat extensions with small increments (2/16 of a ply), strange out of checks extensions, and so on. I tried singular extensions too, but with bad results.
```

```
When Wizard detects some patterns in the position, it simply tones down, and sometimes even shuts down completely, entire parts of the evaluation function to concentrate on the parameters that really counts (so other parameters don't get in the way).
```

```
But I really would like to find super-efficient forward pruning techniques, like those used in the top commercial programs. For the moment, I compensate with extensions. Maybe it is not possible to do both. Maybe it is the same thing, from a certain point of view.
```

```
But I have learned a few important things :
```

1. `You must never dismiss some thing that doesn't work now. Maybe in a year from now, It will work.`
2. `You must never assume that something that works in someone else program wil work in your program.`
3. `Like Christophe Théron rightly says, you must believe in statistics. Your testing methodology must be extremely well thought out.`
4. `If you hear someone say "this algorithm sucks", or "it doesn't work", don't forget to add "for me" to the sentence. You must try it for yourself.`
5. `Sometimes, you should completely leave the world of chess programming (even for one or two weeks). Some ideas have a way of being found only when you don't think about them !`

# See also

- [Chess Wizard (GUI)](/index.php?title=Chess_Wizard_(GUI)&action=edit&redlink=1 "Chess Wizard (GUI) (page does not exist)") by [Huang Chen](/index.php?title=Huang_Chen&action=edit&redlink=1 "Huang Chen (page does not exist)")
- [Raptor](/Raptor "Raptor")
- [Wizard](/Wizard "Wizard")

# Forum Posts

- [Match Rebel 8 - Chess Wizard on PP200](https://groups.google.com/d/msg/rec.games.chess.computer/0tVOKQd7iRI/szJtYUEzkeAJ) by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), December 12, 1996 » [Rebel](/Rebel "Rebel")
- [Fritz and Chess Wizard vs Deep Blue Junior](https://www.stmintz.com/ccc/index.php?id=52005) by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), [CCC](/CCC "CCC"), May 17, 1999
- [Chess Wizard on ICC](https://www.stmintz.com/ccc/index.php?id=245180) by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), [CCC](/CCC "CCC"), August 11, 2002
- [Chess Wizard, some history and techniques](https://www.stmintz.com/ccc/index.php?id=257088) by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), [CCC](/CCC "CCC"), October 08, 2002
- [Attacking chess from 2002, Dragon - ChessWizard](http://www.talkchess.com/forum/viewtopic.php?p=391785) by Robert Flesher, [CCC](/CCC "CCC"), January 31, 2011

# External Links

- [Wizard from Wikipedia](https://en.wikipedia.org/wiki/Wizard)
- [The Wizard (nickname) from Wikipedia](https://en.wikipedia.org/wiki/The_Wizard_%28nickname%29)

# References

1. [↑](#cite_ref-1) [Igor Moski: Wizard](http://yrnxt.com/2013/05/igor-morski/001-igor-morski/#main)
2. [↑](#cite_ref-2) [Igor Morski: An Interview with the Gifted Surrealist ArtistSunrise Artists](http://sunriseartists.com/2013/06/13/igor-morski-interview/)
3. [↑](#cite_ref-3) [Subject: FCCC 2003 : Chess Wizard champion !](https://www.stmintz.com/ccc/index.php?id=319657) by [Stéphane Nguyen](/St%C3%A9phane_Nguyen "Stéphane Nguyen"), [CCC](/CCC "CCC"), October 05, 2003
4. [↑](#cite_ref-4) [Chess Wizard won Massy 2004 ...](https://www.stmintz.com/ccc/index.php?id=371700) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), June 21, 2004
5. [↑](#cite_ref-5) [Massy, France - 5 & 6 Oct 2002 - 9ème Championnat Français de Programmes d'Echecs](http://www.ludochess.com/fccc2002/tournoi.php3)
6. [↑](#cite_ref-6)  [Match Rebel 8 - Chess Wizard on PP200](https://groups.google.com/d/msg/rec.games.chess.computer/0tVOKQd7iRI/szJtYUEzkeAJ) by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), December 12, 1996
7. [↑](#cite_ref-7) [Chess Wizard, some history and techniques](https://www.stmintz.com/ccc/index.php?id=257088) by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), [CCC](/CCC "CCC"), October 08, 2002

**[Up one level](/Engines "Engines")**