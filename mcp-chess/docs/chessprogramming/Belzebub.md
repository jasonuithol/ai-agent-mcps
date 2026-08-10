# Belzebub

Source: https://www.chessprogramming.org/Belzebub

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Belzebub**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Beelzebub.png/330px-Beelzebub.png)](/File:Beelzebub.png)

Beelzebub [[1]](#cite_note-1)

**Belzebub**,  
a [WinBoard](/WinBoard "WinBoard") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") written by [Radosław Kamowski](/Rados%C5%82aw_Kamowski "Radosław Kamowski") in [Java](/Java "Java"), released in May 2002 as free chess game for mobile phones. Belzebub played the first and second [Polish Computer Chess Championship](/Polish_Computer_Chess_Championship "Polish Computer Chess Championship"). After finishing last at the [PCCC 2002](/PCCC_2002 "PCCC 2002"), Belzebub became runner-up of the uniform category at the [PCCC 2003](/PCCC_2003 "PCCC 2003") behind [Tytan](/Tytan "Tytan").

# Etymology

Belzebub is the Polish diction of [Beelzebub](https://en.wikipedia.org/wiki/Beelzebub) or Baalzebûb, [Arabic](https://en.wikipedia.org/wiki/Arabic_language): بعل الذباب‎, Ba‘al az-Zubab, literally "Lord of the Flies", a [Semitic](https://en.wikipedia.org/wiki/Semitic_people) [deity](https://en.wikipedia.org/wiki/Deity) that was worshiped in the [Philistine](https://en.wikipedia.org/wiki/Philistines) city of [Ekron](https://en.wikipedia.org/wiki/Ekron). In later [Christian](https://en.wikipedia.org/wiki/Christian) and [Biblical](https://en.wikipedia.org/wiki/Bible) sources, Beelzebub is referred to as another name for [Devil](https://en.wikipedia.org/wiki/Devil) [[2]](#cite_note-2) [[3]](#cite_note-3) [[4]](#cite_note-4). In [Christian demonology](https://en.wikipedia.org/wiki/Christian_demonology), [classified](https://en.wikipedia.org/wiki/Classification_of_demons) by [Peter Binsfeld](https://en.wikipedia.org/wiki/Peter_Binsfeld) in *Tractatus de confessionibus maleficorum & Sagarum an et quanta fides iis adhibenda sit*, 1589 [[5]](#cite_note-5), Beelzebub is one of the [seven Princes of Hell](https://en.wikipedia.org/wiki/Seven_princes_of_Hell#Binsfeld.27s_classification_of_demons) [[6]](#cite_note-6) associated with [gluttony](https://en.wikipedia.org/wiki/Gluttony), one of the [seven deadly sins](https://en.wikipedia.org/wiki/Seven_deadly_sins#Gluttony). Gluttony also occurs in chess [[7]](#cite_note-7) or even more in computer chess with basically [material](/Material "Material") based [evaluation](/Evaluation "Evaluation"), i.e. grabbing unimportant pawns with the queen, ignoring [development](/Development "Development") and [king safety](/King_Safety "King Safety").

# Description

## Search

Belzebub uses plain [8x8 board](/8x8_Board "8x8 Board") [arrays](/Array "Array"), and applies [alpha-beta](/Alpha-Beta "Alpha-Beta") with [null move pruning](/Null_Move_Pruning "Null Move Pruning") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](/Aspiration_Windows "Aspiration Windows"). [Move ordering](/Move_Ordering "Move Ordering") considers the [principal variation](/Principal_Variation "Principal Variation") from previous iteration maintained in a [triangular PV-table](/Triangular_PV-Table "Triangular PV-Table"), [MVV-LVA](/MVV-LVA "MVV-LVA") for [captures](/Captures "Captures") and [killer-](/Killer_Heuristic "Killer Heuristic") and [history heuristic](/History_Heuristic "History Heuristic") otherwise.

## Repetitions

Like [TSCP](/TSCP "TSCP"), Belzebub uses following algorithm to detect [repetitions](/Repetitions "Repetitions"), credited to [John Stanback](/John_Stanback "John Stanback"), originated from [SCP](/SCP "SCP") and his [GNU Chess](/GNU_Chess "GNU Chess") versions [[8]](#cite_note-8). However, it may detect false repetitions in case of exchanging two unequal pieces [[9]](#cite_note-9). Further, the routine keeps the [garbage collector](https://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29) busy by allocating the integer array each call, even if the [fifty move counter](/Fifty-move_Rule "Fifty-move Rule") is less or equal three.

```
/* reps() returns the number of times that the current
   position has been repeated. Thanks to John Stanback
   for this clever algorithm. */
int reps() {
   int i;
   int b[] = new int[64];
   int c = 0;
   /* count of squares that are different from
     the current position */
   int r = 0; /* number of repetitions */
   /* is a repetition impossible? */
   if (fifty <= 3) {
      return 0;
   }

   /* loop through the reversible moves */
   int m = hply - fifty - 1;
   if (m < 0) {
      m = 0;
   } // gdy gra jest wznawiana to tablica hist jest pusta
   for (i = hply - 1; i >= m; --i) {
      if (++b[hist_from[i]] == 0) {
         --c;
      } else {
         ++c;
      }
      if (--b[hist_to[i]] == 0) {
         --c;
      } else {
         ++c;
      }
      if (c == 0) {
         ++r;
      }
   }
   return r;
}
```

# Selected Games

[PCCC 2003](/PCCC_2003 "PCCC 2003") - Belzebub - [Robin](/index.php?title=Robin_PL&action=edit&redlink=1 "Robin PL (page does not exist)") [[10]](#cite_note-10)

```
[Event "PCCC 2003"]
[Site " Łódź, Poland"]
[Date "2003.08.?"]
[Round "?"]
[White "Belzebub"]
[Black "Robin"]
[Result "1-0"]

1.Nf3 Nf6 2.e3 e6 3.Bb5 Be7 4.d4 O-O 5.O-O d5 6.Re1 Bd7 7.Bd3 c5 8.Bd2 Nc6 
9.Nc3 Rc8 10.Bb5 Ne4 11.a4 Nxd2 12.Qxd2 cxd4 13.exd4 Bb4 14.Re3 Qa5 15.Qd1 
a6 16.Bxc6 Bxc6 17.Ne2 Be8 18.c3 Be7 19.b3 Bd8 20.Re5 Bd7 21.Rh5 f6 22.Qc2 
g6 23.Rh6 Re8 24.Nh4 Kg7 25.Rxh7+ Kxh7 26.Qxg6+ Kh8 27.Qf7 Rg8 28.Nf4 Rg7 
29.Nhg6+ Kh7 30.Nf8+ Kh8 31.N4g6+ Rxg6 32.Nxg6# 1-0
```

# External Links

## Chess Engine

- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Belzebub 0.67](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Belzebub%200.67) in [CCRL 40/4](/CCRL "CCRL")

## Demonology

- [Belzebub from Wikipedia.pl](http://pl.wikipedia.org/wiki/Belzebub) (Polish)
- [Beelzebub from Wikipedia](https://en.wikipedia.org/wiki/Beelzebub)
- [Baalzebub (Beelzebub) - Hastings' Dictionary of the Bible](http://www.studylight.org/dic/hdb/view.cgi?n=683)
- [Baal (demon) from Wikipedia](https://en.wikipedia.org/wiki/Baal_%28demon%29) [[11]](#cite_note-11)
- [Classification of demons from Wikipedia](https://en.wikipedia.org/wiki/Classification_of_demons)
- [List of demons in the Ars Goetia from Wikipedia](https://en.wikipedia.org/wiki/List_of_demons_in_the_Ars_Goetia)

## Misc

- [Beelzebub (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Beelzebub_%28disambiguation%29)
- [Beelzebub - Final Fantasy Encyclopaedia](http://ffe.hendersongdi.com/b/beelzebub.html)
- [Beelzebub (manga) from Wikipedia](https://en.wikipedia.org/wiki/Beelzebub_%28manga%29)
- [Beelzebub's Tales to His Grandson - Wikipedia](https://en.wikipedia.org/wiki/Beelzebub%27s_Tales_to_His_Grandson)
- [Baal from Wikipedia](https://en.wikipedia.org/wiki/Baal)
- [Fly from Wikipedia](https://en.wikipedia.org/wiki/Fly)

:   [Drosophila melanogaster from Wikipedia](https://en.wikipedia.org/wiki/Drosophila_melanogaster)

- [Baalzebul (Dungeons & Dragons) from Wikipedia](https://en.wikipedia.org/wiki/Baalzebul_%28Dungeons_%26_Dragons%29)
- [Lord of the Flies from Wikipedia](https://en.wikipedia.org/wiki/Lord_of_the_Flies)
- [Lord of the Flies (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Lord_of_the_Flies_%28disambiguation%29)
- [Bruford](https://en.wikipedia.org/wiki/Bruford#Solo_career) - [Beelzebub](https://en.wikipedia.org/wiki/Feels_Good_to_Me) ([Rock Goes to College, 1979](https://en.wikipedia.org/wiki/Rock_Goes_to_College#Original_Broadcasts_1979_.288_episodes.29), [BBC](https://en.wikipedia.org/wiki/BBC) series), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Allan Holdsworth](/Category:Allan_Holdsworth "Category:Allan Holdsworth"), [Jeff Berlin](https://en.wikipedia.org/wiki/Jeff_Berlin), [Dave Stewart](https://en.wikipedia.org/wiki/Dave_Stewart_%28keyboardist%29) and [Bill Bruford](/Category:Bill_Bruford "Category:Bill Bruford")

# References

1. [↑](#cite_ref-1) Beelzebub as depicted in [Collin de Plancy's](https://en.wikipedia.org/wiki/Collin_de_Plancy) [Dictionnaire Infernal](https://en.wikipedia.org/wiki/Dictionnaire_Infernal) (Paris, 1863)
2. [↑](#cite_ref-2) [Catholic Encyclopedia: Beelzebub](http://www.newadvent.org/cathen/02388c.htm)
3. [↑](#cite_ref-3) [New Advent Bible: Matthew 12:24-29](http://www.newadvent.org/bible/mat012.htm#vrs24)
4. [↑](#cite_ref-4) [New Advent Bible: Luke 11:15-22](http://www.newadvent.org/bible/luk011.htm#vrs15)
5. [↑](#cite_ref-5) [historicum.net: Traktate: Binsfeld (Themenschwerpunkt Hexenverfolgung)](http://www.historicum.net/themen/hexenforschung/quellen/traktate/binsfeld/)
6. [↑](#cite_ref-6) [Beelzebub from Wikipedia](https://en.wikipedia.org/wiki/Beelzebub)
7. [↑](#cite_ref-7) [Reykjavik Open 2013. Fifth round. The advantages of communing with nature | WhyChess](http://whychess.com/node/10942)
8. [↑](#cite_ref-8) [Re: Detecting three-fold repetition?](https://www.stmintz.com/ccc/index.php?id=119911) by [John Stanback](/John_Stanback "John Stanback"), [CCC](/CCC "CCC"), July 17, 2000
9. [↑](#cite_ref-9) [Re: Move Tables - explain as if I'm five](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=490672&t=45846) by [Karlo Bala Jr.](/Karlo_Balla "Karlo Balla"), [CCC](/CCC "CCC"), November 05, 2012
10. [↑](#cite_ref-10) [II Mistrzostwa Polski Programów Szachowych - PGN](http://mpps.maciej.szmit.info/mpps-2/)
11. [↑](#cite_ref-11) The demon [Bael](https://en.wikipedia.org/wiki/Baal_%28demon%29) from [Collin de Plancy's](https://en.wikipedia.org/wiki/Collin_de_Plancy) [Dictionnaire Infernal](https://en.wikipedia.org/wiki/Dictionnaire_Infernal), 1862

**[Up one Level](/Engines "Engines")**