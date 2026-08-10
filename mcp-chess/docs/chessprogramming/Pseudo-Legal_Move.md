# Pseudo-Legal Move

Source: https://www.chessprogramming.org/Pseudo-Legal_Move

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Moves](/Moves "Moves") \* Pseudo-Legal Move**

A **Pseudo-Legal Move** is legal in the sense that it is consistent with the current [board representation](/Board_Representation "Board Representation") it is assigned to, and it must be member of all pseudo legal [generated](/Move_Generation "Move Generation") moves for that [position](/Chess_Position "Chess Position") and [side to move](/Side_to_move "Side to move"). For a test of a given but not already generated move, the moving [piece](/Pieces "Pieces") on its valid origin [square](/Squares "Squares") of the [board](/Chessboard "Chessboard") must have a valid target square according to its possible move [directions](/Direction "Direction") and [distances](/Distance "Distance"). The [occupancy](/Occupancy "Occupancy") of the target square in conjunction with its piece [color](/Color "Color") (if any piece), or in case of distant sliding moves and double pawn pushes, the occupancy of squares between origin and target must be further considered, to determine the move is pseudo legal [quiet](/Quiet_Moves "Quiet Moves") or [capture](/Captures "Captures") (including [promotion](/Promotions "Promotions")). [En passant](/En_passant "En passant") needs the target square trigger set from previous double push and special square tests. [Castling](/Castling "Castling") requires appropriate [castling rights](/Castling_Rights "Castling Rights"), [occupancy](/Occupancy "Occupancy")- and attacking square checks.

Pseudo-legal moves may still be **illegal** if they leave the own [king](/King "King") in [check](/Check "Check"), most often if the king was already in check before, or the moving piece was [absolutely pinned](/Pin#AbsolutePin "Pin"). Pseudo-legal moves versus strictly [legal moves](/Legal_Move "Legal Move") is a matter of [move generation](/Move_Generation "Move Generation"), and also playing [hash](/Hash_Move "Hash Move")- or even [killer moves](/Killer_Move "Killer Move") immediately without explicit move generation, but a [pseudo legality test](/Square_Attacked_By#LegalityTest "Square Attacked By").

# See also

- [Legal Move](/Legal_Move "Legal Move")
- [Influence Quantity of Pieces](/Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
- [Pseudo Legality Test](/Square_Attacked_By#LegalityTest "Square Attacked By") with [Bitboards](/Bitboards "Bitboards")
- [Move Generation](/Move_Generation "Move Generation")

# Forum Posts

- [Do you use illigal moves in the ply zero and 1?](https://www.stmintz.com/ccc/index.php?id=79074) by [Leonid](/Leonid_Liberman "Leonid Liberman"), [CCC](/CCC "CCC"), November 22, 1999
- [I just discovered a design flaw in my engine](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73479) by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), [CCC](/CCC "CCC"), March 27, 2020

# External Links

- [Move generation](http://mediocrechess.blogspot.de/2006/12/guide-move-generation.html) from [Mediocre Chess](http://mediocrechess.blogspot.com/) by [Jonatan Pettersson](/Jonatan_Pettersson "Jonatan Pettersson"), December 18, 2006

**[Up one Level](/Moves "Moves")**