# Enhanced Forward Pruning

Source: https://www.chessprogramming.org/Enhanced_Forward_Pruning

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Pruning](/Pruning "Pruning") \* Enhanced Forward Pruning**

[![](/images/8/8c/270px-Hoch-Cut_With_the_Kitchen_Knife.jpg)](https://en.wikipedia.org/wiki/File:Hoch-Cut_With_the_Kitchen_Knife.jpg)

[Hannah Höch](/Category:Hannah_H%C3%B6ch "Category:Hannah Höch"), Cut with the Dada ... [[1]](#cite_note-1) [[2]](#cite_note-2)

**Enhanced Forward Pruning**,  
a pruning technique introduced by [Mark Winands](/Mark_Winands "Mark Winands") et al. in 2003 [[3]](#cite_note-3) , which applies forward pruning like [null move pruning](/Null_Move_Pruning "Null Move Pruning") and [multi-cut](/Multi-Cut "Multi-Cut") [[4]](#cite_note-4) not only at expected [Cut-nodes](/Node_Types#CUT "Node Types"), but also at expected [All-nodes](/Node_Types#ALL "Node Types") based on considerations and modifications on the [PVS](/Principal_Variation_Search "Principal Variation Search") framework.

# Pruning in the Null-Window Search

It has become practice to use forward-pruning methods only in the [NWS](/Principal_Variation_Search#ZWS "Principal Variation Search") part of the PVS framework. The idea is that it is too risky to prune forward at an expected [PV-node](/Node_Types#PV "Node Types"), because a possible mistake causes an immediate change of the [principal variation](/Principal_Variation "Principal Variation").

## Cut-Node

If one erroneously prunes forward at some [Cut-node](/Node_Types#CUT "Node Types") and the resulting score is backed up all the way to a PV-node, it obtains a [fail-low](/Fail-Low "Fail-Low"), due to the odd ply distance to its [PV-ancestor](/Node_Types#PV "Node Types"), no re-search will be performed. The result of the mistake is that a possible new principal variation is overlooked in this position. Therefore, forward pruning at a Cut-node without further provisions is dangerous. However, by the large savings achieved it has proven worthwhile to implement further provisions making forward pruning at Cut-nodes more safe (and thus acceptable).

## All-Node

If one erroneously forward prunes at some [All-node](/Node_Types#ALL "Node Types") and the resulting score is backed up all the way to a PV-node, it obtain a [fail-high](/Fail-High "Fail-High") and a re-search will be performed. The algorithm is then searching for a new principal variation and regards the subsequent nodes as PV-nodes. Because no forward pruning is done at PV-nodes, it is possible to find out whether there exists a new [PV](/Principal_Variation "Principal Variation") or not. In this case the result of the mistake will be that an extra amount of nodes has been searched. In principle, forward pruning at an expected All-node is not dangerous but can trigger unnecessary re-searches.

# Four Additions

1. To prevent that a backed-up value of a forward-pruned All-node causes a [cutoff](/Beta-Cutoff "Beta-Cutoff") at the PV-node lying above, the forward-pruning mechanism should return a value equal to [β](/Beta "Beta") in case of a cutoff (which is equal to α+1 at an All-node).
2. If the window of the PV-node was already closed and the [NWS](/Principal_Variation_Search#ZWS "Principal Variation Search") should return a value equal to β (α+1), we still have to do a re-search.
3. If we do a re-search and the returned value of the NWS equals α+1, we should do a re-search with α as [lower bound](/Lower_Bound "Lower Bound").
4. Cut-nodes where a [fail-low](/Fail-Low "Fail-Low") has occurred with a value equal to α are not stored in the [transposition table](/Transposition_Table "Transposition Table") because their values are uncertain.

# Pseudo Code

```
enum {PV_NODE = 0, CUT_NODE = 1, ALL_NODE = -1};

int PVS(node, alpha, beta, depth, node_type)
{
   //Transposition table lookup, omitted
   ...
   if (depth == 0)
      return evaluate(pos);
   if (node_type != PV_NODE)
   {
      //Forward-pruning code, omitted
      ...
      if (forward_pruning condition holds) /* Addition 1 */
         return beta; 
   }
   next = firstSuccessor(node);
   best = -PVS(next, -beta, -alpha, depth-1, -node_type);
   if (best >= beta)
      goto Done;
   next = nextSibling(next);
   while (next != null)
   {
      alpha = max(alpha, best);
      //Null-Window Search Part
      value = -PVS(next, -alpha-1, -alpha, depth-1, (node_type == CUT_NODE)? ALL_NODE : CUT_NODE) );
      //Re-search
      if ( (value > alpha && value < beta) 
      ||   (node_type == PV_NODE && value == beta && beta == alpha+1) ) /* Addition 2 */
      {
         //Value is not a real lower bound
         if (value == alpha+1) /* Addition 3 */
            value = alpha;
         value = -PVS(next, -beta, -value, depth-1, node_type);
      }
      if (value > best)
      {
         best = value;
         if (best >= beta)
            goto Done;
      }
      next = nextSibling(next);
   }
   if (node_type == CUT_NODE && best == alpha)  /* Addition 4 */
      return best;
   Done: //Store in Transposition table, omitted
   ...
}
```

# See also

- [Multi-Cut](/Multi-Cut "Multi-Cut")
- [Node Types](/Node_Types "Node Types")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [ProbCut](/ProbCut "ProbCut")

# Publications

- [Mark Winands](/Mark_Winands "Mark Winands"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](/Erik_van_der_Werf "Erik van der Werf") (**2003**). *[Enhanced forward pruning](https://research.tilburguniversity.edu/en/publications/enhanced-forward-pruning)*. JCIS 2003
- [Mark Winands](/Mark_Winands "Mark Winands"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](/Erik_van_der_Werf "Erik van der Werf") (**2005**). *Enhanced Forward Pruning*. [Information Sciences](https://en.wikipedia.org/wiki/Information_Sciences_(journal)), Vol. 175, No. 4, [pdf preprint](http://erikvanderwerf.tengen.nl/pubdown/Enhanced%20forward%20pruning.pdf)

# Forum Posts

- [NMP on ALL nodes](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6392) by [Onno Garms](/Onno_Garms "Onno Garms"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 15, 2007 » [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning"), [All Nodes](/Node_Types#ALL "Node Types")

# References

1. [↑](#cite_ref-1) [Hannah Höch](/Category:Hannah_H%C3%B6ch "Category:Hannah Höch") - [Cut with the Dada Kitchen Knife through the Last Weimar Beer-Belly Cultural Epoch in Germany](https://en.wikipedia.org/wiki/File:Hoch-Cut_With_the_Kitchen_Knife.jpg), [Collage](https://en.wikipedia.org/wiki/Collage) of pasted papers, 90×144 cm, 1919, [National Gallery](https://en.wikipedia.org/wiki/National_Gallery_%28Berlin%29), [Berlin State Museums](https://en.wikipedia.org/wiki/Berlin_State_Museums), [Hannah Höch from Wikipedia](https://en.wikipedia.org/wiki/Hannah_H%C3%B6ch), [Dada from Wikipedia](https://en.wikipedia.org/wiki/Dada), [Weimar culture from Wikipedia](https://en.wikipedia.org/wiki/Weimar_culture)
2. [↑](#cite_ref-2) [le monde de kitchi: Great Women #1: Hannah Höch](http://lemondedekitchi.blogspot.de/2014/10/great-women-1-hannah-hoch.html) (German)
3. [↑](#cite_ref-3) [Mark Winands](/Mark_Winands "Mark Winands"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](/Erik_van_der_Werf "Erik van der Werf") (**2003**). *Enhanced forward pruning.* JCIS 2003
4. [↑](#cite_ref-4) [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland") (**2001**). *Multi-cut Alpha-Beta Pruning in Game Tree Search.* [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_(journal)), Vol. 252, [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01a.pdf)

**[Up one Level](/Pruning "Pruning")**