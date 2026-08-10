# Kholin

Source: https://www.chessprogramming.org/Kholin

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Kholin**

**Kholin**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Emil Fredrik Østensen](/index.php?title=Emil_Fredrik_%C3%98stensen&action=edit&redlink=1 "Emil Fredrik Østensen (page does not exist)"), written in [C](/C "C") as part of his 2016 Master's thesis
[[1]](#cite_note-1).
Kholin is licensed under the [GPL 3](/Free_Software_Foundation#GPL "Free Software Foundation") [[2]](#cite_note-2),
and focuses on [parallel search](/Parallel_Search "Parallel Search"), in particular [Lazy SMP](/Lazy_SMP "Lazy SMP").

# Features

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [8x8 Board](/8x8_Board "8x8 Board")
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")

## [Search](/Search "Search")

- [Lazy SMP](/Lazy_SMP "Lazy SMP")
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Shared Hash Table](/Shared_Hash_Table "Shared Hash Table")
  - [Lockless Hashing](/Shared_Hash_Table#Lockless "Shared Hash Table")
  - [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [Selectivity](/Selectivity "Selectivity")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Check Extensions](/Check_Extensions "Check Extensions")

## [Evaluation](/Evaluation "Evaluation")

- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Rooks on (Semi) Open Files](/Rook_on_Open_File "Rook on Open File")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")

## Misc

- [Perft](/Perft "Perft")

# Publications

- [Emil Fredrik Østensen](/index.php?title=Emil_Fredrik_%C3%98stensen&action=edit&redlink=1 "Emil Fredrik Østensen (page does not exist)") (**2016**). *A Complete Chess Engine Parallelized Using Lazy SMP*. M.Sc. thesis, [University of Oslo](https://en.wikipedia.org/wiki/University_of_Oslo), [pdf](https://www.duo.uio.no/bitstream/handle/10852/53769/master.pdf?sequence=1)

# External Links

## Chess Engine

- [GitHub - emilfo/master - Kholin Chess Engine](https://github.com/emilfo/master)

## Misc

- [Igor Kholin from Wikipedia](https://en.wikipedia.org/wiki/Igor_Kholin)
- [The Stormlight Archive from Wikipedia](https://en.wikipedia.org/wiki/The_Stormlight_Archive)
- [House Kholin - The Coppermind - 17th Shard](https://coppermind.net/wiki/House_Kholin)

# References

1. [↑](#cite_ref-1) [Emil Fredrik Østensen](/index.php?title=Emil_Fredrik_%C3%98stensen&action=edit&redlink=1 "Emil Fredrik Østensen (page does not exist)") (**2016**). *A Complete Chess Engine Parallelized Using Lazy SMP*. M.Sc. thesis, [University of Oslo](https://en.wikipedia.org/wiki/University_of_Oslo), [pdf](https://www.duo.uio.no/bitstream/handle/10852/53769/master.pdf?sequence=1)
2. [↑](#cite_ref-2) [GitHub - emilfo/master - Kholin Chess Engine](https://github.com/emilfo/master)

**[Up one Level](/Engines "Engines")**