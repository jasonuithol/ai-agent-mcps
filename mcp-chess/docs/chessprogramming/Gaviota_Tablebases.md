# Gaviota Tablebases

Source: https://www.chessprogramming.org/Gaviota_Tablebases

**[Home](/Main_Page "Main Page") \* [Knowledge](/Knowledge "Knowledge") \* [Endgame Tablebases](/Endgame_Tablebases "Endgame Tablebases") \* Gaviota Tablebases**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Dreizehenmoewen.jpg/330px-Dreizehenmoewen.jpg)](/File:Dreizehenmoewen.jpg)

Gaviota base on Runde [[1]](#cite_note-1)

**Gaviota Tablebases**,  
a [depth to mate](/Endgame_Tablebases#DTM "Endgame Tablebases") endgame tablebase by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), initially developed for his [Gaviota](/Gaviota "Gaviota") engine [[2]](#cite_note-2) . The probing code, written in [C](/C "C"), is open source, along with the tablebase files licensed under the [MIT license](/Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology"). Gaviota Tablebases [cache system](/Memory "Memory") works like [bitbases](/Endgame_Bitbases "Endgame Bitbases") on the fly, allowing to probe WDL information with fourfold increased cache efficiency. Further, the [thread safe](/Thread "Thread") probing [API](https://en.wikipedia.org/wiki/Application_programming_interface) allows soft probes to get information from the cache without reading the [hard disk](https://en.wikipedia.org/wiki/Hard_disk_drive) - intended to use everywhere inside the [search](/Search "Search"), and the classical *hard* probe, suited to use with some distance to the horizon. The up to 5-men tablebase files can be generated [[3]](#cite_note-3) and checked [[4]](#cite_note-4) using the free command line program *tbgen*, performing several compression schemes using *tbcp* [[5]](#cite_note-5), yielding in 5-men sizes below 7 GB.

# See also

- [Bitbases](/Endgame_Bitbases "Endgame Bitbases")
- [Edwards' Tablebases](/Edwards%27_Tablebases "Edwards' Tablebases")
- [Gaviota](/Gaviota "Gaviota")
- [Felicity Tablebases](/Felicity_Tablebases "Felicity Tablebases")
- [Lomonosov Tablebases](/Lomonosov_Tablebases "Lomonosov Tablebases")
- [Nalimov Tablebases](/Nalimov_Tablebases "Nalimov Tablebases")
- [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases")
- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")
- [Thompson's Databases](/Thompson%27s_Databases "Thompson's Databases")

# Forum Posts

## 2008

- [Gaviota's Endgame Tablebases](http://www.talkchess.com/forum/viewtopic.php?t=25311) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), December 07, 2008

## 2009

- [Gaviota 0.74 released](http://www.talkchess.com/forum/viewtopic.php?t=30264) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), October 21, 2009
- [Gaviota 0.74.6 (special for EGTB builders)](http://www.talkchess.com/forum/viewtopic.php?t=30416) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), October 31, 2009
- [Gaviota's EGTBs are only 6.5 Gb now](http://www.talkchess.com/forum/viewtopic.php?t=30884) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), December 01, 2009
- [Gaviota EGTBs, interface proposal for programmers](http://www.talkchess.com/forum/viewtopic.php?t=31065) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), December 13, 2009
- [Gaviota Tablebases vs. Nalimov](http://www.talkchess.com/forum/viewtopic.php?t=31240) by Greg Simpson, [CCC](/CCC "CCC"), December 24, 2009
- [Gaviota TBs, compression schemes](http://www.talkchess.com/forum/viewtopic.php?t=31354) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), December 30, 2009

## 2010 ...

- [Gaviota TBs, compressor available (win32 for now)](http://www.talkchess.com/forum/viewtopic.php?t=31470) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), January 04, 2010
- [Gaviota tablebases, probing code license](http://www.talkchess.com/forum/viewtopic.php?t=32508) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), February 10, 2010
- [Gaviota tablebases, Probing Code Release (Finally)](http://www.talkchess.com/forum/viewtopic.php?t=32527) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), February 10, 2010
- [Gaviota Tablebases Probing Code (v0.1.2) UPDATE](http://www.talkchess.com/forum/viewtopic.php?t=32626) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), February 15, 2010
- [Gaviota TBs [0.1.6.1](http://www.talkchess.com/forum/viewtopic.php?t=32835), bitbase-like interface] by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), February 22, 2010
- [Gaviota TBs Probing Code (v0.2) UPDATE, Bitbases on the fly](http://www.talkchess.com/forum/viewtopic.php?t=33382) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), March 20, 2010
- [Gaviota Tablebases and Delphi](http://www.talkchess.com/forum/viewtopic.php?t=33516) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), March 28, 2010
- [libgaviota?](http://www.talkchess.com/forum/viewtopic.php?t=33742) by [Michel Van den Bergh](/Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](/CCC "CCC"), April 11, 2010
- [Gaviota tablebases probing code (v0.2.2) small update](http://www.talkchess.com/forum/viewtopic.php?t=33902) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), April 21, 2010
- [Gaviota tablebases probing code (v0.3) UPDATE](http://www.talkchess.com/forum/viewtopic.php?t=34707) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), June 04, 2010
- [About Gaviota Tablebases License](http://www.talkchess.com/forum/viewtopic.php?t=35167) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), June 26, 2010
- [Chessbase GUI & Critter + Gaviota tablebases](http://www.talkchess.com/forum/viewtopic.php?t=36874) by [Richard Vida](/Richard_Vida "Richard Vida"), [CCC](/CCC "CCC"), December 01, 2010 » [Critter](/Critter "Critter")
- [Gaviota EGTB in Houdini 1.5 + contacting Eugene Nalimov](http://www.talkchess.com/forum/viewtopic.php?t=36886) by [Robert Houdart](/Robert_Houdart "Robert Houdart"), [CCC](/CCC "CCC"), December 01, 2010
- [Gaviota EGTBs: How long to generate 5-men TBs?](http://www.talkchess.com/forum/viewtopic.php?t=36953) by Joerg Oster, [CCC](/CCC "CCC"), December 05, 2010
- [Gaviota tablebases, probing code v0.3.2 (UPDATE)](http://www.talkchess.com/forum/viewtopic.php?t=37335) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), December 28, 2010

**2011**

- [For Miguel B: Gaviota tb\_availability() sometimes incorrect](http://www.talkchess.com/forum/viewtopic.php?t=37619) by [Robert Houdart](/Robert_Houdart "Robert Houdart"), [CCC](/CCC "CCC"), January 14, 2011 » [Houdini](/Houdini "Houdini")
- [Houdini and Gaviota Tablebases](http://www.talkchess.com/forum/viewtopic.php?t=37652) by Edwin Meiners, [CCC](/CCC "CCC"), January 16, 2011
- [Gaviota tablebases, probing code v4 (UPDATE)](http://www.talkchess.com/forum/viewtopic.php?t=38372) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), March 11, 2011
- [Gaviota table bases in Scid?](http://www.talkchess.com/forum/viewtopic.php?t=40217) by [Michel Van den Bergh](/Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](/CCC "CCC"), August 30, 2011 » [SCID](/SCID "SCID")

**2012**

- [Gaviota access in Critter 1.4](http://www.talkchess.com/forum/viewtopic.php?t=41950) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), January 12, 2012 » [Critter](/Critter "Critter")
- [Gaviota tablebases - how many files? - how big?](http://www.talkchess.com/forum/viewtopic.php?t=44208) by [Marek Soszynski](/index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), [CCC](/CCC "CCC"), June 27, 2012

**2013**

- [6-men Gaviota (Question to Miguel)](http://www.talkchess.com/forum/viewtopic.php?t=50652) by [Harun Taner](/Harun_Taner "Harun Taner"), [CCC](/CCC "CCC"), December 27, 2013

**2014**

- [En passant problem in gaviota tablebases](http://www.talkchess.com/forum/viewtopic.php?t=52836) by [Peter Österlund](/Peter_%C3%96sterlund "Peter Österlund"), [CCC](/CCC "CCC"), July 02, 2014 » [En passant](/En_passant "En passant")

## 2015 ...

- [How texel probes endgame tablebases](http://www.talkchess.com/forum/viewtopic.php?t=60833) by [Peter Österlund](/Peter_%C3%96sterlund "Peter Österlund"), [CCC](/CCC "CCC"), July 16, 2016 » [Syzygy Bases](/Syzygy_Bases "Syzygy Bases"), [Texel](/Texel "Texel")
- [Probing tablebases in python-chess](http://www.talkchess.com/forum/viewtopic.php?t=63504) by [Robert Pope](/Robert_Pope "Robert Pope"), [CCC](/CCC "CCC"), March 20, 2017 » [python-chess](/Python-chess "Python-chess")
- [EGTB probe in search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64767) by [Erin Dame](/Erin_Dame "Erin Dame"), [CCC](/CCC "CCC"), July 30, 2017
- [Gaviota TB download link](http://www.talkchess.com/forum/viewtopic.php?t=67189) by [Sven Schüle](/Sven_Sch%C3%BCle "Sven Schüle"), [CCC](/CCC "CCC"), April 21, 2018

# External Links

- [Endgame Tablebases - gaviota chess engine](https://sites.google.com/site/gaviotachessengine/Home/endgame-tablebases-1)
- [Download - gaviota chess engine - Gaviota Tablebases probing code, examples and APIs. v0.4](https://sites.google.com/site/gaviotachessengine/download)
- [michiguel/Gaviota-Tablebases · GitHub](https://github.com/michiguel/Gaviota-Tablebases)
- [Gaviota 3-4-5 EGTB files Compressed](http://olympuschess.com/egtb/gaviota/) hosted by [Joshua Shriver](/index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)")
- [Interview with Miguel Ballicora](http://www.playwitharena.com/?Interviews:Interview_with_Miguel_Ballicora%26nbsp%3B) by [Michael Diosi](/index.php?title=Michael_Diosi&action=edit&redlink=1 "Michael Diosi (page does not exist)"), [Arena](/Arena "Arena"), December 2010
- [OICS Chess and EGTB Tracker Statistics](http://oics.olympuschess.com/tracker/index.php) by [Joshua Shriver](/index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)") [[6]](#cite_note-6)

# References

1. [↑](#cite_ref-1) [Black-legged Kittiwakes](https://en.wikipedia.org/wiki/Black-legged_kittiwake) at [Runde](https://en.wikipedia.org/wiki/Runde), [Herøy](https://en.wikipedia.org/wiki/Her%C3%B8y,_M%C3%B8re_og_Romsdal), [Møre og Romsdal](https://en.wikipedia.org/wiki/M%C3%B8re_og_Romsdal), [Norway](https://en.wikipedia.org/wiki/Norway), [Photo](https://commons.wikimedia.org/wiki/File:Dreizehenmoewen.jpg) by [T.Müller](https://commons.wikimedia.org/wiki/User:Islandmen), July 2006
2. [↑](#cite_ref-2) [Gaviota's Endgame Tablebases](http://www.talkchess.com/forum/viewtopic.php?t=25311) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), December 07, 2008
3. [↑](#cite_ref-3) [Generation from Console - gaviota chess engine](https://sites.google.com/site/gaviotachessengine/Home/endgame-tablebases-1/gtb-generation)
4. [↑](#cite_ref-4) [Checking Files After Generation - gaviota chess engine](https://sites.google.com/site/gaviotachessengine/Home/endgame-tablebases-1/gtb-checking)
5. [↑](#cite_ref-5) [Compressing Tablebases - gaviota chess engine](https://sites.google.com/site/gaviotachessengine/Home/endgame-tablebases-1/gtb-compression)
6. [↑](#cite_ref-6) [BitTorrent from Wikipedia](https://en.wikipedia.org/wiki/BitTorrent)

**[Up one level](/Endgame_Tablebases "Endgame Tablebases")**