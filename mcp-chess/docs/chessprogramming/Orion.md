# Orion

Source: https://www.chessprogramming.org/Orion

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Orion**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Orion_3008_huge.jpg/250px-Orion_3008_huge.jpg)](/File:Orion_3008_huge.jpg)

Orion Constellation [[1]](#cite_note-1)

**Orion**,  
an [UCI](/UCI "UCI") compliant chess engine by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), written in [C](/C "C") and first released in May 2014.
In August 2020, David Carteau published results using an own [AVX2](/AVX2 "AVX2") [NNUE](/NNUE "NNUE") implementation, initially compatible with [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE") nets,
with a huge improvement in [playing strength](/Playing_Strength "Playing Strength") [[2]](#cite_note-2). He has designed and trained his own NNUE-like approach published as [Cerebrum](/index.php?title=Cerebrum&action=edit&redlink=1 "Cerebrum (page does not exist)") open source library on [GitHub](https://en.wikipedia.org/wiki/GitHub) [[3]](#cite_note-3), first used within **Orion 0.8**, released in December 2020 [[4]](#cite_note-4).

# Features

[[5]](#cite_note-5)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Plain Magic Bitboards](/Magic_Bitboards#Plain "Magic Bitboards")
- [BMI2 - PEXT Bitboards](/BMI2#PEXTBitboards "BMI2")

## [Search](/Search "Search")

- [Lazy SMP](/Lazy_SMP "Lazy SMP") (0.9)
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Selectivity](/Selectivity "Selectivity")
  - [Adaptive Null Move Pruning](/Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
  - [Static Null Move Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Razoring](/Razoring "Razoring")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")
  - [SEE Pruning](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move"), even [Quiet Moves](/Quiet_Moves "Quiet Moves") in [Quiescence](/Quiescence_Search "Quiescence Search")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [History Heuristic](/History_Heuristic "History Heuristic")

## [Evaluation](/Evaluation "Evaluation")

- [NNUE](/NNUE "NNUE") (0.7.nnue)
- [NNUE](/NNUE "NNUE")-like [Cerebrum](/index.php?title=Cerebrum&action=edit&redlink=1 "Cerebrum (page does not exist)") (0.8)
- [Automated Tuning](/Automated_Tuning "Automated Tuning") by [Linear Regression](/Automated_Tuning#LinearRegression "Automated Tuning") using [Python](/Python "Python") [scikit-learn](https://en.wikipedia.org/wiki/Scikit-learn) (0.6) [[6]](#cite_note-6)
- [Automated Tuning](/Automated_Tuning "Automated Tuning") by [PBIL](/Genetic_Programming#PBIL "Genetic Programming") (pre 0.6)
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Isolated Pawns](/Isolated_Pawn "Isolated Pawn") etc ...
  - [Passed Pawns](/Passed_Pawn "Passed Pawn")
- [Mobility](/Mobility "Mobility")
- [Square Control](/Square_Control "Square Control")
- [Space](/Space "Space")
- [King Safety](/King_Safety "King Safety")
- [Attacking King Zone](/King_Safety#Attacking "King Safety")

## Misc

- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases") (removed in 0.8)

# Forum Posts

## 2014 ...

- [New free engine - Orion](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=52414) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), May 24, 2014
- [New Orion release : v0.3 !](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=59736) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), April 03, 2016
- [New Orion release : v0.4 !](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65455) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), October 15, 2017
- [New Orion release : v0.5 !](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67786) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), June 21, 2018
- [New Orion release : v0.6 !](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70887) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), June 01, 2019

## 2020 ...

- [Orion 0.7 release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74365) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), July 04, 2020
- [Orion 0.7 : NNUE experiment](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74828) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), August 19, 2020
- [Re: You've trained a brilliant NN(UE) King-Piece Network. Now what?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75870&start=19) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), November 19, 2020 » [NNUE](/NNUE "NNUE")
- [Orion 0.8 + The Cerebrum release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75953) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), December 01, 2020
- [Orion 0.9 release](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79673) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), April 12, 2022

# External Links

## Chess Engine

- [Orion UCI chess engine](https://orionchess.pagesperso-orange.fr/)
- [GitHub - david-carteau/cerebrum: The Cerebrum library](https://github.com/david-carteau/cerebrum)
- [Orion (Schachprogramm) – Wikipedia.de](https://de.wikipedia.org/wiki/Orion_(Schachprogramm)) (German)
- [Orion](http://computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Orion&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")

## Misc

- [Orion from Wikipedia](https://en.wikipedia.org/wiki/Orion)
- [Orion (mythology) from Wikipedia](https://en.wikipedia.org/wiki/Orion_(mythology))
- [Orion (constellation) from Wikipedia](https://en.wikipedia.org/wiki/Orion_(constellation))
- [Orion (comics) from Wikipedia](https://en.wikipedia.org/wiki/Orion_(comics))
- [Orion (sculpture) from Wikipedia](https://en.wikipedia.org/wiki/Orion_(sculpture)) » [University of Michigan](/University_of_Michigan "University of Michigan")
- [Steps Ahead](/Category:Steps_Ahead "Category:Steps Ahead") - Orion, [Yin-Yang](https://www.discogs.com/de/Steps-Ahead-Yin-Yang/release/2727533) (1992), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   lineup: [Mike Mainieri](/Category:Mike_Mainieri "Category:Mike Mainieri"), [Steve Smith](/Category:Steve_Smith "Category:Steve Smith"), [Jeff Andrews](https://www.discogs.com/de/artist/486643-Jeff-Andrews), [Bendik Hofseth](https://en.wikipedia.org/wiki/Bendik_Hofseth), [Rachel Z](https://en.wikipedia.org/wiki/Rachel_Z)

# References

1. [↑](#cite_ref-1) [deep sky image](https://commons.wikimedia.org/wiki/File:Orion_3008_huge.jpg) of the constellation [Orion](https://en.wikipedia.org/wiki/Orion_(constellation)) by [Mouser](https://en.wikipedia.org/wiki/User:Mouser), December 14, 2004, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Orion 0.7 : NNUE experiment](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74828) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), August 19, 2020
3. [↑](#cite_ref-3) [GitHub - david-carteau/cerebrum: The Cerebrum library](https://github.com/david-carteau/cerebrum)
4. [↑](#cite_ref-4) [Orion 0.8 + The Cerebrum release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75953) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), December 01, 2020
5. [↑](#cite_ref-5) based on [Orion UCI chess engine](https://orionchess.pagesperso-orange.fr/)
6. [↑](#cite_ref-6) [1.1. Linear Models — scikit-learn 0.23.2 documentation](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification)

**[Up one level](/Engines "Engines")**