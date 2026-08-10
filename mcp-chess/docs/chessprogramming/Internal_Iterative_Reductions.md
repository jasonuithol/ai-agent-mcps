# Internal Iterative Reductions

Source: https://www.chessprogramming.org/Internal_Iterative_Reductions

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Reductions](/Reductions "Reductions") \* Internal Iterative Reductions**

**Internal Iterative Reductions** is an idea first introduced by [Ed Schroder](/Ed_Schroder "Ed Schroder") into his engine [Rebel](/Rebel "Rebel") in 2020. It is used as a replacement or in conjunction with [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening"), although the name is a bit of a misnomer.

Internal Iterative Deepening (IID) and Internal Iterative Reductions (IIR) are both meant to handle nodes where no [hash move](/Hash_Move "Hash Move") is found. IID would attempt to fix this by running an internal, reduced depth search. However, IIR instead opts to simply reduce the depth of the entire node, in the hope that the node must not be very important as there was no hash move present. In early implementations, IIR was used on all types of nodes (in the case of Rebel) and only on [PV-nodes](/Node_Types#PV-Nodes "Node Types") (in the case of Stockfish). However, in 2021, [Michael Chaly](/Michael_Chaly "Michael Chaly") introduced IIR on expected cut-nodes in Stockfish, and was later adapted by [Ethereal](/Ethereal "Ethereal"). There is also an idea of reducing depth by more if the node has been searched before at a depth greater than or equal to current depth, but yet no hash move is found.

# Conditions

Where to use IIR is also an important question. Limiting the depth is an obvious condition (only use IIR if depth > 5, say). Most only use IIR in PV-Nodes and expected [cut-nodes](/Node_Types#Cut-Nodes "Node Types"), but some implementations use IIR on [all-nodes](/Node_Types#All-Nodes "Node Types") as well.

# See also

- [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
- [Razoring](/Razoring "Razoring")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Delta Pruning](/Delta_Pruning "Delta Pruning")

# Forum Posts

- [An alternative to IID](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=74769) by [Ed Schroder](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), August 13, 2020 » Internal Iterative Reductions