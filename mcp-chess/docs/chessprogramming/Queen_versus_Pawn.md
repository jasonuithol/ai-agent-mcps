# Queen versus Pawn

Source: https://www.chessprogramming.org/Queen_versus_Pawn

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Game Phases](/Game_Phases "Game Phases") \* [Endgame](/Endgame "Endgame") \* Queen versus Pawn**

The **Queen versus Pawn Endgame** (KQKP) is usually won by the queen side, in particular if the queen can occupy the pawn's [frontspan](/Pawn_Spans "Pawn Spans").
Even if the pawn is ready to [promote](/Promotions "Promotions"), supported by its own king, the technique is to come closer with the attacking king, after the defending king was forced to block the [promotion square](/Promotion_Square "Promotion Square") due to a queen check.
However, with rook and bishop pawns on the seventh (second) rank, [stalemate](/Stalemate "Stalemate") is looming with the defending king in the corner.
There are even some rare cases with center and knight pawns where the attacking king hinders its own queen to give check [[1]](#cite_note-1).
This endgame with pawn on the 7th rank often occurs after a [KPKP](/index.php?title=KPKP&action=edit&redlink=1 "KPKP (page does not exist)") [pawn race](/Pawn_Race "Pawn Race") with [unstoppable passers](/Unstoppable_Passer "Unstoppable Passer"), where the [cardinality](/Population_Count "Population Count") of their [frontspans](/Pawn_Spans "Pawn Spans") differs by two with the defending side to move.

# Rook Pawn on 7th

The [draw](/Draw "Draw") motive is a [stalemate](/Stalemate "Stalemate") threat, after the defending king blocks its own pawn after a queen check on the neighbouring knight file, so that the attacking king can't come closer.
A [Chebyshev distance](/Distance "Distance") of at least four to the [promotion square](/Promotion_Square "Promotion Square") with a [Manhattan distance](/Manhattan-Distance "Manhattan-Distance") less than eight for the attacking king is necessary to win that game (green area below).
However, there are positions where the attacking king may reduce the distance due to [discovered check](/Discovered_Check "Discovered Check").

|  |  |  |  |
| --- | --- | --- | --- |
| |  | | --- | |                                                                                                  ♕                           ♔                      ♟♚       ♚♚ | | |  | | --- | |                                                                                              ♕                       ♔                      ♟♚       ♚ | |
| Draw, ¬([♚](/King "King")[a1](/Squares "Squares") ∧ [♕](/Queen "Queen")[⤇](/Square_Control "Square Control")[c1](/Squares "Squares")) | Win due to [discovered check](/Discovered_Check "Discovered Check") |

# Bishop Pawn on 7th

A similar draw motive occurs here with [stalemate](/Stalemate "Stalemate") after the queen captured the bishop pawn.
The winning area of the attacking king is depending whether the defending king resides on the [lee-side](/Pawn_Spans "Pawn Spans") or [luff-side](/Pawn_Spans "Pawn Spans") .

## Lee case

The defending king on the [lee-side](/Pawn_Spans "Pawn Spans") is able to threaten [stalemate](/Stalemate "Stalemate") in the corner.
Critical squares are the neighbouring square on the [luff-side](/Pawn_Spans "Pawn Spans") (i.e. for black pawn on c2, d2),
and the diagonal neighbouring square on the lee-side one rank back (i.e. for black pawn on c2, b3).
Only if the attacking king can reach these squares in one move, it can assist in a [checkmate](/Checkmate "Checkmate") with the queen - otherwise it is a draw
- except the rare cases the attacking king may reduce the [Chebyshev distance](/Distance "Distance") accordantly, giving [discovered check](/Discovered_Check "Discovered Check") [[2]](#cite_note-2).

|  |  |  |  |
| --- | --- | --- | --- |
| |  | | --- | |                                                                                                  ♕                                   ♔      •        ♚♟•     ♚♚ | | |  | | --- | |                                                                                              ♕                               ♔      •        ♚♟•     ♚ | |
| Draw, ¬([♚](/King "King")[a1](/Squares "Squares") ∧ [♕](/Queen "Queen")[⤇](/Square_Control "Square Control")[c1](/Squares "Squares")) | Win due to [discovered check](/Discovered_Check "Discovered Check") |

## Luff case

When the defending king supports its pawn from the "wrong" [luff-side](/Pawn_Spans "Pawn Spans"), including occupying its [promotion square](/Promotion_Square "Promotion Square"),
the winning area for the attacking king is enlarged by at least one move, in luff-direction even two moves.
The critical luff-side square is now one file farther away (i.e. for black pawn on c2, e2), and one critical square needs to be reached in two moves now,
to either transpose to a winning [lee-side case](#Lee), or to assist in a checkmate on the luff-side.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| |  | | --- | |                                                                                   ♕            ♔            •         ♟♚•      ♚♚ | | |  | | --- | |                                                                       ♕       ♔            •         ♟♚• | | |  | | --- | |                                                                               ♕       ♔            •         ♟ •      ♚ | |
| Draw | Win due to [discovered check](/Discovered_Check "Discovered Check") | Draw since check parried by [Kb1/b2](#Lee) |

# See also

- [Draw Evaluation](/Draw_Evaluation "Draw Evaluation")
- [Interior Node Recognizer](/Interior_Node_Recognizer "Interior Node Recognizer")
- [KPKP](/index.php?title=KPKP&action=edit&redlink=1 "KPKP (page does not exist)")

# Publications

- [Reuben Fine](https://en.wikipedia.org/wiki/Reuben_Fine) (**1941**). *[Basic Chess Endings](https://archive.org/details/basicchessending00reub)*. [Bell & Sons](https://en.wikipedia.org/wiki/George_Bell_%26_Sons)
- [Yuri Averbakh](https://en.wikipedia.org/wiki/Yuri_Averbakh), Victor Henkin, [Vitaly Chekhover](https://en.wikipedia.org/wiki/Vitaly_Chekhover) (**1986**). *Comprehensive Chess Endings 3: Queen Endings*. [Pergamon Press](https://en.wikipedia.org/wiki/Pergamon_Press)
- [Karsten Müller](/Karsten_M%C3%BCller "Karsten Müller"), [Frank Lamprecht](https://en.wikipedia.org/wiki/Frank_Lamprecht) (**2001**). *[Fundamental Chess Endings](http://www.gambitbooks.com/books/Fundamental_Chess_Endings.html)*. [Gambit Publications](https://en.wikipedia.org/wiki/Gambit_Publications)
- [Reuben Fine](https://en.wikipedia.org/wiki/Reuben_Fine), [Pal Benko](https://en.wikipedia.org/wiki/Pal_Benko) (**2003**). *[Basic Chess Endings](https://en.wikipedia.org/wiki/Basic_Chess_Endings)*. [McKay](https://en.wikipedia.org/wiki/David_McKay_Publications)
- [Yasser Seirawan](https://en.wikipedia.org/wiki/Yasser_Seirawan) (**2003**). *[Winning Chess Endings](https://dl.acm.org/doi/book/10.5555/1200939)*. [Everyman Chess](https://en.wikipedia.org/wiki/Everyman_Chess)

# Forum Posts

- [Marcel Duchamp endgame "splits" engines / hash phenomenon](http://www.talkchess.com/forum/viewtopic.php?t=66640) by [Kenneth Regan](/Kenneth_W._Regan "Kenneth W. Regan"), [CCC](/CCC "CCC"), February 19, 2018 » [Chess Problems, Compositions and Studies](/Chess_Problems,_Compositions_and_Studies "Chess Problems, Compositions and Studies"), [Marcel Duchamp](/Category:Marcel_Duchamp "Category:Marcel Duchamp"), [Transposition Table](/Transposition_Table "Transposition Table")
- [KQKP and the like](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70827) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), May 25, 2019

# External Links

- [Queen versus pawn endgame from Wikipedia](https://en.wikipedia.org/wiki/Queen_versus_pawn_endgame)
- [Queen vs. Pawn on 7th‎](https://www.chess.com/article/view/queen-vs-pawn-on-7th) by TonightOnly, [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), July 12, 2008

# References

1. [↑](#cite_ref-1) [Queen versus pawn endgame - Central pawn or knight pawn | Wikipedia](https://en.wikipedia.org/wiki/Queen_versus_pawn_endgame#Central_pawn_or_knight_pawn)
2. [↑](#cite_ref-2) Lee-case implemented as [Interior Node Recognizer](/Interior_Node_Recognizer "Interior Node Recognizer") in [IsiChess](/IsiChess "IsiChess")

**[Up one Level](/Endgame "Endgame")**