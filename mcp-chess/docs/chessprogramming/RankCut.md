# RankCut

Source: https://www.chessprogramming.org/RankCut

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Reductions](/Reductions "Reductions") \* RankCut**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Rank_badge.jpg/330px-Rank_badge.jpg)](/File:Rank_badge.jpg)

[Korean](https://en.wikipedia.org/wiki/Korea) [Rank badge](https://en.wikipedia.org/wiki/Mandarin_square) [[1]](#cite_note-1)

**RankCut**,  
a probability based depth reduction technique introduced by [Yew Jin Lim](/Yew_Jin_Lim "Yew Jin Lim") and [Wee Sun Lee](/Wee_Sun_Lee "Wee Sun Lee") in 2006 [[2]](#cite_note-2). It estimates the probability of discovering a better move later in the search by using the relative frequency of such cases for various states during the search. These probabilities are pre-computed off-line using several self-play games. RankCut can then reduce search effort by performing a shallow search when the probability of a better move appearing is below a certain threshold.
RankCut requires good [move ordering](/Move_Ordering "Move Ordering") and [fail-soft](/Fail-Soft "Fail-Soft") to work well. Further elaborated by [Yew Jin Lim](/Yew_Jin_Lim "Yew Jin Lim") in his 2007 Ph.D. thesis [[3]](#cite_note-3),
RankCut was successfully implemented with [Crafty](/Crafty "Crafty") and [Toga II](/Toga "Toga").

# RankCut Pseudocode

[[4]](#cite_note-4)

```
RankCutReSearch = false;

int RankCut(State & state, int α, int β, int depth) {
  if ((depth == 0) || isTerminal(state))
    return Evaluate(state);
  pruneRest = false;
  score = −∞;
  while (move = NextMove(state) ) {
    r = 0;
    features = determineFeatures(state);
    if (pruneRest || (probability(features) < threshold) ) {
      r = depthReduction(state);
      pruneRest = true;
    }
    score = −RankCut(successor(state, move), −β, −α, depth−1−r);
    if (RankCutReSearch && (score > α) && pruneRest)
      score = −RankCut(successor(state, move), −β, −α, depth−1);
    if (score ≥ β )
      break;
    if (score > α) {
      pruneRest = false;
      α = score;
    }
  }
  return score;
}
```

# Crafty

In the case of [Crafty](/Crafty "Crafty") 19.19, The probability computation considers following features:

- [Depth](/Depth "Depth")
- [In Check](/Check "Check")
- [Move](/Moves "Moves") [Extended](/Extensions "Extensions")
- Move Number
- Number of times [Best Move](/Best_Move "Best Move") changed
- Difference between the [Score](/Score "Score") of the current [Best Move](/Best_Move "Best Move") from [Alpha](/Alpha "Alpha") (discretized to 7 intervals)
- Difference between the [Score](/Score "Score") of the Last Move from the current [Best Move](/Best_Move "Best Move") (discretized to 7 intervals)
- [Phase](/Move_Generation#Staged "Move Generation") of the [Move Generation](/Move_Generation "Move Generation") (History Moves or Remaining Moves)

# See also

- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [ProbCut](/ProbCut "ProbCut")

# Publications

- [Yew Jin Lim](/Yew_Jin_Lim "Yew Jin Lim"), [Wee Sun Lee](/Wee_Sun_Lee "Wee Sun Lee") (**2006**). *RankCut - A Domain Independent Forward Pruning Method for Games*. [AAAI 2006](/Conferences#AAAI-2006 "Conferences"), [pdf](http://www.yewjin.com/storage/papers/rankcut.pdf)
- [Yew Jin Lim](/Yew_Jin_Lim "Yew Jin Lim") (**2007**). *On Forward Pruning in Game-Tree Search*. Ph.D. thesis, [National University of Singapore](https://en.wikipedia.org/wiki/National_University_of_Singapore), [pdf](http://www.yewjin.com/storage/papers/PhDThesisLimYewJin.pdf)

# External Links

- [Ranking from Wikipedia](https://en.wikipedia.org/wiki/Ranking)
- [Pruning from Wikipedia](https://en.wikipedia.org/wiki/Decision_tree_pruning)

# References

1. [↑](#cite_ref-1) [Korean](https://en.wikipedia.org/wiki/Korea) [Rank badge](https://commons.wikimedia.org/wiki/File:Rank_badge.jpg), 1850-1900, [V&A Museum](https://en.wikipedia.org/wiki/Victoria_and_Albert_Museum) (no. FE.272-1995), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Yew Jin Lim](/Yew_Jin_Lim "Yew Jin Lim"), [Wee Sun Lee](/Wee_Sun_Lee "Wee Sun Lee") (**2006**). *RankCut - A Domain Independent Forward Pruning Method for Games*. [AAAI 2006](/Conferences#AAAI-2006 "Conferences")
3. [↑](#cite_ref-3) [Yew Jin Lim](/Yew_Jin_Lim "Yew Jin Lim") (**2007**). *On Forward Pruning in Game-Tree Search*. Ph.D. thesis, [National University of Singapore](https://en.wikipedia.org/wiki/National_University_of_Singapore)
4. [↑](#cite_ref-4) based on pseudocode pp. 90 in [Yew Jin Lim](/Yew_Jin_Lim "Yew Jin Lim") (**2007**). *On Forward Pruning in Game-Tree Search*. Ph.D. thesis, [National University of Singapore](https://en.wikipedia.org/wiki/National_University_of_Singapore), [pdf](http://www.yewjin.com/storage/papers/PhDThesisLimYewJin.pdf)

**[Up one level](/Reductions "Reductions")**