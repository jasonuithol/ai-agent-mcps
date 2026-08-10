# Winglet

Source: https://www.chessprogramming.org/Winglet

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Winglet**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Winglet_with_attached_tufts_of_an_KC-135A.jpg/330px-Winglet_with_attached_tufts_of_an_KC-135A.jpg)](/File:Winglet_with_attached_tufts_of_an_KC-135A.jpg)

Winglet [[1]](#cite_note-1)

**Winglet**,  
a didactic [open source chess engine](/Category:Open_Source "Category:Open Source") by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), written in [C++](/Cpp "Cpp") and licensed under the [GNU General Public License](/Free_Software_Foundation#GPL "Free Software Foundation").
The development of Winglet was documented on the website tutorial *Winglet, Writing a Chess Program in 99 Steps*, started in 2011, now hosted by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine) [[2]](#cite_note-2).
Winglet is intended as [bitboard](/Bitboards "Bitboards") version of [TSCP](/TSCP "TSCP") with [WinBoard](/WinBoard "WinBoard") support [[3]](#cite_note-3),
and is loosely derived from [Wing](/Wing "Wing"), Stef Luijten's former private engine [[4]](#cite_note-4),
in the meantime also open source [[5]](#cite_note-5).

# Description

## Board Representation

Winglet applies a mixture of [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards") and [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") [[6]](#cite_note-6) to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") with 32 [KiB](https://en.wikipedia.org/wiki/Kibibyte) precalculated lookup tables[64][64] each on [ranks](/Ranks "Ranks"), [files](/Files "Files"), [diagonals](/Diagonals "Diagonals") and [anti-diagonals](/Anti-Diagonals "Anti-Diagonals"), indexed by [square](/Squares "Squares") and hashed line [occupancy](/Occupancy "Occupancy") - the [inner six bits](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks") multiplied by a [magic factor](/Magic_Bitboards "Magic Bitboards") and shifted right by the strange looking 57, while 58 is more natural to ensure a six bit index range, using a constant factor (b-File) for all squares of a diagonal or anti-diagonal, ...

```
U64 arrDiagonalAttacks[64][64]] /* requires initialization */

U64 diagonalKindergartenAttacks(U64 occ, enumSquare sq) {
   occ = (diagonalMaskEx[sq] & occ) * C64(0x0202020202020202) >> 58;
   return arrDiagonalAttacks[sq][occ];
}
```

... but "magic" Winglet factors are designed such that the most significant bit of the 64-bit product will always be clear, that is positive if interpreted as signed 64-bit integer. It seems, Winglet's occupied index calculations emulate Wing's [rotated bitboard](/Rotated_Bitboards "Rotated Bitboards") indices for same attack table layout:

```
/*                 Winglet's occupancy state             ==            Wing's occupancy state */
(occ & MG_DIAGA8H1MASK[sq]) * MG_DIAGA8H1MAGIC[sq] >> 57 == (occ045 >> DIAGA8H1_ATTACK_SHIFT[sq]) & 63
(occ & MG_DIAGA1H8MASK[sq]) * MG_DIAGA1H8MAGIC[sq] >> 57 == (occ315 >> DIAGA1H8_ATTACK_SHIFT[sq]) & 63
(occ & MG_FILEMASK[sq])     * MG_FILEMAGIC[sq])    >> 57 == (occ090 >> FILE_ATTACK_SHIFT[sq])     & 63
```

## Search

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [MVV-LVA](/MVV-LVA "MVV-LVA")
- [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")

## Evaluation

- [Material Balance](/Material#Balance "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")

:   [Passed Pawn](/Passed_Pawn "Passed Pawn")
:   [Backward Pawn](/Backward_Pawn "Backward Pawn")
:   [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
:   [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")

- [Bishop Pair](/Bishop_Pair "Bishop Pair")
- [Rook on Open File](/Rook_on_Open_File "Rook on Open File")
- [Rook behind Passers](/Tarrasch_Rule "Tarrasch Rule")
- [King Safety](/King_Safety "King Safety") in [Opening](/Opening "Opening"), [Middlegame](/Middlegame "Middlegame")

:   [Pawn Shield](/King_Safety#PawnShield "King Safety")
:   [King Tropism](/King_Safety#KingTropism "King Safety")

- [King Centralization](/King_Centralization "King Centralization") in [Endgame](/Endgame "Endgame")

# See also

- [Chesser](/index.php?title=Chesser&action=edit&redlink=1 "Chesser (page does not exist)") by [Syed Fahad](/Syed_Fahad "Syed Fahad") [[7]](#cite_note-7)
- [Godot](/Godot "Godot") by [Ulysse Carion](/index.php?title=Ulysse_Carion&action=edit&redlink=1 "Ulysse Carion (page does not exist)") [[8]](#cite_note-8)
- [Kenny](/index.php?title=Kenny&action=edit&redlink=1 "Kenny (page does not exist)") by [Kenshin Himura](/index.php?title=Kenshin_Himura&action=edit&redlink=1 "Kenshin Himura (page does not exist)") [[9]](#cite_note-9) [[10]](#cite_note-10)
- [Vajolet](/Vajolet "Vajolet") by [Marco Belli](/Marco_Belli "Marco Belli") [[11]](#cite_note-11)
- [Wing](/Wing "Wing") by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)")

# Forum Posts

- [writing a chess engine in xx steps](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51701) by [wing](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 18, 2011
- [Writing a chess program in xx steps](http://www.talkchess.com/forum/viewtopic.php?t=38787) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [CCC](/CCC "CCC"), April 18, 2011
- [Chess Programming/Concepts for Beginners](http://www.open-chess.org/viewtopic.php?f=5&t=1354) by MoldyJacket, [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 18, 2011

# External Links

## Chess Engine

- [Index of /chess/engines/Jim Ablett/WINGLET](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/WINGLET/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")

## Tutorial Archive

- [Winglet, Writing a Chess Program in 99 Steps](http://web.archive.org/web/20120621100214/http://www.sluijten.com/winglet/) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), hosted by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)

:   [01 Introduction - 05 First steps with Visual Studio C++](http://web.archive.org/web/20120621100214/http://www.sluijten.com/winglet/#02%20%20Anatomy%20of%20a%20chess%20program)
:   [06 Reading user commands](http://web.archive.org/web/20120112065051/http://www.sluijten.com/winglet/06commands01.htm#06%20%20Reading%20user%20commands)
:   [07 Internal representation of the chess board - bitboards](http://web.archive.org/web/20120112114121/http://www.sluijten.com/winglet/07boardrep01.htm) » [Board Representation](/Board_Representation "Board Representation"), [Bitboards](/Bitboards "Bitboards")
:   [08 Displaying the position](http://web.archive.org/web/20120112084004/http://www.sluijten.com/winglet/08display01.htm) » [Chess Position](/Chess_Position "Chess Position")
:   [09 Reading a FEN string](http://web.archive.org/web/20120112113815/http://www.sluijten.com/winglet/09readfen01.htm) » [Forsyth-Edwards Notation](/Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
:   [10 Setting up the board manually](http://web.archive.org/web/20120112113841/http://www.sluijten.com/winglet/10setup01.htm)
:   [11 The move generator](http://web.archive.org/web/20120112113911/http://www.sluijten.com/winglet/11movegen01.htm) » [Move Generation](/Move_Generation "Move Generation")
:   [12 Making the moves](http://web.archive.org/web/20120112114201/http://www.sluijten.com/winglet/12makemove01.htm) » [Make Move](/Make_Move "Make Move")
:   [13 The evaluation function](http://web.archive.org/web/20120112114146/http://www.sluijten.com/winglet/13evaluation01.htm) » [Evaluation](/Evaluation "Evaluation")
:   [14 Search](http://web.archive.org/web/20120713102202/http://www.sluijten.com/winglet/14search01.htm) » [Search](/Search "Search"), [Minimax](/Minimax "Minimax"), [Alpha-Beta](/Alpha-Beta "Alpha-Beta"), [PVS](/Principal_Variation_Search "Principal Variation Search")
:   [15 Mate and draw detection](http://web.archive.org/web/20120112114126/http://www.sluijten.com/winglet/15draw01.htm) » [Checkmate](/Checkmate "Checkmate"), [Stalemate](/Stalemate "Stalemate")
:   [16 Repetition detection - Zobrist keys](http://web.archive.org/web/20110722072635/http://www.sluijten.com/winglet/16repetition01.htm) » [Repetitions](/Repetitions "Repetitions"), [Zobrist Keys](/Zobrist_Hashing "Zobrist Hashing")
:   [17 Iterative deepening and move ordering](http://web.archive.org/web/20120112113836/http://www.sluijten.com/winglet/17iterativedeepening01.htm) » [Iterative Deepening](/Iterative_Deepening "Iterative Deepening"), [Move Ordering](/Move_Ordering "Move Ordering")
:   [18 Quiescence search and SEE](http://web.archive.org/web/20120112113805/http://www.sluijten.com/winglet/18quiesc01.htm) » [Quiescence Search](/Quiescence_Search "Quiescence Search"), [MVV-LVA](/MVV-LVA "MVV-LVA"), [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation")
:   [19 Null move pruning](http://web.archive.org/web/20120112113901/http://www.sluijten.com/winglet/19nullmove01.htm) » [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
:   [20 Time control and running test suites](http://web.archive.org/web/20120111180207/http://www.sluijten.com/winglet/20timecontrol01.htm) » [Time Management](/Time_Management "Time Management")
:   [21 Connecting to Winboard](http://web.archive.org/web/20120109090839/http://www.sluijten.com/winglet/21winboard01.htm) » [CECP](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [WinBoard](/WinBoard "WinBoard")

## Misc

- [Winglet from Wingtip device - Wikipedia](https://en.wikipedia.org/wiki/Wingtip_device#Winglet)
- [Winglets and Sharklets | The Flying Engineer](http://theflyingengineer.com/flightdeck/winglets-and-sharklets/)
- [Boeing 737 Winglets](http://www.b737.org.uk/winglets.htm)

# References

1. [↑](#cite_ref-1) Winglet with attached [tufts](https://en.wikipedia.org/wiki/Tuft_%28aeronautics%29) of an [KC-135A](https://en.wikipedia.org/wiki/Boeing_KC-135_Stratotanker) during [NASA](https://en.wikipedia.org/wiki/NASA) Winglet stu dy 1979. The tufts are needed to measure the [airflow](https://en.wikipedia.org/wiki/Airflow), [Winglet from Wingtip device - Wikipedia](https://en.wikipedia.org/wiki/Wingtip_device#Winglet), [KC-135 EC79-11481: KC-135A in flight - closeup of winglet with attached tufts](http://www.dfrc.nasa.gov/Gallery/Photo/KC-135/HTML/EC79-11481.html), August 20, 1979
2. [↑](#cite_ref-2) [Winglet, Writing a Chess Program in 99 Steps](http://web.archive.org/web/20120621100214/http://www.sluijten.com/winglet/) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), hosted by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
3. [↑](#cite_ref-3) [Writing a chess program in xx steps](http://www.talkchess.com/forum/viewtopic.php?t=38787) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [CCC](/CCC "CCC"), April 18, 2011
4. [↑](#cite_ref-4) [Winglet, Writing a Chess Program in 99 Steps](http://web.archive.org/web/20120621100214/http://www.sluijten.com/winglet/) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), hosted by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
5. [↑](#cite_ref-5) [Index of /chess/engines/Jim Ablett/WING](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/WING/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
6. [↑](#cite_ref-6) [Writing a chess program in 99 steps - Move generation for sliding pieces](http://web.archive.org/web/20120621060943/http://www.sluijten.com/winglet/11movegen03.htm#Move_generation_for_sliding_pieces_-_magic_bitboards_) by [Stef Luijten](/index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
7. [↑](#cite_ref-7) [Chesser: A Chess Engine derived from wingletx](http://www.talkchess.com/forum/viewtopic.php?t=54740) by [Syed Fahad](/Syed_Fahad "Syed Fahad"), [CCC](/CCC "CCC"), December 24, 2014
8. [↑](#cite_ref-8) [ucarion/godot · GitHub](https://github.com/ucarion/godot)
9. [↑](#cite_ref-9) [kenshinthebattosai/Kenny · GitHub](https://github.com/kenshinthebattosai/kenny)
10. [↑](#cite_ref-10) [New Winboard Engine 'Kenny' - JA builds available](http://www.talkchess.com/forum/viewtopic.php?t=46814) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [CCC](/CCC "CCC"), January 08, 2013
11. [↑](#cite_ref-11) [Re: where to start chess programming?](http://www.talkchess.com/forum/viewtopic.php?t=52709&start=18) by [Marco Belli](/Marco_Belli "Marco Belli"), [CCC](/CCC "CCC"), June 22, 2014

**[Up one Level](/Engines "Engines")**