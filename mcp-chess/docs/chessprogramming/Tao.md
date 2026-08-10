# Tao

Source: https://www.chessprogramming.org/Tao

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Tao**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Yin_and_Yang_symbol.svg/330px-Yin_and_Yang_symbol.svg.png)](/File:Yin_and_Yang_symbol.svg)

[Taoist](https://en.wikipedia.org/wiki/Taoism) [Taijitu](https://en.wikipedia.org/wiki/Taijitu) [[1]](#cite_note-1)

**Tao**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and later [UCI](/UCI "UCI") [[2]](#cite_note-2) compliant chess engine by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), famous for its attacking playing style encouraged by an [opening book](/Opening_Book "Opening Book") cooked by [Cock de Gorter](/Cock_de_Gorter "Cock de Gorter") [[3]](#cite_note-3). Tao played the [WMCCC 2001](/WMCCC_2001 "WMCCC 2001") in [Maastricht](https://en.wikipedia.org/wiki/Maastricht), six [Dutch Open Computer Chess Championships](/Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship") and four [International CSVN Tournaments](/International_CSVN_Tournament "International CSVN Tournament") from [2000](/DOCCC_2000 "DOCCC 2000") until [2005](/DOCCC_2005 "DOCCC 2005"), and three [CCT Tournaments](/CCT_Tournaments "CCT Tournaments").

# Description

Tao is a [bitboard](/Bitboards "Bitboards") engine that uses [PVS](/Principal_Variation_Search "Principal Variation Search") without root [aspiration windows](/Aspiration_Windows "Aspiration Windows"). Tao applies [incremental updated](/Incremental_Updates "Incremental Updates") [attacks](/Attack_and_Defend_Maps "Attack and Defend Maps"), incremental [move generation](/Move_Generation "Move Generation"), uses [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") to prune losing [captures](/Captures "Captures"), and [extends](/Extensions "Extensions") [checks](/Check_Extensions "Check Extensions"), [one reply](/One_Reply_Extensions "One Reply Extensions"), [recaptures](/Recapture_Extensions "Recapture Extensions") and [mate threats](/Mate_Threat_Extensions "Mate Threat Extensions") along with [null move pruning](/Null_Move_Pruning "Null Move Pruning") of [R=2](/Depth_Reduction_R "Depth Reduction R") [[4]](#cite_note-4).
It further considers [check](/Check "Check") giving moves in [quiescence search](/Quiescence_Search "Quiescence Search") [[5]](#cite_note-5). Version 5.5 uses [evaluation](/Evaluation "Evaluation") [tuning](/Automated_Tuning "Automated Tuning") based on [temporal differences](/Temporal_Difference_Learning "Temporal Difference Learning") [[6]](#cite_note-6).

# Photos & Games

[![Hamstra32.jpg](/images/4/40/Hamstra32.jpg)](http://old.csvn.nl/gallery21.html)

[DOCCC 2004](/DOCCC_2004 "DOCCC 2004"): [Elke Van Vlierberghe](/Elke_Van_Vlierberghe "Elke Van Vlierberghe") and [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), Tao - [Deep Sjeng](/Deep_Sjeng "Deep Sjeng") [[7]](#cite_note-7)

```
[Event "DOCCC 2004"]
[Site "Leiden Ned"]
[Date "2004.10.17"]
[Round "06"]
[White "Tao"]
[Black "Deep Sjeng"]
[Result "1/2-1/2"]

1.c3 e5 2.e4 d5 3.Qa4+ Nd7 4.exd5 Ngf6 5.c4 Bc5 6.Nc3 O-O 7.d3 Nb6 8.Qd1 Qe7 9.Bg5 h6 
10.Bxf6 Qxf6 11.Nf3 Bd4 12.Be2 Qg6 13.O-O Bh3 14.Ne1 Bd7 15.Nc2 Bh3 16.Bf3 Bxc3 17.bxc3 
Bf5 18.Bh5 Qh7 19.Ne1 e4 20.dxe4 Bxe4 21.Qd4 Rfe8 22.f3 Bf5 23.Rd1 Rad8 24.Rd2 c5 25.Qxc5 
Rc8 26.Qb5 Nxc4 27.Rd4 Ne3 28.Rf2 g6 29.d6 Nd5 30.Rxd5 Rxe1+ 31.Rf1 Rxf1+ 32.Kxf1 Be6 
33.d7 Rd8 34.Qa5 b6 35.Qxa7 Qg7 36.Qxb6 Qf8 37.Rd4 gxh5 38.a4 Qe7 39.Qc7 Rxd7 40.Rxd7 Bxd7 
41.c4 Qe6 42.a5 Bc8 43.Qd8+ Kg7 44.Qd4+ Kg6 45.Kf2 Ba6 46.c5 h4 47.Qxh4 Qe2+ 48.Kg3 Qe5+ 
49.Qf4 Qxc5 50.Qe4+ Kg7 51.Qg4+ Kf8 52.Qf4 Qxa5 53.Qxh6+ Kg8 54.h3 Qe5+ 55.f4 Qe1+ 56.Kh2 
Bd3 57.Qg5+ Bg6 58.Qd8+ Kg7 59.Qd4+ Kh7 60.Qc5 Qd2 61.Qe5 Qc2 62.Qf6 Qf2 63.Qe5 Kg8 64.Qg5 
Kg7 65.Qe5+ f6 66.Qe7+ Bf7 67.Qe4 Kh6 68.Qf5 Qb2 69.Qd3 Bg6 70.Qd8 Kg7 71.Qd7+ Bf7 72.Qg4+ 
Kh6 73.Qf5 Bc4 74.Qe4 Ba2 75.Qf5 Bb3 76.Kg3 Qd4 77.Kh4 Bf7 78.g3 Bg6 79.Qc8 Kg7 80.Qc1 Bf5 
81.Qe1 Kf7 82.Qe2 Be6 83.Qh5+ Kf8 84.Qh8+ 1/2-1/2
```

# Publications

- [Raymond Smullyan](/Raymond_Smullyan "Raymond Smullyan") (**1977**). *The Tao Is Silent*. [HarperOne](https://en.wikipedia.org/wiki/HarperCollins)
- [Raymond Smullyan](/Raymond_Smullyan "Raymond Smullyan") (**1977**). *[Is God a Taoist?](http://www.mit.edu/people/dpolicar/writing/prose/text/godTaoist.html)* [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")

# Forum Posts

- [Tao](https://www.stmintz.com/ccc/index.php?id=72400) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), October 08, 1999
- [Tao 4.3 (won against Quest, Dutch-ch 2000) is available !](https://www.stmintz.com/ccc/index.php?id=134675) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), October 23, 2000
- [Some questions on Tao](https://www.stmintz.com/ccc/index.php?id=147907) by [Peter Berger](/Peter_Berger "Peter Berger"), [CCC](/CCC "CCC"), January 03, 2001
- [Tao update](https://www.stmintz.com/ccc/index.php?id=149645) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), January 12, 2001
- [Tao at ICC](https://www.stmintz.com/ccc/index.php?id=208102) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), January 17, 2002
- [CCT4 Tao/Quark](https://www.stmintz.com/ccc/index.php?id=210007) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), January 26, 2002 » [CCT4](/CCT4 "CCT4"), [Quark](/Quark "Quark")
- [About Tao 5.2](https://www.stmintz.com/ccc/index.php?id=242621) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), July 25, 2002

# External Links

## Chess

- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Tao's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=125)
- [Tao 5.6](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Tao%205.6#Tao_5_6) in [CCRL 40/40](/CCRL "CCRL")
- [Tao 5.6](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Tao%205.6) in [KCEC](/KCEC "KCEC")

## Misc

- [Tao from Wikipedia](https://en.wikipedia.org/wiki/Tao)
- [Tao (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Tao_%28disambiguation%29)
- [Taoism from Wikipedia](https://en.wikipedia.org/wiki/Taoism)
- [Yin and yang from Wikipedia](https://en.wikipedia.org/wiki/Yin_and_yang)
- [The United Jazz + Rock Ensemble](/Category:The_United_Jazz_%2B_Rock_Ensemble "Category:The United Jazz + Rock Ensemble") - [Yin](https://www.allmusic.com/song/yin-mt0012147462), [Teamwork](https://www.allmusic.com/album/teamwork-mw0000062413) (1978), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Eberhard Weber](/Category:Eberhard_Weber "Category:Eberhard Weber"), [Jon Hiseman](/Category:Jon_Hiseman "Category:Jon Hiseman"), [Barbara Thompson](/Category:Barbara_Thompson "Category:Barbara Thompson"), [Volker Kriegel](/Category:Volker_Kriegel "Category:Volker Kriegel"), [Wolfgang Dauner](/Category:Wolfgang_Dauner "Category:Wolfgang Dauner"),
:   [Charlie Mariano](/Category:Charlie_Mariano "Category:Charlie Mariano"), [Albert Mangelsdorff](/Category:Albert_Mangelsdorff "Category:Albert Mangelsdorff"), [Ian Carr](/Category:Ian_Carr "Category:Ian Carr"), [Ack van Rooyen](https://en.wikipedia.org/wiki/Ack_van_Rooyen)

# References

1. [↑](#cite_ref-1) [Yin and yang from Wikipedia](https://en.wikipedia.org/wiki/Yin_and_yang)
2. [↑](#cite_ref-2) [About Tao 5.2](https://www.stmintz.com/ccc/index.php?id=242621) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), July 25, 2002
3. [↑](#cite_ref-3) [Shredder and Ruffian lead in Leiden](http://www.chessbase.com/newsdetail.asp?newsid=1599) by [Eric van Reem](/Eric_van_Reem "Eric van Reem") and [Theo van der Storm](/Theo_van_der_Storm "Theo van der Storm"), [ChessBase](/ChessBase "ChessBase"), April 24, 2004 » [ICT 2004](/ICT_2004 "ICT 2004")
4. [↑](#cite_ref-4) [Tao](https://www.stmintz.com/ccc/index.php?id=72400) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), October 08, 1999
5. [↑](#cite_ref-5) [Re: Tao at ICC](https://www.stmintz.com/ccc/index.php?id=208110) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), January 17, 2002
6. [↑](#cite_ref-6) [Tao update](https://www.stmintz.com/ccc/index.php?id=149645) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), January 12, 2001
7. [↑](#cite_ref-7) [24th Open Dutch Computer-Chess Championship 2004 Photo Gallery](http://old.csvn.nl/gallery21.html)

**[Up one Level](/Engines "Engines")**