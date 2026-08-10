# Jeiqi Notation

Source: https://www.chessprogramming.org/Jeiqi_Notation

**[Home](/Main_Page "Main Page") \* [Games](/Games "Games") \* [Chinese Chess](/Chinese_Chess "Chinese Chess") \* [Jeiqi](/Jeiqi "Jeiqi") \* Jeiqi Notation’’’**

**Jeiqi Notation** is the set of various abbreviator notational systems used to describe the [Jeiqi position](/Chess_Position "Chess Position") or moves in a Jeiqi game record.

# Names & notations

- Jeiqi piece: a dark/unseen/covered piece
- Reveal move/revelation: a move of a Jeiqi piece. A Jeiqi piece should do the first move as the original piece in which it is located. After the first move, it will be revealed/uncovered to show its real material

Piece names and abbreviators:

```
King / k
Advisor / a
Elephant / e
Rook / r
Cannon / c
Horse / h
Pawn / p
Jeiqi / x
White / w
Black / b
```

# [FEN](/FEN "FEN")

It is similar to the standard of FEN with some extra information about captures since that information is very important to guess to which piece a dark piece could be revealed.

Standard FEN has 6 fields as below:

1) Piece placement: there are two parts

- piece placement: similar to chess. Use x/X for Jeiqi pieces
- captured pieces: all revealed captured pieces and their numbers, enclosed by brackets []. This part appears immediately after the first part, without any space. Pieces with no capture are ignored. Jeiqi pieces are not compulsory since we can calculate them from the board and revealed captures. That can make the FEN string a bit shorter, avoid redundancy and inconsistent data, avoid ugly due to 2-digit numbers (Jeiqi pieces could be 15). Empty brackets could be omitted too. Pieces can be placed in any order. For being beautiful, it is suggested to list all-white pieces first.

Example of a capturing record:

```
[C1H2P3r1p3]
```

White loses 1 Cannon, 2 Horses, 3 Pawns, 1. Black loses 1 Rook, 3 Pawns

2) Active color: similar to chess, w for white, b for black

3) Castling availability: ignore. Use ‘-’ instead

4) En passant: ignore. Use ‘-’ instead

5) Halfmove clock: similar to chess. This is the number of halfmoves since the last capture or pawn advance

6) Fullmove number: similar to chess. The number of the full moves. It starts at 1 and is incremented after Black's move

Examples:
Starting position, empty brackets are totally omitted:

```
xxxxkxxxx/9/1x5x1/x1x1x1x1x/9/9/X1X1X1X1X/1X5X1/9/XXXXKXXXX w - - 0 1
```

Captured Jeiqi pieces (X7) are counted even that is not compulsory.

```
2e6/4k4/9/2Ha1P2p/2a2P3/9/3p5/4E4/e8/2X1K4[R1C1P1X7r1h1p1d6] w - 3 55
```

Another FEN strings:

```
P2xkx2x/2a6/h7e/H5h2/P1P3e1p/6P2/9/4P2X1/1a2A4/1X2K1XA1[R1H1r1p2] b - - 0 1
x3k3x/c3e4/4R4/E4r2x/4p4/4A1R1P/3A5/6E2/9/3XKX2X[C2H1P2a2r1c1h2p1] b - - 0 1
```

# Move notations

It is similar to [Chinese Chess](/Chinese_Chess "Chinese Chess") about pieces, moves notations, and to chess about promotions for revelations.

## Algebraic Notation

Basically, it is similar to [Chinese Chess](/Chinese_Chess "Chinese Chess") move notations. Columns are named from a to i, rows from 0 to 9. For a move of a Jeiqi piece, we notate it as its original piece and use promotion notation for the revelation.

Bellow is a revelation move when a dark piece in original Pawn position i3 pushed to i4 and revealed into a Horse, Rook on i5 moves to d5, dark Horse in b0 moves to c2 and revealed to a Pawn:

Long algebraic notion (LAN):

```
1) i3i4=h i5d5 2) b0c2=p
```

Short algebraic notion (SAN):

```
1) i4=h rc7 2) Hc2=p
```

Coordinate notation:

```
i3i4h i5d5 b0c2p
```

## Traditional Notation

The traditional move notation uses column number by side. We can use them as Xiangqi with some notes:

- Revealing move uses promotional symbol: P1+1=h
- Jeiqi pieces don’t use Jeiqi symbol (X) but their fake pieces. That is just for solving ambitious cases. For example, if the move is written as “x9.1=c” we don’t know if that is a move of a fake Pawn or a fake Rook at column 9. However, “r9.1=c” says clearly the fake Rook at column 9 moved and revealed into a Cannon. The move of a Jeiqi piece and a revealed one can be easily distinguished by checking if they are revealing. For example, if there is a Rook at column 9 advanced 1, it’s move should be “r9.1”.

# [PGN](/PGN "PGN")

Use Jeiqi as the variant name:

```
[Variant “Jeiqi”]
```

# [UCI](/UCI "UCI")

It can use all terms of standard [UCI](/UCI "UCI") for chess with some additions:

## Send from engines

Inform it can play Jeiqi variant:

```
UCI_Variant var jeiqi
UCI_Variant var xiangqi var jeiqi
```

**bestmove:** as typical but it could not have a revelational piece even the moving piece is a Jeiqi one. Reason: the engine cannot decide about revealed piece:

```
bestmove a3a4
```

## Send from chess [GUIs](/GUI "GUI")

A chess GUI should always add revelational pieces to Jeiqi moves:

```
position startpos moves e3e4e b9c7c h2h7r i9h9p e4g2
position fen x3k3x/c3e4/4R4/E4r2x/4p4/4A1R1P/3A5/6E2/9/3XKX2X[C2H1P2a2r1c1h2p1] b - - 0 1 moves e5e4 d3e4
```

# Forum Posts

## 2015 ...

- [A proposal for Jeiqi notation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69386) by [Nguyen Pham](/Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](/CCC "CCC"), December 26, 2018

# External Links

## Chinese Chess

- [World Xiangqi Federation](http://www.wxf.org/xq/in.htm)
- [Xiangqi from Wikipedia](https://en.wikipedia.org/wiki/Xiangqi)
- [Xiangqi: Chinese Chess](http://www.chessvariants.com/xiangqi.html) from [The Chess Variant Pages](http://www.chessvariants.com/)

# References

**[Up one Level](/Games "Games")**