# King Centralization

Source: https://www.chessprogramming.org/King_Centralization

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Game Phases](/Game_Phases "Game Phases") \* [Endgame](/Endgame "Endgame") \* King Centralization**

**King Centralization**,  
an endgame evaluation feature as used in some engines to encourage the [king](/King "King") to become a more active piece in the endgame, when due to appropriate reduced material [king safety](/King_Safety "King Safety") is less important. From the [center](/Center "Center"), the king has more possibilities to reach upcoming critical areas of the board in time, i.e. to support own, or to attack or stop opponent [passers](/Passed_Pawn "Passed Pawn").

# Implementation

A common technique is to apply endgame [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") based on [center distance](/Center_Distance "Center Distance") and/or [center Manhattan-distance](/Center_Manhattan-Distance "Center Manhattan-Distance") penalties, likely interpolated by a [tapered eval](/Tapered_Eval "Tapered Eval") with their [opening](/Opening "Opening")/[middlegame](/Middlegame "Middlegame") counterpart of antipodal center edge relationship. King centralization interacts with [king pawn tropism](/King_Pawn_Tropism "King Pawn Tropism"), amplified the more central the gravity point of [passers](/Passed_Pawn "Passed Pawn") and possibly [weak pawns](/Weak_Pawns "Weak Pawns") is.

# See also

- [Center](/Center "Center")
- [Center Control](/Center_Control "Center Control")
- [Center Distance](/Center_Distance "Center Distance")
- [Center Manhattan-Distance](/Center_Manhattan-Distance "Center Manhattan-Distance")
- [King Pawn Tropism](/King_Pawn_Tropism "King Pawn Tropism")
- [Mop-up Evaluation](/Mop-up_Evaluation "Mop-up Evaluation")
- [Pawn Endgame](/Pawn_Endgame "Pawn Endgame")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Tapered Eval](/Tapered_Eval "Tapered Eval")

# Forum Posts

- [The king in the endgame](http://www.talkchess.com/forum/viewtopic.php?t=53523) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), August 31, 2014
- [Simple method for simple mates for programs without TBs](http://www.talkchess.com/forum/viewtopic.php?t=62257) by [J. Wesley Cleveland](/index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](/CCC "CCC"), November 25, 2016 » [KBNK Endgame](/KBNK_Endgame "KBNK Endgame"), [Mop-up Evaluation](/Mop-up_Evaluation "Mop-up Evaluation")

**[Up one Level](/Endgame "Endgame")**