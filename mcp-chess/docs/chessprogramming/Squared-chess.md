# Squared-chess

Source: https://www.chessprogramming.org/Squared-chess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* squared-chess**

[![](/images/f/fd/Squared-chess.png)](/File:Squared-chess.png)

squared-chess [[1]](#cite_note-1)

**squared-chess**, (Squared-chess, ^2-chess)  
an [UCI](/UCI "UCI") compatible [open source chess engine](/Category:Open_Source "Category:Open Source") by [Jost Triller](/Jost_Triller "Jost Triller"),
written in [C++](/Cpp "Cpp"), first released in September 2018 under the [MIT license](/Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") [[2]](#cite_note-2).
Like its successors [Googleplex Starthinker](/Googleplex_Starthinker "Googleplex Starthinker") and [Nalwald](/Nalwald "Nalwald"), squared-chess is a [bitboard](/Bitboards "Bitboards") engine and generates [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") [Kindergarten](/Kindergarten_Bitboards "Kindergarten Bitboards") like,
by looking up four pre-calculated line attack arrays, 32-Kbyte each, indexed by square and [inner six bit](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks") [line occupancy](/Occupancy_of_any_Line "Occupancy of any Line")
[[3]](#cite_note-3).

# Features

[[4]](#cite_note-4)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards")

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta") [Negamax](/Negamax "Negamax")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [MVV-LVA](/MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
- [Selectivity](/Selectivity "Selectivity")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Check Extensions](/Check_Extensions "Check Extensions")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")

## [Evaluation](/Evaluation "Evaluation")

- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
  - [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [King Safety](/King_Safety "King Safety")

# See also

- [Googleplex Starthinker](/Googleplex_Starthinker "Googleplex Starthinker")
- [Hactar](/Hactar "Hactar")
- [Nalwald](/Nalwald "Nalwald")

# Forum Posts

- [New chess engine '^2-chess' - release 1.1.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68472) by [Jost Triller](/Jost_Triller "Jost Triller"), [CCC](/CCC "CCC"), September 20, 2018

:   [Re: New chess engine '^2-chess' - release 1.1.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68472&start=20) by [Jost Triller](/Jost_Triller "Jost Triller"), [CCC](/CCC "CCC"), November 05, 2018

# External Links

- [Tsoj Tsoj / squared-chess · GitLab](https://gitlab.com/tsoj/squared-chess)
- [Squared-chess](https://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Squared-chess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")

# References

1. [↑](#cite_ref-1) squared-chess logo based on [media/^2.png · master · Tsoj Tsoj / squared-chess · GitLab](https://gitlab.com/tsoj/squared-chess/-/blob/master/media/%5E2.png)
2. [↑](#cite_ref-2) [New chess engine '^2-chess' - release 1.1.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68472) by [Jost Triller](/Jost_Triller "Jost Triller"), [CCC](/CCC "CCC"), September 20, 2018
3. [↑](#cite_ref-3) [ChessData.hpp · master · Tsoj Tsoj / squared-chess · GitLab](https://gitlab.com/tsoj/squared-chess/-/blob/master/ChessData.hpp#L129)
4. [↑](#cite_ref-4) [README.md · master · Tsoj Tsoj / squared-chess · GitLab](https://gitlab.com/tsoj/squared-chess/-/blob/master/README.md)

**[Up one Level](/Engines "Engines")**