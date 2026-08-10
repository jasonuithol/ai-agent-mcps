# Loop (Program)

Source: https://www.chessprogramming.org/Loop_(Program)

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Loop**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Tigerandturtle.jpg/330px-Tigerandturtle.jpg)](/File:Tigerandturtle.jpg)

[Tiger and Turtle](https://en.wikipedia.org/wiki/Tiger_and_Turtle_%E2%80%93_Magic_Mountain) - illuminated looping [[1]](#cite_note-1)

**Loop**,  
an [UCI](/UCI "UCI") compliant chess engine by [Fritz Reul](/Fritz_Reul "Fritz Reul") with different [board representations](/Board_Representation "Board Representation") for 32-bit and 64-bit platforms, at times commercial. Loop became subject of its author's Ph.D. thesis *New Architectures in Computer Chess* [[2]](#cite_note-2) . Despite different board representation, both Loop versions presumably share same [search](/Search "Search") and [evaluation](/Evaluation "Evaluation") with similar features and weights.

# 32-bit Loop

The 32-bit program, based on Reul's former program [List](/List_(Program) "List (Program)"), relies on a [15x12 board](/Vector_Attacks#15x12 "Vector Attacks") representation in conjunction with disjoint [piece-lists](/Piece-Lists#NewArchitecture "Piece-Lists") with adequate [move generation](/Move_Generation "Move Generation") of [blocker loops](/Vector_Attacks#NewArchitecture "Vector Attacks"). It participated as *Loop Leiden* at the [DOCCC 2006](/DOCCC_2006 "DOCCC 2006"), becoming strong runner up behind [Rybka](/Rybka "Rybka"). A specially adapted version called *Loop Express* became the engine of [Wii Chess](/Wii_Chess "Wii Chess") for the [Nintendo](https://en.wikipedia.org/wiki/Nintendo) [Wii](https://en.wikipedia.org/wiki/Wii) [console](https://en.wikipedia.org/wiki/Video_game_console) in 2008 [[3]](#cite_note-3) . The non-bitboard data-structure of Loop was also applied in [Chrilly Donninger's](/Chrilly_Donninger "Chrilly Donninger") chess machine [Hydra](/Hydra "Hydra") [[4]](#cite_note-4) .

Reul in his thesis [[5]](#cite_note-5) :

```
This computerchess architecture was first implemented in the quite successful computerchess engine Loop Leiden 2006. The computerchess architecture was later implemented partially in Hydra and completely in Wii Chess by Nintendo (see Section 2.1). The high performance was just as important for these projects as the simplicity and ease of implementation in the following two environments: (1) the environment of a sophisticated computer-chess machine (Hydra) and (2) the environment of a commercial games console with the highest quality and security standards.
```

# 64-bit Loop

The [bitboard](/Bitboards "Bitboards") based Loop applies [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") for [sliding piece attack generation](/Sliding_Piece_Attacks "Sliding Piece Attacks"). Further, iterative [alpha-beta](/Alpha-Beta "Alpha-Beta") bounded [static exchange evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation") was applied to *Loop Amsterdam* [[6]](#cite_note-6) , also performing a [parallel search](/Parallel_Search "Parallel Search") for a quad-core processor, which played a strong [WCCC 2007](/WCCC_2007 "WCCC 2007") in [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam), and became Third, behind the later disqualified [Rybka](/Rybka "Rybka"), and [Zappa](/Zappa "Zappa") [[7]](#cite_note-7).

Fritz Reul on an essential reason of Loop's success in Amsterdam in his thesis [[8]](#cite_note-8) :

```
A complete computer-chess architecture based on hash functions and magic multiplications for the examination of bitboards is implemented in the computerchess engine Loop Amsterdam. This engine was able to reach the 3rd place at the 15th World Computer-Chess Championship, Amsterdam (NL) 2007. An essential reason for the success of this 64-bit computer-chess engine was the use of highly sophisticated perfect hash functions and magic multipliers for the computation of compound bit-patterns (bitboards) via perfect hashing.
```

# Evaluation

## Preliminary Considerations

Evaluation was only marginally covered in Reul's thesis. In *Preliminary Considerations* he mentioned discussions with [Chrilly Donninger](/Chrilly_Donninger "Chrilly Donninger"), [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey") and [Tord Romstad](/Tord_Romstad "Tord Romstad"), and the exchange of source codes [[9]](#cite_note-9) :

```
This thesis also does not aim at the explicit consideration of known computer-chess architectures, such as Rotated Bitboards [10] [11] or the 0x88 representation [12]. Many a reference used in this thesis is not available in a scientifically elaborate form. This includes personal conversations with programmers [13] [14] [15], and the exchange of source codes as well as discussions via email. In this way the contents of this thesis can be regarded to be on a state-of the-art level of the research and development in the field of the computer-chess architectures.
```

## Fruit Evaluation Overlap

During the [ICGA Investigations](/ICGA_Investigations "ICGA Investigations") concerning the [Rybka Controversy](/Rybka_Controversy "Rybka Controversy") and [evaluation overlaps](/Evaluation_Overlap "Evaluation Overlap"), 64-bit Loop was inspected by [Mark Watkins](/Mark_Watkins "Mark Watkins") who found congruence with the evaluation of [Fruit 2.1](/Fruit "Fruit") [[16]](#cite_note-16) . As confirmed by [David Levy](/David_Levy "David Levy") [[17]](#cite_note-17), the [ICGA](/ICGA "ICGA") has received a complaint on Loop by Fruit author [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey") and an investigation has been started about this case, as already mentioned by Watkins in August 2011 [[18]](#cite_note-18) .

# Complaints

[ICGA](/ICGA "ICGA") President [David Levy](/David_Levy "David Levy"), May 09, 2014 [[19]](#cite_note-19)

```
The ICGA has received formal complaints against the Chess programs LOOP and THINKER, both of which have participated in the World Computer Chess Championship. LOOP was entered by Fritz Reul into the 2007 WCCC in Amsterdam. THINKER was entered into the 2010 WCCC in Kanazawa.
...
Here we present extracts from the first section of each of Mark Watkins reports.
```

```
Loop  “The version examined here is Loop 2007 (64-bit), which was released at approximately the same time as the WCCC. There is notable similarity to Fruit in the evaluation function (other components were not examined).”
...
Based on the above mentioned reports by Mark Watkins the ICGA is convinced that, at the very least, both Fritz Reul and Kerwin Medina have a case to answer. Depending on how Reul and/or Medina respond to these allegations the ICGA might decide to conduct further investigations and/or take some form of strong sanctioning action against the programmers.  However, the ICGA does not intend to proceed further along the route to strong sanctions for the time being, in order to give these programmers more time in which to make contact with the ICGA President and present their defence to the allegations. If either or both of these programmers fail to do so by December 31st 2014, or refuses to do so, the ICGA will disqualify them from all their results in ICGA events.  In the meantime the ICGA has decided to suspend both Fritz Reul and Kerwin Medina from participation in all ICGA events until such time as they have made contact and offered a defence.
```

# See also

- [Coiled](/Coiled "Coiled")
- [Iteration](/Iteration "Iteration")
- [Iterative Search](/Iterative_Search "Iterative Search")
- [List](/List_(Program) "List (Program)")
- [Wii Chess](/Wii_Chess "Wii Chess")

# Publications

- [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. thesis, [pdf](https://pure.uvt.nl/ws/portalfiles/portal/1098572/Proefschrift_Fritz_Reul_170609.pdf)
- [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2010**). *Static Exchange Evaluation with αβ-Approach*. [ICGA Journal, Vol. 33, No. 1](/ICGA_Journal#33_1 "ICGA Journal")

# Forum Posts

## 2005 ...

- [Loop List available soon](https://www.stmintz.com/ccc/index.php?id=455003) by [Fritz Reul](/Fritz_Reul "Fritz Reul"), [CCC](/CCC "CCC"), October 11, 2005

:   [Re: Loop List commercially available soon](https://www.stmintz.com/ccc/index.php?id=455043) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [CCC](/CCC "CCC"), October 11, 2005

- [Loop 13.6 soon available](http://www.talkchess.com/forum/viewtopic.php?t=13270) by [Gerhard Sonnabend](/index.php?title=Gerhard_Sonnabend&action=edit&redlink=1 "Gerhard Sonnabend (page does not exist)"), [CCC](/CCC "CCC"), April 20, 2007
- [doing undoing](http://www.talkchess.com/forum/viewtopic.php?t=13764) by [Fritz Reul](/Fritz_Reul "Fritz Reul"), [CCC](/CCC "CCC"), May 14, 2007
- [Iterative DTS](http://www.talkchess.com/forum/viewtopic.php?t=14832) by [Fritz Reul](/Fritz_Reul "Fritz Reul"), [CCC](/CCC "CCC"), July 02, 2007
- [Re: Bob Hyatt says that...](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=213390&t=23375) by [Mike Scheidl](/index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](/CCC "CCC"), August 29, 2008
- [Re: Bob Hyatt says that...](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=213593&t=23375) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), August 30, 2008

## 2010 ...

- [Loop 2007 / Fruit 2.1](http://www.open-chess.org/viewtopic.php?f=5&t=1353) by [BB+](/Mark_Watkins "Mark Watkins"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 18, 2011 » [Fruit](/Fruit "Fruit")
- [Loop as a Fruit clone](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=27681) by [Rebel](/Ed_Schroder "Ed Schroder"), [Rybka Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 20, 2013
- [Complaints against the Chess programs LOOP and THINKER](http://hiarcs.net/forums/viewtopic.php?t=6707) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [Hiarcs Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 12, 2014
- [Complaints against the Chess programs LOOP and THINKER](http://www.talkchess.com/forum/viewtopic.php?t=52325) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [CCC](/CCC "CCC"), May 14, 2014

## 2015 ...

- [Re: FIDE Rules on ICGA - Rybka controversy](http://www.open-chess.org/viewtopic.php?f=3&t=2808&start=81) by [BB+](/Mark_Watkins "Mark Watkins"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 08, 2015

# External Links

## Chess Engine

- [Loop Computer Chess](https://www.loopchess.com/)
- [List's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=123) (covers Loop)
- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Loop](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Loop-List&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/40](/CCRL "CCRL")
- [Wii Chess from Wikipedia](https://en.wikipedia.org/wiki/Wii_Chess)
- [ICGA/Rybka controversy: Feedback - Allegations against another Chess Engine – The LOOP Program](https://en.chessbase.com/post/icga-rybka-controversy-feedback) by [David Levy](/David_Levy "David Levy"), [ChessBase News](/ChessBase "ChessBase"), February 17, 2012
- [Allegations against two more Chess Engines – The LOOP Program](https://icga.org/?p=354) by [David Levy](/David_Levy "David Levy"), [ICGA](/ICGA "ICGA") president, May 22, 2012 » [Thinker](/Thinker "Thinker")
- [Complaints against the Chess programs LOOP and THINKER](https://icga.org/?p=919) by [David Levy](/David_Levy "David Levy"), [ICGA](/ICGA "ICGA") President, May 9, 2014

## Misc

- [Loop disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/Loop)
- [The Loop disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/The_Loop)
- [Looping disambiguation page from Wikipedia](https://en.wikipedia.org/wiki/Looping)
- [Loop control flow from Wikipedia](https://en.wikipedia.org/wiki/Control_flow#Loops)

:   [For loop](https://en.wikipedia.org/wiki/For_loop)
:   [Foreach loop](https://en.wikipedia.org/wiki/Foreach_loop)
:   [While loop](https://en.wikipedia.org/wiki/While_loop)
:   [Do while loop](https://en.wikipedia.org/wiki/Do_while_loop)
:   [Infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)

- [Dirty Loops](https://en.wikipedia.org/wiki/Dirty_Loops) - Songs for Lovers - Coffee Break is over, Guitar cover with [Sandeep Mohan](/Category:Sandeep_Mohan "Category:Sandeep Mohan"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Tiger and Turtle – Magic Mountain](https://en.wikipedia.org/wiki/Tiger_and_Turtle_%E2%80%93_Magic_Mountain) is a monument in the [Angerpark](https://de.wikipedia.org/wiki/Angerpark) in [Duisburg](https://en.wikipedia.org/wiki/Duisburg), Germany. Here you see its illuminated looping at night, [Image](https://commons.wikimedia.org/wiki/File:Tigerandturtle.jpg) by Kleunam, November 18, 2011, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), [Category:Tiger and Turtle – Magic Mountain](https://commons.wikimedia.org/wiki/Category:Tiger_and_Turtle_%E2%80%93_Magic_Mountain), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [The Industrial Heritage Trail](/Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail")
2. [↑](#cite_ref-2) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. thesis
3. [↑](#cite_ref-3) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 2.2.2 Nintendo Wii Chess, pp. 11
4. [↑](#cite_ref-4) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 2.2.1 The Chess Machine Hydra, pp. 11
5. [↑](#cite_ref-5) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 5.1.1 Non-Bitboard Architectures, pp. 96
6. [↑](#cite_ref-6) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2010**). *Static Exchange Evaluation with αβ-Approach*. [ICGA Journal, Vol. 33, No. 1](/ICGA_Journal#33_1 "ICGA Journal")
7. [↑](#cite_ref-7) [15th World Computer Chess Championship - Amsterdam 2007 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/tournament.php?id=173)
8. [↑](#cite_ref-8) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 5.1.2 Magic Hash Functions for Bitboards, pp. 97
9. [↑](#cite_ref-9) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. thesis, 1.2 Preliminary Considerations, pp. 3-4
10. [↑](#cite_ref-10) [Stuart Cracraft](/Stuart_Cracraft "Stuart Cracraft") (**1984**). *Bitmap move generation in Chess*. [ICCA Journal, Vol. 7, No. 3](/ICGA_Journal#7_3 "ICGA Journal")
11. [↑](#cite_ref-11) [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.cis.uab.edu/hyatt/bitmaps.html)*. [ICCA Journal, Vol. 22, No. 4](/ICGA_Journal#22_4 "ICGA Journal")
12. [↑](#cite_ref-12) [0x88 Move Generation](http://web.archive.org/web/20070716111804/www.brucemo.com/compchess/programming/0x88.htm) by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland")
13. [↑](#cite_ref-13) [Chrilly Donninger](/Chrilly_Donninger "Chrilly Donninger") (**2006**). *Discussion with Dr. Christian Donninger*.
14. [↑](#cite_ref-14) [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey") (**2006**). *Personal discussion with Fabien Letouzey*.
15. [↑](#cite_ref-15) [Tord Romstad](/Tord_Romstad "Tord Romstad") (**2007**). *Discussion with Tord Romstad*.
16. [↑](#cite_ref-16) [Loop 2007 / Fruit 2.1](http://www.open-chess.org/viewtopic.php?f=5&t=1353) by [BB+](/Mark_Watkins "Mark Watkins"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 18, 2011
17. [↑](#cite_ref-17) [ICGA/Rybka controversy: Feedback - Allegations against another Chess Engine – The LOOP Program](https://en.chessbase.com/post/icga-rybka-controversy-feedback) by [David Levy](/David_Levy "David Levy"), [ChessBase News](/ChessBase "ChessBase"), February 17, 2012
18. [↑](#cite_ref-18) [Re: Loop 2007 / Fruit 2.1](http://www.open-chess.org/viewtopic.php?f=5&t=1353#p13794) by [BB+](/Mark_Watkins "Mark Watkins"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 22, 2011
19. [↑](#cite_ref-19) [Complaints against the Chess programs LOOP and THINKER](https://icga.org/?p=919) by [David Levy](/David_Levy "David Levy"), [ICGA](/ICGA "ICGA") President, May 9, 2014

**[Up one level](/Engines "Engines")**