# CHUMP

Source: https://www.chessprogramming.org/CHUMP

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* CHUMP**

**CHUMP**, (CHUnking of Moves and Patterns)  
was an experimental chess program by [Fernand Gobet](/Fernand_Gobet "Fernand Gobet") and [Peter Jansen](/Peter_Jansen "Peter Jansen") that [learned](/Learning "Learning") to [recognize](/Pattern_Recognition "Pattern Recognition") piece patterns and associated move sequences, introduced at the [Advances in Computer Chess 7](/Advances_in_Computer_Chess_7 "Advances in Computer Chess 7") conference in 1993. The aim was to model human 'computational' mechanisms, not only to understand better those machanisms in human beings, but to yield techniques and algorithms that could lead to valuable additions to competitive game playing programs, for instance in improving [move ordering](/Move_Ordering "Move Ordering") and in learning search control aka [selectivity](/Selectivity "Selectivity") of classical [alpha-beta](/Alpha-Beta "Alpha-Beta") searchers [[1]](#cite_note-1).

CHUMP is based on [CHREST](/CHREST "CHREST") (Chunk Hierarchy and REtrieval STructures), a computer model of human chess memory and perception [[2]](#cite_note-2). CHREST was inspired by earlier programs [MAPP](/MAPP "MAPP") [[3]](#cite_note-3) and [Perceiver](/Perceiver "Perceiver") [[4]](#cite_note-4) by [Herbert Simon](/Herbert_Simon "Herbert Simon") and colleages. CHREST was not conceived as a component of a game playing program - its knowledge was limited to pattern of chess positions and had no concept of moves, goals and values. In learning about moves and when to make them, CHUMP was the first step towards a game playing, [pattern learning](/index.php?title=Pattern_Learning&action=edit&redlink=1 "Pattern Learning (page does not exist)") chess program. In 1997, [Fernand Gobet](/Fernand_Gobet "Fernand Gobet") developed a second simulation of move-selection called **SEARCH**, which begins to incorporate [search](/Search "Search") processes [[5]](#cite_note-5).

# Structure of CHUMP

CHUMP consists of the following components:

1. [Eye movement](/Eye_Movements "Eye Movements") simulator module
2. [EPAM like](/EPAM "EPAM") discrimination nets, one for piece patterns, one for move sequences
3. [Short-term memory](https://en.wikipedia.org/wiki/Short-term_memory) (STM)
4. [Retrieval structure](/CHREST "CHREST")

## Eye Movements

The [eye movement](/Eye_Movements "Eye Movements") simulator is the only part of the system where the rules of the game influence the learning process. It scans the board, and directs its attention to [pieces](/Pieces "Pieces") and [squares](/Squares "Squares") it expects, given the current node in its discrimination net, attack, defense and [proximity relations](/Distance "Distance") between pieces. It is hoped, that this leads to the formation of meaningful chunks.

## Discrimination and Familiarization

The discrimination nets are based o the [EPAM](/EPAM "EPAM") model of memory and perception, with some differences in the way uses recursion in encoding chunks and in the nature of the discrimination data structure - EPAM uses a tree, CHUMP a graph. Each node in the net contains the image of the object that lead to its creation, and a list of descendants. There are two different types of learning, depending on whether is new or not. If an objcet is new, that is does not match the image of the chunk found in the discrimination net, a new branch is created - dubbed *discrimination*. Otherwise, CHUMP extends the image - called *familiarization*.

## Short-term Memory

[Short-term memory](https://en.wikipedia.org/wiki/Short-term_memory) (STM) is a n-pointer structure (n ≡ 7 for human simulations), in which each pointer refers to a single piece pattern recognized in the position. In CHUMP, to obtain faster learning, an STM size of n = 20 was applied.

## Retrieval Structure

The retrieval structure is an intermediate memory structure that, in humans, allows a rapid access to [long-term memory](https://en.wikipedia.org/wiki/Long-term_memory). In CHUMP. the retrieval structure consists of an internal [board representation](/Board_Representation "Board Representation") - a representation augmented with information about lines, diagonals and directions of movement of the pieces - and the hypothesis - the most information-rich pattern recognized so far, linking for instance to relevant plans.

# Learning

CHUMP builds its discrimination nets for pieces and moves based on the patterns it recognizes when scanning the set of training positions. For each position three learning steps take place.

1. The eye movement recognizes piece pattern, which are discriminated or familiarized inside the piece patterns net.
2. The move actually played is learned inside its move sequence discrimination net.
3. The current move (sequence) is associated with those piece patterns that contain the moving piece on its correct [from square](/Origin_Square "Origin Square"); a link is created between the piece pattern and the move entry in the move sequence discrimination net. If this move has already been associated with the same pattern earlier, its activation (a counter that keeps track of how often a particular move has been associated with a given pattern) is increased.

# Move Proposal

After (or during) learning, CHUMP can use its discrimination nets to suggests moves in certain positions. Again, three steps were applied.

1. The eye movement simulator iterates over all relevant piece patterns.
2. The moves associated with every piece pattern are retrieved from the net, along with the number of chunks associating it and its activation.
3. The move with the greatest number of chunks is prefered, if equal, the move with higher activation is considered best

# Experiments

CHUMP's proposed moves were compared with actual moves in several different learning and testing situations, e.g. games by [Mikhail Tal](https://en.wikipedia.org/wiki/Mikhail_Tal) and positions from the KQKR domain. The experiments show that CHUMP improves performance with learning in all cases.

# See also

- [CHREST](/CHREST "CHREST")
- [Chunker](/Chunker "Chunker")
- [Chunking](/Chunking "Chunking")
- [EPAM](/EPAM "EPAM")
- [Eye Movements](/Eye_Movements "Eye Movements")
- [Learning Chess Programs](/Learning#Programs "Learning")
- [MAPP](/MAPP "MAPP")
- [Pattern Learning](/index.php?title=Pattern_Learning&action=edit&redlink=1 "Pattern Learning (page does not exist)")

# Publications

- [Fernand Gobet](/Fernand_Gobet "Fernand Gobet"), [Peter Jansen](/Peter_Jansen "Peter Jansen") (**1994**). *Towards a Chess Program Based on a Model of Human Memory.* [Advances in Computer Chess 7](/Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
- [Roy W. Roring III](/index.php?title=Roy_W._Roring_III&action=edit&redlink=1 "Roy W. Roring III (page does not exist)") (**2008**). *Reviewing Expert Chess Performance: A Production-Based Theory of Chess Skill*. Ph.D. thesis, advisor [Neil Charness](/index.php?title=Neil_Charness&action=edit&redlink=1 "Neil Charness (page does not exist)"), [Florida State University](https://en.wikipedia.org/wiki/Florida_State_University)
- [Andrew Cook](/index.php?title=Andrew_Cook&action=edit&redlink=1 "Andrew Cook (page does not exist)") (**2008**). *Chunk Learning and Move Prompting: Making Moves in Chess*. Technical Report CSR-08-12, [University of Birmingham](https://en.wikipedia.org/wiki/University_of_Birmingham)

# External Links

## Chess Program

- [CHREST projects - CHUMP](http://www.chrest.info/projects.html)

## Misc

- [chump Wiktionary](https://en.wiktionary.org/wiki/chump)
- [Chump from Wikipedia](https://en.wikipedia.org/wiki/Chump)
- [A Chump at Oxford from Wikipedia](https://en.wikipedia.org/wiki/A_Chump_at_Oxford)

# References

1. [↑](#cite_ref-1) This article incorporates text from [Fernand Gobet](/Fernand_Gobet "Fernand Gobet"), [Peter Jansen](/Peter_Jansen "Peter Jansen") (**1994**). *Towards a Chess Program Based on a Model of Human Memory.* [Advances in Computer Chess 7](/Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
2. [↑](#cite_ref-2)  [Fernand Gobet](/Fernand_Gobet "Fernand Gobet") (**1993**). *[A Computer Model of Chess Memory](http://bura.brunel.ac.uk/handle/2438/2129).* Proceedings of the 15th Annual Meeting of the Cognitive Science Society
3. [↑](#cite_ref-3) [Herbert Simon](/Herbert_Simon "Herbert Simon"), [Kevin J. Gilmartin](/Kevin_J._Gilmartin "Kevin J. Gilmartin") (**1973**). *A Simulation of Memory for Chess Positions*. Cognitive Psychology, Vol. 5, pp. 29-46, reprinted in [Herbert Simon](/Herbert_Simon "Herbert Simon") (**1979**). *[Models of Thought](http://yalepress.yale.edu/yupbooks/book.asp?isbn=9780300024326)*. [Yale University Press](https://en.wikipedia.org/wiki/Yale_University_Press)
4. [↑](#cite_ref-4) [Herbert Simon](/Herbert_Simon "Herbert Simon"), [Michael Barenfeld](/Michael_Barenfeld "Michael Barenfeld") (**1968**). *Information Processing in the Perception of Chess Positions*. [Carnegie Mellon University](/Carnegie_Mellon_University "Carnegie Mellon University"), Paper #127
5. [↑](#cite_ref-5) [Fernand Gobet](/Fernand_Gobet "Fernand Gobet") (**1997**). *A Pattern-Recognition Theory of Search in Expert Problem Solving.* Thinking and Reasoning, Vol. 3, No. 4

**[Up one Level](/Engines "Engines")**