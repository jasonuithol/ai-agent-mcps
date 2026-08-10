# Superpawn

Source: https://www.chessprogramming.org/Superpawn

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Superpawn**

[![](/images/thumb/2/21/Superpawn_logo.jpg/190px-Superpawn_logo.jpg)](/File:Superpawn_logo.jpg)

Superpawn logo [[1]](#cite_note-1)

**Superpawn**, (Super Pawn)  
an [UCI](/UCI "UCI") conform, experimental [open source chess engine](/Category:Open_Source "Category:Open Source") by [John Byrd](/index.php?title=John_Byrd&action=edit&redlink=1 "John Byrd (page does not exist)"), written in [C++](/Cpp "Cpp"), licensed under [Creative Commons 3.0](https://en.wikipedia.org/wiki/Creative_Commons_license) Attribution Unported, and first released in January 2015 [[2]](#cite_note-2).
Superpawn comes with a single C++ source file [[3]](#cite_note-3) , requires a [C++11](/Cpp#11 "Cpp") compiler,
and provides a [CMake](https://en.wikipedia.org/wiki/CMake) implementation to target builds using [Microsoft](/Microsoft "Microsoft") [VC 2013](https://en.wikipedia.org/wiki/Visual_C%2B%2B#32-bit_and_64-bit_versions), [GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) 3.8.2 (or higher) or [Clang](https://en.wikipedia.org/wiki/Clang) compilers, to run Superpawn on [Windows](/Windows "Windows"), [Linux](/Linux "Linux") or [Mac OS](/Mac_OS "Mac OS") respectively.

# Description

The program features a [principal variation search](/Principal_Variation_Search "Principal Variation Search") with [transposition table](/Transposition_Table "Transposition Table"), and a basic [material](/Material "Material") and [mobility](/Mobility "Mobility") [evaluation](/Evaluation "Evaluation"), considering [middlegame](/Middlegame "Middlegame") and [endgame](/Endgame "Endgame") [piece-square tables](/Piece-Square_Tables "Piece-Square Tables"), [tapered](/Tapered_Eval "Tapered Eval") by current [game stage](/Game_Phases "Game Phases").
The [board is represented](/Board_Representation "Board Representation") as [array](/Array "Array") of 64 [pointers](https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29) to [piece](/Pieces "Pieces") [objects](https://en.wikipedia.org/wiki/Object_%28computer_science%29). A piece is an [abstract class](https://en.wikipedia.org/wiki/Abstract_type) with [pure virtual](https://en.wikipedia.org/wiki/Virtual_function#Abstract_classes_and_pure_virtual_functions) *PieceValue* and *GenerateMoves* methods,
implemented in the concrete, derived piece classes including NoPiece for empty squares.

# Quote

by Superpawn's author, [John Byrd](/index.php?title=John_Byrd&action=edit&redlink=1 "John Byrd (page does not exist)") [[4]](#cite_note-4) :

```
Superpawn is an excellent example of the “objects gone wild” style of programming, in which Everything Is An Object. Even the pieces themselves are objects; they know how to move, capture, etc. This of course slows down the move generation and evaluation process immensely, making this program irredeemably slow in tournament conditions. However, its logic is easy to follow and extend as you see fit.
```

# See also

- [SuperChess](/SuperChess "SuperChess")
- [Superstar](/Superstar "Superstar")

# Forum Posts

- [Greetings](http://www.open-chess.org/viewtopic.php?f=5&t=2764) by [John Byrd](/index.php?title=John_Byrd&action=edit&redlink=1 "John Byrd (page does not exist)"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 21, 2015
- [Greetings, and a new engine](http://www.open-chess.org/viewtopic.php?f=5&t=2766) by [John Byrd](/index.php?title=John_Byrd&action=edit&redlink=1 "John Byrd (page does not exist)"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 25, 2015
- [Greetings, and a new engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=55079) by [John Byrd](/index.php?title=John_Byrd&action=edit&redlink=1 "John Byrd (page does not exist)"), [CCC](/CCC "CCC"), January 25, 2015

# External Links

## Chess Engine

- [Superpawn](http://web.archive.org/web/20180307002550/http://chess.johnbyrd.org/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [johnwbyrd/superpawn · GitHub](https://github.com/johnwbyrd/superpawn)

## Misc

- [super- - Wiktionary](https://en.wiktionary.org/wiki/super-)
- [Secrets of the Super Pawn](https://www.chess.com/article/view/the-super-pawn) by [Gregory Serper](https://en.wikipedia.org/wiki/Gregory_Serper), [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), November 02, 2014
- [Superman from Wikipedia](https://en.wikipedia.org/wiki/Superman)
- [Supergirl from Wikipedia](https://en.wikipedia.org/wiki/Supergirl)
- [Superboy (Kon-El) from Wikipedia](https://en.wikipedia.org/wiki/Superboy_%28Kon-El%29)

# References

1. [↑](#cite_ref-1) [Superpawn logo](http://web.archive.org/web/20180307002550/http://chess.johnbyrd.org/) designed by Angela M. Eads, ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
2. [↑](#cite_ref-2) [Greetings, and a new engine](http://www.open-chess.org/viewtopic.php?f=5&t=2766) by [John Byrd](/index.php?title=John_Byrd&action=edit&redlink=1 "John Byrd (page does not exist)"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 25, 2015
3. [↑](#cite_ref-3) [superpawn/Chess.cpp at master · johnwbyrd/superpawn · GitHub](https://github.com/johnwbyrd/superpawn/blob/master/Chess.cpp)
4. [↑](#cite_ref-4) [Superpawn](http://web.archive.org/web/20180307002550/http://chess.johnbyrd.org/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))

**[Up one Level](/Engines "Engines")**