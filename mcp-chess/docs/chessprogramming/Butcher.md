# Butcher

Source: https://www.chessprogramming.org/Butcher

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Butcher**

[File:11-alimenti,carni ovine, Taccuino Sanitatis, Casanatense 4182.jpg](/index.php?title=Special:Upload&wpDestFile=11-alimenti,carni_ovine,_Taccuino_Sanitatis,_Casanatense_4182.jpg "File:11-alimenti,carni ovine, Taccuino Sanitatis, Casanatense 4182.jpg")

14th-century butcher [[1]](#cite_note-1)

**Butcher** (Rzeźnik in Polish [[2]](#cite_note-2) )  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Marek Kołacz](/Marek_Ko%C5%82acz "Marek Kołacz"), written in [C](/C "C"), first released in September 2001 [[3]](#cite_note-3). Executables are available for [Windows](/Windows "Windows") and [Linux](/Linux "Linux"), early versions ran under [DOS](/MS-DOS "MS-DOS").

# Parallel Search

Since version 1.60, Butcher can perform a [parallel search](/Parallel_Search "Parallel Search") under [Windows](/Windows "Windows") using [processes](/Process "Process") and a [shared hash table](/Shared_Hash_Table "Shared Hash Table"). A master process spawns worker processes, which run independently without any supervision. The Master process prepares all the structures necessary to split the node and continues the search. Worker processes use existing "split nodes" to start their search and report the results. The master process is responsible for killing the workers upon exit [[4]](#cite_note-4).

# Tournament Play

Rzeźnik aka Butcher played all [Polish Computer Chess Championships](/Polish_Computer_Chess_Championship "Polish Computer Chess Championship"), and won its first edition, the [PCCC 2002](/PCCC_2002 "PCCC 2002"), and the open category of the [PCCC 2004](/PCCC_2004 "PCCC 2004") and [PCCC 2006](/PCCC_2006 "PCCC 2006") [[5]](#cite_note-5) , and otherwise was always a top scorer, at the [PCCC 2012](/PCCC_2012 "PCCC 2012") best Polish program.
Butcher further played multiple [CCT Tournaments](/CCT_Tournaments "CCT Tournaments") and had its tournament debut at the [CCT3](/CCT3 "CCT3") in May 2001.

# Publications

- [Maciej Szmit](/Maciej_Szmit "Maciej Szmit") (**2006**). *The 5th Polish Computer-Chess Championship: The Second Comeback of Butcher*. [ICGA Journal, Vol. 29, No. 4](/ICGA_Journal#29_4 "ICGA Journal") » [PCCC 2006](/PCCC_2006 "PCCC 2006")

# Forum Posts

- [New Butcher](https://www.stmintz.com/ccc/index.php?id=190209) by [Grzegorz Sidorowicz](/Grzegorz_Sidorowicz "Grzegorz Sidorowicz"), [CCC](/CCC "CCC"), September 24, 2001
- [Gauntlet Petir v2.0 and Butcher v1.53 with download](https://www.stmintz.com/ccc/index.php?id=400642) by [Karl-Heinz Söntges](/index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](/CCC "CCC"), December 13, 2004
- [Gauntlets Liste B 5' + 5" - Butcher v1.56 - games](https://www.stmintz.com/ccc/index.php?id=436144) by [Karl-Heinz Söntges](/index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](/CCC "CCC"), July 11, 2005

# External Links

- [Butcher homepage](http://butcher-chess.cba.pl/)

## Chess Engine

- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Butcher 1.61 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Butcher%201.61%2064-bit#Butcher_1_61_64-bit) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Butcher (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Butcher_%28disambiguation%29)
- [Butcher from Wikipedia](https://en.wikipedia.org/wiki/Butcher)

# References

1. [↑](#cite_ref-1) Butcher's [Tacuinum Sanitatis](https://en.wikipedia.org/wiki/Tacuinum_Sanitatis) [Casanatensis](https://en.wikipedia.org/wiki/Biblioteca_Casanatense), This picture is showing a 14th-century butcher making his trade in a traditional manner - unknown master, [Butcher from Wikipedia](https://en.wikipedia.org/wiki/Butcher)
2. [↑](#cite_ref-2) [Rzeźnictwo from Wikipedia.pl](http://pl.wikipedia.org/wiki/Rze%C5%BAnictwo) (Polish)
3. [↑](#cite_ref-3) [New Butcher](https://www.stmintz.com/ccc/index.php?id=190209) by [Grzegorz Sidorowicz](/Grzegorz_Sidorowicz "Grzegorz Sidorowicz"), [CCC](/CCC "CCC"), September 24, 2001
4. [↑](#cite_ref-4) [Butcher's Homepage](http://markol4.republika.pl/) (expired link)
5. [↑](#cite_ref-5) [Maciej Szmit](/Maciej_Szmit "Maciej Szmit") (**2006**). *The 5th Polish Computer-Chess Championship: The Second Comeback of Butcher*. [ICGA Journal, Vol. 29, No. 4](/ICGA_Journal#29_4 "ICGA Journal")

**[Up one Level](/Engines "Engines")**