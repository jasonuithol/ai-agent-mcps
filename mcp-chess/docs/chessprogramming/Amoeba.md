# Amoeba

Source: https://www.chessprogramming.org/Amoeba

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Amoeba**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Nelder-Mead_Simionescu.gif/330px-Nelder-Mead_Simionescu.gif)](/File:Nelder-Mead_Simionescu.gif)

[Amoeba search](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) of [Simionescu function](https://en.wikipedia.org/wiki/Test_functions_for_optimization) [[1]](#cite_note-1)

**Amoeba**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Richard Delorme](/Richard_Delorme "Richard Delorme"), written in the [D programming language](/D_(Programming_Language) "D (Programming Language)"), first released in May 2016 [[2]](#cite_note-2), licensed under the [GPL v3.0](/Free_Software_Foundation#GPL "Free Software Foundation"). Amoeba uses the [Nelder–Mead method](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) [[3]](#cite_note-3) or downhill simplex method [[4]](#cite_note-4) to [tune](/Automated_Tuning "Automated Tuning") its [evaluation](/Evaluation "Evaluation") parameters, also called **amoeba** method and eponym of the program [[5]](#cite_note-5).

# Features

[[6]](#cite_note-6)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence") and [Rank Attacks](/First_Rank_Attacks#AttacksOnAllRanks "First Rank Attacks")
- [Mailbox](/Mailbox "Mailbox")
- [Staged Move Generation](/Move_Generation#Staged "Move Generation")

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows") (improved in 2.6)
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table") (improved in 2.6)
- [Check Extensions](/Check_Extensions "Check Extensions")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
- [Razoring](/Razoring "Razoring")
- [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions") (improved in 2.6)
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation") (SEE pruning improved in 2.6)

## [Evaluation](/Evaluation "Evaluation")

- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Lazy Evaluation](/Lazy_Evaluation "Lazy Evaluation")
- [Mobility](/Mobility "Mobility")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [Tempo](/Tempo "Tempo")
- [Automated Tuning](/Automated_Tuning "Automated Tuning") using [Nelder–Mead method](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) aka Amoeba method

## [Tournament Manager](/Tournament_Manager "Tournament Manager")

:   With the release of Amoeba **2.1**, the code of a tournament manager was published also written in [D language](/D_(Programming_Language) "D (Programming Language)"), used to validate or reject Amoeba changes [[7]](#cite_note-7). So far only with fixed time per move, it

- can use various [openings](/Opening_Book "Opening Book") from [pgn file](/Portable_Game_Notation "Portable Game Notation")
- can play several games in parallel
- can set H0 & H1 [hypothesis](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing) for [SPRT](/Match_Statistics#SPRT "Match Statistics") [[8]](#cite_note-8)
- can saves played game to a pgn file

# See also

- [Dumb](/Dumb "Dumb")

# Forum Posts

## 2016 ...

- [amoeba a new UCI engine](http://www.talkchess.com/forum/viewtopic.php?t=60228) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), May 20, 2016
- [Amoeba 1.3 released](http://www.talkchess.com/forum/viewtopic.php?t=61022) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), August 03, 2016
- [Amoeba 2.0](http://www.talkchess.com/forum/viewtopic.php?t=62293) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), November 27, 2016
- [amoeba 2.1](http://www.talkchess.com/forum/viewtopic.php?t=62921) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), January 24, 2017
- [sprt tourney manager](http://www.talkchess.com/forum/viewtopic.php?t=62922) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), January 24, 2017 » [Amoeba Tournament Manager](#TournamentManager), [SPRT](/Match_Statistics#SPRT "Match Statistics")
- [amoeba 2.2 released](http://www.talkchess.com/forum/viewtopic.php?t=63324) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [CCC](/CCC "CCC"), March 03, 2017
- [Amoeba 2.4](http://www.talkchess.com/forum/viewtopic.php?t=63775) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), April 19, 2017
- [Amoeba 2.5](http://www.talkchess.com/forum/viewtopic.php?t=64212) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), June 07, 2017
- [Amoeba 2.6](http://www.talkchess.com/forum/viewtopic.php?t=65255) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), September 22, 2017
- [Amoeba 2.7](http://www.talkchess.com/forum/viewtopic.php?t=65981) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), December 11, 2017
- [Amoeba 2.8](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66877) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), March 18, 2018
- [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=60) (Amoeba 3.0) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), March 28, 2019

## 2020 ...

- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=41) (Amoeba 3.1) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), January 16, 2020
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=284) (Amoeba 3.2) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), July 25, 2020
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=140) (Amoeba 3.3) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), March 14, 2021
- [Re: New engine releases & news 2021](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=950) (Amoeba 3.4) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), December 16, 2021

# External Links

## Chess Engine

- [GitHub - abulmo/amoeba: an UCI chess engine in d language](https://github.com/abulmo/amoeba)
- [Amoeba](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Amoeba&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Amoeba from Wikipedia](https://en.wikipedia.org/wiki/Amoeba)
- [amoeba - Wiktionary](https://en.wiktionary.org/wiki/amoeba)
- [Amoeba (genus) from Wikipedia](https://en.wikipedia.org/wiki/Amoeba_(genus))
- [Amoeba (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Amoeba_(disambiguation))
- [Amoeba (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Amoeba_(mathematics))

# References

1. [↑](#cite_ref-1) Animated [Nelder-Mead minimum search](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) of [Simionescu function](https://en.wikipedia.org/wiki/Test_functions_for_optimization), by Pasimi, November 22, 2016, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [amoeba a new UCI engine](http://www.talkchess.com/forum/viewtopic.php?t=60228) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), May 20, 2016
3. [↑](#cite_ref-3) [John Nelder](https://en.wikipedia.org/wiki/John_Nelder), [Roger Mead](https://de.wikipedia.org/wiki/Roger_Mead) (**1965**). *A Simplex Method for Function Minimization*. [The Computer Journal](https://en.wikipedia.org/wiki/The_Computer_Journal), Vol. 7, No. 4, doi:[10.1093/comjnl/7.4.308](http://comjnl.oxfordjournals.org/content/7/4/308)
4. [↑](#cite_ref-4) [Margaret H. Wright](/Mathematician#MHWright "Mathematician") (**2012**). *Nelder, Mead, and the Other Simplex Method*. [Documenta Mathematica](https://www.math.uni-bielefeld.de/documenta/Welcome-eng.html), [Extra Volume Optimization Stories](https://www.math.uni-bielefeld.de/documenta/vol-ismp/vol-ismp.html), [pdf](http://www.math.uiuc.edu/documenta/vol-ismp/42_wright-margaret.pdf)
5. [↑](#cite_ref-5) [amoeba/README.md at master · abulmo/amoeba · GitHub](https://github.com/abulmo/amoeba/blob/master/README.md)
6. [↑](#cite_ref-6) Features as mentioned in [amoeba/README.md at master · abulmo/amoeba · GitHub](https://github.com/abulmo/amoeba/blob/master/README.md)
7. [↑](#cite_ref-7) [sprt tourney manager](http://www.talkchess.com/forum/viewtopic.php?t=62922) by [Richard Delorme](/Richard_Delorme "Richard Delorme"), [CCC](/CCC "CCC"), January 24, 2017
8. [↑](#cite_ref-8) [The SPRT without draw model, elo model or whatever...](http://www.talkchess.com/forum/viewtopic.php?t=57465) by [Michel Van den Bergh](/Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](/CCC "CCC"), September 01, 2015

**[Up one Level](/Engines "Engines")**