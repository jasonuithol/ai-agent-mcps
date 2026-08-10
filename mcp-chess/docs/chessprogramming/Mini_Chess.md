# Mini Chess

Source: https://www.chessprogramming.org/Mini_Chess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Mini Chess**

[![](/images/c/cf/Acetronic.jpg)](http://www.flickr.com/photos/10261668@N05/859036624/in/set-72157600922172552/)

Acetronic aka Mini Chess [[1]](#cite_note-1)

**Mini Chess**, (SciSys Mini Chess)  
along with [Junior Chess](#Junior) and [Graduate Chess](#Graduate), a series of portable [dedicated chess computers](/Dedicated_Chess_Computers "Dedicated Chess Computers") manufactured and sold by [SciSys](/Saitek "Saitek"), first released in early 1981. The computers had a [Hitachi](https://en.wikipedia.org/wiki/Hitachi_Ltd.) [HD44801](/HMCS4xC "HMCS4xC") 4-bit [CMOS](https://en.wikipedia.org/wiki/CMOS) [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) with 2K of 10-bit word [ROM](/Memory#ROM "Memory"), 128 10-bit words of pattern ROM supported by pattern generation instructions with table lookup capability, and **160** [nibbles](/Nibble "Nibble") or digits (80 [bytes](/Byte "Byte")) of [RAM](/Memory#RAM "Memory"), running at 400 KHz. The programs were delivered by [Philidor Software](/Philidor_Software "Philidor Software"), developed by [Mark Taylor](/Mark_Taylor "Mark Taylor") under guidance of [David Levy](/David_Levy "David Levy"), who contributed the basic chess algorithm [[2]](#cite_note-2) including [promotions](/Promotions "Promotions"), [en passant](/En_passant "En passant"), and [castling](/Castling "Castling"), and even managed [mate](/Checkmate "Checkmate") with KR v K in some versions all in astonishing 160 nibbles of RAM. A piece of work that Mark Taylor is still rightly proud of today [[3]](#cite_note-3).

# 160 Nibble Challenge

160 nibbles of RAM is a challenge. The HD44801 has an internal 4 word return [stack](/Stack "Stack"), so one may assume a maximum [search depth](/Depth "Depth") of 4, but one has to be careful with external [interrupts](https://en.wikipedia.org/wiki/Interrupt), i. e. from keyboard or timer, since they cause an implicit call to an [interrupt handler](https://en.wikipedia.org/wiki/Interrupt_handler), pushing the instruction pointer on the internal stack as well, with the possibility to cause an [stack overflow](https://en.wikipedia.org/wiki/Stack_overflow). One may better implement a simple [iterative search](/Iterative_Search "Iterative Search"), called after [making a move](/Make_Move "Make Move") at the [root](/Root "Root") within its [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework.

The board is apparently represented by an [incremental updated](/Incremental_Updates "Incremental Updates") [8x8](/8x8_Board "8x8 Board") [array](/Array "Array") of nibbles. The ply stack entry consists of [en passant](/En_passant "En passant")- and [castling rights](/Castling_Rights "Castling Rights"), the [move](/Moves "Moves") to [unmake](/Unmake_Move "Unmake Move"), likely 3 nibbles [12-bit from-to encoding](/Encoding_Moves "Encoding Moves") also interpreted as state of a deterministic [move generator](/Move_Generation "Move Generation"), and [alpha](/Alpha "Alpha"), while [beta](/Beta "Beta") might be restored from alpha of the previous ply in [negamax](/Negamax "Negamax") manner. Of course, with such a minimalistic design, [move ordering](/Move_Ordering "Move Ordering") is a big issue, and how to utilize the remaining nibbles in a most efficient manner, considering [MVV-LVA](/MVV-LVA "MVV-LVA") and possibly maintaining a small [triangular PV-table](/Triangular_PV-Table "Triangular PV-Table") say for four plies.

# Derivatives

**Mini Chess** was the basic model with [keypad](https://en.wikipedia.org/wiki/Keypad) and [seven-segment](https://en.wikipedia.org/wiki/Seven-segment_display) [LCD](https://en.wikipedia.org/wiki/Liquid_crystal_display) to display move coordinates and small status messages, also sold in the UK under the marketing company name *Acetronic*.

## Junior Chess

[![](/images/e/e1/JuniorChess.jpg)](http://www.flickr.com/photos/10261668@N05/858189105/in/set-72157600922172552)

Junior Chess [[4]](#cite_note-4)

**Junior Chess** had almost the same hardware and program than Mini Chess, but an integrated travel pegboard.

## Graduate Chess

Like [Junior Chess](#Junior), **Graduate Chess** was almost identical to Mini Chess, also with an integrated travel pegboard.

## CXG

The 4-bit program initiated [Eric White's](/Eric_White "Eric White") involvement in computer chess business and long time collaboration with Levy, when [Hong Kong](https://en.wikipedia.org/wiki/Hong_Kong) based manufacturer *White and Allcock*, forerunner of [Newcrest Technology](/Newcrest_Technology "Newcrest Technology") introduced the [CXG](/Newcrest_Technology#CXG "Newcrest Technology") brand in 1981 with [CXG Sensor Computachess](/CXG_Sensor_Computachess "CXG Sensor Computachess") [[5]](#cite_note-5) [[6]](#cite_note-6). It was further adapted for the more advanced **HMCS40** 4-bit singlechip processor [[7]](#cite_note-7).

## Chess Cards

[![](/images/b/b0/FidelityChessCard.JPG)](http://www.flickr.com/photos/10261668@N05/2071464244/in/set-72157600922174174)

Fidelity Chess Card [[8]](#cite_note-8)

In the late 80 and early 90, the 4-Bit program appeared in low cost chess card computers by [CXG](/Newcrest_Technology#CXG "Newcrest Technology") [[9]](#cite_note-9) and [Fidelity Electronics](/Fidelity_Electronics "Fidelity Electronics") [[10]](#cite_note-10), at that time already acquired by [Hegener & Glaser](/Hegener_%26_Glaser "Hegener & Glaser").

# See also

- [Chess Champion Pocket Chess](/Chess_Champion_Pocket_Chess "Chess Champion Pocket Chess")
- [Junior](/Junior "Junior")
- [Mini](/Mini "Mini")
- [Move Generation with 256 bytes RAM or less?](/Sensor_Chess#MoveGeneration "Sensor Chess")
- [Novag Micro Chess](/Novag_Micro_Chess "Novag Micro Chess")
- [Philidor Software](/Philidor_Software "Philidor Software")

# External Links

- [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [Scisys and Novag : The Early Years](http://www.chesscomputeruk.com/html/scisys_and_novag___the_early_y.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [Scisys/Saitek | Photo collection](http://www.flickr.com/photos/10261668@N05/sets/72157600922172552/) by [Chewbanta](/Steve_Blincoe "Steve Blincoe")

## Mini Chess

- [Mini Chess](http://www.chesscomputeruk.com/html/mini_chess.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [Mini Chess | My Chess Computers](http://electronicchess.free.fr/prehistory.html#minichess)
- [SciSys Mini Chess](http://www.schach-computer.info/wiki/index.php/SciSys_Mini_Chess) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)

## Junior Chess

- [Junior Chess](http://www.chesscomputeruk.com/html/junior_chess.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [Scisys Junior Chess | My Chess Computers](http://electronicchess.free.fr/prehistory.html#juniorchess2)
- [SciSys Junior Chess](http://www.schach-computer.info/wiki/index.php/SciSys_Junior_Chess) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)

## Graduate Chess

- [Graduate Chess](http://www.chesscomputeruk.com/html/graduate_chess.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [Acetronic Graduate Chess | My Chess Computers](http://electronicchess.free.fr/prehistory.html#acetronic)

## Chess Cards

- [Fidelity Chess Card Electronic Chess Computer](http://www.spacious-mind.com/html/chess_card.html) from [The Spacious Mind](/The_Spacious_Mind "The Spacious Mind")
- [Ismenio's chess computer collection | Fidelity Chess Card 6115](http://www.ismenio.com/chess_fidelity_chess_card.html)
- [CXG Pocket Chess](http://www.schach-computer.info/wiki/index.php/CXG_Pocket_Chess) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
- [CXG Sphinx Chess Card](http://www.schach-computer.info/wiki/index.php/CXG_Sphinx_Chess_Card) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
- [Fidelity Chess Card](http://www.schach-computer.info/wiki/index.php/Fidelity_Chess_Card) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
- [Fidelity Chess Pal](http://www.schach-computer.info/wiki/index.php/Fidelity_Chess_Pal) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
- [Fidelity Micro Chess Challenger](http://www.schach-computer.info/wiki/index.php/Fidelity_Micro_Chess_Challenger) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)

# References

1. [↑](#cite_ref-1) [Acetronic](http://www.flickr.com/photos/10261668@N05/859036624/in/set-72157600922172552/) from [Scisys/Saitek | Photo collection](http://www.flickr.com/photos/10261668@N05/sets/72157600922172552/) by [Chewbanta](/Steve_Blincoe "Steve Blincoe")
2. [↑](#cite_ref-2) [David Levy interview](http://www.schach-computer.info/wiki/index.php/Levy,_David) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
3. [↑](#cite_ref-3) [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
4. [↑](#cite_ref-4) [Junior Chess](http://www.flickr.com/photos/10261668@N05/858189105/in/set-72157600922172552) with [FIDE](/FIDE "FIDE") recommendation for novice and junior chess players, [Scisys/Saitek | Photo collection](http://www.flickr.com/photos/10261668@N05/sets/72157600922172552/) by [Chewbanta](/Steve_Blincoe "Steve Blincoe")
5. [↑](#cite_ref-5) [CXG Sensor Computachess](http://www.schach-computer.info/wiki/index.php/CXG_Sensor_Computachess) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
6. [↑](#cite_ref-6) [CXG Pocket Chess](http://www.schach-computer.info/wiki/index.php/CXG_Pocket_Chess) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
7. [↑](#cite_ref-7) [HD614048\_511862.PDF Datasheet Download --- IC-ON-LINE](http://www.ic-on-line.cn/view_download.php?id=1124980&file=0065%5Chd614048_511862.pdf)
8. [↑](#cite_ref-8) [Fidelity Chess Card](http://www.flickr.com/photos/10261668@N05/2071464244/in/set-72157600922174174) from [Exotic: Photo collection](http://www.flickr.com/photos/10261668@N05/sets/72157600922174174/with/2071464268/) by [Chewbanta](/Steve_Blincoe "Steve Blincoe")
9. [↑](#cite_ref-9) [CXG Sphinx Chess Card](http://www.schach-computer.info/wiki/index.php/CXG_Sphinx_Chess_Card) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
10. [↑](#cite_ref-10) [Fidelity Chess Card](http://www.schach-computer.info/wiki/index.php/Fidelity_Chess_Card) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)

**[Up one Level](/Engines "Engines")**