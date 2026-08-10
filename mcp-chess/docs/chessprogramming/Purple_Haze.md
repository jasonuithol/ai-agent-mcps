# Purple Haze

Source: https://www.chessprogramming.org/Purple_Haze

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Purple Haze**

[File:Purple Haze (Cannabis).jpg](/index.php?title=Special:Upload&wpDestFile=Purple_Haze_(Cannabis).jpg "File:Purple Haze (Cannabis).jpg")

Purple Haze flower [[1]](#cite_note-1)

**Purple Haze**,  
a free [open source chess engine](/Category:Open_Source "Category:Open Source") by [Vincent Ollivier](/Vincent_Ollivier "Vincent Ollivier") compliant to the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and distributed under the terms of the [GNU General Public License](/Free_Software_Foundation#GPL "Free Software Foundation") version 3 [[2]](#cite_note-2).
Purple Haze uses some features of [C++11](/Cpp "Cpp"), so one needs [GCC >= 4.6](https://en.wikipedia.org/wiki/GNU_Compiler_Collection#GCC_stable_release) or [Clang](https://en.wikipedia.org/wiki/Clang) >= 3.0 [[3]](#cite_note-3) to compile it.

# Description

## [Board Representation](/Board_Representation "Board Representation")

Purple Haze has a [0x88](/0x88 "0x88") board representation combined with [piece-lists](/Piece-Lists "Piece-Lists"), and utilizes two [arrays](/Array "Array") indexed by [0x88 square relations](/0x88#SquareRelations "0x88"),
containing either [direction](/Direction "Direction") and boolean information in [std::bitset<7>](https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library#Containers) whether a [piece type](/Pieces "Pieces") may [attack](/Attacks "Attacks") a [square](/Squares "Squares") [[4]](#cite_note-4),
both used for lazy or [staged move generation](/Move_Generation#Staged "Move Generation") concerning [legality](/Legal_Move "Legal Move") of [hash move](/Hash_Move "Hash Move") and [killers](/Killer_Move "Killer Move").

## [Search](/Search "Search")

The [PVS](/Principal_Variation_Search "Principal Variation Search") implementation [[5]](#cite_note-5) uses [node type](/Node_Types "Node Types") as [template parameter](https://en.wikipedia.org/wiki/Template_%28C%2B%2B%29#Function_templates), and applies [adaptive null move pruning](/Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [extended futility pruning](/Futility_Pruning#Extendedfutilitypruning "Futility Pruning"), and [LMR](/Late_Move_Reductions "Late Move Reductions") etc. [[6]](#cite_note-6) inside its [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [transposition table](/Transposition_Table "Transposition Table").

## [Evaluation](/Evaluation "Evaluation")

The evaluation features a [material hash table](/Material_Hash_Table "Material Hash Table") and [tapers](/Tapered_Eval "Tapered Eval") between [opening](/Opening "Opening") and [endgame](/Endgame "Endgame") [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") [[7]](#cite_note-7).

# See also

- [Little Wing](/Little_Wing "Little Wing")

# Forum Posts

- [MSVC build of Purple Haze](http://www.talkchess.com/forum/viewtopic.php?t=39437) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), June 20, 2011
- [Purple Haze v2.0.2](http://www.talkchess.com/forum/viewtopic.php?t=43028) by [Vincent Ollivier](/Vincent_Ollivier "Vincent Ollivier"), [CCC](/CCC "CCC"), March 26, 2012
- [Purple Haze v2.1.0](http://www.talkchess.com/forum/viewtopic.php?t=45932) by [Vincent Ollivier](/Vincent_Ollivier "Vincent Ollivier"), [CCC](/CCC "CCC"), November 10, 2012

# External Links

## Chess Engine

- [Purple Haze](https://vinc.cc/projects/purplehaze.html)
- [· GitHub - vinc/purplehaze: 0x88 chess engine written in C++](https://github.com/vinc/purplehaze)

## Misc

- [Purple Haze (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Purple_Haze_%28disambiguation%29)
- [Purple Haze (cannabis) from Wikipedia](https://en.wikipedia.org/wiki/Purple_Haze_%28cannabis%29)
- [Purple from Wikipedia](https://en.wikipedia.org/wiki/Purple)
- [Haze from Wikipedia](https://en.wikipedia.org/wiki/Haze)
- [The Jimi Hendrix Experience](https://en.wikipedia.org/wiki/The_Jimi_Hendrix_Experience) - [Purple Haze](https://en.wikipedia.org/wiki/Purple_Haze), [Beat-Club](https://en.wikipedia.org/wiki/Beat-Club) 1967, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   line-up: [Jimi Hendrix](/Category:Jimi_Hendrix "Category:Jimi Hendrix"), [Mitch Mitchell](https://en.wikipedia.org/wiki/Mitch_Mitchell), [Noel Redding](https://en.wikipedia.org/wiki/Noel_Redding)

- [Nguyên Lê](/Category:Nguy%C3%AAn_L%C3%AA "Category:Nguyên Lê") - Purple Haze - Philips Music World Festival 2004, [São Paulo](https://en.wikipedia.org/wiki/S%C3%A3o_Paulo), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   line-up: [Nguyên Lê](/Category:Nguy%C3%AAn_L%C3%AA "Category:Nguyên Lê"), [Michel Alibo](https://fr.wikipedia.org/wiki/Michel_Alibo), [Cathy Renoir](http://www.discogs.com/artist/426356-Cathy-Renoir), [Francis Lassus](https://fr.wikipedia.org/wiki/Francis_Lassus)

# References

1. [↑](#cite_ref-1) [Purple Haze flower](https://commons.wikimedia.org/wiki/File:Purple_Haze_(Cannabis).jpg), Photo by [Hans Roht](https://en.wikipedia.org/wiki/User:HansRoht), May 01, 2010, [Purple Haze (cannabis) from Wikipedia](https://en.wikipedia.org/wiki/Purple_Haze_%28cannabis%29), [Cannabis (drug) from Wikipedia](https://en.wikipedia.org/wiki/Cannabis_%28drug%29)
2. [↑](#cite_ref-2) [purplehaze/README.md at master · vinc/purplehaze · GitHub](https://github.com/vinc/purplehaze/blob/master/README.md)
3. [↑](#cite_ref-3) [Purple Haze v2.0.2](http://www.talkchess.com/forum/viewtopic.php?t=43028) by [Vincent Ollivier](/Vincent_Ollivier "Vincent Ollivier"), [CCC](/CCC "CCC"), March 26, 2012
4. [↑](#cite_ref-4) [github.com/vinc/purplehaze/blob/master/src/board.h](https://github.com/vinc/purplehaze/blob/master/src/board.h)
5. [↑](#cite_ref-5) [PVS](http://www.talkchess.com/forum/viewtopic.php?t=26974) by [Edmund Moshammer](/Edmund_Moshammer "Edmund Moshammer"), [CCC](/CCC "CCC"), March 12, 2009
6. [↑](#cite_ref-6) [github.com/vinc/purplehaze/blob/master/src/search.cpp](https://github.com/vinc/purplehaze/blob/master/src/search.cpp)
7. [↑](#cite_ref-7) [github.com/vinc/purplehaze/blob/master/README.md](https://github.com/vinc/purplehaze/blob/master/README.md)

**[Up one level](/Engines "Engines")**