# Promotion Square

Source: https://www.chessprogramming.org/Promotion_Square

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Squares](/Squares "Squares") \* Promotion Square**

The **Promotion Square** is the farthest [telestop](/Pawn_Spans#StopandDistantStop "Pawn Spans") of a [pawn](/Pawn "Pawn"). It is the square on the same [file](/Files "Files") on opponent's [back rank](/Ranks "Ranks") where finally a [promotion](/Promotions "Promotions") of the pawn would happen, assuming non-capturing [pawn pushes](/Pawn_Push "Pawn Push"). The promotion square can easily calculated from the pawn [origin](/Origin_Square "Origin Square") and [color](/Color "Color") of the pawn, by adding the file to the respective back rank offset (assuming [Little endian file and rank coordinates](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") here):

```
promotionSquare ::= ((color-1) & 56) + (pawnSquare & 7);  // white = 0, black = 1
```

# See also

- [Pawn Spans](/Pawn_Spans "Pawn Spans") in [Bitboards](/Bitboards "Bitboards")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [Promotions](/Promotions "Promotions")
- [Stop Square](/Stop_Square "Stop Square")

# Forum Posts

- [making code color independant](https://www.stmintz.com/ccc/index.php?id=334247) by [Georg von Zimmermann](/Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](/CCC "CCC"), December 08, 2003

**[Up one Level](/Squares "Squares")**