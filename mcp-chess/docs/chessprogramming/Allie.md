# Allie

Source: https://www.chessprogramming.org/Allie

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Allie**

**Allie**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Adam Treat](/Adam_Treat "Adam Treat"), written in [C++](/Cpp "Cpp") using [Qt](https://en.wikipedia.org/wiki/Qt_(software)), released under the terms of [GPL version 3](/Free_Software_Foundation#GPL "Free Software Foundation").
Allie is inspired by the seminal [AlphaZero](/AlphaZero "AlphaZero") paper [[1]](#cite_note-1) and the [Leela Chess Zero](/Leela_Chess_Zero "Leela Chess Zero") project - utilizing the [networks](/Neural_Networks "Neural Networks") produced by Leela Chess, and sharing the [CuDNN](https://en.wikipedia.org/wiki/CuDNN) backend written by [Ankan Banerjee](/Ankan_Banerjee "Ankan Banerjee") [[2]](#cite_note-2). Allie is a replacement of [Lc0's](/Leela_Chess_Zero#Lc0 "Leela Chess Zero") search with an own implementation of a [PUCT](/UCT#PUCT "UCT") [Monte-Carlo tree search](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") [[3]](#cite_note-3).

# AllieStein

AllieStein is the combination of Allie with Leela's third party **Stein** network by [Mark Jordan](/index.php?title=Mark_Jordan&action=edit&redlink=1 "Mark Jordan (page does not exist)") [[4]](#cite_note-4) [[5]](#cite_note-5), which is trained by [supervised learning](/Supervised_Learning "Supervised Learning") feeding in games from [CCRL](/CCRL "CCRL"),
supported by [SGDR](/Ilya_Loshchilov#SGDR "Ilya Loshchilov") ([Stochastic Gradient Descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) with Warm Restarts) [[6]](#cite_note-6)
and **GGT** (full-matrix adaptive [regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics))) [[7]](#cite_note-7),
using [batch renormalization](https://en.wikipedia.org/wiki/Batch_normalization) [[8]](#cite_note-8),
and adding [gradient noise](https://en.wikipedia.org/wiki/Gradient_noise) [[9]](#cite_note-9).

# Features

- [Fancy Magic Bitboards](/Magic_Bitboards#Fancy "Magic Bitboards") largely from [Ethereal](/Ethereal "Ethereal") by [Andrew Grant](/Andrew_Grant "Andrew Grant") [[10]](#cite_note-10) [[11]](#cite_note-11)
- [BMI2 - PEXT Bitboards](/BMI2#PEXTBitboards "BMI2")
- [Lc0 NN Backend](/Leela_Chess_Zero#Lc0 "Leela Chess Zero") by [Ankan Banerjee](/Ankan_Banerjee "Ankan Banerjee") [[12]](#cite_note-12)
- [Monte-Carlo Tree Search](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
- [PUCT](/UCT#PUCT "UCT")
- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases") via [Fathom](/Syzygy_Bases#Fathom "Syzygy Bases") by [Basil Falcinelli](/Basil_Falcinelli "Basil Falcinelli")
- [Chess960](/Chess960 "Chess960")

# Lc0 Intersections

[![Lc0diagram.png](/images/2/20/Lc0diagram.png)](/File:Lc0diagram.png)

[![Alliestein.png](/images/4/47/Alliestein.png)](/File:Alliestein.png)

What Alliestein has in Common with Lc0 [[13]](#cite_note-13)

# See also

- [AlphaZero](/AlphaZero "AlphaZero")
- [Deep Learning](/Deep_Learning "Deep Learning")
- [Deus X](/Deus_X "Deus X")
- [Leela Chess Zero](/Leela_Chess_Zero "Leela Chess Zero")

# Forum Posts

## 2019

- [New Engine: Allie (NN)](http://www.talkchess.com/forum3/viewtopic.php?t=69972) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), February 20, 2019
- [Allie & Stein](http://www.talkchess.com/forum3/viewtopic.php?t=70116) by Sven Steppenwolf, [CCC](/CCC "CCC"), March 06, 2019

:   [Re: Allie & Stein](http://www.talkchess.com/forum3/viewtopic.php?t=70116&start=8) by [Alexander Lyashuk](/Alexander_Lyashuk "Alexander Lyashuk"), [CCC](/CCC "CCC"), March 07, 2019
:   [Re: Allie & Stein](http://www.talkchess.com/forum3/viewtopic.php?t=70116&start=10) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), March 07, 2019

- [Allie 0.2](http://www.talkchess.com/forum3/viewtopic.php?t=70282) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), March 22, 2019
- [New release of Allie v0.3](http://www.talkchess.com/forum3/viewtopic.php?t=70662) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), May 04, 2019
- [New release of Allie v0.4](http://www.talkchess.com/forum3/viewtopic.php?t=70874) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), May 31, 2019
- [My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822) by [Alexander Lyashuk](/Alexander_Lyashuk "Alexander Lyashuk"), [CCC](/CCC "CCC"), September 14, 2019 » [TCEC](/TCEC "TCEC")

:   [Re: My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822&start=48) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), September 19, 2019

- [Allie v0.5 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72085) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), October 14, 2019 » [TCEC Season 16](/TCEC_Season_16 "TCEC Season 16")

## 2020 ...

- [New version of Allie v0.6](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73712) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), April 20, 2020
- [Release v0.7 of Allie](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74449) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), July 11, 2020
- [Why I stood up for Allie is why I stand up for FF2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76686) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe"), [CCC](/CCC "CCC"), February 23, 2021 » [Fat Fritz](/Fat_Fritz "Fat Fritz")

# External Links

## Chess Engine

- [GitHub - manyoso/allie: Allie: A UCI compliant chess engine](https://github.com/manyoso/allie)
- [Allie+Stein, the new neural network based engine entering TCEC S15 | Chessdom](http://www.chessdom.com/alliestein-the-new-neural-network-entering-tcec-s15/), March 02, 2019

## Misc

- [Allie from Wikipedia](https://en.wikipedia.org/wiki/Allie)

# References

1. [↑](#cite_ref-1) [David Silver](/David_Silver "David Silver"), [Thomas Hubert](/Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](/Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](/Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](/Matthew_Lai "Matthew Lai"), [Arthur Guez](/Arthur_Guez "Arthur Guez"), [Marc Lanctot](/Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](/Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](/Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](/Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](/Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](/Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](/Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
2. [↑](#cite_ref-2) [Re: My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822&start=48) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), September 19, 2019
3. [↑](#cite_ref-3) [allie/node.h at master · manyoso/allie · GitHub](https://github.com/manyoso/allie/blob/master/lib/node.h)
4. [↑](#cite_ref-4) [Third Party Nets · LeelaChessZero/lc0 Wiki · GitHub](https://github.com/LeelaChessZero/lc0/wiki/Third-Party-Nets)
5. [↑](#cite_ref-5) [Jjosh is creating Leelenstein | Patreon](https://www.patreon.com/jjosh)
6. [↑](#cite_ref-6) [Ilya Loshchilov](/Ilya_Loshchilov "Ilya Loshchilov"), [Frank Hutter](/Frank_Hutter "Frank Hutter") (**2016**). *SGDR: Stochastic Gradient Descent with Warm Restarts*. [arXiv:1608.03983](https://arxiv.org/abs/1608.03983)
7. [↑](#cite_ref-7) [Naman Agarwal](/index.php?title=Naman_Agarwal&action=edit&redlink=1 "Naman Agarwal (page does not exist)"), [Brian Bullins](/index.php?title=Brian_Bullins&action=edit&redlink=1 "Brian Bullins (page does not exist)"), [Xinyi Chen](/index.php?title=Xinyi_Chen&action=edit&redlink=1 "Xinyi Chen (page does not exist)"), [Elad Hazan](/index.php?title=Elad_Hazan&action=edit&redlink=1 "Elad Hazan (page does not exist)"), [Karan Singh](/index.php?title=Karan_Singh&action=edit&redlink=1 "Karan Singh (page does not exist)"), [Cyril Zhang](/index.php?title=Cyril_Zhang&action=edit&redlink=1 "Cyril Zhang (page does not exist)"), [Yi Zhang](/index.php?title=Yi_Zhang&action=edit&redlink=1 "Yi Zhang (page does not exist)") (**2018**). *The Case for Full-Matrix Adaptive Regularization*. [arXiv:1806.02958](https://arxiv.org/abs/1806.02958)
8. [↑](#cite_ref-8) [Sergey Ioffe](/Mathematician#SIoffe "Mathematician") (**2017**). *Batch Renormalization: Towards Reducing Minibatch Dependence in Batch-Normalized Models*. [arXiv:1702.03275](https://arxiv.org/abs/1702.03275)
9. [↑](#cite_ref-9) [Arvind Neelakantan](/index.php?title=Arvind_Neelakantan&action=edit&redlink=1 "Arvind Neelakantan (page does not exist)"), [Luke Vilnis](/index.php?title=Luke_Vilnis&action=edit&redlink=1 "Luke Vilnis (page does not exist)"), [Quoc V. Le](/index.php?title=Quoc_V._Le&action=edit&redlink=1 "Quoc V. Le (page does not exist)"), [Ilya Sutskever](/Ilya_Sutskever "Ilya Sutskever"), [Lukasz Kaiser](/index.php?title=Lukasz_Kaiser&action=edit&redlink=1 "Lukasz Kaiser (page does not exist)"), [Karol Kurach](/index.php?title=Karol_Kurach&action=edit&redlink=1 "Karol Kurach (page does not exist)"), [James Martens](/index.php?title=James_Martens&action=edit&redlink=1 "James Martens (page does not exist)") (**2015**). *Adding Gradient Noise Improves Learning for Very Deep Networks*. [arXiv:1511.06807](https://arxiv.org/abs/1511.06807)
10. [↑](#cite_ref-10) [allie/movegen.cpp at master · manyoso/allie · GitHub](https://github.com/manyoso/allie/blob/master/lib/movegen.cpp)
11. [↑](#cite_ref-11) [Ethereal/attacks.h at master · AndyGrant/Ethereal · GitHub](https://github.com/AndyGrant/Ethereal/blob/master/src/attacks.h)
12. [↑](#cite_ref-12) [Re: My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822&start=48) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), September 19, 2019
13. [↑](#cite_ref-13) [My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822) by [Alexander Lyashuk](/Alexander_Lyashuk "Alexander Lyashuk"), [CCC](/CCC "CCC"), September 14, 2019 » [TCEC](/TCEC "TCEC")

**[Up one level](/Engines "Engines")**