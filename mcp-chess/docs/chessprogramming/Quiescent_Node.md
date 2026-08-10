# Quiescent Node

Source: https://www.chessprogramming.org/Quiescent_Node

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Node](/Node "Node") \* Quiescent Node**

**Quiescent Nodes** are [nodes](/Node "Node") at [depth](/Depth "Depth") zero or below, where a [Quiescence Search](/Quiescence_Search "Quiescence Search") is performed [[1]](#cite_note-1) [[2]](#cite_note-2). The most top subset of quiescent nodes at depth zero are also called [horizon nodes](/Horizon_Node "Horizon Node"). If the quiescent node is an expected [Cut-Node](/Node_Types#CUT "Node Types"), that is the evaluated [standing pat](/Quiescence_Search#StandPat "Quiescence Search") score is already greater or equal than [beta](/Beta "Beta"), the quiescent node becomes a [leaf](/Leaf_Node "Leaf Node") with the [lower bound](/Lower_Bound "Lower Bound") score of beta ([fail-hard](/Fail-Hard "Fail-Hard")) or the stand pat score ([fail-soft](/Fail-Soft "Fail-Soft")). Otherwise, winning captures (or checks) may either cause a [beta-cutoff](/Beta-Cutoff "Beta-Cutoff") or raise [alpha](/Alpha "Alpha") with an [exact score](/Exact_Score "Exact Score") at [PV-Nodes](/Node_Types#PV "Node Types"). At expected [All-Nodes](/Node_Types#ALL "Node Types") with evaluated score (far) below alpha, if no [tactical move](/Tactical_Moves "Tactical Moves") is available, or due to [Delta Pruning](/Delta_Pruning "Delta Pruning") good enough to raise alpha, those [leaves](/Leaf_Node "Leaf Node") return alpha ([fail-hard](/Fail-Hard "Fail-Hard")) as an [upper bound](/Upper_Bound "Upper Bound"). This may also appear, if this quiescent node was not a leaf, since some captures were not pruned, but tried without raising alpha.

# See also

- [Horizon Node](/Horizon_Node "Horizon Node")
- [Leaf Node](/Leaf_Node "Leaf Node")
- [Terminal Node](/Terminal_Node "Terminal Node")

# Forum Posts

- [quiescent nodes, and history heuristic...](https://www.stmintz.com/ccc/index.php?id=280447) by [Joel Veness](/Joel_Veness "Joel Veness"), [CCC](/CCC "CCC"), January 30, 2003 » [History Heuristic](/History_Heuristic "History Heuristic")
- [Quiescence node explosion](http://www.open-chess.org/viewtopic.php?f=5&t=2984) by [sandermvdb](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), June 01, 2016

# External Links

- [Flora Purim](/Category:Flora_Purim "Category:Flora Purim") - Once I Ran Away, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [quiescent vs non-quiescent node counting](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/926eaf0869b6f176#) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") from [rec.games.chess.computer](/Computer_Chess_Forums "Computer Chess Forums"), July 01, 1996
2. [↑](#cite_ref-2) [Re: simple node definitions question](https://www.stmintz.com/ccc/index.php?id=387518) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), September 13, 2004

**[Up one Level](/Node "Node")**