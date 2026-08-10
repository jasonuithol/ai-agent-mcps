# Frenzee

Source: https://www.chessprogramming.org/Frenzee

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Frenzee**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Physiognomy.jpg/330px-Physiognomy.jpg)](/File:Physiognomy.jpg)

Frenzied [[1]](#cite_note-1)

**Frenzee**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess engine by [Sune Fischer](/Sune_Fischer "Sune Fischer"), written in [C++](/Cpp "Cpp") and capable to play [Chess960](/Chess960 "Chess960"), first released in January 2002 [[2]](#cite_note-2) as **ChessCraft** [[3]](#cite_note-3) and soon renamed to avoid confusion with [Crafty](/Crafty "Crafty") [[4]](#cite_note-4).
Frenzee is a [bitboard](/Bitboards "Bitboards") engine using [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") [[5]](#cite_note-5). It applies [PVS](/Principal_Variation_Search "Principal Variation Search") and [null move pruning](/Null_Move_Pruning "Null Move Pruning"), has its own [book learning](/Book_Learning "Book Learning") technique, and is able to probe [Nalimov tablebases](/Nalimov_Tablebases "Nalimov Tablebases"). The [parallel searching](/Parallel_Search "Parallel Search") version **Deep Frenzee** [shares](/Shared_Hash_Table "Shared Hash Table") the [transposition table](/Transposition_Table "Transposition Table") [[6]](#cite_note-6). Frenzee further supports [UCI](/UCI "UCI") in analyze mode.

# Tournament Play

Frenzee played five consecutive [CCT Tournaments](/CCT_Tournaments "CCT Tournaments"), starting with [CCT5](/CCT5 "CCT5") in January 2003, and two strong [ACCA World Computer Rapid Chess Championships](/ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship"), the [WCRCC 2007](/WCRCC_2007 "WCRCC 2007") and [WCRCC 2008](/WCRCC_2008 "WCRCC 2008").

# Selected Games

[WCRCC 2008](/WCRCC_2008 "WCRCC 2008"), round 5, Frenzee - [ZCT](/ZCT "ZCT") [[7]](#cite_note-7)

```
[Event "WCRCC 2008"]
[Site "Internet Chess Club"]
[Date "2008.06.21"]
[Round "5"]
[White "Frenzee"]
[Black "ZCT"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.c3 d5 4.Qa4 f6 5.d3 Be6 6.Be3 Nh6 7.Bxh6 gxh6 8.Nbd2 Qe7 9.O-O-O d4 
10.cxd4 exd4 11.Nxd4 Qc5+ 12.Nc2 O-O-O 13.Nf3 b5 14.d4 bxa4 15.Ba6+ Kb8 16.dxc5 Rxd1+ 
17.Rxd1 Bxc5 18.Bb5 Ne5 19.Ncd4 Bxa2 20.Nxe5 fxe5 21.Nc6+ Kb7 22.Bxa4 Rg8 23.Rd2 Rxg2 
24.b4 Bxf2 25.Rxa2 Be3+ 26.Kb1 Rg1+ 27.Kc2 Bf4 28.Kd3 Re1 29.Kc4 Rxe4+ 30.Kd5 Re3 31.Bb5 
Rc3 32.Rxa7+ Kb6 33.Ra5 Be3 34.Nxe5 c6+ 35.Bxc6 Kc7 36.Ra8 Bg1 37.Rh8 Bxh2 38.Rxh7+ Kc8 
39.b5 Bg1 40.Nc4 Rd3+ 41.Ke6 Re3+ 42.Nxe3 Bxe3 43.Bb7+ Kb8 44.Kd6 Bf4+ 45.Kc6 Be5 46.b6 
Bd4 47.Rc7 Bxb6 48.Rc8+ Ka7 49.Ra8# 1-0
```

# Forum Posts

## 2002 ...

- [New engine?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35736) by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 14, 2002
- [Re: KDL Chess released! + Update and new name for ChessCraft](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36801&start=4) by [Leo Dijksman](/Leo_Dijksman "Leo Dijksman"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 10, 2002
- [New Frenzee version 117](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37042) by [Sune Fischer](/Sune_Fischer "Sune Fischer"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 27, 2002
- [Bug in Frenzee](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37162) by [Sune Fischer](/Sune_Fischer "Sune Fischer"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 06, 2002
- [The Frenzee Report](https://www.stmintz.com/ccc/index.php?id=278587) by [Sune Fischer](/Sune_Fischer "Sune Fischer"), [CCC](/CCC "CCC"), January 21, 2003 » [CCT5](/CCT5 "CCT5")
- [New frenzee](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46310) by [Sune Fischer](/Sune_Fischer "Sune Fischer"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 02, 2004
- [Message for Frenzee programmer ...](https://www.stmintz.com/ccc/index.php?id=358305) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), April 04, 2004
- [Re: Attack table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=171#p518) by [Sune Fischer](/Sune_Fischer "Sune Fischer"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), October 07, 2004

## 2005 ...

- [PocketPC](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3138&p=15323) by [Sune Fischer](/Sune_Fischer "Sune Fischer"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 20, 2005
- [Re: 6-men Nalimov EGTB](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4692&p=25039) by [Sune Fischer](/Sune_Fischer "Sune Fischer"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 22, 2006
- [Frenzee 3.0 64-bit: #13 free 1-CPU engine in CCRL 40/4](http://www.talkchess.com/forum/viewtopic.php?t=14579) by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov"), [CCC](/CCC "CCC"), June 20, 2007
- [Deep Frenzee 3.0 as UCI: hash size?](http://www.talkchess.com/forum/viewtopic.php?t=17498) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), October 31, 2007
- [Question about Frenzee feb 08](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=7133&p=32748) by Tugo, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 11, 2008

## 2010 ...

- [Next one: The good programmers come back ... Frenzee](http://talkchess.com/forum3/viewtopic.php?t=40991) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), November 03, 2011

# External Links

## Chess Engine

- [Frenzee](https://web.archive.org/web/20020412101849/http://www.fys.ku.dk/~fischer/frenzee/frenzee.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2002)
- [Chess Engine Frenzee](https://web.archive.org/web/20060614093847/http://www.geocities.com/ruleren/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2006)
- [Chess Engine Frenzee](https://web.archive.org/web/20080705055115/http://www.computerskak.dk/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2008)

:   [Chess Engine Frenzee - FAQ.txt](https://web.archive.org/web/20080607180347/http://www.computerskak.dk/faq.txt)

- [Frenzee](http://web.archive.org/web/20080704173318/http://wbec-ridderkerk.nl/html/details1/Frenzee.html) from [WBEC Ridderkerk](/WBEC "WBEC") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Index of /chess/engines/Norbert's collection/Frenzee (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Frenzee%20%28Compilation%29/) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Frenzee](http://computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Frenzee&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")
- [Frenzee](http://www.computerchess.org.uk/ccrl/404FRC/cgi/compare_engines.cgi?family=Frenzee&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Score+with+common+opponents&match_length=30) in [CCRL 40/2 FRC](/CCRL "CCRL")

## Misc

- [frenzy - Wiktionary](https://en.wiktionary.org/wiki/frenzy)
- [Frenzy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Frenzy_(disambiguation))
- [Frenzy from Wikipedia](https://en.wikipedia.org/wiki/Frenzy)

# References

1. [↑](#cite_ref-1) [Illustration](https://commons.wikimedia.org/wiki/File:Physiognomy.jpg) in a 19th century book about [Physiognomy](https://en.wikipedia.org/wiki/Physiognomy) (on the left: "Utter despair", and on the right: "Anger mixed with fear"), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Frenzee](http://web.archive.org/web/20080704173318/http://wbec-ridderkerk.nl/html/details1/Frenzee.html) from [WBEC Ridderkerk](/WBEC "WBEC") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
3. [↑](#cite_ref-3) [New engine?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35736) by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 14, 2002
4. [↑](#cite_ref-4) [Frenzee](http://web.archive.org/web/20020412101849/http://www.fys.ku.dk/~fischer/frenzee/frenzee.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2002)
5. [↑](#cite_ref-5) [Chess Engine Frenzee - Sources](https://web.archive.org/web/20061204195709/http://www.geocities.com/ruleren/sources.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2006)
6. [↑](#cite_ref-6) [Deep Frenzee 3.0 - by Sune Fischer - FAQ](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Frenzee%20%28Compilation%29/Deep%20Frenzee%20v3.0%20wb/DeepFrenzee_3.0/faq.txt)
7. [↑](#cite_ref-7) [ZCTACCAWCRCC](http://www.talkchess.com/forum/viewtopic.php?t=22100) by [Zach Wegner](/Zach_Wegner "Zach Wegner"), [CCC](/CCC "CCC"), July 02, 2008

**[Up one Level](/Engines "Engines")**