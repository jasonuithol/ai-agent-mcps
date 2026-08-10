# Kogge-Stone Algorithm

Source: https://www.chessprogramming.org/Kogge-Stone_Algorithm

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Kogge-Stone Algorithm**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/4_bit_Kogge_Stone_Adder_Example_new.png/330px-4_bit_Kogge_Stone_Adder_Example_new.png)](/File:4_bit_Kogge_Stone_Adder_Example_new.png)

4-bit Kogge-Stone adder [[1]](#cite_note-1)

The **Kogge-Stone Algorithm** for set-wise [sliding piece](/Sliding_Pieces "Sliding Pieces") attack generation was first introduced by [Steffan Westcott](/Steffan_Westcott "Steffan Westcott") in [CCC](/CCC "CCC") [[2]](#cite_note-2) . It is a [parallel prefix](/Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") approach of a occluded [dumb7](/Dumb7Fill "Dumb7Fill") [flood-fill](https://en.wikipedia.org/wiki/Flood_fill), propagating sliding piece attacks like [carries](https://en.wikipedia.org/wiki/Carry_(arithmetic)) of a [Kogge-Stone](https://en.wikipedia.org/wiki/Kogge-Stone_adder) [hardware adder](/Combinatorial_Logic#Adder "Combinatorial Logic") [[3]](#cite_note-3) in [software](/Parallel_Prefix_Algorithms#KoggeStoneAdder "Parallel Prefix Algorithms"). One needs to pass sliding pieces as generator set "g" and the set of empty squares as propagator set "p". For appropriate attacks we need to shift the occluded fill [one step](/General_Setwise_Operations#OneStepOnly "General Setwise Operations") further, considering wraps.

|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](/Square_Mapping_Considerations "Square Mapping Considerations") | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*. |

# Parallel Prefix

The routine fillUpOccluded() smears the set bits of bitboard g upwards, but only along set bits of p; a reset bit in p is enough to halt a smear. Other routines have a similar effect.

```
U64 fillUpOccluded(U64 g, U64 p) {
   g |= p & (g <<  8);
   p &=     (p <<  8);
   g |= p & (g << 16);
   p &=     (p << 16);
   g |= p & (g << 32);
   return g;
}
```

The method chosen in FillUpOccluded() is based on a Kogge-Stone parallel prefix network, because it can be implemented very easily in software. The diagram below (trust me, it really \_is\_ supposed to look like that) is an illustration of how it works. The corresponding lines of program code are shown on the right. The inputs are fed into the network at the top, pass along the connecting lines, are combined by the # operator at various points, and the outputs appear at the bottom.

```
x1 x2 x3 x4 x5 x6 x7 x8         Input : g, p
|  |  |  |  |  |  |  |
V  V  V  V  V  V  V  V
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|\ |\ |\ |\ |\ |\ |\ |
| \| \| \| \| \| \| \|
|  #  #  #  #  #  #  #          g |= p & (g <<  8);
|  |  |  |  |  |  |  |          p &=     (p <<  8);
|\ |\ |\ |\ |\ |\ |  |
| \: \: \: \: \: \:  |
|  \  \  \  \  \  \  |
|  :\ :\ :\ :\ :\ :\ |
|  | \| \| \| \| \| \|
|  |  #  #  #  #  #  #          g |= p & (g << 16);
|  |  |  |  |  |  |  |          p &=     (p << 16);
|\ |\ |\ |\ |  |  |  |
| \: \: \: \:  |  |  |
|  \  \  \  \  |  |  |
|  :\ :\ :\ :\ |  |  |
|  | \: \: \: \:  |  |
|  |  \  \  \  \  |  |
|  |  :\ :\ :\ :\ |  |
|  |  | \: \: \: \:  |
|  |  |  \  \  \  \  |
|  |  |  ;\ ;\ :\ :\ |
|  |  |  | \| \| \| \|
|  |  |  |  #  #  #  #          g |= p & (g << 32);
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
V  V  V  V  V  V  V  V
q1 q2 q3 q4 q5 q6 q7 q8         Output : g
```

# Direction-wise Fill

*We further rely on the [compass rose](https://en.wikipedia.org/wiki/Compass_rose) to identify [ray-directions](/Direction "Direction").*

```
  noWe         nort         noEa
          +7    +8    +9
              \  |  /
  west    -1 <-  0 -> +1    east
              /  |  \
          -9    -8    -7
  soWe         sout         soEa
```

Assuming [little-endian](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") file mapping. Big-endian file mapping has to swap A and H and east and west. As a reminder - [shifting bitboards](/General_Setwise_Operations#ShiftingBitboards "General Setwise Operations") - the base of further stuff.

## Fill on an empty Board

We already used the south- and north- [parallel prefix](/Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") [fill-routines](/Pawn_Fills "Pawn Fills") while calculating [pawn spans](/Pawn_Spans "Pawn Spans"). We need one additional direction step for ray-attacks on the otherwise empty board to exclude sliders. Convenient to initialize [ray-attacks](/On_an_empty_Board#RayAttacks "On an empty Board") [arrays](/Array "Array") of single sliders. We may conduct those routines from the general occluded fills by passing the universal propagator set. The vertical fills already look familiar.

```
U64 soutFill(U64 gen) {
   gen |= (gen >>  8);
   gen |= (gen >> 16);
   gen |= (gen >> 32);
   return gen;
}

U64 nortFill(U64 gen) {
   gen |= (gen <<  8);
   gen |= (gen << 16);
   gen |= (gen << 32);
   return gen;
}
```

Using explicit propagators as compile time constants to manage the A-, H-file-wraps.

```
U64 eastFill(U64 gen) {
   const U64 pr0 = notAFile;
   const U64 pr1 = pr0 & (pr0 << 1);
   const U64 pr2 = pr1 & (pr1 << 2);
   gen |= pr0 & (gen  << 1);
   gen |= pr1 & (gen  << 2);
   gen |= pr2 & (gen  << 4);
   return gen;
}

U64 noEaFill(U64 gen) {
   const U64 pr0 = notAFile;
   const U64 pr1 = pr0 & (pr0 <<  9);
   const U64 pr2 = pr1 & (pr1 << 18);
   gen |= pr0 & (gen <<  9);
   gen |= pr1 & (gen << 18);
   gen |= pr2 & (gen << 36);
   return gen;
}

U64 soEaFill(U64 gen) {
   const U64 pr0 = notAFile;
   const U64 pr1 = pr0 & (pr0 >>  7);
   const U64 pr2 = pr1 & (pr1 >> 14);
   gen |= pr0 & (gen >>  7);
   gen |= pr1 & (gen >> 14);
   gen |= pr2 & (gen >> 28);
   return gen;
}

U64 westFill(U64 gen) {
   const U64 pr0 = notHFile;
   const U64 pr1 = pr0 & (pr0 >> 1);
   const U64 pr2 = pr1 & (pr1 >> 2);
   gen |= pr0 & (gen >> 1);
   gen |= pr1 & (gen >> 2);
   gen |= pr2 & (gen >> 4);
   return gen;
}

U64 soWeFill(U64 gen) {
   const U64 pr0 = notHFile;
   const U64 pr1 = pr0 & (pr0 >>  9);
   const U64 pr2 = pr1 & (pr1 >> 18);
   gen |= pr0 & (gen >>  9);
   gen |= pr1 & (gen >> 18);
   gen |= pr2 & (gen >> 36);
   return gen;
}

U64 noWeFill(U64 gen) {
   const U64 pr0 = notHFile;
   const U64 pr1 = pr0 & (pr0 <<  7);
   const U64 pr2 = pr1 & (pr1 << 14);
   gen |= pr0 & (gen <<  7);
   gen |= pr1 & (gen << 14);
   gen |= pr2 & (gen << 28);
   return gen;
}
```

## Occluded Fill

Occluded fills include sliders, but exclude blockers [[4]](#cite_note-4).

```
U64 soutOccl(U64 gen, U64 pro) {
   gen |= pro & (gen >>  8);
   pro &=       (pro >>  8);
   gen |= pro & (gen >> 16);
   pro &=       (pro >> 16);
   gen |= pro & (gen >> 32);
   return gen;
}

U64 nortOccl(U64 gen, U64 pro) {
   gen |= pro & (gen <<  8);
   pro &=       (pro <<  8);
   gen |= pro & (gen << 16);
   pro &=       (pro << 16);
   gen |= pro & (gen << 32);
   return gen;
}

U64 eastOccl(U64 gen, U64 pro) {
   pro &= notAFile;
   gen |= pro & (gen << 1);
   pro &=       (pro << 1);
   gen |= pro & (gen << 2);
   pro &=       (pro << 2);
   gen |= pro & (gen << 4);
   return gen;
}

U64 noEaOccl(U64 gen, U64 pro) {
   pro &= notAFile;
   gen |= pro & (gen <<  9);
   pro &=       (pro <<  9);
   gen |= pro & (gen << 18);
   pro &=       (pro << 18);
   gen |= pro & (gen << 36);
   return gen;
}

U64 soEaOccl(U64 gen, U64 pro) {
   pro &= notAFile;
   gen |= pro & (gen >>  7);
   pro &=       (pro >>  7);
   gen |= pro & (gen >> 14);
   pro &=       (pro >> 14);
   gen |= pro & (gen >> 28);
   return gen;
}

U64 westOccl(U64 gen, U64 pro) {
   pro &= notHFile;
   gen |= pro & (gen >> 1);
   pro &=       (pro >> 1);
   gen |= pro & (gen >> 2);
   pro &=       (pro >> 2);
   gen |= pro & (gen >> 4);
   return gen;
}

U64 soWeOccl(U64 gen, U64 pro) {
   pro &= notHFile;
   gen |= pro & (gen >>  9);
   pro &=       (pro >>  9);
   gen |= pro & (gen >> 18);
   pro &=       (pro >> 18);
   gen |= pro & (gen >> 36);
   return gen;
}

U64 noWeOccl(U64 gen, U64 pro) {
   pro &= notHFile;
   gen |= pro & (gen <<  7);
   pro &=       (pro <<  7);
   gen |= pro & (gen << 14);
   pro &=       (pro << 14);
   gen |= pro & (gen << 28);
   return gen;
}
```

## Ray-wise Attacks

Ray-wise attacks need the occluded fills [shift one](/General_Setwise_Operations#OneStepOnly "General Setwise Operations") further, considering wraps.

```
U64 soutAttacks (U64 rooks,   U64 empty) {return soutOne(soutOccl(rooks,   empty));}
U64 nortAttacks (U64 rooks,   U64 empty) {return nortOne(nortOccl(rooks,   empty));}
U64 eastAttacks (U64 rooks,   U64 empty) {return eastOne(eastOccl(rooks,   empty));}
U64 noEaAttacks (U64 bishops, U64 empty) {return noEaOne(noEaOccl(bishops, empty));}
U64 soEaAttacks (U64 bishops, U64 empty) {return soEaOne(soEaOccl(bishops, empty));}
U64 westAttacks (U64 rooks,   U64 empty) {return westOne(westOccl(rooks,   empty));}
U64 soWeAttacks (U64 bishops, U64 empty) {return soWeOne(soWeOccl(bishops, empty));}
U64 noWeAttacks (U64 bishops, U64 empty) {return noWeOne(noWeOccl(bishops, empty));}
```

# Generalized Rays

Since [rotate 64](/General_Setwise_Operations#Rotate "General Setwise Operations") works like a [generalized shift](/General_Setwise_Operations#GeneralizedShift "General Setwise Operations") with positive or negative shift amount, it might be applied to get pawn-attacks for both sides - or a Kogge-Stone fill with a direction parameter and small lookups for shift amount and wrap ands, instead of multiple code for eight directions. Of course generalized shift will be a bit slower due to lookups and using cl as the shift amount register.

```
U64 occludedFill (U64 gen, U64 pro, int dir8)
{
   int r = shift[dir8]; // {+-1,7,8,9}
   pro &= avoidWrap[dir8];
   gen |= pro & rotateLeft(gen, r);
   pro &=       rotateLeft(pro, r);
   gen |= pro & rotateLeft(gen, 2*r);
   pro &=       rotateLeft(pro, 2*r);
   gen |= pro & rotateLeft(gen, 4*r);
   return gen;
}

U64 shiftOne (U64 b, int dir8)
{
   int r = shift[dir8]; // {+-1,7,8,9}
   return rotateLeft(b, r) & avoidWrap[dir8];
}

U64 slidingAttacks (U64 sliders, U64 empty, int dir8)
{
   U64 fill = occludedFill(slider, empty, dir8)
   return shiftOne(fill, dir8);
}

// positve left, negative right shifts
int shift[8] = {9, 1,-7,-8,-9,-1, 7, 8};

U64 avoidWrap[8] =
{
   0xfefefefefefefe00,
   0xfefefefefefefefe,
   0x00fefefefefefefe,
   0x00ffffffffffffff,
   0x007f7f7f7f7f7f7f,
   0x7f7f7f7f7f7f7f7f,
   0x7f7f7f7f7f7f7f00,
   0xffffffffffffff00,
};
```

# See also

- [Steffan Westcott's](/Steffan_Westcott "Steffan Westcott") [Elaboration on Kogge-Stone algorithm](/Parallel_Prefix_Algorithms#FurtherElaborationsOnKoggeStone "Parallel Prefix Algorithms")
- [Add/Sub versus Attacks](/Parallel_Prefix_Algorithms#KoggeStoneAdder "Parallel Prefix Algorithms")
- [Design Principles](/Design_Principles "Design Principles") by [Steffan Westcott](/Steffan_Westcott "Steffan Westcott")
- [Dumb7Fill](/Dumb7Fill "Dumb7Fill")
- [Fill by Subtraction](/Fill_by_Subtraction "Fill by Subtraction")
- [Fill Algorithms](/Fill_Algorithms "Fill Algorithms")
- [Pieces versus Directions](/Pieces_versus_Directions "Pieces versus Directions")
- [SSE2-Wrapper](/SSE2#SSE2WrapperinCpp "SSE2") in [C++](/Cpp "Cpp")

# Publications

- [Peter M. Kogge](/Mathematician#PMKogge "Mathematician"), [Harold S. Stone](/Mathematician#HSStone "Mathematician") (**1972**). *[A Parallel Algorithm for the Efficient Solution of a General Class of Recurrence Equations](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB212080.xhtml)*. Technical Report 25, [Stanford University](/Stanford_University "Stanford University")
- [Peter M. Kogge](/Mathematician#PMKogge "Mathematician") (**1973**). *Parallel Solution of Recurrence Problems*. Ph.D. thesis, [Stanford University](/Stanford_University "Stanford University"), advisor [Harold S. Stone](/Mathematician#HSStone "Mathematician"), [pdf](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.2724&rep=rep1&type=pdf)
- [Peter M. Kogge](/Mathematician#PMKogge "Mathematician"), [Harold S. Stone](/Mathematician#HSStone "Mathematician") (**1973**). *[A Parallel Algorithm for the Efficient Solution of a General Class of Recurrence Equations](https://ieeexplore.ieee.org/document/5009159)*. [IEEE Transactions on Computers](/IEEE#TOC "IEEE"), Vol. C-22, No. 8

# Forum Posts

- [Re: flood fill attack bitboards](https://www.stmintz.com/ccc/index.php?id=252289) by [Steffan Westcott](/Steffan_Westcott "Steffan Westcott"), [CCC](/CCC "CCC"), September 15, 2002
- [Kogge Stone Algorithm mistake on chessprogramming Wiki](http://www.talkchess.com/forum/viewtopic.php?t=22038) by [Christopher Conkie](/index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [CCC](/CCC "CCC"), June 29, 2008
- [Re: Hyperbola Quiesscene: hardly any improvement](http://www.talkchess.com/forum/viewtopic.php?start=0&t=25979&start=10) by [Karlo Bala Jr.](/Karlo_Balla "Karlo Balla"), [CCC](/CCC "CCC"), January 14, 2009 » [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence")
- [Kogge Stone, Vector Based](http://www.talkchess.com/forum/viewtopic.php?t=46974) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), January 22, 2013 » [GPU](/GPU "GPU") [[5]](#cite_note-5) [[6]](#cite_note-6)
- [Fast perft on GPU (upto 20 Billion nps w/o hashing)](http://www.talkchess.com/forum/viewtopic.php?t=48387) by [Ankan Banerjee](/Ankan_Banerjee "Ankan Banerjee"), [CCC](/CCC "CCC"), June 22, 2013 » [Perft](/Perft "Perft"), [GPU](/GPU "GPU")
- [Kogge-Stone example in Chess Programming Wiki](https://talkchess.com/viewtopic.php?t=84876) by Marco Brenco, [CCC](/CCC "CCC"), March 01, 2025

# External Links

- [Kogge-Stone adder from Wikipedia](https://en.wikipedia.org/wiki/Kogge-Stone_adder)
- [Kogge-Stone algorithm](http://terra.fendrich.se/Terra%20Help-1763.htm) from [Terra Help and Information - Theories](http://terra.fendrich.se/Terra%20Help-1647.htm) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich")
- [Gong](/Category:Gong "Category:Gong") - [Shapeshifter](https://en.wikipedia.org/wiki/Shapeshifter_%28Gong_album%29) [[7]](#cite_note-7), 1992, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Kogge-Stone adder from Wikipedia](https://en.wikipedia.org/wiki/Kogge-Stone_adder)
2. [↑](#cite_ref-2) [Re: flood fill attack bitboards](https://www.stmintz.com/ccc/index.php?id=252289) by [Steffan Westcott](/Steffan_Westcott "Steffan Westcott"), [CCC](/CCC "CCC"), September 15, 2002
3. [↑](#cite_ref-3) [Hardware algorithms for arithmetic modules](http://www.aoki.ecei.tohoku.ac.jp/arith/mg/algorithm.html#fsa_pfx) from the ARITH research group, Aoki lab., [Tohoku University](https://en.wikipedia.org/wiki/Tohoku_University)
4. [↑](#cite_ref-4) [Kogge Stone Algorithm mistake on chessprogramming Wiki](http://www.talkchess.com/forum/viewtopic.php?t=22038) by [Christopher Conkie](/index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [CCC](/CCC "CCC"), June 29, 2008
5. [↑](#cite_ref-5) [Parallel Thread Execution from Wikipedia](https://en.wikipedia.org/wiki/Parallel_Thread_Execution)
6. [↑](#cite_ref-6) NVIDIA Compute PTX: Parallel Thread Execution, ISA Version 1.4, March 31, 2009, [pdf](http://www.nvidia.com/content/CUDA-ptx_isa_1.4.pdf)
7. [↑](#cite_ref-7) [Shapeshifting from Wikipedia](https://en.wikipedia.org/wiki/Shapeshifting)

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**