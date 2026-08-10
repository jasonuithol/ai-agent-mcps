# Blockage Detection

Source: https://www.chessprogramming.org/Blockage_Detection

**[Home](/Main_Page "Main Page") \* [Knowledge](/Knowledge "Knowledge") \* [Pattern Recognition](/Pattern_Recognition "Pattern Recognition") \* Blockage Detection**

|  |  |  |
| --- | --- | --- |
| **Blockage Detection**,  a pattern recognition technique to statically discover [rammed positions](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)") in [pawn endgames](/Pawn_Endgame "Pawn Endgame"), and permanently prevented kings from penetrating into opponent's camp. In those positions material advantage is not sufficient to win such games, otherwise only recognizably by a very deep [search](/Search "Search"), when a [draw](/Draw "Draw") by [fifty-move rule](/Fifty-move_Rule "Fifty-move Rule") rises the horizon. Best not only applied in [leaf node](/Leaf_Node "Leaf Node") [evaluation](/Evaluation "Evaluation"), but as [interior node recognizer](/Interior_Node_Recognizer "Interior Node Recognizer") within the [search](/Search "Search"), a detected blockade either [prunes](/Pruning "Pruning") forward or narrows the [search window](/Window "Window"). | |  | | --- | |                                                                                    ♚                ♟♙♟    ♟ ♙ ♙ ♟  ♙     ♙      ♙      ♔ | |

# Search Application

Blockage detection is only applied for the side with advantage, proving its [upper bound](/Upper_Bound "Upper Bound") is a [draw score](/Score#DrawScore "Score") [[1]](#cite_note-1):

```
int search(int alpha, int beta, ...) {
  ...
  /* blockade detection */
  if ( beta > DRAW_SCORE ) {
    if ( blockage() ) {
      if ( alpha >= DRAW_SCORE )
        return DRAW_SCORE;
      beta = DRAW_SCORE; 
    }    
  }
  /* continue regular search */
}
```

# Ram Fence

*Following sample assumes White the "winning" side to move*

The blockage requires a fence consisting of own fixed pawns and opponent [pawn attacks](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)"), to divide the board into two disconnected regions. There are various algorithms to deal with fence detection, and fixed and dynamic pawns, following [fill based](/Fill_Algorithms "Fill Algorithms") proposal deals with [bitboards](/Bitboards "Bitboards") and should only take none [lever pawns](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)") into account to prove the fence is impenetrable. First cheap condition is the presence of at least three [rams](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)"). Further own pawns blocked by own rams are included successively into the fence set, and finally opponent pawn attacks. The precondition, the defending king has at least one vacant square to avoid [zugzwang](/Zugzwang "Zugzwang") issues, is omitted.

