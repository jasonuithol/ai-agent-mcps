# Floyd

Source: https://www.chessprogramming.org/Floyd

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Floyd**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Floyd_1999-09-14_2030Z_%28borderless%29.jpg/330px-Floyd_1999-09-14_2030Z_%28borderless%29.jpg)](/File:Floyd_1999-09-14_2030Z_(borderless).jpg)

Hurricane Floyd [[1]](#cite_note-1)

**Floyd**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") for study purposes and prototyping of new ideas by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), written in [C](/C "C"), and first released in October 2015 [[2]](#cite_note-2) with a permissive license [[3]](#cite_note-3) . Floyd can be build to run under [Windows](/Windows "Windows"), [Linux](/Linux "Linux") and [Mac OS](/Mac_OS "Mac OS"). Floyd had its over the board tournament debut at the [IGT 2016](/IGT_2016 "IGT 2016") with a 50% score.

# Description

## Board Representation

Floyd uses an [8x8 Board](/8x8_Board "8x8 Board"), agnostic to [square indexing](/Square_Mapping_Considerations "Square Mapping Considerations"), in the sense that it can be adapted to any of the eight possible board geometries with just a local change [[4]](#cite_note-4) . It uses an [attack table](/Attack_and_Defend_Maps "Attack and Defend Maps"), for each side an array of 64 [bytes](/Byte "Byte"), with following one- or two-bit attack counters per square ...

```
+-----+-----+-----+-----+-----+-----+-----+-----+
|   Pawns   |   Minors  |   Rooks   |Queen|King |
+-----+-----+-----+-----+-----+-----+-----+-----+
     7..6        5..4        3..2      1     0
```

... as used in [move generation](/Move_Generation "Move Generation"), [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") and [evaluation](/Evaluation "Evaluation").

## Search

The [search](/Search "Search") is a classical [PVS](/Principal_Variation_Search "Principal Variation Search") [iterative deepening](/Iterative_Deepening "Iterative Deepening") approach with [Zobrist key](/Zobrist_Hashing "Zobrist Hashing") [transposition table](/Transposition_Table "Transposition Table"), [quiescence search](/Quiescence_Search "Quiescence Search"), [null move pruning](/Null_Move_Pruning "Null Move Pruning") and [mate distance pruning](/Mate_Distance_Pruning "Mate Distance Pruning"). [Move ordering](/Move_Ordering "Move Ordering") considers [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") and a simple [killer heuristic](/Killer_Heuristic "Killer Heuristic").

## Evaluation

Floyd's [evaluation](/Evaluation "Evaluation") employs a vector of feature and weight pairs to calculate a [score](/Score "Score") as [weighted sum](https://en.wikipedia.org/wiki/Weighted_sum_model). In conjunction with a draw model [[5]](#cite_note-5) using [sigmoid functions](https://en.wikipedia.org/wiki/Sigmoid_function), the score is mapped to [winning probabilities](/Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), suited for [logistic regression](/Automated_Tuning#LogisticRegression "Automated Tuning") tuning.

```
def evaluate(board, wiloVector, drawVector):
        wiloScore = ...snip... // a weighted sum of board features
        drawScore = ...snip... // another weighted sum of board features

        return sigmoid(drawScore) * 0.5
             + sigmoid(wiloScore)
             - sigmoid(wiloScore) * sigmoid(drawScore)
```

## Misc

Floyd provides a [Python](/Python "Python") [API](https://en.wikipedia.org/wiki/Application_programming_interface) for search and evaluation functions [[6]](#cite_note-6) , i.e. for [automated tuning](/Automated_Tuning "Automated Tuning") [[7]](#cite_note-7) . It generates a compact [KPK](/KPK "KPK") [tablebase](/Endgame_Tablebases "Endgame Tablebases") to deal with [perfect knowledge](/Knowledge#PerfectKnowledge "Knowledge"), also available as stand alone project [[8]](#cite_note-8) [[9]](#cite_note-9) .

# See also

- [Mathematician - Robert W. Floyd (1936 - 2001)](/Mathematician#RWFloyd "Mathematician")
- [MSCP](/MSCP "MSCP")
- [Rookie](/Rookie "Rookie")

# Forum Posts

- [Floyd 0.5 released](http://www.talkchess.com/forum/viewtopic.php?t=57913) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](/CCC "CCC"), October 11, 2015
- [Floyd 0.6 released](http://www.talkchess.com/forum/viewtopic.php?t=57973) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](/CCC "CCC"), October 17, 2015
- [Floyd 0.7 released](http://www.talkchess.com/forum/viewtopic.php?t=58259) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](/CCC "CCC"), November 15, 2015
- [Floyd 0.8 released](http://www.talkchess.com/forum/viewtopic.php?t=59695) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](/CCC "CCC"), March 31, 2016
- [Floyd 0.9 released](http://www.open-chess.org/viewtopic.php?f=3&t=3005) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 20, 2016

# External Links

## Chess Engine

- [kervinck/floyd · GitHub](https://github.com/kervinck/floyd)
- [Download page - Floyd chess engine - /etc/marcelk](https://marcelk.net/floyd/)
- [Floyd 0.6 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Floyd%200.7%2064-bit#Floyd_0_7_64-bit) in [CCRL 40/4](/CCRL "CCRL")

## Misc

- [Floyd from Wikipedia](https://en.wikipedia.org/wiki/Floyd)
- [Hurricane Floyd from Wikipedia](https://en.wikipedia.org/wiki/Hurricane_Floyd)
- [Robert W. Floyd from Wikipedia](https://en.wikipedia.org/wiki/Robert_W._Floyd)
- [Floyd's cycle-finding algorithm from Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare)
- [Floyd–Hoare logic from Wikipedia](https://en.wikipedia.org/wiki/Hoare_logic)
- [Floyd–Steinberg dithering from Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering)
- [Floyd–Warshall algorithm from Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [Pink Floyd](/Category:Pink_Floyd "Category:Pink Floyd") - [High Hopes](https://en.wikipedia.org/wiki/High_Hopes_%28Pink_Floyd_song%29), [The Division Bell](https://en.wikipedia.org/wiki/The_Division_Bell), 1994, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Hurricane Floyd near peak intensity on September 14, 1999 at 2030 UTC. This image was produced from data from [NOAA-14](https://en.wikipedia.org/wiki/Television_Infrared_Observation_Satellite#Advanced_TIROS-N), provided by [NOAA](https://en.wikipedia.org/wiki/National_Oceanic_and_Atmospheric_Administration), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Hurricane Floyd from Wikipedia](https://en.wikipedia.org/wiki/Hurricane_Floyd)
2. [↑](#cite_ref-2) [Floyd 0.5 released](http://www.talkchess.com/forum/viewtopic.php?t=57913) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](/CCC "CCC"), October 11, 2015
3. [↑](#cite_ref-3) [floyd/LICENSE at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/LICENSE)
4. [↑](#cite_ref-4) [floyd/geometry.h at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/Source/geometry.h)
5. [↑](#cite_ref-5) [floyd/drawModel.txt at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/Docs/drawModel.txt)
6. [↑](#cite_ref-6) [floyd/README.md at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/README.md)
7. [↑](#cite_ref-7) [floyd/tune.py at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/Tools/tune.py)
8. [↑](#cite_ref-8) [Yet another KPK endgame table generator: pfkpk](http://www.talkchess.com/forum/viewtopic.php?t=57517) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](/CCC "CCC"), September 05, 2015
9. [↑](#cite_ref-9) [kervinck/pfkpk · GitHub](https://github.com/kervinck/pfkpk)

**[Up one Level](/Engines "Engines")**