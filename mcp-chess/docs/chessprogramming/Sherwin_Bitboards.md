# Sherwin Bitboards

Source: https://www.chessprogramming.org/Sherwin_Bitboards

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Sherwin Bitboards**

The **Sherwin bitboards** were created by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin") with some help from other people in [CCC](/CCC "CCC") [[1]](#cite_note-1). The idea is to generate the attacks of a sliding piece by collecting all occupied squares on its rays for each row. Then use a first lookup table to get an index into a second table that contains the attack bitboards. Most of the hard work is done in the initialization of the tables. Care must be taken with the right order and enumeration of the table indizes. The code below is taken from the chess engine [Elephant](/Elephant "Elephant") and it uses the same [big-endian file-mapping](/Square_Mapping_Considerations "Square Mapping Considerations") as the [exploding bitboards](/Exploding_Bitboards "Exploding Bitboards").

# Bishops

These are the relevant squares for a bishop on d4. We don't have to look at pieces at the border of the board to decide whether their squares can be attacked or defended.

```
 . . . . . . . -
 - . . . . . 1 .  giving 1 bit  or 2 different values from row 7
 . 1 . . . 1 . .  giving 2 bits or 4 different values from row 6
 . . 1 . 1 . . .  giving 2 bits or 4 different values from row 5
 . . . B . . . .  giving 0 bits or 0 different values from row 4
 . . 1 . 1 . . .  giving 2 bits or 4 different values from row 3
 . 1 . . . 1 . .  giving 2 bits or 4 different values from row 2
 - . . . . . - .
```

We need an helper array and an initializing function for the rays. This mask covers the inner 6x6 board only.

```
Bitboard bishopBits[64];
void initBishopBits()
{
    int sq;
    for ( sq = 0; sq < 64; ++sq )
    {
        bishopBits[sq] = 0;
        int i;
        for ( i = sq - 9; i >= 0 && i % 8 != 7; i -= 9 )
            bishopBits[sq] |= C64(1) << i;
        for ( i = sq - 7; i >= 0 && i % 8 != 0; i -= 7 )
            bishopBits[sq] |= C64(1) << i;
        for ( i = sq + 9; i < 64 && i % 8 != 0; i += 9 )
            bishopBits[sq] |= C64(1) << i;
        for ( i = sq + 7; i < 64 && i % 8 != 7; i += 7 )
            bishopBits[sq] |= C64(1) << i;
        bishopBits[sq] &= C64(0x007e7e7e7e7e7e00);
    }
}
```

With the help of a first table we condense the scattered bits to a compact index number. For bits named a to i the value for Bd4 will be:

```
 . . . . . . . -
 - . . . . . i .  giving 1 bit  or 2 different values from row 7
 . g . . . h . .  giving 2 bits or 4 different values from row 6
 . . e . f . . .  giving 2 bits or 4 different values from row 5
 . . . B . . . .  giving 0 bits or 0 different values from row 4
 . . c . d . . .  giving 2 bits or 4 different values from row 3
 . a . . . b . .  giving 2 bits or 4 different values from row 2
 - . . . . . - .

-> 0x0000000ihgfedcba as index. With 2^9 = 512 index values.
```

There are 4 squares with 9 bits like Bd4. Other squares need another amount of bits.

```
const byte squareBitsB[64] =
{
  6, 5, 5, 5, 5, 5, 5, 6,
  5, 5, 5, 5, 5, 5, 5, 5,
  5, 5, 7, 7, 7, 7, 5, 5,
  5, 5, 7, 9, 9, 7, 5, 5,
  5, 5, 7, 9, 9, 7, 5, 5,
  5, 5, 7, 7, 7, 7, 5, 5,
  5, 5, 5, 5, 5, 5, 5, 5,
  6, 5, 5, 5, 5, 5, 5, 6,
};
```

Here is how much values of the first table we need. That is also the size of the second table.

```
 4 squares with 9 bits for 512 indices are 2048 indices.
12 squares with 7 bits for 128 indices are 1536 indices.
44 squares with 5 bits for  32 indices are 1408 indices.
 4 squares with 6 bits for  64 indices are  256 indices.
                                     Total 5248 indices.
```

This is the layout of the first big table with index-bits for each square and all rows. The indices are in this order:

```
0000999999999 4 times 9 bit
0001999999999
0010999999999
0011999999999
0100007777777 12 times 7 bit
01....7777777
0110117777777
0111000666666 4 times 6 bit
0111001666666
0111010666666
0111011666666
0111100055555 44 times 5 bit
........55555
1010001155555
```

