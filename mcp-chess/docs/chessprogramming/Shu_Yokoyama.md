# Shu Yokoyama

Source: https://www.chessprogramming.org/Shu_Yokoyama

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Shu Yokoyama**

[![](/images/8/83/ShuYokoyama.jpg)](https://acg2015.wordpress.com/videos-of-presentations/)

Shu Yokoyama [[1]](#cite_note-1)

**Shu Yokoyama**,  
a Japanese computer scientist affiliated with the Graduate School of Arts and Sciences, [University of Tokyo](https://en.wikipedia.org/wiki/University_of_Tokyo). His research interests include game playing algorithms and [search](/Search "Search"), and in particular massively [parallel](/Parallel_Search "Parallel Search") or distributed search algoritms. At the [Advances in Computer Games 14](/Advances_in_Computer_Games_14 "Advances in Computer Games 14") conference in [Leiden](/Leiden_University "Leiden University") 2015, he introduced the distributed search algorithm dubbed **P-GPP**, or pipelined game position parallelization.

# P-GPP

Along with [Tomoyuki Kaneko](/Tomoyuki_Kaneko "Tomoyuki Kaneko") and [Tetsuro Tanaka](/Tetsuro_Tanaka "Tetsuro Tanaka") [[2]](#cite_note-2), Shu Yokoyama worked on pipelined game position parallelization (P-GPP), applied to [Shogi](/Shogi "Shogi") inside [GPS Shogi](/index.php?title=GPS_Shogi&action=edit&redlink=1 "GPS Shogi (page does not exist)"), and to [Chess](/Chess "Chess") using [Stockfish DD](/Stockfish "Stockfish"). GPP conducts a [minimax](/Minimax "Minimax") search by integrating the results obtained locally by workers assigned to [leaf nodes](/Leaf_Node "Leaf Node") of a master [tree](/Search_Tree "Search Tree"). The [root](/Root "Root") of a master tree corresponds to the current [game position](/Chess_Position "Chess Position"), and the number of nodes of the master tree must be the number of workers available. Neither [transposition table](/Transposition_Table "Transposition Table") nor [windows](/Window "Window") are shared. P-GPP both extends [optimistic pondering](/GridChess#OptimisticPondering "GridChess") [[3]](#cite_note-3), and game position parallelization by improving worker management. In P-GPP, positions are assigned to workers automatically by a [greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm) on the basis of [realization](https://en.wikipedia.org/wiki/Realization_%28probability%29) probabilities, acquired from game records and a playing program. The realization probability of a node, defined as the product of the transition probability of each move, is the probability that the corresponding sequence of moves is actually played. By definition, the realization probability of the root is one. After making a move during the course of the game, all workers formerly assigned to siblings of the made move were reassigned to new leaves of the growing new root, deepening and widening the search tree.

[Stockfish DD](/Stockfish "Stockfish") was adopted as a worker program, adding a function of reporting information extending the [UCI](/UCI "UCI") protocol. Each worker and the master are connected via standard [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) [sockets](https://en.wikipedia.org/wiki/Network_socket). The master is implemented in [C++](/Cpp "Cpp") with the [boost](https://en.wikipedia.org/wiki/Boost_%28C%2B%2B_libraries%29)/[asio](https://en.wikipedia.org/wiki/Asio_C%2B%2B_library) library. For a worker, a utility program [Netcat](https://en.wikipedia.org/wiki/Netcat) is adopted as a proxy connecting [standard streams](https://en.wikipedia.org/wiki/Standard_streams) and a TCP socket. To simulate a distributed environment, they used at most 64 cores in two computers each of which is equipped with two [Intel](/Intel "Intel") [Xeon E5-4650](/X86-64 "X86-64") processors. Stockfish ran as a sequential program using a single [thread](/Thread "Thread"). Each worker was allowed to use 32MiB for its transposition table . Shu Yokoyama et al confirmed improved playing strength with up to sixty Stockfish workers [[4]](#cite_note-4).

# See also

- [GridChess](/GridChess "GridChess")

:   [Optimistic Pondering](/GridChess#OptimisticPondering "GridChess")

- [Stockfish](/Stockfish "Stockfish")

# Selected Publications

- Shu Yokoyama, [Tomoyuki Kaneko](/Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Tetsuro Tanaka](/Tetsuro_Tanaka "Tetsuro Tanaka") (**2015**). *Parameter-Free Tree Style Pipeline in Asynchronous Parallel Game-Tree Search*. [Advances in Computer Games 14](/Advances_in_Computer_Games_14 "Advances in Computer Games 14"), [pdf](http://www.graco.c.u-tokyo.ac.jp/~kaneko/papers/acg2015-yokoyama.pdf)

# External Links

- [Shu Yokoyama — slides](https://acg2015.wordpress.com/videos-of-presentations/) from [Advances in Computer Games 14](/Advances_in_Computer_Games_14 "Advances in Computer Games 14"), Video Download, July 03, 2015

# References

1. [↑](#cite_ref-1) Shu Yokoyama lecturing on *Parameter-Free Tree Style Pipeline in Asynchronous Parallel Game-Tree Search*/ at [Advances in Computer Games 14](/Advances_in_Computer_Games_14 "Advances in Computer Games 14"), [Shu Yokoyama — slides](https://acg2015.wordpress.com/videos-of-presentations/). Video Download, July 03, 2015, capture at 2:55
2. [↑](#cite_ref-2) [Tetsuro Tanaka](/Tetsuro_Tanaka "Tetsuro Tanaka"), [Tomoyuki Kaneko](/Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2010**). *Massively Parallel Execution of Shogi Programs*. The Special Interest Group Technical Reports of IPSJ. 2, Vol. GI-24, No.8 (Japanese)
3. [↑](#cite_ref-3) [Kai Himstedt](/Kai_Himstedt "Kai Himstedt") (**2012**). *GridChess: Combining Optimistic Pondering with the Young Brothers Wait Concept*. [ICGA Journal, Vol. 35, No. 2](/ICGA_Journal#35_2 "ICGA Journal")
4. [↑](#cite_ref-4) Shu Yokoyama, [Tomoyuki Kaneko](/Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Tetsuro Tanaka](/Tetsuro_Tanaka "Tetsuro Tanaka") (**2015**). *Parameter-Free Tree Style Pipeline in Asynchronous Parallel Game-Tree Search*. [Advances in Computer Games 14](/Advances_in_Computer_Games_14 "Advances in Computer Games 14"), [pdf](http://www.graco.c.u-tokyo.ac.jp/~kaneko/papers/acg2015-yokoyama.pdf)

**[Up one level](/People "People")**