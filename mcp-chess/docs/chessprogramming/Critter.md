# Critter

Source: https://www.chessprogramming.org/Critter

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Critter**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Agropelter.jpg/330px-Agropelter.jpg)](/File:Agropelter.jpg)

[Agropelter](https://en.wikipedia.org/wiki/Agropelter), a [fearsome critter](https://en.wikipedia.org/wiki/Fearsome_critters) [[1]](#cite_note-1)

**Critter**,  
an [UCI](/UCI "UCI") compliant chess engine by [Richard Vida](/Richard_Vida "Richard Vida"), executables freely available for personal use to run under [Windows](/Windows "Windows"), [Linux](/Linux "Linux"), [Android](/Android "Android") and [Mac OS](/Mac_OS "Mac OS") [[2]](#cite_note-2) . Starting in late 2008, Critter was first written in [Object Pascal](/Pascal "Pascal") compiled with [Delphi](/Delphi "Delphi"), now available as [open source engine](/Category:Open_Source "Category:Open Source") [[3]](#cite_note-3) [[4]](#cite_note-4), and was ported to [C](/C "C") / [C++](/Cpp "Cpp") in 2009 [[5]](#cite_note-5) . It consistently evolved through various board representations from [0x88](/0x88 "0x88") to [bitboards](/Bitboards "Bitboards"), as acknowledged by Richard Vida, also incorporating ideas from strong open source programs like [Ippolit](/Ippolit "Ippolit") [[6]](#cite_note-6) , to a world class engine which achieved top five of most [engine rating lists](/Engine_Rating_Lists "Engine Rating Lists") [[7]](#cite_note-7). In 2012, Critter had its over the board debut at the [ICT 2012](/ICT_2012 "ICT 2012"), where it became strong runner-up behind the [Rybka](/Rybka "Rybka") cluster.

# Description

Critter applies a [principal variation search](/Principal_Variation_Search "Principal Variation Search") with [aspiration windows](/Aspiration_Windows "Aspiration Windows"), [null move pruning](/Null_Move_Pruning "Null Move Pruning") [[8]](#cite_note-8) and other state of the art [forward pruning](/Pruning "Pruning"), [reduction](/Reductions "Reductions") and [extension techniques](/Extensions "Extensions"), such as the [Botvinnik-Markoff extensions](/Botvinnik-Markoff_Extension "Botvinnik-Markoff Extension") [[9]](#cite_note-9) . It can [search in parallel](/Parallel_Search "Parallel Search") with up to eight [threads](/Thread "Thread") [[10]](#cite_note-10) , supports [Gaviota tablebases](/Gaviota_Tablebases "Gaviota Tablebases") [[11]](#cite_note-11) , and is able to play [Chess960](/Chess960 "Chess960") [[12]](#cite_note-12) . Critter features a [tapered eval](/Tapered_Eval "Tapered Eval") with a [score pair](/Score "Score") class and overloaded operators [[13]](#cite_note-13) [[14]](#cite_note-14) , and [blockage detection](/Blockage_Detection "Blockage Detection") in late [endgames](/Endgame "Endgame") [[15]](#cite_note-15) .

# Selected Games

[ICT 2012](/ICT_2012 "ICT 2012"), round 7, [Rybka](/Rybka "Rybka") - Critter [[16]](#cite_note-16) [[17]](#cite_note-17)

```
[Event "ICT12"]
[Site "Leiden"]
[Date "2012.05.13"]
[Round "7"]
[White "Rybka"]
[Black "Critter"]
[Result "1/2-1/2"]

1.d4 d5 2.c4 e6 3.Nf3 c6 4.e3 Bd6 5.b3 f5 6.Bd3 Nf6 7.O-O Qe7 8.Bb2 O-O
9.Qc1 b6 10.Ba3 Bb7 11.Bxd6 Qxd6 12.Nc3 dxc4 13.Bxc4 Nbd7 14.Re1 b5
15.Bd3 b4 16.Na4 c5 17.Nxc5 Bxf3 18.gxf3 Rfc8 19.Bc4 Nxc5 20.dxc5 Rxc5
21.a3 bxa3 22.Qxa3 Nd5 23.Red1 Qc7 24.Kg2 Rd8 25.Bxd5 Rdxd5 26.Qa4 Qe7
27.Rxd5 Rxd5 28.Qxa7 Qxa7 29.Rxa7 Rb5 30.Re7 Rb6 31.Kg3 Kf8 32.Rd7 Rxb3
33.Kf4 Rb5 34.h4 h6 35.Kg3 Rb8 36.h5 Re8 37.Rb7 Re7 38.Rb5 Kf7 39.e4 Kf6
40.exf5 exf5 41.Kf4 Re2 42.Rxf5+ Ke6 43.Rb5 Rxf2 44.Rb6+ Kf7 45.Rb7+ Kf6
1/2-1/2
```

# Publications

- [Arno Nickel](/Arno_Nickel "Arno Nickel") (**2012**). *[Die schöne neue Welt der Schachengines](http://www.edition-marco-shop.de/epages/64079634.sf/de_DE/?ObjectPath=/Shops/64079634/Categories/Schachgeschehen/Computerschach)*. [SCHACH](http://www.zeitschriftschach.de/) 2,3,5,6 2012, [pdf](http://www.edition-marco-shop.de/WebRoot/Store14/Shops/64079634/5177/F0A3/C389/D0DD/3A71/C0A8/2935/25F6/Die_schoene_neue_Welt_der_Schachengines.pdf) (German) [[18]](#cite_note-18)

# Forum Posts

## 2009

- [Critter 0.34 : 2146](http://www.talkchess.com/forum/viewtopic.php?t=27504) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), April 18, 2009
- [Critter 0.38 : 2330](http://www.talkchess.com/forum/viewtopic.php?t=28064) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), May 22, 2009
- [Critter 0.40 released](http://www.talkchess.com/forum/viewtopic.php?t=29114) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), July 26, 2009
- [Critter 0.40 : 2471](http://www.talkchess.com/forum/viewtopic.php?t=29199) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), August 01, 2009
- [Critter: Pascal vs C](http://www.talkchess.com/forum/viewtopic.php?t=29562) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), August 27, 2009 » [C](/C "C"), [Pascal](/Pascal "Pascal")
- [Critter 0.42 available](http://www.talkchess.com/forum/viewtopic.php?t=30053) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), October 08, 2009 » [Pascal](/Pascal "Pascal")
- [Critter 0.42 : 2649](http://www.talkchess.com/forum/viewtopic.php?t=30093) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), October 11, 2009

## 2010 ...

- [Critter 0.52 available](http://www.talkchess.com/forum/viewtopic.php?t=32030) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), Jan 25, 2010 » [C](/C "C")
- [Critter 0.52b added to the IPON list ...](http://www.talkchess.com/forum/viewtopic.php?t=32370) by [Ingo Bauer](/Ingo_Bauer "Ingo Bauer"), [CCC](/CCC "CCC"), February 04, 2010
- [Strange knight underpromotion by Critter](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=335316&t=33059) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), March 04, 2010
- [Critter goes SMP (version 0.60 is released)](http://www.talkchess.com/forum/viewtopic.php?t=33774) by [Richard Vida](/Richard_Vida "Richard Vida"),[CCC](/CCC "CCC"), April 13, 2010
- [Critter 0.60: 2718](http://www.talkchess.com/forum/viewtopic.php?t=33801) by [Patrick Buchmann](/Patrick_Buchmann "Patrick Buchmann"), [CCC](/CCC "CCC"), April 14, 2010
- [Critter 0.70 is out](http://www.talkchess.com/forum/viewtopic.php?t=34470) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), May 23, 2010
- [Critter 0.80](http://www.talkchess.com/forum/viewtopic.php?t=35565) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), July 24, 2010
- [Critter 0.90 released](http://www.talkchess.com/forum/viewtopic.php?t=36854) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), November 29, 2010
- [Critter - looking at static evaluation](http://www.talkchess.com/forum/viewtopic.php?t=37041) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), December 11, 2010

**2011**

- [Critter 1.0 available](http://www.talkchess.com/forum/viewtopic.php?t=38435) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), March 16, 2011
- [Critter 1.0 for Linux](http://www.talkchess.com/forum/viewtopic.php?t=38515) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), March 22, 2011 » [Linux](/Linux "Linux")
- [My experience with Linux/GCC](http://www.talkchess.com/forum/viewtopic.php?t=38523) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), March 23, 2011
- [Critter bugfix update](http://www.talkchess.com/forum/viewtopic.php?t=38575) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), March 28, 2011 [[19]](#cite_note-19)
- [Critter 1.2 update + new homepage](http://www.talkchess.com/forum/viewtopic.php?t=39488) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), June 25, 2011 » [Android](/Android "Android")
- [Critter 1.2 SEEMS to be a member of the Ippo family](http://www.talkchess.com/forum/viewtopic.php?t=39577) by [Kai Laskos](/Kai_Laskos "Kai Laskos"), [CCC](/CCC "CCC"), July 02, 2011
- [for Pascal fans: Critter](http://www.talkchess.com/forum/viewtopic.php?t=40414) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), September 16, 2011

**2012 ...**

- [Re: World Computer Chess Championship ?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=468701&t=44000) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), June 11, 2012
- [Re: Critter 1.6 released!](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=469334&t=44065) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), June 15, 2012
- [Continuation of Critter would be very appreciated](http://www.talkchess.com/forum/viewtopic.php?t=48010) by [Mike Scheidl](/index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](/CCC "CCC"), May 15, 2013

## 2020 ...

- [OpenCritter compiled for Linux with Free Pascal](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75850) by [Roland Chastain](/Roland_Chastain "Roland Chastain"), [CCC](/CCC "CCC"), November 17, 2020

# External Links

## Chess Engine

- [Critter (chess) from Wikipedia](https://en.wikipedia.org/wiki/Critter_%28chess%29)
- [Critter for win32/64, linux and android platforms](http://www.vlasak.biz/critter/) hosted by [Emil Vlasák](/index.php?title=Emil_Vlas%C3%A1k&action=edit&redlink=1 "Emil Vlasák (page does not exist)")
- [SourceForge.net: Critter Chess - Project Web Hosting - Open Source Software](https://sourceforge.net/projects/critterchess/) (Pascal Version)
- [GitHub - rchastain/open-critter: UCI chess engine written in Pascal by Richard Vida](https://github.com/rchastain/open-critter) hosted by [Roland Chastain](/Roland_Chastain "Roland Chastain") [[20]](#cite_note-20)
- [Critter](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Critter&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/15](/CCRL "CCRL")

## Misc

- [Critter (disambiguation page) from Wikipedia](https://en.wikipedia.org/wiki/Critter)
- [Critters (block cellular automaton) from Wikipedia](https://en.wikipedia.org/wiki/Critters_(block_cellular_automaton))
- [Little Critter from Wikipedia](https://en.wikipedia.org/wiki/Mercer_Mayer_bibliography#Little_Critter_related_books)
- ["The Critter" (Chinese pangolin) from Wikipedia](https://en.wikipedia.org/wiki/Chinese_pangolin#%22The_Critter%22)
- [Fearsome critters from Wikipedia](https://en.wikipedia.org/wiki/Fearsome_critters)
- [Critters (film series) from Wikipedia](https://en.wikipedia.org/wiki/Critters_(film_series))
- [Critters (comics) from Wikipedia](https://en.wikipedia.org/wiki/Critters_(comics))

# References

1. [↑](#cite_ref-1) [Agropelter](https://en.wikipedia.org/wiki/Agropelter) from Henry H. Tryon (**1939**). *[Fearsome Critters](http://www.lumberwoods.com/fearsome_critters.htm)*. Illustrated by Margaret R. Tryon, Idlewild Press, Cornwall, NY, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Critter for win32/64, linux and android platforms](http://www.vlasak.biz/critter/) hosted by [Emil Vlasák](/index.php?title=Emil_Vlas%C3%A1k&action=edit&redlink=1 "Emil Vlasák (page does not exist)"), Mac OS version compiled by [Jeremy Bernstein](/Jeremy_Bernstein "Jeremy Bernstein")
3. [↑](#cite_ref-3) [for Pascal fans: Critter](http://www.talkchess.com/forum/viewtopic.php?t=40414) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), September 16, 2011
4. [↑](#cite_ref-4) [SourceForge.net: Critter Chess - Project Web Hosting - Open Source Software](http://critterchess.sourceforge.net/)
5. [↑](#cite_ref-5) [Critter: Pascal vs C](http://www.talkchess.com/forum/viewtopic.php?t=29562) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), August 27, 2009
6. [↑](#cite_ref-6) [Re: World Computer Chess Championship ?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=468701&t=44000) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), June 11, 2012
7. [↑](#cite_ref-7) [Critter (chess) from Wikipedia](https://en.wikipedia.org/wiki/Critter_%28chess%29)
8. [↑](#cite_ref-8) [Interview with Richard Vida](http://www.schach-welt.de/interviews/richard-vida) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), February 20, 2010
9. [↑](#cite_ref-9) [Re: World Computer Chess Championship ?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=468701&t=44000) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), June 11, 2012
10. [↑](#cite_ref-10) [Critter goes SMP (version 0.60 is released)](http://www.talkchess.com/forum/viewtopic.php?t=33774) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), April 13, 2010
11. [↑](#cite_ref-11) [Critter 0.70 is out](http://www.talkchess.com/forum/viewtopic.php?t=34470&) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), May 23, 2010
12. [↑](#cite_ref-12) [Critter 0.80](http://www.talkchess.com/forum/viewtopic.php?t=35565) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), July 24, 2010
13. [↑](#cite_ref-13) [Re: talk about IPP's evaluation](http://www.talkchess.com/forum/viewtopic.php?p=301746#301746) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), November 07, 2009 » [Ippolit](/Ippolit "Ippolit"), [SIMD and SWAR Techniques](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
14. [↑](#cite_ref-14) [My experience with Linux/GCC](http://www.talkchess.com/forum/viewtopic.php?t=38523) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), March 23, 2011
15. [↑](#cite_ref-15) [Chiron 1.1 bug?](http://www.talkchess.com/forum/viewtopic.php?t=41569) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), December 24, 2011
16. [↑](#cite_ref-16) [Leiden Round 7: Rybka vs Critter](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=24906) by Ray, [Rybka Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 13, 2012
17. [↑](#cite_ref-17) [ICT 12 - PGN download](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=39&Itemid=26&lang=en), [CSVN](/CSVN "CSVN")
18. [↑](#cite_ref-18) Part 1 covers [Houdini](/Houdini "Houdini"), [Rybka](/Rybka "Rybka"), [Komodo](/Komodo "Komodo"), [Stockfish](/Stockfish "Stockfish"), Critter, [Naum](/Naum "Naum"), [Chiron](/Chiron "Chiron") and [Spike](/Spike "Spike")
19. [↑](#cite_ref-19) [Difficult position to Critter](http://www.talkchess.com/forum/viewtopic.php?t=38533) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), March 24, 2011
20. [↑](#cite_ref-20) [OpenCritter compiled for Linux with Free Pascal](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75850) by [Roland Chastain](/Roland_Chastain "Roland Chastain"), [CCC](/CCC "CCC"), November 17, 2020

**[Up one level](/Engines "Engines")**