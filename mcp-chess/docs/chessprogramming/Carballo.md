# Carballo

Source: https://www.chessprogramming.org/Carballo

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Carballo**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Storkeegen_by_A._Schovelin_1914.jpg/330px-Storkeegen_by_A._Schovelin_1914.jpg)](/File:Storkeegen_by_A._Schovelin_1914.jpg)

Storkeegen [[1]](#cite_note-1)

**Carballo**,  
an [open source chess engine](/Category:Open_Source "Category:Open Source") by [Alberto Alonso Ruibal](/Alberto_Alonso_Ruibal "Alberto Alonso Ruibal"), written in [Java](/Java "Java"),
licensed under the [GNU General Public License](/Free_Software_Foundation#GPL "Free Software Foundation"), and first released in 2009 [[2]](#cite_note-2).
Carballo supports the [UCI](/UCI "UCI") protocol, and a [HTML5](https://en.wikipedia.org/wiki/HTML5) based [GUI](/GUI "GUI") dubbed [Mobialia Chess](/index.php?title=Mobialia_Chess&action=edit&redlink=1 "Mobialia Chess (page does not exist)") [[3]](#cite_note-3), developed by [Lukas Laag](/index.php?title=Lukas_Laag&action=edit&redlink=1 "Lukas Laag (page does not exist)") with the [Google Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit) (GWT) using the *Vectomatic SVG* library [[4]](#cite_note-4) [[5]](#cite_note-5).
Carballo features [pondering](/Pondering "Pondering"), a [PolyGlot](/PolyGlot "PolyGlot") [opening book](/Opening_Book "Opening Book"), and since version 1.2, [Chess960](/Chess960 "Chess960"). [Karballo](/index.php?title=Karballo&action=edit&redlink=1 "Karballo (page does not exist)") is a [Kotlin](https://en.wikipedia.org/wiki/Kotlin_(programming_language)) version of Carballo [[6]](#cite_note-6) [[7]](#cite_note-7).

# Etymology

Carballo is actually a [Galician](https://en.wikipedia.org/wiki/Galician_language) word meaning [oak](https://en.wikipedia.org/wiki/Oak), it's all about [search trees](/Search_Tree "Search Tree") [[8]](#cite_note-8).

# Description

[[9]](#cite_note-9)

## Board Representation

Carballo is a [bitboard](/Bitboards "Bitboards") engine and applies [magic bitboards](/Magic_Bitboards "Magic Bitboards") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks").
[Staged move generation](/Move_Generation#Staged "Move Generation") along with [move ordering](/Move_Ordering "Move Ordering") is controlled by an [iterator](https://en.wikipedia.org/wiki/Iterator) object which gets the next move during [search](/Search "Search"),
and uses [legal move generation](/Move_Generation#Legal "Move Generation"). This is so far implemented by [making](/Make_Move "Make Move") and testing whether [pseudo-legal moves](/Pseudo-Legal_Move "Pseudo-Legal Move") leave the own king in [check](/Check "Check").

## Search

The [search](/Search "Search") performs [alpha-beta](/Alpha-Beta "Alpha-Beta") [PVS](/Principal_Variation_Search "Principal Variation Search") inside the [iterative deepening](/Iterative_Deepening "Iterative Deepening") loop with [aspiration windows](/Aspiration_Windows "Aspiration Windows"), utilizing a [transposition table](/Transposition_Table "Transposition Table") also in [quiescence](/Quiescence_Search "Quiescence Search"), verified and indexed by [Zobrist Keys](/Zobrist_Hashing "Zobrist Hashing"). [Selectivity](/Selectivity "Selectivity") considers the wide range of state of the art techniques.

### Move Ordering

- [History Heuristic](/History_Heuristic "History Heuristic")
- [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic") (4 Slots)
- [MVV-LVA](/MVV-LVA "MVV-LVA")
- [Principal Variation Extraction from TT](/Principal_Variation "Principal Variation")
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation") (SEE)

### Selectivity

- [Check Extensions](/Check_Extensions "Check Extensions") (SEE >= 0)
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
- [Mate Threat Extensions](/Mate_Threat_Extensions "Mate Threat Extensions")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Passed Pawn Extensions](/Passed_Pawn_Extensions "Passed Pawn Extensions")
- [Razoring](/Razoring "Razoring")
- [Quiescence Search](/Quiescence_Search "Quiescence Search") (SEE >= 0)
- [Static Null Move Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")

## Evaluation

The [evaluation](/Evaluation "Evaluation") is designed to plug in various [evaluation functions](/Evaluation_Function "Evaluation Function"). Available are a [simplified evaluation function](/Simplified_Evaluation_Function "Simplified Evaluation Function"), a sophisticated, complete evaluation function, an experimental one, and some dynamic for specialized endgames, such as a [KPK](/KPK "KPK") [bitbases](/Endgame_Bitbases "Endgame Bitbases") [[10]](#cite_note-10). Most important features are listed below.

### Simplified

- [Material Balance](/Material#Balance "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")

### Complete

- [Mobility](/Mobility "Mobility")
- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [King Safety](/King_Safety "King Safety")
- [Tempo Bonus](/Tempo "Tempo")
- [Trapped Pieces](/Trapped_Pieces "Trapped Pieces")

# See also

- [Godot](/Godot "Godot")
- [Karballo](/index.php?title=Karballo&action=edit&redlink=1 "Karballo (page does not exist)")
- [Mobialia Chess](/index.php?title=Mobialia_Chess&action=edit&redlink=1 "Mobialia Chess (page does not exist)")

# Postings

## 2009

- [Carballo (Java UCI) by Alberto Alonso Ruibal](http://www.talkchess.com/forum/viewtopic.php?t=30361) by [Christopher Conkie](/index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [CCC](/CCC "CCC"), October 28, 2009

:   [Re: Carballo (Java UCI)](http://www.talkchess.com/forum/viewtopic.php?t=30361&start=4) by [Alberto Alonso Ruibal](/Alberto_Alonso_Ruibal "Alberto Alonso Ruibal"), [CCC](/CCC "CCC"), October 29, 2009

## 2010 ...

- [A new Carballo 0.5](http://www.talkchess.com/forum/viewtopic.php?t=38788) by Ruxy Sylwyka, [CCC](/CCC "CCC"), April 19, 2011
- [Test Carballo 0.8 JA](http://www.talkchess.com/forum/viewtopic.php?t=48528) by [Pedro Castro](/Pedro_Castro "Pedro Castro"), [CCC](/CCC "CCC"), July 03, 2013
- [Carballo 1.2 Gauntlet for CCRL 40/40](http://www.talkchess.com/forum/viewtopic.php?t=56014) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), April 15, 2015
- [Carballo 1.2 exe](http://www.talkchess.com/forum/viewtopic.php?t=56244) by Arnaud lohéac, [CCC](/CCC "CCC"), May 05, 2015
- [Carballo 1.3 is out](http://www.talkchess.com/forum/viewtopic.php?t=57007) by Arnaud lohéac, [CCC](/CCC "CCC"), July 18, 2015
- [Carballo Chess engines](http://www.talkchess.com/forum/viewtopic.php?t=61579) by Damir Desevac, [CCC](/CCC "CCC"), October 02, 2016
- [Converting Carballo to Kotlin](https://www.alonsoruibal.com/converting-carballo-kotlin/) by [Alberto Alonso Ruibal](/Alberto_Alonso_Ruibal "Alberto Alonso Ruibal"), April 02, 2017

# External Links

## Chess Engine

- [albertoruibal/carballo · GitHub](https://github.com/albertoruibal/carballo)
- [Carballo Chess Engine | SourceForge.net](https://sourceforge.net/projects/carballo/)
- [Index of /chess/engines/Jim Ablett/CARBALLO](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/CARBALLO/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Carballo](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Carballo&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")
- [Carballo](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Carballo&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [Carballo (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Carballo_%28disambiguation%29)
- [Carballo from Wikipedia](https://en.wikipedia.org/wiki/Carballo)
- [Serafin Carballo](http://serafincarballo.com/) con [Abuña Jazz](http://serafincarballo.com/bio.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Storkeegen](https://en.wikipedia.org/wiki/Storkeegen) was (The last living branch on the tree died in 1981) an old [oak](https://en.wikipedia.org/wiki/Oak) ([Quercus robur](https://en.wikipedia.org/wiki/Quercus_robur)) in [Nordskoven](http://horns-herred.dk/page70.html), [Hornsherred](https://en.wikipedia.org/wiki/Hornsherred) near [Jægerspris](https://en.wikipedia.org/wiki/J%C3%A6gerspris) in the northern part of the island of [Zealand](https://en.wikipedia.org/wiki/Zealand), [Denmark](https://en.wikipedia.org/wiki/Denmark). [This drawing](https://commons.wikimedia.org/wiki/File:Storkeegen.jpg) is by [Axel Schovelin](http://da.wikipedia.org/wiki/Axel_Schovelin) and printed in [Troels Frederik Troels-Lund](https://en.wikipedia.org/wiki/Troels_Frederik_Lund) (**1914**). *[Daglivt liv i Norden i det sekstende Aarhundrede](http://runeberg.org/dagligt/)*. Volume 1, 4th Edition, [Egen i Danmark, p. 27](http://runeberg.org/dagligt/1/0079.html), [Roble - Wikipedia.es](https://es.wikipedia.org/wiki/Roble) (Spanish), [Quercus robur](http://commons.wikimedia.org/wiki/Quercus_robur), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Re: Carballo (Java UCI)](http://www.talkchess.com/forum/viewtopic.php?t=30361&start=4) by [Alberto Alonso Ruibal](/Alberto_Alonso_Ruibal "Alberto Alonso Ruibal"), [CCC](/CCC "CCC"), October 29, 2009
3. [↑](#cite_ref-3) [Mobialia Chess - Mobialia](http://www.mobialia.com/apps/chess/)
4. [↑](#cite_ref-4) [lib-gwt-svg « vectomatic](https://www.vectomatic.org/libs/lib-gwt-svg)
5. [↑](#cite_ref-5) [vectomatic - standard dynamic 2D graphics in web browsers - Google Project Hosting](https://code.google.com/archive/p/vectomatic/)
6. [↑](#cite_ref-6) [GitHub - albertoruibal/karballo: A Kotlin Chess Engine](https://github.com/albertoruibal/karballo)
7. [↑](#cite_ref-7) [Converting Carballo to Kotlin](https://www.alonsoruibal.com/converting-carballo-kotlin/) by [Alberto Alonso Ruibal](/Alberto_Alonso_Ruibal "Alberto Alonso Ruibal"), April 02, 2017
8. [↑](#cite_ref-8) [albertoruibal/carballo · GitHub](https://github.com/albertoruibal/carballo)
9. [↑](#cite_ref-9) [carballo/readme.md at master · albertoruibal/carballo · GitHub](https://github.com/albertoruibal/carballo/blob/master/readme.md)
10. [↑](#cite_ref-10) [carballo/core/src/main/java/com/alonsoruibal/chess/evaluation at master · albertoruibal/carballo · GitHub](https://github.com/albertoruibal/carballo/tree/master/core/src/main/java/com/alonsoruibal/chess/evaluation)

**[Up one Level](/Engines "Engines")**