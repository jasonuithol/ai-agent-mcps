# Jaglavak

Source: https://www.chessprogramming.org/Jaglavak

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Jaglavak**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Dorylus_gribodoi_casent0172627_dorsal_1.jpg/330px-Dorylus_gribodoi_casent0172627_dorsal_1.jpg)](/File:Dorylus_gribodoi_casent0172627_dorsal_1.jpg)

[Jaglavak](https://en.wikipedia.org/wiki/Jaglavak) [[1]](#cite_note-1)

**Jaglavak**,  
an experimental [UCI](/UCI "UCI") compliant [open source](/Category:Open_Source "Category:Open Source") chess engine under construction by [Stuart Riffle](/Stuart_Riffle "Stuart Riffle"), written in [C++](/Cpp "Cpp").
Like Stuart Riffle's earlier engine [Pigeon](/Pigeon "Pigeon"), Jaglavak uses [bitboards](/Bitboards "Bitboards"), and generates [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") by [Kogge-Stone](/Kogge-Stone_Algorithm "Kogge-Stone Algorithm") [[2]](#cite_note-2).
Unlike Pigeon, Jaglavak performs a [MCTS](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") and uses the [UCT](/UCT "UCT") formula to guide the selection of a node.
The random playouts of the simulation phase may be distributed on CPUs, utilizing [SIMD](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") aka [SSE2/4](/SSE2 "SSE2") [[3]](#cite_note-3), [AVX2](/AVX2 "AVX2") [[4]](#cite_note-4) or even [AVX-512](/AVX-512 "AVX-512") [[5]](#cite_note-5) instructions - or on [Nvidia](/Nvidia "Nvidia") [GPUs](/GPU "GPU") utilizing [CUDA](https://en.wikipedia.org/wiki/CUDA) [[6]](#cite_note-6).

# See also

- [Ant](/Ant "Ant")
- [Matant](/Matant "Matant")
- [Pigeon](/Pigeon "Pigeon")

# Forum Posts

- [Lazy-evaluation of futures for parallel work-efficient Alpha-Beta search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71058) by Percival Tiglao, [CCC](/CCC "CCC"), Jun 20, 2019

# External Links

## Chess Engine

- [GitHub - StuartRiffle/Jaglavak: MCTS chess engine for GPU and SIMD](https://github.com/StuartRiffle/Jaglavak)
- [GitHub - StuartRiffle/JaglavakTestData: Games, opening books, and test suites](https://github.com/StuartRiffle/JaglavakTestData)

## Misc

- [NOVA | Master of the Killer Ants | Jaglavak, Prince of Insects | PBS](https://www.pbs.org/wgbh/nova/ants/mofu.html) by [Christian Seignobos](https://www.cairn-int.info/publications-de-Christian-Seignobos--783.htm#)
- [Jaglavak, Prince of Insects - Jerome Raynaud](https://www.jeromeraynaud.com/en/portfolio-items/jaglavak-prince-insectes/)
- [Dorylus (Jaglavak) from Wikipedia](https://en.wikipedia.org/wiki/Dorylus)

# References

1. [↑](#cite_ref-1) Dorsal view of ant [Dorylus gribodoi](https://en.wikipedia.org/wiki/Dorylus_gribodoi) specimen [casent0172627](https://www.antweb.org/specimen.do?name=casent0172627), Author: [April Nobile](https://www.antweb.org/artist.do?id=69), February 12, 2007, [AntWeb.org](http://www.antweb.org/bigPicture.do?name=casent0172627&number=1&shot=d), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Jaglavak/BitBoard.h at master · StuartRiffle/Jaglavak · GitHub](https://github.com/StuartRiffle/Jaglavak/blob/master/Source/Chess/BitBoard.h)
3. [↑](#cite_ref-3) [Jaglavak/SSE4.h at master · StuartRiffle/Jaglavak · GitHub](https://github.com/StuartRiffle/Jaglavak/blob/master/Source/Player/SSE4.h)
4. [↑](#cite_ref-4) [Jaglavak/AVX2.h at master · StuartRiffle/Jaglavak · GitHub](https://github.com/StuartRiffle/Jaglavak/blob/master/Source/Player/AVX2.h)
5. [↑](#cite_ref-5) [Jaglavak/AVX512.h at master · StuartRiffle/Jaglavak · GitHub](https://github.com/StuartRiffle/Jaglavak/blob/master/Source/Player/AVX512.h)
6. [↑](#cite_ref-6) [Jaglavak/CudaPlayer.h at master · StuartRiffle/Jaglavak · GitHub](https://github.com/StuartRiffle/Jaglavak/blob/master/Source/Player/CudaPlayer.h)

**[Up one level](/Engines "Engines")**