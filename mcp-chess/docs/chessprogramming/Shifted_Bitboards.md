# Shifted Bitboards

Source: https://www.chessprogramming.org/Shifted_Bitboards

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Shifted Bitboards**

**Shifted Bitboards**,  
an method to determine sliding piece attacks introduced by [Neels Groenewald](/Neels_Groenewald "Neels Groenewald") as implemented in his engine [NagaSkaki](/NagaSkaki "NagaSkaki") [[1]](#cite_note-1).
The idea is original and does not need huge memory tables. However, with the proposed 56 64-bit operations for either rook and bishop attacks its [space-time tradeoff](/Space-Time_Tradeoff "Space-Time Tradeoff") seems not that advantageous with respect to time, which looks more in the range of set-wise [fill algorithms](/Fill_Algorithms "Fill Algorithms") for multiple sliders, like [dumb7fill](/Dumb7Fill "Dumb7Fill") or its parallel prefix [Kogge-Stone](/Kogge-Stone_Algorithm "Kogge-Stone Algorithm") pendant.

# Description

Shifted Bitboards work ray-wise and uses pre-calculated [ray-attacks](/On_an_empty_Board#RayAttacks "On an empty Board") on the otherwise empty board for each of the eight [ray-directions](/Rays#RayDirections "Rays") for all [origin squares](/Origin_Square "Origin Square"),
and [intersects](/General_Setwise_Operations#Intersection "General Setwise Operations") one of them with the [occupancy](/Occupancy "Occupancy") to determine the blockers on the attacking [ray](/Rays "Rays") in question,
quite similar to the [Classical Approach](/Classical_Approach "Classical Approach"). While the Classical Approach performs a [bitscan](/BitScan "BitScan"), either [forward](/BitScan#Bitscanforward "BitScan") or [reverse](/BitScan#Bitscanreverse "BitScan") to determine the first blocker (if any) for the covered ray-attack [exclusion](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations") by a ray-square lookup,
Shifted Bitboards performs a [fill-like](/Fill_Algorithms "Fill Algorithms") [union](/General_Setwise_Operations#Union "General Setwise Operations") of all six [direction shifts](/General_Setwise_Operations#ShiftingBitboards "General Setwise Operations") of the blocker(s) from one to six (the maximum amount of covered squares behind a blocker), which were then [excluded](/General_Setwise_Operations#XorWithout "General Setwise Operations") from the initial [empty board ray-wise attack set](/On_an_empty_Board#RayAttacks "On an empty Board").

```
U64 rayAttacks[8][64]; // requires initialization

U64 getRightRayAttacks(U64 occupied, enumSquare square) {
   U64 attacks = rayAttacks[right][square];
   U64 blocker = attacks & occupied;
   if ( blocker ) {
      blocker = (blocker << 1) | (blocker << 2)
              | (blocker << 3) | (blocker << 4)
              | (blocker << 5) | (blocker << 6);
      attacks ^= (blocker & attacks);
   }
   return attacks;
}
```

# See also

- [Classical Approach](/Classical_Approach "Classical Approach")
- [Bitfoot - A/B Bitboards](/Bitfoot#ABBitboards "Bitfoot")
- [Blockers and Beyond](/Blockers_and_Beyond "Blockers and Beyond")
- [Obstruction Difference](/Obstruction_Difference "Obstruction Difference")

# External Links

- [How NagaSkaki plays chess - Move generation](https://mayothi.com/nagaskakichess6.html)
- [How NagaSkaki plays chess - Move generation](https://web.archive.org/web/20120104163142/http://www.mayothi.com/nagaskakichess6.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), January 04, 2012)
- [How NagaSkaki plays chess](http://mysite.mweb.co.za/residents/lollapot/nagaskaki_chess.html) (2002, NagaSkaki 2.0)

# References

1. [↑](#cite_ref-1) [How NagaSkaki plays chess - Move generation](https://mayothi.com/nagaskakichess6.html)

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**