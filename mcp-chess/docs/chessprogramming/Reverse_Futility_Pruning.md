# Reverse Futility Pruning

Source: https://www.chessprogramming.org/Reverse_Futility_Pruning

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Pruning](/Pruning "Pruning") \* Reverse Futility Pruning**

**Reverse Futility Pruning**, (RFP, Static Null Move Pruning)  
postpones a [extended futility pruning](/Futility_Pruning#Extendedfutilitypruning "Futility Pruning") (EFP) condition applied at [pre]... [pre frontier nodes](/Pre_Frontier_Node "Pre Frontier Node") to skip moves inside its move loop if [material balance](/Material#Balance "Material") plus gain of the move and safety margin does not improve [alpha](/Alpha "Alpha"), with the "reversed" or [negamaxed](/Negamax "Negamax") [fail-high](/Fail-High "Fail-High") condition of a more reliable [score](/Score "Score") minus safety margin greater or equal than [beta](/Beta "Beta") - after [making the move](/Make_Move "Make Move"), and calling the child and its [static evaluation](/Evaluation "Evaluation"). Thus, Reverse Futility Pruning relies on the [null move observation](/Null_Move_Observation "Null Move Observation"), and is a generalisation of [standing pat](/Quiescence_Search#StandPat "Quiescence Search") at [quiescent nodes](/Quiescent_Node "Quiescent Node"), or a special case of [null move pruning](/Null_Move_Pruning "Null Move Pruning") without explicitly making [one](/Null_Move "Null Move") [[1]](#cite_note-1):

# Pseudo Code

```
int search( int alpha, int beta, ... ) {
  int eval = evaluate(...);
  int margin = ...; // e.g. 150 * depth
  if (... && eval >= beta + margin)
    return eval; // fail soft
  ...
}
```

# Tweaks

## Conditions

It is common to skip RFP when one of the following conditions are met:

- Position is in check
- Node type is a [PV](/Node_Types#PV-Nodes "Node Types") node.
- Position is or has been a [PV](/Node_Types#PV-Nodes "Node Types") node.
- [TT move](/Hash_Move "Hash Move") does not exist or is capture.

## Margin Adjustments

The base RFP margin is usually a constant multiple of depth. The following additional tweaks to the RFP margin are also common in top engines.

- Reduce RFP margin when position is [improving](/Improving "Improving")
- Tweak RFP margin by the aggregate history score of previous move, divided by some factor.

## Return Value

Adjusting the return value of RFP is also found to gain strength in some engines. For example, some engines return (eval + beta) / 2 or beta + (eval - beta) / 3 on successful RFP.

# See also

- [AEL-Pruning](/AEL-Pruning "AEL-Pruning")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Null Move Observation](/Null_Move_Observation "Null Move Observation")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Razoring](/Razoring "Razoring")
- [Standing Pat in Quiescence Search](/Quiescence_Search#StandPat "Quiescence Search")

# Forum Posts

## 2008 ...

- [Toga/Glaurung/Strelka Prunings/Reductions](http://www.talkchess.com/forum/viewtopic.php?t=19316) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), January 31, 2008 » [Toga](/Toga "Toga"), [Glaurung](/Glaurung "Glaurung"), [Strelka](/Strelka "Strelka"), [Reductions](/Reductions "Reductions")
- [Null move in quiescence search idea from Don Beal, 1986](http://www.talkchess.com/forum/viewtopic.php?t=29439) by [Eelco de Groot](/index.php?title=Eelco_de_Groot&action=edit&redlink=1 "Eelco de Groot (page does not exist)"), [CCC](/CCC "CCC"), August 17, 2009 » [Quiescence Search](/Quiescence_Search "Quiescence Search"), [Don Beal](/Don_Beal "Don Beal")

## 2010 ...

- [static null move pruning is stockfish](http://www.talkchess.com/forum/viewtopic.php?t=34909) by [Tom King](/Tom_King "Tom King"), [CCC](/CCC "CCC"), June 13, 2010 » [Stockfish](/Stockfish "Stockfish")
- [Reverse Futility Pruning](http://www.talkchess.com/forum/viewtopic.php?t=41302) by [Matthew R. Brades](/Matthew_R._Brades "Matthew R. Brades"), [CCC](/CCC "CCC"), December 02, 2011
- [mate distance pruning problems and static null move pruning](http://www.talkchess.com/forum/viewtopic.php?t=41337) by Pierre Bokma, [CCC](/CCC "CCC"), December 04, 2011 » [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")

## 2015 ...

- [Futile attempts at futility pruning](http://www.talkchess.com/forum/viewtopic.php?t=59661) by [Martin Fierz](/Martin_Fierz "Martin Fierz"), [CCC](/CCC "CCC"), March 27, 2016
- [Futility prunning](http://www.talkchess.com/forum/viewtopic.php?t=61093) by [Daniel Anulliero](/Daniel_Anulliero "Daniel Anulliero"), [CCC](/CCC "CCC"), August 11, 2016 » [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Static null move pruning](http://www.talkchess.com/forum/viewtopic.php?t=62522) by Fernando Tenorio, [CCC](/CCC "CCC"), December 18, 2016
- [Static NULL Move](http://www.open-chess.org/viewtopic.php?f=5&t=3056) by thevinenator, [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 26, 2016 » [CPW-Engine\_search](/CPW-Engine_search "CPW-Engine search")
- [Futility pruning ?](http://www.talkchess.com/forum/viewtopic.php?t=63344) by [Mahmoud Uthman](/index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](/CCC "CCC"), March 04, 2017 » [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [increasing futility prunning depth](http://www.talkchess.com/forum/viewtopic.php?t=63852) by [Alexandru Mosoi](/Alexandru_Mosoi "Alexandru Mosoi"), [CCC](/CCC "CCC"), April 28, 2017

# References

1. [↑](#cite_ref-1) [Re: Reverse Futility Pruning](http://www.talkchess.com/forum/viewtopic.php?t=41302&start=1) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), December 02, 2011

**[Up one Level](/Pruning "Pruning")**