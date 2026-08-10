# The Nolot Suite

Source: https://www.chessprogramming.org/The_Nolot_Suite

**[Home](/Main_Page "Main Page") \* [Engine Testing](/Engine_Testing "Engine Testing") \* [Test-Positions](/Test-Positions "Test-Positions") \* The Nolot Suite**

A test-suite created by [Pierre Nolot](/Pierre_Nolot "Pierre Nolot"), in 1994 introduced by [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot") [[1]](#cite_note-1) [[2]](#cite_note-2) in [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums").

# Discussion and Results

The suite was widely discussed in the news groups by [Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu") [[3]](#cite_note-3) [[4]](#cite_note-4), [Steven Edwards](/Steven_Edwards "Steven Edwards") [[5]](#cite_note-5) [[6]](#cite_note-6) and others.

# Bruce's Analysis

[Bruce Moreland](/Bruce_Moreland "Bruce Moreland") made an analysis of those hard positions [[7]](#cite_note-7) :
The suite contains eleven positions:

|  |  |  |
| --- | --- | --- |
| Nolot #1 bm Nxh6 | Nolot #2 bm Rxc5 | Nolot #3 bm Nxg5 |
| |  | | --- | |                                                                                       ♜   ♛♝ ♚  ♝    ♟  ♟  ♟♜  ♟    ♞     ♙♞♟ ♘ ♘        ♖♙  ♗   ♙♙   ♗ ♕♖ ♔ | | |  | | --- | |                                                                                    ♜    ♜♚  ♟♟ ♞ ♟ ♟  ♞♛♙  ♟    ♝ ♙ ♗      ♘♕    ♗   ♙   ♙♙  ♔  ♙   ♖ | | |  | | --- | |                                                                                   ♜  ♛♚  ♜ ♟♟♟ ♝ ♟♟   ♞ ♟       ♟♙ ♞     ♙  ♝    ♙♗ ♘♘  ♙♙    ♙♙ ♖ ♗♕♔  ♖ | |
| This one seems to work, but I don't think that anyone has ever gotten a big score. | This one is correct, but whether or not you find it could be a matter of luck. You might start out with a negative score, but you should get a score of +3 or so if you search long enough. | I don't think that anyone has ever solved this one. |
| Nolot #4 bm Nxe6 | Nolot #5 bm e5 | Nolot #6 bm ... axb |
| |  | | --- | |                                                                                  ♜ ♝ ♚♝ ♜  ♟ ♞ ♟♟♟ ♟  ♟♟♞         ♗♗   ♛♘♙      ♘      ♙♙♙  ♙♙♙ ♖  ♕ ♖♔ | | |  | | --- | |                                                                                       ♜  ♛♜♝ ♚  ♟ ♝  ♟  ♟  ♟♟♞ ♟             ♘♙     ♗♘      ♙♙♙   ♕♙  ♔   ♖♖ | | |  | | --- | |                                                                                   ♜♞♝♛♚  ♜  ♟   ♟♟♟ ♟         ♘♟♙♟    ♕♙♙ ♙ ♞  ♙    ♘       ♔♝♙♙ ♖ ♗  ♗ ♖ | |
| This one also seems to work, but I don't know that anyone has gotten a big score. | Deep Thought got > +3 in four hours. I've gotten +5 in 93 hours. So this one is correct and extremely difficult. | I don't think that anyone has ever solved this. |
| Nolot #7 bm Rxd8 | Nolot #8 bm Bxh7 | Nolot #9 bm Ng5 |
| |  | | --- | |                                                                                          ♜ ♝♚  ♜   ♖  ♟♟♟ ♟   ♟     ♝  ♙  ♛     ♕♙       ♘     ♗    ♙♙    ♖  ♔ | | |  | | --- | |                                                                                        ♜   ♜♝♚  ♟♟♛  ♟♟♟   ♝ ♟♗                  ♕   ♙ ♗   ♙ ♙ ♙  ♙♙  ♖  ♖  ♔ | | |  | | --- | |                                                                                   ♜    ♜ ♚     ♝♟♟♝   ♞ ♟  ♟ ♟ ♞ ♙     ♟ ♟ ♗♘♙    ♙ ♘♙  ♛♙  ♕♙♗    ♖♖  ♔ | |
| This one is hard but works. I've gotten +2 in 37 hours. | Hsu expresses doubt about this one, but mine returned a score of +1 after a day. I don't know whether the key move wins or not. | I don't think that anyone has ever found the key. |
| Nolot #10 bm Rxf7 | Nolot #11 bm Rxh6 |  |
| |  | | --- | |                                                                                      ♜ ♝  ♜♚   ♟ ♞♝♟♟♟ ♟♛ ♟        ♗     ♙  ♘♙      ♘ ♟     ♙♙   ♙♙ ♖  ♕ ♖ ♔ | | |  | | --- | |                                                                                       ♜ ♝   ♚  ♟  ♟ ♞♙    ♟♛♜ ♖♟  ♟  ♟  ♙   ♗ ♙♞♕   ♙       ♙ ♙♙      ♔    ♖ | |  |
| This one is easy. Rxf7 should come back at +1 pretty quickly. I don't know if anyone has done better than this. | This one seems to be pretty easy to find, with a draw score or a score that is a little positive or negative, depending upon the program. |  |

```
So 3, 6, and 9 are monsters and remain unsolved, if they aren't actually broken.
1, 4, and 10 are solvable, but the scores haven't been convincing yet.
11 is also findable, but it seems that the best result is a draw, so don't expect a big positive score.
8 is also solvable, but it might be found due to speculation.
2, 5, and 7 are known to be findable as wins.
```

# EPD

The Nolot Suite as [EPD](/Extended_Position_Description "Extended Position Description") records:

```
r3qb1k/1b4p1/p2pr2p/3n4/Pnp1N1N1/6RP/1B3PP1/1B1QR1K1 w - - bm Nxh6; id "Position 1";
r4rk1/pp1n1p1p/1nqP2p1/2b1P1B1/4NQ2/1B3P2/PP2K2P/2R5 w - - bm Rxc5; id "Position 2";
r2qk2r/ppp1b1pp/2n1p3/3pP1n1/3P2b1/2PB1NN1/PP4PP/R1BQK2R w KQkq - bm Nxg5; id "Position 3";
r1b1kb1r/1p1n1ppp/p2ppn2/6BB/2qNP3/2N5/PPP2PPP/R2Q1RK1 w kq - bm Nxe6; id "Position 4";
r2qrb1k/1p1b2p1/p2ppn1p/8/3NP3/1BN5/PPP3QP/1K3RR1 w - - bm e5; id "Position 5";
rnbqk2r/1p3ppp/p7/1NpPp3/QPP1P1n1/P4N2/4KbPP/R1B2B1R b kq - bm axb5; id "Position 6";
1r1bk2r/2R2ppp/p3p3/1b2P2q/4QP2/4N3/1B4PP/3R2K1 w k - bm Rxd8+; id "Position 7";
r3rbk1/ppq2ppp/2b1pB2/8/6Q1/1P1B3P/P1P2PP1/R2R2K1 w - - bm Bxh7+; id "Position 8";
r4r1k/4bppb/2n1p2p/p1n1P3/1p1p1BNP/3P1NP1/qP2QPB1/2RR2K1 w - - bm Ng5; id "Position 9";
r1b2rk1/1p1nbppp/pq1p4/3B4/P2NP3/2N1p3/1PP3PP/R2Q1R1K w - - bm Rxf7; id "Position 10";
r1b3k1/p2p1nP1/2pqr1Rp/1p2p2P/2B1PnQ1/1P6/P1PP4/1K4R1 w - - bm Rxh6; id "Position 11";
```

# Forum Posts

## 1994

- [11 tactical positions computers can't solve](http://groups.google.com/group/rec.games.chess/browse_frm/thread/79a6da1235df64e7#) by [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 11, 1994
- [Pierre Nolot's solutions to the 11 positions](http://groups.google.com/group/rec.games.chess/browse_frm/thread/90b656d5218b1ed3#) by [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 29, 1994
- [Nolot's 11 difficult positions (possible spoilers)](http://groups.google.com/group/rec.games.chess/browse_frm/thread/cca5343249f882f4#) by [Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 29, 1994
- [Nolot test positions: EPD version](http://groups.google.com/group/rec.games.chess/browse_frm/thread/ce2a1506f6656821#) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 29, 1994
- [Nolot's test vs. Spector](http://groups.google.com/group/rec.games.chess/browse_frm/thread/a5e8ec975daa956a#) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 29, 1994
- [A second look at the Nolot positions](http://groups.google.com/group/rec.games.chess/browse_frm/thread/eecc575a7e25fdd3#) by [Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums") August 2, 1994

## 2000 ...

- [Nolot Bxh7 and deep thought/deep blue](https://www.stmintz.com/ccc/index.php?id=88032) by [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen"), [CCC](/CCC "CCC"), January 12, 2000
- [Rybka in the nolot suite](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=23157) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), August 21, 2008 » [Rybka](/Rybka "Rybka")

## 2010 ...

- [nolot number 3 again](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=37144) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), December 18, 2010
- [ThrowBack Tuesday - Nolot 11](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66401) by [Michael B](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), January 24, 2018

# External Links

- [Nolot from Wikipedia](https://en.wikipedia.org/wiki/Nolot)
- [Gambisco](http://www.blitzchess.fr/fr/tests/gambiscopresentation/index.html) from [blitzchess.fr](http://www.blitzchess.fr/)(French)

# References

1. [↑](#cite_ref-1) [11 tactical positions computers can't solve](http://groups.google.com/group/rec.games.chess/browse_frm/thread/79a6da1235df64e7#) by [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 11, 1994
2. [↑](#cite_ref-2) [Pierre Nolot's solutions to the 11 positions](http://groups.google.com/group/rec.games.chess/browse_frm/thread/90b656d5218b1ed3#) by [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 29, 1994
3. [↑](#cite_ref-3) [Nolot's 11 difficult positions (possible spoilers)](http://groups.google.com/group/rec.games.chess/browse_frm/thread/cca5343249f882f4#) by [Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 29, 1994
4. [↑](#cite_ref-4) [A second look at the Nolot positions](http://groups.google.com/group/rec.games.chess/browse_frm/thread/eecc575a7e25fdd3#) by [Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums") August 2, 1994
5. [↑](#cite_ref-5) [Nolot test positions: EPD version](http://groups.google.com/group/rec.games.chess/browse_frm/thread/ce2a1506f6656821#) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 29, 1994
6. [↑](#cite_ref-6) [Nolot's test vs. Spector](http://groups.google.com/group/rec.games.chess/browse_frm/thread/a5e8ec975daa956a#) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 29, 1994
7. [↑](#cite_ref-7) [The Nolot Suite](http://web.archive.org/web/20040403210216/brucemo.com/compchess/nolot/index.htm) analyzed by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland")

**[Up one level](/Test-Positions "Test-Positions")**