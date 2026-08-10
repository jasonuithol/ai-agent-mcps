# Axon

Source: https://www.chessprogramming.org/Axon

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Axon**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Blausen_0657_MultipolarNeuron.png/330px-Blausen_0657_MultipolarNeuron.png)](/File:Blausen_0657_MultipolarNeuron.png)

Multipolar [neuron](https://en.wikipedia.org/wiki/Neuron) [[1]](#cite_note-1)

**Axon** (Geniss Axon),  
a chess engine by primary author [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") with chess knowledge and opening moves contributed by [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"). Geniss Axon, a plain [alpha-beta](/Alpha-Beta "Alpha-Beta") searcher whose development started in 2001, was written in compact 16-bit [8086](/8086 "8086") [assembly](/Assembly "Assembly"), also incorporated into the *Axon Benchmark* program, which is available from the [Arena](/Arena "Arena") site [[2]](#cite_note-2). The [benchmark](https://en.wikipedia.org/wiki/Benchmarking) indicates how well [x86](/X86 "X86") processors will support Axon's 16-bit instructions.

# Description

Axon used a 12x12 [mailbox](/Mailbox "Mailbox") to represent the board, and applies a unique [move repetition detection](/Repetitions#RepetitionofMoves "Repetitions") technique, as described by Vučković and Vidanović in 2004 [[3]](#cite_note-3). Further developments were Axon I, the successor of Geniss Axon XP, first using [null move pruning](/Null_Move_Pruning "Null Move Pruning") with [R](/Depth_Reduction_R "Depth Reduction R") = 2, the 32-bit port Axon II utilizing 64-bit [MMX](/MMX "MMX") extensions, and Axon 3 the serial program of the parallel chess system [Achilles](/Achilles "Achilles") [[4]](#cite_note-4) [[5]](#cite_note-5). In 2008, Vučković introduced the [Compact Chessboard Representation](/Nibble#ArrayOfNibbles "Nibble") as used in Axon [[6]](#cite_note-6) [[7]](#cite_note-7).

# See also

- [Achilles](/Achilles "Achilles")
- [SOMA](/SOMA "SOMA")

# Publications

- [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković"), [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović") (**2004**). *A New Approach to Draw Detection by Move Repetition in Computer Chess Programming.* CoRR cs.AI/0406038, [pdf](http://arxiv.org/ftp/cs/papers/0406/0406038.pdf) [[8]](#cite_note-8)
- [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2007**). *The Method of the Chess Search Algorithms - Parallelization using Two-Processor distributed System.* Facta Universitatis (Niš) Ser. Math. Inform. Vol. 22, No. 2, [pdf](http://facta.junis.ni.ac.rs/mai/mai222/f22-2-175-188.pdf)
- [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2007**). *Axon Development*. [pdf](http://chess.elfak.ni.ac.rs/axon.pdf) (Serbian)
- [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2008**). *The Compact Chessboard Representation*. [ICGA Journal, Vol. 31, No. 3](/ICGA_Journal#31_3 "ICGA Journal")
- [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2012**). *An Alternative Efficient Chessboard Representation based on 4-Bit Piece Coding*. [Yugoslav Journal of Operations Research, Vol. 22, No. 1](http://www.doiserbia.nb.rs/issue.aspx?issueid=1761), [pdf](http://www.doiserbia.nb.rs/img/doi/0354-0243/2012/0354-02431200011V.pdf)

# Forum Posts

- [Geniss Axon - a new chess program. Would your program play 15.Nd4?](https://www.stmintz.com/ccc/index.php?id=307016) by [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [CCC](/CCC "CCC"), July 18, 2003
- [Question about Axon Benchmark](https://www.stmintz.com/ccc/index.php?id=458033) by [Dagh Nielsen](/index.php?title=Dagh_Nielsen&action=edit&redlink=1 "Dagh Nielsen (page does not exist)"), [CCC](/CCC "CCC"), October 27, 2005

# External Links

- [Arena Chess GUI 3.0 - Axon, EloStat, Nalimov](http://www.playwitharena.com/?User_Files%2C_Engines:Axon%2C_EloStat%2C_Nalimov)
- [Axon from Wikipedia](https://en.wikipedia.org/wiki/Axon)
- [Axon (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Axon_%28disambiguation%29)

# References

1. [↑](#cite_ref-1) [Axon from Wikipedia](https://en.wikipedia.org/wiki/Axon)
2. [↑](#cite_ref-2) [Arena Chess GUI 3.0 - Axon, EloStat, Nalimov](http://www.playwitharena.com/?User_Files%2C_Engines:Axon%2C_EloStat%2C_Nalimov)
3. [↑](#cite_ref-3) [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković"), [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović") (**2004**). *A New Approach to Draw Detection by Move Repetition in Computer Chess Programming.* CoRR cs.AI/0406038, [pdf](http://arxiv.org/ftp/cs/papers/0406/0406038.pdf)
4. [↑](#cite_ref-4) [Achilles Home](http://chess.elfak.ni.ac.rs/)
5. [↑](#cite_ref-5) [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2007**). *Axon Development*. [pdf](http://chess.elfak.ni.ac.rs/axon.pdf) (Serbian)
6. [↑](#cite_ref-6) [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2008**). *The Compact Chessboard Representation*. [ICGA Journal, Vol. 31, No. 3](/ICGA_Journal#31_3 "ICGA Journal")
7. [↑](#cite_ref-7) [Vladan Vučković](/Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2012**). *An Alternative Efficient Chessboard Representation based on 4-Bit Piece Coding*. [Yugoslav Journal of Operations Research, Vol. 22, No. 1](http://www.doiserbia.nb.rs/issue.aspx?issueid=1761), [pdf](http://www.doiserbia.nb.rs/img/doi/0354-0243/2012/0354-02431200011V.pdf)
8. [↑](#cite_ref-8) [Draw Detection by Move Repetition Procedure -- Comments](https://www.stmintz.com/ccc/index.php?id=380201) by [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [CCC](/CCC "CCC"), August 01, 2004

**[Up one level](/Engines "Engines")**