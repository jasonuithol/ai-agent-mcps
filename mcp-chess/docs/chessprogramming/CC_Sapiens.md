# CC Sapiens

Source: https://www.chessprogramming.org/CC_Sapiens

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* CC Sapiens**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Wither_-_Emblem_Wisdom.jpg/330px-Wither_-_Emblem_Wisdom.jpg)](/File:Wither_-_Emblem_Wisdom.jpg)

Wisdom Emblem [[1]](#cite_note-1)

**CC Sapiens**, (Chess Computer Sapiens)  
a computer chess project headed by [Mikhail Botvinnik](/Mikhail_Botvinnik "Mikhail Botvinnik") during the early 90s after the [dissolution of the Soviet Union](https://en.wikipedia.org/wiki/Dissolution_of_the_Soviet_Union). Further contributors, specially on the application of [economic planning](https://en.wikipedia.org/wiki/Economic_planning) (EC Sapiens) were mathematician [Vasily Vladimirov](/Vasily_Vladimirov "Vasily Vladimirov"), and the economists [Evgeniĭ Dmitrievich Cherevik](/Evgeni%C4%AD_Dmitrievich_Cherevik "Evgeniĭ Dmitrievich Cherevik") and [Vitaly Vygodsky](/Vitaly_Vygodsky "Vitaly Vygodsky").
CC Sapiens was a trial to resurrect the [Pioneer](/Pioneer "Pioneer") project with the aim to develop a chess program to model a Chess Master's Mind - ultimately terminated with Botvinnik's death in May 1995. Botvinnik's attempt to demonstrate the ability of CC Sapiens on three selected positions with narrow [search trees](/Search_Tree "Search Tree") in [ICCA Journal, Vol. 16, No. 2](/ICGA_Journal#16_2 "ICGA Journal") [[2]](#cite_note-2) was criticized by [Hans Berliner](/Hans_Berliner "Hans Berliner") [[3]](#cite_note-3) [[4]](#cite_note-4) and Botvinnik's old chess rival [David Bronstein](/David_Bronstein "David Bronstein") [[5]](#cite_note-5), due to obvious flaws and allegation of forged results [[6]](#cite_note-6).

# A Muse A-Musing

Excerpt of the Editorial, [ICCA Journal, Vol. 16, No. 3](/ICGA_Journal#16_3 "ICGA Journal") by [Bob Herschberg](/Bob_Herschberg "Bob Herschberg") and [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik") [[7]](#cite_note-7):

```
Controversy is not only not harmful, it is the only way to recognize the eventual truth which is fated to have its origin as a dispute between heretics and the current orthodoxy, the latter only recently absolved itself from the charge of heresy. It is therefore that we welcome an unusual amount of controversy arising out of the last issue of our Journal. Whether it is Botvinnik being challenged by Berliner, or by his former comrade-in-arms, Bronstein, whether it is one of your Editors taking up the cudgels against proponents of Chinese Chess-by-program, a double heresy, - all are welcome. Their discussions may not be among the most edifying of exchanges - well, neither was the language in which heresy was discussed and orthodoxy arrived at on many famous occasions, Church counsels among them.
```

```
Yet, we maintain: the discussion, even the confrontation is helpful and conducive to the health of computer chess. Following this belief, we feel a duty to extend the hospitality of our columns generously to all heretics. Caïssa, still smiling, will be amused.
```

# Kasparov - Ribli

The first one of Botvinnik's *Three Positions* [[8]](#cite_note-8) and most criticized analysis is from the [Garry Kasparov](/Garry_Kasparov "Garry Kasparov") vs. [Zoltán Ribli](https://en.wikipedia.org/wiki/Zolt%C3%A1n_Ribli) game [[9]](#cite_note-9), [Skellefteå](https://en.wikipedia.org/wiki/Skellefte%C3%A5) [World Cup 1989](https://en.wikipedia.org/wiki/1989_in_chess#Grandmasters_Association_World_Cup) [[10]](#cite_note-10), after 26.Rxb5 Bxe3 [[11]](#cite_note-11) [[12]](#cite_note-12):

|  |
| --- |
|                                                                                         ♜♚       ♟♟♟ ♟ ♕ ♟     ♖       ♛            ♝ ♙  ♙  ♖♙♙ ♙       ♔ |

```
5rk1/5ppp/p1Q1p3/1R6/q7/4b1P1/P2RPP1P/6K1 w - -
```

CC Sapiens produced an analysis of a mere 18 nodes, and determined that this position is a win for White with Rd8. Botvinnik gives one variation with 1.Rd8! Qxb5 2.Qd6! Bxf2 3.Kxf2 Re8 4.Qe7, satisfying the stated goal, but missed to consider other alternatives of Black's first (1... Bxf2) and third move. Berliner: "Presumably the beckoning 3. ...Qf5+ is dismissed since it can't possibly lead to a win for Black. Botvinnik knows that, and I know that, but can a computer program figure this out without searching?". The blunder 4.Qe7 was apparently discovered by Botvinnik or his team just before press time, given in a footnote, but due to mistake of the editors, three pages apart.

[Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu"), who already analyzed the position with [Deep Thought](/Deep_Thought "Deep Thought") along with [Garry Kasparov](/Garry_Kasparov "Garry Kasparov") in 1990, posted the winning lines of 3. ... Re8 4.a4 or more difficult 3 ...Qf5+! 4.Kg1! in [rgc](/Computer_Chess_Forums "Computer Chess Forums") [[13]](#cite_note-13) as reply to Berliner's [B\*](/B* "B*") [HiTech](/HiTech "HiTech") analysis with the wrong 3 ...Qf5+! 4.Kg2 line [[14]](#cite_note-14). As admitted by Berliner in his *Playing Computer Chess in the Human Style* [ICCA](/ICCA "ICCA") correspondence [[15]](#cite_note-15), it was possible to identify a serious bug in B\* HiTech's [search](/Search "Search") algorithm thanks to Hsu's information.

# Solving Shannon's Problem

## Abstract

from *Solving Shannon's Problem: Ways and Means*, [Advances in Computer Chess 7](/Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), July 01, 1993 [[16]](#cite_note-16) [[17]](#cite_note-17):

```
A proposal by Shannon (1950) indicated two styles of constructing computer-chess programs: brute-force and following the experience of chess masters. Of the first style examples abound, of the second only CC Sapiens, as yet incomplete, exists. From the experience with CC Sapiens and its economical analogue, it is confidently predicted that methods based on making the computer understand the problem may well gain the upper hand, both in computer chess and in high-dimensional search programs related to it, following the master's style.
```

## Chains

Excerpt from *Solving Shannon's Problem: Ways and Means*:

```
In the program CC Sapiens, the intermediate step of the model is identified with the analysis of a chain of pieces. An attacking piece L0 and an attacked piece L2 constitute the basis of the chain; the remaining pieces oppose or support it. Whereas a chain of pieces connects material entities, there is also, as an intermediate step, a positional chain. The latter is composed of links relating squares to specific other squares, such as holes and weak squares, and to properties enjoyed by the totality of squares and their subsets, such as ranks, files and diagonals.
```

# See also

- [Pioneer](/Pioneer "Pioneer")

# Selected Publications

[[18]](#cite_note-18)

- [Mikhail Botvinnik](/Mikhail_Botvinnik "Mikhail Botvinnik") (**1993**). *Three Positions*. [ICCA Journal, Vol. 16, No. 2](/ICGA_Journal#16_2 "ICGA Journal")
- [Bob Herschberg](/Bob_Herschberg "Bob Herschberg"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik") (**1993**). *[A Muse A-Musing](http://ilk.uvt.nl/icga/journal/contents/node4.html)*. (Editorial) [ICCA Journal, Vol. 16, No. 3](/ICGA_Journal#16_3 "ICGA Journal")
- [Hans Berliner](/Hans_Berliner "Hans Berliner") (**1993**). *Playing Computer Chess in the Human Style*. [ICCA Journal, Vol. 16, No. 3](/ICGA_Journal#16_3 "ICGA Journal")
- [David Bronstein](/David_Bronstein "David Bronstein") (**1993**). *Mimicking Human Oversight*. [ICCA Journal, Vol. 16, No. 3](/ICGA_Journal#16_3 "ICGA Journal")
- [Mikhail Botvinnik](/Mikhail_Botvinnik "Mikhail Botvinnik"), [Evgeniĭ Dmitrievich Cherevik](/Evgeni%C4%AD_Dmitrievich_Cherevik "Evgeniĭ Dmitrievich Cherevik"), [Vasily Vladimirov](/Vasily_Vladimirov "Vasily Vladimirov"), [Vitaly Vygodsky](/Vitaly_Vygodsky "Vitaly Vygodsky") (**1994**). *Solving Shannon's Problem: Ways and Means*. [Advances in Computer Chess 7](/Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), English translation by Igor Botvinnik [[19]](#cite_note-19) [[20]](#cite_note-20) and the Editors

# Forum Posts

- [Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/83d0wqxy-VoJ) by [Hans Berliner](/Hans_Berliner "Hans Berliner"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 9, 1993

:   [Re: Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/nZWR2BkOlFsJ) by [Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 10, 1993

- [Botvinnik article](https://groups.google.com/d/msg/rec.games.chess.computer/ZWQ5ZwvXx_s/EgXPrz6jZFYJ) by [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 23, 1996

:   [Re: Botvinnik article](https://groups.google.com/d/msg/rec.games.chess.computer/ZWQ5ZwvXx_s/Cozl-N5kZkMJ) by [Peter Gillgasch](/Peter_Gillgasch "Peter Gillgasch"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 23, 1996

# External Links

## Chess Program

- [Hans Berliner against Mikhail Botvinnik](http://atimopheyev.narod.ru/AfterPIONEER/info/PIONEER/2-Berliner.htm) by [Alexander Timofeev](/Alexander_Timofeev "Alexander Timofeev")

## Misc

- [sapiens - Wiktionary](https://en.wiktionary.org/wiki/sapiens)
- [Sapiens from Wikipedia](https://en.wikipedia.org/wiki/Sapiens)
- [Sapience from Wikipedia](https://en.wikipedia.org/wiki/Wisdom#Sapience)
- [Homo sapiens from Wikipedia](https://en.wikipedia.org/wiki/Homo_sapiens)
- [RoboSapien from Wikipedia](https://en.wikipedia.org/wiki/RoboSapien)
- [FemiSapien from Wikipedia](https://en.wikipedia.org/wiki/FemiSapien)
- [Endgame – the mating habits of homo sapiens](http://en.chessbase.com/post/endgame-the-mating-habits-of-homo-sapiens) | [ChessBase News](/ChessBase "ChessBase"), April 08, 2004
- [Nuno Ferreira Septeto](https://nunoferreirajazz.wordpress.com/) - Cromo Sapiens, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Wisdom Emblem](https://commons.wikimedia.org/wiki/File:Wither_-_Emblem_Wisdom.jpg), from [George Wither](https://en.wikipedia.org/wiki/George_Wither) (**1635**). *[A Collection of Emblemes Anciente and Moderne](https://archive.org/details/collectionofembl00withe)*. London, [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Wisdom from Wikipedia.simple](http://simple.wikipedia.org/wiki/Wisdom): The words of this old print read, in modern English: 'He over all the stars does reign That unto wisdom can attain', in other words: 'Whoever can become wise will rule over everything'.
2. [↑](#cite_ref-2) [Mikhail Botvinnik](/Mikhail_Botvinnik "Mikhail Botvinnik") (**1993**). *Three Positions*. [ICCA Journal, Vol. 16, No. 2](/ICGA_Journal#16_2 "ICGA Journal")
3. [↑](#cite_ref-3) [Hans Berliner](/Hans_Berliner "Hans Berliner") (**1993**). *Playing Computer Chess in the Human Style*. [ICCA Journal, Vol. 16, No. 3](/ICGA_Journal#16_3 "ICGA Journal")
4. [↑](#cite_ref-4) [Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/83d0wqxy-VoJ) by [Hans Berliner](/Hans_Berliner "Hans Berliner"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 9, 1993
5. [↑](#cite_ref-5) [David Bronstein](/David_Bronstein "David Bronstein") (**1993**). *Mimicking Human Oversight*. [ICCA Journal, Vol. 16, No. 3](/ICGA_Journal#16_3 "ICGA Journal")
6. [↑](#cite_ref-6) [Botvinnik article](https://groups.google.com/d/msg/rec.games.chess.computer/ZWQ5ZwvXx_s/EgXPrz6jZFYJ) by [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 23, 1996
7. [↑](#cite_ref-7)  [Bob Herschberg](/Bob_Herschberg "Bob Herschberg"), [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik") (**1993**). *[A Muse A-Musing](http://ilk.uvt.nl/icga/journal/contents/node4.html)*. (Editorial) [ICCA Journal, Vol. 16, No. 3](/ICGA_Journal#16_3 "ICGA Journal")
8. [↑](#cite_ref-8) [Mikhail Botvinnik](/Mikhail_Botvinnik "Mikhail Botvinnik") (**1993**). *Three Positions*. [ICCA Journal, Vol. 16, No. 2](/ICGA_Journal#16_2 "ICGA Journal")
9. [↑](#cite_ref-9) [Garry Kasparov vs Zoltan Ribli (1989)](http://www.chessgames.com/perl/chessgame?gid=1070471) from [chessgames.com](http://www.chessgames.com/index.html)
10. [↑](#cite_ref-10) [Skelleftea World Cup 1989](http://www.chessgames.com/perl/chesscollection?cid=1015939) from [chessgames.com](http://www.chessgames.com/index.html)
11. [↑](#cite_ref-11) [Kasparov-Ribli, 1989](https://www.stmintz.com/ccc/index.php?id=46260) by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland"), [CCC](/CCC "CCC"), March 19, 1999
12. [↑](#cite_ref-12) [Test position ==> Kasparov-Ribli,1989](https://www.stmintz.com/ccc/index.php?id=201865) by [José Antônio Fabiano Mendes](/Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](/CCC "CCC"), December 14, 2001
13. [↑](#cite_ref-13) [Re: Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/nZWR2BkOlFsJ) by [Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 10, 1993
14. [↑](#cite_ref-14) [Kasparov missed Beautiful win; Botvinnik's Program muffs analysis](https://groups.google.com/d/msg/rec.games.chess/xsgbuxorOZ8/83d0wqxy-VoJ) by [Hans Berliner](/Hans_Berliner "Hans Berliner"), [rec.games.chess](/Computer_Chess_Forums "Computer Chess Forums"), July 9, 1993
15. [↑](#cite_ref-15)  [Hans Berliner](/Hans_Berliner "Hans Berliner") (**1993**). *Playing Computer Chess in the Human Style*. [ICCA Journal, Vol. 16, No. 3](/ICGA_Journal#16_3 "ICGA Journal")
16. [↑](#cite_ref-16)  [Mikhail Botvinnik](/Mikhail_Botvinnik "Mikhail Botvinnik"), [Evgeniĭ Dmitrievich Cherevik](/Evgeni%C4%AD_Dmitrievich_Cherevik "Evgeniĭ Dmitrievich Cherevik"), [Vasily Vladimirov](/Vasily_Vladimirov "Vasily Vladimirov"), [Vitaly Vygodsky](/Vitaly_Vygodsky "Vitaly Vygodsky") (**1994**). *Solving Shannon's Problem: Ways and Means*. [Advances in Computer Chess 7](/Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
17. [↑](#cite_ref-17) [Claude Shannon](/Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](https://www.pi.infn.it/~carosi/chess/shannon.txt)*.
18. [↑](#cite_ref-18) [ICGA Reference Database](/ICGA_Journal#RefDB "ICGA Journal")
19. [↑](#cite_ref-19) [Igor Botvinnik Has Passed Away](http://chess-news.ru/en/node/5190) | [chess-news.ru](http://chess-news.ru/en), December 06, 2011
20. [↑](#cite_ref-20) [Interview mit Igor Botvinnik](http://de.chessbase.com/post/interview-mit-igor-botvinnik), [ChessBase](/ChessBase "ChessBase"), January 04, 2007 (German)

**[Up one Level](/Engines "Engines")**