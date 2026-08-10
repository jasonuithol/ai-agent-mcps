# Chess22k

Source: https://www.chessprogramming.org/Chess22k

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* chess22k**

**chess22k**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), written in [Java](/Java "Java") first released in January 2017 [[1]](#cite_note-1). While already in the 2400 Elo range using a 64-bit [Java Runtime Environment (JRE)](https://en.wikipedia.org/wiki/Java_virtual_machine), it has not initially implemented a [tapered evaluation](/Tapered_Eval "Tapered Eval"), but abrupt transition based on piece counts per side to distinguish between [middlegame](/Middlegame "Middlegame") and [endgame](/Endgame "Endgame") terms [[2]](#cite_note-2) [[3]](#cite_note-3). However, tapered evaluation was implemented in chess22k **1.5** along with new evaluation terms adjusted by [Texel's tuning method](/Texel%27s_Tuning_Method "Texel's Tuning Method") [[4]](#cite_note-4). In November 2017, chess22k had its over the board tournament debut, version **1.6** played the [CSVN](/CSVN "CSVN") [PT 52](/PT_52 "PT 52") in Leiden, quite successful - shared 4th place with 6/9. Soon released afterwards, chess22k **1.6** requires [Java 9](/Java#9 "Java") [[5]](#cite_note-5).

# Features

[[6]](#cite_note-6)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")

## [Search](/Search "Search")

- [Lazy SMP](/Lazy_SMP "Lazy SMP") (1.10)
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [Selectivity](/Selectivity "Selectivity")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Razoring](/Razoring "Razoring")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [SEE Pruning](/Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](/Evaluation "Evaluation")

- [Evaluation Hash Table](/Evaluation_Hash_Table "Evaluation Hash Table")
- [Tapered Eval](/Tapered_Eval "Tapered Eval") 1.5
- [Material](/Material "Material")
- [Bishop Pair](/Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
  - [Trapped Pieces](/Trapped_Pieces "Trapped Pieces")
  - [Rooks on (Semi) Open Files](/Rook_on_Open_File "Rook on Open File")
- [Outposts](/Outposts "Outposts")
- [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
  - [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [King Safety](/King_Safety "King Safety")
  - [Pawn Shelter](/King_Safety#PawnShield "King Safety")
- [Tactical Penalties](/Tactics "Tactics")
  - [In Check](/Check "Check")
  - [Hanging Pieces](/Hanging_Piece "Hanging Piece")
  - [Pinnned Pieces](/Pin "Pin")
- [Texel's Tuning Method](/Texel%27s_Tuning_Method "Texel's Tuning Method")

# Forum Posts

## 2017

- [chess22k v1.0](http://open-chess.org/viewtopic.php?t=3068) by [sandermvdb](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 13, 2017
- [New release: chess22k v1.1](http://www.talkchess.com/forum/viewtopic.php?t=63118) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), February 09, 2017
- [chess22k 1.2 released](http://www.talkchess.com/forum/viewtopic.php?t=63496) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), March 19, 2017
- [chess22k 1.3 released](http://www.talkchess.com/forum/viewtopic.php?t=63835) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), April 26, 2017
- [Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), June 05, 2017 » [Texel's Tuning Method](/Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Impressive Texel-tuning results](http://www.talkchess.com/forum/viewtopic.php?t=64310) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), June 16, 2017
- [chess22k 1.4 released](http://www.talkchess.com/forum/viewtopic.php?t=64337) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), June 18, 2017
- [chess22k 1.5 released](http://www.talkchess.com/forum/viewtopic.php?t=64869) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), August 12, 2017
- [chess22k 1.6 released](http://www.talkchess.com/forum/viewtopic.php?t=65714) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), November 13, 2017
- [chess22k 1.7 released](http://www.talkchess.com/forum/viewtopic.php?t=66171) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), December 28, 2017

## 2018

- [chess22k progress overview](http://www.talkchess.com/forum/viewtopic.php?t=66282) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), January 09, 2018
- [chess22k 1.8 released](http://www.talkchess.com/forum/viewtopic.php?t=66727) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), March 04, 2018
- [chess22k 1.9 released](http://www.talkchess.com/forum/viewtopic.php?t=67206) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), April 23, 2018
- [chess22k 1.10 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67941) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), July 09, 2018
- [chess22k 1.12 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69139) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), December 03, 2018

## 2019

- [chess22k 1.13 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71396) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), July 28, 2019

## 2020

- [chess22k 1.14 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73773) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), April 26, 2020

# External Links

- [GitHub - sandermvdb/chess22k](https://github.com/sandermvdb/chess22k)
- [chess22k 1.4 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=chess22k%201.4%2064-bit) in [CCRL 40/4](/CCRL "CCRL")

# References

1. [↑](#cite_ref-1)  [chess22k v1.0](http://open-chess.org/viewtopic.php?t=3068) by [sandermvdb](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 13, 2017
2. [↑](#cite_ref-2) public boolean isEndGame(int color) in [chess22k/ChessBoard.java at master · sandermvdb/chess22k · GitHub](https://github.com/sandermvdb/chess22k/blob/master/src/main/java/nl/s22k/chess/ChessBoard.java)
3. [↑](#cite_ref-3) isEndGame used in [chess22k/EvalUtil.java at master · sandermvdb/chess22k · GitHub](https://github.com/sandermvdb/chess22k/blob/master/src/main/java/nl/s22k/chess/eval/EvalUtil.java)
4. [↑](#cite_ref-4) [chess22k 1.5 released](http://www.talkchess.com/forum/viewtopic.php?t=64869) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), August 12, 2017
5. [↑](#cite_ref-5) [chess22k 1.6 released](http://www.talkchess.com/forum/viewtopic.php?t=65714) by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](/CCC "CCC"), November 13, 2017
6. [↑](#cite_ref-6) Based on readme and [GitHub - sandermvdb/chess22k](https://github.com/sandermvdb/chess22k)

**[Up one Level](/Engines "Engines")**