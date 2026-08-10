# Fortress (Engine)

Source: https://www.chessprogramming.org/Fortress_(Engine)

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Fortress**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Buhen3.jpg/330px-Buhen3.jpg)](/File:Buhen3.jpg)

Buhen fortress [[1]](#cite_note-1)

**Fortress**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), written in [C](/C "C"), first released in October 1998. Fortress pioneered in [Rotated Indices](/Rotated_Indices "Rotated Indices"), a deconcentrated version of [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards"). Alessandro once mentioned improving a version of [Schrüfer's](/G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") "most selective" [quiescence search](/Quiescence_Search "Quiescence Search") [[2]](#cite_note-2), found in Schrüfer's Ph.D. thesis *Minimax-Suchen* [[3]](#cite_note-3).

# Technical Details

[[4]](#cite_note-4)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards") [Rotated Indices](/Rotated_Indices "Rotated Indices")

## [Search](/Search "Search")

- [Fail-Soft](/Fail-Soft "Fail-Soft") [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Search Extensions](/Extensions "Extensions")
  - [Check Extensions](/Check_Extensions "Check Extensions")
  - [Promotion Threats](/Passed_Pawn_Extensions "Passed Pawn Extensions")
  - [Piece Threats](/Mate_Threat_Extensions "Mate Threat Extensions")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [History Heuristic](/History_Heuristic "History Heuristic")

## [Evaluation](/Evaluation "Evaluation")

- Mostly [calculated incrementally](/Incremental_Updates "Incremental Updates")

# See also

- [Fortress](/Fortress "Fortress") (Chess term)
- [Gk](/Gk "Gk")
- [Rotated Indices](/Rotated_Indices "Rotated Indices")
- [Stonewall](/index.php?title=Stonewall&action=edit&redlink=1 "Stonewall (page does not exist)")
- [Ziggurat](/Ziggurat "Ziggurat")

# Forum Posts

- [futility cut-offs](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/375e65821715995f) by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), November 14, 1997
- [New Version: FORTRESS V1.5, the new Morphy?](https://www.stmintz.com/ccc/index.php?id=39509) by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), [CCC](/CCC "CCC"), January 15, 1999
- [Re: Home page for Fortress! ToDo: Opening book, ...](https://www.stmintz.com/ccc/index.php?id=67954) by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), [CCC](/CCC "CCC"), September 09, 1999
- [Fortress 1.62 is available !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30206&p=115019) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 22, 2000
- [Fortress 1.62 and Draw by 50 moves rule ?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37189&p=141153) by [Brice Boissel](/index.php?title=Brice_Boissel&action=edit&redlink=1 "Brice Boissel (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 08, 2002

# External Links

## Chess Engine

- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Fortress « G 6](http://www.g-sei.org/fortress/)
- [Fortress 1.62](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Fortress%201.62#Fortress_1_62) in [CCRL 40/4](/CCRL "CCRL")

## Chess

- [Fortress (chess) from Wikipedia](https://en.wikipedia.org/wiki/Fortress_%28chess%29)
- [Fortress chess (Variant) from Wikipedia](https://en.wikipedia.org/wiki/Fortress_chess)

## Misc

- [Fortress (programming language) - Wikipedia](https://en.wikipedia.org/wiki/Fortress_%28programming_language%29)
- [Fortification from Wikipedia](https://en.wikipedia.org/wiki/Fortification)
- [Fort (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Fort_%28disambiguation%29)
- [North Texas Wind Symphony](https://music.unt.edu/ensembles/north-texas-wind-symphony) - Fortress by [Frank Ticheli](https://en.wikipedia.org/wiki/Frank_Ticheli), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Artists impression of the battlements at [Buhen fortress](https://en.wikipedia.org/wiki/Buhen) in [Ancient Egypt](https://en.wikipedia.org/wiki/Ancient_Egypt) about 1800 BC, Source: [Franck Monnier](http://www.safran.be/products.php?cat=385) (**2010**). *[Les forteresses égyptiennes. Du Prédynastique au Nouvel Empire, collection Connaissance de l'Égypte ancienne](http://www.safran.be/proddetail.php?prod=CEA11)*. Safran (éditions), Bruxelles, 978-2-87457-033-9, [Defensive wall from Wikipedia](https://en.wikipedia.org/wiki/Defensive_wall)
2. [↑](#cite_ref-2) [futility cut-offs](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/375e65821715995f) by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), November 14, 1997
3. [↑](#cite_ref-3) [Günther Schrüfer](/G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") (**1988**). *Minimax-Suchen : Kosten, Qualität und Algorithmen*. [TU Braunschweig](https://en.wikipedia.org/wiki/Technical_University_of_Braunschweig) (German)
4. [↑](#cite_ref-4) based on Fortress 1.62.zip / readme.doc, [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)

**[Up one level](/Engines "Engines")**