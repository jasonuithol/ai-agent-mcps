# Napoleon

Source: https://www.chessprogramming.org/Napoleon

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Napoleon**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Chrono-partie-echecs-longwood.jpg/330px-Chrono-partie-echecs-longwood.jpg)](/File:Chrono-partie-echecs-longwood.jpg)

[Napoleon](https://en.wikipedia.org/wiki/Napoleon) playing Chess with [Bertrand](https://en.wikipedia.org/wiki/Henri_Gatien_Bertrand) [[1]](#cite_note-1)

**Napoleon**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), initialy written in [C#](/C_sharp "C sharp") and soon re-written in [C++](/Cpp "Cpp") and released in September 2013 [[2]](#cite_note-2).
Napoleon had its over the board tournament debut in [Turin](https://en.wikipedia.org/wiki/Turin) 2014, where it quite successfully participated at the [IGT 2014](/IGT_2014 "IGT 2014") becoming fourth with 4 out of 7.

# Features

[[3]](#cite_note-3)

## [Move Generation](/Move_Generation "Move Generation")

- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")
- [Pseudo-legal Move Generation](/Move_Generation#PseudoLegal "Move Generation")
- [16 Bit Move Encoding](/Encoding_Moves "Encoding Moves")

## [Search](/Search "Search")

- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows") [[4]](#cite_note-4)

### [Transposition Table](/Transposition_Table "Transposition Table")

- [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")
- [Four Bucket System](/Transposition_Table#Bucket "Transposition Table")
- [Depth-preferred Replacement Scheme](/Transposition_Table#ReplacementStrategies "Transposition Table")

### [Move Ordering](/Move_Ordering "Move Ordering")

- [Principal Variation Extraction from TT](/Principal_Variation "Principal Variation")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [History Heuristic](/History_Heuristic "History Heuristic")
- [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
- [MVV-LVA](/MVV-LVA "MVV-LVA")

### [Selectivity](/Selectivity "Selectivity")

- [AEL-Pruning](/AEL-Pruning "AEL-Pruning")
  - [Adaptive Null Move Pruning](/Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
  - [Extended Futility Pruning](/Futility_Pruning#Extendedfutilityprunning "Futility Pruning")
  - [Limited Razoring](/Razoring#LimitedRazoring "Razoring")
- [Adaptive Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")

## [Evaluation](/Evaluation "Evaluation")

- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [Tapered Eval](/Tapered_Eval "Tapered Eval") [[5]](#cite_note-5)

:   and more ...

## Misc

- [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [Pondering](/Pondering "Pondering")

# Forum Posts

- [Aspiration windows](http://www.talkchess.com/forum/viewtopic.php?t=47996) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), May 14, 2013
- [Re: Napoleon PP by crybot - current edition](http://www.talkchess.com/forum3/viewtopic.php?t=50972) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), January 21, 2014
- [Tapered evaluation](http://www.talkchess.com/forum/viewtopic.php?t=51656) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), March 18, 2014
- [Napoleon 1.4.0](http://www.talkchess.com/forum/viewtopic.php?t=51709) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), March 22, 2014
- [Napoleon 1.5.0 64-bit Gauntlet for CCRL 40/40](http://www.talkchess.com/forum/viewtopic.php?t=53082) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), July 25, 2014
- [Parameter tuning with multi objective optimization](http://www.talkchess.com/forum/viewtopic.php?t=63926) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), May 07, 2017 » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [search efficiency](http://www.talkchess.com/forum/viewtopic.php?t=64390) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), June 23, 2017 » [Search](/Search "Search")
- [Napoleon 1.8](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=64444) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), June 28, 2017

# External Links

## Chess Engine

- [crybot/Napoleon · GitHub](https://github.com/crybot/Napoleon)
- [crybot/Napoleon-old · GitHub](https://github.com/crybot/Napoleon-old) ([C#](/C_sharp "C sharp"))
- [Napoleon](http://www.g-sei.org/napoleon/) « [G 6](/G_6 "G 6")
- [Napoleon](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Napoleon&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")
- [Napoleon](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Napoleon&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents)  in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [Napoleon from Wikipedia](https://en.wikipedia.org/wiki/Napoleon)
- [Napoleon (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Napoleon_%28disambiguation%29)
- [Napoleone from Wikipedia](https://en.wikipedia.org/wiki/Napoleone)
- [Napoleon of India from Wikipedia](https://en.wikipedia.org/wiki/Napoleon_of_India)
- [Napoleon.org](http://www.napoleon.org/en/home.asp)

### Chess

- [Napoleon Bonaparte and Chess](https://www.chesshistory.com/winter/extra/napoleon.html) by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29)
- [Napoleon Bonaparte and Chess](http://www.edochess.ca/batgirl/NapoleonChess.html) from [Sarah's Chess Journal](http://www.edochess.ca/batgirl/welcome.html)
- [The chess games of Napoleon Bonaparte](http://www.chessgames.com/player/napoleon_bonaparte.html) from [chessgames.com](http://www.chessgames.com/index.html)

:   [The chess games of Madame de Remusat](http://www.chessgames.com/perl/chessplayer?pid=77027) from [chessgames.com](http://www.chessgames.com/index.html) [[6]](#cite_note-6)

- [Napoleon Opening from Wikipedia](https://en.wikipedia.org/wiki/Napoleon_Opening)
- [Napoleon Gambit](https://en.wikipedia.org/wiki/Scotch_Game#Analysis) in the [Scotch Game from Wikipedia](https://en.wikipedia.org/wiki/Scotch_Game)

### Games

- [Napoleon (card game) from Wikipedia](https://en.wikipedia.org/wiki/Napoleon_%28card_game%29)
- [Napoleon (board game) from Wikipedia](https://en.wikipedia.org/wiki/Napoleon_%28game%29)
- [Napoleon (GBA game) from Wikipedia](https://en.wikipedia.org/wiki/Napoleon_%28GBA_game%29)

# References

1. [↑](#cite_ref-1) [Napoleon](https://en.wikipedia.org/wiki/Napoleon) playing Chess with [Bertrand](https://en.wikipedia.org/wiki/Henri_Gatien_Bertrand) at [Longwood](https://en.wikipedia.org/wiki/Longwood_House), [Saint Helena](https://en.wikipedia.org/wiki/Saint_Helena), [Drawing](http://www.lautresaintehelene.com/other-st-helena-index.html) from [Inside Longwood - Napoleon's captivity in 1818](http://www.inside-longwood.com/inside-longwood-chronology-1818.html), Chronology to complement the books, Albert Benhamou (**2010**). *[L'autre Sainte-Hélène](http://www.lautresaintehelene.com/other-st-helena-index.html)*. (French) and Albert Benhamou (**2012**). *[Inside Longwood](http://www.napoleon.org/en/magazine/just_published/files/481397.asp) - [Barry O'Meara's](https://en.wikipedia.org/wiki/Barry_Edward_O%27Meara) Clandestine Letters*. © [Albert Benhamou Publishing](https://www.bookdepository.com/publishers/Albert-Benhamou-Publishing), [Наполеон Бонапарт и шахматы — Википедия](https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D0%BF%D0%BE%D0%BB%D0%B5%D0%BE%D0%BD_%D0%91%D0%BE%D0%BD%D0%B0%D0%BF%D0%B0%D1%80%D1%82_%D0%B8_%D1%88%D0%B0%D1%85%D0%BC%D0%B0%D1%82%D1%8B), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Napoleon](http://www.g-sei.org/napoleon/) « [G 6](/G_6 "G 6")
3. [↑](#cite_ref-3) [Napoleon/README.md at master · crybot/Napoleon · GitHub](https://github.com/crybot/Napoleon/blob/master/README.md)
4. [↑](#cite_ref-4) [Aspiration windows](http://www.talkchess.com/forum/viewtopic.php?t=47996) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), May 14, 2013
5. [↑](#cite_ref-5) [Tapered evaluation](http://www.talkchess.com/forum/viewtopic.php?t=51656) by [Marco Pampaloni](/Marco_Pampaloni "Marco Pampaloni"), [CCC](/CCC "CCC"), March 18, 2014
6. [↑](#cite_ref-6) [Madame de Rémusat from Wikipedia](https://en.wikipedia.org/wiki/Madame_de_R%C3%A9musat)

**[Up one Level](/Engines "Engines")**