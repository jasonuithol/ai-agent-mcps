# ChessV

Source: https://www.chessprogramming.org/ChessV

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* ChessV**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Chessv.jpg/330px-Chessv.jpg)](/File:Chessv.jpg)

ChessV Universal Chess Program [[1]](#cite_note-1)

**ChessV**,  
an [open source engine](/Category:Open_Source "Category:Open Source") that plays over 50 [chess variants](/Chess#Variants "Chess") with various board sizes as well as [orthodox chess](/Chess "Chess"), written by [Gregory Strong](/Gregory_Strong "Gregory Strong") in [C++](/Cpp "Cpp"), released under the [GPL v2](/Free_Software_Foundation#GPL "Free Software Foundation"), first published in 2004 [[2]](#cite_note-2).
ChessV 0.95 was released in November 2016 [[3]](#cite_note-3).
ChessV runs under [Windows](/Windows "Windows") with 32-bit and 64-bit executables available and can run on [Linux](/Linux "Linux") under [Wine](https://en.wikipedia.org/wiki/Wine_(software)). It features an own [GUI](/GUI "GUI"), but includes also an executable named *ChessV\_Winboard.exe* which allows running ChessV under [WinBoard](/WinBoard "WinBoard").
ChessV **2.0**, released in March 2017, completely rewritten from scratch [[4]](#cite_note-4) in [C#](/C_sharp "C sharp"), is a [.NET Framework](https://en.wikipedia.org/wiki/.NET_Framework) application, and can run on non-Windows operating systems, such as [Linux](/Linux "Linux"), using [Mono](https://en.wikipedia.org/wiki/Mono_(software)).

# Features

## [Board Representation](/Board_Representation "Board Representation")

ChessV [encapsulates](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) the board, [position](/Chess_Position "Chess Position") and game related data inside a huge C++ class, with number of [files](/Files "Files"), [ranks](/Ranks "Ranks") and [squares](/Squares "Squares") as member, and specifies a [bitboard](/Bitboards "Bitboards") type accordant to its size, either with 64, 96 or 128 bits.
[Sliding pieces attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") are generated using [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards").

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Negamax](/Negamax "Negamax") [Alpha-Beta](/Alpha-Beta "Alpha-Beta") [PVS](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Repetition](/Repetitions "Repetitions") [Hash Table](/Hash_Table "Hash Table")
- [Selectivity](/Selectivity "Selectivity")
  - [Extensions](/Extensions "Extensions")
    - [Check Extensions](/Check_Extensions "Check Extensions")
    - [Threat Extensions](/Mate_Threat_Extensions "Mate Threat Extensions")
  - [Pruning](/Pruning "Pruning")
    - [Futility Pruning](/Futility_Pruning "Futility Pruning")
    - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning") (NMP)
  - [Reductions](/Reductions "Reductions")
    - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions") (LMR)
    - [Razoring](/Razoring "Razoring")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](/Evaluation "Evaluation")

- [Evaluation Hash Table](/Evaluation_Hash_Table "Evaluation Hash Table")
- [Lazy Evaluation](/Lazy_Evaluation "Lazy Evaluation")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [Mobility](/Mobility "Mobility")
- [King Safety](/King_Safety "King Safety")
- [King Tropism](/King_Safety#KingTropism "King Safety")

# Variants

[[5]](#cite_note-5)

- Alapo
- Almost Chess
- Angels and Devils
- Archchess
- Berolina Chess
- Bird’s Chess
- Cagliostro’s Chess
- [Capablanca Chess](/index.php?title=Capablanca_Chess&action=edit&redlink=1 "Capablanca Chess (page does not exist)")
- Capablanca Chess, Aberg variant
- Capablanca Chess, Paulowich variant
- Carrera’s Chess
- Chess256
- Chess 480
- Chess and a Half
- Chess with Augmented Knights
- Chess with Different Armies
- Chess with Ultima Pieces
- Compound Courier Custom Chess
- Courier Chess
- Cylindrical Chess
- Diagonal Chess
- Diamond Chess
- Embassy Chess
- Emperor’s Game
- Enep
- Eurasian Chess
- Exinction Chess
- [Fischer Random Chess](/Chess960 "Chess960")
- Great Chess
- Great Shatranj
- Grand Chess
- Grotesque Chess
- Hannibal Chess
- Janus Chess
- Janus Kamil Chess
- Kinglet
- Ladorean Chess
- Latrunculi duo milia et septum
- Legan’s Game
- Lemurian Shatranj
- Lions and Unicorns Chess
- [Los Alamos Chess](/index.php?title=Los_Alamos_Chess&action=edit&redlink=1 "Los Alamos Chess (page does not exist)")
- Modern Kamil
- Modern Shatranj
- Odin’s Rune Chess
- Opti Chess (mirror I)
- Opulent Chess
- [Orthodox Chess](/Chess "Chess")
- Polymorph Chess
- Roman Chess
- Royal Court
- Schoolbook Chess
- [Shatranj](/Shatranj "Shatranj")
- Shatranj Kamil
- Shatranj Kamil (64)
- Sosarian Chess
- Switching Chess
- TenCubed Chess
- Three Checks Chess
- Ultima
- Unicorn Chess
- Unicorn Great Chess
- Unicorn Grand Chess
- Univers Chess

# See also

- [Fairy-Max](/Fairy-Max "Fairy-Max")
- [Sjaak](/Sjaak_(Glebbeek) "Sjaak (Glebbeek)")
- [Sjeng](/Sjeng "Sjeng")
- [SMIRF](/SMIRF "SMIRF")

# Forum Posts

- [Interesting multi-variant chess thingy called chessv](https://www.stmintz.com/ccc/index.php?id=396326) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), November 16, 2004
- [Sources of ChessV?](http://www.talkchess.com/forum/viewtopic.php?t=18346) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), December 13, 2007
- [Anything new about the ChessV Project?](http://www.talkchess.com/forum/viewtopic.php?t=22474) by [Reinhard Scharnagl](/Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](/CCC "CCC"), July 20, 2008
- [ChessV...](http://www.talkchess.com/forum/viewtopic.php?t=29922) by [Alexander Schmidt](/index.php?title=Alexander_Schmidt&action=edit&redlink=1 "Alexander Schmidt (page does not exist)"), September 29, 2009
- [ChessV 0.95 Released](http://www.chessvariants.com/index/listcomments.php?itemid=ChessVUniversalC) by [Greg Strong](/Gregory_Strong "Gregory Strong"), [chessvariants.com](http://www.chessvariants.com/), November 13, 2016
- [Re: One of The best Weeks in Chess Engine History?](http://www.talkchess.com/forum/viewtopic.php?t=62129&start=2) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), November 14, 2016
- [ChessV 2.0 - open source GUI and engine for chess variants](http://www.talkchess.com/forum/viewtopic.php?t=63489) by [Gregory Strong](/Gregory_Strong "Gregory Strong"), [CCC](/CCC "CCC"), March 19, 2017
- [ChessV 2.1 Released](http://www.talkchess.com/forum/viewtopic.php?t=66371) by [Gregory Strong](/Gregory_Strong "Gregory Strong"), [CCC](/CCC "CCC"), January 20, 2018

# External Links

## Chess Engine

- [ChessV Universal Chess Program](http://www.chessv.org/)
- [ChessV from Wikipedia](https://en.wikipedia.org/wiki/ChessV)
- [ChessV Universal Chess Program - Chessvariants](https://www.chessvariants.com/link/ChessVUniversalC)
- [Sam Trenholme's webpage - ChessV](https://samiam.org/chessv/)

## Misc

- [Kazumi Watanabe](/Category:Kazumi_Watanabe "Category:Kazumi Watanabe") featuring Tochika All Stars - Unicorn, [Tokyo Jazz 2010](http://www.tokyo-jazz.com/2010/jp/artists/), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   Tochika All Stars are [Warren Bernhardt](https://en.wikipedia.org/wiki/Warren_Bernhardt), [Omar Hakim](https://en.wikipedia.org/wiki/Omar_Hakim), [Mike Mainieri](/Category:Mike_Mainieri "Category:Mike Mainieri"), and [Marcus Miller](/Category:Marcus_Miller "Category:Marcus Miller")

# References

1. [↑](#cite_ref-1) Image from [ChessV Universal Chess Program](http://www.chessv.org/), ChessV Copyright (C) 2007-2020 by [Gregory Strong](/Gregory_Strong "Gregory Strong"), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Interesting multi-variant chess thingy called chessv](https://www.stmintz.com/ccc/index.php?id=396326) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), November 16, 2004
3. [↑](#cite_ref-3) [ChessV 0.95 Released](http://www.chessvariants.com/index/listcomments.php?itemid=ChessVUniversalC) by [Greg Strong](/Gregory_Strong "Gregory Strong"), [chessvariants.com](http://www.chessvariants.com/), November 13, 2016
4. [↑](#cite_ref-4) [ChessV 2.0 - open source GUI and engine for chess variants](http://www.talkchess.com/forum/viewtopic.php?t=63489) by [Gregory Strong](/Gregory_Strong "Gregory Strong"), [CCC](/CCC "CCC"), March 19, 2017
5. [↑](#cite_ref-5) Variants from ChessV 0.95, [ChessV Universal Chess Program](http://www.chessv.org/)

**[Up one Level](/Engines "Engines")**