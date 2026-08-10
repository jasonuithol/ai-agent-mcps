# HIARCS

Source: https://www.chessprogramming.org/HIARCS

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* HIARCS**

[![](/images/thumb/8/86/HCE-main3.jpg/400px-HCE-main3.jpg)](/File:HCE-main3.jpg)

Deep HIARCS 14 WCSC with [HIARCS Chess Explorer](/HIARCS_Chess_Explorer "HIARCS Chess Explorer") [[1]](#cite_note-1)

**HIARCS** (Hiarcs),  
an [UCI](/UCI "UCI") compliant chess engine written by [Mark Uniacke](/Mark_Uniacke "Mark Uniacke"). HIARCS is an acronym for Higher Intelligence Auto Response Chess System, and its history of development lasts over 30 years now. Because HIARCS is written portable in [C](/C "C"), it is available for multiple platforms such as [Pocket PC](https://en.wikipedia.org/wiki/Pocket_PC), [Palm](https://en.wikipedia.org/wiki/Palm_%28PDA%29), [Apple](/index.php?title=Apple&action=edit&redlink=1 "Apple (page does not exist)") [iPhone](/index.php?title=IPhone&action=edit&redlink=1 "IPhone (page does not exist)") & [iPod Touch](/index.php?title=IPod_Touch&action=edit&redlink=1 "IPod Touch (page does not exist)"), [PDAs](https://en.wikipedia.org/wiki/Personal_digital_assistant), [PC](/IBM_PC "IBM PC") and [Macintosh](/Macintosh "Macintosh") computers.

# History

## Basic

The very first version of HIARCS was already written 1980 in [PDP-11](/PDP-11 "PDP-11") [Basic](/Basic "Basic"), when Mark was a 15 year old schoolboy [[2]](#cite_note-2) . Subsequent versions (5 aka 0.5) were still written in interpreted Basic as well, and to compensate that speed disadvantage, HIARCS used to be smart rather than fast. [Mark Uniacke](/Mark_Uniacke "Mark Uniacke") from *Now Walking, 1982-1983: HIARCS 5* [[3]](#cite_note-3) :

```
The inspiration for the new HIARCS search was sought from the book Chess Skill in Man and Machine and in particular the article "The heuristic search: An alternative to the alpha-beta minimax procedure" by Larry Harris from Dartmouth College [4] . HIARCS was still written in the relatively primitive BASIC programming language and being interpreted it meant the program was rather slow. To compensate for this I developed some heuristics to help guide the search and evaluation in a more targeted way.
```

## C

[![](/images/thumb/6/66/Hiaclassic.jpg/300px-Hiaclassic.jpg)](http://www.thorstenczub.de/hiarcs.html)

HIARCS 1 for [MS-DOS](/MS-DOS "MS-DOS"), 1991 [[5]](#cite_note-5) , download from the HIARCS site [[6]](#cite_note-6)

End of the 80s HIARCS was rewritten in [C](/C "C"). In 1991 HIARCS **1.0** was released for [PCs](/IBM_PC "IBM PC") and the [MS-DOS](/MS-DOS "MS-DOS") operatig system. Subsequent Hiacs versions were compiled to run under various processors and operating systems, such as [x86](/X86 "X86") and [PowerPC](/PowerPC "PowerPC") under [Windows](/Windows "Windows") and [Mac OS](/Mac_OS "Mac OS"), as well as mobile devices.

# Achievements

The rewritten HIARCS soon competed in [computer chess tournaments](/Tournaments_and_Matches "Tournaments and Matches"), in 1989 the [1st Computer Olympiad](/1st_Computer_Olympiad#Chess "1st Computer Olympiad"), and the [WMCCC 1991](/WMCCC_1991 "WMCCC 1991") in [Vancouver](https://en.wikipedia.org/wiki/Vancouver) where HIARCS won the title of the *World Amateur Microcomputer Chess Champion*. HIARCS won the gold medal (shared) at the [4th Computer Olympiad](/4th_Computer_Olympiad#Chess "4th Computer Olympiad"), and became [World Microcomputer Chess Software Champion](/World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship") at the [WMCCC 1993](/WMCCC_1993 "WMCCC 1993") in [Munich](https://en.wikipedia.org/wiki/Munich). HIARCS won several other tournaments or got top rankings, it won the [IPCCC 2007](/IPCCC_2007 "IPCCC 2007"), after [Rybka's](/Rybka "Rybka")  [disqualification](/World_Computer_Chess_Championship#RybkaDisqualification "World Computer Chess Championship") in June 2011 the [WCCC 2008](/WCCC_2008 "WCCC 2008"), and the [ICT 2009](/ICT_2009 "ICT 2009") [[7]](#cite_note-7). Further, HIARCS is two time [World Chess Software Champion](/World_Chess_Software_Championship "World Chess Software Championship"), succeeding at the [WCSC 2011](/WCSC_2011 "WCSC 2011") in [Tilburg](https://en.wikipedia.org/wiki/Tilburg), the [WCSC 2013](/WCSC_2013 "WCSC 2013") in [Yokohama](https://en.wikipedia.org/wiki/Yokohama), and the [PT 51](/PT_51 "PT 51") and [PT 53](/PT_53 "PT 53").

# HIARCS Team

HIARCS' [opening book authors](/Category:Opening_Book_Author "Category:Opening Book Author") over the time were [Eric Hallsworth](/Eric_Hallsworth "Eric Hallsworth"), [Sebastian Böhme](/Sebastian_B%C3%B6hme "Sebastian Böhme") and [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), who is also operating HIARCS regularly at various computer chess tournaments.

# Man-Machine

- [Aegon 1997](/Aegon_1997 "Aegon 1997")
- [Bareev versus HIARCS 2003](/Bareev_versus_HIARCS_2003 "Bareev versus HIARCS 2003")

# Descriptions

from the [ICGA](/ICGA "ICGA") tournament site [[8]](#cite_note-8) :

## 1999

```
HIARCS is written entirely in 'C' on a very spare time basis.
```

```
HIARCS searches around an order of magnitude less positions per second (av. 18,000) than most of its competitors. However, it makes up for this apparent slow speed by clever searching and accurate evaluation. HIARCS uses many selective search extension heuristics to guide the search and incorporates a sophisticated tapered search to resolve tactical uncertainties while finding positionally beneficial lines.
```

```
HIARCS won the title of World Microcomputer Chess Software Champion in 1993 in Munich, Germany and has won numerous other computer and human tournaments. HIARCS 7.0 is currently the top rated chess program on the SSDF and Selective Search rating lists.
```

```
In April 1997, HIARCS 6.0 became the first PC chess program to win a match played at tournament time controls over a FIDE International Master. This great achievement was further built on when HIARCS won the Godesberg Open ahead of Grandmasters and International Masters.
```

```
The version competing in this tournament is a new experimental version. The program will be a 32bit Windows version of HIARCS and will support tablebases. It is expected that all 4 piece and most 5 piece endgame tablebases will be available.
```

## 2008

```
HIARCS is one of the few original PC chess programs still competing in top level chess competition. It has been in development over the last twenty years and since 1991 has always been among the top chess programs in the world. In this time it has led world computer rating lists and won World Championship titles. It was the first PC chess program to defeat a FIDE International Master in a match and has been a favourite of a number of World Chess Champions. So much so that Garry Kasparov said towards the end of his match with Deep Blue2 that "HIARCS is much better positionally than Deep Blue". HIARCS is available on a number of platforms including PC, Macintosh and handheld devices. The handheld Palm version has won multiple matches against GMs and even won a GM/IM tournament in the Philippines. HIARCS' playing style is now very aggressive with a distinctive liking for attacking the opponent's king. This often leads to dynamic exciting games which are often played on a knife-edge. HIARCS is now capable of taking advantage of multi-processors/cores to improve its chess performance making it a very dangerous opponent.
```

# Commerce

HIARCS is commercially available since 1991. PC- and [Windows](/Windows "Windows") versions until 12.0 were market as [ChessBase](/ChessBase "ChessBase") engine in conjunction with the [Fritz GUI](/Fritz#FritzGUI "Fritz") [[9]](#cite_note-9) , *PC Chess HIARCS 13 UCI* is purchased as download product from its own site [[10]](#cite_note-10) , and requires a [Windows](/Windows "Windows") PC and an external [GUI](/GUI "GUI") supporting the [UCI](/UCI "UCI") protocol. HIARCS 12.1 and 13 are the chess engines of [Pocket Fritz](/Fritz#PocketFritz "Fritz") by [ChessBase](/ChessBase "ChessBase") [[11]](#cite_note-11) [[12]](#cite_note-12) .

# Chess Explorer

Since August 2012, HIARCS has its own [GUI](/GUI "GUI"). The [HIARCS Chess Explorer](/HIARCS_Chess_Explorer "HIARCS Chess Explorer") is bundled with HIARCS 14, based on the program which won the [WCSC 2011](/WCSC_2011 "WCSC 2011"), and can further be used with any [UCI](/UCI "UCI") compatible chess engine [[13]](#cite_note-13) .

# Release Dates

- HIARCS 1 : 1992
- HIARCS 2 : 1993
- HIARCS 2.1 : 1993
- HIARCS 3 : 1994
- HIARCS 4 : 1995
- HIARCS 5 : 1996
- HIARCS 6 : 1997
- HIARCS 7 : 1998
- HIARCS 7.32 : 1999
- HIARCS 8 : 2002
- HIARCS 9: 2003
- HIARCS 9.6 : 2004
- HIARCS 10 : 2005
- HIARCS X50 :
- HIARCS X54 :
- HIARCS 11 : 2006
- HIARCS 11.1 : 2007
- HIARCS 11.2 : 2007
- HIARCS Paderborn 2007-12
- HIARCS 12.1 : 2008
- HIARCS 13 : 2009
- HIARCS 13.1 : 2010
- HIARCS 13.2 : 2010
- HIARCS 14 : 2011

[![Hiarcs14.gif](/images/5/5c/Hiarcs14.gif)](/File:Hiarcs14.gif)

HIARCS [Chess Strength](/Playing_Strength "Playing Strength") [[14]](#cite_note-14)

# See also

- [Knowledge | Search versus Evaluation](/Knowledge#SearchVersusEvaluation "Knowledge")

# Publictions

- [Eric Hallsworth](/Eric_Hallsworth "Eric Hallsworth") (**1992**). *HIARCS for PC's*. [Selective Search](/Selective_Search "Selective Search") 43, pp. 2, [pdf](http://www.chesscomputeruk.com/SS_43.pdf) hosted by [Mike Watters](/Mike_Watters "Mike Watters")
- [Jan van Reek](/Jan_van_Reek "Jan van Reek"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**2003**). *The Match Bareev vs. HIARCS X*. [ICGA Journal, Vol. 26, No. 1](/ICGA_Journal#26_1 "ICGA Journal") » [Bareev versus HIARCS 2003](/Bareev_versus_HIARCS_2003 "Bareev versus HIARCS 2003")
- [Eric Hallsworth](/Eric_Hallsworth "Eric Hallsworth") (**2003**). *HIARCS 8X v Evgeny Bareev*. [Selective Search](/Selective_Search "Selective Search") 104, pp. 20, [pdf](http://www.chesscomputeruk.com/SS_104.pdf) hosted by [Mike Watters](/Mike_Watters "Mike Watters")
- [Eric Hallsworth](/Eric_Hallsworth "Eric Hallsworth") (**2003**). *HIARCS 8X v Evgeny Bareev - The Final Game*. [Selective Search](/Selective_Search "Selective Search") 105, pp. 11, [pdf](http://www.chesscomputeruk.com/SS_105.pdf) hosted by [Mike Watters](/Mike_Watters "Mike Watters")
- [Thorsten Czub](/Thorsten_Czub "Thorsten Czub") (**2003**). *Mark Uniacke interviewed - Programming HIARCS 9*. [Selective Search](/Selective_Search "Selective Search") 108, pp. 12, [pdf](http://www.chesscomputeruk.com/SS_108.pdf) hosted by [Mike Watters](/Mike_Watters "Mike Watters")

# Forum Posts

## 1993 ...

- [Challenger to MCh/CG](http://groups.google.com/group/rec.games.chess/browse_frm/thread/5e54bae88f6b6eb1) by [Mark Uniacke](/Mark_Uniacke "Mark Uniacke"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), August 25, 1993
- [QMW computer chess](http://groups.google.com/group/rec.games.chess/browse_frm/thread/51267e26536fa912) by [Don Beal](/Don_Beal "Don Beal"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), August 19, 1993 » [UPCCC 1993](/UPCCC_1993 "UPCCC 1993")
- [HIARCS 2.0 Chess Program](http://groups.google.com/group/rec.games.chess/browse_frm/thread/58dba369aec90ce6/027edb10614a55fc) by Bryant Fujimoto, [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), December 5, 1993

## 1995 ...

- [Announcing HIARCS 4.0 for PC and MAC](https://groups.google.com/d/msg/rec.games.chess.computer/Pr3v1IamqT0/wdbB8PnDYEgJ) by [Mark Uniacke](/Mark_Uniacke "Mark Uniacke"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), December 19, 1995
- [Hiarchs Mac: First Impressions](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1ebbee2bcc0ae853) by [Eric Schiller](/Eric_Schiller "Eric Schiller"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 27, 1996
- [HIARCS 5 Maximum Search Depth](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/cc9d40ca3989dfac) by Kevin Miller, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 7, 1997
- [AEGON 97/ 1st round: HIARCS lost](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/49e5507bd20aa3ca) by Enrico, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), April 16, 1997
- [[REVIEW](https://groups.google.com/d/msg/rec.games.chess.computer/8T8Vu5RExFs/ly4pvg-ihg4J) HIARCS 6.0 Macintosh (long)] by Richard A. Fowell, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), December 12, 1997
- [LCT II results of Reb9, F5, and H6 on K6/233](https://www.stmintz.com/ccc/index.php?id=13605) by [Albert Silver](/Albert_Silver "Albert Silver"), [CCC](/CCC "CCC"), January 03, 1998 » [LCT II](/LCT_II "LCT II"), [Rebel](/Rebel "Rebel"), [Fritz](/Fritz "Fritz")
- [Horrible move!](https://www.stmintz.com/ccc/index.php?id=18139) by [Tony Hedlund](/Tony_Hedlund "Tony Hedlund"), [CCC](/CCC "CCC"), May 07, 1998 » [Fifty-move Rule](/Fifty-move_Rule "Fifty-move Rule")
- [Mark Uniacke has written on of the very best chess programs - HIARCS 6](https://www.stmintz.com/ccc/index.php?id=24082) by [Moritz Berger](/Moritz_Berger "Moritz Berger"), [CCC](/CCC "CCC"), August 07, 1998
- [FREE Hiarcs 7.01 update for Hiarcs 7.0 owners!](https://www.stmintz.com/ccc/index.php?id=44057) by [Mark Uniacke](/Mark_Uniacke "Mark Uniacke"), [CCC](/CCC "CCC"), February 21, 1999

## 2000 ...

- [Mark Uniacke has made really progress with Hiarcs9!](https://www.stmintz.com/ccc/index.php?id=317072) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), September 22, 2003
- [Palm Hiarcs stronger than Pocket Fritz 2](https://www.stmintz.com/ccc/index.php?id=378533) by [[Mark Uniacke], [CCC](/CCC "CCC"), July 22, 2004
- [HIARCS 11.1 SP / MP Macintosh has arrived!](http://www.talkchess.com/forum/viewtopic.php?t=12843) by rafowell, [CCC](/CCC "CCC"), Apr 03, 2007 » [Macintosh](/Macintosh "Macintosh")
- [Re: Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?p=2944) by [Mark Uniacke](/Mark_Uniacke "Mark Uniacke"), [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), October 14, 2007
- [World Computer Chess Championship 2008 HIARCS wins!](http://www.hiarcs.net/forums/viewtopic.php?t=1677) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 06, 2008 » [WCCC 2008](/WCCC_2008 "WCCC 2008")

:   [World Computer Chess Championship 2008 HIARCS wins!](http://hiarcs.net/forums/viewtopic.php?t=1677&postdays=0&postorder=asc&start=180) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 16, 2011

- [Free HIARCS Chess Software Programs](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=29812) by [Ted Summers](/Ted_Summers "Ted Summers"), [CCC](/CCC "CCC"), September 19, 2009

## 2010 ...

- [Hiarcs 13.1 MP UCI](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=34915) by [Kurt Utzinger](/Kurt_Utzinger "Kurt Utzinger"), [CCC](/CCC "CCC"), June 13, 2010
- [World Computer Software Championship 2011 - HIARCS wins!!](http://www.hiarcs.net/forums/viewtopic.php?t=4550) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 26, 2011 » [WCSC 2011](/WCSC_2011 "WCSC 2011")
- [HIARCS World Computer Software Champion 2013!](http://www.hiarcs.net/forums/viewtopic.php?t=6024) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), June 04, 2013 » [WCSC 2013](/WCSC_2013 "WCSC 2013")
- [The Future of HIARCS](http://www.hiarcs.net/forums/viewtopic.php?t=7961) by [Fernando Villegas](/Fernando_Villegas "Fernando Villegas"), [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 05, 2016 » [WCCC 2016](/WCCC_2016 "WCCC 2016"), [WCSC 2016](/WCSC_2016 "WCSC 2016")
- [53rd Programmers Tournament Leiden 2018 - Hiarcs wins!](http://www.hiarcs.net/forums/viewtopic.php?t=8965) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 30, 2018 » [PT 53](/PT_53 "PT 53")

## 2020 ...

- [Hiarcs Version 1](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79006) by [AdminX](/Ted_Summers "Ted Summers"), [CCC](/CCC "CCC"), December 31, 2021
- [Hiarcs Chess Explorer Pro - Coming Soon! (Now Released)](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79025) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [CCC](/CCC "CCC"), January 01, 2022 » [HIARCS Chess Explorer](/HIARCS_Chess_Explorer "HIARCS Chess Explorer")

# External Links

- [HIARCS Chess Software for PC, Mac, Pocket PC, iPhone, iPod and Palm Chess](https://www.hiarcs.com/)
- [HIARCS' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=53)
- [HIARCS from Wikipedia](https://en.wikipedia.org/wiki/HIARCS)
- [HIARCS Fan Page](http://www.thorstenczub.de/hiarcs.html) by [Thorsten Czub](/Thorsten_Czub "Thorsten Czub")
- [HIARCS 9](http://www.thorstenczub.de/hiarcs9.html) by [Thorsten Czub](/Thorsten_Czub "Thorsten Czub")
- [HIARCS 13 – the Professional Openings Book](https://en.chessbase.com/post/hiarcs-13-the-profeional-openings-book) by [Mark Uniacke](/Mark_Uniacke "Mark Uniacke"), [ChessBase News](/ChessBase "ChessBase"), March 10, 2011 » [Opening Book](/Opening_Book "Opening Book")
- [HIARCS Forum](https://www.hiarcs.net/forums/)

# References

1. [↑](#cite_ref-1) [PC Chess Software - HIARCS Chess Explorer download](http://www.hiarcs.com/pc-chess-explorer.htm)
2. [↑](#cite_ref-2) [HIARCS: Where It All Began](http://www.hiarcs.com/beginning.htm)
3. [↑](#cite_ref-3) [Now Walking, 1982-1983: HIARCS 5](http://www.hiarcs.com/nowwalking.htm)
4. [↑](#cite_ref-4) [Larry Harris](/Larry_Harris "Larry Harris") (**1974**). *Heuristic Search under Conditions of Error*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 5, No. 3, also as (**1977**). *The heuristic search: An alternative to the alpha-beta minimax procedure.* [Chess Skill in Man and Machine](/Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
5. [↑](#cite_ref-5) [HIARCS Fan Page](http://www.thorstenczub.de/hiarcs.html) by [Thorsten Czub](/Thorsten_Czub "Thorsten Czub")
6. [↑](#cite_ref-6) [Free HIARCS Chess Software Programs](http://www.hiarcs.com/freechess.htm)
7. [↑](#cite_ref-7) [HIARCS Milestone Achievements](http://www.hiarcs.com/hiarcs_milestones.htm)
8. [↑](#cite_ref-8) [HIARCS' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=53)
9. [↑](#cite_ref-9) [ChessBase Shop - HIARCS 12](http://www.chessbase.com/shop/productlist.asp?product=cp&subd=HIARCS) from [ChessBase](/ChessBase "ChessBase")
10. [↑](#cite_ref-10) [HIARCS for PC Chess Software](http://www.hiarcs.com/pc_chess_hiarcs.htm)
11. [↑](#cite_ref-11) [HIARCS Chess Software: What's New](http://www.hiarcs.com/news.htm)
12. [↑](#cite_ref-12) [HIARCS from Wikipedia](https://en.wikipedia.org/wiki/HIARCS#HIARCS_13_.282009.29)
13. [↑](#cite_ref-13) [HIARCS Chess Explorer - World class chess database and chess playing program](http://www.hiarcs.com/chess-explorer.htm)
14. [↑](#cite_ref-14) [HIARCS Chess Strength - from the official HIARCS site](http://www.hiarcs.com/hiarcs_info.htm)

**[Up one level](/Engines "Engines")**