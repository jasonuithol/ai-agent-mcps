# Zeta Dva

Source: https://www.chessprogramming.org/Zeta_Dva

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Zeta Dva**

[![](/images/2/28/ZetaDva_JA.jpg)](/File:ZetaDva_JA.jpg)

Logo by [Jim Ablett](/Jim_Ablett "Jim Ablett")

**Zeta Dva**,  
an amateur [open source chess engine](/Category:Open_Source "Category:Open Source") by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), written in [C](/C "C"). The engine has been in development since 2010 and was first released March 06, 2011 under the [GNU GPL](/Free_Software_Foundation#GPL "Free Software Foundation"), later MIT license.
Zeta Dva supports some basic commands of the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](/WinBoard "WinBoard") or [XBoard](/XBoard "XBoard").
Features are the use of [Bitboards](/Bitboards "Bitboards") and a simple [Evaluation](/Evaluation "Evaluation") .

# Features

- C99 + GCC vector-extensions
- XBoard (CECP v2) protocol
- Quad-Bitboards board presentation
- vectorized Kogge-Stone move generation
- single thread AlphaBeta search
- PolyGlot opening book support
- MIT license

# Origins Ideas

- [Quad-Bitboards](/Quad-Bitboards "Quad-Bitboards") idea by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg")
- [Kogge-Stone Algorithm](/Kogge-Stone_Algorithm "Kogge-Stone Algorithm") move generator based on work by [Steffan Westcott](/Steffan_Westcott "Steffan Westcott")

# Origins Code

- [Simplified Evaluation Function](/Simplified_Evaluation_Function "Simplified Evaluation Function") based on proposal by [Tomasz Michniewski](/Tomasz_Michniewski "Tomasz Michniewski")
- [PolyGlot](/PolyGlot "PolyGlot") probing code by Michel Van den Bergh[[1]](#cite_note-1)[[2]](#cite_note-2)

# Origins Opening Book

- Opening book by [Dann Corbit](/Dann_Corbit "Dann Corbit")

# Releases

- [Re: New engine releases & news H1 2025 - Zeta](https://talkchess.com/viewtopic.php?p=979457#p979457) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), May 21, 2025
- [Zeta Dva v0301](https://talkchess.com/viewtopic.php?p=679520#p679520) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), July 18, 2016
- [Zeta Dva ver 0.202](https://talkchess.com/viewtopic.php?p=427105) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), October 05, 2011
- [Zeta Dva v 0.1.5.3](https://talkchess.com/viewtopic.php?p=400229) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), March 21, 2011

# See also

- [Zeta](/Zeta "Zeta")

# Forum Posts

- [Zeta Dva](http://www.talkchess.com/forum/viewtopic.php?t=61745) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [CCC](/CCC "CCC"), October 17, 2016
- [Re: New J.A Compiles](https://talkchess.com/viewtopic.php?p=979460) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [CCC](/CCC "CCC"), May 21, 2025

# External Links

- [GitLab - smatovic/ZetaDva: Amateur level chess engine](https://gitlab.com/smatovic/ZetaDva)
- [Zeta Chess blog](https://zeta-chess.app26.de/)
- [Zeta Dva](https://computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Zeta%20Dva&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) on [CCRL](/CCRL "CCRL")

# References

1. [↑](#cite_ref-1) <http://hardy.uhasselt.be/Toga/book_format.html>
2. [↑](#cite_ref-2) <https://web.archive.org/web/20191216195456/http://hardy.uhasselt.be/Toga/book_format.html>

**[Up one level](/Engines "Engines")**