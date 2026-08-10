# Nalwald

Source: https://www.chessprogramming.org/Nalwald

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Nalwald**

[![](/images/thumb/d/d8/Nalwald_logo.png/300px-Nalwald_logo.png)](/File:Nalwald_logo.png)

Nalwald logo [[1]](#cite_note-1)

**Nalwald**,  
an [UCI](/UCI "UCI") compatible [open source chess engine](/Category:Open_Source "Category:Open Source") by [Jost Triller](/Jost_Triller "Jost Triller"),
written in the [Nim programming language](/Nim_(Programming_Language) "Nim (Programming Language)") [[2]](#cite_note-2),
first released in April 2021 [[3]](#cite_note-3).
Nalwald is a [bitboard](/Bitboards "Bitboards") engine and generates [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") [Kindergarten](/Kindergarten_Bitboards "Kindergarten Bitboards") like,
by looking up four pre-calculated line attack arrays, 32-Kbyte each, indexed by square and [inner six bit](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks") [line occupancy](/Occupancy_of_any_Line "Occupancy of any Line") [[4]](#cite_note-4).
Nalwald uses alpha-beta for search and a BAE (big array evaluation) for evaluating leaf nodes.

# Features

[[5]](#cite_note-5)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards")

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Lazy SMP](/Lazy_SMP "Lazy SMP")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Selectivity](/Selectivity "Selectivity")
  - [Null Move Reductions](/Null_Move_Reductions "Null Move Reductions")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Check Extensions](/Check_Extensions "Check Extensions")
  - [Futility Reductions](/Futility_Pruning "Futility Pruning")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")

## [Evaluation](/Evaluation "Evaluation")

- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- Piece-relative [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- 3x3 pawn structure tables
- Piece combinations
- [Passed Pawns](/Passed_Pawn "Passed Pawn")
- [Evaluation Tuning](/Automated_Tuning "Automated Tuning") using [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent)

# See also

- [Googleplex Starthinker](/Googleplex_Starthinker "Googleplex Starthinker")
- [Hactar](/Hactar "Hactar")

# Forum Posts

- [Nalwald: Chess engine written in Nim](https://www.reddit.com/r/nim/comments/myfjx6/nalwald_chess_engine_written_in_nim/) by [Jost Triller](/Jost_Triller "Jost Triller"), [Reddit](/Computer_Chess_Forums "Computer Chess Forums"), April 25, 2021
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=328) (Nalwald 1.8.1) by [Tony Mokonen](/index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](/CCC "CCC"), May 08, 2021
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=419) (Nalwald 1.9) by [Jost Triller](/Jost_Triller "Jost Triller"), [CCC](/CCC "CCC"), June 16, 2021
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=468) (Nalwald 1.10) by [Jost Triller](/Jost_Triller "Jost Triller"), [CCC](/CCC "CCC"), July 03, 2021
- [Nalwald](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78198) by [Jost Triller](/Jost_Triller "Jost Triller"), [CCC](/CCC "CCC"), September 17, 2021
- [Re:Nalwald](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78198&start=3) by [Jost Triller](/Jost_Triller "Jost Triller"), [CCC](/CCC "CCC"), February 08, 2022

# External Links

## Chess Engine

- [tsoj / Nalwald · GitHub](https://github.com/tsoj/Nalwald)
- [Nalwald](https://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Nalwald&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")

## Misc

- [Nalwald | PaxCalradica Wiki | Fandom](https://paxcalradica.fandom.com/wiki/Nalwald)

# References

1. [↑](#cite_ref-1) Nalwald logo based on [banner.png · master · tsoj / Nalwald · GitHub](https://repository-images.githubusercontent.com/827023648/427f752f-633f-4e2d-ad79-db40141368ff)
2. [↑](#cite_ref-2) [Nim programming language from Wikipedia](https://en.wikipedia.org/wiki/Nim_(programming_language))
3. [↑](#cite_ref-3) [Nalwald: Chess engine written in Nim](https://www.reddit.com/r/nim/comments/myfjx6/nalwald_chess_engine_written_in_nim/) by [Jost Triller](/Jost_Triller "Jost Triller"), [Reddit](/Computer_Chess_Forums "Computer Chess Forums"), April 25, 2021
4. [↑](#cite_ref-4) [bitboard.nim · master · tsoj / Nalwald · GitHub](https://github.com/tsoj/Nalwald/blob/master/src/bitboard.nim)
5. [↑](#cite_ref-5) [README.md · master · tsoj / Nalwald · GitHub](https://github.com/tsoj/Nalwald/blob/master/README.md)

**[Up one Level](/Engines "Engines")**