And here is the initializing function.

```
short int bishopRows[64][6][64];
void initBishopRows()
{
    int baseIndex = 0;
    for ( int bits = 9; bits >= 5; --bits )
    {
        for ( int sq = 0; sq < 64; ++sq )
        {
            if ( squareBitsB[sq] != bits )
                continue;
            Bitboard bb = bishopBits[sq];
            bb >>= 9;
            int shift = 0;
            for ( int row = 0; row < 6; ++row )
            {
                int p = (bb >> (row * 8)) & 0x3f;
                for ( int pattern = 0; pattern < 64; ++pattern )
                {
                    int index = 0;
                    int s = shift;
                    for ( int i = 0; i < 6; ++i )
                    {
                        if ( p & (1 << i) )
                        {
                            index |= ( (pattern & (1 << i)) ? (1 << s) : 0 );
                            s++;
                            if ( pattern == 63 )
                                shift++;
                        }
                    }
                    bishopRows[sq][row][pattern] = baseIndex + index;
                }
            }
            baseIndex += (1 << bits);
        }
    }
}
```

A second table with 5248 entries can hold all bishop attack bitboards. This table must also be initialized.

```
Bitboard bishopAttackTable[5248];
void initBishopAttacks()
{
    int baseIndex = 0;
    for ( int bits = 9; bits >= 5; --bits )
    {
        for ( int sq = 0; sq < 64; ++sq )
        {
            if ( squareBitsB[sq] != bits )
                continue;
            Bitboard bb = bishopBits[sq];
            for ( int index = 0; index < (1 << bits); ++ index )
            {
                Bitboard occ = 0;
                int i = index;
                for ( int rsq = 0; rsq < 64; ++rsq )
                {
                    if ( bb.test_bit( rsq ) )
                    {
                        if ( i & 1 )
                            occ.set_bit( rsq );
                        i >>= 1;
                    }
                }
                Bitboard att = 0;
                int j;
                for ( j = sq + 9; j < 64 && (j & 7) != 0; j += 9 )
                {
                    att.set_bit( j );
                    if ( occ.test_bit( j ) )
                        break;
                }
                for ( j = sq + 7; j < 64 && (j & 7) != 7; j += 7 )
                {
                    att.set_bit( j );
                    if ( occ.test_bit( j ) )
                        break;
                }
                for ( j = sq - 9; j >= 0 && (j & 7) != 7; j -= 9 )
                {
                    att.set_bit( j );
                    if ( occ.test_bit( j ) )
                        break;
                }
                for ( j = sq - 7; j >= 0 && (j & 7) != 0; j -= 7 )
                {
                    att.set_bit( j );
                    if ( occ.test_bit( j ) )
                        break;
                }
                bishopAttackTable[baseIndex + index] = att;
            }
            baseIndex += (1 << bits);
        }
    }
}
```

Ok, here comes the function to get the bishop attack bitboard for a square and occupied bitboard.

```
Bitboard bishopAttacks( int sq, Bitboard occ )
{
    // The remaining blocking pieces in the X-rays
    occ  &= bishopBits[sq];
    occ >>= 9;
    // Since every square has its set of row values the six row lookups
    // simply map any blockers to specific bits that when ored together
    // gives an offset in the bishop attack table.
    short int *bRows = &bishopRows[sq][0][0];
    int index = (bRows +   0)[(occ >>  0) & 0x3f]  // row 2
              | (bRows +  64)[(occ >>  8) & 0x3f]  // row 3
              | (bRows + 128)[(occ >> 16) & 0x3f]  // row 4
              | (bRows + 192)[(occ >> 24) & 0x3f]  // row 5
              | (bRows + 256)[(occ >> 32) & 0x3f]  // row 6
              | (bRows + 320)[(occ >> 40) & 0x3f]; // row 7
    return bishopAttackTable[index];
}
```

Perhaps you should look at this function first to understand the algorithm.

After the creation of the lookup tables which is only done once the often used bishopAttacks() function is rather easy and performant. And it is branchless.

There is a possible modification of this function that uses unions rather than >> and &. Some people believe that is faster. But it depends on big and little endianess.

