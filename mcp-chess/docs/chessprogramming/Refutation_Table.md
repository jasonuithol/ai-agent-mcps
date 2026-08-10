# Refutation Table

Source: https://www.chessprogramming.org/Refutation_Table

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Move Ordering](/Move_Ordering "Move Ordering") \* Refutation Table**

The **Refutation Table** is based on a [triangular PV-Table](/Triangular_PV-Table "Triangular PV-Table") utilized in early chess programs with no or only a small [transposition table](/Transposition_Table "Transposition Table"). It is used not only to store and re-use the [PV](/Principal_Variation "Principal Variation") of the [best root move](/Best_Move "Best Move"), but variants or at least one [refutation move](/Refutation_Move "Refutation Move") of all other [root](/Root "Root") moves, which may be considered during the next [iteration](/Iteration "Iteration") of an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework. However that requires a different update of the triangular [array](/Array "Array") even at [Cut-nodes](/Node_Types#CUT "Node Types") at least near the root. Todays modern programs therefor typically abandon the refutation table and rely on transposition table and [Killer heuristic](/Killer_Heuristic "Killer Heuristic").

# History

In 1982, [William Fink](/William_Fink "William Fink"), author of the [Sfinks](/Sfinks "Sfinks") program, mentions to save two moves of the variation for every root move [[1]](#cite_note-1). [Tony Marsland](/Tony_Marsland "Tony Marsland") and [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") mention refutation tables in their respective papers and both quote [Selim Akl's](/Selim_Akl "Selim Akl") and [Monroe Newborn's](/Monroe_Newborn "Monroe Newborn") 1977 paper *The principal continuation and the killer heuristic* [[2]](#cite_note-2) as original source.

## Tony Marsland

[Tony Marsland](/Tony_Marsland "Tony Marsland") mentions refutation table in his 1983 paper [[3]](#cite_note-3):

```
For each initial move in the game tree, the alpha-beta algorithm determines a sequence of moves which is sufficient to cut off the search. These sequences may be stored in a refutation table. After a search to depth D on a tree of constant width W this table will contain W*D entries. Thus upon the next iteration there exists a set of move sequences of length D-ply that are to be tried first. The next ply is then added and the search continues. The candidate principal variation is fully searched, but for the alternate variations the moves in the refutation table may again be sufficient to cut off the search, and thus save the move generation that would normally occur at each node. The storage overhead is very small, although a small triangular table is also needed to identify the refutations.
```

## Jonathan Schaeffer

[Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") describes the refutation tables as follows [[4]](#cite_note-4):

```
Refutation tables. The major disadvantage of transposition tables is their size. Refutation tables attempt to retain one of the advantages of transposition tables, when used with iterative deepening, but with smaller memory requirements. For each iteration, the search yields a path for each move from the root to a leaf node that results in either the correct minimax score or an upper bound on its value. This path from the d - 1 ply search can be used as the basis for the search to d ply. Often, searching the previous iteration’s path or refutation for a move as the initial path examined for the current iteration will prove sufficient to refute the move one ply deeper.
```

# Publications

- [Selim Akl](/Selim_Akl "Selim Akl"), [Monroe Newborn](/Monroe_Newborn "Monroe Newborn") (**1977**). *[The Principal Continuation and the Killer Heuristic](http://dl.acm.org/citation.cfm?id=810240)*. 1977 ACM Annual Conference Proceedings
- [William Fink](/William_Fink "William Fink") (**1982**). *An Enhancement to the Iterative, Alpha-Beta, Minimax Search Procedure*. [ICCA Newsletter, Vol. 5, No. 1](/ICGA_Journal#5_1 "ICGA Journal")
- [Tony Marsland](/Tony_Marsland "Tony Marsland") (**1983**). *Relative Efficiency of Alpha-beta Implementations*. [IJCAI 1983](/Conferences#IJCAI1983 "Conferences"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/IJCAI-83.pdf)
- [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *The History Heuristic and Alpha-Beta Search Enhancements in Practice*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](/IEEE#TPAMI "IEEE"), Vol. 11, No. 11, [zipped ps](http://ljk.imag.fr/membres//Jean-Guillaume.Dumas/Enseignements/Polys/Externes/schaeffer_history_heuristic.ps.gz), [pdf](https://eprints.kfupm.edu.sa/70119/1/70119.pdf)
- [Tsan-sheng Hsu](/Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2012**). *Transposition Table, History Heuristic, and other Search Enhancements*. [slides as pdf](http://www.iis.sinica.edu.tw/~tshsu/tcg2012/slides/slide10.pdf)

# Postings

- [alpha beta search iterative deepening refutation table](http://stackoverflow.com/questions/16235923/alpha-beta-search-iterative-deepening-refutation-table) by [bysreg](http://stackoverflow.com/users/854058/bysreg), [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow), April 26, 2013
- [killer trees](http://www.talkchess.com/forum/viewtopic.php?t=55438) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), February 23, 2015 » [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")

# See also

- [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [Last Best Reply](/Last_Best_Reply "Last Best Reply")
- [Principal Variation](/Principal_Variation "Principal Variation")
- [Refutation Move](/Refutation_Move "Refutation Move")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Triangular PV-Table](/Triangular_PV-Table "Triangular PV-Table")

# References

1. [↑](#cite_ref-1) [William Fink](/William_Fink "William Fink") (**1982**). *An Enhancement to the Iterative, Alpha-Beta, Minimax Search Procedure*. [ICCA Newsletter, Vol. 5, No. 1](/ICGA_Journal#5_1 "ICGA Journal")
2. [↑](#cite_ref-2) [Selim Akl](/Selim_Akl "Selim Akl"), [Monroe Newborn](/Monroe_Newborn "Monroe Newborn") (**1977**). *The Principal Continuation and the Killer Heuristic*. 1977 ACM Annual Conference Proceedings
3. [↑](#cite_ref-3) [Tony Marsland](/Tony_Marsland "Tony Marsland") (**1983**). *Relative Efficiency of Alpha-beta Implementations*. [IJCAI 1983](/Conferences#IJCAI1983 "Conferences"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/IJCAI-83.pdf)
4. [↑](#cite_ref-4) [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *The History Heuristic and Alpha-Beta Search Enhancements in Practice*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](/IEEE#TPAMI "IEEE"), Vol. 11, No. 11, [zipped ps](http://ljk.imag.fr/membres//Jean-Guillaume.Dumas/Enseignements/Polys/Externes/schaeffer_history_heuristic.ps.gz), [pdf](https://eprints.kfupm.edu.sa/70119/1/70119.pdf)

**[Up one level](/Move_Ordering "Move Ordering")**