# Chessmaps Heuristic

Source: https://www.chessprogramming.org/Chessmaps_Heuristic

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Move Ordering](/Move_Ordering "Move Ordering") \* Chessmaps Heuristic**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Polyphony%2C_1932_Paul_Klee%2C_2.jpg/330px-Polyphony%2C_1932_Paul_Klee%2C_2.jpg)](/File:Polyphony,_1932_Paul_Klee,_2.jpg)

[Paul Klee](/Category:Paul_Klee "Category:Paul Klee") - Polyphony, 1922 [[1]](#cite_note-1)

**Chessmaps Heuristic**,  
a move ordering heuristic proposed in 1999 by [Kieran Greer](/Kieran_Greer "Kieran Greer") et al. [[2]](#cite_note-2), which uses a board vector of 64 [square controls](/Square_Control "Square Control") {dominated by White (1), Black (-1), or neutral (0)}, the **Chessmap**, along with king locations, to determine an importance vector of [square](/Squares "Squares") areas or **sectors** by probing a [neural network](/Neural_Networks "Neural Networks"). [Quiet moves](/Quiet_Moves "Quiet Moves") are then sorted by the number and ranking of areas, they influence.

# Sectors

Following square sector definition with arbitrary enumeration had most promising results.

```
  ╔════╤════╤════╦════╤════╦════╤════╤════╗
8 ║    │    │    ║    │    ║    │    │    ║
  ╟────┼─11─┼────║────┼────║────┼─ 9 ┼────╢
7 ║    │    │    ║    7    ║    │    │    ║
  ╠══════════════╣────┼────╠══════════════╣
6 ║    │    │    ║    │    ║    │    │    ║
  ╟────┼─10─┼────╠═════════╣────┼─ 8─┼────╢
5 ║    │    │    ║    │    ║    │    │    ║
  ╠══════════════╣─── 6 ───╠══════════════╣
4 ║    │    │    ║    │    ║    │    │    ║
  ╟────┼─ 2─┼────╠═════════╣────┼─ 4─┼────╢
3 ║    │    │    ║    │    ║    │    │    ║
  ╠══════════════╣────┼────╠══════════════╣
2 ║    │    │    ║    5    ║    │    │    ║
  ╟────┼─ 1─┼────║────┼────║────┼─ 3─┼────╢
1 ║    │    │    ║    │    ║    │    │    ║
  ╚════╧════╧════╩════╧════╩════╧════╧════╝
     A    B    C    D    E    F    G    H
```

# Neural Network

## Topology

The input layer has 70 neurons, 64 for each square of the chessmap, and six for the relative king positions concerning sectors. Each of the 12 output neurons correspondents to one sector. Testing suggested that a 3-layer architecture with 16 hidden nodes being a good number [[3]](#cite_note-3).

## Training

The [supervised learning](/Supervised_Learning "Supervised Learning") [backpropagation algorithm](/Neural_Networks#Backpropagation "Neural Networks") on a 10000 position training set, generated from complete and randomly chosen chess games taken from master and grandmaster play, was used to train the neural network. For each position in the set, the Chessmap was calculated, and the desired output was a vector quantifying the sector influences of the move played in that position, that is for each sector whether the move increased (+1), decreased (-1) the control, or was neutral (0). All positions were considered from the White side, so when it was Black to move the position was [color flipped](/Color_Flipping "Color Flipping").

Backpropagation algorithm for a 3-layer network [[4]](#cite_note-4):

```
   initialize the weights in the network (often small random values)
   do
      for each example e in the training set
         O = neural-net-output(network, e)  // forward pass
         T = teacher output for e
         compute error (T - O) at the output units
         compute delta_wh for all weights from hidden layer to output layer  // backward pass
         compute delta_wi for all weights from input layer to hidden layer   // backward pass continued
         update the weights in the network
   until all examples classified correctly or stopping criterion satisfied
   return the network
```

# Results

Various experiments were conducted to compare the performance of the Chessmaps Heuristic with the [History Heuristic](/History_Heuristic "History Heuristic") on the 24 positions of the [Bratko-Kopec Test](/Bratko-Kopec_Test "Bratko-Kopec Test"). Both reduce a randomly ordered tree by about 80%, in favor to HH which can perform the search in much less time. However, along with [iterative deepening](/Iterative_Deepening "Iterative Deepening"), and more refined move ordering strategies concerning [captures](/Captures "Captures"), forced and unsafe moves, the Chessmaps Heuristic got the upper hand in node reductions, specially in combination of an additional heuristic to store the last sector that caused a cutoff at each [ply](/Ply "Ply"), quite similar to a killer slot. This sector was then retrieved and ordered first in any sector ordering, overriding the output of the neural network [[5]](#cite_note-5). The Chessmaps Heuristic is applied in [Kieran Greer's](/Kieran_Greer "Kieran Greer") chess playing program [ChessMaps](/ChessMaps "ChessMaps"), written in [C#](/C_sharp "C sharp") [[6]](#cite_note-6).

# Résumé

In his 2012 paper *Tree Pruning for New Search Techniques in Computer Games*, [Kieran Greer](/Kieran_Greer "Kieran Greer") further outlines the Chessmaps Heuristic [[7]](#cite_note-7):

```
This research has been carried out using an existing computer chess game-playing program called Chessmaps. The Chessmaps Heuristic  was created as part of a DPhil research project that was completed in 1998. The intention was to try and add some intelligence into a chess game-playing program. If the goal is to build the best possible chess program, then the experience-based approach has probably solved the problem already, as the best programs are now better or at least equal to the best human players. Computer chess can also be used, however, simply as a domain for testing AI-related algorithms. It is still an interesting platform for trying to mimic the human thought process or add human-like intelligence to a game-playing program. Exactly this argument, along with some other points made in this paper, are also written or thought about. While chess provides too much variability for the whole game to be defined, it is still a small enough domain to make it possible to accurately evaluate different kinds of search and evaluation processes. It provides complete information about its environment, meaning that the evaluation functions can be reliable, and is not so complex that trying to encapsulate the process in a comprehensive manner would be impossible.
```

and further

```
The Chessmaps Heuristic is therefore used as the move-ordering heuristic at each position in the tree search. The neural network was really only used to order the moves in the “other” moves category, although this would still be a large majority of the moves. The research therefore resulted in a heuristic that was knowledge based, but also still lightweight enough to be used as part of a brute-force alpha-beta (α-β) search. Test results showed that it would reduce the search by more than the History Heuristic, but because of its additional computational requirements; it would use more time to search for a move and would ultimately be inferior. The heuristic, however, proved difficult to optimize in code, for example, trying to create quick move generators through bitmap boards, and so the only way to reduce the search time would probably be to introduce more AI-related techniques into the program. This has led to the following new suggestion for dynamic move sequences.
```

# See also

- [Chunking](/Chunking "Chunking")
- [Guard Heuristic](/Guard_Heuristic "Guard Heuristic")
- [History Heuristic](/History_Heuristic "History Heuristic")
- [Learning](/Learning "Learning")
- [Neural MoveMap Heuristic](/Neural_MoveMap_Heuristic "Neural MoveMap Heuristic")
- [Neural Networks](/Neural_Networks "Neural Networks")
- [Pattern Recognition](/Pattern_Recognition "Pattern Recognition")

# Publications

- [Kieran Greer](/Kieran_Greer "Kieran Greer") (**1998**). *A Neural Network Based Search Heuristic and its Application to Computer Chess*. D.Phil. Thesis, [University of Ulster](https://en.wikipedia.org/wiki/University_of_Ulster)
- [Kieran Greer](/Kieran_Greer "Kieran Greer"), [Piyush Ojha](/index.php?title=Piyush_Ojha&action=edit&redlink=1 "Piyush Ojha (page does not exist)"), [David A. Bell](/index.php?title=David_A._Bell&action=edit&redlink=1 "David A. Bell (page does not exist)") (**1999**). *A Pattern-Oriented Approach to Move Ordering: the Chessmaps Heuristic*. [ICCA Journal, Vol. 22, No. 1](/ICGA_Journal#22_1 "ICGA Journal")
- [Kieran Greer](/Kieran_Greer "Kieran Greer") (**2000**). *[Computer chess move-ordering schemes using move influence](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TYF-40TY77M-3&_user=10&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=7858eb0d6e100295c197661d1d454e26)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 120, No. 2
- [Levente Kocsis](/Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](/Eric_Postma "Eric Postma"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_11)*. [CG 2002](/CG_2002 "CG 2002")
- [Kieran Greer](/Kieran_Greer "Kieran Greer") (**2012**). *[Tree Pruning for New Search Techniques in Computer Games](http://www.hindawi.com/journals/aai/2013/357068/)*. Advances in Artificial Intelligence, Vol. 2013

# External Links

- [Backpropagation from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation)
- [Feedforward neural network from Wikipedia](https://en.wikipedia.org/wiki/Feedforward_neural_network)
- [Probabilistic neural network from Wikipedia](https://en.wikipedia.org/wiki/Probabilistic_neural_network)
- [ChessMaps Download](http://www.distributedcomputingsystems.co.uk/chessmapsdownload.html) by [Kieran Greer](/Kieran_Greer "Kieran Greer")

# References

1. [↑](#cite_ref-1) [Paul Klee](/Category:Paul_Klee "Category:Paul Klee") - Polyphony, 1922, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Kunstmuseum Basel](https://en.wikipedia.org/wiki/Kunstmuseum_Basel)
2. [↑](#cite_ref-2) [Kieran Greer](/Kieran_Greer "Kieran Greer"), [Piyush Ojha](/index.php?title=Piyush_Ojha&action=edit&redlink=1 "Piyush Ojha (page does not exist)"), [David A. Bell](/index.php?title=David_A._Bell&action=edit&redlink=1 "David A. Bell (page does not exist)") (**1999**). *A Pattern-Oriented Approach to Move Ordering: the Chessmaps Heuristic*. [ICCA Journal, Vol. 22, No. 1](/ICGA_Journal#22_1 "ICGA Journal")
3. [↑](#cite_ref-3) [Kieran Greer](/Kieran_Greer "Kieran Greer") (**2000**). *[Computer chess move-ordering schemes using move influence](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TYF-40TY77M-3&_user=10&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=7858eb0d6e100295c197661d1d454e26)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 120, No. 2
4. [↑](#cite_ref-4) [Backpropagation algorithm from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation#Algorithm)
5. [↑](#cite_ref-5) [Kieran Greer](/Kieran_Greer "Kieran Greer") (**2000**). *[Computer chess move-ordering schemes using move influence](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TYF-40TY77M-3&_user=10&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=7858eb0d6e100295c197661d1d454e26)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 120, No. 2
6. [↑](#cite_ref-6) [ChessMaps Download](http://www.distributedcomputingsystems.co.uk/chessmapsdownload.html)
7. [↑](#cite_ref-7) [Kieran Greer](/Kieran_Greer "Kieran Greer") (**2012**). *[Tree Pruning for New Search Techniques in Computer Games](http://www.hindawi.com/journals/aai/2013/357068/)*. Advances in Artificial Intelligence, Vol. 2013

**[Up one Level](/Move_Ordering "Move Ordering")**