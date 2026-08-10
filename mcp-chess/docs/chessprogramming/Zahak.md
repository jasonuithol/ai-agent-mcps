# Zahak

Source: https://www.chessprogramming.org/Zahak

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Zahak**

[![](/images/8/85/Zahak_logo.jpg)](/File:Zahak_logo.jpg)

Zahak's Logo [[1]](#cite_note-1) - Designed by Nasrin Zaza [[2]](#cite_note-2)

**Zahak**,  
a [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Amanj Sherwany](/Amanj_Sherwany "Amanj Sherwany"), written in [Go](/Go "Go"), licensed under the [MIT License](/Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") and first released on [GitHub](https://en.wikipedia.org/wiki/GitHub) in February 2021 [[3]](#cite_note-3).
Since version 7, Zahak's hand crafted  [evaluation function](/Evaluation_Function "Evaluation Function") is replaced with an  [NNUE style](/NNUE "NNUE") evaluation, which is trained by a from scratch written trainer, that is written in [Go](/Go "Go") as well [[4]](#cite_note-4). The network is trained on self-play games between different versions of Zahak. As of version 8, Zahak features an own network architecture which consists of 769 input features, that represents all the pieces on the board as well as a feature to represent white-to-move. The training process is thoroughly documented [[5]](#cite_note-5). As of the time of this writing, Zahak is the only [NNUE](/NNUE "NNUE") engine that is written in [Go](/Go "Go").

Zahak started its first debut in [TCEC](/TCEC "TCEC") in Swiss 2 event of S21 [[6]](#cite_note-6).

# Etymology

Zahak (or Zahhak or Azhi Dahak) is an evil figure in Iranian/Kurdish/Perisan mythology, evident in ancient Iranian folklore as Azhi Dahāka, the name by which he also appears in the texts of the Avesta. Legend has it, that he had two giant snakes on his shoulders and he had to feed them two human brains on daily basis [[7]](#cite_note-7).

# Features

[[8]](#cite_note-8)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") for sliding pieces.
- Multi-Stage Pseudo-Legal [Move Generation](/Move_Generation "Move Generation")

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Lazy SMP](/Lazy_SMP "Lazy SMP")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
  - [Shared Hash Table](/Shared_Hash_Table "Shared Hash Table")
  - [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") for [Captures](/Captures "Captures")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic")
- [Selectivity](/Selectivity "Selectivity")
  - [Check Extensions](/Check_Extensions "Check Extensions")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")
  - [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") based Pruning
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Late Move Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")

## [Evaluation](/Evaluation "Evaluation")

- [NNUE](/NNUE "NNUE") (>= Zahak 7)

## Misc

- [PolyGlot](/PolyGlot "PolyGlot") [Opening Book](/Opening_Book "Opening Book")
- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")
- [MultiPV](/Principal_Variation#MultiPV "Principal Variation")
- [Skill Levels](/Playing_Strength "Playing Strength")

# Forum Posts

- [Zahak, a GoLang based chess engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76855) by [Amanj Sherwany](/Amanj_Sherwany "Amanj Sherwany"), [CCC](/CCC "CCC"), March 13, 2021

# External Links

## Chess Engine

- [GitHub - amanjpro/zahak: A UCI compatible chess AI in Go](https://github.com/amanjpro/zahak)
- [Zahak in CCRL 40/15](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Zahak&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents)

## Misc

- [Zahhak from Wikipedia](https://en.wikipedia.org/wiki/Zahhak)

# References

1. [↑](#cite_ref-1) [GitHub - amanjpro/zahak: A UCI compatible chess AI in Go - Name](https://github.com/amanjpro/zahak#zahak)
2. [↑](#cite_ref-2) [Nasrin Zaza · LinkedIn Profile](https://www.linkedin.com/in/nasrin-zaza)
3. [↑](#cite_ref-3) [Release Zahak 0.0.1 · amanjpro/zahak · GitHub](https://github.com/amanjpro/zahak/releases/tag/0.0.1)
4. [↑](#cite_ref-4) [amanjpro/zahak-trainer · GitHub](https://github.com/amanjpro/zahak-trainer)
5. [↑](#cite_ref-5) [Training Documentation · amanjpro/zahak · GitHub](https://github.com/amanjpro/zahak/blob/master/training.md)
6. [↑](#cite_ref-6) [TCEC Swiss 2 Wiki](https://wiki.chessdom.org/TCEC_Swiss_2)
7. [↑](#cite_ref-7) [Zahhak from Wikipedia](https://en.wikipedia.org/wiki/Zahhak)
8. [↑](#cite_ref-8) Features based on [README.md · amanjpro/zahak · GitHub](https://github.com/amanjpro/zahak#implemented-features)

**[Up one level](/Engines "Engines")**