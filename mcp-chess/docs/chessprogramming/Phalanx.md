# Phalanx

Source: https://www.chessprogramming.org/Phalanx

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Phalanx**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Greek_Phalanx.jpg/330px-Greek_Phalanx.jpg)](/File:Greek_Phalanx.jpg)

Greek Phalanx [[1]](#cite_note-1)

**Phalanx**,  
an [open source chess engine](/Category:Open_Source "Category:Open Source"), originally released by a Czech student [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš") under [GPL](/Free_Software_Foundation#GPL "Free Software Foundation"), also available as [Young Talent](/ChessBase#YoungTalents "ChessBase") by [ChessBase](/ChessBase "ChessBase") running under the [Fritz6 GUI](/Fritz#FritzGUI "Fritz"). In about 2000 the project has been abandoned [[2]](#cite_note-2) , but it was resurrected in 2006 by [José de Paula Rodrigues](/index.php?title=Jos%C3%A9_de_Paula_Rodrigues&action=edit&redlink=1 "José de Paula Rodrigues (page does not exist)") [[3]](#cite_note-3) [[4]](#cite_note-4). In October 2014, after fourteen years and nine months, Phalanx XXIII was released by Dušan Dobeš [[5]](#cite_note-5).

# Description

Phalanx's board is [represented](/Board_Representation "Board Representation") by a [10x12 mailbox](/10x12_Board "10x12 Board") with [piece-lists](/Piece-Lists "Piece-Lists"). The [search](/Search "Search") uses [PVS](/Principal_Variation_Search "Principal Variation Search") with [transposition table](/Transposition_Table "Transposition Table") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") centiply framework for [fractional extensions](/Extensions#FractionalExtensions "Extensions") and [reductions](/Reductions "Reductions") without [aspiration windows](/Aspiration_Windows "Aspiration Windows"), performing state of the art [null move pruning](/Null_Move_Pruning "Null Move Pruning"), [late move reductions](/Late_Move_Reductions "Late Move Reductions") and [futility pruning](/Futility_Pruning "Futility Pruning") near the tips. Phalanx pioneered in [tapered eval](/Tapered_Eval "Tapered Eval") and speculatively computes both [endgame](/Endgame "Endgame") and [middlegame](/Middlegame "Middlegame") [scores](/Score "Score") to balance them by total [material](/Material "Material"). This prevents [evaluation discontinuity](/Evaluation_Discontinuity "Evaluation Discontinuity") when searching a position on the edge of middlegame and endgame. The [static evaluation](/Evaluation "Evaluation") first extracts knowledge and prepares a [color flipped](/Color_Flipping "Color Flipping") board, and applies that knowledge in a second pass using the flipped board to do stuff for both sides with the same color independent code.

# Quotes

by [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš") from [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), July 16, 1998 [[6]](#cite_note-6) :

```
Phalanx is my hobby project. It started in March 1997. It's developed under Linux and GCC, I also prepared binary distribution for Win32 with latter versions. Licensing policy is GPL (free and in sources). Interface is xboard/winboard/RoboFICS compatible. It plays on FICS as 'pikozrout', it's current blitz rating is 2380, standard 2210.
```

# Forum Posts

## 1997 ...

- [Phalanx III - chess playing program for Linux](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/dba5dc4e35dae67) by [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), July 08, 1997
- [Phalanx ?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7ab1751bddacb97a#) by [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), July 16, 1998

## 2000 ...

- [Phalanx is dead?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a56fb4fa7b0d427b) by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 27, 2002
- [Phalanx XXII - Reborn](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/3819371b750533f1#) by [José de Paula Rodrigues](/index.php?title=Jos%C3%A9_de_Paula_Rodrigues&action=edit&redlink=1 "José de Paula Rodrigues (page does not exist)"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 19, 2006

## 2010 ...

- [Phalanx source code](http://www.talkchess.com/forum/viewtopic.php?t=42398) by [Carlos Pesce](/Carlos_Pesce "Carlos Pesce"), [CCC](/CCC "CCC"), February 09, 2012
- [New Phalanx code](http://www.talkchess.com/forum/viewtopic.php?t=52127) by [Steven Atkinson](/Steven_Atkinson "Steven Atkinson"), [CCC](/CCC "CCC"), April 26, 2014
- [Phalanx XXIII](http://www.talkchess.com/forum/viewtopic.php?t=54098) by [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš"), [CCC](/CCC "CCC"), October 20, 2014
- [Phalanx XXIV](http://www.talkchess.com/forum/viewtopic.php?t=54744) by [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš"), [CCC](/CCC "CCC"), December 24, 2014
- [Phalanx XXV](http://www.talkchess.com/forum/viewtopic.php?t=60019) by [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš"), [CCC](/CCC "CCC"), May 01, 2016

# External Links

## Chess Engine

- [Phalanx Chess | Free software downloads at SourceForge.net](https://sourceforge.net/projects/phalanx/)
- [Phalanx Chess at SourceForge.net](https://sourceforge.net/projects/phalanx/files/)
- [phalanx from SourceForge.net](http://phalanx.sourceforge.net/)
- [Phalanx](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Phalanx&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")
- [Young Talents, Teil 2](http://scleinzell.schachvereine.de/p_spielprogramme/youngtal_b.shtml) by [Peter Schreiner](/Peter_Schreiner "Peter Schreiner"), Mai 2000, hosted by [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml) (German)

## Misc

- [phalanx - Wiktionary](https://en.wiktionary.org/wiki/phalanx)
- [Phalanx disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/Phalanx)
- [Phalanx formation from Wikipedia](https://en.wikipedia.org/wiki/Phalanx_formation)
- [Close order formation from Wikipedia](https://en.wikipedia.org/wiki/Close_order_formation)
- [Phalanx](https://en.wikipedia.org/wiki/Phalanx_(band)) - Where Did All The Girls Come From, [East Berlin](https://en.wikipedia.org/wiki/East_Berlin) 1985, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   lineup: [James Blood Ulmer](https://en.wikipedia.org/wiki/James_Blood_Ulmer), [George Adams](https://en.wikipedia.org/wiki/George_Adams_(musician)), [Amin Ali](https://de.wikipedia.org/wiki/Amin_Ali), [Calvin Weston](https://de.wikipedia.org/wiki/Calvin_Weston)

# References

1. [↑](#cite_ref-1) An [EDSITEment-reconstructed](http://edsitement.neh.gov/edsitements-persian-wars-resource-pages#node-20463) Greek phalanx based on sources from [The Perseus Project](https://en.wikipedia.org/wiki/Perseus_Project), [Phalanx formation from Wikipedia](https://en.wikipedia.org/wiki/Phalanx_formation)
2. [↑](#cite_ref-2) [Phalanx is dead?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a56fb4fa7b0d427b) by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 27, 2002
3. [↑](#cite_ref-3) [Phalanx XXII - Reborn](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/3819371b750533f1#) by [José de Paula Rodrigues](/index.php?title=Jos%C3%A9_de_Paula_Rodrigues&action=edit&redlink=1 "José de Paula Rodrigues (page does not exist)"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 19, 2006
4. [↑](#cite_ref-4) [José de Paula](http://sourceforge.net/users/espinafre/) from [SourceForge.net](http://sourceforge.net/)
5. [↑](#cite_ref-5) [Phalanx XXIII](http://www.talkchess.com/forum/viewtopic.php?t=54098) by [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš"), [CCC](/CCC "CCC"), October 20, 2014
6. [↑](#cite_ref-6) [Phalanx ?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7ab1751bddacb97a#) by [Dušan Dobeš](/Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), July 16, 1998

**[Up one Level](/Engines "Engines")**