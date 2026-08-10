# 8x8 Board

Source: https://www.chessprogramming.org/8x8_Board

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Mailbox](/Mailbox "Mailbox") \* 8x8 Board**

[![](/images/thumb/b/b5/Lerf.JPG/300px-Lerf.JPG)](/Bibob "Bibob")

8x8 Board [[1]](#cite_note-1)

The **8x8 Board** as basic square-centric board representation is either a two-dimensional [array](/Array "Array") of [bytes](/Byte "Byte") (or integers), containing [piece](/Pieces "Pieces") and empty square codes, indexed by [file](/Files "Files") and [rank](/Ranks "Ranks") index, or more commonly a one-dimensional array indexed by a [square](/Squares "Squares") in a 0..63 range which combines rank or file indices in three consecutive bits each [[2]](#cite_note-2) .
Such a board representation is often used redundantly in [bitboard](/Bitboards "Bitboards") programs to answer the question which piece (if any) resides on a square efficiently. It has to deal with [square mapping](/Square_Mapping_Considerations "Square Mapping Considerations") accordantly.

# Programming

## TSCP

[TSCP](/TSCP "TSCP") uses two 64 element arrays, containing empty square plus [pure piece code](/Pieces#PieceTypeCoding "Pieces"), and empty square plus piece color code [[3]](#cite_note-3):.

```
int color[64];  /* LIGHT, DARK, or EMPTY */
int piece[64];  /* PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, or EMPTY */
```

However, when generating moves, TSCP converts the board data into a bigger array [10x12 Board](/10x12_Board "10x12 Board").

## FirstChess

[FirstChess](/FirstChess "FirstChess") uses two 64 integer arrays, for all tasks, including move generating.

```
int piece[64] = {
    ROOK,  KNIGHT,BISHOP,QUEEN, KING,  BISHOP,KNIGHT,ROOK,
    PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,
    ROOK,  KNIGHT,BISHOP,QUEEN, KING,  BISHOP,KNIGHT,ROOK
};

int color[64] = {
    BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
    BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
    WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE
};
```

## Banksia

[Banksia](/Banksia "Banksia") uses only one vector from C++ standard library [[4]](#cite_note-4):

```
std::vector<Piece> pieces;
```

The vector is initialized [[5]](#cite_note-5):

```
Piece empty(PieceType::empty, Side::none);
for(int i = 0; i < 64; i++) {
    pieces.push_back(empty);
}
```

# Alternatives

As a lone board representation, the 8x8 board has some efficiency issues with [move generation](/Move_Generation "Move Generation") related to off the board test. Therefore more common are approaches dealing with that, that is [10x12 board](/10x12_Board "10x12 Board") with surrounding ranks and files, and [Vector Attacks](/Vector_Attacks "Vector Attacks") with its cheap test and unique square difference property with respect to [distance](/Distance "Distance") and [direction](/Direction "Direction") [[6]](#cite_note-6). In *Games Playing with Computers*, 1972 [[7]](#cite_note-7) , [Alex Bell](/Alex_Bell "Alex Bell") introduced an array of 65 squares, where the purpose of square 65 (always empty) is to detect pawns capturing outside the board by a [table driven move generator](/Table-driven_Move_Generation "Table-driven Move Generation").

# See also

- [10x12 Board](/10x12_Board "10x12 Board")
- [Array of Nibbles](/Nibble#ArrayOfNibbles "Nibble")
- [Bitboards](/Bitboards "Bitboards")

:   [Square Mapping Considerations](/Square_Mapping_Considerations "Square Mapping Considerations")

- [Table-driven Move Generation](/Table-driven_Move_Generation "Table-driven Move Generation")
- [Vector Attacks](/Vector_Attacks "Vector Attacks")

:   [0x88](/0x88 "0x88")

# Publications

- [Claude Shannon](/Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
- [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227

# Forum Posts

- [Fastest Conversion from 0x88 board to 8x8 board representation](https://www.stmintz.com/ccc/index.php?id=178465) by [Artem Pyatakov](/Artem_Petakov "Artem Petakov"), [CCC](/CCC "CCC"), July 06, 2001
- [Re: Ferret/Gerbil question](https://www.stmintz.com/ccc/index.php?id=189800) by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland"), [CCC](/CCC "CCC"), September 21, 2001 » [Ferret](/Ferret "Ferret"), [Gerbil](/Gerbil "Gerbil"), [0x88](/0x88 "0x88")
- [C++ code for board[8][8] representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76817) by [Yves De Billoëz](/Yves_De_Billo%C3%ABz "Yves De Billoëz"), [CCC](/CCC "CCC"), March 08, 2021

:   [Re: C++ code for board[8][8] representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76817&start=4) by [Rein Halbersma](/Rein_Halbersma "Rein Halbersma"), [CCC](/CCC "CCC"), March 08, 2021 » [C++](/Cpp "Cpp")

# External Links

- [Board representation (chess) - Array based from Wikipedia](https://en.wikipedia.org/wiki/Board_representation_%28chess%29#Array_based)
- [Chess board representations](http://www.craftychess.com/hyatt/boardrep.html) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt")
- [Chapter 3: Board Games - 3.1 CHESS](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p003.htm) from [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
- [8 x 8: A Chess Sonata in 8 Movements](https://en.wikipedia.org/wiki/8_x_8:_A_Chess_Sonata_in_8_Movements) (1957) directed by [Hans Richter](https://en.wikipedia.org/wiki/Hans_Richter_%28artist%29), [Marcel Duchamp](/Category:Marcel_Duchamp "Category:Marcel Duchamp") and [Jean Cocteau](https://en.wikipedia.org/wiki/Jean_Cocteau), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   Cast [[8]](#cite_note-8): [Jean Arp](https://en.wikipedia.org/wiki/Jean_Arp), [Paul Bowles](https://en.wikipedia.org/wiki/Paul_Bowles), [Ceal Bryson](http://www.imdb.com/name/nm2701438/), [Alexander Calder](https://en.wikipedia.org/wiki/Alexander_Calder), [Jean Cocteau](https://en.wikipedia.org/wiki/Jean_Cocteau), [Willem de Vogel](http://www.imdb.com/name/nm0212232/?ref_=ttfc_fc_cl_t6), [Dorothea Tanning](/Category:Dorothea_Tanning "Category:Dorothea Tanning")
:   [Max Ernst](/Category:Max_Ernst "Category:Max Ernst"), [Richard Huelsenbeck](https://en.wikipedia.org/wiki/Richard_Huelsenbeck), [Frederick Kiesler](https://en.wikipedia.org/wiki/Frederick_John_Kiesler), [Julien Lary](http://www.imdb.com/name/nm1508036/?ref_=ttfc_fc_cl_t12), [Julien Levy](https://en.wikipedia.org/wiki/Julien_Levy), [Jaqueline Matisse](http://www.imdb.com/name/nm1506477/?ref_=ttfc_fc_cl_t14), [Eugene Pellegrini](http://www.imdb.com/name/nm2692339/?ref_=ttfc_fc_cl_t15), [Man Ray](/Category:Man_Ray "Category:Man Ray"), [Yves Tanguy](https://en.wikipedia.org/wiki/Yves_Tanguy)

# References

1. [↑](#cite_ref-1) 8x8 Board with [LERF](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") square indices, captured with [Bibob](/Bibob "Bibob") by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), 2012
2. [↑](#cite_ref-2) [Chess board representations](http://www.craftychess.com/hyatt/boardrep.html) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt")
3. [↑](#cite_ref-3) [TSCP - data.c](https://jim.sh/svn/jim/vendor/microwindows/current/src/demos/tuxchess/data.c)
4. [↑](#cite_ref-4) <https://github.com/nguyenpham/Banksia/blob/master/src/base/base.h> Banksia - base.h
5. [↑](#cite_ref-5) <https://github.com/nguyenpham/Banksia/blob/master/src/chess/chess.cpp> Banksia - chess.cpp
6. [↑](#cite_ref-6) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, *2 Non-Bitboard Architectures*
7. [↑](#cite_ref-7) [Chapter 3: Board Games - 3.1 CHESS](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p003.htm) from [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
8. [↑](#cite_ref-8) [8 X 8: A Chess Sonata in 8 Movements (1957) - Full Cast & Crew - IMDb](http://www.imdb.com/title/tt0122855/fullcredits?ref_=tt_ov_st_sm)

**[Up one Level](/Mailbox "Mailbox")**