# ShashChess

Source: https://www.chessprogramming.org/ShashChess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* [Stockfish](/Stockfish "Stockfish") \* ShashChess**

**ShashChess**,  
a [Stockfish](/Stockfish "Stockfish") [derivative](/Category:Derivative "Category:Derivative") by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo") with the aim to apply the proposals of [Alexander Shashin](/index.php?title=Alexander_Shashin&action=edit&redlink=1 "Alexander Shashin (page does not exist)") as exposed in his book *Best Play: A New Method for Discovering the Strongest Move* [[1]](#cite_note-1) [[2]](#cite_note-2)
[[3]](#cite_note-3).
First released in July 2018 [[4]](#cite_note-4),
subsequent ShashChess versions feature [skill levels](/Playing_Strength "Playing Strength") and handicap modes, [NNUE](/NNUE "NNUE"), [Monte-Carlo Tree Search](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") with one or multiple [threads](/Thread "Thread") in conjunction with [alpha-beta](/Alpha-Beta "Alpha-Beta"),
and various [learning](/Learning "Learning") techniques utilizing a [persistent hash table](/Persistent_Hash_Table "Persistent Hash Table") [[5]](#cite_note-5)
[[6]](#cite_note-6).

# Personalities

Based on static [evaluation](/Evaluation "Evaluation") [score](/Score "Score") ranges derivered from [pawn](/Pawn "Pawn") endgame [point value](/Point_Value "Point Value") (PawnValueEg = 208), ShashChess classifies the position with five personalities of three former [World Chess Champions](https://en.wikipedia.org/wiki/World_Chess_Championship),
[Tigran Petrosian](https://en.wikipedia.org/wiki/Tigran_Petrosian) for negative scores,
[José Raúl Capablanca](https://en.wikipedia.org/wiki/Jos%C3%A9_Ra%C3%BAl_Capablanca) for balanced scores,
and [Mikhail Tal](https://en.wikipedia.org/wiki/Mikhail_Tal) for positive scores [[7]](#cite_note-7):

```
if      (eval < -74) personality =  Petosian;
else if (eval < -31) personality =  Petosian | Capablanca;
else if (eval <  31) personality =             Capablanca;
else if (eval <  74) personality =             Capablanca | Tal;
else                 personality =                          Tal;
```

These personalities are considered in various [search selectivity](/Selectivity "Selectivity") thresholds, along with multiple dynamic evaluation score adjustments.

# Q-Learning

A [rote learning](https://en.wikipedia.org/wiki/Rote_learning) technique inspired from [Q-learning](/Reinforcement_Learning#Q-Learning "Reinforcement Learning"), worked out and introduced by [Kelly Kinyama](/index.php?title=Kelly_Kinyama&action=edit&redlink=1 "Kelly Kinyama (page does not exist)")
[[8]](#cite_note-8)
[[9]](#cite_note-9)
and also employed in [BrainLearn](/index.php?title=BrainLearn&action=edit&redlink=1 "BrainLearn (page does not exist)") 9.0 [[10]](#cite_note-10),
was applied in ShashChess since version 12.0 [[11]](#cite_note-11).
After the end of a decisive selfplay game, the [list of moves](/Move_List "Move List") (ml) and associated [scores](/Score "Score") is merged into the learn table from end to start,
the score of timestep t adjusted as weighted average with the future reward of timestep t+1, using a [learning rate](https://en.wikipedia.org/wiki/Q-learning#Learning_Rate) α of 0.5 and a [discount factor](https://en.wikipedia.org/wiki/Q-learning#Discount_factor) γ of 0.99 [[12]](#cite_note-12):

```
  for (t = ml.size() - 2; t >= 0; t--) {
    ml[t].score = (1-α)*ml[t].score + α*γ*ml[t+1].score;
    insertIntoOrUpdateLearningTable( ml[t] );
  }
```

During repeated selfplay games, subsequently playing along the learned best line so far, decreasing score adjustments will stimulate exploration of alternative siblings, while increasing score adjustments correspondents to exploitation of the best move.

# Forum Posts

## 2018 ...

- [ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [CCC](/CCC "CCC"), July 28, 2018

:   [Re: ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093&start=103) (11.0) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [CCC](/CCC "CCC"), March 06, 2020
:   [Re: ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093&start=105) (12.0) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [CCC](/CCC "CCC"), June 28, 2020
:   [Re: ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093&start=209) (15.0) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [CCC](/CCC "CCC"), October 03, 2020
:   [Re: ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093&start=272) (17.1) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [CCC](/CCC "CCC"), June 01, 2021

- [Build ShashChess for Android](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68120&p=769919) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [CCC](/CCC "CCC"), August 01, 2018

## 2020 ...

- [ShashChess 12.0](https://groups.google.com/g/fishcooking/c/GLag32ARtKo/m/3Zoaq3-rAwAJ) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), June 28, 2020
- [A new reinforcement learning implementation of Q learning algorithm for alphabeta engines to automatically tune the evaluation of chess positions](https://groups.google.com/g/fishcooking/c/6IzmiSCB8lg/m/sFeSq9ykAQAJ) by [Kelly Kinyama](/index.php?title=Kelly_Kinyama&action=edit&redlink=1 "Kelly Kinyama (page does not exist)"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), June 29, 2020
- [ShashChess NNUE 1.0](https://groups.google.com/d/msg/fishcooking/yWtpz_FY5_Y/RMTG56fkAAAJ) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), July 25, 2020
- [Shashchess which executable to use](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76394) by Andrew Bernasrd, [CCC](/CCC "CCC"), January 23, 2021
- [New BrainLearn and ShashChess](https://groups.google.com/g/fishcooking/c/Iy1AlEZJWc8) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), May 19, 2021
- [ShashChess](https://talkchess.com/viewtopic.php?t=78738) by criko, [CCC](/CCC "CCC"), November 25, 2021
- [Shashin theory](https://talkchess.com/viewtopic.php?t=84274) by [Peter Berger](/Peter_Berger "Peter Berger"), [CCC](/CCC "CCC"), September 22, 2024

# External Links

- [GitHub - amchess/ShashChess: A try to implement Alexander Shashin's theory on a Stockfish's derived chess engine](https://github.com/amchess/ShashChess)
- [ShashChess 11.0 64-bit](https://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=ShashChess%2011.0%2064-bit) in [CCRL 40/15](/CCRL "CCRL")
- [ShashChess 15.0 64-bit](https://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=ShashChess%2015.0%2064-bit) in [CCRL 40/15](/CCRL "CCRL")

# References

1. [↑](#cite_ref-1) [Welcome to BS Chess](http://www.bs-chess.com/latin/lectures/2011/shashin4.html)
2. [↑](#cite_ref-2) [Alexander Shashin](/index.php?title=Alexander_Shashin&action=edit&redlink=1 "Alexander Shashin (page does not exist)") (**2013**). *Best Play: A New Method for Discovering the Strongest Move*. [Mongoose Press](https://mongoosepress.com/), [Amazon](https://www.amazon.com/Best-Play-Discovering-Strongest-2013-01-01/dp/B01A0CKJQM)
3. [↑](#cite_ref-3) [Review: Best Play | ChessVibes](https://web.archive.org/web/20130909054429/http://www.chessvibes.com/review-best-play) by [Arne Moll](https://ratings.fide.com/profile/1005820), September 05, 2013 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
4. [↑](#cite_ref-4) [ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [CCC](/CCC "CCC"), July 28, 2018
5. [↑](#cite_ref-5) [ShashChess/README.md at master · amchess/ShashChess · GitHub](https://github.com/amchess/ShashChess/blob/master/README.md)
6. [↑](#cite_ref-6) [Re: Komodo MCTS](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70948&start=17) by [Mark Lefler](/Mark_Lefler "Mark Lefler"), [CCC](/CCC "CCC"), June 12, 2019 » [Komodo MCTS](/Komodo#MCTS "Komodo")
7. [↑](#cite_ref-7) [ShashChess/search.cpp at master · amchess/ShashChess · GitHub](https://github.com/amchess/ShashChess/blob/master/src/All/search.cpp#L446)
8. [↑](#cite_ref-8) [Re: Self-Learning stockfish upgraded](https://groups.google.com/g/fishcooking/c/fhX7dFAsyew/m/NSd0-OJjBwAJ) by [Kelly Kinyama](/index.php?title=Kelly_Kinyama&action=edit&redlink=1 "Kelly Kinyama (page does not exist)"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), May 28, 2019
9. [↑](#cite_ref-9) [A new reinforcement learning implementation of Q learning algorithm for alphabeta engines to automatically tune the evaluation of chess positions](https://groups.google.com/g/fishcooking/c/6IzmiSCB8lg/m/sFeSq9ykAQAJ) by [Kelly Kinyama](/index.php?title=Kelly_Kinyama&action=edit&redlink=1 "Kelly Kinyama (page does not exist)"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), June 29, 2020
10. [↑](#cite_ref-10) [Release BrainLearn 9.0 · amchess/BrainLearn · GitHub](https://github.com/amchess/BrainLearn/releases/tag/9.0)
11. [↑](#cite_ref-11) [ShashChess 12.0](https://groups.google.com/g/fishcooking/c/GLag32ARtKo/m/3Zoaq3-rAwAJ) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), June 28, 2020
12. [↑](#cite_ref-12) [ShashChess/search.cpp at master · amchess/ShashChess · GitHub](https://github.com/amchess/ShashChess/blob/master/src/All/search.cpp#L2625)

**[Up one Level](/Stockfish "Stockfish")**