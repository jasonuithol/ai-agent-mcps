# Multi-Cut

Source: https://www.chessprogramming.org/Multi-Cut

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Pruning](/Pruning "Pruning") \* Multi-Cut**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Master_Pine_Pruner_LACMA_M.2006.136.205a-b.jpg/330px-Master_Pine_Pruner_LACMA_M.2006.136.205a-b.jpg)](/File:Master_Pine_Pruner_LACMA_M.2006.136.205a-b.jpg)

[Katsushika Hokusai](/Category:Katsushika_Hokusai "Category:Katsushika Hokusai") - Master Pine Pruner [[1]](#cite_note-1)

**Multi-Cut**,  
a speculative pruning mechanism for chessplaying programs created by [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") [[2]](#cite_note-2) [[3]](#cite_note-3). The basic idea is to perform a reduced search of the first C (i.e. 3) up to M (i.e. 6) moves, to prove an expected [Cut-node](/Node_Types#CUT "Node Types") is not singular, that is multiple (C) moves [fail high](/Fail-High "Fail-High"), and to prune the whole subtree in that case by returning the hard [beta](/Beta "Beta") [bound](/Bound "Bound"). [Mark Winands'](/Mark_Winands "Mark Winands") [enhanced forward pruning](/Enhanced_Forward_Pruning "Enhanced Forward Pruning") applies Multi-Cut even at expected [All-nodes](/Node_Types#ALL "Node Types"), with slight modifications on a [PVS](/Principal_Variation_Search "Principal Variation Search") framework [[4]](#cite_note-4) . In his 2011 B.Sc. thesis *Investigation of Multi-Cut Pruning in Game-Tree Search* [[5]](#cite_note-5), [Hrafn Eiríksson](/Hrafn_Eir%C3%ADksson "Hrafn Eiríksson") proposed to apply Multi-cut if a [transposition table](/Transposition_Table "Transposition Table") probe indicates a [beta-cutoff](/Beta-Cutoff "Beta-Cutoff") without sufficient [draft](/Depth "Depth") stored.

# Abstract

from the [Workshop Chess and Mathematics](/Workshop_Chess_and_Mathematics "Workshop Chess and Mathematics"), 2008 [[6]](#cite_note-6) [[7]](#cite_note-7) :

```
The alpha-beta algorithm is the most popular method for searching game-trees in adversary board games such as chess. It is much more efficient than a plain brute-force minimax search because it allows a large portion of the game-tree to be pruned, while still backing up the correct game-tree value. However, the number of nodes visited by the algorithm still increases exponentially with increasing search depth. This obviously limits the scope of the search, since game-playing programs must meet external time constraints: often having only a few minutes to make a decision.
```

```
To somewhat alleviate this problem so-called speculative-pruning methods are used to cut off less interesting lines of play prematurely, while allowing interesting lines to be explored more deeply.
```

```
Here we discuss one such speculative-pruning method called multi-cut, which makes pruning decisions based not only on the risk of pruning off relevant lines of play, but also on the likelihood of such an erroneous pruning decision affecting the move decision at the root of the search tree. The method has been successfully employed by several of the world’s strongest commercial chess program for a number of years.
```

# Modern Usage

In recent times, Multi Cut has been successfully integrated into [Restricted Singular Extensions](/Singular_Extensions#Restricted_SE "Singular Extensions"), in the form of Multi Cut Pruning. If the singular search fails high, and the bounds at which they were searched at is greater than or equal to beta, we can predict that multiple moves fail high in the current node, and return a score early.

# Pseudo Code

Multi-Cut inside a [null window](/Null_Window "Null Window")- or [zero window search](/Principal_Variation_Search#ZWS "Principal Variation Search") of a [fail-hard](/Fail-Hard "Fail-Hard") [PVS](/Principal_Variation_Search "Principal Variation Search") framework, applied at expected [Cut-nodes](/Node_Types#CUT "Node Types"):

```
// M is the number of moves to look at when checking for mc-prune.
// C is the number of cutoffs to cause an mc-prune, C < M.
// R is the search depth reduction for mc-prune searches.

int zwSearch( int beta, int depth, bool cut) {
   if ( depth <= 0 ) return quiesce( beta-1, beta );

   if ( depth >= R && cut ) {
      int c = 0;
      for ( first M moves )
         score = -zwSearch( 1-beta, depth-1-R, !cut);
         if ( score >= beta ) {
            if ( ++c == C )
               return beta; // mc-prune
         }
      }
   }
   for ( all moves ) {
      score = -zwSearch( 1-beta, depth-1, !cut);
      if ( score  >= beta )
         return beta;
   }
   return beta - 1;
}
```

# See also

- [Enhanced Forward Pruning](/Enhanced_Forward_Pruning "Enhanced Forward Pruning")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [ProbCut](/ProbCut "ProbCut")

:   [Multi–ProbCut](/ProbCut#MPC "ProbCut")

- [Singular Extensions](/Singular_Extensions "Singular Extensions")
- [Uncertainty Cut-Offs](/Uncertainty_Cut-Offs "Uncertainty Cut-Offs")

# Publications

- [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland") (**1998**). *[Multi-cut Pruning in Alpha-Beta Search](http://link.springer.com/chapter/10.1007/3-540-48957-6_2)*. [CG 1998](/CG_1998 "CG 1998"), see also [MC2001](/index.php?title=Yngvi_Bj%C3%B6rnsso&action=edit&redlink=1 "Yngvi Björnsso (page does not exist)") for an expanded version.
- [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland") (**2000**). *Risk Management in Game-tree Pruning*. Information Sciences, Vol. 122, No. 1, [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM00.pdf)
- [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland") (**2001**). *Multi-cut Alpha-Beta Pruning in Game Tree Search.* Theoretical Computer Science, Vol. 252, [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01a.pdf)
- [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") (**2002**). *[Selective Depth-First Game-Tree Search](http://dl.acm.org/citation.cfm?id=935848)*. Ph.D. thesis, [University of Alberta](/University_of_Alberta "University of Alberta")
- [Mark Winands](/Mark_Winands "Mark Winands"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](/Erik_van_der_Werf "Erik van der Werf") (**2003**). *Enhanced forward pruning.* [pdf](http://www.personeel.unimaas.nl/m-winands/documents/Enhanced%20forward%20pruning.pdf)
- [Hrafn Eiríksson](/Hrafn_Eir%C3%ADksson "Hrafn Eiríksson") (**2011**). *Investigation of Multi-Cut Pruning in Game-Tree Search*. B.Sc. Thesis, [Reykjavík University](https://en.wikipedia.org/wiki/Reykjav%C3%ADk_University), [pdf](http://skemman.is/en/stream/get/1946/9180/22971/1/research-report.pdf)

# Forum Posts

- [Mult-cut, SE and ETC](http://www.talkchess.com/forum/viewtopic.php?t=35697) by Ricardo Gibert, [CCC](/CCC "CCC"), August 05, 2010 » [Singular Extensions](/Singular_Extensions "Singular Extensions"), [Enhanced Transposition Cutoff](/Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff")
- [Re: Some thoughts on QS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=476407&t=44507) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), July 30, 2012
- [Multi-cut and fail-soft](http://www.talkchess.com/forum/viewtopic.php?t=60650) by [Matthew R. Brades](/Matthew_R._Brades "Matthew R. Brades"), [CCC](/CCC "CCC"), June 30, 2016 » [Fail-Soft](/Fail-Soft "Fail-Soft")

# External Links

- [Björk](/Category:Bj%C3%B6rk "Category:Björk") - [Big Time Sensuality](https://en.wikipedia.org/wiki/Big_Time_Sensuality), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Katsushika Hokusai](/Category:Katsushika_Hokusai "Category:Katsushika Hokusai") - [Master Pine Pruner](http://commons.wikimedia.org/wiki/File:Master_Pine_Pruner_LACMA_M.2006.136.205a-b.jpg) cropped, ca. 1802, Series: Famous Views of the Eastern Capital, woodcuts, Current location: [Los Angeles County Museum of Art](https://en.wikipedia.org/wiki/Los_Angeles_County_Museum_of_Art), [Category:Katsushika Hokusai](https://commons.wikimedia.org/wiki/Category:Katsushika_Hokusai), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland") (**1998**). *[Multi-cut Pruning in Alpha-Beta Search](http://link.springer.com/chapter/10.1007/3-540-48957-6_2)*. [CG 1998](/CG_1998 "CG 1998")
3. [↑](#cite_ref-3) [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland") (**2001**). *Multi-cut Alpha-Beta Pruning in Game Tree Search.* Theoretical Computer Science, Vol. 252, [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01a.pdf)
4. [↑](#cite_ref-4) [Mark Winands](/Mark_Winands "Mark Winands"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](/Erik_van_der_Werf "Erik van der Werf") (**2003**). *Enhanced forward pruning.* [pdf](http://www.personeel.unimaas.nl/m-winands/documents/Enhanced%20forward%20pruning.pdf)
5. [↑](#cite_ref-5) [Hrafn Eiríksson](/Hrafn_Eir%C3%ADksson "Hrafn Eiríksson") (**2011**). *Investigation of Multi-Cut Pruning in Game-Tree Search*. B.Sc. Thesis, [Reykjavík University](https://en.wikipedia.org/wiki/Reykjav%C3%ADk_University), [pdf](http://skemman.is/en/stream/get/1946/9180/22971/1/research-report.pdf)
6. [↑](#cite_ref-6) [CHESS AND MATHEMATICS - Workshop Dresden, 21st - 23rd November 2008](http://www.math.tu-dresden.de/num/chess2008/index-en.html)
7. [↑](#cite_ref-7) [Workshop Chess and Mathematics](http://www.math.tu-dresden.de/num/chess2008/abstracts.pdf) (pdf) agenda and abstracts

**[Up one Level](/Pruning "Pruning")**