```
#if BIG_ENDIAN() && !LITTLE_ENDIAN()
// Big end first means row 8 is first byte with my square encoding.
struct BBBytes
{
    unsigned char row8;
    unsigned char row7;
    unsigned char row6;
    unsigned char row5;
    unsigned char row4;
    unsigned char row3;
    unsigned char row2;
    unsigned char row1;
};
#elif LITTLE_ENDIAN() && !BIG_ENDIAN()
// Little end first means row 1 is first byte with my square encoding.
struct BBBytes
{
    unsigned char row1;
    unsigned char row2;
    unsigned char row3;
    unsigned char row4;
    unsigned char row5;
    unsigned char row6;
    unsigned char row7;
    unsigned char row8;
};
#else
    #error big little endian
#endif

union BBUnion
{
    Bits64   bb;    // typedef uint64 Bits64;
    BBBytes  bbb;
};

Bitboard bishopAttacks( int sq, Bitboard occ )
{
    // The remaining blocking pieces in the X-rays
    occ  &= bishopBits[sq];
    occ >>= 1;
    BBUnion occu;
    occu.bb = occ;
    // Since every square has its set of row values the six row lookups
    // simply map any blockers to specific bits that when ored together
    // gives an offset in the bishop attack table.
    short int *bRows = &bishopRows[sq][0][0];
    int index = (bRows +   0)[occu.bbb.row2]  // row 2
              | (bRows +  64)[occu.bbb.row3]  // row 3
              | (bRows + 128)[occu.bbb.row4]  // row 4
              | (bRows + 192)[occu.bbb.row5]  // row 5
              | (bRows + 256)[occu.bbb.row6]  // row 6
              | (bRows + 320)[occu.bbb.row7]; // row 7
    return bishopAttackTable[index];
}
```

# Rooks

Rooks are mostly treated like the bishops. It starts with their rays.

```
Bitboard rookBits[64];
void initRookBits()
{
    int sq;
    for ( sq = 0; sq < 64; ++sq )
    {
        rookBits[sq] = 0;
        int i;
        for ( i = sq - 1; i >= 0 && i % 8 != 7; --i )
            rookBits[sq] |= C64(1) << i;
        for ( i = sq - 8; i >= 0; i -= 8 )
            rookBits[sq] |= C64(1) << i;
        for ( i = sq + 1; i < 64 && i % 8 != 0; ++i )
            rookBits[sq] |= C64(1) << i;
        for ( i = sq + 8; i < 64; i += 8 )
            rookBits[sq] |= C64(1) << i;
        if ( (sq & 7) != 7 )
            rookBits[sq] &= C64(0x7f7f7f7f7f7f7f7f);
        if ( (sq & 7) != 0 )
            rookBits[sq] &= C64(0xfefefefefefefefe);
        if ( (sq / 8) != 7 )
            rookBits[sq] &= C64(0x00ffffffffffffff);
        if ( (sq / 8) != 0 )
            rookBits[sq] &= C64(0xffffffffffffff00);
    }
}
```

There are 36 squares with 10 bits like Rd4. Other squares need another amount of bits.

```
const byte squareBitsR[64] =
{
  12, 11, 11, 11, 11, 11, 11, 12,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  12, 11, 11, 11, 11, 11, 11, 12,
};
```

This is the layout of the first big table with index-bits for each square and all rows. The indices are in this order:

```
00000cccccccccccc 4 times 12 bit
00001cccccccccccc
00010cccccccccccc
00011cccccccccccc
001000bbbbbbbbbbb 24 times 11 bit
0.....bbbbbbbbbbb
100111bbbbbbbbbbb
1010000aaaaaaaaaa 36 times 10 bit
.......aaaaaaaaaa
1110011aaaaaaaaaa
```

For rooks we need a bigger second table. It has 102400 entries. This makes even the first table bigger because it can not use 2 byte short integer values. And the last dimension of the first table has to cover all 8 bits of a row. This is because rooks on file a or h have rays along the outside files.

Here is the initializing function.

```
int rookRows[64][8][256];
void initRookRows()
{
    int baseIndex = 0;
    for ( int bits = 12; bits >= 10; --bits )
    {
        for ( int sq = 0; sq < 64; ++sq )
        {
            if ( squareBitsR[sq] != bits )
                continue;
            Bitboard bb = rookBits[sq];
            int shift = 0;
            for ( int row = 0; row < 8; ++row )
            {
                int p = (bb >> (row * 8)) & 0xff;
                for ( int pattern = 0; pattern < 256; ++pattern )
                {
                    int index = 0;
                    int s = shift;
                    for ( int i = 0; i < 8; ++i )
                    {
                        if ( p & (1 << i) )
                        {
                            index |= ( (pattern & (1 << i)) ? (1 << s) : 0 );
                            s++;
                            if ( pattern == 255 )
                                shift++;
                        }
                    }
                    rookRows[sq][row][pattern] = baseIndex + index;
                    //logf << "rookRows " << sq << " " << row << " " << pattern << " : ";
                    //logf << rookRows[sq][row][pattern] << endl;
                }
            }
            baseIndex += (1 << bits);
        }
    }
}
```

