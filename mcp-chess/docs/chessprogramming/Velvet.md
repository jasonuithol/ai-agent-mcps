# Velvet

Source: https://www.chessprogramming.org/Velvet

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Velvet**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Velvet_warp.svg/330px-Velvet_warp.svg.png)](/File:Velvet_warp.svg)

Illustration depicting the manufacture of velvet fabric [[1]](#cite_note-1)

**Velvet**, (Velvet Chess Engine)  
an [UCI](/UCI "UCI") compatible [open source chess engine](/Category:Open_Source "Category:Open Source") by [Martin Honert](/index.php?title=Martin_Honert&action=edit&redlink=1 "Martin Honert (page does not exist)"), written in [Rust](/Rust "Rust"),
licensed under the [GPL v3.0](/Free_Software_Foundation#GPL "Free Software Foundation"). The first release in August 2020 was based on the author's previous web-based engine [Wasabi](/index.php?title=Wasabi&action=edit&redlink=1 "Wasabi (page does not exist)")
[[2]](#cite_note-2).
Velvet v2.0.0, released in July 2021, features [NNUE](/NNUE "NNUE") [evaluation](/Evaluation "Evaluation") along with [magic bitboards](/Magic_Bitboards "Magic Bitboards") [[3]](#cite_note-3).

# Selected Features

[[4]](#cite_note-4)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Obstruction Difference](/Obstruction_Difference "Obstruction Difference") (v1.1.0)
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") (v2.0.0)

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Lazy SMP](/Lazy_SMP "Lazy SMP") (v3.0.0)
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Selectivity](/Selectivity "Selectivity")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [SEE Pruning](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Check Extensions](/Check_Extensions "Check Extensions")
  - [Singular Extensions](/Singular_Extensions "Singular Extensions") (v3.1.0)
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [MVV-LVA](/MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic")

## [Evaluation](/Evaluation "Evaluation")

- [NNUE](/NNUE "NNUE") (v2.0.0)

# Forum Posts

- [Velvet 3.1.0 for the GRL](https://www.talkchess.com/forum3/viewtopic.php?f=6&t=78666) by [Rebel](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), November 15, 2021

# External Links

## Chess Engine

- [GitHub - mhonert/velvet-chess: Velvet Chess Engine - written in Rust](https://github.com/mhonert/velvet-chess)
- [Velvet](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Velvet&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/15](/CCRL "CCRL")

## Misc

- [Velvet (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Velvet_(disambiguation))
- [Velvet from Wikipedia](https://en.wikipedia.org/wiki/Velvet)
- [The Velvet Underground](https://en.wikipedia.org/wiki/The_Velvet_Underground) - [What Goes On](https://en.wikipedia.org/wiki/What_Goes_On_(Velvet_Underground_song)), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Image](https://commons.wikimedia.org/wiki/File:Velvet_warp.svg) by Vladsinger, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Release v1.0.0 · mhonert/velvet-chess · GitHub](https://github.com/mhonert/velvet-chess/releases/tag/v1.0.0)
3. [↑](#cite_ref-3) [Release v2.0.0 · mhonert/velvet-chess · GitHub](https://github.com/mhonert/velvet-chess/releases/tag/v2.0.0)
4. [↑](#cite_ref-4) [Releases · mhonert/velvet-chess · GitHub](https://github.com/mhonert/velvet-chess/releases)

**[Up one level](/Engines "Engines")**