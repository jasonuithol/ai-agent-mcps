# Leftmost Node

Source: https://www.chessprogramming.org/Leftmost_Node

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Node](/Node "Node") \* Leftmost Node**

**Leftmost Nodes** are the nodes searched **first** from the [root](/Root "Root") inside a [depth-first](/Depth-First "Depth-First") search approach like [Alpha-Beta](/Alpha-Beta "Alpha-Beta") or [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search"). If those nodes have an even [ply](/Ply "Ply") distance from the root, that is the same [Side to move](/Side_to_move "Side to move"), their alpha-beta Window is the same as the root window, {rootAlpha, rootBeta}. An odd ply distance implies a window of {-rootBeta, -rootAlpha} inside a [Negamax](/Negamax "Negamax") framework.

Since the root window is typically wide open (except [MTD(f)](/MTD(f) "MTD(f)")), either {-oo, +oo} or an [aspiration window](/Aspiration_Windows "Aspiration Windows") around the score from the previous [iteration](/Iteration "Iteration") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework, leftmost nodes have the same wide open window and will likely increase their initial alpha to establish a [principal variation](/Principal_Variation "Principal Variation"), to return an [exact score](/Exact_Score "Exact Score"). The left most [Leaf Node](/Leaf_Node "Leaf Node") with its static heuristic value, established by the [evaluation](/Evaluation "Evaluation") is the leaf with the greatest probability to influence the value of the root. In [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search"), leftmost nodes are [PV-Nodes](/Node_Types#PV "Node Types").

# See also

- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Root](/Root "Root")

**[Up one Level](/Node "Node")**