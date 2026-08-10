# Search Progression

Source: https://www.chessprogramming.org/Search_Progression

When creating a new engine from scratch, it is often perplexing to choose which feature to implement first. Written below are some advice from authors of top chess engines.

# Connorpasta

A message sent by [Seer](/Seer "Seer") author [Connor McMonigle](/Connor_McMonigle "Connor McMonigle") in [OpenBench](/OpenBench "OpenBench") discord. It got the name "Connorpasta" due to its prevalence of use in computer chess Discord servers.

```
A reasonable search feature progression (starting with vanilla TT (sorting TT move first), PVS, QS and aspiration windows which are all pretty fundamental) imo is: NMP, LMR (log formula is most principled ~ there are a number of adjustments you can experiment with), static NMP (aka RFP), 
butterfly history heuristic, LMP, futility pruning, CMH+FMH, QS SEE pruning, PVS SEE pruning (captures and quiets), QS delta pruning, history pruning, capture history heuristic, singular extensions, multicut (using singular search result).
(with a healthy amount of parameter tweaking after each addition)
Idk if I'm missing anything major. Those search heuristics constitute the vast majority of the Elo you'll find in any top engine, though the details of the implementation are very important.
```

# Improved Connorpasta

Written by [Integral](/index.php?title=Integral&action=edit&redlink=1 "Integral (page does not exist)") author [Aron Petkovski](/Aron_Petkovski "Aron Petkovski"). It is an improvement to Connorpasta that aims to include more features and covers a wider range of topics.

**A reasonable search feature progression assuming you have the fundamentals i.e. negamax and alpha/beta pruning (ideally in a fail-soft framework)**

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- Basic [Move Ordering](/Move_Ordering "Move Ordering") (sorting [TT move](/Hash_Move "Hash Move") first, captures by [MVV-LVA](/MVV-LVA "MVV-LVA"))
- [Quiescent Search](/Quiescence_Search "Quiescence Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions") (log formula is most principled ~ there are a number of adjustments you can experiment with)
- [Butterfly history heuristic](/History_Heuristic "History Heuristic")
- [Killer moves](/Killer_Heuristic "Killer Heuristic")
- [Late Moves Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Internal Iterative Reductions](/Internal_Iterative_Reductions "Internal Iterative Reductions") (IIR)
- [Improving heuristic](/Improving "Improving")
- QS SEE pruning
- PVS SEE pruning (captures and quiets)
- [Continuation History](/History_Heuristic#Continuation_History "History Heuristic") ([CMH](/History_Heuristic#Counter_Moves_History "History Heuristic") + FMH etc..)
- [Capture History Heuristic](/History_Heuristic#Capture_History "History Heuristic")
- [History Pruning](/index.php?title=History_Pruning&action=edit&redlink=1 "History Pruning (page does not exist)")
- [Singular Extensions](/Singular_Extensions "Singular Extensions")
- [Multicut](/Multi-Cut#Modern_Usage "Multi-Cut") (using singular search result)
- Double/triple/negative extensions
- [Cutnode](/Node_Types#Cut-Nodes "Node Types") (as a part of negative extensions, LMR, etc)
- [Static Evaluation Correction History](/Static_Evaluation_Correction_History "Static Evaluation Correction History")
- [QS futility pruning](/index.php?title=QS_futility_pruning&action=edit&redlink=1 "QS futility pruning (page does not exist)")

There are also time management adjustments that can be done at any point after adding iterative deepening. Ideally you have:

- Hard bound (applies to the entire search)
- Soft bound (checked on each new depth in the ID loop)

For the soft bound the progression can go something like this

- Node-based scaling
- Best move stability
- Eval stability

Additionally, should be a healthy amount of parameter tweaking after each addition.
There are other minor features that top engines have, but these will constitute the majority of the elo you will find in them.