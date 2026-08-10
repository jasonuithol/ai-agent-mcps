# Telepath

Source: https://www.chessprogramming.org/Telepath

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Telepath**

[![](https://upload.wikimedia.org/wikipedia/commons/c/c7/User-FastFission-brain.gif)](/File:User-FastFission-brain.gif)

Brain scanning [[1]](#cite_note-1)

**Telepath**,  
a private, [UCI](/UCI "UCI") compliant [[2]](#cite_note-2) chess engine by [Charles Roberson](/Charles_Roberson "Charles Roberson"), written in [C++](/Cpp "Cpp") [[3]](#cite_note-3), development started in 2004. It had its tournament debut at the [CCT7](/CCT7 "CCT7"), February 2005. Telepath played all further [CCT Tournaments](/CCT_Tournaments "CCT Tournaments"), and also the [ACCA Americas' Computer Chess Championships](/ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship") and [ACCA World Computer Rapid Chess Championships](/ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship"). Telepath uses [bitboards](/Bitboards "Bitboards") as basic data structure and board representation [[4]](#cite_note-4). Its [King safety](/King_Safety "King Safety") considers [tropism](/King_Safety#KingTropism "King Safety") and [square control](/King_Safety#SquareControl "King Safety") by a detailed analysis of attacks and defences around the king [[5]](#cite_note-5).

# Photos

[![CharlesLab.JPG](/images/thumb/c/cb/CharlesLab.JPG/640px-CharlesLab.JPG)](http://aigames.net/ACCA/ACCAChampionships/ACCA2008Championships/SitePics.html)

Charles' portable Lab at [ACCA 2008](/ACCA_2008 "ACCA 2008") running Telepath & [Noonian](/NoonianChess "NoonianChess"). [Bob Hyatt](/Robert_Hyatt "Robert Hyatt") and [Ted Summers](/Ted_Summers "Ted Summers") relaxing [[6]](#cite_note-6)

# Selected Games

[WCRCC 2012](/WCRCC_2012 "WCRCC 2012"), Telepath - [Goldbar](/Goldbar "Goldbar") [[7]](#cite_note-7)

```
[Event "WCRCC 2012"]
[Site "Internet Chess Club"]
[Date "2012.07.14"]
[Round "7"]
[White "Telepath 6.123"]
[Black "Goldbar"]
[Result "1/2-1/2"]

1.d4 Nf6 2.Nf3 e6 3.c4 b6 4.g3 Ba6 5.b3 Bb4+ 6.Bd2 Be7 7.Bg2 c6 8.Bc3 d5 9.Nbd2 Nbd7 
10.O-O O-O 11.Re1 c5 12.e4 dxe4 13.Nxe4 Nxe4 14.Rxe4 Bb7 15.Re3 Bf6 16.dxc5 Bxc3 
17.Rxc3 Nxc5 18.Qe2 Qe7 19.Rd1 Rad8 20.Rcc1 Bxf3 21.Qxf3 a5 22.Qe2 g6 23.Qf3 e5 24.Rd5
Rxd5 25.cxd5 Qd6 26.Qe3 Re8 27.Rd1 Re7 28.a3 Kg7 29.Re1 f6 30.Qc3 Nb7 31.b4 axb4 32.axb4 
Rc7 33.Qb2 Nd8 34.Qb3 Nf7 35.Rd1 f5 36.Qb2 Rc4 37.Rb1 b5 38.Kh1 h5 39.Kg1 h4 40.Qb3 e4 
41.Bf1 Rd4 42.Bxb5 Ne5 43.Be2 Rxd5 44.b5 Qc5 45.Qb4 Qc2 46.Qb2 Qxb2 47.Rxb2 hxg3 48.fxg3
Nd3 49.Rb1 Ne5 50.b6 Rd8 51.b7 Rb8 52.Ba6 g5 53.Kf2 f4 54.Rb4 Nd7 55.Rxe4 Nc5 56.Re5 Nxa6 
57.Rxg5+ Kf6 58.Rb5 fxg3+ 59.Kxg3 Ke7 60.h4 Nc7 61.Rb1 Nd5 62.h5 Kd6 63.h6 Kc7 64.Kh4 Nf6
65.Kg5 Ne4+ 66.Kg6 Rg8+ 67.Kf7 Rb8 68.Rb4 Nd6+ 69.Kf6 Nxb7 70.h7 Rf8+ 71.Kg7 Rd8 72.h8=Q 
Rxh8 73.Kxh8 Nc5 74.Kg7 Kd6 75.Kf6 Kd5 76.Kf5 Nd3 77.Rg4 Ne5 78.Rg8 Nd3 79.Rd8+ Kc4 80.Ke4 
Nc5+ 81.Ke3 Ne6 82.Rd2 Nc5 83.Rd4+ Kc3 84.Rg4 Nd3 85.Re4 Nc5 86.Rh4 Nd3 87.Ke4 Kc4 88.Rh2 
Nc5+ 89.Ke5 Nd3+ 90.Kd6 Kd4 91.Rh4+ Ke3 92.Ke6 Nf4+ 93.Kf5 Nd3 94.Re4+ Kd2 95.Re8 Nf2 
96.Ke5 Kd3 97.Rg8 Ne4 98.Rd8+ Ke3 99.Rh8 Nf2 100.Kd5 Nd1 101.Rh3+ Kf4 102.Kd4 Nf2 103.Rh8 
Kf3 104.Rf8+ Ke2 105.Rf5 Nd3 106.Rg5 Nf2 107.Rg3 Nd1 108.Rd3 Nf2 109.Re3+ Kd2 110.Rb3 Ke2
111.Rc3 Nd1 112.Ra3 Nf2 113.Ra1 Kf3 114.Ra8 Nh3 115.Ra3+ Kg4 116.Rd3 Ng5 117.Ke3 Nh3 
118.Rd4+ Kf5 119.Rd3 Kg4 120.Kd4 Ng5 121.Ke3 Nh3 1/2-1/2
```

# See also

- [Ares](/Ares_US "Ares US")
- [NoonianChess](/NoonianChess "NoonianChess")

# Forum Posts

## 2007 ...

- [Re: Speedup with bitboards on 64-bit CPUs](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=114517&t=13426) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), April 27, 2007
- [king safety](http://www.talkchess.com/forum/viewtopic.php?t=17546) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), November 02, 2007 » [King Safety](/King_Safety "King Safety")
- [Re: Speed up factor when moving from 32 bit to 64 bit operations](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=179844&t=20126) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), March 14, 2008
- [Rule of Square test position](http://www.talkchess.com/forum/viewtopic.php?t=21149) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), May 15, 2008
- [In C++, one does ? for circular dependencies?](http://www.talkchess.com/forum/viewtopic.php?t=26515) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), February 11, 2009
- [I beat Telepath](http://www.talkchess.com/forum/viewtopic.php?t=25956) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), January 12, 2009

## 2010 ...

- [Re: Question for Bob Hyatt](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=321767&t=31708) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), January 20, 2010
- [Re: UCI Implementation in Arena: Bug](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=353482&t=34731) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), June 05, 2010 » [UCI](/UCI "UCI"), [Arena](/Arena "Arena")
- [2011 6th Annual ACCA Pan Am CCC - Telepath games](http://www.talkchess.com/forum/viewtopic.php?t=41061) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), November 12, 2011 » [ACCA 2011](/ACCA_2011 "ACCA 2011")
- [Lone minor piece penalty - What did Larry mean?](http://www.talkchess.com/forum/viewtopic.php?t=41905) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), January 10, 2012
- [How to ponder](http://www.talkchess.com/forum/viewtopic.php?t=47554) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), March 20, 2013 » [Pondering](/Pondering "Pondering")
- [IM Kanan Heydarli vs Telepath](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=47928) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), May 06, 2013 [[8]](#cite_note-8)

## 2015 ...

- [2016 10th Annual WCRCC - Telepath's games](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=60838) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), Jul 16, 2016 » [WCRCC 2016](/WCRCC_2016 "WCRCC 2016")

# External Links

## Chess Engine

- [The chess games of Telepath](http://www.chessgames.com/perl/chessplayer?pid=111044) from [chessgames.com](http://www.chessgames.com/index.html)

## Misc

- [Telepathy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Telepathy_%28disambiguation%29)
- [Telepathy from Wikipedia](https://en.wikipedia.org/wiki/Telepathy)
- [Extrasensory perception from Wikipedia](https://en.wikipedia.org/wiki/Extrasensory_perception)
- [Ganzfeld experiment from Wikipedia](https://en.wikipedia.org/wiki/Ganzfeld_experiment)
- [Paranormal from Wikipedia](https://en.wikipedia.org/wiki/Paranormal)
- [Parapsychology from Wikipedia](https://en.wikipedia.org/wiki/Parapsychology)
- [Thought identification from Wikipedia](https://en.wikipedia.org/wiki/Thought_identification)
- [t e l e p a t h テレパシー能力者](https://www.last.fm/music/t+e+l+e+p+a+t+h+%E3%83%86%E3%83%AC%E3%83%91%E3%82%B7%E3%83%BC%E8%83%BD%E5%8A%9B%E8%80%85) - 永遠に生きる, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Brain scanning technology](https://en.wikipedia.org/wiki/Neuroimaging) is quickly approaching levels of detail that will have serious implications - [this animation](https://en.wikipedia.org/wiki/File:User-FastFission-brain.gif) was made by [Fastfission](https://en.wikipedia.org/wiki/User:Fastfission) and is based on Fastfission's brain. [Thought identification from Wikipedia](https://en.wikipedia.org/wiki/Thought_identification)
2. [↑](#cite_ref-2) [Re: UCI Implementation in Arena: Bug](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=353482&t=34731) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), June 05, 2010
3. [↑](#cite_ref-3) [In C++, one does ? for circular dependencies?](http://www.talkchess.com/forum/viewtopic.php?t=26515) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), February 11, 2009
4. [↑](#cite_ref-4) [Re: Speedup with bitboards on 64-bit CPUs](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=114517&t=13426) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), April 27, 2007
5. [↑](#cite_ref-5) [king safety](http://www.talkchess.com/forum/viewtopic.php?t=17546) by [Charles Roberson](/Charles_Roberson "Charles Roberson"), [CCC](/CCC "CCC"), November 02, 2007
6. [↑](#cite_ref-6) [2008 Third Annual ACCA Americas' Computer Chess Championships - Site Pics](http://aigames.net/ACCA/ACCAChampionships/ACCA2008Championships/SitePics.html)
7. [↑](#cite_ref-7) [The 2012 Sixth Annual ACCA World Computer Rapid Chess Championships| Results](http://aigames.net/ACCA/ACCAWCRCC/2012ACCAWCRCC/WCRCCResults.html)
8. [↑](#cite_ref-8) [Heydarli, Kanan FIDE Chess Profile](https://ratings.fide.com/card.phtml?event=13404423)

**[Up one level](/Engines "Engines")**