# Deep Pink

Source: https://www.chessprogramming.org/Deep_Pink

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Deep Pink**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Color_icon_pink_v2.svg/330px-Color_icon_pink_v2.svg.png)](/File:Color_icon_pink_v2.svg)

[Shades of pink](https://en.wikipedia.org/wiki/Shades_of_pink) [[1]](#cite_note-1)

**Deep Pink**, [[2]](#cite_note-2)  
an experimental [open source chess engine](/Category:Open_Source "Category:Open Source") by [Erik Bernhardsson](/Erik_Bernhardsson "Erik Bernhardsson"),
written in [Python](/Python "Python") as an attempt to [learn](/Deep_Learning "Deep Learning") and play chess.
Deep Pink applies [negamax](/Negamax "Negamax") [alpha-beta](/Alpha-Beta "Alpha-Beta") and a [deep neural network](/Neural_Networks#Deep "Neural Networks") as [evaluation function](/Evaluation "Evaluation"),
using [Theano](https://en.wikipedia.org/wiki/Theano_%28software%29), [python-chess](/Python-chess "Python-chess"), and [Sunfish](/Sunfish "Sunfish") [[3]](#cite_note-3).
The input representation seems similar to [Octavius](/Octavius "Octavius") with 12x64 nodes, not feeding in [side to move](/Side_to_move "Side to move"), [castling rights](/Castling_Rights "Castling Rights"), and [en passant](/En_passant "En passant") target square.
The first hidden layer has 2048 neurons as well. Bernhardsson used a [GPU](/GPU "GPU") instance to train the net with 100M games for about four days using [stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) with [Nesterov](/Mathematician#YNesterov "Mathematician") momentum [[4]](#cite_note-4)
[[5]](#cite_note-5) [[6]](#cite_note-6) [[7]](#cite_note-7).

# See also

- [Deep Blue](/Deep_Blue "Deep Blue")
- [Deep Learning](/Deep_Learning "Deep Learning")
- [Neural MoveMap Heuristic](/Neural_MoveMap_Heuristic "Neural MoveMap Heuristic")
- [Octavius](/Octavius "Octavius")

# Postings

## 2014

- [Deep learning for… chess](https://erikbern.com/2014/11/29/deep-learning-for-chess) by [Erik Bernhardsson](/Erik_Bernhardsson "Erik Bernhardsson"), November 29, 2014 » [Deep Learning](/Deep_Learning "Deep Learning")
- [Deep learning for chess Comments](https://news.ycombinator.com/item?id=8685840) by mlla, [Hacker News](https://en.wikipedia.org/wiki/Hacker_News), December 2, 2014

:   [As the author of sunfish....](https://news.ycombinator.com/item?id=8686995) by [Thomas Ahle](/Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [Hacker News](https://en.wikipedia.org/wiki/Hacker_News), December 2, 2014
:   [This has been tried many times before, with better-but-still-lackluster results....](https://news.ycombinator.com/item?id=8687273) by halfcat, [Hacker News](https://en.wikipedia.org/wiki/Hacker_News), December 2, 2014

- [Deep learning for… chess (addendum)](https://erikbern.com/2014/12/08/deep-learning-for-chess-addendum) by [Erik Bernhardsson](/Erik_Bernhardsson "Erik Bernhardsson"), December 8, 2014

## 2015 ...

- [Deep Pink Chess Engine Concept...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=60341) by supersharp77, [CCC](/CCC "CCC"), June 01, 2016
- [ŷhat | Deep Learning for ... Chess](http://blog.yhat.com/posts/deep-learning-chess.html) by [Erik Bernhardsson](/Erik_Bernhardsson "Erik Bernhardsson"), February 02, 2017
- [Deep Pink: a chess engine using deep learning](http://www.talkchess.com/forum/viewtopic.php?t=63063) by [Chao Ma](/Chao_Ma "Chao Ma"), [CCC](/CCC "CCC"), February 05, 2017

# External Links

- [GitHub - erikbern/deep-pink: Deep Pink is a chess AI that learns to play chess using deep learning](https://github.com/erikbern/deep-pink)
- [Deep Purple](/Category:Deep_Purple "Category:Deep Purple") - [Hush](https://en.wikipedia.org/wiki/Hush_(Billy_Joe_Royal_song)#Deep_Purple_version), [Shades of Deep Purple](https://en.wikipedia.org/wiki/Shades_of_Deep_Purple) (1968), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Shades of pink](https://en.wikipedia.org/wiki/Shades_of_pink) derived from [Color icon pink.svg](https://commons.wikimedia.org/wiki/File:Color_icon_pink.svg), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) color: #ff1493; [Deep Pink - Shades of pink from Wikipedia](https://en.wikipedia.org/wiki/Shades_of_pink#Deep_pink)
3. [↑](#cite_ref-3) [erikbern/deep-pink · GitHub](https://github.com/erikbern/deep-pink)
4. [↑](#cite_ref-4) [Yurii Nesterov from Wikipedia](https://en.wikipedia.org/wiki/Yurii_Nesterov)
5. [↑](#cite_ref-5) [Deep learning for… chess](https://erikbern.com/2014/11/29/deep-learning-for-chess) by [Erik Bernhardsson](/Erik_Bernhardsson "Erik Bernhardsson"), November 29, 2014
6. [↑](#cite_ref-6) [ORF523: Nesterov’s Accelerated Gradient Descent](https://blogs.princeton.edu/imabandit/2013/04/01/acceleratedgradientdescent/) by [Sébastien Bubeck](/index.php?title=S%C3%A9bastien_Bubeck&action=edit&redlink=1 "Sébastien Bubeck (page does not exist)"), [I’m a bandit](https://blogs.princeton.edu/imabandit/), April 1, 2013
7. [↑](#cite_ref-7) [Nesterov’s Accelerated Gradient Descent for Smooth and Strongly Convex Optimization](https://blogs.princeton.edu/imabandit/2014/03/06/nesterovs-accelerated-gradient-descent-for-smooth-and-strongly-convex-optimization/) by [Sébastien Bubeck](/index.php?title=S%C3%A9bastien_Bubeck&action=edit&redlink=1 "Sébastien Bubeck (page does not exist)"), [I’m a bandit](https://blogs.princeton.edu/imabandit/), March 6, 2014

**[Up one level](/Engines "Engines")**