# Knight-Distance

Source: https://www.chessprogramming.org/Knight-Distance

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Squares](/Squares "Squares") \* Knight-Distance**

[![](/images/thumb/4/46/SamuelBakAcross.jpg/300px-SamuelBakAcross.jpg)](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d67d58ae5574bf8baa)

[Samuel Bak](/Category:Samuel_Bak "Category:Samuel Bak") - Across [[1]](#cite_note-1)

The **Knight-Distance** between two squares determines the minimal number of moves a [Knight](/Knight "Knight") needs, to reach one square from the other on the otherwise empty board. Due to its move geometry, the knight changes its [square-color](/Color_of_a_Square "Color of a Square"), each times it moves. Thus, if squares have different color, the number of moves is odd, otherwise with same square color, even. Smaller [distance](/Distance "Distance") does not generally imply smaller KnightDistance.

# Knight Fill

With [bitboards](/Bitboards "Bitboards"), one may use [fill algorithms](/Fill_Algorithms "Fill Algorithms"), to calculate the knight distance by counting the number of fill-cycles until a target set becomes subset of the consecutively expanded [knight attacks](/Knight_Pattern#MultipleKnightAttacks "Knight Pattern").

```
U64 getKnightAttacks(U64 bb) {
   U64 l1 = (bb >> 1) & C64(0x7f7f7f7f7f7f7f7f);
   U64 l2 = (bb >> 2) & C64(0x3f3f3f3f3f3f3f3f);
   U64 r1 = (bb << 1) & C64(0xfefefefefefefefe);
   U64 r2 = (bb << 2) & C64(0xfcfcfcfcfcfcfcfc);
   U64 h1 = l1 | r1;
   U64 h2 = l2 | r2;
   return (h1<<16) | (h1>>16) | (h2<<8) | (h2>>8);
}

// no set should be empty -> assert (b1 != 0 && b2 != 0 )
int calcKnightDistance(U64 b1, U64 b2) {
   int d = 0;
   while ((b1 & b2) == 0) {
      b1 = getKnightAttacks(b1); // as long as sets are disjoint
      d++; // increment distance
   }
   return d;
}

int knightDistance(int a, int b) {
   return calcKnightDistance(C64(1) << a, C64(1) << b);
}
```

# Lookups

One may use this fill-approach to initialize lookup-tables.

## By 64 x 64 Lookup

The obvious and likely fastest solution is to go with a 64 times 64 [array](/Array "Array"), which takes 4 KByte containing all possible knight-distances which are in the 0..6 range on a 8 times 8 board.

```
char arrKnightDistance[64][64]; // 4 KByte, requires some initialization code

int knightDistance(int a, int b) {
   return arrKnightDistance[a][b];
}
```

## By 0x88 Square Relations

Similar to [distance](/Distance "Distance") or [Manhattan-distance](/Manhattan-Distance "Manhattan-Distance"), we may use the [0x88 square relation](/0x88#SquareRelations "0x88") approach for a denser 240 sized [array](/Array "Array") - but there is one minor issue to consider according to [diagonal](/Diagonals "Diagonals") (or [anti-diagonal](/Anti-Diagonals "Anti-Diagonals")) neighbored squares. Those squares have usually a knight distance of two, but a distance of four from (or to) the four corner squares. Those extra cases have to be considered by some extra conditions.

## By Absolute Rank-File Distance

Another alternative is based on a lookup of two 64 element arrays, one is indexed by some absolute 8 x [Rank-Distance](/Ranks#RankDistance "Ranks") plus absolute [File-Distance](/Files#FileDistance "Files"), where diagonal neighbors have a unique distance of 9.

```
const int ndis[64] = { // char
   //  knight-distance
   0, 3, 2, 3, 2, 3, 4, 5,
   3, 2, 1, 2, 3, 4, 3, 4,
   2, 1, 4, 3, 2, 3, 4, 5,
   3, 2, 3, 2, 3, 4, 3, 4,
   2, 3, 2, 3, 4, 3, 4, 5,
   3, 4, 3, 4, 3, 4, 5, 4,
   4, 3, 4, 3, 4, 5, 4, 5,
   5, 4, 5, 4, 5, 4, 5, 6
};

const int corner[64] = { // char
   1, 0, 0, 0, 0, 0, 0, 1,
   0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0,
   1, 0, 0, 0, 0, 0, 0, 1
};

int absRankFileDiff(int a, int b) {
   int rd = (a|7) - (b|7);
   int fd = (a&7) - (b&7);
   return abs(rd) + abs(fd);
}

int knightDistance(int a, int b) {
   int c = absRankFileDiff(a,b);
   int d = ndis[c];
   if (c == 9) d += 2*(corner[a] ^ corner[b]);
   return d;
}
```

Or without a condition:

```
int knightDistance(int a, int b) {
   int c = absRankFileDiff(a,b);
   int d = ndis[c] + 2*((c == 9) & (corner[a] ^ corner[b]));
   return d;
}
```

To avoid further conditions, with the risk of branch miss-predictions up and then, [abs](/Avoiding_Branches#Abs "Avoiding Branches") as intrinsic is likely implemented based on following code snippet ...

```
int abs(int a) {
   int s = a >> 31; // cdq, signed shift, -1 if negative, else 0
   a ^= s;  // ones' complement if negative
   a -= s;  // plus one if negative -> two's complement if negative
   return a;
}
```

... by compilers, on [x86](/X86 "X86") a sequence three instructions: {cdq, xor, sub} or {cdq, add, xor}.

# See also

- [Distance](/Distance "Distance")
- [Manhattan-Distance](/Manhattan-Distance "Manhattan-Distance")

# References

1. [↑](#cite_ref-1) [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d67d58ae5574bf8baa), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](/University_of_Minnesota "University of Minnesota")

**[Up one Level](/Squares "Squares")**