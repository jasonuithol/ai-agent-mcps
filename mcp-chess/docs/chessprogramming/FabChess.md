# FabChess

Source: https://www.chessprogramming.org/FabChess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* FabChess**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/%D0%A1%D0%B2%D1%8F%D1%82%D0%BE%D0%B9_%D0%A4%D0%B0%D0%B1%D0%B8%D0%B0%D0%BD_%D0%B8_%D1%81%D0%B2%D1%8F%D1%82%D0%BE%D0%B9_%D0%A1%D0%B5%D0%B1%D0%B0%D1%81%D1%82%D1%8C%D1%8F%D0%BD_%28XV_%D0%B2%D0%B5%D0%BA_%D0%98%D1%81%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F%29.jpg/250px-%D0%A1%D0%B2%D1%8F%D1%82%D0%BE%D0%B9_%D0%A4%D0%B0%D0%B1%D0%B8%D0%B0%D0%BD_%D0%B8_%D1%81%D0%B2%D1%8F%D1%82%D0%BE%D0%B9_%D0%A1%D0%B5%D0%B1%D0%B0%D1%81%D1%82%D1%8C%D1%8F%D0%BD_%28XV_%D0%B2%D0%B5%D0%BA_%D0%98%D1%81%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F%29.jpg)](/File:%D0%A1%D0%B2%D1%8F%D1%82%D0%BE%D0%B9_%D0%A4%D0%B0%D0%B1%D0%B8%D0%B0%D0%BD_%D0%B8_%D1%81%D0%B2%D1%8F%D1%82%D0%BE%D0%B9_%D0%A1%D0%B5%D0%B1%D0%B0%D1%81%D1%82%D1%8C%D1%8F%D0%BD_(XV_%D0%B2%D0%B5%D0%BA_%D0%98%D1%81%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F).jpg)

St. Sebastian and St. Fabian [[1]](#cite_note-1)

**FabChess**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Fabian von der Warth](/index.php?title=Fabian_von_der_Warth&action=edit&redlink=1 "Fabian von der Warth (page does not exist)"), written in [Rust](/Rust "Rust") and first released on [GitHub](https://en.wikipedia.org/wiki/GitHub) in July 2019.
FabChess comes with its own [Wiki](https://en.wikipedia.org/wiki/Wiki), elaborating on programming details [[2]](#cite_note-2).

# Features

[[3]](#cite_note-3)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboard Board-Definition](/Bitboard_Board-Definition "Bitboard Board-Definition")
- [Fancy Magic Bitboards](/Magic_Bitboards#Fancy "Magic Bitboards")
- [BMI2 - PEXT Bitboards](/BMI2#PEXTBitboards "BMI2")

## [Search](/Search "Search")

- [Parallel Search](/Parallel_Search "Parallel Search") using [Threads](/Thread "Thread")
- [Shared Hash Table](/Shared_Hash_Table "Shared Hash Table")
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Staged Move Generation](/Move_Generation#Staged "Move Generation")
  - [Hash Move](/Hash_Move "Hash Move")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
- [Selectivity](/Selectivity "Selectivity")
  - [Check Extensions](/Check_Extensions "Check Extensions")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Static Null Move Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [History Pruning](/History_Leaf_Pruning "History Leaf Pruning")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")

## [Evaluation](/Evaluation "Evaluation")

[[4]](#cite_note-4)

- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [Passed Pawns](/Passed_Pawn "Passed Pawn")
- [Outposts](/Outposts "Outposts")
- [King Safety](/King_Safety "King Safety")
- [Attacking King Zone](/King_Safety#Attacking "King Safety")
- [Tempo](/Tempo "Tempo")
- [Automated Tuning](/Automated_Tuning "Automated Tuning") by [Logistic Regression](/Automated_Tuning#LogisticRegression "Automated Tuning")

# Forum Posts

- [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=242) by [Fabian von der Warth](/index.php?title=Fabian_von_der_Warth&action=edit&redlink=1 "Fabian von der Warth (page does not exist)"), [CCC](/CCC "CCC"), July 16, 2019

:   [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=244) by [Fabian von der Warth](/index.php?title=Fabian_von_der_Warth&action=edit&redlink=1 "Fabian von der Warth (page does not exist)"), [CCC](/CCC "CCC"), July 17, 2019

# External Links

- [GitHub - fabianvdW/FabChess: FabChess](https://github.com/fabianvdW/FabChess)
- [Home · fabianvdW/FabChess Wiki · GitHub](https://github.com/fabianvdW/FabChess/wiki)
- [FabChess](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=FabChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](/CCRL "CCRL")

# References

1. [↑](#cite_ref-1)  Unknown [Spanish Painter](https://en.wikipedia.org/wiki/List_of_Spanish_painters), [St.Sebastian](https://en.wikipedia.org/wiki/Saint_Sebastian) and [St.Fabian](https://en.wikipedia.org/wiki/Pope_Fabian), Late XV century, [Aragonese](https://en.wikipedia.org/wiki/Aragon) School, From the [Shuvalov](https://en.wikipedia.org/wiki/Ivan_Shuvalov) collection, [Hermitage](https://en.wikipedia.org/wiki/Hermitage_Museum), Photo by [George Shuklin](https://commons.wikimedia.org/wiki/User:George_Shuklin), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Home · fabianvdW/FabChess Wiki · GitHub](https://github.com/fabianvdW/FabChess/wiki)
3. [↑](#cite_ref-3) Features based on [FabChess/src at master · fabianvdW/FabChess · GitHub](https://github.com/fabianvdW/FabChess/tree/master/src)
4. [↑](#cite_ref-4) [Evaluation · fabianvdW/FabChess Wiki · GitHub](https://github.com/fabianvdW/FabChess/wiki/Evaluation)

**[Up one Level](/Engines "Engines")**