# ABDADA

Source: https://www.chessprogramming.org/ABDADA

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Parallel Search](/Parallel_Search "Parallel Search") \* ABDADA**

[![](/images/0/0f/Hannah-hoche_da-dandy-1919.jpg)](http://littlemissartypants.tumblr.com/post/12081930289/hannah-h%C3%B6ch-da-dandy-1919-the-photomontage-da)

[Hannah Höch](/Category:Hannah_H%C3%B6ch "Category:Hannah Höch") - Da Dandy [[1]](#cite_note-1)

**ABDADA**, (Alpha-Bêta Distribué avec Droit d'Aînesse = Distributed Alpha-Beta Search with Eldest Son Right)  
a loosely synchronized, [distributed search algorithm](/Parallel_Search "Parallel Search") developed by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"). The ABDADA search algorithm is based on [Young Brothers Wait Concept](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept") (YBWC) ([Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann") et al. 1986, 1993) [[2]](#cite_note-2) [[3]](#cite_note-3) and αβ\* ([Vincent David](/Vincent_David "Vincent David") 1993) [[4]](#cite_note-4) . From YBWC it retains the basic concept to allow parallel search only if the eldest son has been fully evaluated. From αβ\* as well as [Steve Otto](/Steve_Otto "Steve Otto") and [Ed Felten's](/Ed_Felten "Ed Felten") algorithm (1988) [[5]](#cite_note-5) which both rely on a [Shared Hash Table](/Shared_Hash_Table "Shared Hash Table") and all processors start the search simultaneously at the [root](/Root "Root"), ABDADA retains the simple [recursive](/Recursion "Recursion") control structure similar to a serial algorithm. With the help of additional [transposition table](/Transposition_Table "Transposition Table") information, i.e. the number of processors searching this node, it is possible to control [speculative parallelism](https://en.wikipedia.org/wiki/Speculative_multithreading).

# Recursion

While [YBWC](/YBWC "YBWC") is difficult to implement recursively, ABDADA is not. In YBWC, when a processor receives an evaluation answer from one of its slaves, it must be able to produce a jump in the search depth if this evaluation produces a pruning of the current master node. So the values of [alpha](/Alpha "Alpha") and [beta](/Beta "Beta") must at least be kept in [arrays](/Array "Array") indexed by [ply](/Ply "Ply") distance from root, and special arrangements must be made to counteract the disruption that might occur from confusing depths. Therefor YBWC needs a hugely modified [iterative search](/Iterative_Search "Iterative Search") algorithm. In his paper [[6]](#cite_note-6) , Weill states that using ABDADA within a recursive [NegaScout](/NegaScout "NegaScout") framework was 30% faster than a non-recursive search, which was observed independently by [Mark Brockington](/Mark_Brockington "Mark Brockington") in 1994 [[7]](#cite_note-7) . It can be explained by the fact that within high-level languages and their compilers for certain target platforms, the use of procedure [stacks](/Stack "Stack") is more optimized than the use of indexed arrays, also observed by [Niklaus Wirth](https://en.wikipedia.org/wiki/Niklaus_Wirth) concerning the [Quicksort](https://en.wikipedia.org/wiki/Quicksort) algorithm [[8]](#cite_note-8) .

# Algorithm

The ABDADA algorithm is described in five steps:

1. A TT-Entry has a field *entry.nproc* containing the number of processors currently searching the associated node
2. All processors start the search simultaneously at the root of the [search tree](/Search_Tree "Search Tree")
3. When a processor enters a node, it increments *entry.nproc*
4. When a processor leaves a node, it decrements *entry.nproc*
5. The analysis of a position is done in three phases:
   1. The eldest son is analyzed, regardless of the activities of other processors
   2. Next, all other sons not currently being analyzed by other processors are analyzed
   3. In the final phase, any remaining sons not yet analyzed are searched, i.e. the corresponding entry in the TT indicates this node and its siblings have not been searched to the required depth

# Pseudo Code

The C-like pseudo code below (adopted from the Pascal like pseudo code from Weill's paper), demonstrates the mentioned three phases controlled by an iteration counter. The boolean parameter *exclusiveP* indicates whether the node should be searched exclusively and is passed to the TT-probing code via the procedure *retrieveAsk*. A new value outside the usual [value range](/Score#ValueRange "Score") need to be defined (ON\_EVALUATION), and *retrieveAsk* returns this score if probed in exclusive move, and other processors evaluating this node.

```
int abdada(const CNode &position, int α, int β, int depth, bool exclusiveP) {
   if (depth == 0) return evaluate( position );
   int best = -oo;

   retrieveAsk(position, α, β, depth, exclusiveP);
   /* generate moves while waiting for the answer ... */
   GenerateMoves(position);
   retrieveAnswer(&α, &β, &best);
   /* The current move is not searched if causing a cutoff or */
   /* in exclusive mode and another processor is currently searching it */
   if ( α >= β || best == ON_EVALUATION )
      return best; /* entry.nproc not incremented */

   bool alldone = false;
   for ( int iteration = 0; iteration < 2 && α < β && !alldone; iteration++) {
      alldone = true;
      Move m = firstMove( position );
      while ( (m != 0) && (α < β) ) {
         exclusive = (iteration == 0) && !isFirstMove( m );
         /* On the first iteration, only one processor should search young sons exclusively */
         value = -abdada( position * m, -β, -max(α, best), depth-1, exclusive );
         if ( value == -ON_EVALUATION) {
            alldone = false;
         } else if ( value > best ) {
            best = value;
            if ( best > β ) goto endsearch;
         }
         m = nextMove( position );
      }
   }
endsearch:
   storeHash( position, α, β, depth, best );
   return best;
}
```

# Implementations

## Frenchess

ABDADA was implemented in [Frenchess](/Frenchess "Frenchess") on a [Cray T3D](/Cray_T3D "Cray T3D") with 128 [DEC Alpha 21064](/DEC_Alpha "DEC Alpha") processors. Frenchess participated at the [WCCC 1995](/WCCC_1995 "WCCC 1995") finishing fourth, tied with [Deep Blue Prototype](/Deep_Blue "Deep Blue") [[9]](#cite_note-9), as well inside an [Othello](/Othello "Othello") program called *BUGS* [[10]](#cite_note-10) .

## Smash

The [GPL](/Free_Software_Foundation#GPL "Free Software Foundation") [open source chess engine](/Category:Open_Source "Category:Open Source") [Smash](/Smash "Smash") by [Maurizio Sambati](/index.php?title=Maurizio_Sambati&action=edit&redlink=1 "Maurizio Sambati (page does not exist)") demonstrates an ABDADA implementation in [C++](/Cpp "Cpp") [[11]](#cite_note-11) [[12]](#cite_note-12) .

# See also

- [Dynamic Tree Splitting](/Dynamic_Tree_Splitting "Dynamic Tree Splitting")
- [Jamboree](/Jamboree "Jamboree")
- [Lazy SMP](/Lazy_SMP "Lazy SMP")
- [Parallel Alpha-Beta](/Cilk#ParallelAlphaBeta "Cilk") in [Cilk](/Cilk "Cilk")
- [Shared Hash Table](/Shared_Hash_Table "Shared Hash Table")
- [Young Brothers Wait Concept](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept")

# Publications

- [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") (**1995**). *Programmes d'Échecs de Championnat: Architecture Logicielle Synthèse de Fonctions d'Évaluations, Parallélisme de Recherche*. Ph.D. Thesis. Université Paris 8, Saint-Denis, [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/phdJCW.ps.gz) (French)
- [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"), [Jean-Luc Seret](/Jean-Luc_Seret "Jean-Luc Seret"), [Michel Gondran](/Michel_Gondran "Michel Gondran") (**1995**). *[Frenchess: A Cray T3D at the 8th World Computer Chess Championship](https://www.researchgate.net/publication/228386252_Frenchess_A_Cray_T3D_at_the_8th_World_Computer_Chess_Championship)*. First European Cray-T3D Workshop, [Citeseex](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.78.967)
- [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") (**1996**). *[The ABDADA Distributed Minimax Search Agorithm](http://portal.acm.org/citation.cfm?id=228345)*. Proceedings of the 1996 ACM Computer Science Conference, pp. 131-138. ACM, New York, N.Y, reprinted [ICCA Journal, Vol. 19, No. 1](/ICGA_Journal#19_1 "ICGA Journal"), [zipped postscript](http://www.recherche.enac.fr/%7Eweill/publications/acm.ps.gz)

# Forum Posts

## 1997 ...

- [Parallel searching](https://groups.google.com/d/msg/rec.games.chess.computer/Wl7A-v-gWYQ/QLuvAp0l4_gJ) by [Andrew Tridgell](/Andrew_Tridgell "Andrew Tridgell"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 22, 1997

:   [Re:Parallel searching](https://groups.google.com/d/msg/rec.games.chess.computer/Wl7A-v-gWYQ/w-Ky1kkvfeYJ) by [Mark Brockington](/Mark_Brockington "Mark Brockington"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 22, 1997

## 2000 ...

- [tip for "simulating" an MP computer & performance of ABDADA](https://www.stmintz.com/ccc/index.php?id=112849) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), May 28, 2000
- [A couple of Questions re ABDADA](https://www.stmintz.com/ccc/index.php?id=112884) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), May 29, 2000
- [Parallel algorithms in chess programming](https://www.stmintz.com/ccc/index.php?id=163888) by [Dieter Bürßner](/Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](/CCC "CCC"), April 16, 2001

## 2010 ...

- [Parallelization questions, ABDADA or DTS?](http://www.talkchess.com/forum/viewtopic.php?t=42986) by Benjamin Rosseaux, [CCC](/CCC "CCC"), March 23, 2012
- [ABDADA speedup results](http://www.talkchess.com/forum/viewtopic.php?t=47887) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), May 01, 2013
- [IID and move sorting](http://www.talkchess.com/forum/viewtopic.php?t=47951) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), May 09, 2013 » [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Possible improvement to ABDADA -- checking for cutoffs](http://www.talkchess.com/forum/viewtopic.php?t=56936) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), July 10, 2015
- [Actual speedups from YBWC and ABDADA on 8+ core machines?](http://www.talkchess.com/forum/viewtopic.php?t=56937) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), July 10, 2015
- [Good parallel speedup with ABDADA and cutoff checks](http://www.talkchess.com/forum/viewtopic.php?t=63023) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), February 03, 2017
- [Approximate ABDADA](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=43) by [Peter Österlund](/Peter_%C3%96sterlund "Peter Österlund"), [CCC](/CCC "CCC"), August 23, 2017 » [Lazy SMP - Lazy Cluster](/Lazy_SMP#LazyCluster "Lazy SMP")
- ["How To" guide to parallel-izing an engine](http://www.talkchess.com/forum/viewtopic.php?t=65011) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), August 27, 2017
- ["Simplified ABDADA" updated](http://www.talkchess.com/forum/viewtopic.php?t=65025) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), August 29, 2017
- [ABDADA+ suggestion](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71139) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), June 29, 2019

# External Links

## Algorithm

- [Simplified ABDADA](http://www.tckerrigan.com/Chess/Parallel_Search/Simplified_ABDADA/) from [Parallel Search](http://www.tckerrigan.com/Chess/Parallel_Search/) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan") [[13]](#cite_note-13)

:   [Cutoff Checks](http://www.tckerrigan.com/Chess/Parallel_Search/Cutoff_Checks/) from [Parallel Search](http://www.tckerrigan.com/Chess/Parallel_Search/) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan")

## Misc

- [AB from Wikipedia](https://en.wikipedia.org/wiki/AB)
- [ab - Wiktionary](https://en.wiktionary.org/wiki/ab)
- [ab initio - Wiktionary](https://en.wiktionary.org/wiki/ab_initio)
- [بد - Wiktionary](https://en.wiktionary.org/wiki/%D8%A8%D8%AF)
- [Dada from Wikipedia](https://en.wikipedia.org/wiki/Dada)
- [Jean-Luc Ponty](/Category:Jean-Luc_Ponty "Category:Jean-Luc Ponty") - Final Truth (Part 2), [Montreal Jazz Festival](https://en.wikipedia.org/wiki/Montreal_International_Jazz_Festival), 1982, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   feat. [Allan Zavod](http://wiki.killuglyradio.com/wiki/Allan_Zavod), [Jamie Glaser](https://en.wikipedia.org/wiki/Jamie_Glaser), [Rayford Griffin](http://www.drumsoloartist.com/Site/Drummers3/Rayford_Griffin.html) and [Keith Jones](http://deanguitars.com/keith_jones.php)

# References

1. [↑](#cite_ref-1) [Hannah Höch](/Category:Hannah_H%C3%B6ch "Category:Hannah Höch") - Da Dandy, 1919, [Hannah Höch | Da-Dandy (1919)](http://littlemissartypants.tumblr.com/post/12081930289/hannah-h%C3%B6ch-da-dandy-1919-the-photomontage-da)
2. [↑](#cite_ref-2) [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](/Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](/Oliver_Vornberger "Oliver Vornberger") (**1986**). *A Local Area Network Used as a Parallel Architecture*. Technical Report 31, [Paderborn University](/Paderborn_University "Paderborn University")
3. [↑](#cite_ref-3) [Rainer Feldmann](/Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Ph.D. Thesis, [pdf](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
4. [↑](#cite_ref-4) [Vincent David](/Vincent_David "Vincent David") (**1993**). *[Algorithmique parallèle sur les arbres de décision et raisonnement en temps contraint. Etude et application au Minimax](http://cat.inist.fr/?aModele=afficheN&cpsidt=161774)* = Parallel algorithm for heuristic tree searching and real-time reasoning. Study and application to the Minimax, Ph.D. Thesis, [École nationale supérieure de l'aéronautique et de l'espace](https://en.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_de_l%27a%C3%A9ronautique_et_de_l%27espace), [Toulouse](https://en.wikipedia.org/wiki/Toulouse), [France](https://en.wikipedia.org/wiki/France)
5. [↑](#cite_ref-5) [Ed Felten](/Ed_Felten "Ed Felten"), [Steve Otto](/Steve_Otto "Steve Otto") (**1988**). *[Chess on a Hypercube](http://portal.acm.org/citation.cfm?id=63088)*. The Third Conference on Hypercube Concurrent Computers and Applications, Vol. II-Applications (ed. [G. Fox](http://portal.acm.org/author_page.cfm?id=81100501616&coll=GUIDE&dl=GUIDE&trk=0&CFID=90098691&CFTOKEN=72738297)), pp. 1329-1341
6. [↑](#cite_ref-6) [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") (**1996**). *[The ABDADA Distributed Minimax Search Agorithm](http://portal.acm.org/citation.cfm?id=228345)*. Proceedings of the 1996 ACM Computer Science Conference, pp. 131-138. ACM, New York, N.Y, reprinted [ICCA Journal, Vol. 19, No. 1](/ICGA_Journal#19_1 "ICGA Journal"), [zipped postscript](http://www.recherche.enac.fr/%7Eweill/publications/acm.ps.gz)
7. [↑](#cite_ref-7) [Mark Brockington](/Mark_Brockington "Mark Brockington") (**1994**). *An Implementation of the Young Brothers Wait Concept*. Internal report, [University of Alberta](/University_of_Alberta "University of Alberta")
8. [↑](#cite_ref-8) [Niklaus Wirth](https://en.wikipedia.org/wiki/Niklaus_Wirth) (**1976**). *[Algorithms + Data Structures = Programs](https://en.wikipedia.org/wiki/Algorithms_%2B_Data_Structures_%3D_Programs)*. pp 100
9. [↑](#cite_ref-9) [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"), [Jean-Luc Seret](/Jean-Luc_Seret "Jean-Luc Seret"), [Michel Gondran](/Michel_Gondran "Michel Gondran") (**1995**). *[Frenchess: A Cray T3D at the 8th World Computer Chess Championship](https://www.researchgate.net/publication/228386252_Frenchess_A_Cray_T3D_at_the_8th_World_Computer_Chess_Championship)*. [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/papier.ps.gz)
10. [↑](#cite_ref-10) [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") (**1996**). *[The ABDADA Distributed Minimax Search Agorithm](http://portal.acm.org/citation.cfm?id=228345)*. Proceedings of the 1996 ACM Computer Science Conference, pp. 131-138. ACM, New York, N.Y, reprinted [ICCA Journal, Vol. 19, No. 1](/ICGA_Journal#19_1 "ICGA Journal"), [zipped postscript](http://www.recherche.enac.fr/%7Eweill/publications/acm.ps.gz)
11. [↑](#cite_ref-11) [Re: interested in making single procesor program multi](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=165470&t=18611) by [Alessandro Scotti](/Alessandro_Scotti "Alessandro Scotti"), [CCC](/CCC "CCC"), December 29, 2007
12. [↑](#cite_ref-12) [smash.tar.bz2 search.cpp](http://www.cli.di.unipi.it/~sambati/prog/smash.tar.bz2)
13. [↑](#cite_ref-13) ["How To" guide to parallel-izing an engine](http://www.talkchess.com/forum/viewtopic.php?t=65011) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), August 27, 2017

**[Up one level](/Parallel_Search "Parallel Search")**