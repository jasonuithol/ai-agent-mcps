# Rule of the Square

Source: https://www.chessprogramming.org/Rule_of_the_Square

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Pawn Structure](/Pawn_Structure "Pawn Structure") \* [Passed Pawn](/Passed_Pawn "Passed Pawn") \* Rule of the Square**

The **Rule of the Square** is a didactic auxiliary expedient in [king](/King "King") versus opponent [passed pawn](/Passed_Pawn "Passed Pawn") races in very late [endings](/Endgame "Endgame"), basically [pawn endgames](/Pawn_Endgame "Pawn Endgame") or even [KPK](/KPK "KPK"), assuming the passer may not supported and the king has no obstructions otherwise. It is based on the [Chebyshev distance](/Distance "Distance") due to possible diagonal king moves. If the king stays outside the *Square of the Pawn*, the passer [to move](/Side_to_move "Side to move") is guaranteed to [promote](/Promotions "Promotions") without being immediately [captured](/Captures "Captures") by the king afterwards.

# The Square of the Pawn

The [Square](https://en.wikipedia.org/wiki/Square_%28geometry%29) (of [squares](/Squares "Squares")) is defined vertically by the passer's [front fill](/Pawn_Fills "Pawn Fills") with the horizontal edge in king [direction](/Direction "Direction"), who is assumed on a different [file](/Files "Files") either on the [luff- or lee side](/Pawn_Spans "Pawn Spans") of the passer. If the respective side span is shorter than the [front span](/Pawn_Spans "Pawn Spans") due to border restrictions, the "Square" becomes oblong. The square of a pawn, usually including the pawn itself except the home [rank](/Ranks "Ranks"), due to [double step](/Pawn_Push#DoublePush "Pawn Push") ability, has a maximum size of six times six squares.

King [to move](/Side_to_move "Side to move") may enter the "Square" to catch the passer:

|  |
| --- |
|                                                      •        •        •        ♙•••         ♚ |

# Area of Hope

The whole area, where a king may catch the passer latest after [queening](/Promotions "Promotions"), is the union of both squares from both luff- and lee directions.

|  |
| --- |
|                                          •        •        •     •••♙••• |

# Implementation

The complete area is already implicit in what most programs do, comparisons of absolute [Chebyshev distance](/Distance "Distance") from king- and pawn squares to [promotion square](/Promotion_Square "Promotion Square") considering [side to move](/Side_to_move "Side to move") aka [tempo](/Tempo "Tempo") and possible [double step](/Pawn_Push#DoublePush "Pawn Push") of the passer.

```
if ( min( 5, distance(pawnSq, promoSq) ) < (distance(kingSq, promoSq) - king2move) )
   pawn can safely promote
```

# Sample Game

During the [ACM 1984](/ACM_1984 "ACM 1984"), last round 4, in [Nuchess](/Nuchess "Nuchess") (2/3) versus [Cray Blitz](/Cray_Blitz "Cray Blitz") (3/3), it seemed as if Nuchess would win, forcing a massive tie for first place. The decisive position anatomized by [Boris Baczynskyj](/Boris_Baczynskyj "Boris Baczynskyj") [[1]](#cite_note-1):

```
After 44... Nc8, the following position was found on the board.
```

:   |  |
    | --- |
    |                                                                                       ♞ ♚ ♜  ♟           ♗ ♖♟    ♙  ♟♔♟              ♙ ♙       ♙ ♙ |

```
2n1k1r1/p7/3B1Rp1/2P2pKp/8/4P1P1/5P1P/8 w - - 17 45
While Nuchess has hardly produced an immortal gem of chess, its performance so far has been fairly thematic - for a computer. White is up a Pawn, but an even more important factor in its favor is the superior activity of all three of its pieces. One good move is 45.Kh6, threatening to trap the black Rook with 46.Kh7. Another approach toward a win is 45.Be5, and the threat of 46.Rxg6 forces 46...Ne7, after which White shifts the Rook by 47.Ra6, and Black has to lose more material. Instead, Nuchess played
45. Rxg6??
This is the move which turned a win into a loss, and allowed Cray to clinch its undisputed first. White wins a second Pawn, but in the coming Pawn ending its material edge is worthless as the white King is too far removed to cope with Black's lone, but distant passed a-Pawn. William Blanchard of the Nuchess team dejectedly confirmed that this program failed to include the principle of the King having to be inside the square of the Pawn to catch it. Of course, Nuchess's search did not extend so deeply that it could see the a-Pawn queening. Hyatt said that Cray knew about the square of the Pawn rule, but that this was the first time he was aware the principle was relevant to the computer's move choice...
```

[ACM 1984](/ACM_1984 "ACM 1984"), round 4, [Nuchess](/Nuchess "Nuchess") - [Cray Blitz](/Cray_Blitz "Cray Blitz")

```
[Event "ACM 1984"]
[Site "San Francisco USA"]
[Date "1984.10.09"]
[Round "4"]
[White "Nuchess"]
[Black "Cray Blitz"]
[Result "0-1"]

1.c4 e5 2.Nc3 Bb4 3.a3 Bxc3 4.dxc3 Ne7 5.g3 d5 6.cxd5 Qxd5 7.Qxd5 Nxd5 8.Bg2 Nb6 
9.a4 O-O 10.a5 Nc4 11.Ra4 Nd6 12.a6 Nd7 13.Be3 Nb6 14.Rh4 Rd8 15.axb7 Bxb7 16.Bxb7 
Nxb7 17.Nf3 Rd5 18.c4 Ra5 19.O-O Ra2 20.Rd1 Rxb2 21.c5 Nc8 22.Rd7 f6 23.Rg4 g6 
24.Rh4 h5 25.Rxc7 Nd8 26.Ra4 Rb7 27.Rxb7 Nxb7 28.Ra6 Kf7 29.Nd2 Nd8 30.Ne4 f5 
31.Ng5+ Kg7 32.Nf3 Nf7 33.Nxe5 Nxe5 34.Bd4 Kg8 35.Bxe5 Ne7 36.e3 Kf7 37.Rf6+ Kg8 
38.Kg2 Rc8 39.Kf3 Re8 40.Ra6 Ra8 41.Kf4 Kf7 42.Kg5 Rg8 43.Rf6+ Ke8 44.Bd6 Nc8 
45.Rxg6 Rxg6+ 46.Kxg6 Nxd6 47.cxd6 a5 48.g4 hxg4 49.Kxf5 a4 50.e4 a3 51.Kxg4 a2
52.e5 a1=Q 53.f4 Qg1+ 54.Kf5 Qxh2 55.e6 Qc2+ 0-1
```

# See also

- [Pawn Race](/Pawn_Race "Pawn Race")
- [Promotions](/Promotions "Promotions")
- [Réti Endgame Study](/R%C3%A9ti_Endgame_Study "Réti Endgame Study")
- [Set-wise Rule of the Square](/King_Pattern#SetwiseRuleoftheSquare "King Pattern")
- [Unstoppable Passer](/Unstoppable_Passer "Unstoppable Passer")

# Forum Posts

- [Square-of-the-pawn](https://www.stmintz.com/ccc/index.php?id=14001) by [Stuart Cracraft](/Stuart_Cracraft "Stuart Cracraft"), [CCC](/CCC "CCC"), January 13, 1998
- [Rule of Square test position](http://www.talkchess.com/forum/viewtopic.php?t=21149) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), May 15, 2008
- [Rule of the square](https://groups.google.com/d/msg/fishcooking/T7OFWxD4LK8/pzurkRQNLjwJ) by [Mikael](/Mikael_B%C3%A4ckman "Mikael Bäckman"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), September 24, 2014 » [Stockfish](/Stockfish "Stockfish")

# External Links

- [Rule of the square](https://en.wikipedia.org/wiki/King_and_pawn_versus_king_endgame#Rule_of_the_square) from [King and pawn versus king endgame from Wikipedia](https://en.wikipedia.org/wiki/King_and_pawn_versus_king_endgame)
- [Rule of the Square from Chess/The Endgame/Pawn Endings - Wikibooks](https://en.wikibooks.org/wiki/Chess/The_Endgame/Pawn_Endings#The_Rule_of_the_Square)
- [Square from Wikipedia](https://en.wikipedia.org/wiki/Square)
- [Steps Ahead](/Category:Steps_Ahead "Category:Steps Ahead") - [Steppin Out](https://stepsahead.bandcamp.com/album/steppin-out) Album Preview, 2016, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   feat. [Mike Mainieri](/Category:Mike_Mainieri "Category:Mike Mainieri"), [Bill Evans](/Category:Bill_Evans "Category:Bill Evans"), [Chuck Loeb](https://en.wikipedia.org/wiki/Chuck_Loeb), [Tom Kennedy](https://en.wikipedia.org/wiki/Tom_Kennedy_(musician)), [Steve Smith](/Category:Steve_Smith "Category:Steve Smith") and the [WDR Big Band](https://de.wikipedia.org/wiki/WDR_Big_Band_K%C3%B6ln) conducted by [Mike Abene](https://en.wikipedia.org/wiki/Mike_Abene)

# References

1. [↑](#cite_ref-1) [Boris Baczynskyj](/Boris_Baczynskyj "Boris Baczynskyj") (**1985**). *The 15th ACM NACCC Anatomized*. [ICCA Journal, Vol. 8, No. 3](/ICGA_Journal#8_3 "ICGA Journal")

**[Up one Level](/Passed_Pawn "Passed Pawn")**