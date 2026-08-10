# Fizbo

Source: https://www.chessprogramming.org/Fizbo

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Fizbo**

**Fizbo**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), and since version **1.5**, [UCI](/UCI "UCI") compliant [[1]](#cite_note-1) chess engine by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine") - in October 2019 [Fizbo 2](#Fizbo_2) became [open source](/Category:Open_Source "Category:Open Source"). Fizbo was first released in May 2014 [[2]](#cite_note-2), apparently [bitboard](/Bitboards "Bitboards") based, requiring [x86-64](/X86-64 "X86-64") [bitscan forward](/BitScan#bsfbsr "BitScan") [[3]](#cite_note-3) and taking advantage from [population count](/Population_Count "Population Count") [instruction](/X86-64#gpinstructions "X86-64"). Since version **1.2**, Fizbo performs a [parallel search](/Parallel_Search "Parallel Search") based on a version of enhanced [PV splitting algorithm](/Parallel_Search#PrincipalVariationSplitting "Parallel Search"), only one split-point is active at a time, along with [iterative deepening](/Iterative_Deepening "Iterative Deepening"), since **1.3** with [aspiration windows](/Aspiration_Windows "Aspiration Windows"). [Syzygy Bases](/Syzygy_Bases "Syzygy Bases") with up to five pieces were used since version **1.4** released in May 2015. The [transposition table](/Transposition_Table "Transposition Table") with dense 8 byte entries is used also in [quiescence search](/Quiescence_Search "Quiescence Search") [[4]](#cite_note-4).

# Further Versions

## Fizbo 1.7

Fizbo **1.7**, released in March 2016, improved in [evaluation](/Evaluation "Evaluation") due to changed and new features, including [pawn pattern](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties"), considering all possible combinations of two pawns of the same color [[5]](#cite_note-5), and further supports 6-piece [Syzygy Bases](/Syzygy_Bases "Syzygy Bases").

## Fizbo 1.8

Fizbo **1.8** in August 2016 came with a [BMI2](/BMI2 "BMI2") executable, improved [pondering](/Pondering "Pondering") logic, reworked parallel search logic, and multiple small changes to [search](/Search "Search") and [evaluation](/Evaluation "Evaluation") [[6]](#cite_note-6).

## Fizbo 1.9

Fizbo **1.9**, released on December 31, 2016, further enhanced considerably due to extensive changes and new features in [evaluation](/Evaluation "Evaluation") [[7]](#cite_note-7).

## Fizbo 2

Fizbo **2** was released in December 21, 2017 [[8]](#cite_note-8), and is apparently the last version by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), who stopped working on the engine, and decided to release his source code on [GitHub](https://en.wikipedia.org/wiki/GitHub) [[9]](#cite_note-9) [[10]](#cite_note-10) nearly two years later, featuring a two-layer [neural network](/Neural_Networks "Neural Networks") based [evaluation](/Evaluation "Evaluation") with optional [AVX2](/AVX2 "AVX2") intrinsics [[11]](#cite_note-11).

# Forum Posts

## 2014

- [new engine - Fizbo - could you please test it?](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=7523) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), May 07, 2014
- [Fizbo 1.1](http://www.talkchess.com/forum/viewtopic.php?t=52270) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), May 09, 2014
- [new version of Fizbo engine released](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=7668) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), July 28, 2014
- [Fizbo version 1.3 is released](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=7826) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), November 11, 2014
- [Fizbo 1.3 released](http://www.talkchess.com/forum/viewtopic.php?t=54318) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), November 12, 2014

## 2015

- [Fizbo version 1.4 released](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=8113) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), May 18, 2015
- [Fizbo 1.4 released](http://www.talkchess.com/forum/viewtopic.php?t=56408) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), May 18, 2015
- [Fizbo version 1.5 released](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=8241) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), August 16, 2015
- [Fizbo version 1.5 released](http://www.talkchess.com/forum/viewtopic.php?t=57288) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), August 16, 2015

## 2016

- [Fizbo version 1.6 released](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=8460) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), January 29, 2016
- [Fizbo 1.6 released](http://www.talkchess.com/forum/viewtopic.php?t=59101) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), January 29, 2016
- [Fizbo 1.7 is released](http://www.talkchess.com/forum/viewtopic.php?t=59608) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), March 23, 2016
- [Fizbo 1.8 released](http://www.talkchess.com/forum/viewtopic.php?t=61243) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), August 26, 2016
- [Fizbo 1.9 released](http://www.talkchess.com/forum/viewtopic.php?t=62677) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), December 31, 2016

## 2017 ...

- [Re: Tapered Eval between 4 phases](http://www.talkchess.com/forum3/viewtopic.php?t=65466&start=7) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), October 16, 2017 » [Tapered Eval](/Tapered_Eval "Tapered Eval"), [AVX](/AVX "AVX")
- [Fizbo 2 has been released](http://www.talkchess.com/forum/viewtopic.php?t=66090) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), December 21, 2017
- [Fizbo 2 sources just got released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72021) by Damir, [CCC](/CCC "CCC"), October 06, 2019

## 2020 ...

- [Bug in Fizbo 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73769) by [Kurt Utzinger](/Kurt_Utzinger "Kurt Utzinger"), [CCC](/CCC "CCC"), April 26, 2020

# External Links

## Chess Engine

- [GitHub - MoonstoneLight/Fizbo-Chess: Original codes of Fizbo Chess](https://github.com/MoonstoneLight/Fizbo-Chess). Thanks to original author [Youri Matiounine](/Youri_Matiounine "Youri Matiounine")
- [Fizbo Chess Engine](https://sites.google.com/site/fizbochessengine/)
- [Fizbo](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Fizbo&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](/CCRL "CCRL")
- [Fizbo](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Fizbo&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [fizbo - Wiktionary](https://en.wiktionary.org/wiki/fizbo)
- [Fizbo from Wikipedia](https://en.wikipedia.org/wiki/Fizbo)

# References

1. [↑](#cite_ref-1) [Fizbo version 1.5 released](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=8241) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), August 16, 2015
2. [↑](#cite_ref-2) [new engine - Fizbo - could you please test it?](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=7523) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), May 07, 2014
3. [↑](#cite_ref-3) [new engine - Fizbo - could you please test it?](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=7523) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), May 07, 2014
4. [↑](#cite_ref-4) [Fizbo Chess Engine](https://sites.google.com/site/fizbochessengine/)
5. [↑](#cite_ref-5) [Re: Fizbo 1.7 is released](http://www.talkchess.com/forum/viewtopic.php?t=59608&start=3) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), March 23, 2016
6. [↑](#cite_ref-6) [Fizbo 1.8 released](http://www.talkchess.com/forum/viewtopic.php?t=61243) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), August 26, 2016
7. [↑](#cite_ref-7) [Fizbo 1.9 released](http://www.talkchess.com/forum/viewtopic.php?t=62677) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), December 31, 2016
8. [↑](#cite_ref-8) [Fizbo 2 has been released](http://www.talkchess.com/forum/viewtopic.php?t=66090) by [Youri Matiounine](/Youri_Matiounine "Youri Matiounine"), [CCC](/CCC "CCC"), December 21, 2017
9. [↑](#cite_ref-9) [Fizbo 2 sources just got released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72021) by Damir, [CCC](/CCC "CCC"), October 06, 2019
10. [↑](#cite_ref-10) [GitHub - MoonstoneLight/Fizbo-Chess: Original codes of Fizbo Chess](https://github.com/MoonstoneLight/Fizbo-Chess). Thanks to original author [Youri Matiounine](/Youri_Matiounine "Youri Matiounine")
11. [↑](#cite_ref-11) [Fizbo-Chess/nn2.cpp at master · MoonstoneLight/Fizbo-Chess · GitHub](https://github.com/MoonstoneLight/Fizbo-Chess/blob/master/nn2.cpp)

**[Up one Level](/Engines "Engines")**