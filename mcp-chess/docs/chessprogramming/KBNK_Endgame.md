# KBNK Endgame

Source: https://www.chessprogramming.org/KBNK_Endgame

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Endgame](/Endgame "Endgame") \* KBNK**

A [checkmate](/Checkmate "Checkmate") with a [bishop](/Bishop "Bishop") and a [knight](/Knight "Knight") against a lone [king](/King "King") is delivered in the corner that can be covered by a bishop of the attacking side. For that reason a program ought to use a separate [piece-square table](/Piece-Square_Tables "Piece-Square Tables") for the position of the opponent king in order to drive it to the correct corner. [Draw](/Draw "Draw") cases due to tactical loss of one of the pieces [[1]](#cite_note-1) or the [stalemate](/Stalemate "Stalemate") trap are left to the [search](/Search "Search") routine.

# Corner-Distance

Alternatively, following [Bit-twiddling](/Bit-Twiddling "Bit-Twiddling") determines the [Manhattan-Distance](/Manhattan-Distance "Manhattan-Distance") to the closest corner square of the bishop [square color](/Color_of_a_Square "Color of a Square"), which might be used as a bonus for the lonesome king. First, the [color of the bishop square](/Color_of_a_Square "Color of a Square") is determined by a multiplication based on 9, to find whether its [file](/Files "Files") and [rank](/Ranks "Ranks") sum is odd or even. It is done that way, that an odd sum results in the sign-bit set, to build a mask by shifting arithmetically right and to conditionally [flip the file](/Flipping_Mirroring_and_Rotating#MirrorHorizontally "Flipping Mirroring and Rotating") of the king square, so that squares 0 and 63 become the relevant corner squares. The king's Corner Manhattan-distance is then simply the sum of its [rank](/Ranks "Ranks") and [file](/Files "Files") indices, if it exceeds 7 the difference to 14 is taken to force the symmetry, mirrored along the [diagonal](/Diagonals "Diagonals") or [anti-diagonal](/Anti-Diagonals "Anti-Diagonals").

```
 0 1 2 3 4 5 6 7     7 6 5 4 3 2 1 0
 1 2 3 4 5 6 7 6     6 7 6 5 4 3 2 1
 2 3 4 5 6 7 6 5     5 6 7 6 5 4 3 2
 3 4 5 6 7 6 5 4     4 5 6 7 6 5 4 3
 4 5 6 7 6 5 4 3     3 4 5 6 7 6 5 4
 5 6 7 6 5 4 3 2     2 3 4 5 6 7 6 5
 6 7 6 5 4 3 2 1     1 2 3 4 5 6 7 6
 7 6 5 4 3 2 1 0     0 1 2 3 4 5 6 7
```

```
/**
 * manhattanDistance2ClosestCornerOfBishopSquareColor
 *   for KBNK purpose
 * @author Gerd Isenberg
 * @param b bishop square (to determine its square color)
 * @param k opponent king square (0..63)
 * @return manhattanDistance to the closest corner square
 *         of the bishop square color
 */
int manhattanDistance2ClosestCornerOfBishopSquareColor(int b, int k)
{
   b =  -1879048192*b >> 31; // 0 | -1 to mirror
   k = (k>>3) + ((k^b) & 7); // rank + (mirrored) file
   k = (15*(k>>3)^k)-(k>>3); // if (k > 7) k = 14 - k
   return k;
}
```

which results in following [x86](/X86 "X86") [Assembly](/Assembly "Assembly"):

```
?manhattanDistance2ClosestCornerOfBishopSquareColor PROC NEAR
; _b$ = ecx
; _k$ = edx
  00000	69 c9 00 00 00 90 imul ecx, 90000000H
  00006	c1 f9 1f          sar  ecx, 31
  00009	33 ca             xor  ecx, edx
  0000b	c1 fa 03          sar  edx, 3
  0000e	83 e1 07          and  ecx, 7
  00011	03 ca             add  ecx, edx
  00013	8b d1             mov  edx, ecx
  00015	c1 fa 03          sar  edx, 3
  00018	8b c2             mov  eax, edx
  0001a	6b c0 0f          imul eax, 15
  0001d	33 c1             xor  eax, ecx
  0001f	2b c2             sub  eax, edx
  00021	c3                ret  0
```

# See also

- [Avoiding Branches](/Avoiding_Branches "Avoiding Branches")
- [Center Manhattan-Distance](/Center_Manhattan-Distance "Center Manhattan-Distance")
- [Color of a Square](/Color_of_a_Square "Color of a Square")
- [Huberman's program](/Huberman "Huberman")
- [Manhattan-Distance](/Manhattan-Distance "Manhattan-Distance")
- [Mop-up Evaluation](/Mop-up_Evaluation "Mop-up Evaluation")
- [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")

# Publications

- [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik") (**1983**). *[Representation of Experts' Knowledge in a Subdomain of Chess Intelligence](https://www.semanticscholar.org/paper/Representation-of-Experts'-Knowledge-in-a-Subdomain-Herik/5f29c029a69f2d69980da4b35402050203421ed4)*. [IJCAI 1983](/Conferences#IJCAI1983 "Conferences")
- [Hans Zellner](/Hans_Zellner "Hans Zellner"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](/Bob_Herschberg "Bob Herschberg") (**1987**). *Corrections and Substantiations to KBNK*. [ICCA Journal, Vol. 10, No. 3](/ICGA_Journal#10_3 "ICGA Journal")
- [Matej Guid](/Matej_Guid "Matej Guid"), [Martin Možina](/Martin_Mo%C5%BEina "Martin Možina"), [Aleksander Sadikov](/Aleksander_Sadikov "Aleksander Sadikov"), [Ivan Bratko](/Ivan_Bratko "Ivan Bratko") (**2010**). *[Deriving Concepts and Strategies from Chess Tablebases](http://www.springerlink.com/content/um0l155681087p7h)*. [Advances in Computer Games 12](/Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://www.ailab.si/matej/doc/Deriving_Concepts_and_Strategies_from_Chess_Tablebases.pdf)

# Forum Posts

## 1997 ...

- [How to get chess program to solve KBN mate?](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d25a7b108d1332a5/) by Paul Pedriana, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), September 17, 1997

:   [Re: How to get chess program to solve KBN mate?](https://groups.google.com/group/rec.games.chess.computer/msg/ba9febc300f8698f) by [David John Blackman](/David_Blackman "David Blackman"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), September 18, 1997 » [KnightCap](/KnightCap "KnightCap")

## 2000 ...

- [Caution K v KBN and lazy eval or futility](https://www.stmintz.com/ccc/index.php?id=110681) by [Brian Richardson](/Brian_Richardson "Brian Richardson"), [CCC](/CCC "CCC"), May 14, 2000 » [Lazy Evaluation](/Lazy_Evaluation "Lazy Evaluation"), [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Symbolic: The KBNK recognizer](https://www.stmintz.com/ccc/index.php?id=350837) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), February 23, 2004 » [Symbolic](/Symbolic "Symbolic")
- [Symbolic: KBNK merit sample code](https://www.stmintz.com/ccc/index.php?id=351153) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), February 24, 2004

## 2010 ...

- [Re: Search with bitbase](http://www.talkchess.com/forum/viewtopic.php?t=45009&start=5) by [Joona Kiiski](/Joona_Kiiski "Joona Kiiski"), [CCC](/CCC "CCC"), September 05, 2012
- [Re: Best was to Recognize Know Endgames?](http://www.talkchess.com/forum/viewtopic.php?t=48826&start=22) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), August 03, 2013 » [Interior Node Recognizer](/Interior_Node_Recognizer "Interior Node Recognizer")
- [Scorpio & egbb issue (OSX)](http://www.talkchess.com/forum/viewtopic.php?t=51133) by Max May, [CCC](/CCC "CCC"), February 01, 2014 » [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases")
- [KBNK](http://www.talkchess.com/forum/viewtopic.php?t=54023) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), October 11, 2014
- [Improved corner painting](http://www.talkchess.com/forum/viewtopic.php?t=58965) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), January 18, 2016 » [Fairy-Max](/Fairy-Max "Fairy-Max")
- [Simple method for simple mates for programs without TBs](http://www.talkchess.com/forum/viewtopic.php?t=62257) by [J. Wesley Cleveland](/index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](/CCC "CCC"), November 25, 2016 » [Center Manhattan-Distance](/Center_Manhattan-Distance "Center Manhattan-Distance"), [Mop-up Evaluation](/Mop-up_Evaluation "Mop-up Evaluation")

## 2020 ...

- [knbk DTM](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77249) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), May 05, 2021 » [DTM](/Endgame_Tablebases#DTM "Endgame Tablebases")

:   [Re: knbk DTM](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77249&start=4) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), May 05, 2021 » [Marcel van Kervinck's](/Marcel_van_Kervinck "Marcel van Kervinck") pretty fast kbnk generator

# External links

- [Longest mate in King, Bishop and Knight versus King endgame](http://www.gilith.com/chess/endgames/kbn_k.html) by [Joe Leslie-Hurd](/Joe_Leslie-Hurd "Joe Leslie-Hurd"), February 16, 2005
- [Bishop and knight checkmate from Wikipedia](https://en.wikipedia.org/wiki/Bishop_and_knight_checkmate)

# References

1. [↑](#cite_ref-1) [Re: Search with bitbase](http://www.talkchess.com/forum/viewtopic.php?t=45009&start=5) by [Joona Kiiski](/Joona_Kiiski "Joona Kiiski"), [CCC](/CCC "CCC"), September 05, 2012

**[Up one Level](/Endgame "Endgame")**