# Koivisto

Source: https://www.chessprogramming.org/Koivisto

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Koivisto**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Hjalmar_Munsterhjelm_-_Koivikko_ja_ruispelto_-_A_II_1169_-_Finnish_National_Gallery.jpg/330px-Hjalmar_Munsterhjelm_-_Koivikko_ja_ruispelto_-_A_II_1169_-_Finnish_National_Gallery.jpg)](/File:Hjalmar_Munsterhjelm_-_Koivikko_ja_ruispelto_-_A_II_1169_-_Finnish_National_Gallery.jpg)

[Hjalmar Munsterhjelm](/Category:Hjalmar_Munsterhjelm "Category:Hjalmar Munsterhjelm") - Koivikko ja ruispelto [[1]](#cite_note-1)

**Koivisto**,  
an [UCI](/UCI "UCI") compliant [open source](/Category:Open_Source "Category:Open Source") chess engine by [Kim Kåhre](/Kim_K%C3%A5hre "Kim Kåhre") and [Finn Eggers](/Finn_Eggers "Finn Eggers"), at times supported by [Eugenio Bruno](/index.php?title=Eugenio_Bruno&action=edit&redlink=1 "Eugenio Bruno (page does not exist)"), written in [C++](/Cpp "Cpp"),
and first released on [GitHub](https://en.wikipedia.org/wiki/GitHub) in September 2020 under the [GPL v3.0](/Free_Software_Foundation#GPL "Free Software Foundation").
The [bitboard](/Bitboards "Bitboards") engine provides [automated evaluation tuning](/Automated_Tuning "Automated Tuning") by [logistic regression](/Automated_Tuning#LogisticRegression "Automated Tuning"),
either using [stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) or [AdaGrad](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad).
Koivisto **5.0** in July 2021 replaced the [perceptron](/Neural_Networks#Perceptron "Neural Networks") approach of a real-men-evaluation (RME) by an own [NNUE](/NNUE "NNUE"), as of Koivisto **5.9**, with two layers [[2]](#cite_note-2).

# Features

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")

## [Search](/Search "Search")

- [Lazy SMP](/Lazy_SMP "Lazy SMP") (2.0)
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows") (3.0)
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Counter Moves History](/History_Heuristic#CMHist "History Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [MVV/LVA](/MVV-LVA "MVV-LVA")
  - [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Selectivity](/Selectivity "Selectivity")
  - [Extensions](/Extensions "Extensions")
    - [Check Extensions](/Check_Extensions "Check Extensions") if [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") >= 0
    - [Singular Extensions](/Singular_Extensions "Singular Extensions")
  - [Reductions](/Reductions "Reductions")
    - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
    - [Razoring](/Razoring "Razoring")
  - [Pruning](/Pruning "Pruning")
    - [Futility Pruning](/Futility_Pruning "Futility Pruning")
    - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
    - [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
    - [Late Move Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
    - [SEE Pruning](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")

## [Evaluation](/Evaluation "Evaluation")

- [NNUE](/NNUE "NNUE") (5.0)
- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables") of [floats](/Float "Float")
- [Mobility](/Mobility "Mobility")
  - [Bad Bishop](/Bad_Bishop "Bad Bishop")
  - [Rooks on (Semi) Open Files](/Rook_on_Open_File "Rook on Open File")
- [Tactical Patterns](/Tactics "Tactics")
  - [Hanging Pieces](/Hanging_Piece "Hanging Piece")
  - [Pinned Pieces](/Pin "Pin")
- [Evaluation Patterns](/Evaluation_Patterns "Evaluation Patterns")
  - [Outposts](/Outposts "Outposts")
  - [Fianchetto](/Fianchetto "Fianchetto")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
  - [Passed Pawn](/Passed_Pawn "Passed Pawn")
  - [Blockade of Stop](/Blockade_of_Stop "Blockade of Stop") (3.0)
  - [Backward Pawns](/Backward_Pawns_(Bitboards) "Backward Pawns (Bitboards)")
  - [Open Pawns](/Open_Pawns_(Bitboards) "Open Pawns (Bitboards)")
- [King Safety](/King_Safety "King Safety")
  - [Attacking King Zone](/King_Safety#Attacking "King Safety")
  - [King Tropism](/King_Safety#KingTropism "King Safety")
  - [Castling Rights](/Castling_Rights "Castling Rights") (3.0)
- [Tempo](/Tempo "Tempo") (3.0)
- [Draw Evaluation](/Draw_Evaluation "Draw Evaluation") (3.0)
- [Float](/Float "Float") [SSE](/SSE "SSE") [Dot products](https://en.wikipedia.org/wiki/Dot_product) [[3]](#cite_note-3)
- [Automated Tuning](/Automated_Tuning "Automated Tuning") by [Logistic Regression](/Automated_Tuning#LogisticRegression "Automated Tuning")

## Misc

- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases") via [Fathom](/Syzygy_Bases#Fathom "Syzygy Bases")

# Forum Posts

## 2020

- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=353) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), September 02, 2020

:   [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=357) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), September 03, 2020

- [Koivisto](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75001) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), September 04, 2020

:   [Re: Koivisto](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75001&start=4) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), September 04, 2020

- [Koivisto 2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75052) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), September 08, 2020
- [Koivisto 3.0 (Including binaries)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75423) by [Kim Kåhre](/Kim_K%C3%A5hre "Kim Kåhre"), [CCC](/CCC "CCC"), October 17, 2020
- [Koivisto v4.0 release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75742) by [Eugenio Bruno](/index.php?title=Eugenio_Bruno&action=edit&redlink=1 "Eugenio Bruno (page does not exist)"), [CCC](/CCC "CCC"), November 09, 2020

## 2021

- [Koivisto 5.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77664) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), July 07, 2021
- [Koivisto 6.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77766) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), July 21, 2021
- [Koivisto 7.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78560) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), October 31, 2021

## 2022

- [Koivisto 8.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79523) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), March 15, 2022

# External Links

## Chess Engine

- [GitHub - Luecx/Koivisto: UCI Chess engine](https://github.com/Luecx/Koivisto)
  - [Evaluation · Luecx/Koivisto Wiki · GitHub](https://github.com/Luecx/Koivisto/wiki/Evaluation)
  - [Regression tests · Luecx/Koivisto Wiki · GitHub](https://github.com/Luecx/Koivisto/wiki/Regression-tests)
- [Koivisto Chess](https://koivisto-chess.com/)
- [Koivisto](https://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Koivisto&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [Koivisto - Wiktionary](https://en.wiktionary.org/wiki/Koivisto)

:   [koivikko - Wiktionary](https://en.wiktionary.org/wiki/koivikko)

- [Koivisto from Wikipedia](https://en.wikipedia.org/wiki/Koivisto)
- [Koivisto (surname) from Wikipedia](https://en.wikipedia.org/wiki/Koivisto_(surname))

# References

1. [↑](#cite_ref-1) [Hjalmar Munsterhjelm](/Category:Hjalmar_Munsterhjelm "Category:Hjalmar Munsterhjelm") - Koivikko ja ruispelto (Birch and rye field), 1876, [Finnish National Gallery](https://en.wikipedia.org/wiki/Finnish_National_Gallery), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Evaluation · Luecx/Koivisto Wiki · GitHub](https://github.com/Luecx/Koivisto/wiki/Evaluation)
3. [↑](#cite_ref-3) [Dot products](https://en.wikipedia.org/wiki/Dot_product) using [\_mm\_mul\_ps](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=_mm_mul_ps&expand=3928), [\_mm\_add\_ps](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=_mm_add_ps&expand=3928,133)

**[Up one Level](/Engines "Engines")**