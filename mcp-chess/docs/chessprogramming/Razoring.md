# Razoring

Source: https://www.chessprogramming.org/Razoring

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Reductions](/Reductions "Reductions") \* Razoring**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/William_of_Ockham_-_Logica_1341.jpg/330px-William_of_Ockham_-_Logica_1341.jpg)](/File:William_of_Ockham_-_Logica_1341.jpg)

[Occam's razor](https://en.wikipedia.org/wiki/Occam%27s_razor) [[1]](#cite_note-1)

Unlike [Alpha-Beta](/Alpha-Beta "Alpha-Beta"), classical **Razoring** [[2]](#cite_note-2) [prunes](/Pruning "Pruning") branches forward, if the static evaluation of a move is less than or equal to [Alpha](/Alpha "Alpha"). It assumes that from any given position my opponent will be able to find at least one move that improves his position, the [Null Move Observation](/Null_Move_Observation "Null Move Observation"). There are various implementations of Razoring, somehow diminishing [pruning](/Pruning "Pruning") and [reductions](/Reductions "Reductions") near the [horizon](/Horizon_Node "Horizon Node"). Razoring either prunes forward based on a reduced search, even the [quiescence search](/Quiescence_Search "Quiescence Search"), or it reduces based on [evaluation](/Evaluation "Evaluation") or quiescence search as well.

# Pre Frontier Nodes

The idea introduced by [John Birmingham](/John_Birmingham "John Birmingham") and [Peter Kent](/Peter_Kent "Peter Kent") [[3]](#cite_note-3) was applied at so-called [pre frontier](/Pre_Frontier_Node "Pre Frontier Node") (depth = 2) expected [All-Nodes](/Node_Types#ALL "Node Types"). Before searching deeper, all [moves were generated](/Move_Generation "Move Generation"), [made](/Make_Move "Make Move"), [evaluated](/Evaluation "Evaluation"), [unmade](/Unmake_Move "Unmake Move") and then inserted inside a sorted [move list](/Move_List "Move List"). While fetching the sorted moves in decreasing order - as long as the evaluation of each move exceeds [alpha](/Alpha "Alpha") - they were tried as usual. Once a move statically does no longer improve [alpha](/Alpha "Alpha"), this and all further moves (sorted below) are pruned without any further investigation.

# Deep Razoring

There is even a more aggressive pruning technique at depth = 4 nodes, called Deep Razoring. The weaker assumption is my opponent will be able to improve his position with a *yourmove-mymove-yourmove* sequence.

# Limited Razoring

[Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") introduced *Limited Razoring*, pushing the idea of [futility pruning](/Futility_Pruning "Futility Pruning") one step further to pre-pre-frontier nodes (depth = 3), he combines it with the depth-reduction mechanism of deep razoring [[4]](#cite_note-4) .

```
fscore = mat_balance(current) + razor_margin;
if (!extend
 && (depth == PRE_PRE_FRONRIER)
 && (fscore <= alpha)
 && (opposing_pieces(current) > 3)
   ) depth = PRE_FRONRIER;
```

# Amir Ban's Definition

[Amir Ban](/Amir_Ban "Amir Ban") in a [CCC](/CCC "CCC") discussion with [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") on Razoring versus [Pruning](/Pruning "Pruning") [[5]](#cite_note-5) :

```
Razoring is supposed to be a sort of forward pruning where rather than skipping an entire subtree, you search it to a reduced depth, typically one less than normal depth. The advantage is that you get most of the saving but with much lower risk than pruning entire subtrees. Razoring is the only forward pruning technique Junior uses, with a depth reduction of one (half-ply). Seems like Crafty uses the same definition ...
```

# Implementation

## Stockfish

In 2022 razoring was reintroduced to [Stockfish](/Stockfish "Stockfish") [[6]](#cite_note-6) by [Michael Chaly](/Michael_Chaly "Michael Chaly"). The implementation features a quadratic depth-dependent margin. Certain precautions were made later on to prevent razoring from interfering with mate finding.

```
// Step 7. Razoring (~1 Elo)
// If eval is really low check with qsearch if it can exceed alpha, if it can't,
// return a fail low.
if (eval < alpha - 512 - 293 * depth * depth)
{
    value = qsearch<NonPV>(pos, ss, alpha - 1, alpha);
    if (value < alpha && std::abs(value) < VALUE_TB_WIN_IN_MAX_PLY)
        return value;
}
```

# Historical Implementations

## Crafty 15.17

This code snippet appears in [Crafty 15.17](/Crafty "Crafty") [[7]](#cite_note-7) (~1998) [[8]](#cite_note-8) with [fractional](/Extensions#FractionalExtensions "Extensions") reductions based on [evaluation](/Evaluation "Evaluation") at [pre frontier nodes](/Pre_Frontier_Node "Pre Frontier Node") (depth = 2), already controversially discussed between [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen") and [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") in 2002 [[9]](#cite_note-9) :

```
/*
 ----------------------------------------------------------
|                                                          |
|   now we toss in the "razoring" trick, which simply says |
|   if we are doing fairly badly, we can reduce the depth  |
|   an additional ply, if there was nothing at the current |
|   ply that caused an extension.                          |
|                                                          |
 ----------------------------------------------------------
*/
      if (depth<3*INCREMENT_PLY && depth>=2*INCREMENT_PLY &&
          !tree->in_check[ply] && extensions == -60) {
        register int value=-Evaluate(tree,ply+1,ChangeSide(wtm),
                                     -(beta+51),-(alpha-51));
        if (value+50 < alpha) extensions-=60;
      }
```

## Dropping into Q-search

A different razoring approach was proposed by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") in [CCC](/CCC "CCC") [[10]](#cite_note-10) based on an idea by [Tord Romstad](/Tord_Romstad "Tord Romstad") [[11]](#cite_note-11) , and abandoned in Crafty after cluster testing [[12]](#cite_note-12) . Dropping into the [quiescence search](/Quiescence_Search "Quiescence Search") is intended inside a [PVS](/Principal_Variation_Search "Principal Variation Search") framework at strong expected [All-nodes](/Node_Types#ALL "Node Types") near the tips (pre-pre-frontier nodes or below, depth <= 3), that is a [null window](/Null_Window "Null Window") (alpha = beta - 1) is passed, and the static [evaluation](/Evaluation "Evaluation") is by a margin (~three pawns) below beta (or <= alpha). If under these conditions the quiescence search confirms the fail-low characteristics, its score is trusted and returned.

```
/*
************************************************************
*                                                          *
* now we try a quick Razoring test. If we are within 3     *
* plies of a tip, and the current eval is 3 pawns (or      *
* more) below beta, then we just drop into a q-search      *
* to try to get a quick cutoff without searching more in   *
* a position where we are way down in material.            *
*                                                          *
************************************************************
*/
if (razoring_allowed && depth <= razor_depth) {
   if (alpha == beta - 1) { // null window ?
      if (Evaluate(tree, ply, wtm, alpha, beta) + razor_margin < beta) { // likely a fail-low node ?
         value = QuiesceChecks(tree, alpha, beta, wtm, ply);
         if (value < beta)
            return value; // fail soft
      }
   }
}
```

## Strelka

Similar code appears in [Jury Osipov's](/Jury_Osipov "Jury Osipov") [open source engine](/Category:Open_Source "Category:Open Source") [Strelka 2.0](/Strelka "Strelka") [[13]](#cite_note-13) , failing a bit harder. The interesting thing is the missing new\_value < beta condition in the depth = 1 case. If the static [evaluation](/Evaluation "Evaluation") indicates a [fail-low node](/Node_Types#ALL "Node Types"), but q-search [fails high](/Fail-High "Fail-High"), the score of the reduced fail-high search is returned, since there was obviously a winning capture raising the score, and one assumes a [quiet move](/Quiet_Moves "Quiet Moves") near the horizon will not do better [[14]](#cite_note-14) .

*Strelka.c line 393* (slightly modified for clarification) [user:GerdIsenberg](/User:GerdIsenberg "User:GerdIsenberg")

```
  value = eval + 125;
  if (value < beta) {
    if (depth == 1) {
      new_value = qsearch(...);
      return max(new_value, value);
    }
    value += 175;
    if (value < beta && depth <= 3) {
      new_value = qsearch(...);
      if (new_value < beta)
         return max(new_value, value);
    }
  }
```

In the [Rybka Forum](/Computer_Chess_Forums "Computer Chess Forums") thread on [Strelka 2.0](/Strelka "Strelka") [[15]](#cite_note-15) , [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie") states on this feature [[16]](#cite_note-16) :

```
I'm also pretty amazed at how aggressively the search prunes. Not only will Strelka drop straight into the q-search on a depth-3 search, but because it orders all captures first, it will reduce almost all noncapture/check moves.
```

# See also

Classical Razoring is known for being risky. It likely was a progress in [Shannon](/Claude_Shannon "Claude Shannon") [Type-B](/Type_B_Strategy "Type B Strategy") programs and a fixed width. Todays programs more likely rely on:

- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Extended Futility Pruning](/Futility_Pruning#Extendedfutilityprunning "Futility Pruning")
- [AEL-Pruning](/AEL-Pruning "AEL-Pruning")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- and various [Reductions](/Reductions "Reductions") (and [Extensions](/Extensions "Extensions")) depending on depth left, and probably expected node type.

# Publications

- [John Birmingham](/John_Birmingham "John Birmingham"), [Peter Kent](/Peter_Kent "Peter Kent") (**1977**). *Tree-searching and tree-pruning techniques*. [Advances in Computer Chess 1](/Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"), reprinted 1988 in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
- [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[Extended Futility Pruning](http://people.csail.mit.edu/heinz/dt/node18.html).* [ICCA Journal, Vol. 21, No. 2](/ICGA_Journal#21_2 "ICGA Journal"), including [Limited Razoring at Pre-Pre-Frontier Nodes](http://people.csail.mit.edu/heinz/dt/node28.html)

# Forum Posts

## 1995 ...

- [limited razoring question](https://www.stmintz.com/ccc/index.php?id=28706) by [Werner Inmann](/Werner_Inmann "Werner Inmann"), [CCC](/CCC "CCC"), October 03, 1998
- [Razoring?](https://www.stmintz.com/ccc/index.php?id=40931) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), January 26, 1999
- [razoring?](https://www.stmintz.com/ccc/index.php?id=64838) by [Scott Gasch](/Scott_Gasch "Scott Gasch"), [CCC](/CCC "CCC"), August 16, 1999

## 2000 ...

- [razoring in crafty version 16.9, mid 1999](https://www.stmintz.com/ccc/index.php?id=246598) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), August 21, 2002

## 2005 ...

- [Razoring...](http://www.talkchess.com/forum/viewtopic.php?t=24286) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), October 09, 2008
- [futility pruning - razoring](http://www.talkchess.com/forum/viewtopic.php?t=29777) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), September 16, 2009 » [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Futility pruning, Ext futility pruning and Limited Razoring](http://www.talkchess.com/forum/viewtopic.php?t=30802) by Jesper Nielsen, [CCC](/CCC "CCC"), November 26, 2009

## 2010 ...

- [Bad Pruning](http://www.talkchess.com/forum/viewtopic.php?t=38407) by [Onno Garms](/Onno_Garms "Onno Garms"), [CCC](/CCC "CCC"), March 13, 2011 » [Onno](/Onno "Onno")
- [Re: Still waiting on Ed](http://www.open-chess.org/viewtopic.php?f=3&t=1477&start=20#p13017) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 07, 2011 » on [Crafty](/Crafty "Crafty") 22.1 vs. 23.4. differences
- [futility pruning, razoring question](http://www.talkchess.com/forum/viewtopic.php?t=43165) by [Marco Belli](/Marco_Belli "Marco Belli"), [CCC](/CCC "CCC"), April 04, 2012 » [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Razoring / Lazy eval question](http://www.talkchess.com/forum/viewtopic.php?t=46130) by [Jerry Donald](/index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](/CCC "CCC"), November 24, 2012 » [Lazy Evaluation](/Lazy_Evaluation "Lazy Evaluation")
- [Null move, razoring and mate threats](http://www.talkchess.com/forum/viewtopic.php?t=49863) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), October 28, 2013 » [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")

## 2015 ...

- [Razoring vs Futility pruning](http://www.talkchess.com/forum/viewtopic.php?t=57287) by [Shawn Chidester](/Shawn_Chidester "Shawn Chidester"), [CCC](/CCC "CCC"), August 16, 2015 » [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Verification of pruning techniques](http://www.talkchess.com/forum/viewtopic.php?t=57843) by [Shawn Chidester](/Shawn_Chidester "Shawn Chidester"), [CCC](/CCC "CCC"), October 04, 2015 » [Pruning](/Pruning "Pruning")

## 2020 ...

- [Is razoring useless in modern engines ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72857) by [Alayan Feh](/index.php?title=Alayan_Feh&action=edit&redlink=1 "Alayan Feh (page does not exist)"), [CCC](/CCC "CCC"), January 20, 2020
- [Questions on Razoring and Code Structure for Pruning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74425) by Cheney, [CCC](/CCC "CCC"), July 09, 2020 » [Pruning](/Pruning "Pruning")

# External Links

- [Razor from Wikipedia](https://en.wikipedia.org/wiki/Razor)
- [Razor Blade from Wikipedia](https://en.wikipedia.org/wiki/Razor_Blade)
- [Razor (hair) cut from Wikipedia](https://en.wikipedia.org/wiki/Razor_cut)
- [Razoring](http://liswiki.org/wiki/Razoring) from [Library and Information Science Wiki](http://liswiki.org/wiki/Main_Page)
- [UNISYS-History - A 1955 Remington Rand electric shaver](http://www.computermuseum.li/Testpage/UNISYS-History.htm#RemRandShaver)
- [Philishave from Wikipedia](https://en.wikipedia.org/wiki/Philishave)
- [Occam's razor from Wikipedia](https://en.wikipedia.org/wiki/Occam%27s_razor)
- [Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa") - [Occam's Razor](http://wiki.killuglyradio.com/wiki/Occam%27s_Razor) from [One Shot Deal](https://en.wikipedia.org/wiki/One_Shot_Deal), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa"), [Warren Cuccurullo](https://en.wikipedia.org/wiki/Warren_Cuccurullo), [Denny Walley](https://wiki.killuglyradio.com/wiki/Denny_Walley), [Ike Willis](https://en.wikipedia.org/wiki/Ike_Willis), [Tommy Mars](https://en.wikipedia.org/wiki/Tommy_Mars), [Peter Wolf](https://en.wikipedia.org/wiki/Peter_Wolf_%28producer%29), [Arthur Barrow](https://en.wikipedia.org/wiki/Arthur_Barrow), [Vinnie Colaiuta](/Category:Vinnie_Colaiuta "Category:Vinnie Colaiuta"), [Ed Mann](https://en.wikipedia.org/wiki/Ed_Mann)

# References

1. [↑](#cite_ref-1) [William of Ockham](https://en.wikipedia.org/wiki/William_of_Ockham) – Sketch labeled "frater Occham iste", from a manuscript of Ockham's Summa Logicae, 1341
2. [↑](#cite_ref-2) [John Birmingham](/John_Birmingham "John Birmingham"), [Peter Kent](/Peter_Kent "Peter Kent") (**1977**). *Tree-searching and tree-pruning techniques*. [Advances in Computer Chess 1](/Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"), reprinted 1988 in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
3. [↑](#cite_ref-3) [John Birmingham](/John_Birmingham "John Birmingham"), [Peter Kent](/Peter_Kent "Peter Kent") (**1977**). *Tree-searching and tree-pruning techniques*. [Advances in Computer Chess 1](/Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"), reprinted 1988 in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
4. [↑](#cite_ref-4) [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[Extended Futility Pruning](http://people.csail.mit.edu/heinz/dt/node18.html).* [ICCA Journal, Vol. 21, No. 2](/ICGA_Journal#21_2 "ICGA Journal"), including [Limited Razoring at Pre-Pre-Frontier Nodes](http://people.csail.mit.edu/heinz/dt/node28.html)
5. [↑](#cite_ref-5) [Re: Razoring?](https://www.stmintz.com/ccc/index.php?id=41065) by [Amir Ban](/Amir_Ban "Amir Ban"), [CCC](/CCC "CCC"), January 27, 1999
6. [↑](#cite_ref-6) [Reintroduce razoring. by Vizvezdenec · Pull Request #3921 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3921), Github, February 4, 2022
7. [↑](#cite_ref-7) [Robert Hyatt's FTP Page](ftp://ftp.cis.uab.edu/pub/hyatt), <source> [crafty-15.17.zip](ftp://ftp.cis.uab.edu/pub/hyatt/source/crafty-15.17.zip), search.c
8. [↑](#cite_ref-8) [Re: Razoring](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=439367&t=41597) by [Sven Schüle](/Sven_Sch%C3%BCle "Sven Schüle"), [CCC](/CCC "CCC"), December 25, 2011
9. [↑](#cite_ref-9) [razoring in crafty version 16.9, mid 1999](https://www.stmintz.com/ccc/index.php?id=246598) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), August 21, 2002
10. [↑](#cite_ref-10) [Razoring...](http://www.talkchess.com/forum/viewtopic.php?t=24286) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), October 09, 2008
11. [↑](#cite_ref-11) [Re: Razoring](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=439431&t=41597) by [Marco Costalba](/Marco_Costalba "Marco Costalba"), [CCC](/CCC "CCC"), December 26, 2011
12. [↑](#cite_ref-12) [Re: futility pruning - razoring](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291637&t=29777) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), September 16, 2009
13. [↑](#cite_ref-13) [Download](http://www.sdchess.ru/download_engines.htm) by [sdchess.ru](http://www.sdchess.ru/)
14. [↑](#cite_ref-14) [Razoring](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/8695c3373be2b379#) by [Joe Stella](/index.php?title=Joe_Stella&action=edit&redlink=1 "Joe Stella (page does not exist)"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), August 31, 1995
15. [↑](#cite_ref-15) [Strelka 2.0](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3006) by [Vasik Rajlich](/Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008
16. [↑](#cite_ref-16) [Strelka 2.0 pg 4](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3006;pg=4) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [Rybka Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008

**[Up one Level](/Reductions "Reductions")**