# Zillions of Games

Source: https://www.chessprogramming.org/Zillions_of_Games

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Zillions of Games**

[![](/images/thumb/1/19/Zillions_of_games.jpg/300px-Zillions_of_games.jpg)](https://en.wikipedia.org/wiki/File:Zillions_of_games.jpg)

Zillions of Games 2.0 Start Screen [[1]](#cite_note-1)

**Zillions of Games**,  
a commercial [general game playing](/General_Game_Playing "General Game Playing") [Windows](/Windows "Windows") program developed by [Jeff Mallett](/Jeff_Mallett "Jeff Mallett") and [Mark Lefler](/Mark_Lefler "Mark Lefler") to play [abstract strategy](https://en.wikipedia.org/wiki/Abstract_strategy_game) [board games](https://en.wikipedia.org/wiki/Board_game) with [perfect information](https://en.wikipedia.org/wiki/Perfect_information) and up to 32 players, first released in 1998. Zillions of Games **2**, released in 2003, comes with 100 new features, able to enforce maximal capturing rules as used in some versions of [Checkers](/Checkers "Checkers"), and is packed with 350 board games, puzzles, and variants [[2]](#cite_note-2), including chess and 60 [chess variants](/Chess#Variants "Chess"). Zillions further supports randomness in games through a special, computer-controlled "random player" that chooses its moves randomly, which allows to simulate [dice games](https://en.wikipedia.org/wiki/List_of_dice_games).

# Zillions Rules Language

The game rules are specified by the Zillons rules language, persistant in [ASCII](https://en.wikipedia.org/wiki/ASCII) readable Zillion rules files with the extension **zrf** [[3]](#cite_note-3), based on [Lisp](/index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)") like [S-expressions](https://en.wikipedia.org/wiki/S-expression):

```
(game
  (title "...") 
  (players ...) ; up to 32
  (turn-order ... )
  (board .... )
  (piece ... ; up to 32
    (moves ...)
  ) 
  (board-setup ...)
  (draw-condition ...)
  (win-condition ...)
 )
)
(game ...)
```

Besides defining how pieces move, Zillions can define how pieces may be dropped. All piece and board graphics referred in the rule files, are required in Windows [BMP format](https://en.wikipedia.org/wiki/BMP_file_format).

# Selected Games

## Chess & Variants

- [Chess](/Chess "Chess")
- [Chinese Chess](/Chinese_Chess "Chinese Chess")
- [Crazyhouse](/Crazyhouse "Crazyhouse")
- [Knightmate](/Knightmate_Chess "Knightmate Chess")
- [Losing Chess](/Losing_Chess "Losing Chess")
- [Shatranj](/Shatranj "Shatranj")
- [Shogi](/Shogi "Shogi")

## Board Games

- [Arimaa](/Arimaa "Arimaa")
- [Breakthrough](/Breakthrough_(Game) "Breakthrough (Game)")
- [Checkers](/Checkers "Checkers")
- [Clobber](/Clobber "Clobber")
- [Go](/Go "Go")
- [Hex](/Hex "Hex")
- [Kalah](/Kalah "Kalah")
- [Lines of Action](/Lines_of_Action "Lines of Action")
- [Reversi](/Othello "Othello")
- [Nine Men’s Morris](/Nine_Men%E2%80%99s_Morris "Nine Men’s Morris")

## Puzzles

- [Eight Queens Problem](/Backtracking#8QinBitboards "Backtracking")
- [Knight's Tour](/Knight_Pattern "Knight Pattern")

# See also

- [Game Description Language](/General_Game_Playing#GDL "General Game Playing")
- [Games](/Games "Games")

# Publications

- [Jeff Mallett](/Jeff_Mallett "Jeff Mallett") (**2003**). *ZRF Language References*. [pdf](http://www.cs.duke.edu/courses/spring06/cps108/Assignments/06_vooga/zrf.pdf)
- [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer") (**2003**). *Computer-Aided Game Inventing*. [Friedrich Schiller University of Jena](https://en.wikipedia.org/wiki/University_of_Jena), [pdf](http://www.minet.uni-jena.de/preprints/althoefer_03/CAGI.pdf)
- [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer") (**2004**). *[Improved game play by multiple computer hints](http://www.sciencedirect.com/science/article/pii/S0304397503005851)*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 313, No. 3

# Forum Posts

- [moderation:question about allowed discussions](https://www.stmintz.com/ccc/index.php?id=372641) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), June 26, 2004

:   [Re: Zillions of Games is fantastic](https://www.stmintz.com/ccc/index.php?id=372708) by [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer"), [CCC](/CCC "CCC"), June 26, 2004 [[4]](#cite_note-4) [[5]](#cite_note-5)

- [Zillions of Games and WinBoard](http://www.talkchess.com/forum/viewtopic.php?t=18309) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), December 11, 2007

# External Links

- [Zillions of Games - Unlimited Board Games & Puzzles](http://www.zillionsofgames.com/index.html)

:   [Zillions of Games - How Many Games?](http://www.zillionsofgames.com/games.html)
:   [Zillions of Games - Free Games for Download](http://www.zillionsofgames.com/games/)
:   [Zillions of Games - 2358 Free Games for Download](http://www.zillions-of-games.com/games/index-tripartite.html)

- [Zillions of Games - Wikipedia](https://en.wikipedia.org/wiki/Zillions_of_Games)
- [Zillions of Games](http://www.chessvariants.org/programs.dir/zillions/) from [Chessvariants.org](http://www.chessvariants.org/)
- [600 Zillions Games](http://karlscherer.com/Zillions/swindex2.html) by [Karl Scherer](/index.php?title=Karl_Scherer&action=edit&redlink=1 "Karl Scherer (page does not exist)")
- [WinBoard Adapter for Zillions of Games](http://andreas.pbworks.com/w/page/27366687/WinBoard%20Adapter%20for%20Zillions%20of%20Games) by [Andreas Kaufmann](/index.php?title=Andreas_Kaufmann&action=edit&redlink=1 "Andreas Kaufmann (page does not exist)")
- [Galton Game](http://www.althofer.de/galton-game.html) by [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer")

# References

1. [↑](#cite_ref-1) [Zillions of Games - Wikipedia](https://en.wikipedia.org/wiki/Zillions_of_Games)
2. [↑](#cite_ref-2) [Zillions of Games - How Many Games?](http://www.zillionsofgames.com/games.html)
3. [↑](#cite_ref-3) [Jeff Mallett](/Jeff_Mallett "Jeff Mallett") (**2003**). *ZRF Language References*. [pdf](http://www.cs.duke.edu/courses/spring06/cps108/Assignments/06_vooga/zrf.pdf)
4. [↑](#cite_ref-4) [Nina Hagen](/Category:Nina_Hagen "Category:Nina Hagen")
5. [↑](#cite_ref-5) [BEZZENBERGER Rechtsanwälte - Kanzlei für gewerblichen Rechtsschutz, Urheber- und Medienrecht](http://www.kanzlei-bezzenberger.de/jb.html)

**[Up one level](/Engines "Engines")**