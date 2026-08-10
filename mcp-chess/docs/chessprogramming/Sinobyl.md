# Sinobyl

Source: https://www.chessprogramming.org/Sinobyl

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Sinobyl**

**Sinobyl**,   
initially called **Latista** and in 2008 renamed to Sinobyl due to trademark issues
[[1]](#cite_note-1),
is a [WinBoard](/WinBoard "WinBoard") compliant chess engine by [Eric Oldre](/Eric_Oldre "Eric Oldre"), written in [C++](/Cpp "Cpp"), and first released in 2004
[[2]](#cite_note-2).
Sinobyl, aka Latista 1.4, was one of the first engines besides [Scorpio](/Scorpio "Scorpio") and [Gambit Fruit](/Gambit_Fruit "Gambit Fruit"),
to use [Daniel Shawul's](/Daniel_Shawul "Daniel Shawul") [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases").
Sinobyl was later ported to [C#](/C_sharp "C sharp"), with [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") replaced by [magics](/Magic_Bitboards "Magic Bitboards") [[3]](#cite_note-3),
released in 2014 as [NoraGrace](/NoraGrace "NoraGrace"), dedicated to *Nora Grace Oldre* who was taken from Eric and his wife unexpectedly a few days before she was due to be born [[4]](#cite_note-4).

# Description

*based on Latista 1.5* [[5]](#cite_note-5)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards")

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Move](/Killer_Move "Killer Move")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Selectivity](/Selectivity "Selectivity")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
    - [R](/Depth_Reduction_R "Depth Reduction R")=3
    - [Verification Search](/Null_Move_Pruning#ZugzwangVerification "Null Move Pruning") in [Endgame](/Endgame "Endgame")
  - [Fractional Extensions](/Extensions#FractionalExtensions "Extensions")
    - [Check Extensions](/Check_Extensions "Check Extensions")
    - [Passed Pawn to 7th Rank Extensions](/Passed_Pawn_Extensions "Passed Pawn Extensions")
    - [Horizon](/Horizon_Node "Horizon Node") [Threat Extensions](/Mate_Threat_Extensions#Threat_Extensions "Mate Threat Extensions")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Reductions](/Reductions "Reductions")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")

:   :   To avoid [standing pat](/Quiescence_Search#StandPat "Quiescence Search") in [quiescence](/Quiescence_Search "Quiescence Search") where pieces of the [side to move](/Side_to_move "Side to move") were just attacked and [en prise](/En_prise "En prise"), Eric Oldre introduced [Horizon](/Horizon_Node "Horizon Node") [Threat Extensions](/Mate_Threat_Extensions#Threat_Extensions "Mate Threat Extensions") in Latista 1.4 [[6]](#cite_note-6).

## [Evaluation](/Evaluation "Evaluation")

- [Material](/Material "Material")
- [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [King Safety](/King_Safety "King Safety")

:   [Pawn Shelter](/King_Safety#PawnShield "King Safety")

- [Pawn Races](/Pawn_Race "Pawn Race")
- [Development](/Development "Development")
- [Piece Activity](/Mobility "Mobility")

# See also

- [NoraGrace](/NoraGrace "NoraGrace")

# Forum Posts

- [Bitboard board representation](https://www.stmintz.com/ccc/index.php?id=405590) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), January 13, 2005
- [An interesting bug i found tonight in latista](https://www.stmintz.com/ccc/index.php?id=405910) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), January 16, 2005
- [Idea i'm been using to help tune latista](https://www.stmintz.com/ccc/index.php?id=407347) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), January 24, 2005
- [Latista 1.3 released](https://www.stmintz.com/ccc/index.php?id=434691) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), July 02, 2005
- [Latista 1.4 released. (Rybka killer edition!)](https://www.stmintz.com/ccc/index.php?id=472863) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), December 23, 2005
- [Latista 1.5](https://www.stmintz.com/ccc/index.php?id=479324) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), January 13, 2006
- [Re: new/updated engines: 2008/11/28-29](http://www.open-aurec.com/wbforum/viewtopic.php?p=187799&start=1#p187822) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 01, 2008
- [New open source engine in C# - NoraGrace](http://www.talkchess.com/forum/viewtopic.php?t=52700) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), June 20, 2014

# External Links

## Chess Engine

- [Index of /chess/engines/Norbert's Collection/Sinobyl 1.5 release 29.11.2008](http://kirr.homeunix.org/chess/engines/Norbert%27s%20Collection/Sinobyl%201.5%20release%2029.11.2008/) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Latista (Sinobyl) 1.5](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?match_length=30&print=Details&each_game=1&eng=Latista%20%28Sinobyl%29%201.5#Latista_%28Sinobyl%29_1_5) in [CCRL 40/4](/CCRL "CCRL")
- [Latista (Sinobyl) 1.5](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Latista%20%28Sinobyl%29%201.5) in [KCEC](/KCEC "KCEC")
- [trunk/Sinobyl | SVN | Assembla](https://www.assembla.com/code/sinobyl/subversion/nodes/129/trunk/Sinobyl) ([NoraGrace](/NoraGrace "NoraGrace"))

## Misc

- [latista - Wiktionary](http://en.wiktionary.org/wiki/latista)

:   [latistaa - Wiktionary](http://en.wiktionary.org/wiki/latistaa)

- [Sino- - Wiktionary](http://en.wiktionary.org/wiki/Sino-)
- [Wordlist sinobyl... | Welsh Prose 1300-1425](http://www.rhyddiaithganoloesol.caerdydd.ac.uk/en/wordlist.php?prefix=sinobyl)
- [Chernobyl - Name origin | byllia (билля, grass blades or stalks)](https://en.wikipedia.org/wiki/Chernobyl#Name_origin)

# References

1. [↑](#cite_ref-1) [Re: new/updated engines: 2008/11/28-29](http://www.open-aurec.com/wbforum/viewtopic.php?p=187799&start=1#p187822) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 01, 2008
2. [↑](#cite_ref-2) [Latista](http://wbec-ridderkerk.nl/html/details1/Latista.html) from [WBEC Ridderkerk](/WBEC "WBEC")
3. [↑](#cite_ref-3) [trunk/Sinobyl | SVN | Assembla](https://www.assembla.com/code/sinobyl/subversion/nodes/129/trunk/Sinobyl)
4. [↑](#cite_ref-4) [New open source engine in C# - NoraGrace](http://www.talkchess.com/forum/viewtopic.php?t=52700) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), June 20, 2014
5. [↑](#cite_ref-5) [Latista 1.5](https://www.stmintz.com/ccc/index.php?id=479324) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), January 13, 2006
6. [↑](#cite_ref-6) [Latista 1.4 released. (Rybka killer edition!)](https://www.stmintz.com/ccc/index.php?id=472863) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), December 23, 2005

**[Up one Level](/Engines "Engines")**