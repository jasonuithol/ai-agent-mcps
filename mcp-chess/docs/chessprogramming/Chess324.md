# Chess324

Source: https://www.chessprogramming.org/Chess324

**[Home](/Main_Page "Main Page") \* [Games](/Games "Games") \* Chess324’’’**

**Chess324**, (or Kaufman Random Chess)  
a chess variant invented by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), introduced on Aug 12, 2022 in [CCC](/CCC "CCC"), [[1]](#cite_note-1). In the variant, all Kings, Rooks, Pawns are in their original locations as chess but other pieces are placed randomly in their first and last ranks, with no symmetry requirement between two sides, with the only restriction for bishops of each side must be on different colored squares. The main purpose of the variant is to reduce the number of draw games.

One of 324 initial position:

|  |
| --- |
|                                                                                 ♜♞♛♝♚♞♝♜ ♟♟♟♟♟♟♟♟                                     ♙♙♙♙♙♙♙♙ ♖♘♗♗♔♘♕♖ |

```
rnqbknbr/pppppppp/8/8/8/8/PPPPPPPP/RNBBKNQR w KQkq - 0 1
```

# Programming

Chess324 is almost identical to chess, except for initial positions. Almost all chess software can easily support Chess324 with any change.

## Initial positions

A typical chess engine can support any given position thus it can parse correctly any initial position.

For other software such as chess GUIs which need to generate all initial positions, they can simply store all initial FENs or use some algorithms to generate them when needed.

## Notations

Chess324 can use all chess notations:

- Variant name (in PGN file): should use “chess324”
- UCI engines: should use option UCI\_variant and string "chess324"

# Quotes

by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman") in [CCC](/CCC "CCC"), Aug 22, 2022 [[2]](#cite_note-2) :

```
This version has huge advantages over chess960. First, no special castling rules, any engine or GUI or human can play with no instruction after seeing the initial position. Second, since all but 18 of the 324 positions are asymmetrical, opening play should be much more interesting and complex. Third, the normal positioning of the rooks and kings and normal castling makes the game feel closer to normal chess. Fourth, matches of up to 648 games can be played with no repeat positions, generally enough for most purposes. Most important, no matter how many cores or how much time the engines get, there should be plenty of decisive games for the foreseeable future since many positions are at least not too far from the win/draw line.
```

# See also

- [Chess960 Engines](/Category:Chess960 "Category:Chess960")

# Forum Posts

## 2020 ...

- [Chess324](http://talkchess.com/forum3/viewtopic.php?f=2&t=80482) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), Aug 22, 2022

# External Links

- [Chess324 FEN and PGN](https://github.com/dkappe/leela-chess-weights/tree/master/chess324) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe")

# References

1. [↑](#cite_ref-1) [Chess324](http://talkchess.com/forum3/viewtopic.php?f=2&t=80482) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman")
2. [↑](#cite_ref-2) [Chess324](http://talkchess.com/forum3/viewtopic.php?f=2&t=80482) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), Aug 22, 2022

**[Up one Level](/Games "Games")**