# CCR One Hour Test

Source: https://www.chessprogramming.org/CCR_One_Hour_Test

**[Home](/Main_Page "Main Page") \* [Engine Testing](/Engine_Testing "Engine Testing") \* [Test-Positions](/Test-Positions "Test-Positions") \* CCR One Hour Test**

**CCR One Hour Test** by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), published 1994 in [Computer Chess Reports](/Computer_Chess_Reports "Computer Chess Reports") [[1]](#cite_note-1) [[2]](#cite_note-2).
The test was still used in 2018 by [Marco Wiering](/Marco_Wiering "Marco Wiering") et al. in their [deep learning](/Deep_Learning "Deep Learning") experiments to appraise the performance of a [neural networks](/Neural_Networks "Neural Networks") evaluator with a [lookahead](/Search "Search") of [depth](/Depth "Depth") one [[3]](#cite_note-3).

# EPD-Record

[Extended Position Description](/Extended_Position_Description "Extended Position Description") [[4]](#cite_note-4):

```
rn1qkb1r/pp2pppp/5n2/3p1b2/3P4/2N1P3/PP3PPP/R1BQKBNR w KQkq - 0 1 id "CCR01"; bm Qb3;
rn1qkb1r/pp2pppp/5n2/3p1b2/3P4/1QN1P3/PP3PPP/R1B1KBNR b KQkq - 1 1 id "CCR02";bm Bc8;
r1bqk2r/ppp2ppp/2n5/4P3/2Bp2n1/5N1P/PP1N1PP1/R2Q1RK1 b kq - 1 10 id "CCR03"; bm Nh6; am Ne5;
r1bqrnk1/pp2bp1p/2p2np1/3p2B1/3P4/2NBPN2/PPQ2PPP/1R3RK1 w - - 1 12 id "CCR04"; bm b4;
rnbqkb1r/ppp1pppp/5n2/8/3PP3/2N5/PP3PPP/R1BQKBNR b KQkq - 3 5 id "CCR05"; bm e5; 
rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/P1N5/1PQ1PPPP/R1B1KBNR b KQ - 1 5 id "CCR06"; bm Bcx3+;
r4rk1/3nppbp/bq1p1np1/2pP4/8/2N2NPP/PP2PPB1/R1BQR1K1 b - - 1 12 id "CCR07"; bm Rfb8;
rn1qkb1r/pb1p1ppp/1p2pn2/2p5/2PP4/5NP1/PP2PPBP/RNBQK2R w KQkq c6 1 6 id "CCR08"; bm d5;
r1bq1rk1/1pp2pbp/p1np1np1/3Pp3/2P1P3/2N1BP2/PP4PP/R1NQKB1R b KQ - 1 9 id "CCR09"; bm Nd4;
rnbqr1k1/1p3pbp/p2p1np1/2pP4/4P3/2N5/PP1NBPPP/R1BQ1RK1 w - - 1 11 id "CCR10"; bm a4;
rnbqkb1r/pppp1ppp/5n2/4p3/4PP2/2N5/PPPP2PP/R1BQKBNR b KQkq f3 1 3 id "CCR11"; bm d5;
r1bqk1nr/pppnbppp/3p4/8/2BNP3/8/PPP2PPP/RNBQK2R w KQkq - 2 6 id "CCR12"; bm Bxf7+;
rnbq1b1r/ppp2kpp/3p1n2/8/3PP3/8/PPP2PPP/RNBQKB1R b KQ d3 1 5 id "CCR13"; am Ne4; 
rnbqkb1r/pppp1ppp/3n4/8/2BQ4/5N2/PPP2PPP/RNB2RK1 b kq - 1 6 id "CCR14"; am Nxc4;
r2q1rk1/2p1bppp/p2p1n2/1p2P3/4P1b1/1nP1BN2/PP3PPP/RN1QR1K1 w - - 1 12 id "CCR15"; bm exf6;
r1bqkb1r/2pp1ppp/p1n5/1p2p3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1 b kq - 2 7 id "CCR16"; bm d5;
r2qkbnr/2p2pp1/p1pp4/4p2p/4P1b1/5N1P/PPPP1PP1/RNBQ1RK1 w kq - 1 8 id "CCR17"; am hxg4;
r1bqkb1r/pp3ppp/2np1n2/4p1B1/3NP3/2N5/PPP2PPP/R2QKB1R w KQkq e6 1 7 id "CCR18"; bm Bxf6+;
rn1qk2r/1b2bppp/p2ppn2/1p6/3NP3/1BN5/PPP2PPP/R1BQR1K1 w kq - 5 10 id "CCR19"; am Bxe6;
r1b1kb1r/1pqpnppp/p1n1p3/8/3NP3/2N1B3/PPP1BPPP/R2QK2R w KQkq - 3 8 id "CCR20"; am Ndb5;
r1bqnr2/pp1ppkbp/4N1p1/n3P3/8/2N1B3/PPP2PPP/R2QK2R b KQ - 2 11 id "CCR21"; am Kxe6;
r3kb1r/pp1n1ppp/1q2p3/n2p4/3P1Bb1/2PB1N2/PPQ2PPP/RN2K2R w KQkq - 3 11 id "CCR22"; bm a4;
r1bq1rk1/pppnnppp/4p3/3pP3/1b1P4/2NB3N/PPP2PPP/R1BQK2R w KQ - 3 7 id "CCR23"; bm Bxh7+;
r2qkbnr/ppp1pp1p/3p2p1/3Pn3/4P1b1/2N2N2/PPP2PPP/R1BQKB1R w KQkq - 2 6 id "CCR24"; bm Nxe5;
rn2kb1r/pp2pppp/1qP2n2/8/6b1/1Q6/PP1PPPBP/RNB1K1NR b KQkq - 1 6 id "CCR25"; am Qxb3;
```

# See also

- [Kaufman Test Suite](/index.php?title=Kaufman_Test_Suite&action=edit&redlink=1 "Kaufman Test Suite (page does not exist)")

# Publications

- [Larry Kaufman](/Larry_Kaufman "Larry Kaufman") (**1994**). *The One-Hour CCR Test*. [Computer Chess Reports](/Computer_Chess_Reports "Computer Chess Reports"), Vol. 4, No. 2, pp. 25-30
- [Matthia Sabatelli](/Matthia_Sabatelli "Matthia Sabatelli"), [Francesco Bidoia](/Francesco_Bidoia "Francesco Bidoia"), [Valeriu Codreanu](/Valeriu_Codreanu "Valeriu Codreanu"), [Marco Wiering](/Marco_Wiering "Marco Wiering") (**2018**). *Learning to Evaluate Chess Positions with Deep Neural Networks and Limited Lookahead*. ICPRAM 2018, [pdf](http://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/ICPRAM_CHESS_DNN_2018.pdf)

# Forum Posts

- [1 Hour CCR Test by IM Larry Kaufman](https://www.stmintz.com/ccc/index.php?id=167129) by Dana Turnmire, [CCC](/CCC "CCC"), May 01, 2001
- [CCC users - 1 Hour CCR Test - A little experiment - help needed](https://www.stmintz.com/ccc/index.php?id=168043) by [Peter Berger](/Peter_Berger "Peter Berger"), [CCC](/CCC "CCC"), May 04, 2001
- [1 Hour CCR Test/Zarkov and Duck/Updated Summary](https://www.stmintz.com/ccc/index.php?id=169742) by [Peter Berger](/Peter_Berger "Peter Berger"), [CCC](/CCC "CCC"), May 14, 2001 » [Zarkov](/Zarkov "Zarkov"), [Duck](/Duck "Duck")
- [1 Hour CCR Test revisited](http://www.talkchess.com/forum/viewtopic.php?t=55299) by [Peter Berger](/Peter_Berger "Peter Berger"), [CCC](/CCC "CCC"), February 11, 2015

# External Links

- [Kaufman One Hour Test](http://utzingerk.com/test_kaufman) hosted by [Kurt Utzinger](/Kurt_Utzinger "Kurt Utzinger")
- [NHØP](/Category:NHOP "Category:NHOP") Trio - My Shining Hour, [Subway](http://www.subway-der-club.de/#!jazz-im-subway/c1u5b) 1999, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Niels-Henning Ørsted-Pedersen](/Category:NHOP "Category:NHOP"), [Ulf Wakenius](/Category:Ulf_Wakenius "Category:Ulf Wakenius"), and [Jonas Johansen](http://www.jazz.com/encyclopedia/johansen-jonas)

# References

1. [↑](#cite_ref-1) [Larry Kaufman](/Larry_Kaufman "Larry Kaufman") (**1994**). *The One-Hour CCR Test*. [Computer Chess Reports](/Computer_Chess_Reports "Computer Chess Reports"), Vol. 4, No. 2, pp. 25-30
2. [↑](#cite_ref-2) [Re: 1 Hour CCR Test by IM Larry Kaufman](https://www.stmintz.com/ccc/index.php?id=167138) by [Kurt Utzinger](/Kurt_Utzinger "Kurt Utzinger"), [CCC](/CCC "CCC"), May 01, 2001
3. [↑](#cite_ref-3) [Matthia Sabatelli](/Matthia_Sabatelli "Matthia Sabatelli"), [Francesco Bidoia](/Francesco_Bidoia "Francesco Bidoia"), [Valeriu Codreanu](/Valeriu_Codreanu "Valeriu Codreanu"), [Marco Wiering](/Marco_Wiering "Marco Wiering") (**2018**). *Learning to Evaluate Chess Positions with Deep Neural Networks and Limited Lookahead*. ICPRAM 2018, [pdf](http://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/ICPRAM_CHESS_DNN_2018.pdf)
4. [↑](#cite_ref-4) [Re: 1 Hour CCR Test by IM Larry Kaufman](https://www.stmintz.com/ccc/index.php?id=167135) by [Ulrich Türke](/Ulrich_T%C3%BCrke "Ulrich Türke"), [CCC](/CCC "CCC"), May 01, 2001

**[Up one Level](/Test-Positions "Test-Positions")**