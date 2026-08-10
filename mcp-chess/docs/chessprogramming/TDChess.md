# TDChess

Source: https://www.chessprogramming.org/TDChess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* TDChess**

**TDChess**  
a chess program by [Jonathan Baxter](/Jonathan_Baxter "Jonathan Baxter") based on [KnightCap](/KnightCap "KnightCap") and its [TD learning](/Temporal_Difference_Learning "Temporal Difference Learning") adaption for [minimax](/Minimax "Minimax") search in chess, [TDLeaf](/Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning"). As mentioned by Jonathan, TDChess is about 5-6 times faster in [nodes per second](/Nodes_per_Second "Nodes per Second") than KnightCap. KnightCap had a really complicated [evaluation](/Evaluation "Evaluation") which he had "dumbed down" a lot to get more speed. He also changed the [search](/Search "Search") a fair bit, including how it does [move ordering](/Move_Ordering "Move Ordering") now on the basis of a [static exchange evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation"), and how [quiescence](/Quiescence_Search "Quiescence Search") works. The sorting of moves has become lot faster due to sorting on demand. Also the [book learning](/Book_Learning "Book Learning") is very different from the original KnightCap [[1]](#cite_note-1). TDChess won the [NC3 1999](/NC3_1999 "NC3 1999") [Australasian National Computer Chess Championship](/Australasian_National_Computer_Chess_Championship "Australasian National Computer Chess Championship") [[2]](#cite_note-2).

# See also

- [KnightCap](/KnightCap "KnightCap")
- [Temporal Difference Learning](/Temporal_Difference_Learning "Temporal Difference Learning")

# Forum Posts

- [Re: u2600 Rating List -- Feb 1](https://www.stmintz.com/ccc/index.php?id=41952) by [Jonathan Baxter](/Jonathan_Baxter "Jonathan Baxter"), [CCC](/CCC "CCC"), February 01, 1999

:   [Re: TDchess discussion](https://www.stmintz.com/ccc/index.php?id=42099) by [Jonathan Baxter](/Jonathan_Baxter "Jonathan Baxter"), [CCC](/CCC "CCC"), February 03, 1999

# References

1. [↑](#cite_ref-1) [Re: TDchess discussion](https://www.stmintz.com/ccc/index.php?id=42099) by [Jonathan Baxter](/Jonathan_Baxter "Jonathan Baxter"), [CCC](/CCC "CCC"), February 03, 1999
2. [↑](#cite_ref-2) [Re: Australian-ch, questions !](https://www.stmintz.com/ccc/index.php?id=87251) by [David Blackman](/David_Blackman "David Blackman"), [CCC](/CCC "CCC"), January 09, 2000

**[Up one Level](/Engines "Engines")**