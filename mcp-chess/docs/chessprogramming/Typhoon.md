# Typhoon

Source: https://www.chessprogramming.org/Typhoon

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Typhoon**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Typhoon_Mike_11_nov_1990_2221Z.jpg/250px-Typhoon_Mike_11_nov_1990_2221Z.jpg)](/File:Typhoon_Mike_11_nov_1990_2221Z.jpg)

[Typhoon Mike](https://en.wikipedia.org/wiki/Typhoon_Mike) [[1]](#cite_note-1)

**Typhoon**,  
an [open source chess engine](/Category:Open_Source "Category:Open Source") by [Scott Gasch](/Scott_Gasch "Scott Gasch"), as successor of [Monsoon](/Monsoon "Monsoon") also written in [C](/C "C") and compliant to the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol").

# Description

Like [Monsoon](/Monsoon "Monsoon"), Typhoon represents the board as [0x88](/0x88 "0x88") array, where the [difference of two square coordinates](/0x88#SquareRelations "0x88") has unique [direction](/Direction "Direction") and [distance](/Distance "Distance") relationship, extensively using [vector delta tables](/Vector_Attacks "Vector Attacks") for [in check](/Check "Check") detection, [move generation](/Move_Generation "Move Generation"), [X-ray attack](/X-ray "X-ray") detection, [PGN](/Portable_Game_Notation "Portable Game Notation") file parsing for [book](/Opening_Book "Opening Book") creation, [static exchange evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation"), and [position evaluation](/Evaluation "Evaluation").
It performs a [principal variation search](/Principal_Variation_Search "Principal Variation Search") with [nullmove pruning](/Null_Move_Pruning "Null Move Pruning"), various [extensions](/Extensions "Extensions") and [transposition table](/Transposition_Table "Transposition Table").
For [evaluation](/Evaluation "Evaluation") purpose, Typhoon keeps track of [piece-square](/Piece-Square_Tables "Piece-Square Tables") and [material balance](/Material "Material") [incrementally](/Incremental_Updates "Incremental Updates"). Utilizing a [pawn hash table](/Pawn_Hash_Table "Pawn Hash Table") with some pawn [bitboards](/Bitboards "Bitboards"), it considers the [pawn structure](/Pawn_Structure "Pawn Structure") along with multiple features for [king](/King "King") and [pieces](/Evaluation_of_Pieces "Evaluation of Pieces"), such as [king safety](/King_Safety "King Safety") and [mobility](/Mobility "Mobility") to name a few.
Typhoon supports [Nalimov Tablebases](/Nalimov_Tablebases "Nalimov Tablebases") and has various simple [interior node recognizers](/Interior_Node_Recognizer "Interior Node Recognizer") for [wrong color bishop endgames](/Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn") and trivially won [KPK](/KPK "KPK") games. These recognizers are based on [Thorsten Greiner's](/Thorsten_Greiner "Thorsten Greiner") program [Amy](/Amy "Amy") [[2]](#cite_note-2) [[3]](#cite_note-3).

# Parallel Search

While running on a multi-processor machine, Typhoon uses a tree splitting algorithm somewhat similar to [principal variation splitting](/Parallel_Search#PrincipalVariationSplitting "Parallel Search") to [search in parallel](/Parallel_Search "Parallel Search") with multiple [threads](/Thread "Thread").
Splitting occurs after the first move has been searched at [PV-nodes](/Node_Types#PV "Node Types") or if the first N moves at [All-nodes](/Node_Types#ALL "Node Types") [[4]](#cite_note-4) [[5]](#cite_note-5).

# See also

- [Monsoon](/Monsoon "Monsoon")

# Forum Posts

- [For Jim Ablett, about problems with new Typhoon builds](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5221) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), July 19, 2006
- [Typhoon chess engine bug & bugfix](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51322) by [Daniel Uranga](/Daniel_Uranga "Daniel Uranga"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 18, 2010

# External Links

## Chess Engine

- [Monsoon/Typhoon Homepage](https://wannabe.guru.org/scott/hobbies/chess/)
- [Typhoon Chess Engine](https://wannabe.guru.org/scott/hobbies/chess/typhoon.html)
- [typhoon - Revision 359: /trunk](https://wannabe.guru.org/svn/typhoon/trunk/)
- [Index of /chess/engines/Jim Ablett/TYPHOON](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/TYPHOON/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Typhoon](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Typhoon&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Typhoon from Wikipedia](https://en.wikipedia.org/wiki/Typhoon)

:   [Pacific typhoon season](https://en.wikipedia.org/wiki/Pacific_typhoon_season)

- [Typhoon](https://en.wikipedia.org/wiki/Typhoon_%28American_band%29) - Artificial Light, Live At [The Crystal Ballroom](https://en.wikipedia.org/wiki/Crystal_Ballroom_%28Portland,_Oregon%29), November 29, 2013, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) Super Typhoon Mike at peak intensity on November 11, 1990 at 2221 UTC. [This image](https://commons.wikimedia.org/wiki/File:Typhoon_Mike_11_nov_1990_2221Z.jpg) was produced from data from NOAA-10, provided by [NOAA](https://en.wikipedia.org/wiki/National_Oceanic_and_Atmospheric_Administration), [Typhoons in the Philippines](https://en.wikipedia.org/wiki/Typhoons_in_the_Philippines)
2. [↑](#cite_ref-2) [Monsoon/Typhoon Homepage - Miscellanious](https://wannabe.guru.org/scott/hobbies/chess/)
3. [↑](#cite_ref-3) [recogn.c | Copyright (c) Scott Gasch](https://wannabe.guru.org/svn/typhoon/trunk/recogn.c)
4. [↑](#cite_ref-4) [search.c | Copyright (c) Scott Gasch](https://wannabe.guru.org/svn/typhoon/trunk/search.c)
5. [↑](#cite_ref-5) [split.c | Copyright (c) Scott Gasch](https://wannabe.guru.org/svn/typhoon/trunk/split.c)

**[Up one level](/Engines "Engines")**