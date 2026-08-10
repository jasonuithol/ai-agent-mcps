# CHEKMO-II

Source: https://www.chessprogramming.org/CHEKMO-II

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* CHEKMO-II**

[![](/images/8/80/Checkmo-II.jpg)](https://www.youtube.com/watch?time_continue=7&v=Rp4HIC1crS0)

CHEKMO-II' [[1]](#cite_note-1)

**CHEKMO-II**, (CheckMo-II)
the *classical* chess program for the [PDP-8](/PDP-8 "PDP-8"), written in the 70s by [Digital Equipment Corporation](/Digital_Equipment_Corporation "Digital Equipment Corporation") instructor [John E. Comeau](/John_E._Comeau "John E. Comeau") in PAL-8, the PDP-8 [assembly](/Assembly "Assembly") [[2]](#cite_note-2).

# Abstract

[[3]](#cite_note-3) [[4]](#cite_note-4):

```
CHEKMO-II is a chess playing program which will run on any PDP-8 family computer. The program will play either the white pieces or the black pieces, and will play and accept all classes of legal moves, including castling both short and long, en passant pawn captures, and pawn promoting moves to any legal promotion piece. The program prints out its moves in Algebraic Notation, and accepts moves using Algebraic Notation. Included in the command structure of the program are commands which allow you to input board positions using Forsyth Notation, and get a printout of the board at your terminal.
```

# Known Deficiencies

[[5]](#cite_note-5)

```
CHEKMO-II has been programmed to use the same strategy throughout the game. This strategy has been optimized for good play in the Middlegame, and Opening. As a result CHEKMO-II plays poor moves in some Endgame positions.
```

```
If either the white side or the black side becomes significantly more powerful than the other (about 4 queens) CHEKMO-II may play some strange, but legal moves. This is caused by overflow in an internal evaluator routine.
```

# See also

- [QCHESS](/QCHESS "QCHESS")

# Forum Posts

- [More PDP-8 Software Donated to the RICM](http://groups.google.com/group/alt.sys.pdp8/msg/9b7216d805221f92) by Klemens Krause, [alt.sys.pdp8](http://groups.google.com/group/alt.sys.pdp8/topics), July 5, 2011

# External Links

- [PDP-8 Chess (CHEKMO-II) Instructions](http://www.pdp8.net/games/chess.shtml) [[6]](#cite_note-6)
- [File CHEKMO.PA (PAL assembler source file)](http://www.pdp8.net/pdp8cgi/os8_html/CHEKMO.PA?act=file;fn=images/misc_dectapes/chekmo_misc.tu56;blk=121,252,0;to=auto)
- [GitHub - okalachev/chekmo: 1970’s chess engine CHEKMO-II + UCI adapter](https://github.com/okalachev/chekmo)
- [Norbert's Emulators | The Atari PDP-8 Emulator | b) Chess program CHEKMO-II](http://members.aon.at/nkehrer/pdp8.html)
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](/Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) [[7]](#cite_note-7)
- [PDP-8](/PDP-8 "PDP-8") - Presentation No. 3, [The National Museum of Computing](https://en.wikipedia.org/wiki/The_National_Museum_of_Computing), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Image clipped from the [video](https://www.youtube.com/watch?time_continue=7&v=Rp4HIC1crS0) from [Norbert's Emulators | The Atari PDP-8 Emulator | b) Chess program CHEKMO-II](http://members.aon.at/nkehrer/pdp8.html)
2. [↑](#cite_ref-2) [File CHEKMO.PA (PAL assembler source file)](http://www.pdp8.net/pdp8cgi/os8_html/CHEKMO.PA?act=file;fn=images/misc_dectapes/chekmo_misc.tu56;blk=121,252,0;to=auto)
3. [↑](#cite_ref-3) [DECUS Program Library PDP-8 Catalog 1978](http://www.bitsavers.org/pdf/dec/decus/programCatalogs/DECUS_Catalog_PDP-8_Aug78.pdf) (pdf)
4. [↑](#cite_ref-4) [PDP-8 Chess (CHEKMO-II) Instructions](http://www.pdp8.net/games/chess.shtml)
5. [↑](#cite_ref-5) [PDP-8 Chess (CHEKMO-II) Instructions](http://www.pdp8.net/games/chess.shtml)
6. [↑](#cite_ref-6) [CHEKMO-II German manual](http://www.technikum29.de/de/lernprojekte/schach/Chekmo%20II%20%28deutsch,%20ungekuerzt%29.pdf) (pdf)
7. [↑](#cite_ref-7) [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), July 11, 2015

**[Up one level](/Engines "Engines")**