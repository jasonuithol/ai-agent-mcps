# History Heuristic

Source: https://www.chessprogramming.org/History_Heuristic

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Move Ordering](/Move_Ordering "Move Ordering") \* History Heuristic**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Agache_-_La_Fortuna.jpg/330px-Agache_-_La_Fortuna.jpg)](/File:Agache_-_La_Fortuna.jpg)

[Alfred Agache](/Category:Alfred_Agache "Category:Alfred Agache") - La Fortuna, 1885 [[1]](#cite_note-1)

**History Heuristic**,  
a dynamic move ordering method based on the number of cutoffs caused by a given move irrespectively from the position in which the move has been made. The Heuristic was invented by [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") in 1983 [[2]](#cite_note-2) and works as follows: on a [cutoff](/Beta-Cutoff "Beta-Cutoff") we increment a counter in a special table, addressed either by [from][to] (the [Butterfly Boards](/Butterfly_Boards "Butterfly Boards")) or by [piece][to] [[3]](#cite_note-3) . The added value is typically a multiple of depth or depth \* depth, based on the assumption that otherwise moves from the plies near the leaves would have to much impact on the result. Values retrieved from that table are used to order non-capturing moves. This simple heuristics performs usually better than domain-dependent heuristics, though it may be combined with them. For example, in [Stockfish](/Stockfish "Stockfish") all quiet moves that are not hash moves are ordered by history, while in [Rebel](/Rebel "Rebel") only a few non-captures are ordered by history heuristics, then a piece-square approach is used [[4]](#cite_note-4) . In the literature, history heuristic is often presented as depth-independent generalization of the [killer moves](/Killer_Heuristic "Killer Heuristic"). It is also said to reflect long-term plans in a position.

# Update

## History Bonuses

This is how the history [array](/Array "Array") may be updated, if a [beta-cutoff](/Beta-Cutoff "Beta-Cutoff") occurs:

```
if ( score >= beta ) { // cutoff
   if ( isNonCapture (move) )
      history[sideToMove][move.from][move.to] += depth*depth;
   ...
   return score;
}
```

Modern programs use a more sophisticated formula for history updates, namely the **history gravity** formula:

```
void update(Color sideToMove, Square from, Square to, int bonus)
{
    int clampedBonus = clamp(bonus, -MAX_HISTORY, MAX_HISTORY);
    history[sideToMove][from][to]
        += clampedBonus - history[sideToMove][from][to] * abs(clampedBonus) / MAX_HISTORY;
}
```

This scales up history updates when a beta cutoff is unexpected, and scales down history updates when a beta cutoff is expected. A beneficial side effect is that this formula also clamps history values from -MAX\_HISTORY to MAX\_HISTORY, which prevents oversaturated values.

## History Maluses

When a quiet move fails high, it is also common to apply a penalty to all quiet moves that were previously searched. This not only prevents saturated history values, but also gives unpromising moves negative history. In programs with history gravity formula, this is done by applying negative bonus to the history array.

```
const int bonus = 300 * depth - 250;
history.update(bestMove, bonus);
for (Move move : quietsSearched)
{
    history.update(move, -bonus); // Stronger programs have a separate formula for maluses
}
```

# Counter Moves History

A combination of the History Heuristic in conjunction with the [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic"), proposed by [Bill Henry](/Bill_Henry "Bill Henry") in March 2015 [[5]](#cite_note-5) , as already used by [Álvaro Begué](/%C3%81lvaro_Begu%C3%A9 "Álvaro Begué") in his [Checkers](/Checkers "Checkers") program 20 years before [[6]](#cite_note-6) , was implemented by [Stockfish](/Stockfish "Stockfish") contributor [Stefan Geschwentner](/Stefan_Geschwentner "Stefan Geschwentner") [[7]](#cite_note-7), further tuned and improved by the Stockfish community, and released in [Stockfish 7](/Stockfish "Stockfish") in January 2016, dubbed **Counter Moves History** and mentioned to gain some Elo points [[8]](#cite_note-8). Stockfish's History and Countermove arrays are piece type and [to-square](/Target_Square "Target Square") based, not butterfly based. Each entry indexed by a previous move, is a complete history table with counters indexed by the move refuting that previous move.
Pushing the idea further, Stockfish applies **Follow Up History** (FUH) tables, indexed by two consecutive moves of the same side [[9]](#cite_note-9).

# Continuation History

**Continuation History** is a generalization of [Counter Moves History](#Counter_Moves_History) and Follow Up History. An **n-ply Continuation History** is the history score indexed by the move played n-ply ago and the current move. 1-ply and 2-ply continuation histories are most popular and correspond to Counter Moves History and Follow Up History respectively. Many programs, notably [Stockfish](/Stockfish "Stockfish"), also makes use of 3, 4, 5, and 6-ply continuation histories.

# Capture History

**Capture History**, introduced by [Stefan Geschwentner](/Stefan_Geschwentner "Stefan Geschwentner") in 2016, is a variation on history heuristic applied on capture moves. It is a history table indexed by moved piece, target square, and captured piece type. The history table receives a bonus for captures that failed high, and maluses for all capture moves that did not fail high. The history values is used as a replacement for LVA in [MVV-LVA](/MVV-LVA "MVV-LVA").

# See also

- [Butterfly Boards](/Butterfly_Boards "Butterfly Boards")
- [Butterfly Heuristic](/Butterfly_Heuristic "Butterfly Heuristic")
- [Chessmaps Heuristic](/Chessmaps_Heuristic "Chessmaps Heuristic")
- [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic")
- [History Leaf Pruning](/History_Leaf_Pruning "History Leaf Pruning")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")

:   [Late Move Reduction Test Results](/Late_Move_Reduction_Test_Results "Late Move Reduction Test Results")

- [Neural MoveMap Heuristic](/Neural_MoveMap_Heuristic "Neural MoveMap Heuristic")
- [Relative History Heuristic](/Relative_History_Heuristic "Relative History Heuristic")
- [Vice Video](/Vice#KillHist "Vice")

# Selected Publications

## 1980 ...

- [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1983**). *The History Heuristic*. [ICCA Journal, Vol. 6, No. 3](/ICGA_Journal#6_3 "ICGA Journal")
- [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *[The History Heuristic and Alpha-Beta Search Enhancements in Practice](https://ieeexplore.ieee.org/document/42858)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](/IEEE#TPAMI "IEEE"), Vol. 11, No. 11
- [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *Memory Efficiency in some Heuristics*. [ICCA Journal, Vol. 15, No. 2](/ICGA_Journal#15_2 "ICGA Journal")
- [Eric Thé](/Eric_Th%C3%A9 "Eric Thé") (**1992**). *[An analysis of move ordering on the efficiency of alpha-beta search](http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=56753&local_base=GEN01-MCG02)*. Master's thesis, [McGill University](/McGill_University "McGill University")

## 2000 ...

- [Mark Winands](/Mark_Winands "Mark Winands"), [Erik van der Werf](/Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**2004**). *[The Relative History Heuristic](http://link.springer.com/chapter/10.1007/11674399_18)*. [CG 2004](/CG_2004 "CG 2004"), [pdf](http://erikvanderwerf.tengen.nl/pubdown/relhis.pdf)
- [Jeff Rollason](/Jeff_Rollason "Jeff Rollason") (**2006**). *[Driving search with Plausibility analysis: Looking at the right moves](http://www.aifactory.co.uk/newsletter/2005_04_plausibility_analysis.htm)*. [AI Factory](/AI_Factory "AI Factory"), Winter 2006
- [Jeff Rollason](/Jeff_Rollason "Jeff Rollason") (**2007**). *[Negative Plausibility](http://www.aifactory.co.uk/newsletter/2007_01_neg_plausibility.htm)*. [AI Factory](/AI_Factory "AI Factory"), Spring 2007 [[10]](#cite_note-10)

# Forum Posts

## 1995 ...

- [(depth \* depth) to replace (1 << depth)](https://groups.google.com/d/msg/rec.games.chess.computer/1uVIWZFB41k/qkPxZjtcFWwJ) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 29, 1996
- [Killer and history](https://www.stmintz.com/ccc/index.php?id=21072) by [Jan Willem de Kort](/index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [CCC](/CCC "CCC"), June 22, 1998
- [History Heuristic on its own](https://www.stmintz.com/ccc/index.php?id=39692) by [Chris Moreton](/Chris_Moreton "Chris Moreton"), [CCC](/CCC "CCC"), January 16, 1999
- [What is the History table?](https://www.stmintz.com/ccc/index.php?id=68832) by [Leonid](/Leonid_Liberman "Leonid Liberman"), [CCC](/CCC "CCC"), September 15, 1999

## 2000 ...

- [What is the Success Rate of Killer/History Moves?](https://www.stmintz.com/ccc/index.php?id=113078) by [Roberto Waldteufel](/Roberto_Waldteufel "Roberto Waldteufel"), [CCC](/CCC "CCC"), May 31, 2000
- [History Heuristic](https://www.stmintz.com/ccc/index.php?id=127122) by Larry Griffiths, [CCC](/CCC "CCC"), August 28, 2000
- [About history heuristics, killers and my futil. pruning code](https://www.stmintz.com/ccc/index.php?id=143331) by [Severi Salminen](/Severi_Salminen "Severi Salminen"), [CCC](/CCC "CCC"), December 06, 2000 » [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [killers and history](https://www.stmintz.com/ccc/index.php?id=278991) by [Nathan Thom](/Nathan_Thom "Nathan Thom"), [CCC](/CCC "CCC"), January 22, 2003 » [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [quiescent nodes, and history heuristic...](https://www.stmintz.com/ccc/index.php?id=280447) by [Joel Veness](/Joel_Veness "Joel Veness"), [CCC](/CCC "CCC"), January 30, 2003
- [History Heuristic](https://www.stmintz.com/ccc/index.php?id=354812) by [Renze Steenhuisen](/Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](/CCC "CCC"), March 16, 2004
- [About history and aging it](https://www.stmintz.com/ccc/index.php?id=355221) by [Mikael Bäckman](/Mikael_B%C3%A4ckman "Mikael Bäckman"), [CCC](/CCC "CCC"), March 17, 2004
- [History heuristic](https://www.stmintz.com/ccc/index.php?id=355347) by [Sergei S. Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), March 18, 2004
- [Re: Artificial Intelligence in Computer Chess - \*DETAILS\* as promised](https://www.stmintz.com/ccc/index.php?id=357112) by [Artem Pyatakov](/Artem_Petakov "Artem Petakov"), [CCC](/CCC "CCC"), March 28, 2004 » [Artificial Intelligence](/Artificial_Intelligence "Artificial Intelligence"), [Golch](/Golch "Golch")

## 2005 ...

- [Improving history tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=15337) by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), [CCC](/CCC "CCC"), July 25, 2007
- [LMR: history or not?](https://www.talkchess.com/forum/viewtopic.php?t=18345) by [Alessandro Scotti](/Alessandro_Scotti "Alessandro Scotti"), [CCC](/CCC "CCC"), December 13, 2007
- [killer moves and history heuristic table](http://www.talkchess.com/forum/viewtopic.php?t=24920) by [Stuart Cracraft](/Stuart_Cracraft "Stuart Cracraft"), [CCC](/CCC "CCC"), November 17, 2008 » [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [Alternatives to History Heuristics](http://www.talkchess.com/forum/viewtopic.php?t=29611) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), September 01, 2009

## 2010 ...

- [dynamically modified evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=37191) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), December 20, 2010
- [Software Engineering](http://www.talkchess.com/forum/viewtopic.php?t=38406) by [Onno Garms](/Onno_Garms "Onno Garms"), [CCC](/CCC "CCC"), March 13, 2011 » [Toga](/Toga "Toga")
- [On history counters again](http://www.talkchess.com/forum/viewtopic.php?t=40229) by [Mincho Georgiev](/Mincho_Georgiev "Mincho Georgiev"), [CCC](/CCC "CCC"), August 31, 2011
- [Killer and History: Increased Node Count](http://www.talkchess.com/forum/viewtopic.php?t=46886) by [Cheney Nattress](/index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](/CCC "CCC"), January 15, 2013
- [On history and piece square tables](http://www.talkchess.com/forum/viewtopic.php?t=48102) by [Evert Glebbeek](/Evert_Glebbeek "Evert Glebbeek"), [CCC](/CCC "CCC"), May 24, 2013 » [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Possible history table improvement](http://www.talkchess.com/forum/viewtopic.php?t=48160) by [Laszlo Gaspar](/index.php?title=L%C3%A1szl%C3%B3_G%C3%A1sp%C3%A1r&action=edit&redlink=1 "László Gáspár (page does not exist)"), [CCC](/CCC "CCC"), May 30, 2013
- [Improved history heuristic](http://www.talkchess.com/forum/viewtopic.php?t=50512) by [Sergei S. Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), December 16, 2013
- [Followup moves](https://groups.google.com/d/msg/fishcooking/d8IhZZJSBGc/PrN-8dP26dIJ) by [Stefan Geschwentner](/Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), January 12, 2014 » [Counter Moves History](/History_Heuristic#CMHist "History Heuristic")
- [Recalculate history for remaining moves after each search](http://www.talkchess.com/forum/viewtopic.php?t=51106) by [Sergei S. Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), January 30, 2014
- [Idea of different history](http://www.talkchess.com/forum/viewtopic.php?t=51992) by [Daniel José Queraltó](/Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](/CCC "CCC"), April 14, 2014

## 2015 ...

- [Improving History Tables](http://www.talkchess.com/forum/viewtopic.php?t=55535) by [Bill Henry](/Bill_Henry "Bill Henry"), [CCC](/CCC "CCC"), March 02, 2015
- [History counters](http://www.talkchess.com/forum/viewtopic.php?t=56332) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), May 12, 2015
- [History heuristic and fixed depth search](http://www.talkchess.com/forum/viewtopic.php?t=56372) by [Peter Österlund](/Peter_%C3%96sterlund "Peter Österlund"), [CCC](/CCC "CCC"), May 16, 2015 » [Late Move Reduction Test Results](/Late_Move_Reduction_Test_Results "Late Move Reduction Test Results"), [Texel](/Texel "Texel")
- [History Heuristic - a new idea on an old idea?](http://www.open-chess.org/viewtopic.php?f=5&t=2917) by thevinenator, [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), Novembere 19, 2015
- [Re: Stockfish 7 progress](http://www.talkchess.com/forum/viewtopic.php?t=58935&start=2) by Lucas Braesch, [CCC](/CCC "CCC"), January 17, 2016
- [History heuristic and quiet move generation](http://www.talkchess.com/forum/viewtopic.php?t=64619) by [Daniel José Queraltó](/Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](/CCC "CCC"), July 16, 2017 » [Move Generation](/Move_Generation "Move Generation")
- [CMH question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72531) by [Vivien Clauzon](/Vivien_Clauzon "Vivien Clauzon"), [CCC](/CCC "CCC"), December 08, 2019 » [Counter Moves History](#CMHist)

## 2020 ...

- [Quick history move](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73880) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), May 09, 2020
- [History bonus](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76540) by [Michael Hoffmann](/Michael_Hoffmann "Michael Hoffmann"), [CCC](/CCC "CCC"), February 09, 2021

# External Links

- [History Reductions](https://web.archive.org/web/20180713063523/http://members.home.nl/matador/hr.htm) from [Ed Schröder's](/Ed_Schroder "Ed Schroder") [Programmer Corner](http://members.home.nl/matador/stuff.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), July 30, 2007)
- [Killer heuristic from Wikipedia](https://en.wikipedia.org/wiki/Killer_heuristic)

# References

1. [↑](#cite_ref-1) [Alfred Agache](/Category:Alfred_Agache "Category:Alfred Agache") - Alegoria da Fortuna, 1885, [Palais des Beaux-arts](https://en.wikipedia.org/wiki/Palais_des_Beaux-Arts_de_Lille), [Lille](https://en.wikipedia.org/wiki/Lille), [Category:Alfred Agache - Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Alfred_Agache)
2. [↑](#cite_ref-2) [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") (**1983**). *The History Heuristic*. [ICCA Journal, Vol. 6, No. 3](/ICGA_Journal#6_3 "ICGA Journal")
3. [↑](#cite_ref-3) [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *Memory Efficiency in some Heuristics*. [ICCA Journal, Vol. 15, No. 2](/ICGA_Journal#15_2 "ICGA Journal")
4. [↑](#cite_ref-4) [Move Ordering in Rebel](https://web.archive.org/web/20070927195511/members.home.nl/matador/chess840.htm#MOVE%20ORDERING) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), also available as [pdf](https://silo.tips/download/how-rebel-plays-chess-1)
5. [↑](#cite_ref-5) [Improving History Tables](http://www.talkchess.com/forum/viewtopic.php?t=55535) by [Bill Henry](/Bill_Henry "Bill Henry"), [CCC](/CCC "CCC"), March 02, 2015
6. [↑](#cite_ref-6) [Re: Improving History Tables](http://www.talkchess.com/forum/viewtopic.php?t=55535&start=2) by [Álvaro Begué](/%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](/CCC "CCC"), March 02, 2015
7. [↑](#cite_ref-7) [Followup moves](https://groups.google.com/d/msg/fishcooking/d8IhZZJSBGc/PrN-8dP26dIJ) by [Stefan Geschwentner](/Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), January 12, 2014 » [Counter Moves History](/History_Heuristic#CMHist "History Heuristic")
8. [↑](#cite_ref-8) [Re: Stockfish 7 progress](http://www.talkchess.com/forum/viewtopic.php?t=58935&start=2) by Lucas Braesch, [CCC](/CCC "CCC"), January 17, 2016
9. [↑](#cite_ref-9) [Re: CMH question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72531&start=1) by Lucas Braesch, [CCC](/CCC "CCC"), December 09, 2019
10. [↑](#cite_ref-10) [Negative Plausibility Move Ordering](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=28873) by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), [CCC](/CCC "CCC"), July 09, 2009

**[Up one Level](/Move_Ordering "Move Ordering")**