# Ghost

Source: https://www.chessprogramming.org/Ghost

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Ghost**

[![](/images/a/a8/Ghostseawolf.png)](https://etc.usf.edu/lit2go/153/the-sea-wolf/)

The Ghost [[1]](#cite_note-1)

**Ghost**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible, free chess engine by [Philipp Claßen](/Philipp_Cla%C3%9Fen "Philipp Claßen"), written in [C++](/Cpp "Cpp").
The name was taken from the name of [Wolf Larsen's](https://en.wikipedia.org/wiki/The_Sea-Wolf#Wolf_Larsen) seal-hunting schooner in the novel [The Sea-Wolf](https://en.wikipedia.org/wiki/The_Sea-Wolf) by [Jack London](https://en.wikipedia.org/wiki/Jack_London).
Ghost started its life in about 2000 as subject of a school project, the first version appeared in early 2001, playing online at [Internet Chess Club](/index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)") [[2]](#cite_note-2) , and later in rating list tournaments such as [CCRL](/CCRL "CCRL") [[3]](#cite_note-3) . Subsequent versions were Ghost 1, Ghost 2, and Ghost 3. Executables are available for [Windows](/Windows "Windows") and [Linux](/Linux "Linux") platforms. Likely, the current Ghost is [bitboard](/Bitboards "Bitboards") based, due to the much faster 64-bit executable.

# Ghost 1

Ghost 1 performed [NegaScout](/NegaScout "NegaScout"), [IID](/Internal_Iterative_Deepening "Internal Iterative Deepening"), [killer heuristic](/Killer_Heuristic "Killer Heuristic") and [history heuristic](/History_Heuristic "History Heuristic"), [recursive](/Recursion "Recursion") [null move pruning](/Null_Move_Pruning "Null Move Pruning") with [depth reduction](/Depth_Reduction_R "Depth Reduction R") of 3, [razoring](/Razoring "Razoring") and [futility pruning](/Futility_Pruning "Futility Pruning"), and a unique technique to detect [perpetual checks](/Check#Perpetual "Check").
It further used the [oracle](/Oracle "Oracle") approach of pre-scanned [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") at the [root](/Root "Root") [[4]](#cite_note-4) .

# Ghost 2

The second version, first released in 2003, is a [MTD(f)](/MTD(f) "MTD(f)") searcher, further utilizing [late move reductions](/Late_Move_Reductions "Late Move Reductions"), [adaptive null move pruning](/Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") with [R](/Depth_Reduction_R "Depth Reduction R") of 2 or 3 [plies](/Ply "Ply"), [ETC](/Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff"), and a unique [pin](/Pin "Pin") detection [extension](/Extensions "Extensions"). Ghost 2 has a safer perpetual check detection than Ghost 1, and usus local history counters [[5]](#cite_note-5).

# Ghost 3

Still using [MTD(f)](/MTD(f) "MTD(f)"), the [search](/Search "Search") has been rewritten from scratch to support [parallelism](/Parallel_Search "Parallel Search") using [work stealing](https://en.wikipedia.org/wiki/Work_stealing) provided by the [Threading Building Blocks](https://en.wikipedia.org/wiki/Threading_Building_Blocks) library.
The stable version 3.1 was released on May 30, 2017 [[6]](#cite_note-6).

# See also

- [Schooner](/Schooner "Schooner")

# Forum Posts

- [crafty vs ghost on ICC ...could Kasparov himself execute such an attack?](https://www.stmintz.com/ccc/index.php?id=194607) by Jeffrey Wadsworth, [CCC](/CCC "CCC"), October 28, 2001 » [Crafty](/Crafty "Crafty")
- [new ghost homepage](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=49019) by Michael Claßen, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 22, 2004
- [Ghost 3.1 released!](http://www.talkchess.com/forum/viewtopic.php?t=64143) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [CCC](/CCC "CCC"), June 01, 2017

# External Links

## Chess Engine

- [Ghost](http://www.ghostchess.de/) by [Philipp Claßen](/Philipp_Cla%C3%9Fen "Philipp Claßen")
- [Ghost](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Ghost&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](/CCRL "CCRL")

## Misc

- [Ghost (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Ghost_%28disambiguation%29)
- [Ghost from Wikipedia](https://en.wikipedia.org/wiki/Ghost)
- [List of ghost ships from Wikipedia](https://en.wikipedia.org/wiki/List_of_ghost_ships)
- [Phish](/Category:Phish "Category:Phish") - [Ghost](https://en.wikipedia.org/wiki/Ghost_(Phish_song)), [Randall's Island](https://en.wikipedia.org/wiki/Randalls_and_Wards_Islands) in [New York City](https://en.wikipedia.org/wiki/New_York_City), July 12, 2014, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [The Sea-Wolf | Jack London | Lit2Go ETC](https://etc.usf.edu/lit2go/153/the-sea-wolf/), Copyright © 2006—2019 by the [Florida Center for Instructional Technology](https://fcit.usf.edu/), [College of Education](https://www.usf.edu/education/), [University of South Florida](https://en.wikipedia.org/wiki/University_of_South_Florida)
2. [↑](#cite_ref-2) [crafty vs ghost on ICC ...could Kasparov himself execute such an attack?](https://www.stmintz.com/ccc/index.php?id=194607) by Jeffrey Wadsworth, [CCC](/CCC "CCC"), October 28, 2001
3. [↑](#cite_ref-3) [Ghost 2.0.1 in CCRL 40/40](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Ghost%202.0.1#Ghost_2_0_1)
4. [↑](#cite_ref-4) [Ghost | Search algorithms: Ghost 1](http://www.ghostchess.de/) by [Philipp Claßen](/Philipp_Cla%C3%9Fen "Philipp Claßen")
5. [↑](#cite_ref-5) [Ghost | Search algorithms: Ghost 2](http://www.ghostchess.de/) by [Philipp Claßen](/Philipp_Cla%C3%9Fen "Philipp Claßen")
6. [↑](#cite_ref-6) [Ghost 3.1 released!](http://www.talkchess.com/forum/viewtopic.php?t=64143) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [CCC](/CCC "CCC"), June 01, 2017

**[Up one Level](/Engines "Engines")**