# Vincent David

Source: https://www.chessprogramming.org/Vincent_David

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Vincent David**

**Vincent David**,  
a French computer scientist and researcher. He holds a Ph.D. in 1993 from [École nationale supérieure de l'aéronautique et de l'espace](https://en.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_de_l%27a%C3%A9ronautique_et_de_l%27espace) (National School of Aeronautics and Space), [Toulouse](https://en.wikipedia.org/wiki/Toulouse) [[1]](#cite_note-1), with the title *Algorithmique parallèle sur les arbres de décision et raisonnement en temps contraint. Etude et application au Minimax = Parallel Minimax algorithm for heuristic tree searching and real-time reasoning. Study and application to the Minimax*
[[2]](#cite_note-2). The thesis was part of the [Saturn](https://en.wikipedia.org/wiki/Saturn) studies conducted at [Onera](https://en.wikipedia.org/wiki/Office_National_d%27%C3%89tudes_et_de_Recherches_A%C3%A9rospatiales), and describes a loosely synchronized distributed [alpha-beta](/Alpha-Beta "Alpha-Beta") search algorithm coined **αβ\***, utilizing a [shared transposition table](/Shared_Hash_Table "Shared Hash Table"), but according to [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"), who advanced **αβ\*** to [ABDADA](/ABDADA "ABDADA"), with an ineffective controller and not considering the eldest son. Further, Vincent David introduced [entropic](https://en.wikipedia.org/wiki/Entropy_%28information_theory%29) [extensions](/Extensions "Extensions") near the horizon if the [position](/Chess_Position "Chess Position") was not stable enough. The idea was implemented by Jean-Christophe Weill and [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot") in [Joker](/Joker "Joker"), but despite some impressive play, later abandoned [[3]](#cite_note-3).

# Selected Publications

[[4]](#cite_note-4)

- Vincent David (**1993**). *Algorithmique parallèle sur les arbres de décision et raisonnement en temps contraint. Etude et application au Minimax*. Parallel algorithm for heuristic tree searching and real-time reasoning. Study and application of Minimax, Ph.D. thesis, [École nationale supérieure de l'aéronautique et de l'espace](https://en.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_de_l%27a%C3%A9ronautique_et_de_l%27espace), [Toulouse](https://en.wikipedia.org/wiki/Toulouse)

```
This thesis presents a parallel processing model for the implementation of reasoning algorithms as part of a smart real-time system, and is part of the SATURNE study conducted at CERT-ONERA. This project is based on the assumption that processing tasks have the ability to adapt to time periods. To satisfy this model, the proposed solutions are the reduction of the search space and the acceleration of the treatments thanks to the parallelism. These changes must occur during the execution of the process, the management of parallelism becomes dynamic. Moreover, decision trees represent a fundamental method for solving many artificial intelligence problems, such as the theory of one-player games, optimization problems, two-player game theory, graphs and / or and many other NP-complete problems. Also, from the example of the minimax algorithm on real game trees, an implementation is performed on Modulor, a distributed architecture machine based on transputers developed at CERT-ONERA. The method of parallelization is based on a suppression of the control between the research processes, in favor of a speculative parallelism and the complete sharing of the information realized thanks to a physically distributed but virtually shared memory. The contribution of our approach for distributed and fault-tolerant real-time systems is evaluated thanks to the experimental results obtained.
```

# See also

- [ABDADA](/ABDADA "ABDADA")
- [Lazy SMP](/Lazy_SMP "Lazy SMP")

# External Links

- [Vincent David, Ecole Nationale Supérieure De L'Aéronautique Et De L'Espace (Supaero)](http://copainsdavant.linternaute.com/membre/15167869/1937553667/vincent_david/)

# References

1. [↑](#cite_ref-1) [Vincent David, Ecole Nationale Supérieure De L'Aéronautique Et De L'Espace (Supaero)](http://copainsdavant.linternaute.com/membre/15167869/1937553667/vincent_david/)
2. [↑](#cite_ref-2) Vincent David (**1993**). *Algorithmique parallèle sur les arbres de décision et raisonnement en temps contraint. Etude et application au Minimax*. Parallel algorithm for heuristic tree searching and real-time reasoning. Study and application of Minimax, Ph.D. thesis, [École nationale supérieure de l'aéronautique et de l'espace](https://en.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_de_l%27a%C3%A9ronautique_et_de_l%27espace), [Toulouse](https://en.wikipedia.org/wiki/Toulouse)
3. [↑](#cite_ref-3) [A Short Story of JCW's Computer Chess Program](http://recherche.enac.fr/~weill/chess.html) by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill")
4. [↑](#cite_ref-4) [David, Vincent informaticien](http://orlabs.oclc.org/identities/viaf-198681136/)

**[Up one level](/People "People")**