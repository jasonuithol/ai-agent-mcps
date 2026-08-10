# Woodpusher

Source: https://www.chessprogramming.org/Woodpusher

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Woodpusher**

[![](/images/c/cb/Woodpusher.JPG)](/File:Woodpusher.JPG)

Woodpusher mascot

**Woodpusher**,  
a chess program developed in 1989 by [John Hamlen](/John_Hamlen "John Hamlen") as part of a university project looking into [null-move](/Null_Move "Null Move") search techniques. Woodpusher played various [World Computer-](/World_Computer_Chess_Championship "World Computer Chess Championship"), [World Microcomputer Chess Championships](/World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship") and [Computer Olympiads](/Computer_Olympiad "Computer Olympiad"). *Woodpusher 1997* played the [WCCC 2004](/WCCC_2004 "WCCC 2004") in [Ramat-Gan](https://en.wikipedia.org/wiki/Ramat_Gan) and the [WCCC 2011](/WCCC_2011 "WCCC 2011") in [Tilburg](https://en.wikipedia.org/wiki/Tilburg) as an experiment to play with a seven respectively fourteen years old program.

# Description

Description given in 1995 from the [ICGA](/ICGA "ICGA") tournament site [[1]](#cite_note-1) :

```
Woodpusher is a small chess program (< 64K) of conventional design. It uses an iterative deepening alpha-beta search with PVS and aspiration window enhancements. The first version of Woodpusher was born in 1989 as part of a university project looking into null-move search techniques. True to it's origins, this new version of the program still uses the null-move throughout the search to recognize threats and to forward prune branches of the search tree. A database of attacks from and to all the squares on the board is maintained by using CHESS 4.5's bit-board implementation. These data structures are used for both generating moves and making positional evaluations. Woodpusher's position evaluation is maintained almost entirely incrementally while making and un-making moves during the search, with very little work done at the terminal nodes. The evaluation is therefore necessarily simple, but does include true measures of mobility rather than relying on piece-square evaluations.
```

# Photos

[![Wccc2011-3.JPG](/images/8/86/Wccc2011-3.JPG)](/File:Wccc2011-3.JPG)

[WCCC 2011](/WCCC_2011 "WCCC 2011"), Woodpusher 1997 by [John Hamlen](/John_Hamlen "John Hamlen") vs. [Pandix](/Pandix "Pandix") by [Gyula Horváth](/Gyula_Horv%C3%A1th "Gyula Horváth") (left) [[2]](#cite_note-2)

# Namesakes

- [WoodPusher](http://mono-code.sourceforge.net/) a chess application written in [C#](/C_sharp "C sharp") by [Jamin P. Gray](http://sourceforge.net/projects/mono-code/)

# See also

- [Knowledge | Search versus Evaluation](/Knowledge#SearchVersusEvaluation "Knowledge")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Patzer](/Patzer "Patzer")
- [Woodpecker](/Woodpecker "Woodpecker")

# Publications

- [John Hamlen](/John_Hamlen "John Hamlen") (**2004**). *Seven Year Itch*. [ICGA Journal, Vol. 27, No. 4](/ICGA_Journal#27_1 "ICGA Journal") [[3]](#cite_note-3) » [WCCC 2004](/WCCC_2004 "WCCC 2004")
- [John Hamlen](/John_Hamlen "John Hamlen") (**2012**). *Game Over for the Woodpusher Experiment: 7+7=0*. [ICGA Journal, Vol. 35, No. 1](/ICGA_Journal#35_1 "ICGA Journal") » [WCCC 2011](/WCCC_2011 "WCCC 2011")

# Forum Posts

- [I think that woodpusher is the surprise of the tournament](https://www.stmintz.com/ccc/index.php?id=376346) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), July 13, 2004 » [WCCC 2004](/WCCC_2004 "WCCC 2004")
- [Re: Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?p=2944) by [Mark Uniacke](/Mark_Uniacke "Mark Uniacke"), [Hiarcs Forum](/Computer_Chess_Forums "Computer Chess Forums"), October 14, 2007 » [Search versus Evaluation](/Knowledge#SearchVersusEvaluation "Knowledge"), [1st Computer Olympiad](/1st_Computer_Olympiad#Chess "1st Computer Olympiad")

# External Links

## Chess Engine

- [Woodpusher's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=33)

## Misc

- [woodpusher - Wiktionary](https://en.wiktionary.org/wiki/woodpusher)
- [Glossary of chess - woodpusher, Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_chess#woodpusher)

# References

1. [↑](#cite_ref-1) [Woodpusher's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=33)
2. [↑](#cite_ref-2) Photos by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg")
3. [↑](#cite_ref-3) [Seven Year Itch (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Seven_Year_Itch_%28disambiguation%29)

**[Up one Level](/Engines "Engines")**