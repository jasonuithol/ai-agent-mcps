# Y!

Source: https://www.chessprogramming.org/Y!

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Y!**

[![](/images/thumb/d/d4/TurboKit20.jpg/300px-TurboKit20.jpg)](/File:TurboKit20.jpg)

[TurboKit TK20](/6502#TK20 "6502") [[1]](#cite_note-1)

**Y!** (Why Not),   
a chess program written by primary author [Ulf Rathsman](/Ulf_Rathsman "Ulf Rathsman"), supported by [Lars Hjörth](/Lars_Hj%C3%B6rth "Lars Hjörth") and [book author](/Category:Opening_Book_Author "Category:Opening Book Author") [Sandro Necchi](/Sandro_Necchi "Sandro Necchi"). It was written in [6502](/6502 "6502") [assembly](/Assembly "Assembly") and played tournaments on the [TurboKit TK20](/6502#TK20 "6502") by *Schaetzle+Bsteh* [[2]](#cite_note-2). Y! competed the [WMCCC 1988](/WMCCC_1988 "WMCCC 1988") as Y!88 and the [WMCCC 1989](/WMCCC_1989 "WMCCC 1989") and [WCCC 1989](/WCCC_1989 "WCCC 1989") as Y!89 (Why Not 89).

# Photos

[![WMCCC88YNot.jpg](/images/d/dd/WMCCC88YNot.jpg)](/File:WMCCC88YNot.jpg)

[Ulf Rathsman](/Ulf_Rathsman "Ulf Rathsman") and [Sandro Necchi](/Sandro_Necchi "Sandro Necchi") of Y!88 at the [WMCCC 1988](/WMCCC_1988 "WMCCC 1988") in [Almería](https://en.wikipedia.org/wiki/Almer%C3%ADa) [[3]](#cite_note-3)

# Description

based on the [WCCC 1989](/WCCC_1989 "WCCC 1989") booklet [[4]](#cite_note-4):

```
Y!89 uses a full, partly extended, width iterative principal variation search with capture and promotion searches in terminal nodes. The program is designed to be used in a cheap commercial environment, thus the work memory is still just 4 kbytes of RAM, and the good old 6502 eight bit processor is used in tournaments emulated by the also commercially available Turbo kit. The search is fast for a micro, and includes detection of repeated positions (actual as well as potential), and performs extensions for check evasions, passed pawn moves and some king moves in pawn endgames.
```

```
Most of the material and positional evaluation is made incrementally by the means of material value tables and positional score boards for each piece type, created once for each position of the game with the computer to move. Some "absolute" evaluation is also done, e.g. for static evaluation of unstoppable passed pawns and pawn structure.
```

# See also

- [Conchess](/Conchess "Conchess")
- [Princhess](/Princhess "Princhess")

# External Links

- [Y!'s ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=356)
- [Why Not 89's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=455)
- [Conchess](http://www.schach-computer.info/wiki/index.php/Conchess) – [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German) [[5]](#cite_note-5)

# References

1. [↑](#cite_ref-1) Image from [ICT 2006](/ICT_2006 "ICT 2006") and 13th Chess Computer Users (Gebruikers) tournament old [CSVN](/CSVN "CSVN") site [Photo Gallery 24](http://old.csvn.nl/gallery24.html), Photos by [Eric van Reem](/Eric_van_Reem "Eric van Reem") and [Kees Sio](/index.php?title=Kees_Sio&action=edit&redlink=1 "Kees Sio (page does not exist)")
2. [↑](#cite_ref-2) [TurboKit – Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/TurboKit)
3. [↑](#cite_ref-3) Image by [László Lindner](/L%C3%A1szl%C3%B3_Lindner "László Lindner") from [László Lindner](/L%C3%A1szl%C3%B3_Lindner "László Lindner") (**1989**).*Die wiederauferstandene Mikro-Weltmeisterschaft - 8.Mikroschachcomputer - WM 1988 in Almeria*. [Europa-Rochade](https://de.wikipedia.org/wiki/Rochade_Europa), 01/02-1989, [pdf](http://schaakcomputers.nl/hein_veldhuis/database/files/11-1988,%20Europa-Rochade,%20Die%208.%20Mikroschachcomputer-WM%201988%20in%20Almeria.pdf) hosted by [Hein Veldhuis](/Hein_Veldhuis "Hein Veldhuis") (German)
4. [↑](#cite_ref-4) [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](/Peter_Jennings "Peter Jennings"), from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)
5. [↑](#cite_ref-5) [Karsten Bauermeister](/Karsten_Bauermeister "Karsten Bauermeister") (**1998**). *Die Geschichte der Conchess-Schachcomputer*. [Computerschach und Spiele](/Computerschach_und_Spiele "Computerschach und Spiele"), Heft 4, August-September 1998

**[Up one level](/Engines "Engines")**