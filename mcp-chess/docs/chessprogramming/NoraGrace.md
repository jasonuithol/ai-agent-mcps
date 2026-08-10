# NoraGrace

Source: https://www.chessprogramming.org/NoraGrace

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* NoraGrace**

[![](/images/c/cd/NoraGrace.png)](/File:NoraGrace.png)

NoraGrace Logo [[1]](#cite_note-1)

**NoraGrace**,  
a [WinBoard](/WinBoard "WinBoard") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Eric Oldre](/Eric_Oldre "Eric Oldre"),
written in [C#](/C_sharp "C sharp") and first released in June 2014 under the [MIT License](/Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology"). NoraGrace evolved from a C# port of [Sinobyl](/Sinobyl "Sinobyl") [[2]](#cite_note-2), and is dedicated to *Nora Grace Oldre* who was taken from Eric and his wife unexpectedly a few days before she was due to be born [[3]](#cite_note-3) [[4]](#cite_note-4) .

# Description

## Board Representation

Like [Sinobyl](/Sinobyl "Sinobyl"), NoraGrace relies on [bitboards](/Bitboards "Bitboards"), and further has an [8x8 mailbox](/8x8_Board "8x8 Board").
It uses [magic bitboards](/Magic_Bitboards "Magic Bitboards") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") - factors were calculated from sparse 64-bit randoms.
[BitScan](/BitScan "BitScan") is implemented via 32-bit [De Bruijn multiplication](/BitScan#DeBruijnMultiplation "BitScan") to conditionally branch on low and high [double words](/Double_Word "Double Word").
[Bitboard serialization](/Bitboard_Serialization "Bitboard Serialization") applies the C# [yield statement](https://en.wikipedia.org/wiki/Generator_%28computer_programming%29#C.23)
[[5]](#cite_note-5),
which is further used in various [move generation](/Move_Generation "Move Generation") routines. NoraGrace's [square mapping](/Square_Mapping_Considerations "Square Mapping Considerations") has [ranks](/Ranks "Ranks") from 8 to 1 mapped to 0-7 at the [big-end](/Big-endian "Big-endian") over [files](/Files "Files") from 'a' to 'h', square zero is a8:

[![Berlef.JPG](/images/6/69/Berlef.JPG)](/Bibob#BERLEF "Bibob#BERLEF")

NoraGrace's [BERLEF Mapping](/Bibob#BERLEF "Bibob")

## Search

NoraGrace applies [negamax](/Negamax "Negamax") [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table") and [quiescence search](/Quiescence_Search "Quiescence Search") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](/Aspiration_Windows "Aspiration Windows"), enhanced by [adaptive null move pruning](/Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") with [verification search](/Null_Move_Pruning#ZugzwangVerification "Null Move Pruning") in the [endgame](/Endgame "Endgame"), [extensions](/Extensions "Extensions") if [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") > 0 for [checks](/Check_Extensions "Check Extensions") and [pawns to 7th rank](/Passed_Pawn_Extensions "Passed Pawn Extensions"), [futility pruning](/Futility_Pruning "Futility Pruning") and [LMR](/Late_Move_Reductions "Late Move Reductions").

## Evaluation

[Evaluation](/Evaluation "Evaluation") takes [game phases](/Game_Phases "Game Phases") into account, using a [tapered eval](/Tapered_Eval "Tapered Eval") along with *PhasedScore* objects, interpreting the low and high 32-bit [double words](/Double_Word "Double Word") of a 64-bit long as two [SIMD](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") integers of an [endgame](/Endgame "Endgame") and [opening](/Opening "Opening") [score](/Score "Score").
Beside other features, NoraGrace considers [material](/Material "Material"), [piece-square tables](/Piece-Square_Tables "Piece-Square Tables"), [king safety](/King_Safety "King Safety"), [cached](/Pawn_Hash_Table "Pawn Hash Table") [pawn structure](/Pawn_Structure "Pawn Structure") and [mobility](/Mobility "Mobility").

# See also

- [Sinobyl](/Sinobyl "Sinobyl")

# Forum Posts

- [New open source engine in C# - NoraGrace](http://www.talkchess.com/forum/viewtopic.php?t=52700) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), June 20, 2014
- [NoraGrace 2.0 (c# engine)](http://www.talkchess.com/forum/viewtopic.php?t=54419) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), November 22, 2014

# External Links

## Chess Engine

- [Ericoldre/NoraGrace-Chess · GitHub](https://github.com/ericoldre/NoraGrace-Chess)
- [Releases · ericoldre/NoraGrace-Chess · GitHub](https://github.com/ericoldre/NoraGrace-Chess/releases)
- [NoraGrace](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=NoraGrace&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [List of Irish-language given names - Wikipedia](https://en.wikipedia.org/wiki/List_of_Irish-language_given_names)

# References

1. [↑](#cite_ref-1) Logo by [Graham Banks](/Graham_Banks "Graham Banks") from a picture of Nora Grace Oldre's footprints, [Release Release 1.0 of the NoraGrace Chess Engine · ericoldre/NoraGrace-Chess · GitHub](https://github.com/ericoldre/NoraGrace-Chess/releases/tag/v1.0), NoraGraceV10.zip/NoraGrace.png, [Re: Some others chess engines written in C#](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=576266&t=52700) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), June 29, 2014
2. [↑](#cite_ref-2) [trunk/Sinobyl | SVN | Assembla](https://www.assembla.com/code/sinobyl/subversion/nodes/129/trunk/Sinobyl)
3. [↑](#cite_ref-3) [New open source engine in C# - NoraGrace](http://www.talkchess.com/forum/viewtopic.php?t=52700) by [Eric Oldre](/Eric_Oldre "Eric Oldre"), [CCC](/CCC "CCC"), June 20, 2014
4. [↑](#cite_ref-4) [Perinatal mortality from Wikipedia](https://en.wikipedia.org/wiki/Perinatal_mortality)
5. [↑](#cite_ref-5) public static IEnumerable<Position> ToPositions(this Bitboard bitboard) in [Bitboard.cs](https://github.com/ericoldre/NoraGrace-Chess/blob/master/NoraGrace/NoraGrace.Engine/Bitboard.cs)

**[Up one Level](/Engines "Engines")**