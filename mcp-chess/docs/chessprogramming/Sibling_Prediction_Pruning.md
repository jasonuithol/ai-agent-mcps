# Sibling Prediction Pruning

Source: https://www.chessprogramming.org/Sibling_Prediction_Pruning

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Pruning](/Pruning "Pruning") \* Sibling Prediction Pruning**

**Sibling Prediction Pruning**,  
a forward pruning technique at [frontier nodes](/Frontier_Nodes "Frontier Nodes") ([depth](/Depth "Depth") == 1) introduced by [Jeroen Carolus](/Jeroen_Carolus "Jeroen Carolus") in his 2006 Masters thesis [[1]](#cite_note-1).
It works like [Futility Pruning](/Futility_Pruning "Futility Pruning"), to skip [quiet](/Quiet_Moves "Quiet Moves"), none checking moves, if they have no potential to exceed the best score so far aka [alpha](/Alpha "Alpha").
Carolus' implementation even breaks the move loop, assuming an ordered [move list](/Move_List "Move List").

# See also

- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")

# Publications

- [Jeroen Carolus](/Jeroen_Carolus "Jeroen Carolus") (**2006**). *Alpha-Beta with Sibling Prediction Pruning in Chess*. Masters thesis, [pdf](http://homepages.cwi.nl/%7Epaulk/theses/Carolus.pdf)

# Publications

- [sibling prediction pruning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=47920) by [Marco Belli](/Marco_Belli "Marco Belli"), [CCC](/CCC "CCC"), May 05, 2013

# References

1. [↑](#cite_ref-1)  [Jeroen Carolus](/Jeroen_Carolus "Jeroen Carolus") (**2006**). *Alpha-Beta with Sibling Prediction Pruning in Chess*. Masters thesis, [pdf](http://homepages.cwi.nl/%7Epaulk/theses/Carolus.pdf)

**[Up one Level](/Pruning "Pruning")**