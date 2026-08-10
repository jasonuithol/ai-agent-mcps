# Berserk

Source: https://www.chessprogramming.org/Berserk

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Berserk**

[File:Beserker, Lewis Chessmen, British Museum.jpg](/index.php?title=Special:Upload&wpDestFile=Beserker,_Lewis_Chessmen,_British_Museum.jpg "File:Beserker, Lewis Chessmen, British Museum.jpg")

Berserker [[1]](#cite_note-1)

**Berserk**,   
an [UCI](/UCI "UCI") compliant [open source](/Category:Open_Source "Category:Open Source") chess engine by [Jay Honnold](/Jay_Honnold "Jay Honnold"), written in [C](/C "C") and licensed under the [GPL v3.0](/Free_Software_Foundation#GPL "Free Software Foundation"), first released in February 2021 [[2]](#cite_note-2).
Berserk 4.2.0-dev had its tournament debut at [TCEC Season 21](/TCEC_Season_21 "TCEC Season 21") in May 2021 and gained a respectable 50% score in its strong [Qualification League](/TCEC_Season_21#Qual "TCEC Season 21"). Version 5 marked the end of [Hand Crafted Evaluation](/Evaluation "Evaluation") in Berserk. Berserk **6** and following feature [NNUE](/NNUE "NNUE") evaluation with an own network architecture [[3]](#cite_note-3).

# Credit

Berserk was influenced by other engines, engine authors and resources [[4]](#cite_note-readme-4):

- [Chess22k](/Chess22k "Chess22k") by [Sander Maassen vd Brink](/index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)")
- [BBC](/BBC "BBC") and its [Video Series](/BBC#YouTube "BBC") by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh")
- [Martin Sedlak](/Martin_Sedlak "Martin Sedlak")
- [Vice](/Vice "Vice") by [BlueFeverSoft](/BlueFeverSoft "BlueFeverSoft")
- [Stockfish](/Stockfish "Stockfish") by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [Marco Costalba](/Marco_Costalba "Marco Costalba"), [Joona Kiiski](/Joona_Kiiski "Joona Kiiski") and [Gary Linscott](/Gary_Linscott "Gary Linscott") et al.
- [Ethereal](/Ethereal "Ethereal") and [OpenBench](/OpenBench "OpenBench") by [Andrew Grant](/Andrew_Grant "Andrew Grant")
- [CPW](/Main_Page "Main Page") (thank you)
- [Connor McMonigle](/Connor_McMonigle "Connor McMonigle") ([Seer](/Seer "Seer") author) for his guidance on [NNs](/Neural_Networks "Neural Networks")

# Features

[[4]](#cite_note-readme-4)

## [Board Representation](/Board_Representation "Board Representation")

- [Bitboards](/Bitboards "Bitboards")
- [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")

## [Search](/Search "Search")

- [Lazy SMP](/Lazy_SMP "Lazy SMP")
- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
- [Negamax](/Negamax "Negamax")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Internal Iterative Deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](/Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](/History_Heuristic "History Heuristic")
  - [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic")
  - [Butterfly Heuristic](/Butterfly_Heuristic "Butterfly Heuristic")
  - [MVV/LVA](/MVV-LVA "MVV-LVA")
  - [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Selectivity](/Selectivity "Selectivity")
  - [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
  - [Reverse Futility Pruning](/Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
  - [Late Move Pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
  - [SEE Pruning](/Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Singular Extensions](/Singular_Extensions "Singular Extensions")
  - [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
  - [Delta Pruning](/Delta_Pruning "Delta Pruning")
  - [Quiescence Search](/Quiescence_Search "Quiescence Search")

## [Evaluation](/Evaluation "Evaluation")

- [NNUE](/NNUE "NNUE") (Berserk 6)
- [Tapered Eval](/Tapered_Eval "Tapered Eval")
- [Material](/Material "Material")
  - [Bishop Pair](/Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Mobility](/Mobility "Mobility")
  - [Trapped Pieces](/Trapped_Pieces "Trapped Pieces")
  - [Rooks on (Semi) Open Files](/Rook_on_Open_File "Rook on Open File")
- [Outposts](/Outposts "Outposts")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
  - [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")
  - [Backward Pawn](/Backward_Pawn "Backward Pawn")
  - [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
  - [Connected Pawns](/Connected_Pawns "Connected Pawns")
  - [Candidate Passed Pawn](/Candidate_Passed_Pawn "Candidate Passed Pawn")
  - [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [King Safety](/King_Safety "King Safety")
  - [Attacking King Zone](/King_Safety#Attacking "King Safety")
  - [Pawn Shelter](/King_Safety#PawnShield "King Safety")
  - [Pawn Storm](/King_Safety#PawnStorm "King Safety")
  - [Square Control](/King_Safety#SquareControl "King Safety")
- [Tactical Pattern](/Tactics "Tactics")
  - [Threats](/Square_Control "Square Control")
  - [Battery](/Battery "Battery")
  - [Hanging Pieces](/Hanging_Piece "Hanging Piece")
- [Tempo](/Tempo "Tempo")

## Misc

- [Texel's Tuning Method](/Texel%27s_Tuning_Method "Texel's Tuning Method")
- [KPK](/KPK "KPK") [Bitbase](/Endgame_Bitbases "Endgame Bitbases") by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak")

# See also

- [Zerker](/Zerker "Zerker")

# Forum Posts

- [Berserk Chess Engine (new)](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=12771) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), February 20, 2021
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=90) by [Gabor Szots](/Gabor_Szots "Gabor Szots"), [CCC](/CCC "CCC"), February 20, 2021

:   [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=117) (Berserk 2.0.0) by [Gabor Szots](/Gabor_Szots "Gabor Szots"), [CCC](/CCC "CCC"), March 05, 2021
:   [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=163) (Berserk 3.0.0) by [Gabor Szots](/Gabor_Szots "Gabor Szots"), [CCC](/CCC "CCC"), March 19, 2021
:   [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=291) (Berserk 4.0.0) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCC](/CCC "CCC"), April 27, 2021
:   [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=307) (Berserk 4.1.0) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCC](/CCC "CCC"), May 02, 2021
:   [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=384) (Berserk 4.2.0) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCC](/CCC "CCC"), May 25, 2021
:   [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=466) (Berserk 4.3.0) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCC](/CCC "CCC"), July 03, 2021
:   [Re: New engine releases & news 2021](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=776) (Berserk 6) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCC](/CCC "CCC"), October 19, 2021

- [Berserk 7](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=845) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCC](/CCC "CCC"), November 05, 2021
- [Berserk 8 Released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78830) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCC](/CCC "CCC"), December 05, 2021

# External Links

## Chess Engine

- [GitHub - jhonnold/berserk: UCI Chess Engine written in C](https://github.com/jhonnold/berserk)
- [Berserk](https://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Berserk&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")
- [Berserk](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Berserk&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [berserk - Wiktionary](https://en.wiktionary.org/wiki/berserk)
- [Berserk from Wikipedia](https://en.wikipedia.org/wiki/Berserk)
- [Berserker (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Berserker_(disambiguation))
- [Berserker from Wikipedia](https://en.wikipedia.org/wiki/Berserker)
- [The Dave Fox Group](https://www.discogs.com/de/artist/2647540-The-Dave-Fox-Group) - Berserker, [Gatewalk](https://www.discogs.com/de/The-Dave-Fox-Group-Gatewalk/release/4174471) (2004), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) "Berserker" warder (rook) of the [Lewis Chessmen](https://en.wikipedia.org/wiki/Lewis_chessmen) in the [British Museum](https://en.wikipedia.org/wiki/British_Museum), probably made in [Norway](https://en.wikipedia.org/wiki/Norway) in the [12th century](https://en.wikipedia.org/wiki/12th_century), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Berserk Chess Engine (new)](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=12771) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [CCRL Discussion Board](/Computer_Chess_Forums "Computer Chess Forums"), February 20, 2021
3. [↑](#cite_ref-3) [Release Berserk 6 · jhonnold/berserk · GitHub](https://github.com/jhonnold/berserk/releases/tag/6)
4. ↑ [4.0](#cite_ref-readme_4-0) [4.1](#cite_ref-readme_4-1) [berserk/README.md at main · jhonnold/berserk · GitHub](https://github.com/jhonnold/berserk/blob/main/README.md)

**[Up one Level](/Engines "Engines")**