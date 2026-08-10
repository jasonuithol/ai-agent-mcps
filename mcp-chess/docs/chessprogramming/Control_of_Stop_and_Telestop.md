# Control of Stop and Telestop

Source: https://www.chessprogramming.org/Control_of_Stop_and_Telestop

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Pawn Structure](/Pawn_Structure "Pawn Structure") \* [Passed Pawn](/Passed_Pawn "Passed Pawn") \* Control of Stop and Telestop**

**Control of Stop and Telestop**,  
an evaluation feature considering [square control](/Square_Control "Square Control") of passed pawn's [front spans](/Pawn_Spans#FrontAndRearspans "Pawn Spans"), their [stop and telestops](/Pawn_Spans#StopandDistantStop "Pawn Spans") including [promotion square](/Promotion_Square "Promotion Square"). Specially in late endgames, if the opponent king is [outside the square](/Rule_of_the_Square "Rule of the Square") of a passer, it might be decisive for the opponent to control the stop or at least one telestop with a piece to dynamically prevent the passer from further advancement or even [queening](/Promotions "Promotions"), or to [blockade the stop](/Blockade_of_Stop "Blockade of Stop") in time. While rooks (and queens) may control the front span indirectly from behind as considered by the [Tarrasch rule](/Tarrasch_Rule "Tarrasch Rule"), light pieces require direct control of the front span. If stops and telestops are not yet directly controlled, one may even apply [fill-algorithms](/Fill_Algorithms "Fill Algorithms") to determine sets of squares controlled in one move, to look whether they [intersect](/General_Setwise_Operations#Intersection "General Setwise Operations") the telestops.

# See also

- [Blockade of Stop](/Blockade_of_Stop "Blockade of Stop")
- [Square Control](/Square_Control "Square Control")
- [Stop Square](/Stop_Square "Stop Square")
- [Tarrasch Rule](/Tarrasch_Rule "Tarrasch Rule")

**[Up one Level](/Passed_Pawn "Passed Pawn")**