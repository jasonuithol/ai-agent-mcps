# NagaSkaki

Source: https://www.chessprogramming.org/NagaSkaki

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* NagaSkaki**

[![](/images/thumb/f/f0/Nagaskaki_grab.jpg/300px-Nagaskaki_grab.jpg)](/File:Nagaskaki_grab.jpg)

Screen capture of NagaSkaki 5.00 [[1]](#cite_note-1)

**NagaSkaki**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess program by [Neels Groenewald](/Neels_Groenewald "Neels Groenewald") with an own [graphical user interface](/GUI "GUI"). Various [evaluation](/Evaluation "Evaluation") features such as [point values](/Point_Value "Point Value") are adjustable through personality sections inside an ini-file.

# Features

## [Board Representation](/Board_Representation "Board Representation")

[[2]](#cite_note-2)

- [Bitboards](/Bitboards "Bitboards")
- [Classical Board Definition](/Bitboard_Board-Definition#CBoardDef "Bitboard Board-Definition")
- [Shifted Bitboards](/Shifted_Bitboards "Shifted Bitboards")

## [Search](/Search "Search")

[[3]](#cite_note-3)

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [MVV/LVA](/MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
- [Selectivity](/Selectivity "Selectivity")
  - [Pruning](/Pruning "Pruning")
    - [Futility Pruning](/Futility_Pruning "Futility Pruning")
    - [Extended Futility Pruning](/Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
    - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Extensions](/Extensions "Extensions")
    - [Check Extensions](/Check_Extensions "Check Extensions")
    - [Passed Pawn Extensions](/Passed_Pawn_Extensions "Passed Pawn Extensions")
    - [Recapture Extensions](/Recapture_Extensions "Recapture Extensions")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")

## [Evaluation](/Evaluation "Evaluation")

[[4]](#cite_note-4)

- [Material](/Material "Material")
  - [Point Values](/Point_Value "Point Value") (100, 310, 320, 500, 1000) [[5]](#cite_note-5)
  - [Bishop Pair](/Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
  - [Trapped Pieces](/Trapped_Pieces "Trapped Pieces")
  - [Rooks on (Semi) Open Files](/Rook_on_Open_File "Rook on Open File")
- [Knight Outposts](/Outposts "Outposts")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
  - [Backward Pawn](/Backward_Pawn "Backward Pawn")
  - [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
  - [Connected Pawns](/Connected_Pawns "Connected Pawns")
  - [Passed Pawn](/Passed_Pawn "Passed Pawn")
    - [Unstoppable Passer](/Unstoppable_Passer "Unstoppable Passer")
    - [Tarrasch Rule](/Tarrasch_Rule "Tarrasch Rule")
- [King Safety](/King_Safety "King Safety")
  - [Castling Rights](/Castling_Rights "Castling Rights")
  - [Pawn Shield](/King_Safety#PawnShield "King Safety")
  - [King Piece Tropism](/King_Safety#KingTropism "King Safety")
  - [Attacking King Zone](/King_Safety#Attacking "King Safety")
  - [King](/King "King") close to [Open File](/Open_File "Open File")

# Forum Posts

- [Nagaskaki ( what a name for a chess program)](https://www.stmintz.com/ccc/index.php?id=315876) by Jorge Pichard, [CCC](/CCC "CCC"), September 14, 2003
- [Nagaskaki chess program](https://www.stmintz.com/ccc/index.php?id=340817) by Lyn Harper, [CCC](/CCC "CCC"), January 07, 2004
- [NagaSkaki 4.0](https://www.stmintz.com/ccc/index.php?id=480627) by Robert Hollay, [CCC](/CCC "CCC"), January 18, 2006
- [NagaSkaki 5.00 - nice free engine with GUI](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=20953) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), May 02, 2008
- [NagaSkaki 5.12 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=21102) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), May 13, 2008
- [NagaSkaki](https://www.hiarcs.net/forums/viewtopic.php?t=10290) by TomFurga, [Hiarcs Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 18, 2020

# External Links

- [NagaSkaki](https://mayothi.com/nagaskaki.html)
- [NagaSkaki](https://web.archive.org/web/20111007181515/http://www.mayothi.com/nagaskaki.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), October 07, 2011)
- [NagaSkaki: A Free chess program for Windows](http://mysite.mweb.co.za/residents/lollapot/homepage.html) (2003, NagaSkaki 2.0)
- [NagaSkaki 5.12](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=NagaSkaki%205.12#NagaSkaki_5_12) in [CCRL 40/15](/CCRL "CCRL")

# References

1. [↑](#cite_ref-1) [NagaSkaki](https://mayothi.com/nagaskaki.html)
2. [↑](#cite_ref-2) [How NagaSkaki plays chess - Move generation](https://mayothi.com/nagaskakichess6.html)
3. [↑](#cite_ref-3) [How NagaSkaki plays chess - The thinking process](https://mayothi.com/computerschess.html)
4. [↑](#cite_ref-4) [How NagaSkaki plays chess - Evaluation](https://web.archive.org/web/20111012015457/http://mayothi.com/nagaskakichess4.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
5. [↑](#cite_ref-5) Default values may be adjusted via ini-file

**[Up one level](/Engines "Engines")**