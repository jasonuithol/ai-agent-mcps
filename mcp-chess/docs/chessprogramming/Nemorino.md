# Nemorino

Source: https://www.chessprogramming.org/Nemorino

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Nemorino**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/NemorinoLelisirDamore.jpg/330px-NemorinoLelisirDamore.jpg)](/File:NemorinoLelisirDamore.jpg)

Nemorino enjoys the alleged effect of the love potion [[1]](#cite_note-1)

**Nemorino**,  
an [UCI](/UCI "UCI") compliant, free [open source chess engine](/Category:Open_Source "Category:Open Source") by [Christian Günther](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), also supporting the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), written in [C++](/Cpp "Cpp") and first released in September 2016 under the [GPLv3](/Free_Software_Foundation#GPL "Free Software Foundation") license. Nemorino's [board representation](/Board_Representation "Board Representation") and [move structure](/Encoding_Moves "Encoding Moves") are taken from [Stockfish](/Stockfish "Stockfish") [[2]](#cite_note-2). Nemorino supports [Syzygy Bases](/Syzygy_Bases "Syzygy Bases") based on [Basil Falcinelli's](/Basil_Falcinelli "Basil Falcinelli") [Fathom API](/Syzygy_Bases#Fathom "Syzygy Bases") [[3]](#cite_note-3), applies a very [lazy parallel search](/Parallel_Search#Lazy "Parallel Search"), and is able to play [Chess960](/Chess960 "Chess960").

# Etymology

Nemorino is named after the a character of [Gaetano Donizetti's](https://en.wikipedia.org/wiki/Gaetano_Donizetti) [comic opera](https://en.wikipedia.org/wiki/Comic_opera)[L'elisir d'amore](https://en.wikipedia.org/wiki/L%27elisir_d%27amore), premiered on May 12, 1832 at the [Teatro alla Canobbiana](https://en.wikipedia.org/wiki/Teatro_Lirico_(Milan)) in [Milan](https://en.wikipedia.org/wiki/Milan). Nemorino, a poor peasant, in love with [Adina](https://en.wikipedia.org/wiki/Adina), asks [quack doctor](https://en.wikipedia.org/wiki/Quackery) [Dulcamara](https://en.wikipedia.org/wiki/Dulcamara) for [Isolde's](/Tristram "Tristram") [love potion](https://en.wikipedia.org/wiki/Love_potion), who sells him a bottle of cheap [Bordeaux wine](https://en.wikipedia.org/wiki/Bordeaux_wine) instead ...

# Features

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")
- [Copy/Make](/Copy-Make "Copy-Make")

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening") with [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [PVS](/Principal_Variation_Search "Principal Variation Search") / [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")
- [Lazy SMP](/Lazy_SMP "Lazy SMP")
- [Selectivity](/Selectivity "Selectivity")
  - [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Check Extensions](/Check_Extensions "Check Extensions")
  - [Recapture Extensions](/Recapture_Extensions "Recapture Extensions")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [PV-Move](/PV-Move "PV-Move")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Followup History Heuristic](/History_Heuristic#CMHist "History Heuristic")

## [Evaluation](/Evaluation "Evaluation")

- [NNUE](/NNUE "NNUE") (Nemorino 6) [[4]](#cite_note-4)
- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Material](/Material "Material")
- [Mobility](/Mobility "Mobility")
- [King Safety](/King_Safety "King Safety")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [Endgame Knowledge](/Endgame "Endgame")

## Misc

- [Chess960](/Chess960 "Chess960")
- [Pondering](/Pondering "Pondering")
- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")

# See also

- [Fiction](/Category:Fiction "Category:Fiction")
- [Nemo](/Nemo "Nemo")
- [Peasant](/Peasant "Peasant")
- [Tristram](/Tristram "Tristram")

# Forum Posts

## 2016 ...

- [Nemorino - new engine](http://www.talkchess.com/forum/viewtopic.php?t=61507) by [Christian Günther](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), September 23, 2016
- [Nemorino 2.0](http://www.talkchess.com/forum/viewtopic.php?t=62845) by [Christian Günther](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), January 16, 2017
- [Nemorino 2.0a is available ...](http://www.talkchess.com/forum/viewtopic.php?t=63450) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), March 15, 2017
- [Nemorino 3](http://www.talkchess.com/forum/viewtopic.php?t=64336) by [Christian Günther](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), June 18, 2017
- [Re: TCEC 10](http://www.talkchess.com/forum/viewtopic.php?t=65447&start=18) by [Christian Günther](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), October 15, 2017 » [TCEC Season 10](/TCEC_Season_10 "TCEC Season 10")
- [Nemorino 4](http://www.talkchess.com/forum/viewtopic.php?t=66086) by [Christian Günther](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), December 21, 2017
- [Nemorino 5](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68046&p=769135) by [Florentino](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), July 22, 2018

## 2020 ...

- [Nemorino 6 (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75241) by [Florentino](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), September 28, 2020
- [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle"), [CCC](/CCC "CCC"), June 17, 2021 » [NNUE](/NNUE "NNUE")

# External Links

## Chess Engine

- [Christian Günther / Nemorino — Bitbucket](https://bitbucket.org/christian_g_nther/nemorino)
- [Nemorino](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Nemorino&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [L'elisir d'amore from Wikipedia](https://en.wikipedia.org/wiki/L%27elisir_d%27amore)
- [Una furtiva lagrima from Wikipedia](https://en.wikipedia.org/wiki/Una_furtiva_lagrima)
- [The Searchers](/Category:The_Searchers "Category:The Searchers") - [Love potion number 9](https://en.wikipedia.org/wiki/Love_Potion_No._9_(song)) (1963), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Nemorino enjoys the alleged effect of the [love potion](https://en.wikipedia.org/wiki/Love_potion), surrounded by the village girls and jealously Adina in the background, [Brown Opera Productions](https://en.wikipedia.org/wiki/Brown_Opera_Productions), [Brown University](https://en.wikipedia.org/wiki/Brown_University), Spring 2009 show [L'elisir d'amore](https://en.wikipedia.org/wiki/L%27elisir_d%27amore), Image by Joeforemperor, April 07, 2009, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2)  [Christian Günther / Nemorino — Bitbucket](https://bitbucket.org/christian_g_nther/nemorino/overview)
3. [↑](#cite_ref-3) [GitHub - basil00/Fathom: Syzygy TB probe tool](https://github.com/basil00/Fathom)
4. [↑](#cite_ref-4) [Nemorino 6 (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75241) by [Florentino](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), September 28, 2020

**[Up one level](/Engines "Engines")**