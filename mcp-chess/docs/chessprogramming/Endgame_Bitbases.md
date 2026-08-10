# Endgame Bitbases

Source: https://www.chessprogramming.org/Endgame_Bitbases

**[Home](/Main_Page "Main Page") \* [Knowledge](/Knowledge "Knowledge") \* [Endgame Tablebases](/Endgame_Tablebases "Endgame Tablebases") \* Bitbases**

**Endgame Bitbases**,  
are compact endgame tablebases with game theoretical values of one or two bits per position stored. They are sufficient for various material configurations to reside inside [RAM](/Memory#RAM "Memory") for short probing access time, intended to use deep inside the [search](/Search "Search"). The boolean or four valued ranges are either {*won*, *not\_won*} or {*won*, *draw*, *loss*, *invalid*}. While WDL information is sufficient to guide the search into won positions, it lacks any sense of progress in won positions. Therefor, programs either probe full tablebases at the [root](/Root "Root") to reveal the number of moves until conversion or mate, or combine WDL-scores with heuristic evaluation [scores](/Score "Score"), considering [material](/Material "Material"), ply-distance to the root, pawn closeness to promotion, [distance](/Distance "Distance") of pieces to opponent king, etc.. Endgame Bitbases were described in 1999 by [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") in *Knowledgeable Encoding and Querying of Endgame Databases*, as applied with 4-men in [DarkThought](/DarkThought "DarkThought") [[1]](#cite_note-1).

# Bitbase Implementations

- [Gaviota Tablebases](/Gaviota_Tablebases "Gaviota Tablebases") [[2]](#cite_note-2)
- [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases")
- [Shredderbases](/Shredder#Bases "Shredder")
- [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")

# See also

- [Interior Node Recognizer](/Interior_Node_Recognizer "Interior Node Recognizer")
- [KPK](/KPK "KPK")
- [Retrograde Analysis](/Retrograde_Analysis "Retrograde Analysis")

# Publications

- [Ken Thompson](/Ken_Thompson "Ken Thompson") (**1996**). *6-Piece Endgames*. [ICCA Journal, Vol. 19, No. 4](/ICGA_Journal#19_4 "ICGA Journal")
- [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") (**1999**). *Knowledgeable Encoding and Querying of Endgame Databases.* [ICCA Journal, Vol. 22, No. 2](/ICGA_Journal#22_2 "ICGA Journal"), [ps](http://people.csail.mit.edu/heinz/ps/know_edb.ps.gz)
- [Ren Wu](/Ren_Wu "Ren Wu"), [Don Beal](/Don_Beal "Don Beal") (**2001**). *Fast, Memory-efficient Retrograde Algorithms*. [ICGA Journal, Vol. 24, No. 3](/ICGA_Journal#24_3 "ICGA Journal") [[3]](#cite_note-3)

# Forum Posts

## 2000

- [EGTB: Better algorithm](https://www.stmintz.com/ccc/index.php?id=162252) by [Urban Koistinen](/Urban_Koistinen "Urban Koistinen"), [CCC](/CCC "CCC"), April 07, 2001 [[4]](#cite_note-4)
- [Generating egtbs ICGAJ](https://www.stmintz.com/ccc/index.php?id=200335) by [Tony Werten](/Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](/CCC "CCC"), December 04, 2001 [[5]](#cite_note-5)

:   [Wu/Beal predates Koistinen](https://www.stmintz.com/ccc/index.php?id=200376) by [Guy Haworth](/Guy_Haworth "Guy Haworth"), [CCC](/CCC "CCC"), December 04, 2001

- [EGTB generation with 1 bit per position?](https://www.stmintz.com/ccc/index.php?id=290629) by [Martin Fierz](/Martin_Fierz "Martin Fierz"), [CCC](/CCC "CCC"), March 25, 2003
- [Need help: End Game Table Base and BitBase](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=47383) by [Josué Forte](/Josu%C3%A9_Forte "Josué Forte"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 24, 2004
- [Any programs besides Yace and Patzer that can use bitbase files](https://www.stmintz.com/ccc/index.php?id=370997) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), June 17, 2004 » [Patzer](/Patzer "Patzer"), [Yace](/Yace "Yace")

## 2005

- [Bitbases - yace, scorpio, gambitfruit](https://www.stmintz.com/ccc/index.php?id=467250) by [Bernhard Bauer](/index.php?title=Bernhard_Bauer&action=edit&redlink=1 "Bernhard Bauer (page does not exist)"), [CCC](/CCC "CCC"), December 06, 2005
- [Open Source bitbase program](http://www.talkchess.com/forum/viewtopic.php?t=12987) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [CCC](/CCC "CCC"), April 09, 2007
- [KQKB and KQKN heuristic for bitbases?!](http://www.talkchess.com/forum/viewtopic.php?t=13511) by [Jesper Nielsen](/index.php?title=Jesper_Nielsen&action=edit&redlink=1 "Jesper Nielsen (page does not exist)"), [CCC](/CCC "CCC"), May 01, 2007
- [bitbases and Linux](http://www.talkchess.com/forum/viewtopic.php?t=14687) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), June 26, 2007
- [Question about bitbases](http://www.talkchess.com/forum/viewtopic.php?t=19361) by [Thomas Gaksch](/Thomas_Gaksch "Thomas Gaksch"), [CCC](/CCC "CCC"), February 02, 2008
- [How to generate a "simple" bitbase?](http://www.talkchess.com/forum/viewtopic.php?t=19575) by [Alessandro Scotti](/Alessandro_Scotti "Alessandro Scotti"), [CCC](/CCC "CCC"), February 12, 2008
- [How much are bitbases worth?](http://www.talkchess.com/forum/viewtopic.php?t=21301) by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [CCC](/CCC "CCC"), May 22, 2008
- [Bitbases](http://www.talkchess.com/forum/viewtopic.php?t=27722) by [Frank Phillips](/Frank_Phillips "Frank Phillips"), [CCC](/CCC "CCC"), May 03, 2009
- [Endgame bitbase / tablebase compromise?](http://www.talkchess.com/forum/viewtopic.php?t=28944) by clgd, [CCC](/CCC "CCC"), July 13, 2009
- [Bitbase indexing and en passant](http://www.talkchess.com/forum/viewtopic.php?t=29390) by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [CCC](/CCC "CCC"), August 14, 2009

## 2010

- [Gaviota TBs [0.1.6.1](http://www.talkchess.com/forum/viewtopic.php?t=32835), bitbase-like interface] by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), February 22, 2010
- [Gaviota TBs Probing Code (v0.2) UPDATE, Bitbases on the fly](http://www.talkchess.com/forum/viewtopic.php?t=33382) by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), March 20, 2010
- [hard-wired bitbases](http://www.talkchess.com/forum/viewtopic.php?t=33781) by Ben Stoker, [CCC](/CCC "CCC"), April 13, 2010
- [Stockfish bitbase](http://www.talkchess.com/forum/viewtopic.php?t=34634) by [kongsian](/Chua_Kong_Sian "Chua Kong Sian"), [CCC](/CCC "CCC"), June 01, 2010
- [Search with bitbase](http://www.talkchess.com/forum/viewtopic.php?t=45009) by [Pham Hong Nguyen](/Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](/CCC "CCC"), September 05, 2012
- [KPK bitbase](http://www.talkchess.com/forum/viewtopic.php?t=46893) by [Maarten Bults](/index.php?title=Maarten_Bults&action=edit&redlink=1 "Maarten Bults (page does not exist)"), [CCC](/CCC "CCC"), January 16, 2013 » [KPK](/KPK "KPK")
- [What happens using egbb](http://www.talkchess.com/forum/viewtopic.php?t=49684) by [Kai Laskos](/Kai_Laskos "Kai Laskos"), [CCC](/CCC "CCC"), October 12, 2013
- [Scorpio 6men EGBB Now available](http://www.talkchess.com/forum/viewtopic.php?t=50894) by [Joshua Shriver](/index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](/CCC "CCC"), January 14, 2014 » [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases")

## 2015 ...

- [Yet another KPK endgame table generator: pfkpk](http://www.talkchess.com/forum/viewtopic.php?t=57517) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](/CCC "CCC"), September 05, 2015 » [KPK](/KPK "KPK") [[6]](#cite_note-6)
- [Eucalyptus - KPK Bitbases Generator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70815) by [Toni Helminen](/Toni_Helminen "Toni Helminen"), [CCC](/CCC "CCC"), May 24, 2019
- [The Poor Man's KP Bitbase](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70942) by [Dennis Sceviour](/Dennis_Sceviour "Dennis Sceviour"), [CCC](/CCC "CCC"), June 07, 2019

## 2020 ...

- [EGBB (endgame bitbases) questions ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75803) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), November 15, 2020 » [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases")

# External Links

- [Endgame tablebase | Computer chess - Wikipedia](https://en.wikipedia.org/wiki/Endgame_tablebase#Computer_chess)
- [Computing endgames with few men](http://www.abc.se/~m10051/eg.txt) by [Urban Koistinen](/Urban_Koistinen "Urban Koistinen")
- [dshawul/Scorpio · GitHub](https://github.com/dshawul/Scorpio) includes Six men egbb code » [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases") [[7]](#cite_note-7)
- [kervinck/pfkpk · GitHub](https://github.com/kervinck/pfkpk) » [KPK](/KPK "KPK") Bitbase by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck") [[8]](#cite_note-8)

# References

1. [↑](#cite_ref-1) [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") (**1999**). *Knowledgeable Encoding and Querying of Endgame Databases.* [ICCA Journal, Vol. 22, No. 2](/ICGA_Journal#22_2 "ICGA Journal"), [ps](http://people.csail.mit.edu/heinz/ps/know_edb.ps.gz)
2. [↑](#cite_ref-2) [Gaviota TBs [0.1.6.1](http://www.talkchess.com/forum/viewtopic.php?t=32835), bitbase-like interface] by [Miguel A. Ballicora](/Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](/CCC "CCC"), February 22, 2010
3. [↑](#cite_ref-3) [Generating egtbs ICGAJ](https://www.stmintz.com/ccc/index.php?id=200335) by [Tony Werten](/Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](/CCC "CCC"), December 04, 2001, with reference to [Computing endgames with few men](http://www.abc.se/~m10051/eg.txt) by [Urban Koistinen](/Urban_Koistinen "Urban Koistinen")
4. [↑](#cite_ref-4) [Computing endgames with few men](http://www.abc.se/~m10051/eg.txt) by [Urban Koistinen](/Urban_Koistinen "Urban Koistinen")
5. [↑](#cite_ref-5) [Ren Wu](/Ren_Wu "Ren Wu"), [Don Beal](/Don_Beal "Don Beal") (**2001**). *Fast, Memory-efficient Retrograde Algorithms*. [ICGA Journal, Vol. 24, No. 3](/ICGA_Journal#24_3 "ICGA Journal")
6. [↑](#cite_ref-6) [kervinck/pfkpk · GitHub](https://github.com/kervinck/pfkpk)
7. [↑](#cite_ref-7) [Scorpio 6men EGBB Now available](http://www.talkchess.com/forum/viewtopic.php?t=50894) by [Joshua Shriver](/index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](/CCC "CCC"), January 14, 2014
8. [↑](#cite_ref-8)  [Yet another KPK endgame table generator: pfkpk](http://www.talkchess.com/forum/viewtopic.php?t=57517) by [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](/CCC "CCC"), September 05, 2015

**[Up one level](/Endgame_Tablebases "Endgame Tablebases")**