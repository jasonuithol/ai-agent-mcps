# Square Control

Source: https://www.chessprogramming.org/Square_Control

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Squares](/Squares "Squares") \* Control**

[![](https://upload.wikimedia.org/wikipedia/commons/d/d0/Piet_Program.gif)](/File:Piet_Program.gif)

Piet [[1]](#cite_note-1)

**Square Control**,  
refers to which and how many pieces [attack](/Attacks "Attacks") or defend a particular square, independently from its [occupancy](/Occupancy "Occupancy") state. Squares diagonally [controlled](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)") by a pawn are usually taboo for opponent pieces, but the [stop](/Stop_Square "Stop Square") and possible [pawn push](/Pawn_Push "Pawn Push") [target square](/Target_Square "Target Square") is not controlled by the pawn itself, and could be [blocked](/Blockade "Blockade"). If the square under investigation is occupied, the question arises whether the piece is [hanging](/Hanging_Piece "Hanging Piece") (if controlled exclusively by the opponent side) or [en prise](/En_prise "En prise"), which is topic of [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") and [quiescence search](/Quiescence_Search "Quiescence Search").

# In Evaluation

Square control is considered in [evaluating](/Evaluation "Evaluation") piece [mobility](/Mobility "Mobility") and [connectivity](/Connectivity "Connectivity"), [controls of squares around the king](/King_Safety#SquareControl "King Safety") are matter of [king safety](/King_Safety "King Safety") evaluation, and [center control](/Center_Control "Center Control") might be considered as evaluation term in the [opening](/Opening "Opening") or [middlegame](/Middlegame "Middlegame"). Control of [stop and telestop](/Pawn_Spans#StopandDistantStop "Pawn Spans") squares of [passers](/Passed_Pawn "Passed Pawn") is another evaluation topic. Some programs calculate a square control balance as difference of the sums of [reciprocal piece values](/Point_Value#Reciprocal "Point Value") of both sides, and further aggregate the controls over all squares, possibly already considering [center](/Center "Center"), king areas and passed pawn [front spans](/Pawn_Spans "Pawn Spans") by a weight matrix.

# See also

- [Attack and Defend Maps](/Attack_and_Defend_Maps "Attack and Defend Maps")
- [Attacks](/Attacks "Attacks")
- [Center Control](/Center_Control "Center Control")
- [Color Weakness](/Color_Weakness "Color Weakness")
- [Connectivity](/Connectivity "Connectivity")
- [Control of Stop and Telestop](/Control_of_Stop_and_Telestop "Control of Stop and Telestop")
- [En prise](/En_prise "En prise")
- [Guard Heuristic](/Guard_Heuristic "Guard Heuristic")
- [Hanging Piece](/Hanging_Piece "Hanging Piece")
- [Mobility](/Mobility "Mobility")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Square Attacked By](/Square_Attacked_By "Square Attacked By")
- [Square Control in King Safety](/King_Safety#SquareControl "King Safety")
- [Square Control in SOMA](/SOMA#SquareControl "SOMA")
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Strategic Test Suite](/Strategic_Test_Suite "Strategic Test Suite")

# Publications

- [Chrilly Donninger](/Chrilly_Donninger "Chrilly Donninger") (**2006**). *Plättchen zählen*. [pdf](https://brigitte-godot.com/wp-content/uploads/2018/03/PlaettchenZaehlen.pdf) (German) » [Mobility](/Mobility "Mobility")

# Forum Posts

- [Binders](http://www.talkchess.com/forum/viewtopic.php?t=55214) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 04, 2015 » [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [Empty!](http://www.talkchess.com/forum/viewtopic.php?t=55342) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 14, 2015
- [Pawn defence](http://www.talkchess.com/forum/viewtopic.php?t=55380) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 18, 2015
- [Identifying weak squares](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77674) by Jon12345, [CCC](/CCC "CCC"), July 08, 2021

# External Links

- [Control of the center | Chess strategy from Wikipedia](https://en.wikipedia.org/wiki/Chess_strategy#Control_of_the_center)
- [RKeTZ](http://www.janklare.de/klare/wordpress/?page_id=1078) - Ground Control, [Lokal Harmonie](http://www.lokal-harmonie.de/), [Duisburg Ruhrort](https://en.wikipedia.org/wiki/Ruhrort), April 2016, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Jan Klare](/Category:Jan_Klare "Category:Jan Klare"), [Luc Ex](https://nl.wikipedia.org/wiki/Luc_Ex), [Michael Vatcher](https://de.wikipedia.org/wiki/Michael_Vatcher), [Achim Zepezauer](/Category:Achim_Zepezauer "Category:Achim Zepezauer")

# References

1. [↑](#cite_ref-1) Program in the [Piet programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language#Piet), printing "Piet", by [Thomas Schoch](https://commons.wikimedia.org/wiki/User:Mosmas), February 26, 2006, see [Obfuscated Programming – Piet](http://www.retas.de/thomas/computer/programs/useless/piet/Piet/index.html), Piet was named after the Dutch painter [Piet Mondrian](/Category:Piet_Mondrian "Category:Piet Mondrian"), [DM's Esoteric Programming Languages - Piet](http://www.dangermouse.net/esoteric/piet.html)

**[Up one Level](/Squares "Squares")**