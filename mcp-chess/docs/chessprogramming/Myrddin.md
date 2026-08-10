# Myrddin

Source: https://www.chessprogramming.org/Myrddin

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Myrddin**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Llyfr_Du_Caerfyrddin_t1.jpg/330px-Llyfr_Du_Caerfyrddin_t1.jpg)](/File:Llyfr_Du_Caerfyrddin_t1.jpg)

[Page 1](https://en.wikipedia.org/wiki/File:Llyfr_Du_Caerfyrddin_t1.jpg) of [Black Book of Carmarthen](https://en.wikipedia.org/wiki/Black_Book_of_Carmarthen) [[1]](#cite_note-1)

**Myrddin**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](/WinBoard "WinBoard") compliant chess engine by [John Merlino](/John_Merlino "John Merlino"). Myrddin started its life in 2009 as a [0x88](/0x88 "0x88") engine with rudimentary [evaluation](/Evaluation "Evaluation") based on [material](/Material "Material") and [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") [[2]](#cite_note-2) , and was converted to [bitboards](/Bitboards "Bitboards") in 2012 with v0.86. [Search](/Search "Search") is basically [alpha-beta](/Alpha-Beta "Alpha-Beta") with generally conservative [extensions](/Extensions "Extensions") and [reductions](/Reductions "Reductions"). Myrddin's [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") implementation is based on pseudo-code by [Andres Valverde](/Andres_Valverde "Andres Valverde") [[3]](#cite_note-3).

# Myrddin 0.87

Myrddin **0.87**, released in January 2015, features a [lazy parallel search](/Lazy_SMP "Lazy SMP") using [processes](/Process "Process") and a [shared hash table](/Shared_Hash_Table "Shared Hash Table") [[4]](#cite_note-4), based on an idea from [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller").

# Myrddin 0.88

Myrddin **0.88**, released in July 2021, is about 110 ELO stronger than v0.87 at 1 CPU and about 100 ELO stronger at 4 CPUs.

# Etymology

The program's name is related to its author's last name [Merlino](https://it.wikipedia.org/wiki/Mago_Merlino), the [Italian](https://en.wikipedia.org/wiki/Italian_language) equivalent of [Merlin](https://en.wikipedia.org/wiki/Merlin) [[5]](#cite_note-5) , a legendary figure best known as the [wizard](/Category:Magic "Category:Magic") featured in the [Arthurian legend](/Category:Arthurian_Legend "Category:Arthurian Legend"), derived from the [Welsh](https://en.wikipedia.org/wiki/Welsh_language) Myrddin, the name of the bard [Myrddin Wyllt](https://en.wikipedia.org/wiki/Myrddin_Wyllt).

# See also

- [The King](/The_King "The King")

# Forum Posts

## 2009

- [Introducing Myrddin v0.0000001a](http://www.talkchess.com/forum/viewtopic.php?t=26729) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), February 24, 2009
- [Myrddin v0.80 Alpha 1 release](http://www.talkchess.com/forum/viewtopic.php?t=26935) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), May 09, 2009
- [Myrddin v0.81 Alpha 2 release](http://www.talkchess.com/forum/viewtopic.php?t=28154) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), May 29, 2009
- [Myrddin 0.82 release](http://www.talkchess.com/forum/viewtopic.php?t=29892) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), September 27, 2009

## 2010 ...

- [Myrddin 0.83 release](http://www.talkchess.com/forum/viewtopic.php?t=32857) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), February 23, 2010
- [Myrddin 0.84 release](http://www.talkchess.com/forum/viewtopic.php?t=36128) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), September 20, 2010
- [Myrddin 0.85 release](http://www.talkchess.com/forum/viewtopic.php?t=38965) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), May 03, 2011
- [Re: Programmers: what's the story behind the name of your engine](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410903&t=39407) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), June 21, 2011
- [Myrddin 0.86 release](http://www.talkchess.com/forum/viewtopic.php?t=46541) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), December 22, 2012
- [SMP and pondering](http://www.talkchess.com/forum/viewtopic.php?t=51198) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), February 08, 2014 » [Parallel Search](/Parallel_Search "Parallel Search"), [Pondering](/Pondering "Pondering")
- [Myrddin 0.87 release](http://www.talkchess.com/forum/viewtopic.php?t=55093) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), January 25, 2015

## 2020 ...

- [Working on Myrddin again](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77567) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), June 28, 2021
- [Myrddin v0.88 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77754) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), July 18, 2021

# External Links

## Chess program

- [Myrddin](http://computer-chess.org/doku.php?id=computer_chess:engines:myrddin:index) by [John Merlino](/John_Merlino "John Merlino"), [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home) by [Ron Murawski](/Ron_Murawski "Ron Murawski")
- [Myrddint](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Myrddin&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](/CCRL "CCRL")

## Misc

- [Myrddin (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Myrddin_%28disambiguation%29)
- [Myrddin Wyllt from Wikipedia](https://en.wikipedia.org/wiki/Myrddin_Wyllt)
- [Merlin from Wikipedia](https://en.wikipedia.org/wiki/Merlin)
- [Mago Merlino from Wikipedia.it](http://it.wikipedia.org/wiki/Mago_Merlino) (Italian)
- [Prophetiae Merlini from Wikipedia](https://en.wikipedia.org/wiki/Prophetiae_Merlini)
- [Myrddin & Merlin: A Guide to the Early Evolution of the Merlin Legend](http://www.arthuriana.co.uk/n&q/myrddin.htm) from [Arthuriana](http://www.arthuriana.co.uk/index.html) by [Thomas Green](http://www.arthuriana.co.uk/contact.htm)
- [Theosophy Avalon / Ynys Witrin - The Theosophy Wales King Arthur Pages - Vortigern's Stronghold Dinas Emrys](http://www.walestheosophy.co.uk/avalondinasemrys.htm)
- [The Myrddin Falcon](http://www.santharia.com/bestiary/myrddin_falcon.htm) by [Bard Judith](http://www.santharia.com/team/bard_judith.htm)
- [The Story of Myrddin Wyllt](http://www.maryjones.us/ctexts/myrddin.html) by [Elis Gruffudd](https://en.wikipedia.org/wiki/Elis_Gruffydd), 16th Century
- [Soft Machine](/Category:Soft_Machine "Category:Soft Machine") - The Tale of [Taliesin](https://en.wikipedia.org/wiki/Taliesin), from [Softs](https://en.wikipedia.org/wiki/Softs), 1976, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   Lineup: [Roy Babbington](/Category:Roy_Babbington "Category:Roy Babbington"), [John Etheridge](https://en.wikipedia.org/wiki/John_Etheridge), [John Marshall](/Category:John_Marshall "Category:John Marshall"), [Karl Jenkins](/Category:Karl_Jenkins "Category:Karl Jenkins")

# References

1. [↑](#cite_ref-1) [Page 1](https://en.wikipedia.org/wiki/File:Llyfr_Du_Caerfyrddin_t1.jpg) of [John Gwenogvryn Evans'](https://en.wikipedia.org/wiki/John_Gwenogvryn_Evans) edition (1907) of the [Black Book of Carmarthen](https://en.wikipedia.org/wiki/Black_Book_of_Carmarthen) (1250), being the [Ymddiddan](https://en.wikipedia.org/wiki/Peredur) (dialogue) between [Myrddin](https://en.wikipedia.org/wiki/Myrddin_Wyllt) and [Taliesin](https://en.wikipedia.org/wiki/Taliesin)
2. [↑](#cite_ref-2) [Introducing Myrddin v0.0000001a](http://www.talkchess.com/forum/viewtopic.php?t=26729) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), February 24, 2009
3. [↑](#cite_ref-3) [Myrddin](http://computer-chess.org/doku.php?id=computer_chess:engines:myrddin:index) by [John Merlino](/John_Merlino "John Merlino"), [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home) by [Ron Murawski](/Ron_Murawski "Ron Murawski")
4. [↑](#cite_ref-4) [Myrddin 0.87 release](http://www.talkchess.com/forum/viewtopic.php?t=55093) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), January 25, 2015
5. [↑](#cite_ref-5) [Re: Programmers: what's the story behind the name of your engine](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410903&t=39407) by [John Merlino](/John_Merlino "John Merlino"), [CCC](/CCC "CCC"), June 21, 2011

**[Up one Level](/Engines "Engines")**