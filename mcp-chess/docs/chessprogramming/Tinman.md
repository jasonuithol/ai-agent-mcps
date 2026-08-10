# Tinman

Source: https://www.chessprogramming.org/Tinman

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Tinman**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Tin_Woodman.png/250px-Tin_Woodman.png)](/File:Tin_Woodman.png)

Tin Woodman [[1]](#cite_note-1)

**Tinman**,  
a didactic [open source chess engine](/Category:Open_Source "Category:Open Source") by [Mike Leany](/Mike_Leany "Mike Leany"), written in [Rust](/Rust "Rust"), compliant to the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). Tinman is licensed under the [Mozilla Public License](https://en.wikipedia.org/wiki/Mozilla_Public_License), V. 2.0, and was first released in January 2020 [[2]](#cite_note-2).

# Description

So far, Tinman is quite rudimentary and lacks state of the art [search](/Search "Search") techniques and [evaluation](/Evaluation "Evaluation") terms - and has therefore huge potential to improve further.
It [represents the board](/Board_Representation "Board Representation") with a [little-endian file-rank mapped](/Square_Mapping_Considerations#LittleEndianFileRankMapping "Square Mapping Considerations") [bitboard definition](/Bitboard_Board-Definition "Bitboard Board-Definition"),
and applies [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") [[3]](#cite_note-3).
Search is plain [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table"), [check extension](/Check_Extensions "Check Extensions") and [quiescence](/Quiescence_Search "Quiescence Search") inside the [iterative deepening](/Iterative_Deepening "Iterative Deepening") loop [[4]](#cite_note-4),
considering [material](/Material "Material") and [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") as evaluation terms at the [leaves](/Leaf_Node "Leaf Node") [[5]](#cite_note-5).

# See also

- [Zilch](/Zilch "Zilch")
- [Vapor](/Vapor "Vapor")

# Forum Posts

- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=53) by [Tony Mokonen](/index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](/CCC "CCC"), January 26, 2020
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=75) by [Tony Mokonen](/index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](/CCC "CCC"), February 16, 2020

# External Links

## Chess Engine

- [GitHub - mikeleany/tinman: A Rusty Chess Engine](https://github.com/mikeleany/tinman)
- [Tinman](https://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Tinman&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](/CCRL "CCRL")

## Misc

- [tinman - Wiktionary](https://en.wiktionary.org/wiki/tinman)
- [tin man - Wiktionary](https://en.wiktionary.org/wiki/tin_man)
- [Tin Man - Wiktionary](https://en.wiktionary.org/wiki/Tin_Man)
- [Tinman - Wiktionary](https://en.wiktionary.org/wiki/Tinman)
- [Tin Man from Wikipedia](https://en.wikipedia.org/wiki/Tin_Man)
- [Tin Woodman from Wikipedia](https://en.wikipedia.org/wiki/Tin_Woodman)
- [Tin Man (Star Trek: The Next Generation) from Wikipedia](https://en.wikipedia.org/wiki/Tin_Man_(Star_Trek:_The_Next_Generation))
- [The Tin Man (American horse) from Wikipedia](https://en.wikipedia.org/wiki/The_Tin_Man_(American_horse))
- [The Tin Man (British horse) from Wikipedia](https://en.wikipedia.org/wiki/The_Tin_Man_(British_horse))
- [America](/Category:America "Category:America") - [Tin Man](https://en.wikipedia.org/wiki/Tin_Man_(America_song)) (1974), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) The [Tin Woodman](https://en.wikipedia.org/wiki/Tin_Woodman) as pictured by [William Wallace Denslow](https://en.wikipedia.org/wiki/William_Wallace_Denslow) in [The Wonderful Wizard of Oz](https://en.wikipedia.org/wiki/The_Wonderful_Wizard_of_Oz) by [L. Frank Baum](https://en.wikipedia.org/wiki/L._Frank_Baum), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=53) by [Tony Mokonen](/index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](/CCC "CCC"), January 26, 2020
3. [↑](#cite_ref-3) [tinman/attacks.rs at master · mikeleany/tinman · GitHub](https://github.com/mikeleany/tinman/blob/master/src/chess/bitboard/attacks.rs)
4. [↑](#cite_ref-4) [tinman/mod.rs at master · mikeleany/tinman · GitHub](https://github.com/mikeleany/tinman/blob/master/src/engine/mod.rs)
5. [↑](#cite_ref-5) [tinman/eval.rs at master · mikeleany/tinman · GitHub](https://github.com/mikeleany/tinman/blob/master/src/engine/eval.rs)

**[Up one level](/Engines "Engines")**