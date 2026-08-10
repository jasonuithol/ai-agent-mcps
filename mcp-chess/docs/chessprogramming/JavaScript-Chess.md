# JavaScript-Chess

Source: https://www.chessprogramming.org/JavaScript-Chess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* JavaScript-Chess**

**JavaScript-Chess**,  
a didactic [open source chess program](/Category:Open_Source "Category:Open Source") by [Bill Jordan](/Bill_Jordan "Bill Jordan"), written in [JavaScript](/JavaScript "JavaScript") to run in a [web browser](https://en.wikipedia.org/wiki/Web_browser).
JavaScript-Chess is available on [GitHub](https://en.wikipedia.org/wiki/GitHub) [[1]](#cite_note-1) - an [ebook](https://en.wikipedia.org/wiki/Ebook) explaining the program is available from [Amazon](https://en.wikipedia.org/wiki/Amazon_(company))
[[2]](#cite_note-2).
The JavaScript code, executed in the background by a [web worker](https://en.wikipedia.org/wiki/Web_worker),
is embedded in a [HTML](https://en.wikipedia.org/wiki/HTML) document of a [web page](https://en.wikipedia.org/wiki/Web_page)
which implements the [graphical user interface](/GUI "GUI"), to [render](https://en.wikipedia.org/wiki/Rendering_(computer_graphics)) a [2D graphics board](/2D_Graphics_Board "2D Graphics Board") with [pieces](/Pieces "Pieces")
using [jpeg](https://en.wikipedia.org/wiki/JPEG) images, and to allow user and web worker interaction through [message passing](https://en.wikipedia.org/wiki/Message_passing).

# Features

[[3]](#cite_note-3)

## [Board Representation](/Board_Representation "Board Representation")

- [8x8 Board](/8x8_Board "8x8 Board")

## [Search](/Search "Search")

- [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
- [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
- [Transposition Table](/Transposition_Table "Transposition Table")
- [Move Ordering](/Move_Ordering "Move Ordering")
  - [Hash Move](/Hash_Move "Hash Move")
  - [MVV-LVA](/MVV-LVA "MVV-LVA")
  - [History Heuristic](/History_Heuristic "History Heuristic")
- [Extensions](/Extensions "Extensions")
- [Reductions](/Reductions "Reductions")
- [Quiescence Search](/Quiescence_Search "Quiescence Search")

## [Evaluation](/Evaluation "Evaluation")

- [Material](/Material "Material")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [Open Files](/Open_File "Open File")
- [Pawn Structure](/Pawn_Structure "Pawn Structure")
- [King Safety](/King_Safety "King Safety")

# See also

- [Awesome](/Awesome "Awesome")
- [Bills Bare Bones Chess](/Bills_Bare_Bones_Chess "Bills Bare Bones Chess")
- [Bitboard-Chess](/Bitboard-Chess "Bitboard-Chess")

# Publication

- [Bill Jordan](/Bill_Jordan "Bill Jordan") (**2020**). *[How to Write a JavaScript Chess Engine](https://amzn.eu/4Tn5dVE)*. [amazon](https://www.amazon.com/How-Write-JavaScript-Chess-Engine-ebook/dp/B087BJ467C/)

# External Links

- [GitHub - billjordanchess/JavaScript-Chess: JavaScript Chess Engine](https://github.com/billjordanchess/JavaScript-Chess)

# References

1. [↑](#cite_ref-1) [GitHub - billjordanchess/JavaScript-Chess: JavaScript Chess Engine](https://github.com/billjordanchess/JavaScript-Chess)
2. [↑](#cite_ref-2) [Bill Jordan](/Bill_Jordan "Bill Jordan") (**2020**). *[How to Write a JavaScript Chess Engine](https://amzn.eu/4Tn5dVE)*. [amazon](https://www.amazon.com/How-Write-JavaScript-Chess-Engine-ebook/dp/B087BJ467C/)
3. [↑](#cite_ref-3) [JavaScript-Chess/README.md at master · billjordanchess/JavaScript-Chess · GitHub](https://github.com/billjordanchess/JavaScript-Chess/blob/master/README.md)

**[Up one Level](/Engines "Engines")**