# Terminal Node

Source: https://www.chessprogramming.org/Terminal_Node

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Node](/Node "Node") \* Terminal Node**

**Terminal nodes** are [leaf nodes](/Leaf_Node "Leaf Node") with a fixed, application-dependent [value](/Score "Score") (e.g., win, loss, [draw](/Draw "Draw")). Thus, nodes representing [mate](/Checkmate "Checkmate") or [stalemate](/Stalemate "Stalemate") positions, which have per [game definition](/Chess_Game "Chess Game") no more child nodes, since there are no [legal moves](/Legal_Move "Legal Move"). If the [root](/Root "Root") becomes a terminal node, the game is [finished](/Chess_Game#endofgame "Chess Game"). That virtually also applies for [three-fold repetitions](/Repetitions "Repetitions"), [fifty-move rule](/Fifty-move_Rule "Fifty-move Rule") and [draws](/Draw_Evaluation#immediate "Draw Evaluation") by [insufficient material](/Material#InsufficientMaterial "Material"), despite strict interpretation of the rules requires a claim and an arbiter instance to finally declare them terminal.

In a wider sense, the search below the [root](/Root "Root") may consider nodes where a cycle occurred ([repetition](/Repetitions "Repetitions") but not yet necessarily three-fold) terminal as well, similar for nodes, where [interior node recognizers](/Interior_Node_Recognizer "Interior Node Recognizer") detect a node state (e.g., a table base draw) with no need to search it further.

# See also

- [Checkmate](/Checkmate "Checkmate")
- [Draw](/Draw "Draw")
- [Draw Evaluation](/Draw_Evaluation "Draw Evaluation")
- [Leaf Node](/Leaf_Node "Leaf Node")
- [Interior Node](/Interior_Node "Interior Node")
- [Stalemate](/Stalemate "Stalemate")

# External Links

- [Terminal node from Wikipedia](https://en.wikipedia.org/wiki/Terminal_node)

**[Up one Level](/Node "Node")**