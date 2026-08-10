# Monolith

Source: https://www.chessprogramming.org/Monolith

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Monolith**

[File:Ahu Tongariki.jpg](/index.php?title=Special:Upload&wpDestFile=Ahu_Tongariki.jpg "File:Ahu Tongariki.jpg")

Moai, monolithic figures [[1]](#cite_note-1) [[2]](#cite_note-2)

**Monolith**,   
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Jonas Mayr](/index.php?title=Jonas_Mayr&action=edit&redlink=1 "Jonas Mayr (page does not exist)"), written in [C++17](/Cpp#17 "Cpp"), first released in Spring 2017 under the [GPL 3](/Free_Software_Foundation#GPL "Free Software Foundation") [[3]](#cite_note-3).
Monolith had its tournament debut in March 2019 at [TCEC Season 15](/TCEC_Season_15 "TCEC Season 15").

# Selected Games

[TCEC Season 15](/TCEC_Season_15 "TCEC Season 15"), Monolith 1 - [Jumbo 0.6.99.2](/Jumbo "Jumbo")

```
[Event "TCEC Season 15 - Division 4b"]
[Site "http://tcec.chessdom.com"]
[Date "2019.03.11"]
[Round "5.5"]
[White "Monolith 1"]
[Black "Jumbo 0.6.99.2"]
[Result "1-0"]

1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.Nf3 Nc6 5.Na3 Bg4 6.Be2 e5 7.d3 O-O-O 8.Nc4 e4 9.Ne3 Qh5 
10.Nxg4 Qxg4 11.Qa4 Nf6 12.dxe4 Qxe4 13.Qxe4 Nxe4 14.Bc4 Nd6 15.Bd3 g6 16.O-O c4 17.Bc2 
Bg7 18.Bg5 f6 19.Be3 Rhe8 20.Rad1 f5 21.Rd5 Ne4 22.Rxd8+ Kxd8 23.Bxe4 fxe4 24.Ng5 h5 
25.Rd1+ Kc7 26.Rd5 Bh6 27.h4 Bxg5 28.Rxg5 Re6 29.Rc5 Kd6 30.Rxc4 b5 31.Rc5 Re5 32.Rxe5 
Kxe5 33.Kf1 a5 34.Ke2 Ne7 35.Bb6 a4 36.b3 axb3 37.axb3 Nf5 38.g3 Kd5 39.Be3 Kc6 40.Bf4 
Kd5 41.Kd2 Kc5 42.Kd1 Ne7 43.Kc2 Nf5 44.Kd2 Kd5 45.Be3 Nd6 46.Kc2 Nf5 47.Bc1 Ne7 48.Bf4 
Nf5 49.Be3 Ne7 50.Kb2 Nc6 51.Ka3 Ne5 52.Kb4 Kc6 53.c4 bxc4 54.Bf4 Ng4 55.Kxc4 Nxf2 56.Kd4
Kb5 57.Ke3 Ng4+ 58.Kxe4 Kc6 59.b4 Kb5 60.Kd5 Kxb4 61.Ke6 Kc4 62.Kf7 Kd3 63.Kxg6 Ke4 64.Kxh5 
1-0
```

# Features

## [Board Representation](/Board_Representation "Board Representation")

- [Six/Three Bitboard Board-Definition](/Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition")
- [8x8 Board](/8x8_Board "8x8 Board")
- [Fancy Magic Bitboards](/Magic_Bitboards#Fancy "Magic Bitboards")
- [PEXT Bitboards](/BMI2#PEXTBitboards "BMI2")

## [Search](/Search "Search")

[[4]](#cite_note-4)

- [Parallel Search](/Parallel_Search "Parallel Search")
  - [Shared Hash Table](/Shared_Hash_Table "Shared Hash Table")
  - [Simplified ABDADA](/ABDADA "ABDADA") [[5]](#cite_note-5)
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Selectivity](/Selectivity "Selectivity")
  - [Check Extensions](/Check_Extensions "Check Extensions")
  - [Recapture Extensions](/Recapture_Extensions "Recapture Extensions")
  - [Passed Pawn Extensions](/Passed_Pawn_Extensions "Passed Pawn Extensions")
  - [Singular Extensions](/Singular_Extensions "Singular Extensions")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Static Null Move Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Late Move Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
  - [Static Exchange Evaluation Pruning](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [MVV/LVA](/MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Counter Moves History](/History_Heuristic#CMHist "History Heuristic")
  - [Follow Up History](/History_Heuristic#CMHist "History Heuristic")

## [Evaluation](/Evaluation "Evaluation")

[[6]](#cite_note-6)

- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Material](/Material "Material")
- [Bishop Pair](/Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
- [Trapped Bishop](/Trapped_Pieces "Trapped Pieces")
- [Outposts](/Outposts "Outposts")
- [Rook on (Half) Open File](/Rook_on_Open_File "Rook on Open File")
- [King-Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Passed Pawn](/Passed_Pawn "Passed Pawn")
  - [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
  - [Backward Pawn](/Backward_Pawn "Backward Pawn")
  - [Connected Pawns](/Connected_Pawns "Connected Pawns")
- [King Safety](/King_Safety "King Safety")
  - [Pawn Shield](/King_Safety#PawnShield "King Safety")
  - [Pawn Storm](/King_Safety#PawnStorm "King Safety")
  - [Attacking King Zone](/King_Safety#Attacking "King Safety")
- [Hanging Pieces](/Hanging_Piece "Hanging Piece")
- [Tempo](/Tempo "Tempo")
- [Texel's Tuning Method](/Texel%27s_Tuning_Method "Texel's Tuning Method")

## Misc

- [PolyGlot](/PolyGlot "PolyGlot") [Opening Book](/Opening_Book "Opening Book")
- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")
- [Chess960](/Chess960 "Chess960")

# Forum Posts

- [CCWiki etc. - new entries](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=63938) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](/CCC "CCC"), May 09, 2017
- [Monolith 1.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68685) by [Jonas Mayr](/index.php?title=Jonas_Mayr&action=edit&redlink=1 "Jonas Mayr (page does not exist)"), [CCC](/CCC "CCC"), October 18, 2018
- [Monolith 2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73708) by [Jonas Mayr](/index.php?title=Jonas_Mayr&action=edit&redlink=1 "Jonas Mayr (page does not exist)"), [CCC](/CCC "CCC"), April 19, 2020

# External Links

## Chess Engine

- [GitHub - cimarronOST/Monolith: UCI chess engine](https://github.com/cimarronOST/Monolith)
- [Monolith](https://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Monolith&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [monolith - Wiktionary](https://en.wiktionary.org/wiki/monolith)
- [Monolith from Wikipedia](https://en.wikipedia.org/wiki/Monolith)
- [Monolith (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Monolith_(disambiguation))
- [List of ancient Greek and Roman monoliths from Wikipedia](https://en.wikipedia.org/wiki/List_of_ancient_Greek_and_Roman_monoliths)
- [List of largest monoliths from Wikipedia](https://en.wikipedia.org/wiki/List_of_largest_monoliths)
- [Laila Biali](/Category:Laila_Biali "Category:Laila Biali") - The Monolith, [Trinity St. Paul's United Church](https://en.wikipedia.org/wiki/Trinity-St._Paul%27s_United_Church) in [Toronto](https://en.wikipedia.org/wiki/Toronto), April 2020, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   feat.: [Rob Christian](http://robchristianmusic.com/), [George Koller](https://en.wikipedia.org/wiki/George_Koller) and [Ben Wittman](https://www.discogs.com/artist/423811-Ben-Wittman)

# References

1. [↑](#cite_ref-1) Six of the 15 [Ahu Tongariki](https://en.wikipedia.org/wiki/Ahu_Tongariki) [Moais](https://en.wikipedia.org/wiki/Moai), restored by Chilean archaeologist [Claudio Cristino](https://www.tourhq.com/guide/cl72261/claudio-cristino) in the 1990s, [image](https://commons.wikimedia.org/wiki/File:Ahu_Tongariki.jpg) by Rivi, March 29, 2006, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Moais](https://en.wikipedia.org/wiki/Moai) are [monolithic](https://en.wikipedia.org/wiki/Monolith) human figures carved by the [Rapa Nui people](https://en.wikipedia.org/wiki/Rapa_Nui_people) on [Easter Island](https://en.wikipedia.org/wiki/Easter_Island) in eastern [Polynesia](https://en.wikipedia.org/wiki/Polynesia) between the years 1250 and 1500
3. [↑](#cite_ref-3) [CCWiki etc. - new entries](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=63938) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](/CCC "CCC"), May 09, 2017
4. [↑](#cite_ref-4) [Monolith/search.cpp at master · cimarronOST/Monolith · GitHub](https://github.com/cimarronOST/Monolith/blob/master/Source/search.cpp)
5. [↑](#cite_ref-5) [Simplified ABDADA](/ABDADA "ABDADA") inspired by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), ["Simplified ABDADA" updated](http://www.talkchess.com/forum/viewtopic.php?t=65025) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), August 29, 2017
6. [↑](#cite_ref-6) [Monolith/eval.cpp at master · cimarronOST/Monolith · GitHub](https://github.com/cimarronOST/Monolith/blob/master/Source/eval.cpp)

**[Up one Level](/Engines "Engines")**