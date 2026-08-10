# Bishops of Opposite Colors

Source: https://www.chessprogramming.org/Bishops_of_Opposite_Colors

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Game Phases](/Game_Phases "Game Phases") \* [Endgame](/Endgame "Endgame") \* Bishops of Opposite Colors**

The endgame in which both sides posses only pawns and **bishops of opposite colors** is notorious difficult to win, as the weaker side is likely to create a [blockade](/Blockade "Blockade") on the squares controlled by its own bishop. One pawn advantage is usually not enough to force the win. The chances for that exist either when the stronger side has either [passed pawns](/Passed_Pawn "Passed Pawn") on both wings or [connected passed pawns](/Connected_Passed_Pawns "Connected Passed Pawns"). In the latter case the winning method is to advance pawns in such a manner that they are placed on the squares controlled by enemy bishop, since it makes blockade impossible.

# Scaling down

A good idea for the evaluation function is to scale down the [material](/Material "Material") value when the pure bishop of opposite colors ending is encountered. If some more pieces beside the bishops are present on the board, winning the endgame is easier, but requires complex strategy, based rather on [zugzwang](/Zugzwang "Zugzwang") and attacking possibilities than on simply advancing passed pawns.

# See also

- [Color of a Square](/Color_of_a_Square "Color of a Square")
- [Color Weakness](/Color_Weakness "Color Weakness")
- [Bad Bishop](/Bad_Bishop "Bad Bishop")

# Forum Posts

- [Deep Thought.. What's this rules of Bishops?](http://groups.google.com/group/rec.games.chess/browse_frm/thread/8ad3bbb2760134b0#) by Aravind Anumala, [rgc](/Computer_Chess_Forums "Computer Chess Forums"), April 11, 1995
- [Hossa - Crafty : bishop endgame](https://www.stmintz.com/ccc/index.php?id=75112) by [Steffen A. Jakob](/Steffen_A._Jakob "Steffen A. Jakob"), [CCC](/CCC "CCC"), October 27, 1999 » [Hossa](/Hossa "Hossa"), [Crafty](/Crafty "Crafty")
- [Opposite Color Bishop Ending](https://www.stmintz.com/ccc/index.php?id=79939) by [Howard Exner](/index.php?title=Howard_Exner&action=edit&redlink=1 "Howard Exner (page does not exist)"), [CCC](/CCC "CCC"), November 29, 1999
- [Test position (opposite colour bishop)..very hard for chess engines](https://www.stmintz.com/ccc/index.php?id=448548) by Masros Tukiran, [CCC](/CCC "CCC"), September 08, 2005

# External Links

- [Opposite-colored bishops endgame from Wikipedia](https://en.wikipedia.org/wiki/Opposite-colored_bishops_endgame)
- [Opposite-colored bishops | Fortress (chess) from Wikipedia](https://en.wikipedia.org/wiki/Fortress_%28chess%29#Opposite-colored_bishops)
- [Bishops of opposite colors, Bishop & Two Connected passed pawns](http://www.jeremysilman.com/chess_adv_endgm/040410_bschp_of_tw_cllrs.html) by [Jeremy Silman](https://en.wikipedia.org/wiki/Jeremy_Silman)

**[Up one Level](/Endgame "Endgame")**