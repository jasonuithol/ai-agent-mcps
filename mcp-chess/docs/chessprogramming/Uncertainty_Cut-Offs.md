# Uncertainty Cut-Offs

Source: https://www.chessprogramming.org/Uncertainty_Cut-Offs

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Pruning](/Pruning "Pruning") \* Uncertainty Cut-Offs**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Indeterminacy_principle.gif/330px-Indeterminacy_principle.gif)](/File:Indeterminacy_principle.gif)

Uncertainty principle [[1]](#cite_note-1)

**Uncertainty Cut-Offs**,  
a safe pruning technique performed in [PVS](/Principal_Variation_Search "Principal Variation Search") at [siblings](/Sibling_Node "Sibling Node") of a [PV-node](/Node_Types#PV "Node Types"), which are [Cut-nodes](/Node_Types#CUT "Node Types"), expected to [fail-high](/Fail-High "Fail-High") and therefor to don't improve the score at the parent PV-node. Even more, the fail-high occurs in > 90% from the first move [[2]](#cite_note-2). Sometimes, previous expectations are changing, and an expected Cut-node turns out to become an [All-node](/Node_Types#ALL "Node Types"), yielding in a re-search.

# The Idea

The basic idea of Uncertainty Cut-Offs is that after the first and some further promising moves didn't fail-high at an expected Cut-Node, to don't waste time with late moves, to premature return an uncertain score of an All-node, indicated by a boolean flag to the PV-node callee. Uncertainty Cut-Offs were investigated by [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") and [Andreas Junghanns](/Andreas_Junghanns "Andreas Junghanns") during the mid 90s at [University of Alberta](/University_of_Alberta "University of Alberta"), as implemented in their chess program [The Turk](/The_Turk "The Turk"). The contribution of Yngvi Björnsson, [Tony Marsland](/Tony_Marsland "Tony Marsland"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") and [Andreas Junghanns](/Andreas_Junghanns "Andreas Junghanns") was introduced by Björnsson at the [Advances in Computer Chess 8](/Advances_in_Computer_Chess_8 "Advances in Computer Chess 8") conference 1996 [[3]](#cite_note-3), published in the conference proceedings and the [ICCA Journal](/ICGA_Journal "ICGA Journal").

# Abstract

[[4]](#cite_note-4)

```
A new domain-independent pruning method is described that guarantees returning a correct game value. Even though alpha-beta-based chess programs are already searching close to the minimal tree, there is still scope for improvement. Our idea hinges on the recognition that the game tree has two types of node, those were cut-offs occur and those that must be fully explored. In the latter case one of the moves is best and yields the subtree value, thus for the remaining alternatives one is simply proving their inferiority. This offers the opportunity for pruning, while introducing some potential for uncertainty in the search process. There are two cases of interest. One considers the immediate alternatives to the Principal Variation itself, and here a safe uncertainty cut-off is presented, the second is a proposal for an unsafe generalization, one which offers substantial search reduction but with the potential for control of the error probability. Experiments with the new pruning method show some potential for savings in the search.
```

# Pseudo Code

*slightly modified [C](/C "C")-like syntax* [[5]](#cite_note-5)

```
TreeValue pvs( node, α, β, depth, ply ) {
   if ( depth == 0 ) return evaluate( node );
   next = firstSuccessor( node );
   best = -pvs( next, -β, -α, depth-1, ply+1 );
   next = nextSibling( next );
   while ( next ) {
      if ( bext >= β ) return best;
      α = max( α, best );
      {merit, unsure} = -nws( next, -α, depth-1, ply+1, PV);
      if ( unsure )
         merit =  -pvs( next, -β, -α, depth-1, ply+1 );
      else if ( merit > α && merit < β )
         merit =  -pvs( next, -β, -merit, depth-1, ply+1 );
      best = max( merit, best );
      next = nextSibling( next );
   }
   return best;
}

{TreeValue, Boolean} nws( node, β, depth, ply, parent ) {
   if ( depth == 0 ) return {evaluate( node ), false};
   next = firstSuccessor( node );
   type = parent == CUT ? ALL : CUT;
   uncertain = false;
   estimate = -oo;
   while ( next ) {
      {merit, unsure} = -nws( next, 1-β, depth-1, ply+1, type);
      if ( unsure ) uncertain = true;
      estimate = max ( merit, estimate );
      if ( merit >= β )
         return {estimate, unsure}; /* CUT node */
      if ( uncertaintyCutoff( estimate, ply,  parent ) )
         return {estimate, true};   /* premature ALL node */
      next = nextSibling( next );
   }
   return {estimate, uncertain};    /* ALL node */
}
```

While the above PVS framework applies the backup of uncertainty, the particular cut-off constraints as implemented in *uncertaintyCutoff* given below does not need to back up uncertainty information. This is because the pruning is only applied if it is guaranteed that the sub-branch will be re-searched.

```
Boolean uncertaintyCutoff( best, ply, parent ) {
   return ( parent == PV
         && searchStack[ply].movesTried > moveLimit
         && -best > searchStack[ply-1].α
         && -best < searchStack[ply-1].β
         && ...
          );
}
```

# Conclusion

Experiments by Björnsson and Junghanns indicate, even though the savings are small, and this pruning technique does not make much difference in most cases, it can significantly decrease the search effort when move ordering heuristics fail.

# See also

- [Enhanced Forward Pruning](/Enhanced_Forward_Pruning "Enhanced Forward Pruning")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Multi-Cut](/Multi-Cut "Multi-Cut")
- [ProbCut](/ProbCut "ProbCut")

# Publications

- [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Andreas Junghanns](/Andreas_Junghanns "Andreas Junghanns") (**1997**). *Searching with Uncertainty Cut-offs.* [ICCA Journal, Vol. 20, No. 1](/ICGA_Journal#20_1 "ICGA Journal"), [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonMSJ00.pdf)
- [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Andreas Junghanns](/Andreas_Junghanns "Andreas Junghanns") (**1997**). *Searching with Uncertainty Cut-offs*. [Advances in Computer Chess 8](/Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")

# External Links

- [Uncertainty from Wikipedia](https://en.wikipedia.org/wiki/Uncertainty)
- [Uncertainty principle from Wikipedia](https://en.wikipedia.org/wiki/Uncertainty_principle)
- [Uncertainty (film) from Wikipedia](https://en.wikipedia.org/wiki/Uncertainty_%28film%29)
- [Uncertainty and Bias](http://apollo.lsc.vsc.edu/classes/remote/lecture_notes/measurements/uncertainty.html) from [Making Meteorological Measurements](http://apollo.lsc.vsc.edu/classes/remote/lecture_notes/measurements/index.html)
- [The Heliocentrics](/Category:The_Heliocentrics "Category:The Heliocentrics") - The Uncertainty Principle, [A World Of Masks](https://theheliocentrics.bandcamp.com/album/a-world-of-masks-2) (2017), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) The [gaussian](https://en.wikipedia.org/wiki/Gaussian_function) [wave function](https://en.wikipedia.org/wiki/Wave_function) Ψ of an initially very localized free particle, by [Thierry Dugnolle](http://commons.wikimedia.org/wiki/User:Thierry_Dugnolle), [Uncertainty principle from Wikipedia](https://en.wikipedia.org/wiki/Uncertainty_principle)
2. [↑](#cite_ref-2) [Aske Plaat](/Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](/Wim_Pijls "Wim Pijls"), [Arie de Bruin](/Arie_de_Bruin "Arie de Bruin") (**1996**). *Exploiting Graph Properties of Game Trees.* [AAAI-96](/Conferences#AAAI-96 "Conferences")
3. [↑](#cite_ref-3) [ICCAJ v.19 n.2 now in North America](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1c08a4963480dbf9) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), July 03, 1996
4. [↑](#cite_ref-4) [Re: ICCAJ v.19 n.2 now in North America](http://groups.google.com/group/rec.games.chess.computer/msg/a034d6ccec29aa01) by [Dennis Breuker](/Dennis_Breuker "Dennis Breuker"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), July 09, 1996
5. [↑](#cite_ref-5) [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Andreas Junghanns](/Andreas_Junghanns "Andreas Junghanns") (**1997**). *Searching with Uncertainty Cut-offs.* [ICCA Journal, Vol. 20, No. 1](/ICGA_Journal#20_1 "ICGA Journal"), [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonMSJ00.pdf)

**[Up one Level](/Pruning "Pruning")**