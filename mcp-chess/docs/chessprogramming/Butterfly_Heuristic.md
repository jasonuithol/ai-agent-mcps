# Butterfly Heuristic

Source: https://www.chessprogramming.org/Butterfly_Heuristic

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Move Ordering](/Move_Ordering "Move Ordering") \* Butterfly Heuristic**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Xvxi1.jpg/250px-Xvxi1.jpg)](/File:Xvxi1.jpg)

Butterfly and Chinese [wisteriaflowers](https://en.wikipedia.org/wiki/Wisteria) [[1]](#cite_note-1)

**Butterfly Heuristic**,  
a dynamic move ordering method based on the number of trials of a given move inside the [search](/Search "Search"), irrespectively from the position in which the move has been made, and in opposition to the [History Heuristic](/History_Heuristic "History Heuristic"), irrespectively whether a move [fails high](/Fail-High "Fail-High") or not.

# Thought Experiment

The Butterfly Heuristic was proposed by [Dap Hartmann](/Dap_Hartmann "Dap Hartmann") in conjunction with so called [Butterfly Boards](/Butterfly_Boards "Butterfly Boards") as a pure thought experiment [[2]](#cite_note-2) :

```
No experiments with real game trees in an actual chess-playing programs have been carried out. The main reason for not doing so lies in the author's notion that this method will be far less effective than the History Heuristic [3]. Still, the main idea of this thought experiment is worth presenting.
```

# Persistence

Another utilization of [Butterfly Boards](/Butterfly_Boards "Butterfly Boards"), as proposed by Hartmann, was to make them persistent, initialized by moves from many Grandmaster and/or Correspondent chess games [[4]](#cite_note-4) [[5]](#cite_note-5) . [Mark Winands](/Mark_Winands "Mark Winands") at al. assimilated both, [Schaeffer's](/Jonathan_Schaeffer "Jonathan Schaeffer") [History Heuristic](/History_Heuristic "History Heuristic") combined with Hartmann's Butterfly Heuristic, and introduced the [Relative History Heuristic](/Relative_History_Heuristic "Relative History Heuristic") [[6]](#cite_note-6)

# See also

- [Butterfly Boards](/Butterfly_Boards "Butterfly Boards")
- [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic")
- [History Heuristic](/History_Heuristic "History Heuristic")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Relative History Heuristic](/Relative_History_Heuristic "Relative History Heuristic")

# Publications

- [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1983**). *The History Heuristic*. [ICCA Journal, Vol. 6, No. 3](/ICGA_Journal#6_3 "ICGA Journal")
- [Dap Hartmann](/Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 1: Grandmasters have Insights - the Problem is what to Incorporate into Practical Problems.* [ICCA Journal, Vol. 10, No. 1](/ICGA_Journal#10_1 "ICGA Journal")
- [Dap Hartmann](/Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 2: the Notion of Mobility, and the Work of [De Groot](/Adriaan_de_Groot "Adriaan de Groot") and [Slater](/Eliot_Slater "Eliot Slater")*. [ICCA Journal, Vol. 10, No. 2](/ICGA_Journal#10_2 "ICGA Journal")
- [Dap Hartmann](/Dap_Hartmann "Dap Hartmann") (**1988**). *Butterfly Boards*. [ICCA Journal, Vol. 11, Nos. 2/3](/ICGA_Journal#11_23 "ICGA Journal")
- [Dap Hartmann](/Dap_Hartmann "Dap Hartmann"), [Peter Kouwenhoven](/Peter_Kouwenhoven "Peter Kouwenhoven") (**1991**). *Sundry Computer Chess Topics*. [Advances in Computer Chess 6](/Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
- [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](/ICGA_Journal#15_1 "ICGA Journal")
- [Mark Winands](/Mark_Winands "Mark Winands"), [Erik van der Werf](/Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**2006**). *The Relative History Heuristic*. [CG 2006](/CG_2006 "CG 2006"), [pdf](http://www.cs.unimaas.nl/m.winands/documents/relhis.pdf)

# External Links

- [Butterfly from Wikipedia](https://en.wikipedia.org/wiki/Butterfly)
- [Heuristic from Wikipedia](https://en.wikipedia.org/wiki/Heuristic)
- [Flora Purim](/Category:Flora_Purim "Category:Flora Purim") - [Butterfly Dreams](https://en.wikipedia.org/wiki/Butterfly_Dreams) (1973), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Joe Henderson](/Category:Joe_Henderson "Category:Joe Henderson"), [George Duke](/Category:George_Duke "Category:George Duke"), [David Amaro](http://davidamaro.com/), [Ernie Hood](http://oxfordindex.oup.com/view/10.1093/gmo/9781561592630.article.J206900), [Stanley Clarke](/Category:Stanley_Clarke "Category:Stanley Clarke"), [Airto Moreira](/Category:Airto_Moreira "Category:Airto Moreira")

# References

1. [↑](#cite_ref-1) by [Xü Xi](https://en.wikipedia.org/wiki/Xu_Xi_%28painter%29) (c.886–c.975), painted around 970 during the early [Song Dynasty](https://en.wikipedia.org/wiki/Song_Dynasty), [Butterfly from Wikipedia](https://en.wikipedia.org/wiki/Butterfly)
2. [↑](#cite_ref-2) [Dap Hartmann](/Dap_Hartmann "Dap Hartmann") (**1988**). *Butterfly Boards*. [ICCA Journal, Vol. 11, Nos. 2/3](/ICGA_Journal#11_23 "ICGA Journal")
3. [↑](#cite_ref-3) [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1983**). *The History Heuristic*. [ICCA Journal, Vol. 6, No. 3](/ICGA_Journal#6_3 "ICGA Journal")
4. [↑](#cite_ref-4) [Dap Hartmann](/Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 1: Grandmasters have Insights - the Problem is what to Incorporate into Practical Problems.* [ICCA Journal, Vol. 10, No. 1](/ICGA_Journal#10_1 "ICGA Journal")
5. [↑](#cite_ref-5) [Dap Hartmann](/Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 2: the Notion of Mobility, and the Work of [De Groot](/Adriaan_de_Groot "Adriaan de Groot") and [Slater](/Eliot_Slater "Eliot Slater")*. [ICCA Journal, Vol. 10, No. 2](/ICGA_Journal#10_2 "ICGA Journal")
6. [↑](#cite_ref-6) [Mark Winands](/Mark_Winands "Mark Winands"), [Erik van der Werf](/Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), and [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**2006**). *The Relative History Heuristic*. [CG 2006](/CG_2006 "CG 2006"), [pdf](http://www.cs.unimaas.nl/m.winands/documents/relhis.pdf)

**[Up one Level](/Move_Ordering "Move Ordering")**