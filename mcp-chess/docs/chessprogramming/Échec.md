# Échec

Source: https://www.chessprogramming.org/Échec

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Échec**

**Échec**,  
the first chess program by [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot") and [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"). Jean-Christophe Weill already had experience in programing [Othello](/Othello "Othello"), when he decited
to develop a chess program for the upcoming [1st Computer Olympiad](/1st_Computer_Olympiad#Chess "1st Computer Olympiad") in 1989. He found his friend and chess player Marc-François Baudot,
who already made first trials in chess programming, to help him with the [positional evaluation](/Evaluation "Evaluation") to start their successful collaboration.

# Description

## 1st Computer Olympiad

[Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") from his *Short Story* [[1]](#cite_note-1)

```
Our goal was to make a fast tactical program with a very fast but good evaluation function. We chose of course to use the PC/Sq paradigm. The program was using Negascout Search with Killers, History Killers, transposition table. In one month, we had a reasonable prototype. It made it first entire game just 2 days before the begin of the Olympiad, and won convincingly against Cyrus on my PC. Oups, it was giving its pieces for the position so we slow down the positional evaluation. The name of the program was Echec. (Yes, Chess in French is Echecs with a S, but if my French spelling is far better than my English one, it is still really weak. Echec in French is failure !) Well, we had many bugs in the Olympiad but we did not finish the last and eventually we had a draw against Mephisto, not so bad.
```

## Draw by Reputation

[Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") continued from his *Short Story*, see also [WMCCC 1990, Draw by Reputation](/WMCCC_1990#DrawbyReputation "WMCCC 1990")

```
We rapidly then improved Echec and the version 1.5 finished second of the 1990 World Microcomputer Chess Championship. Echec even should have win the tournament since it had a winning position against Mephisto but since our new program Cumulus was having visibly a bad bug and that we were not sure that the Bug was not in common code shared by Echec, we were happy with a draw and set the contempt factor to +4. When Richard Lang saw that, he set Mephisto's Contempt Factor to -2, laughing. Well of course, we were all thinking that Mephisto should win... Mephisto took a poisoned pawn and then came into a losing position. Echec tried to repeat the position, and Mephisto did not want at first but its score went bellow -2 and finally the programs drew !
```

## WMCCC 1991

[Don Beal's](/Don_Beal "Don Beal") [WMCCC 1991](/WMCCC_1991 "WMCCC 1991") report [[2]](#cite_note-2):

```
Written by Marc-François Baudot, in association with Jean-Christophe Weill of Cumulus (they collaborate on ideas and code, but have different programs reflecting their different opinions and experiments. Échec's evaluation function includes piece placement relative to pawn structure, pawn structure itself, taking into account of which major or minor pieces are on the board, mobility, etc. (Marc reports that this was badly tuned, with the result that Échec's positional play was poor in the tournament). Search techniques include check extensions but not singular extensions, plus extensions for some mate threats and promotion.
```

# Tournaments

Échec played following  [Computer Olympiads](/Computer_Olympiad "Computer Olympiad"), [World-](/World_Computer_Chess_Championship "World Computer Chess Championship") and [World Microcomputer Chess Championships](/World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship"). In [Lyon 1990](/WMCCC_1990 "WMCCC 1990"), Échec became strong runner up, and had even chances to tie or win the title, after gaining an almost winning position versus later winner [Mephisto](/Mephisto "Mephisto"), but only managed a [draw by reputation](/WMCCC_1990#DrawbyReputation "WMCCC 1990") with a draw score of four Pawns from [contempt factor](/Contempt_Factor "Contempt Factor"):

| Event | year | Site | standing | points |
| --- | --- | --- | --- | --- |
| [1st Computer Olympiad](/1st_Computer_Olympiad#Chess "1st Computer Olympiad") | 1989 | London | 7 / 9 | 2 / 8 |
| [2nd Computer Olympiad](/2nd_Computer_Olympiad#Chess "2nd Computer Olympiad") | 1990 | London | 5 / 11 | 4 / 6 |
| [WMCCC 1990](/WMCCC_1990 "WMCCC 1990") | 1990 | Lyon | 2 / 12 | 5½ / 7 |
| [WMCCC 1991](/WMCCC_1991 "WMCCC 1991") | 1991 | Vancouver | 10 / 15 | 3½ / 7 |
| [WCCC 1992](/WCCC_1992 "WCCC 1992") | 1992 | Madrid | 19 / 22 | 1½ / 5 |

# External Links

## Chess Program

- [A Short Story of JCW's Computer Chess Program](http://recherche.enac.fr/~weill/chess.html) by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill")
- [Échec's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=229)

## Misc

- [échec - Wiktionary](https://en.wiktionary.org/wiki/%C3%A9chec)

# References

1. [↑](#cite_ref-1) [A Short Story of JCW's Computer Chess Program](http://recherche.enac.fr/~weill/chess.html)
2. [↑](#cite_ref-2) [Don Beal](/Don_Beal "Don Beal") (**1991**). *Report on the [11th World Microcomputer Chess Championship](/WMCCC_1991 "WMCCC 1991")*. [ICCA Journal](/ICGA_Journal "ICGA Journal"), Vol. 14, No. 2

**[Up one Level](/Engines "Engines")**