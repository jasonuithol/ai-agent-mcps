# Odd-Even Effect

Source: https://www.chessprogramming.org/Odd-Even_Effect

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Alpha-Beta](/Alpha-Beta "Alpha-Beta") \* Odd-Even Effect**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Odd_even.png/330px-Odd_even.png)](/File:Odd_even.png)

Odd Numbers and Even Numbers [[1]](#cite_note-1)

The **Odd-Even Effect** of [Alpha-Beta](/Alpha-Beta "Alpha-Beta") is caused by the topology of the [minimal game tree](/Search_Tree#MinimalGameTree "Search Tree") of uniform [depth](/Depth "Depth") **n** and [branching factor](/Branching_Factor "Branching Factor") **b**. [Michael Levin](/Michael_Levin "Michael Levin") found the formula of the number of [leaf nodes](/Leaf_Node "Leaf Node"), which was published in [Edwards'](/Daniel_Edwards "Daniel Edwards") and [Hart's](/Timothy_Hart "Timothy Hart") 1961 Alpha-Beta paper [[2]](#cite_note-2) .

# Even Leaves

```
2bn/2 - 1
```

# Odd Leaves

```
b(n+1)/2 + b(n-1)/2 - 1
```

# Node Types

Number of Leaf nodes of a certain [Node type](/Node_Types "Node Types") at depth n [[3]](#cite_note-3):

**n = even:**

```
PVn = 1
CUTn = bn/2 - 1     = CUTn-1
ALLn = bn/2 - 1     = ALLn-1 + bn/2 - b(n-2)/2
```

**n = odd:**

```
PVn = 1
CUTn = b(n+1)/2 - 1 = CUTn-1 + b(n+1)/2 + b(n-1)/2
ALLn = b(n-1)/2 - 1 = ALLn-1
```

So for the sum of the Leaf-nodes at depth n as well as the total sum of nodes (including [interior nodes](/Interior_Node "Interior Node")) up to depth n holds

```
ALLn = CUTn-1
```

# Leaves by Depth

Assuming a constant [branching factor](/Branching_Factor "Branching Factor") of 40, this results in following number of leaves, using the [floor and ceiling](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) formulas :

```
CUTn = b⌈n/2⌉ - 1
ALLn = b⌊n/2⌋ - 1
```

[number of leaves with depth n and b = 40](/Template:Number_of_Leaves "Template:Number of Leaves")

| depth | worst case | best case | PV | CUT | ALL |
| n | bn | b⌈n/2⌉ + b⌊n/2⌋ - 1 | 1 | b⌈n/2⌉ - 1 | b⌊n/2⌋ - 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 40 | 40 | 1 | 39 | 0 |
| 2 | 1,600 | 79 | 1 | 39 | 39 |
| 3 | 64,000 | 1,639 | 1 | 1,599 | 39 |
| 4 | 2,560,000 | 3,199 | 1 | 1,599 | 1,599 |
| 5 | 102,400,000 | 65,569 | 1 | 63,999 | 1,599 |
| 6 | 4,096,000,000 | 127,999 | 1 | 63,999 | 63,999 |
| 7 | 163,840,000,000 | 2,623,999 | 1 | 2,559,999 | 63,999 |
| 8 | 6,553,600,000,000 | 5,119,999 | 1 | 2,559,999 | 2,559,999 |

resulting in following

# Leaf Ratios

**n = even:**

[![OddEven EvenFormula.jpg](/images/c/c4/OddEven_EvenFormula.jpg)](/File:OddEven_EvenFormula.jpg)

**n = odd:**

[![OddEven OddFormula.jpg](/images/a/a3/OddEven_OddFormula.jpg)](/File:OddEven_OddFormula.jpg)

# Iterative Deepening

Inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework, the odd-even effect causes an asymmetry in time usage. Even-odd transitions grow (much) more than odd-even. The effect diminishes due to [quiescence search](/Quiescence_Search "Quiescence Search") and [selectivity](/Selectivity "Selectivity") in the upper part of the tree. However, past and recent programs addressed that issue. For instance [L'Excentrique](/L%27Excentrique "L'Excentrique") used two [ply](/Ply "Ply") increments [[4]](#cite_note-4), and [Bebe](/Bebe "Bebe") had no quiescence at all, and searched in two ply increments as well [[5]](#cite_note-5). Other programs used fractional plies for [extensions](/Extensions#FractionalExtensions "Extensions") [[6]](#cite_note-6) and [ID](/Iterative_Deepening "Iterative Deepening") increments.

# Score Oscillation

Additionally, many programs exhibit an effect on the [score](/Score "Score") based on the [parity](https://en.wikipedia.org/wiki/Parity_%28mathematics%29) of the search depth due to the extra tempo of odd ply searches. Scores are stable when one looks at results from the odd plies only, or even plies only, but are sometimes unstable when they are mixed. One remedial on this odd-even effect is to apply a [tempo bonus](/Tempo "Tempo") in [leaf evaluation](/Evaluation "Evaluation") for the [side to move](/Side_to_move "Side to move").

# See also

- [Asymmetric Evaluation](/Asymmetric_Evaluation "Asymmetric Evaluation")
- [Minimax Wall](/Window#MinimaxWall "Window")
- [Parity Pruning](/Parity_Pruning "Parity Pruning")

# Forum Posts

- [Odd ply versus even ply searches](https://groups.google.com/d/msg/rec.games.chess.computer/-0DHwUHcBio/FJnxLgRajgUJ) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), February 28, 1996 » [Bebe](/Bebe "Bebe")
- [PROG: odd/even score alternance](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d3e7bdb00afc9dc4) by [Rémi Coulom](/R%C3%A9mi_Coulom "Rémi Coulom"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), June 5, 1997 » [Tempo](/Tempo "Tempo")
- [pv score oscillation](https://www.stmintz.com/ccc/index.php?id=10903) by [Willie Wood](/Will_Singleton "Will Singleton"), [CCC](/CCC "CCC"), October 18, 1997
- [Node counts at a given depth/iteration in search](http://www.open-chess.org/viewtopic.php?f=5&t=1403) by [BB+](/Mark_Watkins "Mark Watkins"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 23, 2011
- [CUT/ALL nodes ratio](http://www.talkchess.com/forum/viewtopic.php?t=48205) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), June 06, 2013
- [Asymmetrical evaluation](http://www.talkchess.com/forum/viewtopic.php?t=60262) by [Laurie Tunnicliffe](/Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](/CCC "CCC"), May 24, 2016 » [Asymmetric Evaluation](/Asymmetric_Evaluation "Asymmetric Evaluation")

# External Links

- [Parity (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Parity_(mathematics))

# References

1. [↑](#cite_ref-1) Image by TNSENesamaniTpr, July 06, 2017, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Daniel Edwards](/Daniel_Edwards "Daniel Edwards"), [Timothy Hart](/Timothy_Hart "Timothy Hart"), (**1961**). *The Alpha-Beta Heuristic*. AIM-030, available from [DSpace](http://dspace.mit.edu/handle/1721.1/6098) at [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
3. [↑](#cite_ref-3) [CUT/ALL nodes ratio](http://www.talkchess.com/forum/viewtopic.php?t=48205) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), June 06, 2013
4. [↑](#cite_ref-4) [Eric Thé](/Eric_Th%C3%A9 "Eric Thé") (**1992**). *[An analysis of move ordering on the efficiency of alpha-beta search](http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=56753&local_base=GEN01-MCG02)*. Master's thesis, [McGill University](/McGill_University "McGill University"), advisor [Monroe Newborn](/Monroe_Newborn "Monroe Newborn")
5. [↑](#cite_ref-5) [Odd ply versus even ply searches](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/fb40c7c141dc062a) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), February 28, 1996
6. [↑](#cite_ref-6) [David Levy](/David_Levy "David Levy"), [David Broughton](/David_Broughton "David Broughton"), and [Mark Taylor](/Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](/ICGA_Journal#12_1 "ICGA Journal")

**[Up one level](/Alpha-Beta "Alpha-Beta")**