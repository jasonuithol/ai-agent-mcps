# Paulchen332

Source: https://www.chessprogramming.org/Paulchen332

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* paulchen332**

[![](/images/c/c7/Pchess_logo.jpg)](https://codemetas.de/2020/11/22/The-Royal-Game.html#introducing-)

paulchen332 Logo [[1]](#cite_note-1)

**paulchen332**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Philipp Lenk](/Philipp_Lenk "Philipp Lenk"), written in [C++ 17](/Cpp#17 "Cpp"), licensed under the permissive [BSD 2-clause license](https://en.wikipedia.org/wiki/BSD_licenses), first released in November 2020 [[2]](#cite_note-2).
paulchen332 is a didactic engine, and teaches modern C++. The UCI implementation is already explained in detail [[3]](#cite_note-3) by its author, who proposed more details will follow in subsequent articles [[4]](#cite_note-4)

# Features

## [Board Representation](/Board_Representation "Board Representation")

[[5]](#cite_note-5)

- [Bitboards](/Bitboards "Bitboards") [[6]](#cite_note-6)
- [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") by [Linewise Occupancy Lookup](/Occupancy_of_any_Line "Occupancy of any Line") [[7]](#cite_note-7)

## [Search](/Search "Search")

[[8]](#cite_note-8)

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [NegaScout](/NegaScout "NegaScout")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [PV-Move](/PV-Move "PV-Move")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [MVV/LVA](/MVV-LVA "MVV-LVA")
  - [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Selectivity](/Selectivity "Selectivity")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Razoring](/Razoring "Razoring")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")

## [Evaluation](/Evaluation "Evaluation")

[[9]](#cite_note-9)

- [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Backward Pawn](/Backward_Pawn "Backward Pawn")
  - [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
  - [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [King Safety](/King_Safety "King Safety")
  - [Castling Rights](/Castling_Rights "Castling Rights")
  - [Attacking King Zone](/King_Safety#Attacking "King Safety")
  - [Pawn Shield](/King_Safety#PawnShield "King Safety")
  - [Open Files](/Open_File "Open File") ([Half-open Files](/Half-open_File "Half-open File"))

# See also

- [Paul](/Paul "Paul")
- [Superpawn](/Superpawn "Superpawn")

# Postings

- [The Royal Game](https://codemetas.de/2020/11/22/The-Royal-Game.html) by [Philipp Lenk](/Philipp_Lenk "Philipp Lenk"), [code<metas>](https://codemetas.de/), November 22, 2020
- [New engine: paulchen332](https://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=12550) by [Philipp Lenk](/Philipp_Lenk "Philipp Lenk"), [CCRL Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 23, 2020
- [New engine: paulchen332](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75919) by [Philipp Lenk](/Philipp_Lenk "Philipp Lenk"), [CCC](/CCC "CCC"), November 25, 2020

# External Links

## Chess Eingine

- [GitHub - philipplenk/paulchen332: A simple UCI chess engine](https://github.com/philipplenk/paulchen332)
- [Release paulchen332 v0.1 · philipplenk/paulchen332 · GitHub](https://github.com/philipplenk/paulchen332/releases/tag/v0.1)

## Misc

- [Paulchen – Wiktionary](https://de.wiktionary.org/wiki/Paulchen) (German)
- [Paulchen – Wikipedia](https://de.wikipedia.org/wiki/Paulchen) (German) [Diminutive](https://en.wikipedia.org/wiki/Diminutive) of [Paul](https://en.wikipedia.org/wiki/Paul_(given_name))

# References

1. [↑](#cite_ref-1) Image from [The Royal Game](https://codemetas.de/2020/11/22/The-Royal-Game.html#introducing-) by [Philipp Lenk](/Philipp_Lenk "Philipp Lenk"), November 22, 2020, the Logo was graciously provided by [Jana Ochse](http://www.2dpixx.de/)
2. [↑](#cite_ref-2) [New engine: paulchen332](https://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=12550) by [Philipp Lenk](/Philipp_Lenk "Philipp Lenk"), [CCRL Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 23, 2020
3. [↑](#cite_ref-3) [The Royal Game | UCI](https://codemetas.de/2020/11/22/The-Royal-Game.html#uci) by [Philipp Lenk](/Philipp_Lenk "Philipp Lenk"), [code<metas>](https://codemetas.de/), November 22, 2020
4. [↑](#cite_ref-4) [The Royal Game | Outlook](https://codemetas.de/2020/11/22/The-Royal-Game.html#outlook) by [Philipp Lenk](/Philipp_Lenk "Philipp Lenk"), [code<metas>](https://codemetas.de/), November 22, 2020
5. [↑](#cite_ref-5) [paulchen332/include/philchess/chessboard.hpp · GitHub](https://github.com/philipplenk/paulchen332/blob/main/include/philchess/chessboard.hpp)
6. [↑](#cite_ref-6) [paulchen332/include/philchess/bitboard.hpp · GitHub](https://github.com/philipplenk/paulchen332/blob/main/include/philchess/bitboard.hpp)
7. [↑](#cite_ref-7) [paulchen332/include/philchess/bitboard\_patterns.hpp · GitHub](https://github.com/philipplenk/paulchen332/blob/main/include/philchess/bitboard_patterns.hpp)
8. [↑](#cite_ref-8) [paulchen332/include/philchess/algorithm/negamax.hpp · GitHub](https://github.com/philipplenk/paulchen332/blob/main/include/philchess/algorithm/negamax.hpp); [paulchen332/include/philchess/default\_search\_control.hpp · GitHub](https://github.com/philipplenk/paulchen332/blob/main/include/philchess/default_search_control.hpp)
9. [↑](#cite_ref-9) [paulchen332/include/philchess/eval](https://github.com/philipplenk/paulchen332/tree/main/include/philchess/eval)

**[Up one level](/Engines "Engines")**