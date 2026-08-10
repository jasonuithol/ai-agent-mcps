# Deep Sjeng

Source: https://www.chessprogramming.org/Deep_Sjeng

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Deep Sjeng**

**Deep Sjeng**,  
a private, and former commercial chess engine by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), which emerged in 2002 from the 12.7 closed source branch of the chess variant and chess playing [open source engine](/Category:Open_Source "Category:Open Source") [Sjeng](/Sjeng "Sjeng") [[1]](#cite_note-1) . Opposed to other commercial engines with the surename "deep" to indicate the version is able to play on multiple processors and sold for almost the double price than their "none deep" counterparts, Deep Sjeng, albeit able to play on multiple cores as well, is the native engine name for single as well as multiple processors.
Deep Sjeng was market since 2003 by [Lex Loep's](/Lex_Loep "Lex Loep") company [Lokasoft](/Lokasoft "Lokasoft") [[2]](#cite_note-2) . It came with the [ChessPartner](/ChessPartner "ChessPartner") [graphical interface](/GUI "GUI") and supports [UCI](/UCI "UCI") and the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). Version 2.X with the [Mayura Chess Board](/index.php?title=Mayura_Chess_Board&action=edit&redlink=1 "Mayura Chess Board (page does not exist)") [[3]](#cite_note-3) and its third incarnation Deep Sjeng 3.x were distributed via Gian-Carlo's own site, but Deep Sjeng is no longer for sale [[4]](#cite_note-4) .

# Tournaments

Deep Sjeng played many [computer chess tournaments](/Tournaments_and_Matches "Tournaments and Matches"). It participated (so far) at six [World Computer Chess Championships](/World_Computer_Chess_Championship "World Computer Chess Championship") [[5]](#cite_note-5) :

| Edition | | Tournament | Ranking | Participants | Score | Games |
| --- | --- | --- | --- | --- | --- | --- |
| 11th | [WCCC 2003](/WCCC_2003 "WCCC 2003") | [Graz](https://en.wikipedia.org/wiki/Graz) | 11 | 16 | 4.5 | 11 |
| 12th | [WCCC 2004](/WCCC_2004 "WCCC 2004") | [Ramat Gan](https://en.wikipedia.org/wiki/Ramat_Gan) | 10 | 14 | 5.5 | 11 |
| 13th | [WCCC 2005](/WCCC_2005 "WCCC 2005") | [Reykjavík](https://en.wikipedia.org/wiki/Reykjav%C3%ADk) | 3 | 12 | 7.5 | 11 |
| 15th | [WCCC 2007](/WCCC_2007 "WCCC 2007") | [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam) | 6 | 11 | 6 | 11 |
| 16th | [WCCC 2008](/WCCC_2008 "WCCC 2008") [[6]](#cite_note-6) | [Beijing](https://en.wikipedia.org/wiki/Beijing) | 8 | 10 | 3.5 | 9 |
| 17th | [WCCC 2009](/WCCC_2009 "WCCC 2009") [[7]](#cite_note-7) | [Pamplona](https://en.wikipedia.org/wiki/Pamplona) | 1 | 9 | 6.5 | 9 |

Deep Sjeng further played various [Dutch Open Computer Chess Championships](/Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"), [International CSVN Tournaments](/International_CSVN_Tournament "International CSVN Tournament"), [Livingston Chess960 Computer World Championships](/Livingston_Chess960_Computer_World_Championship "Livingston Chess960 Computer World Championship"), dominated [The Chess Programmers Tournament](/The_Chess_Programmers_Tournament "The Chess Programmers Tournament") with three wins so far from four editions, and won the Italian [IOCSC 2010](/IOCSC_2010 "IOCSC 2010"). Online Deep Sjeng played multiple [CCT Tournaments](/CCT_Tournaments "CCT Tournaments"), where Deep Sjeng won the [CCT12](/CCT12 "CCT12") in 2010 and [CCT13](/CCT13 "CCT13") in 2011. Since 2008, Deep Sjeng participated the [ACCA World Computer Rapid Chess Championship](/ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship") always with top rankings, winning the [WCRCC 2012](/WCRCC_2012 "WCRCC 2012").

# Screenshot

[![Deepsjeng2 1.png](/images/thumb/5/50/Deepsjeng2_1.png/827px-Deepsjeng2_1.png)](https://sjeng.org/deepsjeng2.html)

Deep Sjeng 2.5 with [Mayura Chess Board](/index.php?title=Mayura_Chess_Board&action=edit&redlink=1 "Mayura Chess Board (page does not exist)") [[8]](#cite_note-8)

# Parallel Search

[Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto") in a reply to [Georg von Zimmermann](/Georg_von_Zimmermann "Georg von Zimmermann") on Deep Sjeng's [parallel search](/Parallel_Search "Parallel Search") [[9]](#cite_note-9) :

How is Deep Sjeng going? What did you use to understand the parallel algorithms you are using (which ones) ?

```
I started out with ABDADA (described in ICCA journal article and used in Amy), which got me a speedup of +- 1.2. I went on to try PVS (Crafty 15.0 and described in several articles about parallel search) which got me a speedup of 1.2-1.3.
```

```
1.3 wasn't enough, so I 'bit the bullent' and started looking at DTS (Cray Blitz). Unfortunately, DTS is both hideously complicated and requires a nonrecursive search and a p2p design. I spent some time working on a variant of DTS that can work with a recursive search function and a master-slave design and that is what I am using now. It still needs a lot of test work, but current results indicate a speedup of about 1.6.
```

# Automated Learning

In 2007, Gian-Carlo's experimental program [Stoofvlees](/Stoofvlees "Stoofvlees") aka Deep Sjeng 2.7 [[10]](#cite_note-10) with a set of feature recognizers coupled to a [neural network](/Neural_Networks "Neural Networks") [[11]](#cite_note-11), had its [evaluation function](/Evaluation_Function "Evaluation Function") entirely [automatically](/Automated_Tuning "Automated Tuning") [learned](/Learning "Learning") from "watching" Grandmaster games. The results were incorporated into Deep Sjeng 3.0 [[12]](#cite_note-12). The engine has noticeably improved in strength, particularly in the areas where it was less optimal before.

# Forum Posts

- [Deep Sjeng testers wanted](https://www.stmintz.com/ccc/index.php?id=248485) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), August 28, 2002
- [Deep Sjeng 1.0 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/261bfb217175033a) by [Lex](/Lex_Loep "Lex Loep"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 3, 2003
- [Deep Sjeng Opteron Performance Results](https://www.stmintz.com/ccc/index.php?id=310212) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), August 06, 2003
- [Positions from the WCCC2005: Deep Sjeng - Zappa](https://www.stmintz.com/ccc/index.php?id=445348) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), August 26, 2005
- [Deep Sjeng 2.5 has arrived!](http://www.talkchess.com/forum/viewtopic.php?t=13368) by [Eelco de Groot](/index.php?title=Eelco_de_Groot&action=edit&redlink=1 "Eelco de Groot (page does not exist)"), April 24, 2007
- [Deep Sjeng 2.7 released](http://www.talkchess.com/forum/viewtopic.php?t=16244) by Jens, [CCC](/CCC "CCC"), September 03, 2007
- [Incredibly crazy game from Leiden: Deep Sjeng - The King](http://www.talkchess.com/forum/viewtopic.php?t=30193) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), October 18, 2009
- [Deep Sjeng @ 29th Dutch Open](http://www.talkchess.com/forum/viewtopic.php?t=30221) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), October 19, 2009
- [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316769&t=31545) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), January 08, 2010
- [Deep Sjeng 50-move rule bug](http://www.talkchess.com/forum/viewtopic.php?t=33259) by [Gabor Szots](/Gabor_Szots "Gabor Szots"), [CCC](/CCC "CCC"), March 14, 2010
- [Deep Sjeng @ ICT 2010](http://www.talkchess.com/forum/viewtopic.php?t=34671) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), June 02, 2010

# External Links

- [Sjeng - chess, audio and misc. software - Deep Sjeng 3.x](https://sjeng.org/deepsjeng3.html)
- [Sjeng's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=72) (mostly Deep Sjeng)
- [Sjeng (Chess) from Wikipedia](https://en.wikipedia.org/wiki/Sjeng_%28Chess%29)

# References

1. [↑](#cite_ref-1) [Sjeng 12.7 and 11.2 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/66707061247326df) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 2, 2002
2. [↑](#cite_ref-2) [Deep Sjeng 1.0 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/261bfb217175033a) by [Lex](/Lex_Loep "Lex Loep"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 3, 2003
3. [↑](#cite_ref-3) [SJENG.ORG - Deep Sjeng 2.x](http://sjeng.org/deepsjeng2.html)
4. [↑](#cite_ref-4) [SJENG.ORG - Deep Sjeng 3.x](http://sjeng.org/deepsjeng3.html)
5. [↑](#cite_ref-5) [Sjeng's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=72) (mostly Deep Sjeng)
6. [↑](#cite_ref-6) Deep Sjeng played the [WCCC 2008](/WCCC_2008 "WCCC 2008") under the name Sjeng, not to confused with the "old" Sjeng
7. [↑](#cite_ref-7) After the [disqualification](/World_Computer_Chess_Championship#RybkaDisqualification "World Computer Chess Championship") of [Rybka](/Rybka "Rybka") in June 2011, shared Champion with [Shredder](/Shredder "Shredder") and [Junior](/Junior "Junior")
8. [↑](#cite_ref-8) [Deep Sjeng 2.x - Screenshots](https://sjeng.org/deepsjeng2.html)
9. [↑](#cite_ref-9) [Re: Deep Sjeng testers wanted](https://www.stmintz.com/ccc/index.php?id=248594) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), August 29, 2002
10. [↑](#cite_ref-10) [Deep Sjeng 2.7 released](http://www.talkchess.com/forum/viewtopic.php?t=16244) by Jens, [CCC](/CCC "CCC"), September 03, 2007
11. [↑](#cite_ref-11) [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316511&t=31545) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), January 07, 2010
12. [↑](#cite_ref-12) [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316769&t=31545) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), January 08, 2010

**[Up one Level](/Engines "Engines")**