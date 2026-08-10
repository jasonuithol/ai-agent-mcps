# MBChess

Source: https://www.chessprogramming.org/MBChess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* MBChess**

**MBChess**,  
a chess program by [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé"), written in [C](/C "C"). It was primarily used as test-bed for hardware based [FPGA](/FPGA "FPGA") [move generation](/Move_Generation "Move Generation"), which was subject of Boulé's Masters thesis in 2002 [[1]](#cite_note-1). The FPGA approach performs a [Belle](/Belle#Hardware "Belle") like move generation method with find **victim** and find **aggressor** cycles in [MVV-LVA](/MVV-LVA "MVV-LVA") manner. The move generator includes a [PCI](https://en.wikipedia.org/wiki/Conventional_PCI) interface to connect it to the PC running MBChess. Communication is done via different commands, such as to instruct the move generator to [undo](/Unmake_Move "Unmake Move") the currently stored move, generate and return the next move and [execute](/Make_Move "Make Move") that move on its internal FPGA [board representation](/Board_Representation "Board Representation"). In total, 10,804 out of 18,816 [logic cells](/FPGA#LC "FPGA") of a [Xilinx](https://en.wikipedia.org/wiki/Xilinx) XCV800 [[2]](#cite_note-2) were used, 10,104 as [LUT](https://en.wikipedia.org/wiki/Lookup_table#Hardware_LUTs), 700 as RAM [[3]](#cite_note-3).

# Block Diagram

[![FPGAChessSquares.JPG](/images/3/3f/FPGAChessSquares.JPG)](/File:FPGAChessSquares.JPG)

A block diagram of a chess square with transmitter (TX) and the receiver (RX) [[4]](#cite_note-4)

# Hardware vs. Software

MBChess is a very basic chess program, without [opening book](/Opening_Book "Opening Book"), only rudimentary [evaluation](/Evaluation "Evaluation"), i.e. almost no [king safety](/King_Safety "King Safety"), and without [null move pruning](/Null_Move_Pruning "Null Move Pruning"). The reported ratings obtained on [FICS](/index.php?title=FICS&action=edit&redlink=1 "FICS (page does not exist)") are 1844 and 1692 for MBChess+FPGA and MBChess respectively [[5]](#cite_note-5). Marc Boulé further concluded a bit disappointing results [[6]](#cite_note-6). Even though the pure move generation speed is almost 5 times faster, when using full heuristics, this drops to about 2 times faster. He found that his FPGA move generator, can at best, make/unmake 10M moves a second, which due to PCI bus saturation, will not even transfer from FPGA to PC. [Crafty](/Crafty "Crafty") could already make/unmake 30M moves a second on that machine, which implies the only way to speedup Crafty would be to make an FPGA with search and evaluation.

# Publications

- [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](/McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](/Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](/Monroe_Newborn "Monroe Newborn"))
- [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](/Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [McGill University](/McGill_University "McGill University")
- [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](/Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [ICGA Journal, Vol. 25, No. 2](/ICGA_Journal#25_2 "ICGA Journal")

# Forum Posts

- [A Response From Marc Boule](https://www.stmintz.com/ccc/index.php?id=221124) by [Slater Wold](/index.php?title=Slater_Wold&action=edit&redlink=1 "Slater Wold (page does not exist)"), [CCC](/CCC "CCC"), April 02, 2002
- [Re: Thesis by Marc Boule](https://www.stmintz.com/ccc/index.php?id=250746) by [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé"), [CCC](/CCC "CCC"), September 07, 2002
- [Re: Thesis by Marc Boule](https://www.stmintz.com/ccc/index.php?id=251005) by [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé"), [CCC](/CCC "CCC"), September 08, 2002

# External Links

- [FICS Games Database - Statistics for mbchess](http://www.ficsgames.org/cgi-bin/search.cgi?player=mbchess;statsyear=9999)

# References

1. [↑](#cite_ref-1) [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](/McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](/Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](/Monroe_Newborn "Monroe Newborn")
2. [↑](#cite_ref-2) [Re: Attention - Slater Wold](https://www.stmintz.com/ccc/index.php?id=292813) by [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé"), [CCC](/CCC "CCC"), April 10, 2003
3. [↑](#cite_ref-3) [Re: Thesis by Marc Boule](https://www.stmintz.com/ccc/index.php?id=251005) by [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé"), [CCC](/CCC "CCC"), September 08, 2002
4. [↑](#cite_ref-4) [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](/McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](/Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](/Monroe_Newborn "Monroe Newborn"))
5. [↑](#cite_ref-5) [Marc Boulé](/Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](/Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [ICGA Journal, Vol. 25, No. 2](/ICGA_Journal#25_2 "ICGA Journal")
6. [↑](#cite_ref-6) [A Response From Marc Boule](https://www.stmintz.com/ccc/index.php?id=221124) by [Slater Wold](/index.php?title=Slater_Wold&action=edit&redlink=1 "Slater Wold (page does not exist)"), [CCC](/CCC "CCC"), April 02, 2002

**[Up one Level](/Engines "Engines")**