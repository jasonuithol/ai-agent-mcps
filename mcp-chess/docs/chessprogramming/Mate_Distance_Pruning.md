# Mate Distance Pruning

Source: https://www.chessprogramming.org/Mate_Distance_Pruning

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Pruning](/Pruning "Pruning") \* Mate Distance Pruning**

If a forced [mate](/Checkmate "Checkmate") has been found, **Mate Distance Pruning** (MDP) will cut trees and adjust [bounds](/Bound "Bound") of lines where no shorter mate is possible. Mate Distance Pruning is a safe type of pruning, as it only cuts irrelevant nodes. It will not add much to a programs [playing strength](/Playing_Strength "Playing Strength") as this pruning only comes into effect when a position is already decided, still it helps with analysis and solving "Mate in n" problems.

# Mating Value

The prerequisite for Mate Distance Pruning is that decided positions are properly [scored](/Score "Score"). So a position where the opponent is mated is scored SCORE\_MATE (a very high value), a position where the victory is one move away is worth less SCORE\_MATE - 1, Mate in 2 plies is scored SCORE\_MATE - 2 and so on. On the other side, a position where the side to move is mated in n plies is evaluated -SCORE\_MATE + n. The difference between the actual value and SCORE\_MATE is always the number of plies the mate is away from the root position.

# Upper Bound

Assume we are in a winning position. Through another line we have already found a forced mate in n plies. Thus our alpha is SCORE\_MATE - n. From this information we can take that should we be searching a line that already is equal to or longer than n, we can impossibly increase alpha even if another mate was found. This means we could safely prune that tree.

Furthermore we can lower the upper bound. If we are n plies away from the root, the opponent can impossibly be evaluated > SCORE\_MATE - n. Thus beta can be set to this value should it be higher.

```
mating_value = SCORE_MATE - RootDistance;

if (mating_value < beta) {
   beta = mating_value;
   if (alpha >= mating_value) return mating_value;
}
```

# Lower Bound

Contrary to the pruning if we are in a winning position, scores can also be adjusted and trees pruned if we are in a loosing position.

```
mating_value = -SCORE_MATE + RootDistance;

if (mating_value > alpha) {
   alpha = mating_value;
   if (beta <= mating_value) return mating_value;
}
```

# In Practice

Using the Chess Engine [Glass](/Glass "Glass") 1.0 the treesize of a search without Mate Distance Pruning is compared to one with this feature enabled.

|  |
| --- |
|                                                                                              ♔                                     ♖               ♚ |

8/7K/8/8/8/8/R7/7k w - - 0 1

| Depth | MDP Disabled (Score / Nodes) [[1]](#cite_note-1) | MDP Enabled (Score / Nodes) |
| --- | --- | --- |
| 1 | 1041 / 3 | 1041 / 3 |
| 2 | 1041 / 23 | 1041 / 23 |
| 3 | 1051 / 103 | 1051 / 103 |
| 4 | 1051 / 551 | 1051 / 551 |
| 5 | 1055 / 2151 | 1055 / 2151 |
| 6 | 1051 / 7638 | 1051 / 7638 |
| 7 | 1055 / 24353 | 1055 / 24353 |
| 8 | 1065 / 62692 | 1065 / 62692 |
| 9 | 1065 / 139241 | 1065 / 139241 |
| 10 | 1085 / 253338 | 1085 / 253338 |
| 11 | 1085 / 409101 | 1085 / 409101 |
| 12 | 1105 / 610285 | 1105 / 610285 |
| 13 | 1105 / 873959 | 1105 / 873959 |
| 14 | 1105 / 1417047 | 1105 / 1417047 |
| 15 | 1105 / 1907578 | 1105 / 1907578 |
| 16 | M8 / 2846864 | M8 / 2547293 |
| 17 | M8 / 3715208 | M8 / 2819164 |
| 18 | M8 / 4842666 | M8 / 3092833 |
| 19 | M8 / 6181827 | M8 / 3368068 |
| 20 | M8 / 7774698 | M8 / 3643489 |

From this table one can see that the treesize is equal for the first 15 plies, but then the Version with Mate Distance Pruning enabled found the exact mating line about 10% smaller. Furthermore the risk of treesize explosion for further iterations is greatly decreased. In this example the treesize of the Version with this type of Pruning enabled is less than half as big.

# Forum Posts

- [Search questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6665) by [Sven Schüle](/Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 17, 2007» [Fail-Soft](/Fail-Soft "Fail-Soft")
- [Discussion about Mate Distance Pruning](http://www.talkchess.com/forum/viewtopic.php?t=26995) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), March 14, 2009
- [mate distance pruning problems and static null move pruning](http://www.talkchess.com/forum/viewtopic.php?t=41337) by Pierre Bokma, [CCC](/CCC "CCC"), December 04, 2011 » [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")

# References

1. [↑](#cite_ref-1) Nodes until [PV](/Principal_Variation "Principal Variation") is found

**[Up one level](/Pruning "Pruning")**