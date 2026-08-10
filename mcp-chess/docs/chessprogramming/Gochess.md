# Gochess

Source: https://www.chessprogramming.org/Gochess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Gochess**

**Gochess**,  
a didactic [open source chess engine](/Category:Open_Source "Category:Open Source") by [Franziskus Domig](/index.php?title=Franziskus_Domig&action=edit&redlink=1 "Franziskus Domig (page does not exist)"), written in [Golang](/Go_(Programming_Language) "Go (Programming Language)"), released under the [MIT license](/Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") [[1]](#cite_note-1).
It was inspired by [chess-at-nite](/Chess-at-nite "Chess-at-nite") ([C/C++](/Cpp "Cpp")) and uses most of its concepts [[2]](#cite_note-2)

# Screenshot

[![Gochessscreen.jpg](/images/9/94/Gochessscreen.jpg)](https://github.com/fdomig/gochess/blob/master/gochess.png)

Gochess' [command line interface](/CLI "CLI"): [ASCII-board](/Graphics_Programming#ASCIIDiagrams "Graphics Programming") with [Unicode Pieces](/Pieces#Unicode "Pieces") [[3]](#cite_note-3)

# Unicode

[[4]](#cite_note-4)

```
symbolsUnicode = []string {
  ".",
  "♙", "♘", "♗", "♖", "♕", "♔",
  "♟", "♞", "♝", "♜", "♛", "♚",
}
```

# Features

## [Board Representation](/Board_Representation "Board Representation")

- [0x88 Board](/0x88 "0x88")

## [Search](/Search "Search")

[[5]](#cite_note-5)

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")
- [Check Extensions](/Check_Extensions "Check Extensions")

## [Evaluation](/Evaluation "Evaluation")

[[6]](#cite_note-6)

- [Material Balance](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")

# See also

- [chess-at-nite](/Chess-at-nite "Chess-at-nite")

# External Links

## Chess Engine

- [GitHub - fdomig/gochess: A chess engine written in Go](https://github.com/fdomig/gochess)

## Namesakes

- [GitHub - jonpchin/gochess: Online real time chess web server using websockets](https://github.com/jonpchin/gochess)
- [GitHub - anastasop/gochess: A library for handling chess games. It will support PGN, FEN, UCI](https://github.com/anastasop/gochess)

# References

1. [↑](#cite_ref-1) [gochess/LICENSE at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/LICENSE)
2. [↑](#cite_ref-2) [gochess/README.md at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/README.md)
3. [↑](#cite_ref-3) [gochess/gochess.png at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/gochess.png)
4. [↑](#cite_ref-4) [ochess/piece.go at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/engine/piece.go)
5. [↑](#cite_ref-5) [gochess/search.go at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/engine/search.go)
6. [↑](#cite_ref-6) [gochess/eval.go at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/engine/eval.go)

**[Up one level](/Engines "Engines")**