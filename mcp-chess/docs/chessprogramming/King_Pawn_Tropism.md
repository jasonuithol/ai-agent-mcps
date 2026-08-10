# King Pawn Tropism

Source: https://www.chessprogramming.org/King_Pawn_Tropism

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Game Phases](/Game_Phases "Game Phases") \* [Endgame](/Endgame "Endgame") \* King Pawn Tropism**

**King Pawn Tropism**,  
an endgame evaluation feature concerning the [distance](/Distance "Distance") of a [king](/King "King") to [pawns](/Pawn "Pawn"), with the motivation to either defend or support own ones, or to attack or block opponent ones - in both cases, the closer the better.

# Implementation

A common way to implement tropism is to calculate the average [Manhattan-distance](/Manhattan-Distance "Manhattan-Distance") of the king square to all pawn squares, weighted by some factor to consider [passed](/Passed_Pawn "Passed Pawn") and [weak pawns](/Weak_Pawns "Weak Pawns") (i.e. 6:3:2 for passers, [backward](/Backward_Pawn "Backward Pawn") and remaining pawns as applied in [Bobby](/Bobby "Bobby") and also [Kraas'](/Hans-Joachim_Kraas "Hans-Joachim Kraas") and [Schrüfer's](/G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") didactic [Basic](/Basic "Basic") program [Demoschach](/index.php?title=Demoschach&action=edit&redlink=1 "Demoschach (page does not exist)"), described in *Das große Computerschachbuch* [[1]](#cite_note-1)). Two accumulators are used to aggregate all the Manhattan-distances times weight, and all the weights as well, to finally divide the weighted sum of distances by the number of pawn weights for an average distance

[![KingPawnTropism.jpg](/images/c/ca/KingPawnTropism.jpg)](/File:KingPawnTropism.jpg)

in the 1..14 Manhattan range, somehow interpreted as penalty for the king side.

# See also

- [King Centralization](/King_Centralization "King Centralization")
- [Pawn Endgame](/Pawn_Endgame "Pawn Endgame")
- [Réti Endgame Study](/R%C3%A9ti_Endgame_Study "Réti Endgame Study")
- [Rule of the Square](/Rule_of_the_Square "Rule of the Square")
- [King Piece Tropism](/King_Safety#KingTropism "King Safety")
- [Unstoppable Passer](/Unstoppable_Passer "Unstoppable Passer")

# External Links

- [tropism - Wiktionary](http://en.wiktionary.org/wiki/tropism)
- [Tropism from Wikipedia](https://en.wikipedia.org/wiki/Tropism)

# References

1. [↑](#cite_ref-1) [Rainer Bartel](http://www.rainerbartel.de/), [Hans-Joachim Kraas](/Hans-Joachim_Kraas "Hans-Joachim Kraas"), [Günther Schrüfer](/G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") (**1985**). *[Das große Computerschachbuch](http://www.c64-wiki.de/index.php/Das_grosse_Computerschachbuch)*. [Data Becker](https://en.wikipedia.org/wiki/Data_Becker), ISBN 3-89011-117-3 (German), [amazon.de](http://www.amazon.de/Das-gro%C3%9Fe-Computerschachbuch-Rainer-Bartel/dp/3890111173), pp. 258, Verfahren zur Bewertung der Königsaktivität, 2. Mittlerer Abstand zwischen König und Bauern

**[Up one Level](/Endgame "Endgame")**