# Myopic

Source: https://www.chessprogramming.org/Myopic

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Myopic**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Myopia_Diagram.jpg/330px-Myopia_Diagram.jpg)](/File:Myopia_Diagram.jpg)

Myopia [[1]](#cite_note-1)

**Myopic**,  
a simple [open source chess program](/Category:Open_Source "Category:Open Source") for small systems by [Steven Edwards](/Steven_Edwards "Steven Edwards"), written in [C++](/Cpp "Cpp") and released under the [Creative Commons license](https://en.wikipedia.org/wiki/Creative_Commons_license). Myopic is suited for the [Arduino](/Arduino "Arduino") **Mega** [[2]](#cite_note-2) with the optional addition of a [SparkFun](https://en.wikipedia.org/wiki/SparkFun_Electronics) 8x8 [RGB LED](https://en.wikipedia.org/wiki/Light-emitting_diode#RGB_systems) backpack [[3]](#cite_note-3) as move indicator output device. Otherwise, all I/O is gated through a single pair of routines that currently use the default [serial](https://en.wikipedia.org/wiki/Serial_communication) I/O pins [[4]](#cite_note-4) .

# Description

The board is represented by a [vector of 64](/8x8_Board "8x8 Board") chessmen including vacant square chessmen. Search is plain [alpha-beta](/Alpha-Beta "Alpha-Beta") inside the [iterative deepening](/Iterative_Deepening "Iterative Deepening") loop with [leaf evaluation](/Evaluation "Evaluation") considering [material balance](/Material "Material"), [pawn placement](/Pawn_Structure "Pawn Structure"), [pinned pieces](/Pin "Pin") and [piece mobility](/Mobility "Mobility"), and scaled [king center distance](/Center_Distance "Center Distance") as bonus in the [middlegame](/Middlegame "Middlegame") and penalty in the [endgame](/Endgame "Endgame").

# Download

[File:Myopic.tar](/File:Myopic.tar "File:Myopic.tar")

# See also

- [Arduino](/Arduino "Arduino")
- [CookieCat](/CookieCat "CookieCat")

# Forum Posts

- [Chess for the Arduino](http://forum.arduino.cc/index.php?topic=8330.0) by [chessplayer](/Steven_Edwards "Steven Edwards"), [Arduino Forum](http://forum.arduino.cc/), December 06, 2009
- [Myopic, a new Creative Commons chess program](http://www.talkchess.com/forum/viewtopic.php?t=34445) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), May 22, 2010
- [Re: SAN Move Disambiguation -- looking for test positition](http://www.talkchess.com/forum/viewtopic.php?t=33764&start=3) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), July 11, 2010 » [SAN](/Algebraic_Chess_Notation#SAN "Algebraic Chess Notation")
- [For a limited time, two sources](http://www.talkchess.com/forum/viewtopic.php?t=46964) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), January 22, 2013 » [CookieCat](/CookieCat "CookieCat")

# External Links

- [myopic - Wiktionary](https://en.wiktionary.org/wiki/myopic)
- [Myopia (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Myopia_%28disambiguation%29)
- [Myopia from Wikipedia](https://en.wikipedia.org/wiki/Myopia)
- [Agnes Obel](/Category:Agnes_Obel "Category:Agnes Obel") - [Myopia](https://en.wikipedia.org/wiki/Agnes_Obel#Myopia) (2020), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Diagram of Myopia](https://commons.wikimedia.org/wiki/File:Myopia_Diagram.jpg) in the [human eye](https://en.wikipedia.org/wiki/Human_eye), 2005, [National Eye Institute](https://en.wikipedia.org/wiki/National_Eye_Institute), [Myopia from Wikipedia](https://en.wikipedia.org/wiki/Myopia), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Myopic, a new Creative Commons chess program](http://www.talkchess.com/forum/viewtopic.php?t=34445) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), May 22, 2010
3. [↑](#cite_ref-3) [LED Matrix - Tri Color - Large - COM-00683 - SparkFun Electronics](https://www.sparkfun.com/products/683)
4. [↑](#cite_ref-4) [Chess for the Arduino](http://forum.arduino.cc/index.php?topic=8330.0) by [chessplayer](/Steven_Edwards "Steven Edwards"), [Arduino Forum](http://forum.arduino.cc/), December 06, 2009

**[Up one level](/Engines "Engines")**