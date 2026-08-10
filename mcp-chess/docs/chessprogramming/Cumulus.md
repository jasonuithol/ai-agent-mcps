# Cumulus

Source: https://www.chessprogramming.org/Cumulus

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Cumulus**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Anvil_of_Cumulonimbus_and_Cu_con.JPG/330px-Anvil_of_Cumulonimbus_and_Cu_con.JPG)](/File:Anvil_of_Cumulonimbus_and_Cu_con.JPG)

[Cumulonimbus](https://en.wikipedia.org/wiki/Cumulonimbus_cloud) and [Cumulus clouds](https://en.wikipedia.org/wiki/Cumulus_mediocris) [[1]](#cite_note-1)

**Cumulus**,  
the second chess program by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") and [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), written in [C](/C "C") with a few [8086](/8086 "8086") [Assembly](/Assembly "Assembly") snippets [[2]](#cite_note-2). Cumulus played the [WMCCC 1990](/WMCCC_1990 "WMCCC 1990"), [WMCCC 1991](/WMCCC_1991 "WMCCC 1991"), and [WCCC 1992](/WCCC_1992 "WCCC 1992") [[3]](#cite_note-3), the [Aegon 1993](/Aegon_1993 "Aegon 1993") and various [Aubervilliers Rapid Open](/Aubervilliers_Rapid_Open "Aubervilliers Rapid Open") - the versions since [WCCC 1992](/WCCC_1992 "WCCC 1992") already the [Écume](/%C3%89cume "Écume") codebase, completely written in Assembly language [[4]](#cite_note-4).

# Description

from [Don Beal's](/Don_Beal "Don Beal") [WMCCC 1991](/WMCCC_1991 "WMCCC 1991") report [[5]](#cite_note-5) :

```
Written by Jean-Christophe Weill, in association with Marc-François Baudot of Échec, this is a new program, only in development for 7 months, although it made its first appearance at the 1990 World Micro. Its evaluation function has some overlap with Échec, although Cumulus add hung-piece considerations, king safety and uses different definition of mobility. Its selectivity is driven by swap-off values and certain mate threats. Checks, promotion threats, and re-captures are extended.
```

# Selected Games

[WCCC 1992](/WCCC_1992 "WCCC 1992"), round 4, Cumulus 2 - [Kallisto](/Kallisto "Kallisto") [[6]](#cite_note-6)

```
[Event "WCCC 1992"]
[Site "Madrid, Spain"]
[Date "1992.11.26"]
[Round "4"]
[White "Cumulus 2"]
[Black "Kallisto"]
[Result "1-0"]

1.d4 Nf6 2.Nf3 e6 3.e3 b6 4.Nbd2 Bb7 5.Bd3 Nc6 6.c3 a5 7.O-O Ba6 8.Bxa6 Rxa6 
9.e4 Be7 10.e5 Nh5 11.Ne4 a4 12.Nfg5 g6 13.Qf3 O-O 14.Be3 Ra5 15.g4 Ng7 16.Qh3 
h5 17.b4 axb3 18.axb3 Qa8 19.Rxa5 Qxa5 20.Nf6+ Bxf6 21.exf6 Ne8 22.gxh5 gxh5 
23.Qg3 Kh8 24.Qf3 Kg8 25.Kh1 Qd5 26.Ne4 Qf5 27.Qxf5 exf5 28.Bh6 fxe4 29.Rg1+ 
Ng7 30.Rxg7+ Kh8 31.h4 d6 32.b4 b5 33.Kh2 Na7 34.Rg5 Re8 35.Bg7+ 1-0
```

# See also

- [Échec](/%C3%89chec "Échec")
- [Écume](/%C3%89cume "Écume")

# External Links

## Chess Engine

- [Cumulus' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=225)
- [Chess](http://query.nytimes.com/gst/fullpage.html?res=9D0CE5DB103BF936A15755C0A967958260) by [Robert Byrne](https://en.wikipedia.org/wiki/Robert_Byrne), [New York Times](https://en.wikipedia.org/wiki/The_New_York_Times), June 25, 1991 - on [Chess Machine](/ChessMachine "ChessMachine") [Gideon](/Gideon "Gideon") versus Cumulus, [WMCCC 1991](/WMCCC_1991 "WMCCC 1991") [[7]](#cite_note-7)
- [A Short Story of JCW's Computer Chess Program](http://recherche.enac.fr/~weill/chess.html) by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill")

## Misc

- [cumulus - Wiktionary](https://en.wiktionary.org/wiki/cumulus)
- [Cumulus (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Cumulus_%28disambiguation%29)
- [Cumulus cloud from Wikipedia](https://en.wikipedia.org/wiki/Cumulus_cloud)
- [Terje Rypdal](/Category:Terje_Rypdal "Category:Terje Rypdal"), [Trilok Gurtu](/Category:Trilok_Gurtu "Category:Trilok Gurtu"), [Miroslav Vitouš](/Category:Miroslav_Vitou%C5%A1 "Category:Miroslav Vitouš"), Clouds in the Mountain, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Anvil](https://en.wikipedia.org/wiki/Anvil) of a large [Cumulonimbus](https://en.wikipedia.org/wiki/Cumulonimbus_cloud), [Cumulus congestus](https://en.wikipedia.org/wiki/Cumulus_congestus_cloud) at the bottom, [Photo](https://commons.wikimedia.org/wiki/File:Anvil_of_Cumulonimbus_and_Cu_con.JPG) by [Simon Eugster](https://commons.wikimedia.org/wiki/User:LivingShadow), April 7, 2005, [Cumulus cloud from Wikipedia](https://en.wikipedia.org/wiki/Cumulus_cloud)
2. [↑](#cite_ref-2) [A Short Story of JCW's Computer Chess Program](http://recherche.enac.fr/~weill/chess.html) by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill")
3. [↑](#cite_ref-3)  [Cumulus' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=225)
4. [↑](#cite_ref-4) [A Short Story of JCW's Computer Chess Program](http://recherche.enac.fr/~weill/chess.html) by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill")
5. [↑](#cite_ref-5) [Don Beal](/Don_Beal "Don Beal") (**1991**). *Report on the 11th World Microcomputer Chess Championship*. [ICCA Journal, Vol. 14, No. 2](/ICGA_Journal#14_2 "ICGA Journal")
6. [↑](#cite_ref-6) [Madrid 1992 - Chess - Round 4 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=58&round=4&id=3)
7. [↑](#cite_ref-7) [Vancouver 1991 - Chess - Round 2 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=59&round=2&id=1)

**[Up one Level](/Engines "Engines")**