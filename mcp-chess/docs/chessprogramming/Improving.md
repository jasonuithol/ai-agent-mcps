# Improving

Source: https://www.chessprogramming.org/Improving

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* Improving**

Improving is an important modifier for many search heuristics. It is a boolean flag indicating whether the static evaluation of a position has improved from the position two plys ago. Improving can be used to modify the frequency and aggressiveness of certain pruning heuristics.

# Improving as a Modifier to Search Heuristics

| Heuristic | Modification |
| --- | --- |
| [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning") | Lower pruning margin when improving |
| [Late Move Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning") | Prune more late quiet moves when not improving |
| [ProbCut](/ProbCut "ProbCut") | Lower ProbCut beta threshold when improving |
| [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning") | More NMP when improving. This can be done by allowing pruning   even when eval is under beta (and above a certain threshold) when improving. |
| [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions") | Reduce more when not improving / less when improving |

# Code Example

The following code is taken from [Alexandria](/index.php?title=Alexandria&action=edit&redlink=1 "Alexandria (page does not exist)"). Note that in case the position is in check both 2 and 4 plies ago, improving can be set to either true or false. SPRT testing should be done to determine which of the two options is optimal for a given engine.

```
// Improving is a very important modifier to many heuristics. It checks if our static eval has improved since our last move.
// As we don't evaluate in check, we look for the first ply we weren't in check between 2 and 4 plies ago. If we find that
// static eval has improved, or that we were in check both 2 and 4 plies ago, we set improving to true.
if(inCheck)
    improving = false;
else if ((ss - 2)->staticEval != SCORE_NONE) {
    improving = ss->staticEval > (ss - 2)->staticEval;
}
else if ((ss - 4)->staticEval != SCORE_NONE) {
    improving = ss->staticEval > (ss - 4)->staticEval;
}
else
    improving = true;
```

This following code is from [Integral](/index.php?title=Integral&action=edit&redlink=1 "Integral (page does not exist)"). It demonstrates one way to adjust LMP margin with dynamic improving.

```
const int lmp_threshold = static_cast<int>((3.0 + depth * depth) /
                                           (2.0 - stack->improving_rate));
if (is_quiet && moves_seen >= lmp_threshold) {
    move_picker.SkipQuiets();
    continue;
}
```

# Dynamic Improving

[Aron Petkovski](/Aron_Petkovski "Aron Petkovski") introduced the concept of *Dynamic Improving*. By using static evaluation differences as a bonus to a improving score, Dynamic Improving allows for more control over improving-based mechanisms.

```
SearchStackEntry *past_stack = nullptr;
if ((stack - 2)->static_eval != kScoreNone) {
  past_stack = stack - 2;
} else if ((stack - 4)->static_eval != kScoreNone) {
  past_stack = stack - 4;
}

if (past_stack) {
  // Smoothen the improving rate from the static eval of our position in
  // previous turns
  const Score diff = stack->static_eval - past_stack->static_eval;
  stack->improving_rate =
      std::clamp(past_stack->improving_rate + diff / 50.0, -1.0, 1.0);
}
```