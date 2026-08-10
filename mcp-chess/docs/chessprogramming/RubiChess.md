# RubiChess

Source: https://www.chessprogramming.org/RubiChess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* RubiChess**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Macrothylacia_rubi_male%2C_veelvraat_mannetje.jpg/330px-Macrothylacia_rubi_male%2C_veelvraat_mannetje.jpg)](/File:Macrothylacia_rubi_male,_veelvraat_mannetje.jpg)

Macrothylacia rubi [[1]](#cite_note-1)

**RubiChess**,  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), written in [C++](/Cpp "Cpp"), licensed under the [GPL v3.0](/Free_Software_Foundation#GPL "Free Software Foundation").
RubiChess started in 2017 as [0x88](/0x88 "0x88") engine and soon evolved to a [bitboard](/Bitboards "Bitboards") engine first using [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") and subsequently [magic bitboards](/Magic_Bitboards "Magic Bitboards") (about 24% faster) to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") [[2]](#cite_note-2). In September 2020, Andreas Matthies announced RubiChess [NNUE](/NNUE "NNUE") [[3]](#cite_note-3).

# Features

[[4]](#cite_note-4)

## [Board Representation](/Board_Representation "Board Representation")

- [Classical Bitboard Board-Definition](/Bitboard_Board-Definition#CBoardDef "Bitboard Board-Definition")
- [Plain Magic Bitboards](/Magic_Bitboards#Plain "Magic Bitboards")

## [Search](/Search "Search")

- [Lazy SMP](/Lazy_SMP "Lazy SMP") (1.3)
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Selectivity](/Selectivity "Selectivity")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning") with [Verification](/Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [ProbCut](/ProbCut "ProbCut") (1.3)
  - [Futility Pruning](/Futility_Pruning "Futility Pruning")
  - [Extended Futility Pruning](/Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
  - [Late Move Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
  - [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Razoring](/Razoring "Razoring")
  - [Singular Extensions](/Singular_Extensions "Singular Extensions")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")
  - [SEE Pruning](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [PV-Move](/PV-Move "PV-Move")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Captures](/Captures "Captures") by [MVV/LVA](/MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Counter Moves History](/History_Heuristic#CMHist "History Heuristic")

## [Evaluation](/Evaluation "Evaluation")

- [NNUE](/NNUE "NNUE") (RubiChess NNUE)
- [Texel's Tuning Method](/Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
- [Rooks on (Semi) Open Files](/Rook_on_Open_File "Rook on Open File")
- [Hanging Pieces](/Hanging_Piece "Hanging Piece")
- [Pinned Pieces](/Pin "Pin")
- [Pawn/King Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Phalanx](/Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)")
  - [Passed Pawn](/Passed_Pawn "Passed Pawn")
  - [Candidate Passed Pawn](/Candidate_Passed_Pawn "Candidate Passed Pawn")
- [King Safety](/King_Safety "King Safety")
  - [Attacks](/King_Safety#Attacking "King Safety")
  - [Pawn Storm](/King_Safety#PawnStorm "King Safety")
- [Tempo Bonus](/Tempo#Tempo_Bonus "Tempo")

## Misc

- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")

# Forum Posts

## 2018 ...

- [RubiChess 0.9 is out](http://talkchess.com/forum3/viewtopic.php?f=2&t=67594) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), May 29, 2018
- [RubiChess 1.1](http://talkchess.com/forum3/viewtopic.php?t=68559) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), October 03, 2018
- [RubiChess 1.3](http://talkchess.com/forum3/viewtopic.php?t=69876) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), February 11, 2019
- [Rubichess 1.4](http://talkchess.com/forum3/viewtopic.php?f=2&t=70878) by [Ferdinand Mosca](/Ferdinand_Mosca "Ferdinand Mosca"), [CCC](/CCC "CCC"), May 31, 2019
- [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=369) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), October 17, 2019

## 2020 ...

- [Re: Orion 0.7 : NNUE experiment](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74828&start=5) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), August 21, 2020
- [RubiChess NNUE player implemented](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75016) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), September 06, 2020

:   [Re: RubiChess NNUE player implemented](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75016&start=64) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), November 01, 2020

- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=225) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), April 14, 2021
- [Rubichess NN questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77157) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), April 23, 2021 » [NNUE](/NNUE "NNUE")
- [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle"), [CCC](/CCC "CCC"), June 17, 2021 » [NNUE](/NNUE "NNUE")
- [RubiChess 2.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77665) by Boban Stanojević, [CCC](/CCC "CCC"), July 07, 2021

# External Links

## Chess Engine

- [GitHub - Matthies/RubiChess: Another chess engine](https://github.com/Matthies/RubiChess)

:   [GitHub - Matthies/NN](https://github.com/Matthies/NN)

- [RubiChess](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=RubiChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [rubi - Wiktionary](https://en.wiktionary.org/wiki/rubi)
- [Rubí from Wikipedia](https://en.wikipedia.org/wiki/Rub%C3%AD)
- [Rubí Rodríguez from Wikipedia](https://en.wikipedia.org/wiki/Rub%C3%AD_Rodr%C3%ADguez) » [Rubí Rodríguez](/Mathematician#RRodriguez "Mathematician")
- [Rubí, Barcelona from Wikipedia](https://en.wikipedia.org/wiki/Rub%C3%AD,_Barcelona)
- [Ruby from Wikipedia](https://en.wikipedia.org/wiki/Ruby)
- [Ruby (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Ruby_(disambiguation))
- [Ruby character from Wikipedia](https://en.wikipedia.org/wiki/Ruby_character)
- [Ruby (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Ruby_(programming_language)) » [Ruby](/index.php?title=Ruby&action=edit&redlink=1 "Ruby (page does not exist)")
- [The Rolling Stones](/Category:The_Rolling_Stones "Category:The Rolling Stones") - [Ruby Tuesday](https://en.wikipedia.org/wiki/Ruby_Tuesday_(song)), Official 1991, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Macrothylacia rubi](https://en.wikipedia.org/wiki/Macrothylacia_rubi), male, [Image](https://commons.wikimedia.org/wiki/File:Macrothylacia_rubi_male,_veelvraat_mannetje.jpg) by [Rasbak](https://commons.wikimedia.org/wiki/User:Rasbak), May 11, 2011, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [RubiChess/ChangeLog.txt at master · Matthies/RubiChess · GitHub](https://github.com/Matthies/RubiChess/blob/master/ChangeLog.txt)
3. [↑](#cite_ref-3) [RubiChess NNUE player implemented](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75016) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), September 06, 2020
4. [↑](#cite_ref-4) [RubiChess/ChangeLog.txt at master · Matthies/RubiChess · GitHub](https://github.com/Matthies/RubiChess/blob/master/ChangeLog.txt)

**[Up one level](/Engines "Engines")**