A [king flood](/King_Pattern#FloodFillAlgorithms "King Pattern") starts at its base rank (1st rank for White) over the board (ignoring black passers on the 2rd rank), or all bits below the fence' [least significant one bit](/General_Setwise_Operations#LS1BSeparation "General Setwise Operations"), the potential fence as flood stopping obstruction. If, after a few cycles, the flood reaches the above area, the fence is penetrable, and the blockage test failed. Each time, the king flood drowns (undefended) opponent pawns, the ram-fence is re-calculated with the drown pawns "captured". If the flood does not grow anymore, the fence is detected.

*see [One Step](/General_Setwise_Operations#OneStepOnly "General Setwise Operations"), [Population Count](/Population_Count "Population Count") and [BitScan](/BitScan "BitScan")*

```
bool forms_fence4white(U64 wPawns, U64 bPawns, U64 &fence, U64 &flood) {
  fence = wPawns & soutOne( bPawns ); 
  if (popCount( fence ) < 3)
    return false;
  fence |= wPawns & soutOne( fence );
  fence |= wPawns & soutOne( fence );
  fence |= wPawns & soutOne( fence );
  fence |= wPawns & soutOne( fence );
  fence |= bPawnAttacks( bPawns );
  flood = RANK1BB | allBitsBelow[BitScanForward( fence )];
  U64 above = allBitsAbove[BitScanReverse( fence )];
  while ( true ) {
    U64 temp = flood;
    flood |= eastOne( flood ) | westOne( flood ); /* Set all 8 neighbors */
    flood |= soutOne( flood ) | nortOne( flood );
    flood &= ~fence;
    if (flood == temp) 
      break; /* Fill has stopped, blockage? */
    if (flood & above) /* break through? */
      return false; /* yes, no blockage */
    if (flood & bPawns) {
      bPawns &= ~flood;  /* "capture" undefended black pawns */
      fence = wPawns & soutOne( bPawns ); 
      if (popCount( fence ) < 3)
        return false;
      fence |= wPawns & soutOne( fence );
      fence |= wPawns & soutOne( fence );
      fence |= wPawns & soutOne( fence );
      fence |= wPawns & soutOne( fence );
      fence |= bPawnAttacks( bPawns );
    }
  } 
  return true;
}
```

In order to ensure that White cannot penetrate the fence, the white kings must reside in the below flood set, and the defending, black king outside the below set. If all pawns of the "winning" side are rammed without any [lever](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)"), the most obvious case of a blockage is recognized.

```
. . . k . . . .         a a a a a a a a
. . . . . . . .  above  a a a a a a a a
. . . . . . . .         a a a a a a a a
. b . . b . . b         a a a a a a a a
. w . . w . . w  fence  F_F_F_F_F_F_F_F
. w . . . . . .         b f b b b b b b
. . . K . . . .  below  b b b b b b b b
. . . . . . . .  flood  b b b b b b b b
```

# Blockage with Dynamic Pawns

Otherwise, one has to consider dynamic pawns of the "winning" side, able to [push forward](/Pawn_Push "Pawn Push") or to [capture](/Captures "Captures"), in particular above the fence, as member of the fence (levers) and below the fence (from White's point of view). For instance, one ([protected](/Protected_Passed_Pawn "Protected Passed Pawn")) [passed pawn](/Passed_Pawn "Passed Pawn"), with the defending king on its [front span](/Pawn_Spans "Pawn Spans"), is not sufficient to break the blockage. Similar holds for pawns below the fence not able to lever, and becoming rammed if moving forward, or with some care, most [backward pawns](/Backward_Pawn "Backward Pawn").

```
. . . . k . . .         a a a a a a a a
. . . . . . . .  above  a a a a a a a a
. . . b w b . .         a a a a a a a a
. b . w . w . b         a a F_F_F_F_F a
. w . . . . . w  fence  F_F_F b b b F_F
. . . . . w . .         b b b b b b b b
. . . K . . . .  below  b b b b b b b b
. . . . . . . .  flood  b b b b b b b b
```

More complicated cases for a successful blockage detection also with levers involved are elaborated in [Omid David's](/Eli_David "Eli David") et al. 2004 [ICGA Journal](/ICGA_Journal "ICGA Journal") paper [[2]](#cite_note-2), also published as code of [Chiron](/Chiron "Chiron") by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina") in [CCC](/CCC "CCC") [[3]](#cite_note-3).

# See also

- [Computer Judgment](/Arthur#Computer_Judgment "Arthur")
- [Corresponding Squares](/Corresponding_Squares "Corresponding Squares")
- [Draw Evaluation](/Draw_Evaluation "Draw Evaluation")
- [Flood Fill Algorithm](/King_Pattern#FloodFillAlgorithms "King Pattern")
- [Fortress](/Fortress "Fortress")
- [Interior Node Recognizer](/Interior_Node_Recognizer "Interior Node Recognizer")
- [Pattern Recognition](/Pattern_Recognition "Pattern Recognition")
- [Chunking](/Chunking "Chunking")

# Publications

- [Peter W. Frey](/Peter_W._Frey "Peter W. Frey"), [Larry Atkin](/Larry_Atkin "Larry Atkin") (**1979**). *[Creating a Chess-Player, Part 4: Thoughts on Strategy](https://archive.org/stream/byte-magazine-1979-01/1979_01_BYTE_04-01_Life_Algorithms#page/n127/mode/2up)*. In [Blaise W. Liffick](http://cs.millersville.edu/~liffick/) (ed.), [The Byte Book of Pascal](http://books.google.com/books/about/The_BYTE_book_of_Pascal.html?id=ofpfQgAACAAJ), pp. 143-155. Byte Publications, also [BYTE, Vol. 4, No. 1](/Byte_Magazine#BYTE401 "Byte Magazine")
- [Walter Ravenek](/Walter_Ravenek "Walter Ravenek") (**1995**). *Computer Judgment*. [Computer Chess Reports](/Computer_Chess_Reports "Computer Chess Reports"), Vol. 5, Nos. 3+4, pp. 124 » [Computer Judgment](/Arthur#Computer_Judgment "Arthur")
- [Omid David](/Eli_David "Eli David"), [Ariel Felner](/Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](/Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *[Blockage Detection in Pawn Endings](http://link.springer.com/chapter/10.1007/11674399_13)*. [CG 2004](/CG_2004 "CG 2004"), [pdf](http://www.ise.bgu.ac.il/faculty/felner/newsite/publications/blockage.pdf)
- [Omid David](/Eli_David "Eli David"), [Ariel Felner](/Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](/Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *Blockage Detection in Pawn Endgames*. [ICGA Journal, Vol. 27, No. 3](/ICGA_Journal#27_3 "ICGA Journal")

# Forum Posts

- [Re: Computer Judgment](https://groups.google.com/d/msg/rec.games.chess.computer/DIrf0yWFh-c/hwz26K3gqHAJ) by [Walter Ravenek](/Walter_Ravenek "Walter Ravenek"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 25, 1995 » [Computer Judgment](/Arthur#Computer_Judgment "Arthur")
- [Endgame Blockage Positions](https://www.stmintz.com/ccc/index.php?id=269253) by [Omid David](/Eli_David "Eli David"), [CCC](/CCC "CCC"), December 06, 2002
- [Jeremiah's Wall Detection](https://www.stmintz.com/ccc/index.php?id=423308) by [Renze Steenhuisen](/Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](/CCC "CCC"), April 28, 2005
- [Code of Chiron for Detection of Pawn Blockages](http://www.talkchess.com/forum/viewtopic.php?t=40748) by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [CCC](/CCC "CCC"), October 13, 2011
- [To users of Chiron](http://www.talkchess.com/forum/viewtopic.php?t=41740) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), January 02, 2012
- [Details about Critter 1.4a.](http://www.talkchess.com/forum/viewtopic.php?t=42385&start=16) by [Jesús Muñoz](/index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](/CCC "CCC"), February 10, 2012 » [Critter](/Critter "Critter")
- [Fortress detection?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77768) by [Martin Fierz](/Martin_Fierz "Martin Fierz"), [CCC](/CCC "CCC"), July 21, 2021 » [Checkers](/Checkers "Checkers")

# References

1. [↑](#cite_ref-1) Code snippet from [Omid David](/Eli_David "Eli David"), [Ariel Felner](/Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](/Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *[Blockage Detection in Pawn Endings](http://link.springer.com/chapter/10.1007/11674399_13)*. [CG 2004](/CG_2004 "CG 2004"), [pdf](http://www.ise.bgu.ac.il/faculty/felner/newsite/publications/blockage.pdf)
2. [↑](#cite_ref-2) [Omid David](/Eli_David "Eli David"), [Ariel Felner](/Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](/Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *Blockage Detection in Pawn Endgames*. [ICGA Journal](/ICGA_Journal "ICGA Journal"), Vol. 27, No. 3
3. [↑](#cite_ref-3) [Code of Chiron for Detection of Pawn Blockages](http://www.talkchess.com/forum/viewtopic.php?t=40748) by [Ubaldo Andrea Farina](/Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [CCC](/CCC "CCC"), October 13, 2011

**[Up one level](/Pattern_Recognition "Pattern Recognition")**