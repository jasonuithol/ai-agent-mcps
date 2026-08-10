# Tarrasch Rule

Source: https://www.chessprogramming.org/Tarrasch_Rule

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [of Pieces](/Evaluation_of_Pieces "Evaluation of Pieces") \* Tarrasch Rule**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Tarrasch_72.jpg/250px-Tarrasch_72.jpg)](/File:Tarrasch_72.jpg)

[Siegbert Tarrasch](https://en.wikipedia.org/wiki/Siegbert_Tarrasch) [[1]](#cite_note-1)

The **Tarrasch Rule**,   
formulated by [Siegbert Tarrasch](https://en.wikipedia.org/wiki/Siegbert_Tarrasch), is a [rule of thumb](https://en.wikipedia.org/wiki/Rule_of_thumb) (heuristic) applied in [endgames](/Endgame "Endgame") and sometimes (late) [middlegames](/Middlegame "Middlegame") with [passed pawn(s)](/Passed_Pawn "Passed Pawn") and [rook(s)](/Rook "Rook") involved. Rooks should be placed "behind" own passers as well as [candidates](/Candidate_Passed_Pawn "Candidate Passed Pawn") to support them, as well "behind" opponent passers to hold them.

# Advantage

The advantage of a rook intersecting the passers [rear span](/Pawn_Spans "Pawn Spans") is that it does not hinder the passer from [queening](/Promotions "Promotions"), but indirectly controls its [stop square](/Stop_Square "Stop Square") with increasing vertical rook [mobility](/Mobility "Mobility") the more the passer advances. Since the passers rear spans might also be occupied by other pieces, specially own or opponent file-immobile pawns, the passer should actually be defended or attacked by a rook from south (white passer) or north (black passer). Alternatively, with [bitboards](/Bitboards "Bitboards") and [fill stuff](/Fill_Algorithms "Fill Algorithms") in mind, to determine the relevant subset of the rear span, the north- or south [Dumb7-](/Dumb7Fill#OccludedFill "Dumb7Fill") or [Kogge-Stone occluded fill](/Kogge-Stone_Algorithm#OccludedFill "Kogge-Stone Algorithm") might be applied, only with pawns of both sides as obstructions.

:   |  |
    | --- |
    |                                                     ♙           ♟ |

The green squares of the rear spans are good squares for either white or black rooks

# See also

- [Blockade of Stop](/Blockade_of_Stop "Blockade of Stop")
- [Rook Endgame](/Rook_Endgame "Rook Endgame")
- [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [Pawn Spans](/Pawn_Spans "Pawn Spans")

# External Links

- [Tarrasch rule from Wikipedia](https://en.wikipedia.org/wiki/Tarrasch_rule)

# References

1. [↑](#cite_ref-1) [Tarrasch rule from Wikipedia](https://en.wikipedia.org/wiki/Tarrasch_rule)

**[Up one Level](/Evaluation_of_Pieces "Evaluation of Pieces")**