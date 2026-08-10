# Cheng

Source: https://www.chessprogramming.org/Cheng

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Cheng**

**Cheng**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), written in [C++](/Cpp "Cpp") as exercise in [generic programming](/Generic_Programming "Generic Programming"), first released as Cheng3 in April 2011.
Cheng is able to play [Chess960](/Chess960 "Chess960"), target platforms are [Windows](/Windows "Windows"), [Linux](/Linux "Linux"), [Mac OS](/Mac_OS "Mac OS") and [Android](/Android "Android") systems [[1]](#cite_note-1). **Cheng4** 0.38, released in January 2015, is available at [GitHub](https://en.wikipedia.org/wiki/GitHub) under the permissive [zlib license](https://en.wikipedia.org/wiki/Zlib_License) [[2]](#cite_note-2).

# Description

Cheng [[3]](#cite_note-3) is a [bitboard](/Bitboards "Bitboards") engine using [fancy magic bitboards](/Magic_Bitboards#Fancy "Magic Bitboards") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks"). It applies [staged move generation](/Move_Generation#Staged "Move Generation").

## Search

The [parallel](/Parallel_Search "Parallel Search") [multi-threaded](/Thread "Thread") [search](/Search "Search") performs [PVS](/Principal_Variation_Search "Principal Variation Search") [alpha-beta](/Alpha-Beta "Alpha-Beta") with a [shared](/Shared_Hash_Table "Shared Hash Table") [transposition table](/Transposition_Table "Transposition Table") inside a [fractional ply](/Depth#FractionalPlies "Depth") [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](/Aspiration_Windows "Aspiration Windows"), featuring [Lazy SMP](/Lazy_SMP "Lazy SMP") [[4]](#cite_note-4). Search routines are instantiated at [compile time](https://en.wikipedia.org/wiki/Compile_time) from a [generic routine](/Generic_Programming "Generic Programming") with three boolean [template parameters](https://en.wikipedia.org/wiki/Template_%28C%2B%2B%29#Function_templates), [PV-node](/Node_Types#PV "Node Types"), [in check](/Check "Check"), and [null move pruning](/Null_Move_Pruning "Null Move Pruning") on-off, similar [quiescence search](/Quiescence_Search "Quiescence Search") has four instances for on-off combinations of PV-node and check. Further [selectivity](/Selectivity "Selectivity") is applied by [mate distance pruning](/Mate_Distance_Pruning "Mate Distance Pruning"), [razoring](/Razoring "Razoring"), [IID](/Internal_Iterative_Deepening "Internal Iterative Deepening"), [futility pruning](/Futility_Pruning "Futility Pruning"), [check extensions](/Check_Extensions "Check Extensions") and [late move reductions](/Late_Move_Reductions "Late Move Reductions"). [Move ordering](/Move_Ordering "Move Ordering") is improved by the [killer-](/Killer_Heuristic "Killer Heuristic") and [history heuristic](/History_Heuristic "History Heuristic").

## Evaluation

[Evaluation](/Evaluation "Evaluation") employs three further [hash tables](/Hash_Table "Hash Table") - [evaluation hash table](/Evaluation_Hash_Table "Evaluation Hash Table"), [material hash table](/Material_Hash_Table "Material Hash Table") and [pawn hash table](/Pawn_Hash_Table "Pawn Hash Table"). The evaluation function determines hardware [population count](/Population_Count "Population Count") support at compile time, passed as template parameter to internal eval functions, finally adding a [tempo bonus](/Tempo "Tempo"). Pawn and piece specific evaluators are further implemented with a color template, considering [pawn structure](/Pawn_Structure "Pawn Structure"), [mobility](/Mobility "Mobility"), [king safety](/King_Safety "King Safety") and various piece pattern. Most of the gain in **Cheng4** 0.38, released in January 2015, is due to [eval tuning](/Automated_Tuning "Automated Tuning") using the [Texel's Tuning Method](/Texel%27s_Tuning_Method "Texel's Tuning Method") by [Peter Österlund](/Peter_%C3%96sterlund "Peter Österlund") [[5]](#cite_note-5).

# Forum Posts

## 2010 ...

- [cheng3 uci v1.0](http://www.talkchess.com/forum/viewtopic.php?t=38792) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), April 19, 2011
- [cheng3 1.03 released](http://www.talkchess.com/forum/viewtopic.php?t=39191) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), May 27, 2011
- [cheng3 1.05 released](http://www.talkchess.com/forum/viewtopic.php?t=40531) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), September 26, 2011
- [cheng3 1.06 released](http://www.talkchess.com/forum/viewtopic.php?t=41181) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), November 23, 2011
- [cheng3 1.07 released](http://www.talkchess.com/forum/viewtopic.php?t=42097) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), January 21, 2012
- [cheng4 0.35](http://www.talkchess.com/forum/viewtopic.php?t=49443) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), September 24, 2013
- [cheng4 0.36](http://www.talkchess.com/forum/viewtopic.php?t=50014) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), November 10, 2013
- [cheng4 0.36a (FRC bugfix)](http://www.talkchess.com/forum/viewtopic.php?t=50081) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), November 15, 2013
- [cheng4 0.36c - last version](http://www.talkchess.com/forum/viewtopic.php?t=51110) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), January 30, 2014
- [Tragic that Martin Sedlak has discontinued Cheng](http://www.open-chess.org/viewtopic.php?f=5&t=2584) by [User923005](/Dann_Corbit "Dann Corbit"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 31, 2014

## 2015 ...

- [Cheng: A great lost to the community](http://www.talkchess.com/forum/viewtopic.php?t=54988) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), January 15, 2015
- [cheng4 0.38 release](http://www.talkchess.com/forum/viewtopic.php?t=55000) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), January 18, 2015
- [Lazy SMP in Cheng](http://www.talkchess.com/forum/viewtopic.php?t=55188) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), February 02, 2015 » [Lazy SMP](/Lazy_SMP "Lazy SMP")
- [Lazy SMP scaling Cheng0.38](https://groups.google.com/d/msg/fishcooking/VL4pEYZXuuM/wJSehP7SQlYJ) by Bertil, [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), February 24, 2015
- [Empirical results with Lazy SMP, YBWC, DTS](http://www.talkchess.com/forum/viewtopic.php?t=56019) by [Kai Laskos](/Kai_Laskos "Kai Laskos"), [CCC](/CCC "CCC"), April 16, 2015 » [Lazy SMP](/Lazy_SMP "Lazy SMP"), [YBWC](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), [DTS](/Dynamic_Tree_Splitting "Dynamic Tree Splitting")
- [Cheng 4.39 release](http://www.talkchess.com/forum/viewtopic.php?t=57046) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), July 20, 2015
- [Cheng 4.39 Android version bugfix](http://www.talkchess.com/forum/viewtopic.php?t=58238) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), November 13, 2015
- [Cheng 4.39 Re-release for the Mac](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=58866) by [MikeB](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), January 09, 2016

## 2020 ...

- [Cheng 4.40](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76215) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), January 02, 2021
- [Cheng 4.41](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=289) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), April 27, 2021

# External Links

## Chess Engine

- [GitHub - kmar/cheng4: cheng4 chess engine](https://github.com/kmar/cheng4)
- [Cheng chess engine](http://www.vlasak.biz/cheng/) hosted by [Emil Vlasák](/index.php?title=Emil_Vlas%C3%A1k&action=edit&redlink=1 "Emil Vlasák (page does not exist)")
- [Index of /chess/engines/Jim Ablett/CHENG](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/CHENG/) compiled by [Jim Ablett](/Jim_Ablett "Jim Ablett") hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Cheng](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Cheng&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Cheng (Disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Cheng)
- [Chief engineer from Wikipedia](https://en.wikipedia.org/wiki/Chief_engineer)

# References

1. [↑](#cite_ref-1) [UCI and XBoard Engines for Android](http://www.aartbik.com/MISC/eng.html) by [Aart Bik](/Aart_Bik "Aart Bik")
2. [↑](#cite_ref-2) [GitHub - kmar/cheng4: cheng4 chess engine](https://github.com/kmar/cheng4)
3. [↑](#cite_ref-3) Description based on **Cheng4** 036c
4. [↑](#cite_ref-4) [Lazy SMP in Cheng](http://www.talkchess.com/forum/viewtopic.php?t=55188) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), February 02, 2015
5. [↑](#cite_ref-5) [cheng4 0.38 release](http://www.talkchess.com/forum/viewtopic.php?t=55000) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), January 18, 2015

**[Up one level](/Engines "Engines")**