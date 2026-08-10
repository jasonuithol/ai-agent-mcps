# Wb2UCI

Source: https://www.chessprogramming.org/Wb2UCI

**[Home](/Main_Page "Main Page") \* [Software](/Software "Software") \* [Utilities](/Utilities "Utilities") \* Wb2UCI**

**Wb2UCI**, (Wb2Uci, WB2UCI)  
a [protocol](/Protocols "Protocols") adapter by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin") to run [WinBoard Engines](/Category:WinBoard "Category:WinBoard") using the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") under chess [GUIs](/GUI "GUI") supporting [UCI](/UCI "UCI"), such as the [Shredder GUI](/Shredder#GUI "Shredder"). Wb2UCI is a [console application](https://en.wikipedia.org/wiki/Console_application) running under [Windows](/Windows "Windows").
Along with the executable **Wb2Uci.exe**, one must place a **Wb2Uci.eng** textfile into the engine folder [[1]](#cite_note-1) [[2]](#cite_note-2).

# Wb2Uci.eng

The **Wb2Uci.eng** file consists of following mandatory [attribute–value pairs](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair) [[3]](#cite_note-3), and many more optional.

```
;---------------------------
[ENGINE]
Name=Name of engine
Author=Name of engine author
Filename=Wb2Uci.exe

[OPTIONS]
Program=engine.exe
;---------------------------
```

# Engines

- [WinBoard Engines](/Category:WinBoard "Category:WinBoard")

# GUIs

- [UCI compatible GUIs](/UCI#GUI "UCI")

# See also

- [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
- [InBetween](/InBetween "InBetween")
- [PolyGlot](/PolyGlot "PolyGlot")
- [UCI](/UCI "UCI")
- [UCI2WB](/UCI2WB "UCI2WB")
- [WinBoard](/WinBoard "WinBoard")

# Postings

## 2001 ...

- [Help - The King; Chessbase/Fritz GUI](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=33936) by John Hatcher, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), June 10, 2001

**2002**

- [UCI2Wb by Odd Gunnar Malin](https://www.stmintz.com/ccc/index.php?id=215566) by [Matthias Gemuh](/Matthias_Gemuh "Matthias Gemuh"), [CCC](/CCC "CCC"), February 26, 2002 » [UCI2WB](/UCI2WB "UCI2WB")
- [Wb2Uci from Odd Gunnar Malin is working well on Shredder5 GUI](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36342) by Carlos E.A. Drake, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 06, 2002 » [Shredder GUI](/Shredder#GUI "Shredder")
- [The King and Wb2Uci](https://www.stmintz.com/ccc/index.php?id=218644) by Ralph Patriquin, [CCC](/CCC "CCC"), March 19, 2002 » [The King](/The_King "The King")
- [Wb2uci question](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36656) by Jouni, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 02, 2002
- [Re: Fritz protocol](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36819&p=139614#p139734) by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 14, 2002 » [Fritz](/Fritz "Fritz")
- [Wb2Uci](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=39155) by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 23, 2002

**2003**

- [Need help with CM 9000 and WB2UCI](https://www.stmintz.com/ccc/index.php?id=274600) by Ralph Patriquin, [CCC](/CCC "CCC"), January 02, 2003 » [Chessmaster](/Chessmaster "Chessmaster")
- [Wb2Uci and XP](https://www.stmintz.com/ccc/index.php?id=284077) by Chessfun, [CCC](/CCC "CCC"), February 13, 2003
- [Re: Can Gandalf 5 be run under Fritz GUI as an UCI engine w/ Wb2UCI ?](https://www.stmintz.com/ccc/index.php?id=284985) by [Manfred Meiler](/index.php?title=Manfred_Meiler&action=edit&redlink=1 "Manfred Meiler (page does not exist)"), [CCC](/CCC "CCC"), February 18, 2003 » [Gandalf](/Gandalf "Gandalf")
- [List of 31 not-working engines (Fritz-GUI, XP). Any help?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41334) by Surak, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 20, 2003
- [wb2uci,eng w comments](https://www.stmintz.com/ccc/index.php?id=306801) by [Mike Byrne](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), July 16, 2003 » [Rebel](/Rebel "Rebel")
- [Wb2UCI and Problems with ExChess4.03a and GnuChess4.0.8](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43496) by [Arturo Ochoa](/Arturo_Ochoa "Arturo Ochoa"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 24, 2003 » [EXchess](/EXchess "EXchess"), [GNU Chess](/GNU_Chess "GNU Chess")
- [Engine Gaviota + WB2UCI in Fritz7 don,t Work pondering](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43805) by Luis Andraschnik, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 15, 2003 » [Gaviota](/Gaviota "Gaviota")

**2004**

- [Crafty 19.08 SE 2004 released ...](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45863) by [Michael Byrne](/Michael_Byrne "Michael Byrne"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 01, 2004 » [Crafty](/Crafty "Crafty")
- [The King's Wb2UCI file](https://www.stmintz.com/ccc/index.php?id=341498) by Darren Rushton, [CCC](/CCC "CCC"), January 10, 2004 » [The King](/The_King "The King")
- [GLC and others when using wb2uci](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48455) by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 03, 2004 » [Green Light Chess](/Green_Light_Chess "Green Light Chess")

## 2005 ...

- [To Odd-Gunnar Malin: Bug in WB2UCI-adaptor](https://www.stmintz.com/ccc/index.php?id=407137) by [Franz Huber](/index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)"), [CCC](/CCC "CCC"), January 23, 2005
- [Re: New Wb2Uci 1.3 B21](https://www.stmintz.com/ccc/index.php?id=431484) by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin"), [CCC](/CCC "CCC"), June 16, 2005
- [Where is the latest wb2uci.exe file available from?](http://www.talkchess.com/forum/viewtopic.php?t=13045) by [Graham Banks](/Graham_Banks "Graham Banks"), [CCC](/CCC "CCC"), April 12, 2007
- [UCI protocol in winboard](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=50429) by [Engin Üstün](/Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 24, 2009 » [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [UCI](/UCI "UCI"), [WinBoard](/WinBoard "WinBoard")

## 2010 ...

- [n/s speed of search through Wb2Uci - need some clarification](http://www.talkchess.com/forum/viewtopic.php?t=32256) by [Martin Thoresen](/Martin_Thoresen "Martin Thoresen"), [CCC](/CCC "CCC"), February 01, 2010
- [Need help reading Arena debug and wb2uci logfiles](http://www.talkchess.com/forum/viewtopic.php?t=39426) by [Adam Hair](/Adam_Hair "Adam Hair"), [CCC](/CCC "CCC"), June 19, 2011
- [wb2uci adaptor,where can I get it? please!](http://www.talkchess.com/forum/viewtopic.php?t=47232) by markchessman, [CCC](/CCC "CCC"), February 15, 2013
- [WB2UCI for Java executable chess engines too?](http://www.talkchess.com/forum/viewtopic.php?t=51276) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](/CCC "CCC"), February 14, 2014
- [WB2UCI.EXE adapter](http://www.talkchess.com/forum/viewtopic.php?t=52914) by Jim Logan, [CCC](/CCC "CCC"), July 08, 2014

## 2015 ...

- [wb2uci adapter - different results with different versions](http://www.talkchess.com/forum/viewtopic.php?t=58982) by Wilhelm Hudetz, [CCC](/CCC "CCC"), January 20, 2016
- [WB2UCI](http://www.talkchess.com/forum/viewtopic.php?t=60699) by [Brendan J. Norman](/index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](/CCC "CCC"), July 05, 2016

# External Links

- [Winboard as UCI engine](http://web.archive.org/web/20120515104014/http://home.online.no:80/%7Emalin/sjakk/Wb2Uci/) by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin"), hosted by the [WaybackMachine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Adam's Computer Chess Pages: Computer Chess Utility Programs - WB2UCI](http://adamsccpages.blogspot.de/p/computer-chess-utility-programs.html#h) by [Adam Hair](/Adam_Hair "Adam Hair")
- [Le Système du Suisse](http://americanfoot.free.fr/echecs/suisse/fichiers.htm) has wbconf07.zip with approximately 300 Wb2Uci.eng files
- [Crafty Chess Interface / Wiki / wb2uci with multiple engines](https://sourceforge.net/p/craftychessinterface/wiki/wb2uci%20with%20multiple%20engines/)

# References

1. [↑](#cite_ref-1)  [Adam's Computer Chess Pages: Computer Chess Utility Programs - WB2UCI](http://adamsccpages.blogspot.de/p/computer-chess-utility-programs.html#h) by [Adam Hair](/Adam_Hair "Adam Hair")
2. [↑](#cite_ref-2) [Le Système du Suisse](http://americanfoot.free.fr/echecs/suisse/fichiers.htm) has wbconf07.zip with approximately 300 Wb2Uci.eng files
3. [↑](#cite_ref-3) [Winboard as UCI engine](http://web.archive.org/web/20120515104014/http://home.online.no:80/%7Emalin/sjakk/Wb2Uci/) by [Odd Gunnar Malin](/Odd_Gunnar_Malin "Odd Gunnar Malin"), hosted by the [WaybackMachine](https://en.wikipedia.org/wiki/Wayback_Machine)

**[Up one Level](/Utilities "Utilities")**