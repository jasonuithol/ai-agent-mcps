# Zappa

Source: https://www.chessprogramming.org/Zappa

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Zappa**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Frank_Zappa_in_Toronto%2C_Sept._24_1977.jpg/330px-Frank_Zappa_in_Toronto%2C_Sept._24_1977.jpg)](/File:Frank_Zappa_in_Toronto,_Sept._24_1977.jpg)

[Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa") [[1]](#cite_note-1)

**Zappa**,  
an [UCI](/UCI "UCI") compliant chess program developed by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"). Zappa won the [WCCC 2005](/WCCC_2005 "WCCC 2005") in [Reykjavík](https://en.wikipedia.org/wiki/Reykjav%C3%ADk), and after the [Rybka](/Rybka "Rybka") [disqualification](/World_Computer_Chess_Championship#RybkaDisqualification "World Computer Chess Championship") in 2011 the [WCCC 2007](/WCCC_2007 "WCCC 2007") in [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam), the [DOCCC 2005](/DOCCC_2005 "DOCCC 2005") and [CCT7](/CCT7 "CCT7").During the [World Chess Championship 2007](https://en.wikipedia.org/wiki/World_Chess_Championship_2007) in [Mexico City](https://en.wikipedia.org/wiki/Mexico_City), September 2007, Zappa played a [match](/Zappa_versus_Rybka_2007 "Zappa versus Rybka 2007") versus [Rybka](/Rybka "Rybka") and scored 5.5 / 10 to win the match [[2]](#cite_note-2) [[3]](#cite_note-3) [[4]](#cite_note-4) . Zappa's book authors for different events were [Arturo Ochoa](/Arturo_Ochoa "Arturo Ochoa") ([CCT7](/CCT7 "CCT7")) and [Erdogan Günes](/Erdogan_G%C3%BCnes "Erdogan Günes") [[5]](#cite_note-5) .

# Photos

[[6]](#cite_note-6)

[![Anthony2005.JPG](/images/7/79/Anthony2005.JPG)](/File:Anthony2005.JPG)

[Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie") before round 7, Zappa - [Junior](/Junior "Junior"), [WCCC 2005](/WCCC_2005 "WCCC 2005") [[7]](#cite_note-7)

[![ZappaTeam2006.JPG](/images/3/39/ZappaTeam2006.JPG)](/File:ZappaTeam2006.JPG)

Zappa Team, [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie") and [Erdogan Günes](/Erdogan_G%C3%BCnes "Erdogan Günes"), Closing Dinner [WCCC 2006](/WCCC_2006 "WCCC 2006"), [Turin](https://en.wikipedia.org/wiki/Turin)

# Etymology

Zappa is not directly named for [Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa"), but from a scene from [Austin Powers 2](https://en.wikipedia.org/wiki/Austin_Powers:_The_Spy_Who_Shagged_Me), where [Dr. Evil's](https://en.wikipedia.org/wiki/Dr._Evil_%28character%29) base in the moon is divided in two units: Moon Unit Alpha and Moon Unit Zappa - the latter being the name of Frank Zappa's daughter, [Moon Unit Zappa](https://en.wikipedia.org/wiki/Moon_Unit_Zappa) [[8]](#cite_note-8) .

# Strictly Commercial

Immediately after the successful [WCCC 2005](/WCCC_2005 "WCCC 2005"), there were plans to commercialize Zappa. First attempts with [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen") involved failed [[9]](#cite_note-9) . In April 2006 [[10]](#cite_note-10) , a commercial version dubbed **Zap!Chess** running under the [Fritz GUI](/Fritz#FritzGUI "Fritz") was released by [ChessBase](/ChessBase "ChessBase"). The version which played the Rybka match, Zappa Mexico, is distributed by [Stefan Meyer-Kahlen](/Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen").

Quote from *No Commercial Potential : The Saga of Frank Zappa* (**1972**) by David Walley, p. 4 [[11]](#cite_note-11) [[12]](#cite_note-12) [[13]](#cite_note-13) :

|  |  |
| --- | --- |
| Jawaka | Information is not knowledge  Knowledge is not wisdom  Wisdom is not truth  Truth is not beauty  Beauty is not love  Love is not music  Music is the best |

# Program Internals

## Board Representation

Zappa utilizes [bitboards](/Bitboards "Bitboards") and uses [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") to generate [sliding attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") on the fly. Anthony once experimented with [incremental updated](/Incremental_Updates "Incremental Updates") [attack tables](/Attack_and_Defend_Maps "Attack and Defend Maps"), which was a win on 32-bit systems [[14]](#cite_note-14) .

## Hash Collisions

Excerpt from *The Effect of [Hash Signature Collisions](/Transposition_Table#KeyCollisions "Transposition Table") in a Chess Program*, that is [Crafty](/Crafty "Crafty") and Zappa [[15]](#cite_note-15) :

```
Both programs are traditional computer chess programs that use the alpha/beta algorithm to search a minimax game tree. The search is done in three distinct phases.
```

```
Phase 1 is the normal full-width search that is done to some fixed depth as limited by the total time allowed for a move. This fixed-depth search is modified by various search extensions.
```

```
Phase 2 is an add-on search done after the basic search has reached a satisfactory depth. Phase 2 only considers captures in Crafty, while Zappa also includes some checking moves.
```

```
Phase 3 is the static evaluation, which takes the current position after phase 2 has completed, and computes a numerical score based on the material, the locations of the pieces, pawn structure, and many other positional considerations. In Crafty/Zappa, all of the hashing is done in phase1 of the search, there is no hashing in the quiescence search.
```

## Singular Extensions

**Zap!Chess**, the commercial [ChessBase](/ChessBase "ChessBase") version, has an implementation of [Singular Extensions](/Singular_Extensions "Singular Extensions"), the famous [Deep Blue](/Deep_Blue "Deep Blue") search algorithm. They are disabled by default, but they increase the tactical strength of the program at the cost of positional strength [[16]](#cite_note-16) .

## Parallel Search

Zappa was designed to run on multiple processors and massive parallel systems using [shared memory](/Memory#Shared "Memory") and [threads](/Thread "Thread") and has an efficient [parallel search](/Parallel_Search "Parallel Search") [[17]](#cite_note-17) . Zappa Mexico can be used on [Windows](/Windows "Windows") or [Linux](/Linux "Linux") computers with up to 512 CPU cores.

# 100% Finished

In March 2008 Anthony Cozzie announced that "the Zappa project is 100% finished", which includes both tournaments and future releases [[18]](#cite_note-18) .

# Rondo

In 2010, [Zach Wegner](/Zach_Wegner "Zach Wegner") started to work with [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), who, still in computer chess retirement, has given control for further development of his massive parallel program, now called [Rondo](/Rondo "Rondo"), to Zach [[19]](#cite_note-19) [[20]](#cite_note-20) .

# See also

- [Rondo](/Rondo "Rondo")

# Publications

- The Editor (**2005**). *ZAPPA Wins the Computer-Chess Tournament 7*. [ICGA Journal, Vol. 28, No. 2](/ICGA_Journal#28_2 "ICGA Journal") » [CCT7](/CCT7 "CCT7")
- [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie") (**2005**). *[The Effect of Hash Signature Collisions in a Chess Program](http://www.cis.uab.edu/hyatt/collisions.html)*. [ICGA Journal, Vol. 28, No. 3](/ICGA_Journal#28_3 "ICGA Journal")
- [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie") (**2007**). *Zappa vs. Rybka*. [ICGA Journal, Vol. 30, No. 4](/ICGA_Journal#30_4 "ICGA Journal")
- [Monty Newborn](/Monroe_Newborn "Monroe Newborn") (**2011**). *[Beyond Deep Blue: Chess in the Stratosphere](http://www.springer.com/computer/general+issues/book/978-0-85729-340-4)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), ISBN-13: 978-0857293404, [amazon](http://www.amazon.com/Beyond-Deep-Blue-Chess-Stratosphere/dp/0857293400)

:   [![BejDeepBlue.jpg](/images/d/dd/BejDeepBlue.jpg)](http://www.springer.com/computer/general+issues/book/978-0-85729-340-4)
:   Chapter 9: 2005: Zappa Red Hot at 13th WCCC, page 119
:   Chapter 14: 2007: Zappa Upsets Rybka in Mexico City, 5.5–4.5, page 169

# Forum Posts

## 2003

- [Zappa CCT5 Report](https://www.stmintz.com/ccc/index.php?id=278632) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), January 21, 2003 » [CCT5](/CCT5 "CCT5")

## 2004

- [Zappa @ CCT6](https://www.stmintz.com/ccc/index.php?id=346423) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), February 01, 2004 » [CCT6](/CCT6 "CCT6")
- [The Zappa Attack Table Code](https://www.stmintz.com/ccc/index.php?id=363519) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), May 05, 2004

## 2005 ...

- [Zappa 1.0 released](https://www.stmintz.com/ccc/index.php?id=413233) by [Volker Pittlik](/index.php?title=Volker_Pittlik&action=edit&redlink=1 "Volker Pittlik (page does not exist)"), [CCC](/CCC "CCC"), February 22, 2005
- [Zappa - TCB 1-0](https://www.stmintz.com/ccc/index.php?id=441791) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 14, 2005 » [WCCC 2005](/WCCC_2005 "WCCC 2005")
- [Sjeng-Zappa](https://www.stmintz.com/ccc/index.php?id=441966) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 14, 2005
- [FUTE-Zappa](https://www.stmintz.com/ccc/index.php?id=442363) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 15, 2005
- [Zappa=Fruit live](https://www.stmintz.com/ccc/index.php?id=442149) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 15, 2005
- [Zappa - Jonny 1-0](https://www.stmintz.com/ccc/index.php?id=442550) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 16, 2005
- [The Baron - Zappa 0-1](https://www.stmintz.com/ccc/index.php?id=442974) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 18, 2005
- [Zappa - Junior](https://www.stmintz.com/ccc/index.php?id=443224) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 19, 2005
- [Zappa-Isichess](https://www.stmintz.com/ccc/index.php?id=443322) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 19, 2005
- [Shredder-Zappa](https://www.stmintz.com/ccc/index.php?id=443467) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 20, 2005
- [Zappa - Crafty](https://www.stmintz.com/ccc/index.php?id=443579) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 20, 2005
- [Diep-Zappa](https://www.stmintz.com/ccc/index.php?id=443831) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 21, 2005
- [Zappa scaling #s](https://www.stmintz.com/ccc/index.php?id=444686) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 23, 2005
- [Zappa web update & a few other things](https://www.stmintz.com/ccc/index.php?id=445829) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 27, 2005
- [Zappa commercial and available in september](https://www.stmintz.com/ccc/index.php?id=445832) by Thomas Logan, [CCC](/CCC "CCC"), August 27, 2005
- [Re: Zappa Retail: No UCI?](https://www.stmintz.com/ccc/index.php?id=447511) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), September 04, 2005
- [Zappa UCI: You are all a bunch of HYPOCRITES](https://www.stmintz.com/ccc/index.php?id=447620) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), September 04, 2005
- [I will not buy Zappa and Sjeng](https://www.stmintz.com/ccc/index.php?id=447987) by [Sandro Necchi](/Sandro_Necchi "Sandro Necchi"), [CCC](/CCC "CCC"), September 06, 2005
- [Zappa 1.1](https://www.stmintz.com/ccc/index.php?id=449578) by [Ernst Walet](/index.php?title=Ernst_Walet&action=edit&redlink=1 "Ernst Walet (page does not exist)"), [CCC](/CCC "CCC"), September 14, 2005
- [Re: what do we know about zappa](https://www.stmintz.com/ccc/index.php?id=469523) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), December 12, 2005
- [Zappa Hardware Upgrade](https://www.stmintz.com/ccc/index.php?id=472806) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), December 23, 2005
- [Zappa Report](https://www.stmintz.com/ccc/index.php?id=475497) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), December 30, 2005 » [IPCCC 2005 b](/IPCCC_2005_b "IPCCC 2005 b")

:   [Re: Zappa Report](https://www.stmintz.com/ccc/index.php?id=475521) by [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer"), [CCC](/CCC "CCC"), December 30, 2005 [[21]](#cite_note-21)

**2006**

- [Zappa?](https://www.stmintz.com/ccc/index.php?id=482676) by James T. Walker, [CCC](/CCC "CCC"), January 27, 2006

**2007**

- [Zappa Mexico UCI going commercial](http://www.talkchess.com/forum/viewtopic.php?t=16369) by Kaj Soderberg, [CCC](/CCC "CCC"), September 09, 2007
- [Zappa V Rybka Mexico 2007 - Zappa wins 5.5-4.5 - The Games](http://hiarcs.net/forums/viewtopic.php?t=320) by [Harvey Williamson](/Harvey_Williamson "Harvey Williamson"), [Hiarcs Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 27, 2007

**2008 ...**

- [bad news from zappa ...](http://www.talkchess.com/forum/viewtopic.php?t=20058) by Powell, [CCC](/CCC "CCC"), Mar 09, 2008

## 2010 ...

- [info about zappa on 512 cores ?](http://www.talkchess.com/forum/viewtopic.php?t=44164) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), June 23, 2012
- [Threads-Test - SF, Zappa, Komodo - 1 vs. 2, 4, 8, 16 Threads](http://www.talkchess.com/forum/viewtopic.php?t=52219) by [Andreas Strangmüller](/Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](/CCC "CCC"), May 04, 2014 » [Thread](/Thread "Thread"), [Stockfish](/Stockfish "Stockfish"), Zappa, [Komodo](/Komodo "Komodo")
- [Threads factor: Komodo, Houdini, Stockfish and Zappa](http://www.talkchess.com/forum/viewtopic.php?p=570955) by [Andreas Strangmüller](/Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](/CCC "CCC"), May 17, 2014 » [Thread](/Thread "Thread"), [Komodo](/Komodo "Komodo"), [Houdini](/Houdini "Houdini"), [Stockfish](/Stockfish "Stockfish"), Zappa

## 2015 ...

- [Empirical results with Lazy SMP, YBWC, DTS](http://www.talkchess.com/forum/viewtopic.php?t=56019) by [Kai Laskos](/Kai_Laskos "Kai Laskos"), [CCC](/CCC "CCC"), April 16, 2015 » [Lazy SMP](/Lazy_SMP "Lazy SMP"), [YBWC](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), [DTS](/Dynamic_Tree_Splitting "Dynamic Tree Splitting")
- [What is the secret of Zappa?](http://www.talkchess.com/forum/viewtopic.php?t=61400) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), September 11, 2016

# External Links

## Zappa Chess

- [Zappa Chess Engine](http://www.acoz.net/zappa/)
- [Zappa's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=58)
- [Zappa (chess) from Wikipedia](https://en.wikipedia.org/wiki/Zappa_%28chess%29)
- [The chess games of Zappa (Computer)](http://www.chessgames.com/perl/chessplayer?pid=96888) from [chessgames.com](http://www.chessgames.com/index.html)
- [World Computer Chess Champion: Zap!Chess](http://www.chessbase.com/newsdetail.asp?newsid=3043), [ChessBase News](/ChessBase "ChessBase"), April 13, 2006
- [Man vs Machine, Zap!Chess vs Erwin L'Ami 1-1](http://www.chessbase.com/newsdetail.asp?newsid=3718) by [Eric van Reem](/Eric_van_Reem "Eric van Reem"), [ChessBase News](/ChessBase "ChessBase"), March 08, 2007 [[22]](#cite_note-22) » [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk")
- [Zappa Mexico II available now](http://www.shredderchess.com/chess-news/shredder-news/zappa-mexico-ii.html) from [shredderchess.com](http://www.shredderchess.com/)

## Zappa

- [Frank Zappa from Wikipedia](https://en.wikipedia.org/wiki/Frank_Zappa)
- [Moon Zappa from Wikipedia](https://en.wikipedia.org/wiki/Moon_Zappa)
- [Dweezil Zappa from Wikipedia](https://en.wikipedia.org/wiki/Dweezil_Zappa)
- [Frank Zappa - Wikiquote](http://en.wikiquote.org/wiki/Frank_Zappa)
- [The Mothers of Invention from Wikipedia](https://en.wikipedia.org/wiki/The_Mothers_of_Invention)
- [Zappanale from Wikipedia](https://en.wikipedia.org/wiki/Zappanale)
- [Zappa Wiki Jawaka!](http://wiki.killuglyradio.com/wiki/Main_Page)
- [(3834) Zappafrank](https://minorplanetcenter.net//iau/special/rocknroll/0003834.html) (Planet)
- [3834 Zappafrank from Wikipedia](https://en.wikipedia.org/wiki/3834_Zappafrank)
- [Pachygnatha Zappa from Wikipedia](https://en.wikipedia.org/wiki/Pachygnatha_zappa)
- [Zappa confluentus from Wikipedia](https://en.wikipedia.org/wiki/Zappa_confluentus)
- [Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa") - [The Ocean Is the Ultimate Solution](https://en.wikipedia.org/wiki/Sleep_Dirt) (1979), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   lineup: [Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa"), [Patrick O'Hearn](https://en.wikipedia.org/wiki/Patrick_O%27Hearn), [Terry Bozzio](/Category:Terry_Bozzio "Category:Terry Bozzio"), [George Duke](/Category:George_Duke "Category:George Duke"), [Bruce Fowler](https://en.wikipedia.org/wiki/Bruce_Fowler), [Chester Thompson](/Category:Chester_Thompson "Category:Chester Thompson"), [Ruth Underwood](https://en.wikipedia.org/wiki/Ruth_Underwood)

# References

1. [↑](#cite_ref-1) [Frank Zappa](/Category:Frank_Zappa "Category:Frank Zappa"), [Records on wheels, Toronto](https://www.blogto.com/music/2016/03/10_lost_but_not_forgotten_record_stores_in_toronto/), September 24, 1977, [Frank Zappa - Wikimedia Commons](https://commons.wikimedia.org/wiki/Frank_Zappa)
2. [↑](#cite_ref-2) [WM Mexiko-City 2007: 108 Bilder, Namen, Themen, kommentiert, ...](http://www.chesstigers.de/index_news.php?id=1269&rubrik=3) (German) [Chess Tigers News](http://www.chesstigers.de/index.php) October 08, 2007
3. [↑](#cite_ref-3) [Zappa fillets the Fish: Mexico 2007](http://www.acoz.net/zappa/mexico/) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie")
4. [↑](#cite_ref-4) [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie") (**2007**). *Zappa vs. Rybka*. [ICGA Journal, Vol. 30, No. 4](/ICGA_Journal#30_4 "ICGA Journal")
5. [↑](#cite_ref-5) [Zappa Chess Engine](http://www.acoz.net/zappa/)
6. [↑](#cite_ref-6) By [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg")
7. [↑](#cite_ref-7) [Zappa - Junior](https://www.stmintz.com/ccc/index.php?id=443224) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 19, 2005
8. [↑](#cite_ref-8) [Zappa Chess Engine - Genealogy](http://www.acoz.net/zappa/#Name)
9. [↑](#cite_ref-9) [Re: Zappa Retail: No UCI?](https://www.stmintz.com/ccc/index.php?id=447511) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), September 04, 2005
10. [↑](#cite_ref-10) [World Computer Chess Champion: Zap!Chess](http://www.chessbase.com/newsdetail.asp?newsid=3043), [ChessBase News](/ChessBase "ChessBase"), April 13, 2006
11. [↑](#cite_ref-11) [No Commercial Potential: The Saga Of Frank Zappa](http://www.amazon.com/No-Commercial-Potential-Frank-Zappa/dp/0306807106)
12. [↑](#cite_ref-12) [Frank Zappa - Wikiquote](http://en.wikiquote.org/wiki/Frank_Zappa)
13. [↑](#cite_ref-13) [No Commercial Potential: The Saga of Frank Zappa - Zappa Wiki Jawaka](http://wiki.killuglyradio.com/wiki/No_Commercial_Potential:_The_Saga_of_Frank_Zappa)
14. [↑](#cite_ref-14) [The Zappa Attack Table Code](https://www.stmintz.com/ccc/index.php?id=363519) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), May 05, 2004
15. [↑](#cite_ref-15) [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie") (**2005**). *[The Effect of Hash Signature Collisions in a Chess Program](http://www.cis.uab.edu/hyatt/collisions.html)*. [ICGA Journal, Vol. 28, No. 3](/ICGA_Journal#28_3 "ICGA Journal")
16. [↑](#cite_ref-16) [World Computer Chess Champion: Zap!Chess](http://www.chessbase.com/newsdetail.asp?newsid=3043), [ChessBase News](/ChessBase "ChessBase"), April 13, 2006
17. [↑](#cite_ref-17) [Zappa scaling #s](https://www.stmintz.com/ccc/index.php?id=444686) by [Anthony Cozzie](/Anthony_Cozzie "Anthony Cozzie"), [CCC](/CCC "CCC"), August 23, 2005
18. [↑](#cite_ref-18) [bad news from zappa ...](http://www.talkchess.com/forum/viewtopic.php?t=20058) by Powell, [CCC](/CCC "CCC"), Mar 09, 2008
19. [↑](#cite_ref-19) [Zach, is this true?](http://www.talkchess.com/forum/viewtopic.php?t=34749) by [Gabor Szots](/Gabor_Szots "Gabor Szots"), [CCC](/CCC "CCC"), June 06, 2010
20. [↑](#cite_ref-20) [Zappa's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=58)
21. [↑](#cite_ref-21) [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1993**). *On Telescoping Linear Evaluation Functions.* [ICCA Journal, Vol. 16, No. 2](/ICGA_Journal#16_2 "ICGA Journal"), pp. 91-94
22. [↑](#cite_ref-22) [Erwin l'Ami from Wikipedia](https://en.wikipedia.org/wiki/Erwin_l%27Ami)

**[Up one level](/Engines "Engines")**