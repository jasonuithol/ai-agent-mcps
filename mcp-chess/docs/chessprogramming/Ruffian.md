# Ruffian

Source: https://www.chessprogramming.org/Ruffian

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Ruffian**

**Ruffian**,  
a chess engine developed by [Perola Valfridsson](/Perola_Valfridsson "Perola Valfridsson") since 1998, which appeared in July 2002 as a surprisingly strong newcomer playing on [ICC](/index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)") and [FICS](/index.php?title=Free_Internet_Chess_Server&action=edit&redlink=1 "Free Internet Chess Server (page does not exist)") [[1]](#cite_note-1), supporting both, the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](/UCI "UCI").

# Description

With portability and performance in mind, Ruffian was written in [C](/C "C"), and used a hybrid [board representation](/Board_Representation "Board Representation") of [bitboard](/Bitboards "Bitboards") and [8x8 board](/8x8_Board "8x8 Board"). It performs [PVS](/Principal_Variation_Search "Principal Variation Search") with [null move pruning](/Null_Move_Pruning "Null Move Pruning") and other [forward pruning](/Pruning "Pruning") techniques as well as a few own algorithms and tricks [[2]](#cite_note-2). One of the major [evaluation](/Evaluation "Evaluation") terms is [mobility](/Mobility "Mobility") based on pre-calculated tables considering various patterns [[3]](#cite_note-3) [[4]](#cite_note-4).

# Photos

[![Ict2004win29.jpg](/images/d/de/Ict2004win29.jpg)](http://old.csvn.nl/ict4tour.html)

[ICT 2004](/ICT_2004 "ICT 2004") winners: [Chrilly Donninger](/Chrilly_Donninger "Chrilly Donninger"), [Erdogan Günes](/Erdogan_G%C3%BCnes "Erdogan Günes") ([Hydra](/Hydra "Hydra") 2nd), [Stefan Meyer-Kahlen](/Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") ([Shredder](/Shredder "Shredder") 1st),  
[Johan Havegheer](/Johan_Havegheer "Johan Havegheer") (Ruffian 3rd), [Vincent Diepeveen](/Vincent_Diepeveen "Vincent Diepeveen") ([Diep](/Diep "Diep") 3rd) [[5]](#cite_note-5)

# Achievements

Ruffian was shared winner of the [CCT5](/CCT5 "CCT5") and lonesome winner of the [DOCCC 2003](/DOCCC_2003 "DOCCC 2003") supported by [book author](/Category:Opening_Book_Author "Category:Opening Book Author") [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), operated by [Johan Havegheer](/Johan_Havegheer "Johan Havegheer"), [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky") and [Leo Dijksman](/Leo_Dijksman "Leo Dijksman") [[6]](#cite_note-6) [[7]](#cite_note-7), winner of the (unofficial) Swedish Championship in 2003 [[8]](#cite_note-8), and further played a strong [CCT6](/CCT6 "CCT6") and [ICT 2004](/ICT_2004 "ICT 2004").

# Free Ruffian

The free [Windows](/Windows "Windows") versions 1.0 from September 2002 is still available for download from [Ed Schröder's](/Ed_Schroder "Ed Schroder") Winboard and UCI engines download site [[9]](#cite_note-9).

# Commercial Ruffian

In 2003, Ruffian 2 went commercial, first bundled with [Chess Assistant](/Chess_Assistant "Chess Assistant") by [Convekta](/ChessOK "ChessOK"), where [Victor Zakharov](/Victor_Zakharov "Victor Zakharov") mentions [Dann Corbit](/Dann_Corbit "Dann Corbit") was a big help [[10]](#cite_note-10), and further with the otherwise free [Arena](/Arena "Arena") [GUI](/GUI "GUI"), CD production by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky") and distribution by [Schachversand Niggemann](/Schachversand_Niggemann "Schachversand Niggemann") [[11]](#cite_note-11), and soon as bundle with [ChessPartner](/ChessPartner "ChessPartner") by [Lokasoft](/Lokasoft "Lokasoft") [[12]](#cite_note-12).
Ruffian is base of the chess AI in [Kasparov Chessmate](/Kasparov_Chessmate "Kasparov Chessmate") [[13]](#cite_note-13), with [Perola Valfridsson](/Perola_Valfridsson "Perola Valfridsson") credited as author by [MobyGames](https://en.wikipedia.org/wiki/MobyGames) [[14]](#cite_note-14).
The initial hype about Ruffian's commercialization was apparently detrimental to its authors motivation to continue the development [[15]](#cite_note-15). In conjunction with the upcoming strong free engines catching up, this was slowly but surely the fall of the commercial endeavor [[16]](#cite_note-16).
In May 2017, [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky") rescued Ruffian versions 2.02 and 2.1 from their commercial burdens [[17]](#cite_note-17).

# See also

- [Chester](/Chester "Chester")
- [Kasparov Chessmate](/Kasparov_Chessmate "Kasparov Chessmate")
- [King of Kings](/index.php?title=King_of_Kings&action=edit&redlink=1 "King of Kings (page does not exist)")
- [Tinker](/Tinker "Tinker")

# Forum Posts

## 2002

- [What is Ruffian?](https://www.stmintz.com/ccc/index.php?id=242402) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), July 24, 2002
- [Some info about Ruffian](https://www.stmintz.com/ccc/index.php?id=243152) by [Benny Antonsson](/Benny_Antonsson "Benny Antonsson"), [CCC](/CCC "CCC"), July 29, 2002
- [Ruffian 0.76 is still playing incredible strong!](https://www.stmintz.com/ccc/index.php?id=252726) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), September 19, 2002
- [Ruffian is here - Make your move Bob Hyatt!](https://www.stmintz.com/ccc/index.php?id=253512) by [Peter Fendrich](/Peter_Fendrich "Peter Fendrich"), [CCC](/CCC "CCC"), September 23, 2002
- [Interview with Ruffian programmer Per-Ola Valfridsson available!](https://www.stmintz.com/ccc/index.php?id=257897) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), October 09, 2002

## 2003

- [Dutch Open Leiden final ranking - Ruffian Champion](https://www.stmintz.com/ccc/index.php?id=323778) by [Theo van der Storm](/Theo_van_der_Storm "Theo van der Storm"), [CCC](/CCC "CCC"), October 26, 2003
- [First impression of Ruffian 1.0.5](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45030) by capgadget, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 07, 2003
- [Arena 1.0 / Ruffian 2.0 ... information!](https://www.stmintz.com/ccc/index.php?id=329068) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), November 21, 2003
- [Ruffian's Secret?](https://www.stmintz.com/ccc/index.php?id=329957) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), November 23, 2003
- [The America/Ruffian ordeal...](https://www.stmintz.com/ccc/index.php?id=333338) by [Slater Wold](/index.php?title=Slater_Wold&action=edit&redlink=1 "Slater Wold (page does not exist)"), [CCC](/CCC "CCC"), December 03, 2003
- [Questions about Ruffian2 and other platforms](https://www.stmintz.com/ccc/index.php?id=336611) by [Daniel Clausen](/index.php?title=Daniel_Clausen&action=edit&redlink=1 "Daniel Clausen (page does not exist)"), [CCC](/CCC "CCC"), December 17, 2003
- [One more post on Ruffian 2.0](https://www.stmintz.com/ccc/index.php?id=337021) by [Đorđe Vidanović](/%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [CCC](/CCC "CCC"), December 19, 2003

## 2004

- [Ruffian on a G5 isn't bad!](https://www.stmintz.com/ccc/index.php?id=346058) by George Sobala, [CCC](/CCC "CCC"), January 31, 2004
- [Ruffian 2.1.0 ...](https://www.stmintz.com/ccc/index.php?id=348116) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), February 09, 2004
- [Good news for Ruffian Lovers from outside europe](https://www.stmintz.com/ccc/index.php?id=350465) by [Johan Havegheer](/Johan_Havegheer "Johan Havegheer"), [CCC](/CCC "CCC"), February 21, 2004
- [Ruffian 2.1.0 or Ruffian 2.0.2 ...](https://www.stmintz.com/ccc/index.php?id=350771) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), February 23, 2004
- [Ruffian 2.0.2 copy protection](https://www.stmintz.com/ccc/index.php?id=352351) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), March 02, 2004
- [Ruffian's most peculiar way of pondering](https://www.stmintz.com/ccc/index.php?id=356976) by [Peter Berger](/Peter_Berger "Peter Berger"), [CCC](/CCC "CCC"), March 27, 2004

## 2005 ...

- [Re: CSVN Leiden (Ruffian and Sjeng missing)](https://www.stmintz.com/ccc/index.php?id=429271) by [Johan Havegheer](/Johan_Havegheer "Johan Havegheer"), [CCC](/CCC "CCC"), June 01, 2005
- [SSDF(Fruit 2.2.1 - Ruffian 1.0.1)A1200, 2½-2½, ended 26-14](https://www.stmintz.com/ccc/index.php?id=478190) by [Tony Hedlund](/Tony_Hedlund "Tony Hedlund"), [CCC](/CCC "CCC"), January 09, 2006 » [Fruit](/Fruit "Fruit")

## 2015 ...

- [Computer Chess Progress: Stockfish 7 vs Ruffian 1.0.5](http://www.talkchess.com/forum/viewtopic.php?t=59543) by [Martin Fierz](/Martin_Fierz "Martin Fierz"), [CCC](/CCC "CCC"), March 17, 2016 » [Stockfish](/Stockfish "Stockfish")
- [Ruffian support ...](http://www.talkchess.com/forum/viewtopic.php?t=63995) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), May 16, 2017

# External Links

## Chess Engine

- [Ruffian](https://web.archive.org/web/20120106020305/http://www.playwitharena.com/?Partner_Chess_Engines:Ruffian%26nbsp%3B) from [Arena](/Arena "Arena") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- <https://web.archive.org/web/20170830232610/http://www.top-5000.nl/int/ruffian.htm> Ruffian, the replacement to ABBA], Interview with [Perola Valfridsson](/Perola_Valfridsson "Perola Valfridsson") by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky") et al., October, 2002, hosted by [Ed Schröder](/Ed_Schroder "Ed Schroder") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Shredder and Ruffian lead in Leiden](https://en.chessbase.com/post/shredder-and-ruffian-lead-in-leiden) by [Eric van Reem](/Eric_van_Reem "Eric van Reem") and [Theo van der Storm](/Theo_van_der_Storm "Theo van der Storm"), [ChessBase](/ChessBase "ChessBase"), April 24, 2004 » [ICT 2004](/ICT_2004 "ICT 2004")
- [Ruffian](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Ruffian&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")
- [Download Winboard and UCI engines](http://www.top-5000.nl/wbuci.htm) by [Ed Schröder](/Ed_Schroder "Ed Schroder")
- [Frank's Chess Page, Downloads](http://www.amateurschach.de/main/_download.htm) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky")

## Misc

- [ruffian - Wiktionary](https://en.wiktionary.org/wiki/ruffian)
- [ruffiano - Wiktionary](https://en.wiktionary.org/wiki/ruffiano)
- [from Wikipedia](https://en.wikipedia.org/wiki/Ruffian)
- [Ruffian Games from Wikipedia](https://en.wikipedia.org/wiki/Ruffian_Games)
- [Ruffian (horse) from Wikipedia](https://en.wikipedia.org/wiki/Ruffian_%28horse%29)
- [The Ruffian - eBike](https://www.ruff-cycles.com/ruffian/)

# References

1. [↑](#cite_ref-1) [What is Ruffian?](https://www.stmintz.com/ccc/index.php?id=242402) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), July 24, 2002
2. [↑](#cite_ref-2) [Ruffian, the replacement to ABBA](http://www.top-5000.nl/int/ruffian.htm), Interview with [Perola Valfridsson](/Perola_Valfridsson "Perola Valfridsson") by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky") et al., October, 2002, hosted by [Ed Schröder](/Ed_Schroder "Ed Schroder")
3. [↑](#cite_ref-3) [Ruffian 2.0: 3 Euro](http://www.schachversand.de/e/detail/software/464.html) - [Schachversand Niggemann](/Schachversand_Niggemann "Schachversand Niggemann")
4. [↑](#cite_ref-4) [Ruffian's Secret?](https://www.stmintz.com/ccc/index.php?id=329957) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), November 23, 2003
5. [↑](#cite_ref-5) [Photos](http://old.csvn.nl/ict4tour.html) from the old [CSVN](/CSVN "CSVN") site
6. [↑](#cite_ref-6) [Participants 23rd Open Dutch Computer-Chess Championship 18, 19, 25, 26 Oct. 2003; Leiden, Netherlands](http://old.csvn.nl/partic03.html) old [CSVN](/CSVN "CSVN") site
7. [↑](#cite_ref-7) [Dutch Open Leiden final ranking - Ruffian Champion](https://www.stmintz.com/ccc/index.php?id=323778) by [Theo van der Storm](/Theo_van_der_Storm "Theo van der Storm"), [CCC](/CCC "CCC"), October 26, 2003
8. [↑](#cite_ref-8) [iSMDS-03 (unofficial) Swedish Championship 2003](http://www.albert.nu/SMDS/) by [Albert Bertilsson](/Albert_Bertilsson "Albert Bertilsson")
9. [↑](#cite_ref-9) [Download Winboard and UCI engines](http://www.top-5000.nl/wbuci.htm) by [Ed Schröder](/Ed_Schroder "Ed Schroder")
10. [↑](#cite_ref-10) [ChessAssistance.com A talk with Victor Zakharov, head of Convekta development, part b](http://chessok.com/files/bobpawlak/Articles/Victor_Zakharov_b.html) by [Robert Pawlak](/Robert_Pawlak "Robert Pawlak"), February 14, 2003
11. [↑](#cite_ref-11) [Arena 1.0 / Ruffian 2.0 ... information!](https://www.stmintz.com/ccc/index.php?id=329068) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), November 21, 2003
12. [↑](#cite_ref-12) [Good news for Ruffian Lovers from outside europe](https://www.stmintz.com/ccc/index.php?id=350465) by [Johan Havegheer](/Johan_Havegheer "Johan Havegheer"), [CCC](/CCC "CCC"), February 21, 2004
13. [↑](#cite_ref-13) [Kasparov Chessmate review](https://www.stmintz.com/ccc/index.php?id=306057) by Alastair Scott, [CCC](/CCC "CCC"), July 12, 2003
14. [↑](#cite_ref-14) [Perola Valfridsson](http://www.mobygames.com/developer/sheet/view/by_genre/developerId,281982/) from [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
15. [↑](#cite_ref-15) [Re: CSVN Leiden (Ruffian and Sjeng missing)](https://www.stmintz.com/ccc/index.php?id=429271) by [Johan Havegheer](/Johan_Havegheer "Johan Havegheer"), [CCC](/CCC "CCC"), June 01, 2005
16. [↑](#cite_ref-16) [Ruffian 2.0: 3 Euro](http://www.schachversand.de/e/detail/software/464.html) - [Schachversand Niggemann](/Schachversand_Niggemann "Schachversand Niggemann")
17. [↑](#cite_ref-17) [Ruffian support ...](http://www.talkchess.com/forum/viewtopic.php?t=63995) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [CCC](/CCC "CCC"), May 16, 2017

**[Up one Level](/Engines "Engines")**