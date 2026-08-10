# Marcus Hutter

Source: https://www.chessprogramming.org/Marcus_Hutter

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Marcus Hutter**

[![](/images/b/bd/Marcushutter.jpg)](http://www.hutter1.net/index.htm)

Marcus Hutter [[1]](#cite_note-1)

**Marcus Hutter**,  
a German physicist and computer scientist, professor in the *Research School of Computer Science* at [Australian National University](/Australian_National_University "Australian National University"). Before, he researched at [IDSIA](https://en.wikipedia.org/wiki/IDSIA), [Lugano](https://en.wikipedia.org/wiki/Lugano), [Switzerland](https://en.wikipedia.org/wiki/Switzerland) in [Jürgen Schmidhuber's](/J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") group. Marcus Hutter defended his PhD and BSc in physics from the [Ludwig Maximilian University of Munich](https://en.wikipedia.org/wiki/Ludwig_Maximilian_University_of_Munich) and a [Habilitation](https://en.wikipedia.org/wiki/Habilitation), MSc, and BSc in computer science from [Technical University of Munich](/Technical_University_of_Munich "Technical University of Munich"). He is author of the AI-book *Universal Artificial Intelligence* [[2]](#cite_note-2) , a novel algorithmic information theory [[3]](#cite_note-3) perspective, also introducing the universal algorithmic agent called **AIXI**.

# AIXI

Quote from *The AIXI Model in One Line* [[4]](#cite_note-4)

```
It is actually possible to write down the AIXI model explicitly in one line, although one should not expect to be able to grasp the full meaning and power from this compact representation.
```

```
AIXI is an agent that interacts with an environment in cycles k=1,2,...,m. In cycle k, AIXI takes action ak (e.g. a limb movement) based on past perceptions o1 r1...ok-1 rk-1 as defined below. Thereafter, the environment provides a (regular) observation ok (e.g. a camera image) to AIXI and a real-valued reward rk. The reward can be very scarce, e.g. just +1 (-1) for winning (losing) a chess game, and 0 at all other times. Then the next cycle k+1 starts. Given the above, AIXI is defined by:
```

[![Aixi1line.gif](/images/8/8f/Aixi1line.gif)](http://www.hutter1.net/ai/uaibook.htm#oneline)

```
The expression shows that AIXI tries to maximize its total future reward rk+...+rm. If the environment is modeled by a deterministic program q, then the future perceptions ...okrk...omrm = U(q,a1..am) can be computed, where U is a universal (monotone Turing) machine executing q given a1..am. Since q is unknown, AIXI has to maximize its expected reward, i.e. average rk+...+rm over all possible perceptions created by all possible environments q. The simpler an environment, the higher is its a-priori contribution 2-l(q), where simplicity is measured by the length l of program q. Since noisy environments are just mixtures of deterministic environments, they are automatically included. The sums in the formula constitute the averaging process. Averaging and maximization have to be performed in chronological order, hence the interleaving of max and Σ (similarly to minimax for games).
```

# Selected Publications

[[5]](#cite_note-5) [[6]](#cite_note-6)

## 2005 ...

- Marcus Hutter (**2005**). *[Universal Artificial Intelligence](http://www.hutter1.net/ai/uaibook.htm)*. Sequential Decisions based on Algorithmic Probability, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- Marcus Hutter (**2007**). *[Universal Algorithmic Intelligence: A mathematical top->down approach](http://www.hutter1.net/ai/aixigentle.htm)*. Technical Report IDSIA-01-03 In Artificial General Intelligence, [pdf](http://www.hutter1.net/ai/aixigentle.pdf)
- [Joel Veness](/Joel_Veness "Joel Veness"), [Kee Siong Ng](/index.php?title=Kee_Siong_Ng&action=edit&redlink=1 "Kee Siong Ng (page does not exist)"), Marcus Hutter, [David Silver](/David_Silver "David Silver") (**2009**). *A Monte Carlo AIXI Approximation*, [pdf](http://jveness.info/publications/arXive2009%20-%20a%20monte%20carlo%20aixi%20approximation.pdf)

## 2010 ...

- [Joel Veness](/Joel_Veness "Joel Veness"), [Kee Siong Ng](/index.php?title=Kee_Siong_Ng&action=edit&redlink=1 "Kee Siong Ng (page does not exist)"), Marcus Hutter, [David Silver](/David_Silver "David Silver") (**2010**). *Reinforcement Learning via AIXI Approximation*. [AAAI-2010](/Conferences#AAAI-2010 "Conferences"), [pdf](http://jveness.info/publications/veness_rl_via_aixi_approx.pdf)
- [Tor Lattimore](/Tor_Lattimore "Tor Lattimore"), Marcus Hutter, [Vaibhav Gavane](http://www.informatik.uni-trier.de/~ley/pers/hd/g/Gavane:Vaibhav.html) (**2011**). *Universal Prediction of Selected Bits*. [Algorithmic Learning Theory](http://www.informatik.uni-trier.de/~ley/db/conf/alt/alt2011.html), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 6925, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Tor Lattimore](/Tor_Lattimore "Tor Lattimore"), Marcus Hutter (**2011**). *Asymptotically Optimal Agents*. [Algorithmic Learning Theory](http://www.informatik.uni-trier.de/~ley/db/conf/alt/alt2011.html), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 6925, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Tor Lattimore](/Tor_Lattimore "Tor Lattimore"), Marcus Hutter (**2011**). *Time Consistent Discounting*. [Algorithmic Learning Theory](http://www.informatik.uni-trier.de/~ley/db/conf/alt/alt2011.html), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 6925, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Tor Lattimore](/Tor_Lattimore "Tor Lattimore"), Marcus Hutter (**2011**). *No Free Lunch versus Occam's Razor in Supervised Learning*. [Solomonoff](https://en.wikipedia.org/wiki/Ray_Solomonoff) Memorial, [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), [Springer](https://en.wikipedia.org/wiki/Springer-Verlag), [arXiv:1111.3846](https://arxiv.org/abs/1111.3846) [[7]](#cite_note-7) [[8]](#cite_note-8)
- [Joel Veness](/Joel_Veness "Joel Veness"), [Kee Siong Ng](/index.php?title=Kee_Siong_Ng&action=edit&redlink=1 "Kee Siong Ng (page does not exist)"), Marcus Hutter, [William Uther](/William_Uther "William Uther") , [David Silver](/David_Silver "David Silver") (**2011**). *A Monte-Carlo AIXI Approximation*. [JAIR](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 40, [pdf](http://www.aaai.org/Papers/JAIR/Vol40/JAIR-4004.pdf)
- [Tor Lattimore](/Tor_Lattimore "Tor Lattimore"), Marcus Hutter (**2012**). *PAC Bounds for Discounted MDPs*. [Algorithmic Learning Theory](http://www.informatik.uni-trier.de/~ley/db/conf/alt/alt2012.htm), [arXiv:1202.3890](https://arxiv.org/abs/1202.3890) [[9]](#cite_note-9)
- [Peter Auer](/Peter_Auer "Peter Auer"), Marcus Hutter, [Laurent Orseau](/index.php?title=Laurent_Orseau&action=edit&redlink=1 "Laurent Orseau (page does not exist)") (**2013**). *[Reinforcement Learning](http://drops.dagstuhl.de/opus/volltexte/2013/4340/)*. [Dagstuhl Reports, Vol. 3, No. 8](http://dblp.uni-trier.de/db/journals/dagstuhl-reports/dagstuhl-reports3.html#AuerHO13), DOI: [10.4230/DagRep.3.8.1](http://drops.dagstuhl.de/opus/volltexte/2013/4340/), URN: [urn:nbn:de:0030-drops-43409](http://drops.dagstuhl.de/opus/volltexte/2013/4340/)
- [Tor Lattimore](/Tor_Lattimore "Tor Lattimore"), Marcus Hutter (**2014**). *[Bayesian Reinforcement Learning with Exploration](https://link.springer.com/chapter/10.1007/978-3-319-11662-4_13)*. [Algorithmic Learning Theory](http://dblp.uni-trier.de/db/conf/alt/alt2014.html), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 8776, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

## 2015 ...

- [Tom Everitt](/index.php?title=Tom_Everitt&action=edit&redlink=1 "Tom Everitt (page does not exist)"), Marcus Hutter (**2015**). *Analytical Results on the BFS vs. DFS Algorithm Selection Problem. Part I: Tree Search*. Australasian Conference on Artificial Intelligence, [pdf](https://pdfs.semanticscholar.org/1b4b/c878b2d068214e39b258ee250e5b8889e84c.pdf)
- [Tom Everitt](/index.php?title=Tom_Everitt&action=edit&redlink=1 "Tom Everitt (page does not exist)"), Marcus Hutter (**2015**). *Analytical Results on the BFS vs. DFS Algorithm Selection Problem: Part II: Graph Search*. Australasian Conference on Artificial Intelligence
- [Tom Everitt](/index.php?title=Tom_Everitt&action=edit&redlink=1 "Tom Everitt (page does not exist)"), [Tor Lattimore](/Tor_Lattimore "Tor Lattimore"), Marcus Hutter (**2016**). *Free Lunch for Optimisation under the Universal Distribution*. [arXiv:1608.04544](https://arxiv.org/abs/1608.04544)
- Marcus Hutter (**2017**). *Universal Learning Theory*. [Encyclopedia of Machine Learning and Data Mining 2017](https://link.springer.com/referencework/10.1007%2F978-1-4899-7687-1), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

# External Links

- [Marcus Hutter from Wikipedia](https://en.wikipedia.org/wiki/Marcus_Hutter)
- [HomePage of Marcus Hutter](http://www.hutter1.net/)
- [Hutter Prize](http://prize.hutter1.net/)

# References

1. [↑](#cite_ref-1) [HomePage of Marcus Hutter](http://www.hutter1.net/index.htm)
2. [↑](#cite_ref-2) Marcus Hutter (**2005**). *[Universal Artificial Intelligence](http://www.hutter1.net/ai/uaibook.htm)*. Sequential Decisions based on Algorithmic Probability, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
3. [↑](#cite_ref-3) [Algorithmic information theory - Scholarpedia](http://www.scholarpedia.org/article/Algorithmic_information_theory)
4. [↑](#cite_ref-4) [The AIXI Model in One Line](http://www.hutter1.net/ai/uaibook.htm#oneline)
5. [↑](#cite_ref-5) [Publications of Marcus Hutter](http://www.hutter1.net/official/publ.htm)
6. [↑](#cite_ref-6) [dblp: Marcus Hutter:](http://www.informatik.uni-trier.de/~ley/pers/hd/h/Hutter:Marcus.html)
7. [↑](#cite_ref-7) [No free lunch in search and optimization - Wikipedia](https://en.wikipedia.org/wiki/No_free_lunch_in_search_and_optimization)
8. [↑](#cite_ref-8) [Occam's razor from Wikipedia](https://en.wikipedia.org/wiki/Occam%27s_razor)
9. [↑](#cite_ref-9) [Markov decision process from Wikipedia](https://en.wikipedia.org/wiki/Markov_decision_process)

**[Up one level](/People "People")**