# Undermining

Source: https://www.chessprogramming.org/Undermining

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Tactics](/Tactics "Tactics") \* Undermining**

**Undermining** is a chess tactic where an opponent guard, defending an attacked piece, is captured. While the removed guard itself is usually not [en prise](/En_prise "En prise") and the attacker even has a negative [static exchange evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation"), the point is that there is no recapture available to perpetuate the guards defensive obligations, and leaving a former attacked but guarded piece en prise, with a final net gain for the attacker. Those pattern may be considered in [quiescence search](/Quiescence_Search "Quiescence Search") to encourage capturing pawns and pieces with otherwise negative SEE ...

# Sample

... like Rxc7, capturing the lonesome guard of Be6:

|  |
| --- |
|                                                                                                    ♚       ♞   ♟     ♝♝           ♟                         ♙    ♖ ♖  ♔ |

```
3k4/2n3p1/3bb3/7p/8/8/6P1/2R1R2K w - -
```

# Counter Sample

If the undermined piece has a [Zwischenzug](/Zwischenzug "Zwischenzug"), things are more complicated. Here quiescence has to deal with [checks](/Check "Check") below the [horizon](/Horizon_Node "Horizon Node"), to become aware undermining does not work here ...

|  |
| --- |
|                                                                                                    ♚       ♞   ♟     ♝♝           ♟                ♙             ♖ ♖  ♔ |

```
3k4/2n3p1/3bb3/7p/8/6P1/8/2R1R2K w - -
```

# See also

- [Combination](/Combination "Combination")
- [Deflection](/index.php?title=Deflection&action=edit&redlink=1 "Deflection (page does not exist)")
- [En prise](/En_prise "En prise")
- [Overloading](/Overloading "Overloading")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Square Attacked By](/Square_Attacked_By "Square Attacked By")
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Strategic Test Suite](/Strategic_Test_Suite "Strategic Test Suite")

# External Links

- [Undermining (chess) from Wikipedia](https://en.wikipedia.org/wiki/Undermining_%28chess%29)
- [Undermine disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/Undermine)

**[Up one Level](/Tactics "Tactics")**