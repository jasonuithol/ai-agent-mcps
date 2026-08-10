# Guard Heuristic

Source: https://www.chessprogramming.org/Guard_Heuristic

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Move Ordering](/Move_Ordering "Move Ordering") \* Guard Heuristic**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Bob_Cousy_NYWTS.jpg/330px-Bob_Cousy_NYWTS.jpg)](/File:Bob_Cousy_NYWTS.jpg)

Point guard [[1]](#cite_note-1)

**Guard Heuristic**,  
a move ordering and [pruning](/Pruning "Pruning") heuristic introduced by [Yi-Fan Ke](/Yi-Fan_Ke "Yi-Fan Ke") and [Tai-Ming Parng](/Tai-Ming_Parng "Tai-Ming Parng") in the 1993 [ICCA Journal, Vol. 16, No. 2](/ICGA_Journal#16_2 "ICGA Journal") [[2]](#cite_note-2) . The guard heuristic was successfully applied in [chinese chess](/Chinese_Chess "Chinese Chess") and compared with the other heuristics such as the [killer heuristic](/Killer_Heuristic "Killer Heuristic"), and also proposed for chess. A similar move ordering algorithm was mentioned by [Carl Ebeling](/Carl_Ebeling "Carl Ebeling") in his 1986 Ph.D. thesis *All the Right Moves* [[3]](#cite_note-3) , utilizing the [value](/Point_Value "Point Value") of the moving piece, the value of the captured piece if any, and the value of the piece and pawn guards. In contrast, the guard heuristics is based on the **guard value** of each [square](/Squares "Squares"), and considers those values not only for [target squares](/Target_Square "Target Square") but also for [origin squares](/Origin_Square "Origin Square") of moves to decide whether the move is searched at all, with a [reduced](/Reductions "Reductions") [depth](/Depth "Depth"), or when.

# Guard Values

The guard value of a square is the sum of the capture strengths (CS) of those pieces that are able to capture a potential opponent piece on that square. The capture strength of a piece is roughly inverse proportional to its [point value](/Point_Value "Point Value"), in white point of view metric, positive values for white and negative values for black. Further, if the square is occupied by a defended black piece, and target of a capture, the (negative) capture strength of that piece is added to the guard value as well.

## Pseudo-Code

```
int guardValueWPOV(enumSquare sq) {
  isAttacked = false;
  isDefended = false;
  int gv = 0;
  for ( all Pieces p controlling sq ) {
    gv += captureStrength[p];
    if ( isWhitePiece (p) )
      isAttacked = true;
    else
      isDefended = true;
  }
  if ( isAttacked && isDefended ) {
    p = board[sq];
    if ( isBlackPiece (p) )
      gv += captureStrength[p];
  }
  return gv;
}
```

## Capture Strength

### Chess

|  | King | Queen | Rook | Bishop | Knight | Pawn |
| --- | --- | --- | --- | --- | --- | --- |
| White | +1 | +1 | +2 | +5 | +6 | +9 |
| Black | -1 | -1 | -2 | -5 | -6 | -9 |

### Chinese Chess

|  | General | Guard | Elephant | Warrior | Horse | Cannon | Soldier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| White | +1 | +9 | +9 | +2 | +5 | +4 | +9 |
| Black | -1 | -9 | -9 | -2 | -5 | -4 | -9 |

# Pruning and Ordering

The guard heuristic aims at both rejecting moves at deep nodes and ordering moves to reduce the search time. Moves with unsafe target squares, that is negative guard values less some margin, are pruned near the tips and the remaining moves are ordered by the **Escape-first-if-origin-unsafe**, giving priority for most valuable piece, and **Capture-first-if-target-safe** rules, considering [MVV-LVA](/MVV-LVA "MVV-LVA").

# See also

- [Chessmaps Heuristic](/Chessmaps_Heuristic "Chessmaps Heuristic")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [MVV-LVA](/MVV-LVA "MVV-LVA")
- [Pruning](/Pruning "Pruning")
- [Square Attacked By](/Square_Attacked_By "Square Attacked By")
- [Square Control](/Square_Control "Square Control")
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")

# Publications

- [Yi-Fan Ke](/Yi-Fan_Ke "Yi-Fan Ke"), [Tai-Ming Parng](/Tai-Ming_Parng "Tai-Ming Parng") (**1993**). *The Guard Heuristic: Legal Move Ordering with Forward Game-Tree Pruning*. [ICCA Journal, Vol. 16, No. 2](/ICGA_Journal#16_2 "ICGA Journal")
- [Mei-En Chen](/index.php?title=Mei-En_Chen&action=edit&redlink=1 "Mei-En Chen (page does not exist)"), [Yo-Ping Huang](/index.php?title=Yo-Ping_Huang&action=edit&redlink=1 "Yo-Ping Huang (page does not exist)") (**1995**). *[Guard heuristic by dynamic fuzzy reasoning model for Chinese chess](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=527751)*. Proceedings of ISUMA-NAFIPS '95

# Forum Posts

- [Bonus for "null move SEE"](http://www.talkchess.com/forum/viewtopic.php?t=57346) by [Matthew Lai](/Matthew_Lai "Matthew Lai"), [CCC](/CCC "CCC"), August 23, 2015

# External Links

- [Guard from Wikipedia](https://en.wikipedia.org/wiki/Guard)
- [John McLaughlin](/Category:John_McLaughlin "Category:John McLaughlin") and [Jonas Hellborg](/Category:Jonas_Hellborg "Category:Jonas Hellborg") - Guardian Angel - [You Know You Know](/Knowledge#youknow "Knowledge"), [Fabrik Hamburg](https://en.wikipedia.org/wiki/Fabrik_%28Hamburg%29), February 19, 1987, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Point guards [Bob Cousy](https://en.wikipedia.org/wiki/Bob_Cousy) (left) and [Bob McNeill](https://en.wikipedia.org/wiki/Bob_McNeill) (center) chase after the ball. Cousy won six [NBA](https://en.wikipedia.org/wiki/National_Basketball_Association) championships with the [Boston Celtics](https://en.wikipedia.org/wiki/Boston_Celtics), Description: "[Life in the old Cousy yet](http://www.loc.gov/pictures/item/94505330/)", [New York World-Telegram & Sun](https://en.wikipedia.org/wiki/New_York_World-Telegram) photo by Wm. C. Greene, 1960, [Library of Congress](https://en.wikipedia.org/wiki/Library_of_Congress), Prints and Photographs Division, [Point guard from Wikipedia](https://en.wikipedia.org/wiki/Point_guard), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Yi-Fan Ke](/Yi-Fan_Ke "Yi-Fan Ke"), [Tai-Ming Parng](/Tai-Ming_Parng "Tai-Ming Parng") (**1993**). *The Guard Heuristic: Legal Move Ordering with Forward Game-Tree Pruning*. [ICCA Journal, Vol. 16, No. 2](/ICGA_Journal#16_2 "ICGA Journal")
3. [↑](#cite_ref-3) [Carl Ebeling](/Carl_Ebeling "Carl Ebeling") (**1986**). *[All the Right Moves: A VLSI Architecture for Chess](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=7692)*. Ph.D. thesis, [Carnegie Mellon University](/Carnegie_Mellon_University "Carnegie Mellon University"), [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)

**[Up one Level](/Move_Ordering "Move Ordering")**