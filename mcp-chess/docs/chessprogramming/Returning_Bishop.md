# Returning Bishop

Source: https://www.chessprogramming.org/Returning_Bishop

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [of Pieces](/Evaluation_of_Pieces "Evaluation of Pieces") \* Returning Bishop**

The term **returning bishop** refers to a bishop that went back to its original square after allowing own king to castle in the same direction. The typical example would be something like that: 1.e4 c5 2.Nf3 Nc6 3.Bb5 d6 4.0-0 Bd7 5. c3 Nf6 6.Re1 a6 7.Bf1.

Simplistic [piece-square](/Piece-Square_Tables "Piece-Square Tables") evaluation would treat such a bishop as undeveloped. Yet it is a good defender and, more importantly, "[developing](/Development "Development")" it would waste another [tempo](/Tempo "Tempo"). For that reasons it might be beneficial to assign a bonus erasing the development penalty for such a bishop.

The idea has been proposed (or just reinvented?) by [Pawel Koziol](/Pawel_Koziol "Pawel Koziol").

**[Up one Level](/Evaluation_of_Pieces "Evaluation of Pieces")**