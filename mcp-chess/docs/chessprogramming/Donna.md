# Donna

Source: https://www.chessprogramming.org/Donna

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Donna**

[![](/images/b/b7/DonatasLapienis.jpg)](http://lksf.lt/lt/Donatas_Lapienis)

Donatas Lapienis [[1]](#cite_note-1)

**Donna**,  
an [UCI](/UCI "UCI") compliant, experimental [open source chess engine](/Category:Open_Source "Category:Open Source") by [Michael Dvorkin](/Michael_Dvorkin "Michael Dvorkin"), written in the [Go programming language](/Go_(Programming_Language) "Go (Programming Language)"),
freely distributable under the terms of [MIT license](/Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") and first released in December 2014.

# Dedication

Donna is dedicated to [Lithuanian](https://en.wikipedia.org/wiki/Lithuania) chess grandmaster [Donatas Lapienis](https://lt.wikipedia.org/wiki/Donatas_Lapienis) (April 8, 1936, [Kaunas](https://en.wikipedia.org/wiki/Kaunas) - April 10, 2014, [Vilnius](https://en.wikipedia.org/wiki/Vilnius) [[2]](#cite_note-2) ), who was Michael Dvorkin's chess teacher.
In the mid 80s, Donatas Lapienis was highest ranked [correspondence chess](https://en.wikipedia.org/wiki/Correspondence_chess) player in the world with an [Elo rating](https://en.wikipedia.org/wiki/Elo_rating_system) of 2715 [[3]](#cite_note-3) .

# Acknowledgments

Michael Dvorkin thanks his friend chess grandmaster [Eduardas Rozentalis](https://en.wikipedia.org/wiki/Eduardas_Rozentalis), who inspired him to write a chess engine. Donna would never have been possible without the open source authors of their respective engines [[4]](#cite_note-4) :

- [Aaron Becker](/Aaron_Becker "Aaron Becker") of [Daydreamer](/Daydreamer "Daydreamer")
- [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey") of [Senpai](/Senpai "Senpai")
- [Igor Korshunov](/Igor_Korshunov "Igor Korshunov") of [Murka](/Murka "Murka")
- [Jon Dart](/Jon_Dart "Jon Dart") of [Arasan](/Arasan "Arasan")
- [Steve Maughan](/Steve_Maughan "Steve Maughan") of [Maverick](/Maverick "Maverick")
- [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan") of [TSCP](/TSCP "TSCP")
- [Tord Romstad](/Tord_Romstad "Tord Romstad"), [Marco Costalba](/Marco_Costalba "Marco Costalba"), [Joona Kiiski](/Joona_Kiiski "Joona Kiiski") of [Stockfish](/Stockfish "Stockfish")
- [ThinkingALot](/ThinkingALot "ThinkingALot") of [Gull](/Gull "Gull")
- [Vladimir Medvedev](/Vladimir_Medvedev "Vladimir Medvedev") of [GreKo](/GreKo "GreKo")

# Features

[[5]](#cite_note-5)

## [Data Structures](/Data "Data")

- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Material Imbalance Table](/Material_Tables "Material Tables")
- [Pawn Cache](/Pawn_Hash_Table "Pawn Hash Table")

## [Search](/Search "Search")

- [Root](/Root "Root"), [Tree](/Search_Tree "Search Tree"), and [Quiescence](/Quiescence_Search "Quiescence Search") Search
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Extensions](/Extensions "Extensions")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
- [Razoring](/Razoring "Razoring")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Delta Pruning](/Delta_Pruning "Delta Pruning")
- [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
- [Insufficient Material](/Material#InsufficientMaterial "Material")
- [Repetition Detection](/Repetitions "Repetitions")

## [Evaluation](/Evaluation "Evaluation")

- [Material](/Material "Material") with [Imbalance Adjustment](/Material_Tables "Material Tables")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [King Safety](/King_Safety "King Safety") and [Pawn Shield](/King_Safety#PawnShield "King Safety") Quality
- [Castling Rights](/Castling_Rights "Castling Rights")
- [Mobility](/Mobility "Mobility")
- [Center Control](/Center_Control "Center Control")
- [Threats](/Attacks "Attacks") and [Hanging Pieces](/Hanging_Piece "Hanging Piece")
- [Passed](/Passed_Pawn "Passed Pawn"), [Isolated](/Isolated_Pawn "Isolated Pawn"), [Doubled](/Doubled_Pawn "Doubled Pawn"), and [Backward Pawns](/Backward_Pawn "Backward Pawn")
- [Trapped Pieces](/Trapped_Pieces "Trapped Pieces")
- [Endgame Knowledge](/Endgame "Endgame")
- [Bitbase](/Endgame_Bitbases "Endgame Bitbases") for [KPK](/KPK "KPK")

## Misc

- [PolyGlot](/PolyGlot "PolyGlot") [Opening Books](/Opening_Book "Opening Book") [[6]](#cite_note-6)
- [Interactive Read–Eval–Print Loop (REPL)](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
- Donna Chess Format Position Notation

# Forum Posts

- [Donna, a new UCI chess engine by Michael Dvorkin](http://www.talkchess.com/forum/viewtopic.php?t=54596) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](/CCC "CCC"), December 09, 2014
- [Donna v2.0 released](http://www.talkchess.com/forum/viewtopic.php?t=56218) by [Michael Dvorkin](/Michael_Dvorkin "Michael Dvorkin"), [CCC](/CCC "CCC"), May 03, 2015
- [Donna 3.0 released](http://www.talkchess.com/forum/viewtopic.php?t=57921) by [Michael Dvorkin](/Michael_Dvorkin "Michael Dvorkin"), [CCC](/CCC "CCC"), October 12, 2015
- [Donna v3.1 released](http://www.talkchess.com/forum/viewtopic.php?t=58058) by [Michael Dvorkin](/Michael_Dvorkin "Michael Dvorkin"), [CCC](/CCC "CCC"), October 26, 2015
- [Donna v4.0 released](http://www.talkchess.com/forum/viewtopic.php?t=58849) by [Michael Dvorkin](/Michael_Dvorkin "Michael Dvorkin"), [CCC](/CCC "CCC"), January 08, 2016
- [Donna v4.1 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68745) by [Michael Dvorkin](/Michael_Dvorkin "Michael Dvorkin"), [CCC](/CCC "CCC"), October 28, 2018

# External Links

## Chess Engine

- [Donna Chess Engine Downloads](http://donnachess.github.io/)
- [michaeldv/donna · GitHub](https://github.com/michaeldv/donna)
- [michaeldv/donna\_opening\_books · GitHub](https://github.com/michaeldv/donna_opening_books)
- [Donna](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Donna&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Donna - Wiktionary](https://en.wiktionary.org/wiki/Donna)
- [donna - Wiktionary](https://en.wiktionary.org/wiki/donna)
- [Donna from Wikipedia](https://en.wikipedia.org/wiki/Donna)
- [Donna (given name) from Wikipedia](https://en.wikipedia.org/wiki/Donna_%28given_name%29)
- [Belladonna from Wikipedia](https://en.wikipedia.org/wiki/Belladonna)
- [Hurricane Donna from Wikipedia](https://en.wikipedia.org/wiki/Hurricane_Donna)
- [Donna - Wikipedia.it](https://it.wikipedia.org/wiki/Donna) (Italian)
- [Donna (scacchi) - Wikipedia.it](https://it.wikipedia.org/wiki/Donna_(scacchi)) (Italian)
- [Charlie Parker All Stars](https://en.wikipedia.org/wiki/Charlie_Parker%27s_Savoy_and_Dial_sessions#Session_6) - [Donna Lee](https://en.wikipedia.org/wiki/Donna_Lee), 1947 [[7]](#cite_note-7), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Charlie Parker](/Category:Charlie_Parker "Category:Charlie Parker"), [Miles Davis](/Category:Miles_Davis "Category:Miles Davis"), [Bud Powell](https://en.wikipedia.org/wiki/Bud_Powell), [Tommy Potter](https://en.wikipedia.org/wiki/Tommy_Potter), [Max Roach](https://en.wikipedia.org/wiki/Max_Roach)

- [Kinga Głyk Trio](http://kingaglyk.pl) - [Donna Lee](https://en.wikipedia.org/wiki/Donna_Lee), December 2016, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Kinga Głyk](/Category:Kinga_G%C5%82yk "Category:Kinga Głyk"), [Irek Głyk](http://glyk.pl/), [Kuba Gwardecki](https://www.discogs.com/de/artist/6685643-Kuba-Gwardecki)

# References

1. [↑](#cite_ref-1) Image from [Donatas Lapienis](http://lksf.lt/lt/Donatas_Lapienis), [Lietuvos korespondencinių šachmatų federacija](http://lksf.lt/lt/archyvas) (Lithuania correspondence chess federation)
2. [↑](#cite_ref-2) [In memoriam Donatas Lapienis (1936.04.08 – 2014.04.10) «Lietuvos šachmatų federacija](http://www.chessfed.lt/2014/04/in-memoriam-donatas-lapienis-1936-04-08-2014-04-10/)
3. [↑](#cite_ref-3) [michaeldv/donna · GitHub](https://github.com/michaeldv/donna) Readme
4. [↑](#cite_ref-4) [michaeldv/donna · GitHub](https://github.com/michaeldv/donna) Readme
5. [↑](#cite_ref-5) Features according to the Donna [README](https://github.com/michaeldv/donna) file
6. [↑](#cite_ref-6) [michaeldv/donna\_opening\_books · GitHub](https://github.com/michaeldv/donna_opening_books)
7. [↑](#cite_ref-7) [List of jazz contrafacts from Wikipedia](https://en.wikipedia.org/wiki/List_of_jazz_contrafacts)

**[Up one Level](/Engines "Engines")**