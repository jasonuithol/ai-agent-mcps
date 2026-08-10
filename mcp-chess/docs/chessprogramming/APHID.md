# APHID

Source: https://www.chessprogramming.org/APHID

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Parallel Search](/Parallel_Search "Parallel Search") \* APHID**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Aphidoidea_puceron_Luc_Viatour.jpg/330px-Aphidoidea_puceron_Luc_Viatour.jpg)](/File:Aphidoidea_puceron_Luc_Viatour.jpg)

Two adult aphids [[1]](#cite_note-1)

**APHID**, (Asynchronous Parallel Hierarchical Iterative Deepening)  
an asynchronous parallel [alpha-beta](/Alpha-Beta "Alpha-Beta") based search algorithm developed and elaborated by [Mark Brockington](/Mark_Brockington "Mark Brockington") as topic of his Ph.D. thesis at the Department of Computing Science, [University of Alberta](/University_of_Alberta "University of Alberta") [[2]](#cite_note-2), along with his thesis advisor [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"). APHID uses repeated depth-limited searches of the top of the [search tree](/Search_Tree "Search Tree") to instantiate, update and [load balance](https://en.wikipedia.org/wiki/Load_balancing_(computing)) work lists for other processors. APHID can be seen as a [master/slave](https://en.wikipedia.org/wiki/Master/slave_(technology)) model, but can be generalized to a hierarchical processor tree.

# Library

APHID has been programmed as an easy-to-implement, game-independent library [[3]](#cite_note-3), and was implemented into the chess program [The Turk](/The_Turk "The Turk") with less than one day of programming effort [[4]](#cite_note-4). It was further tested in [Crafty](/Crafty "Crafty") in chess, in [Chinook](https://en.wikipedia.org/wiki/Chinook_(draughts_player)) in the domain of [Checkers](/Checkers "Checkers"), and in Brockington's [Othello](/Othello "Othello") program *Keyano* [[5]](#cite_note-5). APHID yields reasonable performance on a [network](https://en.wikipedia.org/wiki/Computer_network) of [workstations](https://en.wikipedia.org/wiki/Workstation), an architecture where it is extremely difficult to use a [shared transposition table](/Shared_Hash_Table "Shared Hash Table") effectively. More recently, APHID was used within the [ChessBrain](/ChessBrain "ChessBrain") project of over 2000 [internet](https://en.wikipedia.org/wiki/Internet) connected machines running [Beowulf](/Beowulf "Beowulf") [[6]](#cite_note-6).

# How it works

The master is responsible for searching the top d' [plies](/Ply "Ply") of the d-ply [tree](/Search_Tree "Search Tree") inside its [iterative deepening](/Iterative_Deepening "Iterative Deepening") frame. When the master reaches a [leaf](/Leaf_Node "Leaf Node") of the d'-ply tree, it uses either a (d-d')-ply search result already available from the slave, or the "best available" i.e. using guessed scores from shallower previous searches marked as **uncertain**. As values get backed up the tree, the master maintains a count of how many uncertain nodes have been visited in a pass of the tree, and has to repeat the root search until all contributing leaves have reliable, certain results. By using the guessed score and expected [node types](/Node_Types "Node Types"), the master decides which child-nodes are searched sequentially or in parallel.

[![Aphidybw.jpg](/images/2/23/Aphidybw.jpg)](/File:Aphidybw.jpg)

Location of Parallelism in typical APHID and [YBW](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept") [search trees](/Search_Tree "Search Tree") [[7]](#cite_note-7)

The slave process essentially executes the same code that a sequential [alpha-beta](/Alpha-Beta "Alpha-Beta") searcher would. It looks in the local copy of the so called APHID table, initially allocated and supplied by the master, to find the highest priority node to search. After finishing the search, it reports the result back to the master, getting an update to its APHID table entry in return.

# See also

- [ChessBrain](/ChessBrain "ChessBrain")
- [Crafty](/Crafty "Crafty")
- [The Turk](/The_Turk "The Turk")
- [Young Brothers Wait Concept](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept")

# Publications

- [Mark Brockington](/Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1996**). *The APHID Parallel αβ Search Algorithm*. Technical Report 96-07, Department of Computing Science, [University of Alberta](/University_of_Alberta "University of Alberta"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.8215&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Mark Brockington](/Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *APHID Game-Tree Search*. [Advances in Computer Chess 8](/Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
- [Mark Brockington](/Mark_Brockington "Mark Brockington") (**1998**). *Asynchronous Parallel Game-Tree Search*. Ph.D. thesis, [University of Alberta](/University_of_Alberta "University of Alberta"), [pdf](http://www.collectionscanada.gc.ca/obj/s4/f2/dsk2/ftp02/NQ29023.pdf)
- [Mark Brockington](/Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1999**). *APHID: Asynchronous Parallel Game-Tree Search*. Department of Computing Science, [University of Alberta](/University_of_Alberta "University of Alberta"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.33.9870&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Mark Brockington](/Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**2000**). *APHID: Asynchronous Parallel Game-Tree Search*. [Journal of Parallel and Distributed Computing](https://www.journals.elsevier.com/journal-of-parallel-and-distributed-computing), Vol. 60, No. 2

# Forum Posts

- [Chess over LAN revisited - APHID](https://www.stmintz.com/ccc/index.php?id=189126) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), September 17, 2001

:   [APHID , advances in ICCA #8](https://www.stmintz.com/ccc/index.php?id=189259) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), September 18, 2001

- [Deep Crafty](https://groups.google.com/d/msg/rec.games.chess.computer/3Z5eCrUmA5U/x_eLJS4kELEJ) by Donald O. Davis, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 29, 2001
- [asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), April 06, 2010

:   [Re: asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652&start=8) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), April 07, 2010
:   [Re: asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652&start=11) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), April 08, 2010

- [scorpio can run on 8192 cores](http://www.talkchess.com/forum/viewtopic.php?t=57343) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), August 22, 2015 » [Scorpio](/Scorpio "Scorpio")

:   [Re: scorpio can run on 8192 cores](http://www.talkchess.com/forum/viewtopic.php?t=57343&start=8) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), August 30, 2015

# External Links

## Game Tree Search

- [APHID Parallel Game-Tree Search Library](http://webdocs.cs.ualberta.ca/~games/aphid/index.html)

## Misc

- [Aphid from Wikipedia](https://en.wikipedia.org/wiki/Aphid)
- [aphid - Wiktionary](https://en.wiktionary.org/wiki/aphid)
- [Aphid (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Aphid_(disambiguation))

# References

1. [↑](#cite_ref-1) [Aphidoidea](https://en.wikipedia.org/wiki/Aphid) in [Belgium](https://en.wikipedia.org/wiki/Belgium), [Image](https://commons.wikimedia.org/wiki/File:Aphidoidea_puceron_Luc_Viatour.jpg) by [Luc Viatour](https://commons.wikimedia.org/wiki/User:Lviatour), 2008, [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Mark Brockington](/Mark_Brockington "Mark Brockington") (**1998**). *Asynchronous Parallel Game-Tree Search*. Ph.D. thesis, [University of Alberta](/University_of_Alberta "University of Alberta"), [pdf](http://www.collectionscanada.gc.ca/obj/s4/f2/dsk2/ftp02/NQ29023.pdf)
3. [↑](#cite_ref-3) [APHID Parallel Game-Tree Search Library](http://webdocs.cs.ualberta.ca/~games/aphid/index.html)
4. [↑](#cite_ref-4) [Mark Brockington](/Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *APHID Game-Tree Search*. [Advances in Computer Chess 8](/Advances_in_Computer_Chess_8 "Advances in Computer Chess 8"), 4. Experiments pp. 83
5. [↑](#cite_ref-5) [Keyano (Othello) Home Page](https://webdocs.cs.ualberta.ca/~games/keyano/)
6. [↑](#cite_ref-6) [Colin Frayn](/Colin_Frayn "Colin Frayn"), [Carlos Justiniano](/Carlos_Justiniano "Carlos Justiniano"), [Kevin Lew](/Kevin_Lew "Kevin Lew") (**2006**). *ChessBrain II – A Hierarchical Infrastructure for Distributed Inhomogeneous Speed-Critical Computation*. [pdf](http://www.chessbrain.net/docs/chessbrainII.pdf)
7. [↑](#cite_ref-7) Image cropped from Figure 4, pp. 6 in [Mark Brockington](/Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1996**). *The APHID Parallel αβ Search Algorithm*. Technical Report 96-07, Department of Computing Science, [University of Alberta](/University_of_Alberta "University of Alberta"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.8215&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)

**[Up one level](/Parallel_Search "Parallel Search")**