# Abulafia

Source: https://www.chessprogramming.org/Abulafia

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Abulafia**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Abraham_abulafia.jpg/330px-Abraham_abulafia.jpg)](/File:Abraham_abulafia.jpg)

[Abulafia's](https://en.wikipedia.org/wiki/Abraham_Abulafia) Light of the Intellect (1285) [[1]](#cite_note-1)

**Abulafia**,  
an [UCI](/UCI "UCI") compliant experimental [open source chess engine](/Category:Open_Source "Category:Open Source") by [Nicu Ionita](/Nicu_Ionita "Nicu Ionita"), written in [Haskell](/index.php?title=Haskell&action=edit&redlink=1 "Haskell (page does not exist)"), and predecessor of [Barbarossa](/Barbarossa "Barbarossa") [[2]](#cite_note-2).
Abulafia uses [monad transformers](https://en.wikipedia.org/wiki/Monad_%28functional_programming%29)
[[3]](#cite_note-3)
[[4]](#cite_note-4)
in [continuation passing style](https://en.wikipedia.org/wiki/Continuation-passing_style) to control the [search](/Search "Search").

# Features

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") [[5]](#cite_note-5)

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search") (PVS)
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")

## [Evaluation](/Evaluation "Evaluation")

- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
- [Center Control](/Center_Control "Center Control")
- [King Safety](/King_Safety "King Safety")
- [Passed Pawns](/Passed_Pawn "Passed Pawn")

# See also

- [Barbarossa](/Barbarossa "Barbarossa")

# Forum Posts

- [Abulafia, chess, Haskell and some (new?) ideas](http://www.talkchess.com/forum/viewtopic.php?t=43384) by [Nicu Ionita](/Nicu_Ionita "Nicu Ionita"), [CCC](/CCC "CCC"), April 20, 2012
- [The best chess engine written in Haskell](http://www.talkchess.com/forum/viewtopic.php?t=46921) by Ruxy Sylwyka, [CCC](/CCC "CCC"), January 18, 2013

# External Links

## Chess Engine

- [nionita/Abulafia · GitHub](https://github.com/nionita/Abulafia)
- [Abulafia 0.61](https://ccrl.chessdom.com/ccrl/404/cgi/engine_details.cgi?match_length=30&print=Details&each_game=1&eng=Abulafia%200.61#Abulafia_0_61) in [CCRL 40/4](/CCRL "CCRL")

## Misc

- [Abulafia (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Abulafia_%28disambiguation%29)
- [Abraham Abulafia from Wikipedia](https://en.wikipedia.org/wiki/Abraham_Abulafia)
- [Meir Abulafia from Wikipedia](https://en.wikipedia.org/wiki/Meir_Abulafia)

# References

1. [↑](#cite_ref-1) An illuminated page from [Abraham Abulafia's](https://en.wikipedia.org/wiki/Abraham_Abulafia) *Light of the Intellect* (1285), [The Vatican Library](https://en.wikipedia.org/wiki/Vatican_Library), Unknown artist; the author of the book is Abulafia, [Kabbalah from Wikipedia](https://en.wikipedia.org/wiki/Kabbalah), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Barbarossa 0.1.0](http://www.talkchess.com/forum/viewtopic.php?t=50213) by [Nicu Ionita](/Nicu_Ionita "Nicu Ionita"), [CCC](/CCC "CCC"), November 24, 2013
3. [↑](#cite_ref-3) [Haskell/Monad transformers - Wikibooks](https://en.wikibooks.org/wiki/Haskell/Monad_transformers)
4. [↑](#cite_ref-4) [Haskell/Understanding monads - Wikibooks](https://en.wikibooks.org/wiki/Haskell/Understanding_monads)
5. [↑](#cite_ref-5) [Abulafia/Magics.hs at master · nionita/Abulafia · GitHub](https://github.com/nionita/Abulafia/blob/master/Moves/Magics.hs)

**[Up one level](/Engines "Engines")**