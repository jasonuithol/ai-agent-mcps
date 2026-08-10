# Matant

Source: https://www.chessprogramming.org/Matant

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Matant**

[![](/images/4/4b/LW441-MC-Escher-Moebius-Strip-II-1963.jpg)](http://www.mcescher.com/gallery/recognition-success/mobius-strip-ii/)

[M. C. Escher](/Category:M._C._Escher "Category:M. C. Escher") - Möbius Strip II [[1]](#cite_note-1) [[2]](#cite_note-2)

**Matant**,  
a [WinBoard](/WinBoard "WinBoard") compatible chess engine by [Antoni Szczepański](/Antoni_Szczepa%C5%84ski "Antoni Szczepański"), written in [C](/C "C"), and first released in July 2005. Matant played six [Polish Computer Chess Championships](/Polish_Computer_Chess_Championship "Polish Computer Chess Championship"), from [2002](/PCCC_2002 "PCCC 2002") until [2007](/IOPCCC_2007 "IOPCCC 2007").
In its [logged](/Logging "Logging") [search statistics](/Search_Statistics "Search Statistics"), Matant reports [nullmove pruning](/Null_Move_Pruning "Null Move Pruning"), [mate threats](/Mate_Threat_Extensions "Mate Threat Extensions"), [check extensions](/Check_Extensions "Check Extensions"), [single reply extensions](/One_Reply_Extensions "One Reply Extensions"), [transposition table](/Transposition_Table "Transposition Table") information, number of [nodes](/Node "Node") of [main search](/Search "Search") and [quiescence search](/Quiescence_Search "Quiescence Search"), maximum positional [score](/Score "Score") for both sides, and [game phases](/Game_Phases "Game Phases") in a 0-13 range from [opening](/Opening "Opening") to [endgame](/Endgame "Endgame") [[3]](#cite_note-3).
Based on that information, Matant apparently applies [lazy evaluation](/Lazy_Evaluation "Lazy Evaluation") as well as [tapered evaluation](/Tapered_Eval "Tapered Eval"). Further, Matant uses [Scorpio Bitbases](/Scorpio_Bitbases "Scorpio Bitbases").

# Selected Games

[PCCC 2003](/PCCC_2003 "PCCC 2003"), Matant - [Armageddon](/Armageddon "Armageddon") [[4]](#cite_note-4)

```
[Event "PCCC 2003"]
[Site "Łódź, Poland"]
[Date "2003.08.?"]
[Round "?"]
[White "Matant"]
[Black "Armageddon"]
[Result "1-0"]

1.d4 e6 2.g3 c5 3.Nf3 Nf6 4.Bg2 cxd4 5.O-O d5 6.Nxd4 e5 7.Nb3 Be6 8.Bg5 Nbd7 
9.e4 dxe4 10.Bxe4 Qc7 11.Bf3 e4 12.Bf4 Qb6 13.Bg2 Rd8 14.N1d2 Nd5 15.Bg5 f6 
16.c4 fxg5 17.cxd5 Bxd5 18.Qh5+ Qg6 19.Qxg6+ hxg6 20.Nxe4 Be7 21.Nd6+ Bxd6 
22.Bxd5 b6 23.Nd4 Ne5 24.Ne6 Rd7 25.Nxg5 Be7 26.Rad1 Kf8 27.Ne6+ Kf7 28.Nf4+ 
Kf6 29.Rfe1 Rd6 30.h4 a5 31.Kg2 Rhd8 32.f3 Rh8 33.Bb3 Rxd1 34.Rxd1 b5 35.Nd5+ 
Kf7 36.Nc3+ Kf8 37.Rd5 Nc6 38.Rxb5 Rh5 39.Bd5 Nd8 40.Rxa5 Bb4 41.Rb5 Bxc3 
42.bxc3 Re5 43.a4 Re3 44.c4 Ra3 45.a5 Ke7 46.Kh3 Ke8 47.Kg4 Ke7 48.c5 Kd7 
49.Kg5 Ne6+ 50.Kxg6 Nc7 51.Rb7 Rxa5 52.c6+ Kd6 53.Be4 Ra8 54.h5 Rh8 55.Rxc7 
Kxc7 56.g4 Re8 57.Kxg7 Re7+ 58.Kf6 Kd6 59.g5 Re6+ 60.Kf5 Re5+ 61.Kg4 1-0
```

# See also

- [Mate](/Checkmate "Checkmate")
- [Mate at a Glance](/Mate_at_a_Glance "Mate at a Glance")
- [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
- [Mate Search](/Mate_Search "Mate Search")
- [Ant](/Ant "Ant")
- [Jaglavak](/Jaglavak "Jaglavak")

# Forum Posts

- [Matant 5.03 wb2uci file question](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6500&p=30553) by [Graham Banks](/Graham_Banks "Graham Banks"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 22, 2007
- [Matant 5.04 Gauntlet for CCRL 40/40](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=69359) by Tirsa Poppins, [CCC](/CCC "CCC"), December 24, 2018

# External Links

## Chess Engine

- [Norbert's collection/Matant (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Matant%20%28Compilation%29/) by [Norbert Raimund Leisner](/Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Matant 5.04](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Matant%205.04) in [KCEC](/KCEC "KCEC")
- [Matant 5.04](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Matant%205.04) in [CCRL 40/4](/CCRL "CCRL")

## Misc

- [matant - Wiktionary](http://en.wiktionary.org/wiki/matant)
- [Mat from Wikipedia](https://en.wikipedia.org/wiki/Mat)
- [Ant from Wikipedia](https://en.wikipedia.org/wiki/Ant)
- [Langton's ant from Wikipedia](https://en.wikipedia.org/wiki/Langton%27s_ant)

:   [![LangtonsAntAnimated.gif](https://upload.wikimedia.org/wikipedia/commons/0/09/LangtonsAntAnimated.gif)](http://en.wikipedia.org/wiki/Langton%27s_ant)

- [Rammstein](/Category:Rammstein "Category:Rammstein") - [Links 2-3-4](https://en.wikipedia.org/wiki/Links_2-3-4) (2001), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [M.C. Escher - The Official Website – Recognition & Success](http://www.mcescher.com/gallery/recognition-success/)
2. [↑](#cite_ref-2) [Moebius Strip from Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_strip)
3. [↑](#cite_ref-3) [Matant\_5\_04/wac.txt](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Matant%20%28Compilation%29/v5.04/Matant_5_04/wac.txt)
4. [↑](#cite_ref-4) [II Mistrzostwa Polski Programów Szachowych - PGN](http://mpps.maciej.szmit.info/mpps-2/)

**[Up one Level](/Engines "Engines")**