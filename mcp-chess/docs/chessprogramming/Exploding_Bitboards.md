# Exploding Bitboards

Source: https://www.chessprogramming.org/Exploding_Bitboards

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Exploding Bitboards**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NTS_-_BEEF_-_WATUSI.jpg/330px-NTS_-_BEEF_-_WATUSI.jpg)](/File:NTS_-_BEEF_-_WATUSI.jpg)

[Nevada Test Site - Big Explosives Experimental Facility](https://en.wikipedia.org/wiki/Nevada_Test_Site#Area_4) (BEEF) [[1]](#cite_note-1)

The expanding or **exploding bitboards** were created by [Harald Lüßen](/Harald_L%C3%BC%C3%9Fen "Harald Lüßen") with some help from other people in [CCC](/CCC "CCC") [[2]](#cite_note-2) . The idea is to generate the attacks of a sliding piece from its square outside on all its rays in parallel like the waves of a stone thrown into water. This is done in some steps with multiplications and shifts like in the [kindergarten bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards"). At each step or distance from the original square the rays can be expanded or stopped by other pieces from an occupied bitboard. There are some nasty overflow problems at the border of the board that must be solved. This approach is slower than other techniques. The code below is taken from the chess engine [Elephant](/Elephant "Elephant") which is known for some bitboard comparisons but not for [playing strength](/Playing_Strength "Playing Strength").

In the example this [big-endian file-mapping](/Square_Mapping_Considerations "Square Mapping Considerations") is used:

```
    directions and shifts
    +-----+-----+-----+
    |<<= 9|<<= 8|<<= 7|
    +-----+-----+-----+
    |<<= 1|     |>>= 1|
    +-----+-----+-----+
    |>>= 7|>>= 8|>>= 9|
    +-----+-----+-----+

    +-------------------------+
    | 63 62 61 60 59 58 57 56 | 8
    | 55 54 53 52 51 50 49 48 | 7
    | 47 46 45 44 43 42 41 40 | 6
    | 39 38 37 36 35 35 33 32 | 5
    | 31 30 29 28 27 26 25 24 | 4
    | 23 22 21 20 19 18 17 16 | 3
    | 15 14 13 12 11 10  9  8 | 2
    |  7  6  5  4  3  2  1  0 | 1
    +-------------------------+
       a  b  c  d  e  f  g  h
```

The general trick of chasing and pushing around the bits on the board is this: First shift down and sideways far enough to get a good start. Then multiply with 2 to shift one square to the side (left in this mapping) and multiply with 2^8 = 0x100 to move the bit upwards. Use any power of 2 that helps you. Build the sum of all the multiplication factors of all moves for all bits and multiply with that number. There will probably be more bits in the result than there should be because the multiplication works on all original bits. Use a mask to get rid of all the bad bits.

# Bishops

For each square there is an ignition of the explosion.

```
/*
First expanding step (explosion) for a bishop
 . . . . . . . .
 . . . . . . . .
 . . . . . . . .
 . . 1 . 1 . . .
 . . .sq . . . .
 . . 1 . 1 . . .
 . . . . . . . .
 . . . . . . . .
*/
Bitboard initB[64];
void makeInitB()
{
    for ( int sq = 0; sq < 64; ++sq )
    {
        Bitboard bb = C64(1) << sq;
        initB[sq]  = (bb >> 9) & C64(0x7f7f7f7f7f7f7f7f);
        initB[sq] |= (bb >> 7) & C64(0xfefefefefefefefe);
        initB[sq] |= (bb << 9) & C64(0xfefefefefefefefe);
        initB[sq] |= (bb << 7) & C64(0x7f7f7f7f7f7f7f7f);
    }
}
```

The explosion is only allowed along the rays.

```
/*
Mask for bishop attack rays
 . . . . . . . 1
 1 . . . . . 1 .
 . 1 . . . 1 . .
 . . 1 . 1 . . .
 . . .sq . . . .
 . . 1 . 1 . . .
 . 1 . . . 1 . .
 1 . . . . . 1 .
*/
Bitboard maskB[64];
void makeMaskB()
{
    int sq;
    for ( sq = 0; sq < 64; ++sq )
    {
        maskB[sq] = 0;
        int i;
        for ( i = sq - 9; i >= 0 && i % 8 != 7; i -= 9 )
            maskB[sq] |= C64(1) << i;
        for ( i = sq - 7; i >= 0 && i % 8 != 0; i -= 7 )
            maskB[sq] |= C64(1) << i;
        for ( i = sq + 9; i < 64 && i % 8 != 0; i += 9 )
            maskB[sq] |= C64(1) << i;
        for ( i = sq + 7; i < 64 && i % 8 != 7; i += 7 )
            maskB[sq] |= C64(1) << i;
    }
}
```

For each square there is a maximum number of steps to take.

```
/*
Number of expanding steps (explosions) for a bishop
*/
const int repsB[64] =
{
    6, 5, 4, 3, 3, 4, 5, 6,
    5, 5, 4, 3, 3, 4, 5, 5,
    4, 4, 4, 3, 3, 4, 4, 4,
    3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3,
    4, 4, 4, 3, 3, 4, 4, 4,
    5, 5, 4, 3, 3, 4, 5, 5,
    6, 5, 4, 3, 3, 4, 5, 6,
};
```

This does one step of the explosion.

```
/*
= init               >>= 9               *= 0x5005          &= mask            at |= bb
 . . . . . . . .     . . . . . . . .     . . . . . . . .    . . . . . . . .    . . . . . . . .
 . . . . . . . .     . . . . . . . .     . . . . . . . .    . . . . . . . .    . . . . . . . .
 . . . . . . . .     . . . . . . . .     . 1 1 . . 1 . .    . 1 . . . 1 . .    . 1 . . . 1 . .
 . . 1 . 1 . . .     . . . . . . . .     . . . . . . . .    . . . . . . . .    . . 1 . 1 . . .
 . . . s . . . .     . . . 1 . 1 . .     1 1 . . 1 . . .    . . . s . . . .    . . . s . . . .
 . . 1 . 1 . . .     . . . . . . . .     . . . . . . . .    . . . . . . . .    . . 1 . 1 . . .
 . . . . . . . .     . . . 1 . 1 . .     . 1 1 . . 1 . .    . 1 . . . 1 . .    . 1 . . . 1 . .
 . . . . . . . .     . . . . . . . .     . . . . . . . .    . . . . . . . .    . . . . . . . .
*/
Bitboard bishopAttacks( int sq, const Bitboard &free )
{
    Bitboard msk = maskB[sq];
    Bitboard bb  = initB[sq];
    Bitboard at  = bb;
    bb &= free;
    switch ( repsB[sq] )
    {
      case 6:
        bb >>= 9; bb *= 0x00050005; bb &= msk; at |= bb; bb &= free;
      case 5:
        bb >>= 9; bb *= 0x00050005; bb &= msk; at |= bb; bb &= free;
      case 4:
        bb >>= 9; bb *= 0x00050005; bb &= msk; at |= bb; bb &= free;
      case 3:
        bb >>= 9; bb *= 0x00050005; bb &= msk; at |= bb; bb &= free;
        bb >>= 9; bb *= 0x00050005; bb &= msk; at |= bb; bb &= free;
        bb >>= 9; bb *= 0x00050005; bb &= msk; at |= bb;
    }
    return at;
}
```

There are some possible optimisations when the repsB[] array is modified in the corners during
the game or search. Some numbers 7, 8, 9 combined with additional switch cases can work
as a shortcut for bishops in the corners behind pawns.

# Rooks

For each square there is an ignition of the explosion.

```
/*
First expanding step (explosion) for a rook
 . . . . . . . .
 . . . . . . . .
 . . . . . . . .
 . . . 1 . . . .
 . . 1sq 1 . . .
 . . . 1 . . . .
 . . . . . . . .
 . . . . . . . .
*/
Bitboard initR[64];
void makeInitR()
{
    for ( int sq = 0; sq < 64; ++sq )
    {
        Bitboard bb = C64(1) << sq;
        initR[sq]  = (bb >> 8);
        initR[sq] |= (bb >> 1) & C64(0x7f7f7f7f7f7f7f7f);
        initR[sq] |= (bb << 1) & C64(0xfefefefefefefefe);
        initR[sq] |= (bb << 8);
        //logf << "initR[sq] " << sq << endl;
        //logf << initR[sq].txt8lines() << endl;
    }
}
```

The explosion is only allowed along the rays.

```
/*
Mask for rook attack rays
 . . . 1 . . . .
 . . . 1 . . . .
 . . . 1 . . . .
 . . . 1 . . . .
 1 1 1sq 1 1 1 1
 . . . 1 . . . .
 . . . 1 . . . .
 . . . 1 . . . .
*/
Bitboard maskR[64];
void makeMaskR()
{
    int sq;
    for ( sq = 0; sq < 64; ++sq )
    {
        maskR[sq] = 0;
        int i;
        for ( i = sq - 8; i >= 0; i -= 8 )
            maskR[sq] |= C64(1) << i;
        for ( i = sq - 1; i >= 0 && (i & 7) != 7; --i )
            maskR[sq] |= C64(1) << i;
        for ( i = sq + 1; i < 64 && (i & 7) != 0; ++i )
            maskR[sq] |= C64(1) << i;
        for ( i = sq + 8; i < 64; i += 8 )
            maskR[sq] |= C64(1) << i;
    }
}
```

For each square there is a maximum number of steps to take. The number 8 is just a variant of the 7th step.

```
/**
Number of expanding steps (explosions) for a rook
*/
const int repsR[64] =
{
    7, 6, 6, 6, 6, 6, 6, 8,
    7, 5, 5, 5, 5, 5, 5, 8,
    7, 5, 4, 4, 4, 4, 5, 8,
    7, 5, 4, 3, 3, 4, 5, 8,
    7, 5, 4, 3, 3, 4, 5, 8,
    7, 5, 4, 4, 4, 4, 5, 8,
    7, 5, 5, 5, 5, 5, 5, 8,
    7, 6, 6, 6, 6, 6, 6, 8,
};
```

This does one step of the explosion.
We have a lot of work to avoid overflows, wrap around the unwanted bits.

```
/*
= init               >>= 8               *= 0x10281         &= mask            at |= bb
 . . . . . . . .     . . . . . . . .     . . . . . . . .    . . . . . . . .    . . . . . . . .
 . . . . . . . .     . . . . . . . .     . . . . . . . .    . . . . . . . .    . . . . . . . .
 . . . . . . . .     . . . . . . . .     . . . 1 . . . .    . . . 1 . . . .    . . . 1 . . . .
 . . . 1 . . . .     . . . . . . . .     . . 1 . 1 . . .    . . . . . . . .    . . . 1 . . . .
 . . 1 s 1 . . .     . . . 1 . . . .     . 1 . 1 . 1 . .    . 1 . s . 1 . .    . 1 1 s 1 1 . .
 . . . 1 . . . .     . . 1 . 1 . . .     . . 1 . 1 . . .    . . . . . . . .    . . . 1 . . . .
 . . . . . . . .     . . . 1 . . . .     . . . 1 . . . .    . . . 1 . . . .    . . . 1 . . . .
 . . . . . . . .     . . . . . . . .     . . . . . . . .    . . . . . . . .    . . . . . . . .
                                       and nasty overflows
*/
Bitboard rookAttacks( int sq, const Bitboard &free )
{
    Bitboard msk = maskR[sq];   // The mask kills scattered bits
    Bitboard bb  = initR[sq];   // This drives the expansion/explosion. Here is the start.
    Bitboard at  = bb;          // Collecting the resulting attacks
    Bitboard cl  = at;          // Clears some intermediate overflows
    Bitboard ov;                // A nasty overflow bit when 4 directions in first step are possible.
                                // Not nessessary on left side of board for repsR[sq] = 4 or 5.
                                // Invent new numbers?
    // Perhaps it would be easier and faster to use rankR[][] on all ranks.
    // But I like the 'explosive' algorithm. And I want to show that it works.
int repsLeft = 0; // will be overwritten
    bb &= free;
    bb >>= 8;
    switch ( repsR[sq] )
    {
      case 8:
        bb *= 0x00010081;
        repsLeft = 5;
        break;
      case 7:
        bb *= 0x00010201;
        repsLeft = 5;
        break;
      case 6:
        bb *= 0x00010281;
        bb &= ~(C64(1) << (sq - 6));      // Clears for b-squares a nasty overflow from south-west-first-step to h file
        repsLeft = 5;
        break;
      case 5:
        bb *= 0x00010281;
        ov = (C64(1) << (sq + 3));
        bb |= (bb & ov) >> 1;
        bb &= ~ov;
        bb &= ~(C64(1) << (sq - 6));      // Clears for b-squares a nasty overflow from south-west-first-step to h file
        repsLeft = 4;
        break;
      case 4:
        bb *= 0x00010281;
        ov = (C64(1) << (sq + 3));
        bb |= (bb & ov) >> 1;
        bb &= ~ov;
        repsLeft = 3;
        break;
      case 3:
        bb *= 0x00010281;
        ov = (C64(1) << (sq + 3));
        bb |= (bb & ov) >> 1;
        bb &= ~ov;
        repsLeft = 2;
        break;
      }
      default:
      /* reaching here is an error */
      break;
    }
    bb &= msk; at |= bb;
    while(repsLeft-- > 0)
    {
        bb &= free; bb &= ~cl;
        cl = at;
        bb >>= 8; bb *= 0x00010281; bb &= msk; at |= bb;
    }
    if ( sq < 8 ) // or do this before the switch
    {
        int a1a8 = free ;
        at |= rankR[sq][a1a8 & 0x7e];
    }
    return at;
}
```

There are some possible optimisations when the repsR[] array is modified in the corners during
the game or search. Some numbers 9, 10, 11 combined with additional switch cases can work
as a shortcut for rooks in the corners behind pawns.

In the function rookAttacks() rankR is the well know simple lookup table from other bitboard algorithms.

```
int rankR[8][128];
void makeRankR()
{
    for ( int sq = 0; sq < 8; ++sq )
    {
        for ( int i = 0; i < 128; i += 2 )
        {
            int rr = 0;
            int j;
            for ( j = sq - 1; j >= 0; --j )
            {
                rr |= (1 << j);
                if ( !(i & (1 << j)) )  // the 1 bits are the free squares
                    break;
            }
            for ( j = sq + 1; j < 8; ++j )
            {
                rr |= (1 << j);
                if ( !(i & (1 << j)) )  // the 1 bits are the free squares
                    break;
            }
            rankR[sq][i  ] = rr;
            rankR[sq][i+1] = rr;
        }
    }
}
```

# Results

The results can be masked or combined just like in other attack bitboards.

```
/*
Get a bitboard with all positions set to 1 which can be attacked
from a rook or queen on the square.
*/
Bitboard Board::orthogonal_attacks( byte square ) const
{
    Bitboard free = ~(wpieces_ | bpieces_); // from the board representation in the board class
    Bitboard result = rookAttacks( square, free );
    return result;
}

/*
Get a bitboard with all positions set to 1 which can be attacked
from a bishop or queen on the square.
*/
Bitboard Board::diagonal_attacks( byte square ) const
{
    Bitboard free = ~(wpieces_ | bpieces_); // from the board representation in the board class
    Bitboard result = bishopAttacks( square, free );
    return result;
}
```

Another usage requires masks

```
const Bitboard dirMaskRight[8] =
{
    // 0, line_h, line_gh, line_fh, line_eh, line_dh, line_ch, line_bh,
    0, C64(0x0101010101010101), C64(0x0303030303030303), C64(0x0707070707070707), C64(0x0f0f0f0f0f0f0f0f),
    C64(0x1f1f1f1f1f1f1f1f), C64(0x3f3f3f3f3f3f3f3f), C64(0x7f7f7f7f7f7f7f7f)
};

const Bitboard dirMaskLeft[8] =
{
    // line_ag, line_af, line_ae, line_ad, line_ac, line_ab, line_a, 0,
    C64(0xfefefefefefefefe), C64(0xfcfcfcfcfcfcfcfc), C64(0xf8f8f8f8f8f8f8f8), C64(0xf0f0f0f0f0f0f0f0),
    C64(0xe0e0e0e0e0e0e0e0), C64(0xc0c0c0c0c0c0c0c0), C64(0x8080808080808080), 0
};

const Bitboard dirMaskUp[8] =
{
    // row_28, row_38, row_48, row_58, row_68, row_78, row_8, 0,
    C64(0xffffffffffffff00), C64(0xffffffffffff0000), C64(0xffffffffff000000), C64(0xffffffff00000000),
    C64(0xffffff0000000000), C64(0xffff000000000000), C64(0xff00000000000000), 0
};

const Bitboard dirMaskDown[8] =
{
    // 0, row_1, row_12, row_13, row_14, row_15, row_16, row_17,
    0, C64(0x00000000000000ff), C64(0x000000000000ffff), C64(0x0000000000ffffff), C64(0x00000000ffffffff),
    C64(0x000000ffffffffff), C64(0x0000ffffffffffff), C64(0x00ffffffffffffff)
};
```

to generate attacks in one direction.

```
/*
Get a bitboard with all positions set to 1 which can be attacked
from a bishop, rook or queen on the square moving in the direction.
*/
Bitboard Board::direction_attacks( byte square, byte dir ) const
{
    Bitboard result;
    Bitboard free = ~(wpieces_ | bpieces_); // from the board representation in the board class
    // 4 3 2
    // 5 0 1
    // 6 7 8
    switch ( dir )
    {
      case 1:
        result = rookAttacks( square, free );
        result &= dirMaskRight[square & 7];
        break;
      case 5:
        result = rookAttacks( square, free );
        result &= dirMaskLeft[square & 7];
        break;
      case 7:
        result = rookAttacks( square, free );
        result &= dirMaskDown[square >> 3];
        break;
      case 3:
        result = rookAttacks( square, free );
        result &= dirMaskUp[square >> 3];
        break;
      case 8:
        result = bishopAttacks( square, free );
        result &= dirMaskRight[square & 7];
        result &= dirMaskDown[square >> 3];
        break;
      case 4:
        result = bishopAttacks( square, free );
        result &= dirMaskLeft[square & 7];
        result &= dirMaskUp[square >> 3];
        break;
      case 2:
        result = bishopAttacks( square, free );
        result &= dirMaskRight[square & 7];
        result &= dirMaskUp[square >> 3];
        break;
      case 6:
        result = bishopAttacks( square, free );
        result &= dirMaskLeft[square & 7];
        result &= dirMaskDown[square >> 3];
        break;
      default:
        result = 0;
        break;
    }
    return result;
}
```

# References

1. [↑](#cite_ref-1) [Explosion from Wikipedia](https://en.wikipedia.org/wiki/Explosion)
2. [↑](#cite_ref-2) [Re: Compact Bitboard Attacks](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4523&start=80) by [Harald Lüßen](/Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 13, 2006

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**