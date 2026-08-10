# Fill Algorithms

Source: https://www.chessprogramming.org/Fill_Algorithms

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* Fill Algorithms**

[![](/images/thumb/7/76/EschersPlaneFillingII.jpg/300px-EschersPlaneFillingII.jpg)](http://www.mcescher.com/Gallery/recogn-bmp/LW422.jpg)

[M. C. Escher](/Category:M._C._Escher "Category:M. C. Escher"), Plane Filling II, 1957 [[1]](#cite_note-1)

**Fill algorithms** perform the [union](/General_Setwise_Operations#Union "General Setwise Operations") of a set with their consecutive [direction-wise](/Direction "Direction") [shifts](/General_Setwise_Operations#ShiftingBitboards "General Setwise Operations"). The shifted intermediate sets are likely [intersected](/General_Setwise_Operations#Intersection "General Setwise Operations") with some mask to avoid board wraps of certain directions, and/or also to consider the [occupancy](/Occupancy "Occupancy") or any reasonable taboo set (i.e. [pawn attacks](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)")) as flood stopping obstruction.

For the non sliding pieces, [pawn](/Pawn "Pawn"), [knight](/Knight "Knight") and [king](/King "King"), one fill cycle covers all potential [moves](/Moves "Moves") in one certain direction, or even all moves in different directions. However, for the sliding pieces, [bishop](/Bishop "Bishop"), [rook](/Rook "Rook") and [queen](/Queen "Queen"), one fill cycle covers a direction-wise move step for a union set of attacked squares reachable in one move. Often, the up to seven direction wise fill cycles may be performed in three [parallel prefix steps](/Parallel_Prefix_Algorithms "Parallel Prefix Algorithms").

Applications of fill algorithms are related to all kinds of [pawn properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties"), [progressive mobility](/Mobility#ProgressiveMobility "Mobility") and [path finding](/All_Shortest_Paths "All Shortest Paths") algorithms, f.i. to find so called [Trajectories](/Trajectory "Trajectory") [[2]](#cite_note-2) [[3]](#cite_note-3) .

# Pawn

Pawn fills are performed by north- or south [steps](/General_Setwise_Operations#OneStepOnly "General Setwise Operations"), for span determination on the otherwise empty board. If it is about to consider obstructions, the north- or south [Dumb7-](/Dumb7Fill#OccludedFill "Dumb7Fill") or [Kogge-Stone occluded fill](/Kogge-Stone_Algorithm#OccludedFill "Kogge-Stone Algorithm") might be applied.

- [Pawn Fills](/Pawn_Fills "Pawn Fills")
- [Pawn Spans](/Pawn_Spans "Pawn Spans")
- [Attack Spans](/Attack_Spans "Attack Spans")
- [Dumb7Fill](/Dumb7Fill#OccludedFill "Dumb7Fill")
- [Kogge-Stone Algorithm](/Kogge-Stone_Algorithm#OccludedFill "Kogge-Stone Algorithm")

# Knight

- [Knight Fill](/Knight_Pattern#KnightFill "Knight Pattern")
- [Knight-Distance](/Knight-Distance "Knight-Distance")

# King

- [Flood Fill Algorithm](/King_Pattern#FloodFillAlgorithms "King Pattern")
- [All shortest Paths](/All_Shortest_Paths "All Shortest Paths")
- [Corresponding Squares](/Corresponding_Squares "Corresponding Squares")

# Sliding Pieces

Albeit intended as direction-wise attack generators, a surrounding loop may determine target in at least N moves sets of sliding pieces as well. One may pass not only pieces as argument, but their attacks repetitively, likely with alternating disjoint directions, i.e. file- versus ranks-attacks for rooks and diagonal versus anti-diagonal attacks for bishops.

- [Dumb7Fill](/Dumb7Fill "Dumb7Fill")

:   [AVX2 Dumb7Fill](/AVX2#Dumb7Fill "AVX2")

- [Kogge-Stone Algorithm](/Kogge-Stone_Algorithm "Kogge-Stone Algorithm")
- [Fill by Subtraction](/Fill_by_Subtraction "Fill by Subtraction")

# Forum Posts

- [Re: Hyperbola Quiesscene: hardly any improvement](http://www.talkchess.com/forum/viewtopic.php?start=0&t=25979&start=10) by [Karlo Bala Jr.](/Karlo_Balla "Karlo Balla"), [CCC](/CCC "CCC"), January 14, 2009 » [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence")

# External Links

- [Flood-fill from Wikipedia](https://en.wikipedia.org/wiki/Flood_fill)

:   [![Recursive Flood Fill 4 (aka).gif](https://upload.wikimedia.org/wikipedia/commons/7/7e/Recursive_Flood_Fill_4_%28aka%29.gif)](/File:Recursive_Flood_Fill_4_(aka).gif)

- [Implementing the flood fill algorithm](http://www.codecodex.com/wiki/index.php?title=Implementing_the_flood_fill_algorithm) from [CodeCodex](http://www.codecodex.com/wiki/Main_Page)
- [Pathfinding from Wikipedia](https://en.wikipedia.org/wiki/Pathfinding)
- [Panta rhei, "everything flows" from Wikipedia](https://en.wikipedia.org/wiki/Heraclitus#Panta_rhei.2C_.22everything_flows.22)
- [Panta Rhei](/Category:Panta_Rhei "Category:Panta Rhei") - [Alles fliesst](http://de.wikipedia.org/wiki/Panta_rhei) (1973), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Picture gallery "Recognition and Success 1955 - 1972"](http://www.mcescher.com/Gallery/gallery-recogn.htm)  from [The Official M.C. Escher Website](http://www.mcescher.com/)
2. [↑](#cite_ref-2) [Boris Stilman](/Boris_Stilman "Boris Stilman") (**1994**). *A Linguistic Geometry of the Chess Model*. [Advances in Computer Chess 7](/Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), [pdf draft](http://www.stilman-strategies.com/bstilman/boris_papers/Jour94_CHESS7.pdf)
3. [↑](#cite_ref-3) [Boris Stilman](/Boris_Stilman "Boris Stilman") (**2000**). *Linguistic Geometry - From Search to Construction (Operations Research/Computer Science Interfaces Series)*. [amazon.com](http://www.amazon.com/Linguistic-Geometry-Construction-Operations-Interfaces/dp/0792377389/ref=sr_1_1?ie=UTF8&s=books&qid=1257674191&sr=1-1)

**[Up one Level](/Bitboards "Bitboards")**