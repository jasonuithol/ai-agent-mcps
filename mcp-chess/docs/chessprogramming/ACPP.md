# ACPP

Source: https://www.chessprogramming.org/ACPP

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* ACPP**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Protein_ACPP_PDB_1cvi.png/330px-Protein_ACPP_PDB_1cvi.png)](/File:Protein_ACPP_PDB_1cvi.png)

Structure of ACCP [[1]](#cite_note-1)

**ACPP**, (Advanced Chess Playing Program)  
an experimental chess program by [William Tunstall-Pedoe](/William_Tunstall-Pedoe "William Tunstall-Pedoe"), which was research vehicle on [genetic algorithms](/Genetic_Programming#GeneticAlgorithm "Genetic Programming") and [automated tuning](/Automated_Tuning "Automated Tuning"), described in the September 1991 [ICCA Journal](/ICGA_Journal#14_3 "ICGA Journal"), and before in his 1991 CST Part II Dissertation.
While Tunstall-Pedoe mentioned the applicability of GA in [search](/Search "Search") parameter tuning for instance with impact in [move ordering](/Move_Ordering "Move Ordering"),
he focused on [evaluation](/Evaluation "Evaluation") weights. A population of 50 individual chess playing programs was used with randomly initialized [chromosomes](https://en.wikipedia.org/wiki/Chromosome) representing the concatenated weights to optimize.
Inside the optimization loop, the [genetic operator](https://en.wikipedia.org/wiki/Genetic_operator) determines the [fitness](https://en.wikipedia.org/wiki/Fitness_function) of all individuals, to breed the new generation favouring parent [selection](https://en.wikipedia.org/wiki/Selection_(genetic_algorithm)) towards fitter individuals.

# Features

- [Material](/Material "Material")
- [Mobility](/Mobility "Mobility") (Number of [Pseudo-Legal Moves](/Pseudo-Legal_Move "Pseudo-Legal Move"))
- [Center Control](/Center_Control "Center Control")
- [Development](/Development "Development")
- [Queen King Tropism](/King_Safety#KingTropism "King Safety")
- [Rook King Tropism](/King_Safety#KingTropism "King Safety")
- [Rook on (Semi) Open Files](/Rook_on_Open_File "Rook on Open File")
- [Isolated Pawns](/Isolated_Pawn "Isolated Pawn")
- [Passed Pawns](/Passed_Pawn "Passed Pawn"), Σ Number of Squares of [Rearspan](/Pawn_Spans "Pawn Spans")
- [Square Control](/Square_Control "Square Control") (Number of Squares Attacked in Opponent's Half)

# Weights

Feature weights are defined by a fixed base value, plus a variable delta range coded by a number of consecutive bits inside a [chromosome](https://en.wikipedia.org/wiki/Chromosome) - a bit array of 145 bits in total.
For instance [material](/Material "Material") weights uses four 11-bit delta scores to modify the weights of [queens](/Queen "Queen"), [rooks](/Rook "Rook"), [bishops](/Bishop "Bishop") and [knights](/Knight "Knight") in a [millipawn](/Millipawns "Millipawns") resolution, to add up to 2048 to its appropriate base values (2000, 2000, 4000, 8000), while [pawns](/Pawn "Pawn") have a fixed weight of 1000.

# Fitness

The [fitness function](https://en.wikipedia.org/wiki/Fitness_function) of a chess entity deals with measuring or estimating its relative [playing strength](/Playing_Strength "Playing Strength").
The obvious approach by pitting all individuals in the population against one another and assess fitness by the score achieved in a tournament,
was too time consuming in 1991 - at least 1250 games need to be played per generation with a reasonable minimal [search depth](/Depth "Depth"), and the known objections against such single-replica round-robin tournaments.
The method eventually adopted was using a set of about 28,000 grandmaster positions to apply [Move adaption](/Automated_Tuning#MoveAdaption "Automated Tuning")
with a shallow one ply plus [quiescence](/Quiescence_Search "Quiescence Search") search. The fitness was defined as the number of times in a random sample of 500 positions that the individual's choice of move matched the Grandmaster move [[2]](#cite_note-2).
Despite the relative efficiency of the fitness function used compared with one from game playing, the algorithm is still very slow, taking about four hours per generation.
ACCP ran at 180 [nodes per second](/Nodes_per_Second "Nodes per Second").

# Results

The generational process was repeated with a [crossover](https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)) probability of 0.5
and a [mutation probability](https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)) of 0.001. Fitness scaling
[[3]](#cite_note-3) [[4]](#cite_note-4)
was used to enhance the fittest members' fitness in each generation to twice the average fitness while keeping the average the same.

[![AcppGA.jpg](/images/e/e2/AcppGA.jpg)](/File:AcppGA.jpg)

The graph shows the raw unscaled fitness against generation number [[5]](#cite_note-5).

# Conclusion

The "learned" values, in particular material weights, showed little correlation with established [point values](/Point_Value "Point Value").
Careful consideration of the fitness function provides a possible explanation for this discrepancy. Although any single move
results in immediate changes to most positional features, the only way it affects material scores is if it is a [capture](/Captures "Captures").
At the time of the publication, the open question remained whether tuning designed to mimic Grandmasters will make the program so tuned optimal in game playing.

# See also

- [Cyber Chess](/Cyber_Chess "Cyber Chess")
- [Falcon](/Falcon "Falcon")

# Publications

- [William Tunstall-Pedoe](/William_Tunstall-Pedoe "William Tunstall-Pedoe") (**1991**). *An Advanced Chess-Playing Program*. CST Part II Dissertation, [University of Cambridge](https://en.wikipedia.org/wiki/University_of_Cambridge) [Computer Laboratory](http://www.cl.cam.ac.uk/), England (unpublished, referred in *Genetic Algorithms ...*)
- [William Tunstall-Pedoe](/William_Tunstall-Pedoe "William Tunstall-Pedoe") (**1991**). *Genetic Algorithms Optimizing Evaluation Functions*. [ICCA Journal, Vol. 14, No. 3](/ICGA_Journal#14_3 "ICGA Journal")

# External Links

- [Prostatic acid phosphatase from Wikipedia](https://en.wikipedia.org/wiki/Prostatic_acid_phosphatase)
- [The Who](/Category:The_Who "Category:The Who") - [My Generation](https://en.wikipedia.org/wiki/My_Generation) (live 1967), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Structure of the [ACPP protein](https://www.uniprot.org/uniprot/P0A6A8). Based on [PyMOL](https://en.wikipedia.org/wiki/PyMOL) rendering of PDB [1cvi](https://www.rcsb.org/structure/1cvi), image created by [Emw](https://commons.wikimedia.org/wiki/User:Emw), December 15, 2009, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [William Tunstall-Pedoe](/William_Tunstall-Pedoe "William Tunstall-Pedoe") (**1991**). *Genetic Algorithms Optimizing Evaluation Functions*. [ICCA Journal, Vol. 14, No. 3](/ICGA_Journal#14_3 "ICGA Journal")
3. [↑](#cite_ref-3) [David E. Goldberg](/David_E._Goldberg "David E. Goldberg") (**1989**). *Genetic Algorithms in Search, Optimization and Machine Learning*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley), pp. 76-80
4. [↑](#cite_ref-4) [Fitness Scaling - MATLAB & Simulink](https://www.mathworks.com/help/gads/fitness-scaling.html)
5. [↑](#cite_ref-5) [William Tunstall-Pedoe](/William_Tunstall-Pedoe "William Tunstall-Pedoe") (**1991**). *Genetic Algorithms Optimizing Evaluation Functions*. [ICCA Journal, Vol. 14, No. 3](/ICGA_Journal#14_3 "ICGA Journal"), image pp. 124

**[Up one Level](/Engines "Engines")**