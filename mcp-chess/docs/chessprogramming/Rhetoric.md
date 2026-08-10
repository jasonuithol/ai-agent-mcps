# Rhetoric

Source: https://www.chessprogramming.org/Rhetoric

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Rhetoric**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/D%C3%A9mosth%C3%A8ne_s%27exer%C3%A7ant_%C3%A0_la_parole_%281870%29_by_Jean-Jules-Antoine_Lecomte_du_Nou%C3%BF.jpg/250px-D%C3%A9mosth%C3%A8ne_s%27exer%C3%A7ant_%C3%A0_la_parole_%281870%29_by_Jean-Jules-Antoine_Lecomte_du_Nou%C3%BF.jpg)](/File:D%C3%A9mosth%C3%A8ne_s%27exer%C3%A7ant_%C3%A0_la_parole_(1870)_by_Jean-Jules-Antoine_Lecomte_du_Nou%C3%BF.jpg)

[Demosthenes](https://en.wikipedia.org/wiki/Demosthenes) Practicing [Oratory](https://en.wikipedia.org/wiki/Oratory) [[1]](#cite_note-1)

**Rhetoric**,  
an [UCI](/UCI "UCI") compliant chess engine by primary author [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan") supported by chess advisers [Jose Antonio Morillas](/index.php?title=Jose_Antonio_Morillas&action=edit&redlink=1 "Jose Antonio Morillas (page does not exist)") and [Juan José Corbalán](/index.php?title=Juan_Jos%C3%A9_Corbal%C3%A1n&action=edit&redlink=1 "Juan José Corbalán (page does not exist)")
[[2]](#cite_note-2),
first released as free engine in April 2012. Rhetoric is written in [C++](/Cpp "Cpp"),
and has been trained with [Genetic Algorithms](/Genetic_Programming#GeneticAlgorithm "Genetic Programming") to fit grandmaster moves from a collection of games played by [Anatoly Karpov](https://en.wikipedia.org/wiki/Anatoly_Karpov) versus strong grandmasters
[[3]](#cite_note-3),
and therefor promises an interesting playing style.
Rhetoric **1.2**, released in February 2014 [[4]](#cite_note-4),
was a huge improvement due to the introduction of [singular extensions](/Singular_Extensions "Singular Extensions") and [late move pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning"),
and further by performing [evaluation tuning](/Automated_Tuning "Automated Tuning") inspired by the [method](/Texel%27s_Tuning_Method "Texel's Tuning Method") proposed by [Peter Österlund](/Peter_%C3%96sterlund "Peter Österlund")
[[5]](#cite_note-5)
[[6]](#cite_note-6).

# Technical Details

[[7]](#cite_note-7)

- [Bitboards](/Bitboards "Bitboards")
  - [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") [[8]](#cite_note-8)
- [Evaluation](/Evaluation "Evaluation")
  - [Tapered Eval](/Tapered_Eval "Tapered Eval")
  - [Material](/Material "Material")
  - [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
  - [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Mobility](/Mobility "Mobility")
  - Occupation of strong squares
  - [King Safety](/King_Safety "King Safety")
  - [Tuning à la Texel](/Texel%27s_Tuning_Method "Texel's Tuning Method") (1.2)
- [Search](/Search "Search")
  - [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [Transposition Table](/Transposition_Table "Transposition Table")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Razoring](/Razoring "Razoring")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Late Move Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (1.2)
  - [Singular Extensions](/Singular_Extensions "Singular Extensions") (1.2)

# Publications

- Robert Wilcocks (**1993**). *[Maelzel's Chess Player: Sigmund Freud and the Rhetoric of Deceit](https://psycnet.apa.org/record/1994-97241-000)*. [Rowman & Littlefield](https://en.wikipedia.org/wiki/Rowman_%26_Littlefield), [amazon](https://www.amazon.com/Maelzels-Chess-Player-Rhetoric-1993-12-22/dp/B01K925A5I) [[9]](#cite_note-9) [[10]](#cite_note-10)

# Forum Posts

## 2012

- [Moving to Magic Bitboards... any advice?](http://www.talkchess.com/forum/viewtopic.php?t=42291) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), February 03, 2012 » [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")
- [New engine: Rhetoric](http://www.talkchess.com/forum/viewtopic.php?t=43144) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), April 03, 2012

## 2013

- [Rhetoric 1.0, new version](http://www.talkchess.com/forum/viewtopic.php?t=48418) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), June 25, 2013
- [Test Rhetoric 1.0 x64](http://www.talkchess.com/forum/viewtopic.php?t=48525) by [Pedro Castro](/Pedro_Castro "Pedro Castro"), [CCC](/CCC "CCC"), July 03, 2013
- [passed pawn question](http://www.talkchess.com/forum/viewtopic.php?t=48823) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), August 02, 2013 » [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [Rhetoric 1.1](http://www.talkchess.com/forum/viewtopic.php?t=50581) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), December 21, 2013

## 2014

- [Rhetoric 1.2 Released](http://www.talkchess.com/forum/viewtopic.php?t=51431) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), February 28, 2014
- [Steps to compile for Android](http://www.talkchess.com/forum/viewtopic.php?t=51660) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), March 19, 2014 » [Android](/Android "Android")
- [Rhetoric 1.4](http://www.talkchess.com/forum/viewtopic.php?t=52699) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), June 20, 2014
- [Rhetoric 1.4.1 available](http://www.talkchess.com/forum/viewtopic.php?t=53783) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), September 22, 2014

## 2015 ...

- [Rhetoric 1.4.3 Released](http://www.talkchess.com/forum/viewtopic.php?t=58376) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), November 26, 2015
- [Rhetoric (Dynamic Settings) Review](http://www.talkchess.com/forum/viewtopic.php?t=59792) by [Brendan J. Norman](/index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](/CCC "CCC"), April 08, 2016
- [Re: A genetic chess engine?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68655&start=6) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), October 18, 2018

# External Links

## Chess Engine

- [Rhetoric, un nuevo estil](https://web.archive.org/web/20180820102052/http://www.chessrhetoric.com/) (Spanish, [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), August 20, 2018)
- [Rhetoric](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Rhetoric&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [Rhetoric from Wikipedia](https://en.wikipedia.org/wiki/Rhetoric)
- [Nathan Parker Smith](http://www.bjurecords.com/nathan-parker-smith) - Rhetoric Machine, [Not Dark Yet](http://www.bjurecords.com/store/bjur-048-nathan-parker-smith-not-dark-yet-320k-mp3-download) (2014), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Jean-Jules-Antoine Lecomte du Nouÿ](/Category:Jean-Jules-Antoine_Lecomte_du_Nou%C3%BF "Category:Jean-Jules-Antoine Lecomte du Nouÿ") - [Demosthenes Practising Oratory](https://en.wikipedia.org/wiki/File:DemosthPracticing.jpg) (1842–1923), [Demosthenes](https://en.wikipedia.org/wiki/Demosthenes) used to study in an underground room he constructed himself. He also used to talk with [pebbles](https://en.wikipedia.org/wiki/Pebble) in his mouth and recited verses while running. [Demosthenes from Wikipedia](https://en.wikipedia.org/wiki/Demosthenes), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Rhetoric - Equipo de Desarrollo](https://web.archive.org/web/20180823125714/http://www.chessrhetoric.com/index.php/equipo) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), August 23, 2018)
3. [↑](#cite_ref-3) [New engine: Rhetoric](http://www.talkchess.com/forum/viewtopic.php?t=43144) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), April 03, 2012
4. [↑](#cite_ref-4) [Rhetoric 1.2 Released](http://www.talkchess.com/forum/viewtopic.php?t=51431) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), February 28, 2014
5. [↑](#cite_ref-5) [Re: Rhetoric 1.2 Released](http://www.talkchess.com/forum/viewtopic.php?t=51431&start=7) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), February 28, 2014
6. [↑](#cite_ref-6) [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=555522&t=50823) by [Peter Österlund](/Peter_%C3%96sterlund "Peter Österlund"), [CCC](/CCC "CCC"), January 31, 2014
7. [↑](#cite_ref-7) [Rhetoric - Detalles técnicos](https://web.archive.org/web/20180823125136/http://chessrhetoric.com/index.php/tecnicos) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), August 23, 2018)
8. [↑](#cite_ref-8) [Moving to Magic Bitboards... any advice?](http://www.talkchess.com/forum/viewtopic.php?t=42291) by [Alberto Sanjuan](/Alberto_Sanjuan "Alberto Sanjuan"), [CCC](/CCC "CCC"), February 03, 2012
9. [↑](#cite_ref-9) [Maelzel's Chess Player from Wikipedia](https://en.wikipedia.org/wiki/Maelzel%27s_Chess_Player)
10. [↑](#cite_ref-10) [Sigmund Freud from Wikipedia](https://en.wikipedia.org/wiki/Sigmund_Freud)

**[Up one level](/Engines "Engines")**