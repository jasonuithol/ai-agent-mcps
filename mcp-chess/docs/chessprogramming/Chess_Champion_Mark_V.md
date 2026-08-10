# Chess Champion Mark V

Source: https://www.chessprogramming.org/Chess_Champion_Mark_V

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Chess Champion Mark V**

[![](/images/5/5a/CCMarkV.jpg)](https://www.flickr.com/photos/10261668@N05/858179951/in/album-72157600922172552/)

Chess Champion Mark V [[1]](#cite_note-1)

**Chess Champion Mark V**,   
a [dedicated chess computer](/Dedicated_Chess_Computers "Dedicated Chess Computers") manufactured by [Scisys-W Ltd.](/Saitek "Saitek") [Hong Kong](https://en.wikipedia.org/wiki/Hong_Kong) from 1981. Primary author of a [Z80](/Z80 "Z80") based development version was [David Broughton](/David_Broughton "David Broughton"), while the translation to the [6502](/6502 "6502") production version was done by [Mark Taylor](/Mark_Taylor "Mark Taylor") [[2]](#cite_note-2). Both programmers were recruited into [Levy's](/David_Levy "David Levy") and [O’Connell's](/Kevin_O%E2%80%99Connell "Kevin O’Connell") company [Philidor Software](/Philidor_Software "Philidor Software") which was closely related to [Winkler's](/Eric_Winkler "Eric Winkler") [Scisys-W Ltd.](/Saitek "Saitek") who manufactured and traded most of their computers until in summer 1981 Levy and O’Connell decided to loosen their relationship with SciSys and founded their new software company [Intelligent Software](/Intelligent_Software "Intelligent Software") [[3]](#cite_note-3) [[4]](#cite_note-4).

# Features

The Mark V had an [LCD](https://en.wikipedia.org/wiki/Liquid_crystal_display)-board, a striking, futuristic design and many new features. For instance, it could play simultaneously on up to 12 internal boards.

# SX Algorithm

The Chess Champion Mark V was mentioned to use the first version of the [SEX Algorithm](/SEX_Algorithm "SEX Algorithm") then called SX Algorithm , which used fractional plies for [extensions](/Extensions "Extensions") and [reductions](/Reductions "Reductions") [[5]](#cite_note-5) [[6]](#cite_note-6) :

```
Our first attempts to formalize this idea were in 1981 when one of us (David Broughton) replaced the usual integer depth (which simply controlled the maximum ply depth) with an integer SX. The SX parameter started out at the root node with some positive value, in a similar way to maximum depth, but instead of being decremented by one at each ply it would be decremented by a number determined by the type (or category) of move just made in the tree. When SX was decremented below zero this signaled the end of the search, except for the usual terminal node evaluations.
```

While they started the first iteration of an [ID framework](/Iterative_Deepening "Iterative Deepening") with a SX-value of 10, which was incremented by 7 or 8 in further iterations, the depth decrement SXDEC was determined by static move properties, varying from 3 for the first [check](/Check "Check"), to 7 for further [tactical moves](/Tactical_Moves "Tactical Moves") such as [captures](/Captures "Captures") and attacking moves, up to 21, 24 or even 34 for non-tactical and apparently loosing moves. Those latter high decrements and reductions gave the Mark V the characteristic of a [Shannon Type B](/Type_B_Strategy "Type B Strategy") program, which caused some tactical oversights with [quiet moves](/Quiet_Moves "Quiet Moves") involved, but made the program a strong mate solver for that time.

# Initial Success

In September 1981, the Chess Champion Mark V won the commercial group of the [2nd World Microcomputer Chess Championship](/WMCCC_1981 "WMCCC 1981") in [Travemünde](https://en.wikipedia.org/wiki/Travem%C3%BCnde), [West Germany](https://en.wikipedia.org/wiki/West_Germany). The initial success could not be sustained with a strong upgrade. The [Chess Champion Mark VI](/index.php?title=Chess_Champion_Mark_VI&action=edit&redlink=1 "Chess Champion Mark VI (page does not exist)") [[7]](#cite_note-7) [[8]](#cite_note-8) module that followed a year or two later was only marginally stronger than the Mark V. A [piece recognition](/Piece_Recognition "Piece Recognition") [sensory board](/Sensory_Board "Sensory Board") was planned and patented but after much delay SciSys released a flawed auto sensory board instead. The Mark VI and sensory board were a commercial flop [[9]](#cite_note-9) .

# See also

- [Chess Champion Mark IV](/Chess_Champion_Mark_IV "Chess Champion Mark IV")
- [Chess Champion Mark VI](/index.php?title=Chess_Champion_Mark_VI&action=edit&redlink=1 "Chess Champion Mark VI (page does not exist)")
- [Milton Bradley Phantom](/Milton_Bradley_Phantom "Milton Bradley Phantom")
- [SEX Algorithm](/SEX_Algorithm "SEX Algorithm")

# Publications

- Editor (**1982**). *[March 1982-News - Experts confounded as machine out-thinks Grandmaster Nunn](http://yourcomputeronline.wordpress.com/2011/01/30/march-1982-news/)*. [Your Computer](/Your_Computer "Your Computer"), [March 1982](http://yourcomputeronline.wordpress.com/2011/01/30/march-1982-contents-and-editorial/)
- [John F. White](/John_F._White "John F. White") (**1982**). *[Review-Chess Computers](http://yourcomputeronline.wordpress.com/2011/01/31/review-chess-computers/)*. [Your Computer](/Your_Computer "Your Computer"), [March 1982](http://yourcomputeronline.wordpress.com/2011/01/30/march-1982-contents-and-editorial/)
- [Max Bramer](/Max_Bramer "Max Bramer") (**1982**). *Chess - Chess Champion Mark V’s ability at solving chess problems*. [Computer & Video Games](https://en.wikipedia.org/wiki/Computer_and_Video_Games), [April 1982](http://www.chesscomputeruk.com/html/publication_archive_1982.html), [pdf](http://www.chesscomputeruk.com/Computer___Video_Games_April_1982.pdf) hosted by [Mike Watters](/Mike_Watters "Mike Watters")
- [David Levy](/David_Levy "David Levy"), [David Broughton](/David_Broughton "David Broughton"), [Mark Taylor](/Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](/ICGA_Journal#12_1 "ICGA Journal") » [SEX Algorithm](/SEX_Algorithm "SEX Algorithm")

# Forum Posts

- [Exist a posibility to play against MK V (1981 computerworldchampion) on PC?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74040) by [Thomas Lagershausen](/index.php?title=Thomas_Lagershausen&action=edit&redlink=1 "Thomas Lagershausen (page does not exist)"), [CCC](/CCC "CCC"), May 29, 2020
- [David Broughtons computer chess Engine Philidor / MKV / MK VI](https://prodeo.actieforum.com/t256-david-broughtons-computer-chess-engine-philidor-mkv-mk-vi) by [Mclane](/Thorsten_Czub "Thorsten Czub"), [ProDeo Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 12, 2021

# External Links

- [Chess Champion Mark V (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/program.php?id=499)
- [Chess Champion Mark V](http://www.chesscomputeruk.com/html/chess_champion_mark_v.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [Scisys and Novag : The Early Years](http://www.chesscomputeruk.com/html/scisys_and_novag___the_early_y.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [SciSys Chess Champion Mark V](http://www.schach-computer.info/wiki/index.php/SciSys_Chess_Champion_Mark_V) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German, parts in English)

# References

1. [↑](#cite_ref-1) [Chess Champion Mark V](https://www.flickr.com/photos/10261668@N05/858179951/in/album-72157600922172552/) from [5.Scisys/Saitek | Flickr - Photo Sharing!](https://www.flickr.com/photos/10261668@N05/albums/72157600922172552/with/858179951/) by [Chewbanta](/Steve_Blincoe "Steve Blincoe")
2. [↑](#cite_ref-2) [David Levy interview](http://www.schach-computer.info/wiki/index.php/Levy,_David) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
3. [↑](#cite_ref-3) [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
4. [↑](#cite_ref-4) [Tony Harrington](/Tony_Harrington "Tony Harrington") (**1983**). *Intelligent Software*. [Personal Computer World](/Personal_Computer_World "Personal Computer World"), [April 1983](http://www.chesscomputeruk.com/html/publication_archive_1983.html), [pdf](http://www.chesscomputeruk.com/PCW_April_1983.pdf) hosted by [Mike Watters](/Mike_Watters "Mike Watters")
5. [↑](#cite_ref-5) [David Levy](/David_Levy "David Levy"), [David Broughton](/David_Broughton "David Broughton"), [Mark Taylor](/Mark_Taylor "Mark Taylor") (**1989**). *The [SEX Algorithm](/SEX_Algorithm "SEX Algorithm") in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](/ICGA_Journal#12_1 "ICGA Journal")
6. [↑](#cite_ref-6) [ICCA1989 12 1 part.jpg](http://www.schach-computer.info/wiki/images/5/56/ICCA1989_12_1_part.jpg) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
7. [↑](#cite_ref-7) [Chess Champion Mark VI + Sensor Board](http://www.chesscomputeruk.com/html/chess_champion_mark_vi___senso.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
8. [↑](#cite_ref-8) [SciSys Chess Champion Mark VI](http://www.schach-computer.info/wiki/index.php/Scisys_Chess_Champion_Mark_VI) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
9. [↑](#cite_ref-9) [Chess Computers - The UK Story](http://www.chesscomputeruk.com/html/chess_computers_-_the_uk_story.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")

**[Up one level](/Engines "Engines")**