# List (Program)

Source: https://www.chessprogramming.org/List_(Program)

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* List**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Leuchtturm_List_West_01.jpg/330px-Leuchtturm_List_West_01.jpg)](/File:Leuchtturm_List_West_01.jpg)

[List West](https://de.wikipedia.org/wiki/List_West) Lighthouse on [Sylt](https://en.wikipedia.org/wiki/Sylt) [[1]](#cite_note-1)

**List**,  
a chess engine by [Fritz Reul](/Fritz_Reul "Fritz Reul"), written in [C](/C "C"). The development started in 2000, and List was first released as [WinBoard](/WinBoard "WinBoard") engine **4.60** in May 2002 [[2]](#cite_note-2), and as free native [ChessBase](/ChessBase "ChessBase") engine **5.04** for the [Fritz GUI](/Fritz#FritzGUI "Fritz") in December 2002 [[3]](#cite_note-3) .

# Description

List **4.6x** is a 32-bit engine operating on [10x8 boards](/Mailbox "Mailbox"). It uses a [recursive](/Recursion "Recursion") [fail-soft](/Fail-Soft "Fail-Soft") [alpha-beta search](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table") and [quiescence search](/Quiescence_Search "Quiescence Search") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") frame with [aspiration](/Aspiration_Windows "Aspiration Windows"), and performs [fractional extensions](/Extensions#FractionalExtensions "Extensions"), [depth](/Depth "Depth") dependent [razoring](/Razoring "Razoring") and [null move search](/Null_Move "Null Move") with [fail-high reductions](/Fail-High_Reductions "Fail-High Reductions"), and [IDD](/Internal_Iterative_Deepening "Internal Iterative Deepening") [[4]](#cite_note-4) . [Dann Corbit](/Dann_Corbit "Dann Corbit"), who had seen some bit of List's [C](/C "C") source code in 2002, on the origin of List's name [[5]](#cite_note-5) :

```
The program uses many piece-lists internally, which is where the name comes from, I think. I have seen the evaluation function, which uses separate lists for each piece type.
```

# WCCC 2003

List participated at the [WCCC 2003](/WCCC_2003 "WCCC 2003") in [Graz](https://en.wikipedia.org/wiki/Graz), not represented by its author himself, but by [Erdogan Günes](/Erdogan_G%C3%BCnes "Erdogan Günes"). Fritz Reul, being circumvented with examination commitments, did not act appropriate to prove his program was not a clone, as accused due to an official protest during the tournament. As a consequence, List was disqualified after eight of eleven rounds [[6]](#cite_note-6) [[7]](#cite_note-7). In 2005, Fritz Reul was rehabilitated by the [ICGA](/ICGA "ICGA"), after List's source code was inspected by an [expert](/Chrilly_Donninger "Chrilly Donninger") approved by the ICGA [[8]](#cite_note-8), who stated List was definitely not a clone of any other program, and that it contains some new ideas in chess programming [[9]](#cite_note-9) [[10]](#cite_note-10).

# List 5.12

In January 2004, List **5.12** was released as free [UCI](/UCI "UCI") engine along with [Aristarch](/Aristarch "Aristarch") by [Stefan Zipproth](/Stefan_Zipproth "Stefan Zipproth") [[11]](#cite_note-11). Able to play [Chess960](/Chess960 "Chess960"), List further played the [Chess960CWC 2005](/Chess960CWC_2005 "Chess960CWC 2005").

# Loop List

In October 2005, Fritz Reul's new 32-bit engine dubbed **Loop List** was released commercially as [UCI](/UCI "UCI") engine [[12]](#cite_note-12) . List and Loop List further evolved to the 32-bit [Loop](/Loop_(Program) "Loop (Program)") engine as described in chapter 2 *Non-Bitboard Architectures* of Fritz Reul's Ph.D. thesis *New Architectures in Computer Chess* [[13]](#cite_note-13).

# Selected Games

[WCCC 2003](/WCCC_2003 "WCCC 2003"), round 7, List - [Brutus](/Brutus "Brutus") [[14]](#cite_note-14)

```
[Event "WCCC 2003"]
[Site "Graz, Austria"]
[Date "2003.11.26"]
[Round "7"]
[White "List"]
[Black "Brutus"]
[Result "1/2-1/2"]

1.Nc3 d5 2.e4 dxe4 3.Nxe4 Nd7 4.d4 Ngf6 5.Ng3 h5 6.Bd3 c5 7.Nf3 h4 8.Ne2 h3 
9.gxh3 a6 10.Ng5 cxd4 11.Nxd4 Nc5 12.Bc4 e6 13.Be2 Nfe4 14.Nxe4 Nxe4 15.Qd3 
f5 16.Nb3 Qf6 17.c3 Bd7 18.Be3 Bb5 19.Qd4 Bxe2 20.Qxf6 Nxf6 21.Kxe2 Rxh3 
22.Nd4 Kf7 23.Nf3 Kg8 24.Ng5 Rh6 25.Nf3 Rh5 26.Bd4 Nd5 27.Be5 a5 28.Rhg1 Rh7 
29.Rad1 Rc8 30.Rd4 Nb6 31.Bd6 Bxd6 32.Rxd6 Na4 33.Rd2 b5 34.h4 Nb6 35.Kf1 b4 
36.cxb4 axb4 37.Rd4 b3 38.axb3 Rh6 39.Kg2 Kf7 40.Ra1 Nd5 41.Rc4 Rb8 42.Ne5+ 
Kg8 43.Ra7 Rxb3 44.Nf7 Rg6+ 45.Ng5 Rb8 46.Kf1 Rf6 47.Rd4 Rg6 48.b3 Rh6 49.Kg2
Rg6 50.f3 Nf6 51.Re7 Nd5 52.Rxe6 Rxe6 53.Nxe6 Rb5 54.Kf2 Kf7 55.Nf4 Nxf4 
56.Rxf4 Rxb3 57.Rxf5+ Kg6 58.Rg5+ Kf6 59.Rc5 Kg6 60.Rc6+ Kh5 61.Kg3 Rb1 62.Rc5+
Kg6 63.Re5 Kf6 64.Ra5 Kg6 65.Kg2 Rb2+ 66.Kh3 Rb1 67.Rg5+ Kf6 68.Rc5 Kg6 1/2-1/2
```

# See also

- [Engine Rating Lists](/Engine_Rating_Lists "Engine Rating Lists")
- [Linked List](/Linked_List "Linked List")
- [Loop](/Loop_(Program) "Loop (Program)")
- [Move List](/Move_List "Move List")
- [Piece-Lists](/Piece-Lists "Piece-Lists")

# Forum Posts

## 2002

- [WB List 4.60 by Fritz Reul is available!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37172) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 07, 2002
- [List 5.04 Native-Engine available for free !!!](https://www.stmintz.com/ccc/index.php?id=269741) by CLiebert, [CCC](/CCC "CCC"), December 09, 2002
- [Re: List is crafty (with a small c)](https://www.stmintz.com/ccc/index.php?id=270338) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), December 12, 2002

## 2003

- [List 5.04](https://www.stmintz.com/ccc/index.php?id=287447) by Mike Hood, [CCC](/CCC "CCC"), March 01, 2003
- [List disqualified?](https://www.stmintz.com/ccc/index.php?id=331085) by Mike Hood, [CCC](/CCC "CCC"), November 27, 2003
- [Crafty-List question](https://www.stmintz.com/ccc/index.php?id=331183) by [Amir Ban](/Amir_Ban "Amir Ban"), [CCC](/CCC "CCC"), November 27, 2003
- [Congratulations to Fritz and List](https://www.stmintz.com/ccc/index.php?id=332346) by [José Carlos](/Jos%C3%A9_Carlos_Mart%C3%ADnez_Gal%C3%A1n "José Carlos Martínez Galán"), [CCC](/CCC "CCC"), November 30, 2003
- [I doubt that List is a crafty clone](https://www.stmintz.com/ccc/index.php?id=332736) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), December 01, 2003
- [BFF Rating List: 2 Thoughts](https://www.stmintz.com/ccc/index.php?id=339050) by Mike Hood, [CCC](/CCC "CCC"), December 29, 2003

## 2004

- [List 512 UCI und Aristarch 4.37 ready for Download :-) !!!](https://www.stmintz.com/ccc/index.php?id=345007) by Andreas Aicher, [CCC](/CCC "CCC"), January 26, 2004

:   [Is List a clone?](https://www.stmintz.com/ccc/index.php?id=345699) by [Stefan Zipproth](/Stefan_Zipproth "Stefan Zipproth"), [CCC](/CCC "CCC"), January 29, 2004
:   [For all Readers / Translation of LIST Key Point from CLiebert /](https://www.stmintz.com/ccc/index.php?id=345763) by [Rolf Tüschen](/Rolf_T%C3%BCschen "Rolf Tüschen"), [CCC](/CCC "CCC"), January 29, 2004

- [Was the List 5.12 issue ever cleared?](https://www.stmintz.com/ccc/index.php?id=351476) by [Albert Silver](/Albert_Silver "Albert Silver"), [CCC](/CCC "CCC"), February 26, 2004
- [ElChinito: A Crafty Clone](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48647) by [Paul Hunter](/index.php?title=Paul_Hunter&action=edit&redlink=1 "Paul Hunter (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 20, 2004 » [Chinito](/Chinito "Chinito"), [Crafty](/Crafty "Crafty")
- [List is NOT a Crafty clone, ... etc](https://www.stmintz.com/ccc/index.php?id=383228) by [Matthias Gemuh](/Matthias_Gemuh "Matthias Gemuh"), [CCC](/CCC "CCC"), August 21, 2004

## 2005 ...

- [Re: Chessbase must be confident that List is not a clone...](https://www.stmintz.com/ccc/index.php?id=416428) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), March 11, 2005
- [Loop List available soon](https://www.stmintz.com/ccc/index.php?id=455003) by [Fritz Reul](/Fritz_Reul "Fritz Reul"), [CCC](/CCC "CCC"), October 11, 2005

:   [Re: Loop List commercially available soon](https://www.stmintz.com/ccc/index.php?id=455043) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [CCC](/CCC "CCC"), October 11, 2005

## 2010 ...

- [List 2013 (new engine?)](http://www.talkchess.com/forum/viewtopic.php?t=47521) by [Jerry Donald](/index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](/CCC "CCC"), March 16, 2013

# External Links

## Chess Engine

- [List's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=123) (includes [Loop](/Loop_(Program) "Loop (Program)"))
- [About List](https://zipproth.com/chess/list/) from [Aristarch and List](https://zipproth.com/chess/) by [Stefan Zipproth](/Stefan_Zipproth "Stefan Zipproth")
- [List 5.12](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=List%205.12#List_5_12) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [List (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/List)

:   [List auf Sylt from Wikipedia](https://en.wikipedia.org/wiki/List_auf_Sylt)

- [List (abstract data type) from Wikipedia](https://en.wikipedia.org/wiki/List_%28abstract_data_type%29)

# References

1. [↑](#cite_ref-1) Image by [Arnoldius](https://commons.wikimedia.org/wiki/User:Arnoldius), November 09, 2016, [Category:Cultural heritage monuments in List auf Sylt - Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Cultural_heritage_monuments_in_List_auf_Sylt)
2. [↑](#cite_ref-2) [List](http://wbec-ridderkerk.nl/html/details1/List.html) from [WBEC Ridderkerk](/WBEC "WBEC")
3. [↑](#cite_ref-3) [List 5.04 Native-Engine available for free !!!](https://www.stmintz.com/ccc/index.php?id=269741) by CLiebert, [CCC](/CCC "CCC"), December 09, 2002
4. [↑](#cite_ref-4) Part of the readme, from [List](http://wbec-ridderkerk.nl/html/details1/List.html) from [WBEC Ridderkerk](/WBEC "WBEC")
5. [↑](#cite_ref-5) [Re: List is crafty (with a small c)](https://www.stmintz.com/ccc/index.php?id=270338) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), December 12, 2002
6. [↑](#cite_ref-6) [11th World Computer Chess Championship](https://www.game-ai-forum.org/icga-tournaments/tournament.php?id=2) from the [ICGA Tournament site](https://www.game-ai-forum.org/icga-tournaments/)
7. [↑](#cite_ref-7) [ICGA disqualifies chess program 'List'](http://www.chessbase.com/Home/TabId/211/PostId/4001330/icga-disqualifies-chess-program-list-.aspx), [ChessBase News](/ChessBase "ChessBase"), November 27, 2003
8. [↑](#cite_ref-8) [Re: Chessbase must be confident that List is not a clone...](https://www.stmintz.com/ccc/index.php?id=416428) by [Frank Schneider](/Frank_Schneider "Frank Schneider"), [CCC](/CCC "CCC"), March 11, 2005
9. [↑](#cite_ref-9) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2005**). *A Letter to the ICGA*. [ICGA Journal](/ICGA_Journal "ICGA Journal"), [Vol. 28, No. 1](http://ilk.uvt.nl/icga/journal/pdf/toc28-1.pdf) (pdf)
10. [↑](#cite_ref-10) [David Levy](/David_Levy "David Levy") (**2005**). *Cancellation of Suspension*. [ICGA Journal](/ICGA_Journal "ICGA Journal"), [Vol. 28, No. 1](http://ilk.uvt.nl/icga/journal/pdf/toc28-1.pdf) (pdf)
11. [↑](#cite_ref-11) [List 512 UCI und Aristarch 4.37 ready for Download :-) !!!](https://www.stmintz.com/ccc/index.php?id=345007) by Andreas Aicher, [CCC](/CCC "CCC"), January 26, 2004
12. [↑](#cite_ref-12) [Re: Loop List commercially available soon](https://www.stmintz.com/ccc/index.php?id=455043) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [CCC](/CCC "CCC"), October 11, 2005
13. [↑](#cite_ref-13) [Fritz Reul](/Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. thesis
14. [↑](#cite_ref-14) [Graz 2003 - Chess - Round 7 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=2&round=7&id=5)

**[Up one level](/Engines "Engines")**