# Zochova

Source: https://www.chessprogramming.org/Zochova

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Zochova**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Zochova_1.jpg/330px-Zochova_1.jpg)](/File:Zochova_1.jpg)

Zochova Street No. 1 [[1]](#cite_note-1)

**Zochova**,  
an [open source chess engine](/Category:Open_Source "Category:Open Source") under the [GNU General Public License](/Free_Software_Foundation#GPL "Free Software Foundation") by [Gabor Buella](/Gabor_Buella "Gabor Buella") written in [C++](/Cpp "Cpp"), compliant with the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol").
Zochova is a [bitboard](/Bitboards "Bitboards") engine, and requires some [Boost libraries](https://en.wikipedia.org/wiki/Boost_%28C%2B%2B_libraries%29), such as Boost.Signals
[[2]](#cite_note-2),
an implementation of managed [Signals and slots](https://en.wikipedia.org/wiki/Signals_and_slots) for [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern), and uses the [ProDeo](/ProDeo "ProDeo") open source code [opening book](/Opening_Book "Opening Book") by [Ed Schröder](/Ed_Schroder "Ed Schroder") [[3]](#cite_note-3).
[Sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") are calculated with some [bit-twiddling](/Bit-Twiddling "Bit-Twiddling") and loops on the fly
[[4]](#cite_note-4). Its [search](/Search "Search") is basically [PVS](/Principal_Variation_Search "Principal Variation Search") with [verified nullmove pruning](/Null_Move_Pruning#ZugzwangVerification "Null Move Pruning"), and [late move reductions](/Late_Move_Reductions "Late Move Reductions").

# Forum Posts

- [Zochova chess engine](http://www.talkchess.com/forum/viewtopic.php?t=30009) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](/CCC "CCC"), October 06, 2009
- [Please, Cluster Toga && Zochova](http://www.talkchess.com/forum/viewtopic.php?t=46179) by [Arturo Ochoa](/Arturo_Ochoa "Arturo Ochoa"), [CCC](/CCC "CCC"), November 28, 2012 » [Cluster Toga](/Cluster_Toga "Cluster Toga")

# External Links

## Chess Engine

- [zochova download | SourceForge.net](https://sourceforge.net/projects/zochova/)
- [Zochova](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/ZOCHOVA/) compiled by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")

## Misc

- [Zochova (Bratislava) from Wikipedia](https://en.wikipedia.org/wiki/Zochova)
- [Zochova X](http://zochova.com/index-en.php)

# References

1. [↑](#cite_ref-1) [Academy of Performing Arts](https://en.wikipedia.org/wiki/Academy_of_Performing_Arts_in_Bratislava) in [Bratislava](https://en.wikipedia.org/wiki/Bratislava), Zochova Street No. 1, [image](https://commons.wikimedia.org/wiki/File:Zochova_1.jpg) by Wizzard, February 2008, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Chapter 24. Boost.Signals - 1.52.0](https://www.boost.org/doc/libs/1_52_0/doc/html/signals.html)
3. [↑](#cite_ref-3) [Zochova/RebelBook.cpp](https://sourceforge.net/p/zochova/code/HEAD/tree/RebelBook.cpp)
4. [↑](#cite_ref-4) [Zochowa/bitboardmoves.cpp](https://sourceforge.net/p/zochova/code/HEAD/tree/bitboardmoves.cpp)

**[Up one level](/Engines "Engines")**