A second table with 102400 entries can hold all rook attack bitboards. This table must also be initialized.

```
Bitboard rookAttackTable[102400];
void initRookAttacks()
{
    int baseIndex = 0;
    for ( int bits = 12; bits >= 10; --bits )
    {
        for ( int sq = 0; sq < 64; ++sq )
        {
            if ( squareBitsR[sq] != bits )
                continue;
            Bitboard bb = rookBits[sq];
            for ( int index = 0; index < (1 << bits); ++ index )
            {
                Bitboard occ = 0;
                int i = index;
                for ( int rsq = 0; rsq < 64; ++rsq )
                {
                    if ( bb.test_bit( rsq ) )
                    {
                        if ( i & 1 )
                            occ.set_bit( rsq );
                        i >>= 1;
                    }
                }
                Bitboard att = 0;
                int j;
                for ( j = sq + 1; j < 64 && (j & 7) != 0; ++j )
                {
                    att.set_bit( j );
                    if ( occ.test_bit( j ) )
                        break;
                }
                for ( j = sq + 8; j < 64; j += 8 )
                {
                    att.set_bit( j );
                    if ( occ.test_bit( j ) )
                        break;
                }
                for ( j = sq - 1; j >= 0 && (j & 7) != 7; --j )
                {
                    att.set_bit( j );
                    if ( occ.test_bit( j ) )
                        break;
                }
                for ( j = sq - 8; j >= 0; j -= 8 )
                {
                    att.set_bit( j );
                    if ( occ.test_bit( j ) )
                        break;
                }
                rookAttackTable[baseIndex + index] = att;
            }
            baseIndex += (1 << bits);
        }
    }
}
```

Ok, here comes the function to get the bishop attack bitboard for a square and occupied bitboard.

```
Bitboard rookAttacks( int sq, Bitboard occ )
{
    // The remaining blocking pieces in the +-rays
    occ &= rookBits[sq];
    // Since every square has its set of row values the six row lookups
    // simply map any blockers to specific bits that when ored together
    // gives an offset in the bishop attack table.
    int *rRows = &rookRows[sq][0][0];
    int index = (rRows +    0)[(occ >>  0) & 0xff]  // row 1
              | (rRows +  256)[(occ >>  8) & 0xff]  // row 2
              | (rRows +  512)[(occ >> 16) & 0xff]  // row 3
              | (rRows +  768)[(occ >> 24) & 0xff]  // row 4
              | (rRows + 1024)[(occ >> 32) & 0xff]  // row 5
              | (rRows + 1280)[(occ >> 40) & 0xff]  // row 6
              | (rRows + 1536)[(occ >> 48) & 0xff]  // row 7
              | (rRows + 1792)[(occ >> 56) & 0xff]; // row 8
    return rookAttackTable[index];
}
```

Perhaps you should look at this function first to understand the algorithm.

After the creation of the lookup tables which is only done once the often used bishopAttacks() function is rather easy and performant. And it is branchless.

Again there is the option to use unions.

```
Bitboard rookAttacks( int sq, Bitboard occ )
{
    // The remaining blocking pieces in the +-rays
    occ &= rookBits[sq];
    BBUnion occu;
    occu.bb = occ;
    // Since every square has its set of row values the six row lookups
    // simply map any blockers to specific bits that when ored together
    // gives an offset in the bishop attack table.
    int *rRows = &rookRows[sq][0][0];
    int index = (rRows +    0)[occu.bbb.row1]  // row 1
              | (rRows +  256)[occu.bbb.row2]  // row 2
              | (rRows +  512)[occu.bbb.row3]  // row 3
              | (rRows +  768)[occu.bbb.row4]  // row 4
              | (rRows + 1024)[occu.bbb.row5]  // row 5
              | (rRows + 1280)[occu.bbb.row6]  // row 6
              | (rRows + 1536)[occu.bbb.row7]  // row 7
              | (rRows + 1792)[occu.bbb.row8]; // row 8
    return rookAttackTable[index];
}
```

# Results

The results of the functions bishopAttacks() and rookAttacks() can be used in the same way as described in [exploding bitboards](/Exploding_Bitboards "Exploding Bitboards").

# See also

- [SISSY Bitboards](/SISSY_Bitboards "SISSY Bitboards")

# References

1. [↑](#cite_ref-1) [New bitboard move generator](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5587) by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 14, 2006

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**