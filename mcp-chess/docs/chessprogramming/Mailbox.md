# Mailbox

Source: https://www.chessprogramming.org/Mailbox

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* Mailbox**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/SauerAspinwallMailbox.jpg/330px-SauerAspinwallMailbox.jpg)](/File:SauerAspinwallMailbox.jpg)

A fantastical mailbox [[1]](#cite_note-1)

**Mailbox**, (Offset board representation [[2]](#cite_note-2))
a square-centric board representation where the [encoding](/Pieces#PieceCoding "Pieces") of every [square](/Squares "Squares") resides in a separately addressable [memory](/Memory "Memory") element, usually an element of an [array](/Array "Array") for random access. The square number, or its [file](/Files "Files") and [rank](/Ranks "Ranks"), acts like an address to a post box, which might be empty or may contain one chess piece. As pointed out by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), not only the embedded [10x12 board](/10x12_Board "10x12 Board"), but various implementations are all mailbox, independently from elements in the array for padding that can act as a [sentinel value](https://en.wikipedia.org/wiki/Sentinel_value) [[3]](#cite_note-3).

# Implementations

- [8x8 Board](/8x8_Board "8x8 Board")
- [10x12 Board](/10x12_Board "10x12 Board")
- [Vector Attacks](/Vector_Attacks "Vector Attacks")

:   [0x88](/0x88 "0x88")

# Pros & cons

## Pros

- Easy, straightforward to understand and implement
- Suitable with the same efficiency for any size of boards, from one can be fitted on 64-bit integers to much larger. Thus it is also easier to support multi-chess variants which boards’ sizes are quite different.
- Suitable for almost all chess tasks and software where computing speed is not high requirements such as chess tools, [GUI](/GUI "GUI") since it is much easier to develop and maintain.

Newcomers are suggested to implement their first chess engines using Mailbox thus they can get some basic knowledge and skills before starting more complicated chess projects.

## Cons

In the view of developing chess engines:

- Programming must use many loop and branch commands such as for, while, if (compare with [Bitboards](/Bitboards "Bitboards"))
- Hard to store patterns and match them
- May have some inefficient high-frequency-use functions such as finding King locations, in-check
- Not efficient to generate moves in stages since generating all moves, captures only, non-captures may take quite similar periods

# Speed

For basic tasks such as generating, making/unmaking moves, a "pure" mailbox maybe slower than [Bitboards](/Bitboards "Bitboards"). However, when combining it with other methods such as [Piece-Lists](/Piece-Lists "Piece-Lists") and optimize the code it could be as fast as Bitboards[[4]](#cite_note-4)

# See also

- [Array](/Array "Array")
- [Array of Nibbles](/Nibble#ArrayOfNibbles "Nibble")
- [Mailbox in Minimax](/Minimax_(program)#Mailbox "Minimax (program)")

# Publications

- [Claude Shannon](/Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
- [Dietrich Prinz](/Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
- [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
- [Dan Spracklen](/Dan_Spracklen "Dan Spracklen"), [Kathe Spracklen](/Kathe_Spracklen "Kathe Spracklen") (**1978**). *First Steps in Computer Chess Programming*. [BYTE, Vol. 3, No. 10](/Byte_Magazine#BYTE310 "Byte Magazine"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-4.First_Steps.Byte_Magazine/First_Steps_in_Computer_Chess_Programing.Spracklen-Dan_Kathe.Byte_Magazine.Oct-1978.062303035.sm.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
- [David Levy](/David_Levy "David Levy") (**1979**). *Computer and Chess - How the monster thinks*. [Elektor](https://en.wikipedia.org/wiki/Elektor), January 1979 [[5]](#cite_note-5)
- [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") (**1981**). *[Checkmate: The Cray-1 Plays Chess. Part 1](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d2f73)*. [Cray Channels](http://www.0x07bell.net/WWWMASTER/CrayWWWStuff/Cfaqccframeset.html), Vol. 3, No. 1. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-2%20and%203-3.Cray_Channels_Vol-3_No-1.Checkmate_The_Cray-1_Plays_Chess.Hyatt.1980/Cray_Channels_Vol-3_No-1.Checkmate_The_Cray-1_Plays_Chess.Hyatt.1980.062303023.sm.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")

# Forum Posts

- [Bitboards vs Mailbox vs 0X88](https://www.stmintz.com/ccc/index.php?id=19808) by Bruce Cleaver, [CCC](/CCC "CCC"), June 02, 1998 » [0x88](/0x88 "0x88"), [Bitboards](/Bitboards "Bitboards")
- [0x88 vs mailbox](https://www.stmintz.com/ccc/index.php?id=387929) by [Stuart Cracraft](/Stuart_Cracraft "Stuart Cracraft"), [CCC](/CCC "CCC"), September 16, 2004 » [0x88](/0x88 "0x88")
- [Mailbox info](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2514) by Anonymous, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 08, 2005
- [Board representation : 0x88 or 10x12 ?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4442) by Philippe, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 02, 2006 » [0x88](/0x88 "0x88")
- [move generation with one dimensional "12 x 10" array](http://www.talkchess.com/forum/viewtopic.php?t=23191) by [Andrew Short](/index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](/CCC "CCC"), August 22, 2008
- [mailbox & CPW](http://www.talkchess.com/forum/viewtopic.php?t=48164) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), May 31, 2013
- [The mailbox trials](http://talkchess.com/forum3/viewtopic.php?f=7&t=76773) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), March 04, 2021 [[6]](#cite_note-6)

# External Links

- [Board representation (chess) - Array based from Wikipedia](https://en.wikipedia.org/wiki/Board_representation_%28chess%29#Array_based)
- [Chess board representations](http://www.craftychess.com/hyatt/boardrep.html) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt")
- [hgm-mailbox-trials/mailbox7b.c at main · maksimKorzh/hgm-mailbox-trials · GitHub](https://github.com/maksimKorzh/hgm-mailbox-trials/blob/main/mailbox7b.c) hosted by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh") [[7]](#cite_note-7)
- [Mailbox (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Mailbox)

# References

1. [↑](#cite_ref-1) A [fantastical](https://en.wikipedia.org/wiki/Fantastic_architecture) mailbox designed by [Frederick C. Sauer](https://en.wikipedia.org/wiki/Frederick_C._Sauer) around 1930 in the [Sauer Buildings Historic District](https://en.wikipedia.org/wiki/Sauer_Buildings_Historic_District) in [Aspinwall, Pennsylvania](https://en.wikipedia.org/wiki/Aspinwall,_Pennsylvania). Image by [Lee Paxton](https://en.wikipedia.org/wiki/User:Leepaxton) on May 16, 2010
2. [↑](#cite_ref-2) [Chess board representations](http://www.craftychess.com/hyatt/boardrep.html) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt")
3. [↑](#cite_ref-3) [mailbox & CPW](http://www.talkchess.com/forum/viewtopic.php?t=48164) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), May 31, 2013
4. [↑](#cite_ref-4) [The mailbox trials](http://talkchess.com/forum3/viewtopic.php?f=7&t=76773#p885878) by [Nguyen Pham](/Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](/CCC "CCC"), Mar 04, 2021
5. [↑](#cite_ref-5) [Publication Archive](http://www.chesscomputeruk.com/html/publication_archive.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
6. [↑](#cite_ref-6) [hgm-mailbox-trials/mailbox7b.c at main · maksimKorzh/hgm-mailbox-trials · GitHub](https://github.com/maksimKorzh/hgm-mailbox-trials/blob/main/mailbox7b.c) hosted by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh")
7. [↑](#cite_ref-7) [The mailbox trials](http://talkchess.com/forum3/viewtopic.php?f=7&t=76773) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), March 04, 2021

**[Up one Level](/Board_Representation "Board Representation")**