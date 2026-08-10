# Passed Pawn Extensions

Source: https://www.chessprogramming.org/Passed_Pawn_Extensions

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Extensions](/Extensions "Extensions") \* Passed Pawn Extensions**

**Passed Pawn Extensions** are triggered after a [passed pawn](/Passed_Pawn "Passed Pawn") is established on the seventh or sometimes sixth rank, that is after a [pawn push](/Pawn_Push "Pawn Push") or [captures](/Captures "Captures") with a [pawn](/Pawn "Pawn"). The idea is to avoid [horizon effects](/Horizon_Effect "Horizon Effect") regarding a possible [promotion](/Promotions "Promotions"), and to determine whether the [stop-](/Stop_Square "Stop Square") or [promotion square](/Promotion_Square "Promotion Square") is or may blocked, defended or supported. Clearly, this extension heavily interacts with the [evaluation](/Evaluation "Evaluation") of passed pawns, and may also restricted to certain [node types](/Node_Types "Node Types") and distance to horizon. Some programs also extend promotions itself and not only if there starts a threat to promote.

# Colin Frayn

[Colin Frayn](/Colin_Frayn "Colin Frayn") on Pawn Push Extensions [[1]](#cite_note-1):

1. If a pawn is pushed to the 7th rank, or promoted, then extend.
2. This helps spot winning tactics in the endgame.
3. Not so useful if your endgame analysis function is good enough at handling passed pawns.

# Forum Posts

- [Passed Pawn Extensions](https://www.stmintz.com/ccc/index.php?id=112415) by [Roberto Waldteufel](/Roberto_Waldteufel "Roberto Waldteufel"), [CCC](/CCC "CCC"), May 24, 2000
- [passed pawn extension](https://www.stmintz.com/ccc/index.php?id=210570) by [James Swafford](/James_Swafford "James Swafford"), [CCC](/CCC "CCC"), January 28, 2002
- [PASSED\_PAWN\_PUSH extension scheme (and SmarThink)](https://www.stmintz.com/ccc/index.php?id=252677) by [Sergei S. Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), September 18, 2002
- [Adding an Extension Results in Deeper General Search!](http://www.talkchess.com/forum/viewtopic.php?t=56311) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), May 10, 2015

# External Links

- [Computer Chess Programming Theory - Search Extensions](http://www.frayn.net/beowulf/theory.html#extend) by [Colin Frayn](/Colin_Frayn "Colin Frayn")

# References

1. [↑](#cite_ref-1) [Computer Chess Programming Theory - Search Extensions](http://www.frayn.net/beowulf/theory.html#extend) by [Colin Frayn](/Colin_Frayn "Colin Frayn")

**[Up one Level](/Extensions "Extensions")**