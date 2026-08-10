# Gromit

Source: https://www.chessprogramming.org/Gromit

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* GromitChess**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Wallace%2C_Gromit%2C_and_creator_Nick_Park.jpg/330px-Wallace%2C_Gromit%2C_and_creator_Nick_Park.jpg)](/File:Wallace,_Gromit,_and_creator_Nick_Park.jpg)

[Gromit, Wallace](https://en.wikipedia.org/wiki/Wallace_and_Gromit), and creator [Nick Park](https://en.wikipedia.org/wiki/Nick_Park) [[1]](#cite_note-1)

**GromitChess**, (Gromit, Gromit Chess)  
a chess engine by [Frank Schneider](/Frank_Schneider "Frank Schneider") and [Kai Skibbe](/Kai_Skibbe "Kai Skibbe"). **Gromit**, later renamed to **GromitChess**, was initially written by Frank. In 1999 former tester Kai Skibbe joined the development [[2]](#cite_note-2).
Gromit and GromitChess played several [IPCCCs](/IPCCC "IPCCC"), the [WMCCC 1995](/WMCCC_1995 "WMCCC 1995"), [WCCC 1999](/WCCC_1999 "WCCC 1999") in Paderborn and the [WMCCC 2001](/WMCCC_2001 "WMCCC 2001") in Maastricht, where it won the title of the Amateur World Microcomputer Chess Champion. Early versions (1.2) were standalone engines with an own [GUI](/GUI "GUI"), later versions (> 2.0) were [WinBoard](/WinBoard "WinBoard")/[XBoard](/XBoard "XBoard") compatible, a dedicated version (3.1) was sold along with other [Young Talents](/ChessBase#YoungTalents "ChessBase") by [ChessBase](/ChessBase "ChessBase"), running under their [Database](/ChessBase_(Database) "ChessBase (Database)") or [Fritz GUI](/Fritz#FritzGUI "Fritz") [[3]](#cite_note-3). GromitChess (3.10.3) emphasized its ambitions going commercial while incorporated into the [PocketGrandmaster](/PocketGrandmaster "PocketGrandmaster") for [Pocket PC](/index.php?title=Pocket_PC&action=edit&redlink=1 "Pocket PC (page does not exist)") [[4]](#cite_note-4) [[5]](#cite_note-5), and became predecessor of [Anaconda](/Anaconda "Anaconda").

# Description

given in 1999 from the [ICGA](/ICGA "ICGA") tournament site [[6]](#cite_note-6):

```
GromitChess is a C++-program, developed in a Linux-environment (Emacs, gcc). It searches about 25000 to 50000 nodes per second on a K6/200 and tries to be intelligent rather than fast. Attacktables are the primary datastructure (16 bit for every square and player; bit n is set if piece n attacks the square). The search uses iterative deepening, PVS, transposition tables, killer- and history heuristic, nullmove (R=2), about 10 chess-specific extensions and some pruning heuristics. The quiescence uses a static exchange evaluator and includes some checks and other threatening moves. Parts of the evaluation are initialized at the root but most of the work is done at the leafnodes. You can find more information and executables in the WWW.
```

# Copy Make

[Frank Schneider](/Frank_Schneider "Frank Schneider") on Gromit's [Copy-Make](/Copy-Make "Copy-Make") approach [[7]](#cite_note-7):

```
I think it depends on your program and the board representation. Gromit uses copy+update and >1KB is copied every move (which is maybe too much). When I decided to do it that way (on an Amiga) I only considered clock cycles, but on a PC the low memory-bandwidth is the real problem. Since Gromit's evaluation and search heuristics use most of the processor time I never tried update+take back, because I guess it would give me less than 10% speedup, probably being slower than copy+update.
```

```
There are some advantages of copy+update:
- it is easy to program
- it is easier to do some 'clever' things that would be difficult to take back
- you can compare the current position with previous positions in the search tree
An alternative would use a mix of copied and static data structures.
```

# See also

- [Anaconda](/Anaconda "Anaconda")
- [PocketGrandmaster](/PocketGrandmaster "PocketGrandmaster")

# Forum Posts

## 1997 ...

- [Where I can get Gromit Chess?](https://groups.google.com/d/msg/rec.games.chess.computer/Nezkk2HVay4/9GbqRMrmJNMJ) by [Torsten Schoop](/index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), February 07, 1997
- [GromitChess homepage](https://www.stmintz.com/ccc/index.php?id=15175) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), February 22, 1998
- [New: xboard-Version of GromitChess](https://www.stmintz.com/ccc/index.php?id=28809) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), October 05, 1998
- [GromitChess [Home Page] update](https://www.stmintz.com/ccc/index.php?id=34750) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), December 04, 1998
- [GromitChess for download](https://www.stmintz.com/ccc/index.php?id=34938) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), December 06, 1998
- [New version of GromitChess](https://www.stmintz.com/ccc/index.php?id=38187) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), January 03, 1999
- [Re: Unmake move v copy the board](https://www.stmintz.com/ccc/index.php?id=40716) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), January 24, 1999
- [New version of GromitChess](https://www.stmintz.com/ccc/index.php?id=46528) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), March 22, 1999
- [GromitChess 2.13](https://www.stmintz.com/ccc/index.php?id=46772) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), March 24, 1999
- [New: Gromit 2.20](https://www.stmintz.com/ccc/index.php?id=56978) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), June 20, 1999 » [WCCC 1999](/WCCC_1999 "WCCC 1999")

## 2000 ...

- [Gromitchess bookcheating (for Vincent DIEPEVEEN)](https://www.stmintz.com/ccc/index.php?id=185200) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), August 23, 2001
- [Goliath Light, Gromit, Patzer, SOS, etc. commercially sold](https://www.stmintz.com/ccc/index.php?id=186009) by [Theo van der Storm](/Theo_van_der_Storm "Theo van der Storm"), [CCC](/CCC "CCC"), August 28, 2001
- [The Crazy Bishop 0046 and Gromit 3.8.2](https://www.stmintz.com/ccc/index.php?id=186640) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](/CCC "CCC"), August 31, 2001 » [The Crazy Bishop](/The_Crazy_Bishop "The Crazy Bishop")
- [PocketGrandmaster 1.1 released](https://www.stmintz.com/ccc/index.php?id=202624) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), December 19, 2001
- [Anyone using the Gromit engine?](https://www.stmintz.com/ccc/index.php?id=207016) by Jonathan Parle, [CCC](/CCC "CCC"), January 12, 2002
- [Re: Gromit 3.8.2 (wb) released!](https://www.stmintz.com/ccc/index.php?id=207297) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), January 14, 2002
- [Re: Is Gromit 3.9.5 is out?](https://www.stmintz.com/ccc/index.php?id=240495) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), July 14, 2002
- [Anaconda 1.0 (ex-GromitChess) available as CB-native](https://www.stmintz.com/ccc/index.php?id=288436) by [Kai Skibbe](/Kai_Skibbe "Kai Skibbe"), [CCC](/CCC "CCC"), March 08, 2003
- [Gromit 1.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=18889) by Philippe, [CCC](/CCC "CCC"), January 12, 2008

## 2010 ...

- [ChessBase native engines (freeware)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=51588) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](/CCC "CCC"), March 13, 2014
- [Gromit 2.20 Correct Configuration](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72596) by [Brendan J. Norman](/index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](/CCC "CCC"), December 17, 2019

# External Links

## Chess Engine

- [GromitChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=89)
- [Index of /chess/engines/Norbert's collection/GromitChess (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert's%20collection/GromitChess%20(Compilation)/) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")

:   [New features in GromitChess 1.2](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/GromitChess%20%28Compilation%29/v1.2%20%28standalone%20application%29/NEWS.TXT)

- [Young Talents, Teil 2](http://scleinzell.schachvereine.de/p_spielprogramme/youngtal_b.shtml) by [Peter Schreiner](/Peter_Schreiner "Peter Schreiner"), Mai 2000, hosted by [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml) (German)

## Misc

- [Wallace & Gromit - The Official Site](http://www.wallaceandgromit.com/)
- [Wallace & Gromit from Wikipedia](https://en.wikipedia.org/wiki/Wallace_and_Gromit)

# References

1. [↑](#cite_ref-1) Creator [Nick Park](https://en.wikipedia.org/wiki/Nick_Park) with his characters in 2005 promoting [Wallace & Gromit: The Curse of the Were-Rabbit](https://en.wikipedia.org/wiki/Wallace_%26_Gromit:_The_Curse_of_the_Were-Rabbit), [Photo](https://commons.wikimedia.org/wiki/File:Wallace,_Gromit,_and_creator_Nick_Park.jpg) by [Sam Felder](https://www.flickr.com/photos/43671133974@N01), September 19, 2005, originally posted on [Flickr](https://en.wikipedia.org/wiki/Flickr), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/deed.en)
2. [↑](#cite_ref-2) [PocketGrandmaster About](http://www.pocketgrandmaster.com/english/about.html)
3. [↑](#cite_ref-3) [Re: Anyone using the Gromit engine?](https://www.stmintz.com/ccc/index.php?id=207034) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), January 13, 2002
4. [↑](#cite_ref-4) [PocketGrandmaster 1.1 released](https://www.stmintz.com/ccc/index.php?id=202624) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), December 19, 2001
5. [↑](#cite_ref-5) [Re: Is Gromit 3.9.5 is out?](https://www.stmintz.com/ccc/index.php?id=240495) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), July 14, 2002
6. [↑](#cite_ref-6) [GromitChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=89)
7. [↑](#cite_ref-7) [Re: Unmake move v copy the board](https://www.stmintz.com/ccc/index.php?id=40716) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), January 24, 1999

**[Up one level](/Engines "Engines")**