# Mop-up Evaluation

Source: https://www.chessprogramming.org/Mop-up_Evaluation

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Game Phases](/Game_Phases "Game Phases") \* [Endgame](/Endgame "Endgame") \* Mop-up Evaluation**

**Mop-up Evaluation** might be applied at decided late endgame positions without any [pawns](/Pawn "Pawn"), where one side has a winning advantage to [checkmate](/Checkmate "Checkmate") and likely a [rook](/Rook "Rook") or [queen](/Queen "Queen") (or even two different colored [bishops](/Bishop "Bishop")). The winning side wants to drive the losing [king](/King "King") to the edges and corners, and has therefor a bonus for [Center distance](/Center_Distance "Center Distance") ([Center Manhattan-distance](/Center_Manhattan-Distance "Center Manhattan-Distance")) of the losing king, and a bonus for a minimum distance of both kings. In practice one often uses some term based on the (weighted) sum of the [Chebyshev distance](/Distance "Distance") and the [Manhattan distance](/Manhattan-Distance "Manhattan-Distance"), to have a higher bonus for the corners and straight rather than diagonal [opposition](/Opposition "Opposition").

# Chess 4.x

For instance, [Chess 4.x](/Chess_(Program) "Chess (Program)") Mop-up evaluation was based on sum of absolute [rank-](/Ranks#RankDistance "Ranks") and [file-distances](/Files#FileDistance "Files") [[1]](#cite_note-1), something like this (ignoring knights, which were equally considered like the king) from the stronger side of view:

```
PosEval = 4.7 * CMD + 1.6 * (14 - MD)
```

CMD is the Center Manhattan distance of the losing king and MD the Manhattan distance between both kings. Of course part of such terms might be covered by [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") of that very late game stage, and most of these positions are handled by [interior node recognizer](/Interior_Node_Recognizer "Interior Node Recognizer") nowadays.

# See also

- [Center Distance](/Center_Distance "Center Distance")
- [Center Manhattan-Distance](/Center_Manhattan-Distance "Center Manhattan-Distance")
- [KBNK Endgame](/KBNK_Endgame "KBNK Endgame")
- [KRK](/KRK "KRK")

# Forum Posts

- [Simple method for simple mates for programs without TBs](http://www.talkchess.com/forum/viewtopic.php?t=62257) by [J. Wesley Cleveland](/index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](/CCC "CCC"), November 25, 2016 » [Center Manhattan-Distance](/Center_Manhattan-Distance "Center Manhattan-Distance"), [KBNK Endgame](/KBNK_Endgame "KBNK Endgame")

# References

1. [↑](#cite_ref-1) [David Slate](/David_Slate "David Slate"), [Larry Atkin](/Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](/Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")

**[Up one Level](/Endgame "Endgame")**