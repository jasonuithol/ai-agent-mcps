# David J. Wu

Source: https://www.chessprogramming.org/David_J._Wu

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* David J. Wu**

[![](/images/1/17/DavidJWu.jpg)](http://www.kingpinchess.net/2015/07/arimaa-game-over/)

David J. Wu [[1]](#cite_note-1)

**David Jian Wu**,  
an American computer scientist and computer games researcher and programmer, who balances a mixture of software development and research within the financial industry [[2]](#cite_note-2).
He defended his B.Sc. degree in 2011 at [Harvard College](https://en.wikipedia.org/wiki/Harvard_College), [Harvard University](/Harvard_University "Harvard University"), delivering the thesis *Move Ranking and Evaluation in the Game of Arimaa* [[3]](#cite_note-3).
David J. Wu is author of the [Arimaa](/Arimaa "Arimaa") bot **Sharp**, and inspired by [AlphaZero](/AlphaZero "AlphaZero"), the [Go](/Go "Go") playing program **KataGo** [[4]](#cite_note-4) [[5]](#cite_note-5).

# Sharp

The [Arimaa](/Arimaa "Arimaa") playing bot **Sharp** won the 2015 *Arimaa Challenge* and the then $12,000 USD prize by defeating each of three top-ranked human players in a three game series [[6]](#cite_note-6).
It already played the 2008 Arimaa computer tournament, and became runner-up behind [David Fotland’s](/David_Fotland "David Fotland") program *Bomb*, and further won the 2011 and 2014 tournaments but not the contest against the best human players of that time [[7]](#cite_note-7).
Sharp's design was elaborated by its author in the 2015 [ICGA Journal, Vol. 38, No. 1](/ICGA_Journal#38_1 "ICGA Journal") [[8]](#cite_note-8).
It follows the same fundamental design as strong Chess programs, using an [iterative deepening](/Iterative_Deepening "Iterative Deepening") [depth](/Depth "Depth") limited [alpha-beta search](/Alpha-Beta "Alpha-Beta") and various enhancements within a [parallel search](/Parallel_Search "Parallel Search") algorithm conceptually similar to the [dynamic tree splitting](/Dynamic_Tree_Splitting "Dynamic Tree Splitting") described by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") in 1994 [[9]](#cite_note-9).
Sharp further implements several Arimaa-specific search enhancements with four steps per move, such as static goal detection and [capture](/Captures "Captures") [generation](/Move_Generation "Move Generation"), and continues to use and benefit greatly from a [move ordering](/Move_Ordering "Move Ordering") function developed in 2011 as described in Wu's thesis - the move ordering function is the result of training a slightly generalized [Bradley-Terry model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model) over thousands of expert Arimaa games to [learn](/Learning "Learning") to predict expert player's moves, using the same optimization procedure described by [Rémi Coulom](/R%C3%A9mi_Coulom "Rémi Coulom") for computer [Go](/Go "Go") [[10]](#cite_note-10).

# KataGo

KataGo is a [Go](/Go "Go") playing entity inspired by the [AlphaZero](/AlphaZero "AlphaZero") approach of combining [Deep learning](/Deep_Learning "Deep Learning") with [Monte-Carlo Tree Search](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") (MCTS) using pure [reinforcement learning](/Reinforcement_Learning "Reinforcement Learning") aka self play to train the [deep neural network](/Neural_Networks "Neural Networks").
Due to modifications and enhancements of the AlphaZero-like training process, self-play with a only few strong [GPUs](/GPU "GPU") of between one and several days is sufficient to reach somewhere in the range of strong-kyu up to mid-dan strength on the full 19x19 board [[11]](#cite_note-11).

# Selected Publications

[[12]](#cite_note-12)

- David J. Wu (**2011**). *Move Ranking and Evaluation in the Game of Arimaa*. B.Sc. thesis, [Harvard College](https://en.wikipedia.org/wiki/Harvard_College), [Cambridge, Massachusetts](https://en.wikipedia.org/wiki/Cambridge,_Massachusetts), [pdf](http://arimaa.com/arimaa/papers/DavidWu/djwuthesis.pdf)
- David J. Wu (**2015**). *Designing a Winning Arimaa Program*. [ICGA Journal, Vol. 38, No. 1](/ICGA_Journal#38_1 "ICGA Journal"), [pdf](https://icosahedral.net/downloads/djwu2015arimaa.pdf) [[13]](#cite_note-13)
- David J. Wu (**2019**). *Accelerating Self-Play Learning in Go*. [arXiv:1902.10565](https://arxiv.org/abs/1902.10565) [[14]](#cite_note-14)

# Postings

- [Neural nets for Go - chain pooling?](https://groups.google.com/d/msg/computer-go-archive/WImAk15gRN4/bhA7kSAnBgAJ) by David Wu, [Computer Go Archive](https://groups.google.com/forum/#!forum/computer-go-archive), August 18, 2017

# External Links

- [lightvector · GitHub](https://github.com/lightvector)
- [Arimaa: Game Over?](http://www.kingpinchess.net/2015/07/arimaa-game-over/) by [Andy Lewis](/index.php?title=Andy_Lewis&action=edit&redlink=1 "Andy Lewis (page does not exist)"), [Kingpin Chess Magazine](http://www.kingpinchess.net/), July 11, 2015
- [Arimaa - David J. Wu - Google Play](https://play.google.com/store/apps/details?id=net.icosahedral.arimaa)

# References

1. [↑](#cite_ref-1) Image from [Arimaa: Game Over?](http://www.kingpinchess.net/2015/07/arimaa-game-over/) by [Andy Lewis](/index.php?title=Andy_Lewis&action=edit&redlink=1 "Andy Lewis (page does not exist)"), [Kingpin Chess Magazine](http://www.kingpinchess.net/), July 11, 2015
2. [↑](#cite_ref-2) [Arimaa: Game Over?](http://www.kingpinchess.net/2015/07/arimaa-game-over/) by [Andy Lewis](/index.php?title=Andy_Lewis&action=edit&redlink=1 "Andy Lewis (page does not exist)"), [Kingpin Chess Magazine](http://www.kingpinchess.net/), July 11, 2015
3. [↑](#cite_ref-3) David J. Wu (**2011**). *Move Ranking and Evaluation in the Game of Arimaa*. B.Sc. thesis, [Harvard College](https://en.wikipedia.org/wiki/Harvard_College), [Cambridge, Massachusetts](https://en.wikipedia.org/wiki/Cambridge,_Massachusetts), [pdf](http://arimaa.com/arimaa/papers/DavidWu/djwuthesis.pdf)
4. [↑](#cite_ref-4) [GitHub - lightvector/KataGo: GTP engine and self-play learning in Go](https://github.com/lightvector/KataGo)
5. [↑](#cite_ref-5) [KataGo](https://groups.google.com/g/lczero/c/gecAk5DflmE/m/lUGWpjZXBwAJ) by [Warren D. Smith](/Warren_D._Smith "Warren D. Smith"), [LCZero Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 16, 2021
6. [↑](#cite_ref-6) [The 2015 Arimaa Challenge](http://arimaa.com/arimaa/challenge/2015/)
7. [↑](#cite_ref-7) [Omar Syed](/Omar_Syed "Omar Syed") (**2015**). *The Arimaa Challenge: From Inception to Completion*. [ICGA Journal, Vol. 38, No. 1](/ICGA_Journal#38_1 "ICGA Journal")
8. [↑](#cite_ref-8) David J. Wu (**2015**). *Designing a Winning Arimaa Program*. [ICGA Journal, Vol. 38, No. 1](/ICGA_Journal#38_1 "ICGA Journal")
9. [↑](#cite_ref-9) [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") (**1994**). *[The DTS high-performance parallel tree search algorithm](http://www.cis.uab.edu/hyatt/search.html)*
10. [↑](#cite_ref-10) [Rémi Coulom](/R%C3%A9mi_Coulom "Rémi Coulom") (**2007**). *[Computing Elo Ratings of Move Patterns in the Game of Go](http://remi.coulom.free.fr/Amsterdam2007/)*. [ICGA Journal, Vol. 30, No. 4](/ICGA_Journal#30_4 "ICGA Journal"), [CGW 2007](/CGW_2007 "CGW 2007"), [pdf](https://www.remi-coulom.fr/Amsterdam2007/icgaj.pdf)
11. [↑](#cite_ref-11) [KataGo/README.md at master · lightvector/KataGo · GitHub](https://github.com/lightvector/KataGo/blob/master/README.md)
12. [↑](#cite_ref-12) [dblp: David J. Wu](https://dblp.uni-trier.de/pers/hd/w/Wu:David_J=), including another [David J. Wu](https://www.cs.virginia.edu/dwu4/) ([Cryptography](https://en.wikipedia.org/wiki/Cryptography), [Computer security](https://en.wikipedia.org/wiki/Computer_security))
13. [↑](#cite_ref-13) [Paper describing "Sharp" the program that won the Arimaa Challenge](https://www.game-ai-forum.org/viewtopic.php?f=2&t=83) by ddyer, [Game-AI Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 14, 2016
14. [↑](#cite_ref-14) [Re: catastrophic forgetting](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70704&start=4) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), May 10, 2019

**[Up one level](/People "People")**