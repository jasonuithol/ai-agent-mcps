# Bitboard-Chess

Source: https://www.chessprogramming.org/Bitboard-Chess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Bitboard-Chess**

**Bitboard-Chess**,  
a [WinBoard](/WinBoard "WinBoard") compliant, didactic [open source chess program](/Category:Open_Source "Category:Open Source") by [Bill Jordan](/Bill_Jordan "Bill Jordan"), written in [C++](/Cpp "Cpp") and licensed under the [GPL version 3](/Free_Software_Foundation#GPL "Free Software Foundation"), available on [GitHub](https://en.wikipedia.org/wiki/GitHub) [[1]](#cite_note-1) - an [ebook](https://en.wikipedia.org/wiki/Ebook) explaining the program is available from [Amazon](https://en.wikipedia.org/wiki/Amazon_(company)) [[2]](#cite_note-2). Bitboard-Chess is designed to show how a chess engine might work, quite similar to [Bills Bare Bones Chess](/Bills_Bare_Bones_Chess "Bills Bare Bones Chess") aka **Basic-Chess**, but using [bitboards](/Bitboards "Bitboards").
[Bitboard serialization](/Bitboard_Serialization "Bitboard Serialization") is done via [Matt Taylor's](/Matt_Taylor "Matt Taylor") [folded BitScan](/BitScan#MattTaylorsFoldingtrick "BitScan") [[3]](#cite_note-3),
but [move generation](/Move_Generation "Move Generation") of [sliding pieces](/Sliding_Pieces "Sliding Pieces") is done in [mailbox](/Mailbox "Mailbox") manner
iterating over [ray directions](/Direction#RayDirections "Direction") and pre-calculated [target squares](/Target_Square "Target Square"), radiating from the [piece origin](/Origin_Square "Origin Square") along with end of ray and blocker conditions [[4]](#cite_note-4).

# Features

[[5]](#cite_note-5)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [8x8 Board](/8x8_Board "8x8 Board")

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [MVV-LVA](/MVV-LVA "MVV-LVA")
  - [History Heuristic](/History_Heuristic "History Heuristic")
- [Extensions](/Extensions "Extensions")
- [Reductions](/Reductions "Reductions")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")

## [Evaluation](/Evaluation "Evaluation")

- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Open Files](/Open_File "Open File")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [King Safety](/King_Safety "King Safety")

# See also

- [Awesome](/Awesome "Awesome")
- [Bills Bare Bones Chess](/Bills_Bare_Bones_Chess "Bills Bare Bones Chess")
- [JavaScript-Chess](/JavaScript-Chess "JavaScript-Chess")

# Publication

- [Bill Jordan](/Bill_Jordan "Bill Jordan") (**2020**). *[How to Write a Bitboard Chess Engine](https://amzn.eu/7p0J2S1)*. [amazon](https://www.amazon.com/How-Write-Bitboard-Chess-Engine-ebook/dp/B0842GRJ6L/)

# External Links

- [GitHub - billjordanchess/Bitboard-Chess: Simple C++ chess playing program which uses bitboards](https://github.com/billjordanchess/Bitboard-Chess)

# References

1. [↑](#cite_ref-1) [GitHub - billjordanchess/Bitboard-Chess: Simple C++ chess playing program which uses bitboards](https://github.com/billjordanchess/Bitboard-Chess)
2. [↑](#cite_ref-2) [Bill Jordan](/Bill_Jordan "Bill Jordan") (**2020**). *[How to Write a Bitboard Chess Engine](https://amzn.eu/7p0J2S1)*. [amazon](https://www.amazon.com/How-Write-Bitboard-Chess-Engine-ebook/dp/B0842GRJ6L/)
3. [↑](#cite_ref-3) [Bitboard-Chess/bitboard.cpp at master · billjordanchess/Bitboard-Chess · GitHub](https://github.com/billjordanchess/Bitboard-Chess/blob/master/bitboard.cpp#L362)
4. [↑](#cite_ref-4) [Bitboard-Chess/gen.cpp at master · billjordanchess/Bitboard-Chess · GitHub](https://github.com/billjordanchess/Bitboard-Chess/blob/master/gen.cpp#L94)
5. [↑](#cite_ref-5) [Bitboard-Chess/README.md at master · billjordanchess/Bitboard-Chess · GitHub](https://github.com/billjordanchess/Bitboard-Chess/blob/master/README.md)

**[Up one Level](/Engines "Engines")**