# Cupcake

Source: https://www.chessprogramming.org/Cupcake

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Cupcake**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Chocolate_Cupcakes_with_Raspberry_Buttercream_detail.jpg/330px-Chocolate_Cupcakes_with_Raspberry_Buttercream_detail.jpg)](/File:Chocolate_Cupcakes_with_Raspberry_Buttercream_detail.jpg)

Cupcake [[1]](#cite_note-1)

**Cupcake**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Dan Honeycutt](/Dan_Honeycutt "Dan Honeycutt"), written in [Java](/Java "Java"), first released in June, 2012.

# Description

Cupcake's [move generator](/Move_Generation "Move Generation") is almost identical to [Bruja's](/Bruja "Bruja"), Dan's earlier [C++](/Cpp "Cpp") program, but its speed is about half [[2]](#cite_note-2). Cupcake utilizes [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") for [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks"). The [Java-bitscan](/Java-Bitscan "Java-Bitscan") uses the 64-bit [De Bruijn multiplication](/BitScan#DeBruijnMultiplation "BitScan").

## Search

[Search](/Search "Search") is [PVS](/Principal_Variation_Search "Principal Variation Search") with [transposition table](/Transposition_Table "Transposition Table") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](/Aspiration_Windows "Aspiration Windows") in conjunction with [null move pruning](/Null_Move_Pruning "Null Move Pruning"), [LMR](/Late_Move_Reductions "Late Move Reductions"), and [check extensions](/Check_Extensions "Check Extensions").

## Evaluation

Cupcake applies a [tapered eval](/Tapered_Eval "Tapered Eval") for a smooth transition between the [game phases](/Game_Phases "Game Phases") and interpolates between the aggregated [opening](/Opening "Opening") and [endgame](/Endgame "Endgame") scores. Beside [material balance](/Material#Balance "Material") of [point values](/Point_Value "Point Value") and [piece-square tables](/Piece-Square_Tables "Piece-Square Tables"), Cupcake considers [mobility](/Mobility "Mobility"), [king safety](/King_Safety "King Safety"), and [pawn structure](/Pawn_Structure "Pawn Structure") including [passed pawns](/Passed_Pawn "Passed Pawn").

# See also

- [Bruja](/Bruja "Bruja")
- [Simon](/Simon "Simon")

# Forum Posts

- [Cupcake](http://www.talkchess.com/forum/viewtopic.php?t=44023) by [Dan Honeycutt](/Dan_Honeycutt "Dan Honeycutt"), [CCC](/CCC "CCC"), June 11, 2012
- [Cupcake 1.1a](http://www.talkchess.com/forum/viewtopic.php?t=46794) by [Dan Honeycutt](/Dan_Honeycutt "Dan Honeycutt"), [CCC](/CCC "CCC"), January 07, 2013

# External Links

## Chess Engine

- [Index of /chess/engines/Jim Ablett/CUPCAKE](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/CUPCAKE/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Cupcake 1.1a](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Cupcake%201.1a#Cupcake_1_1a) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Cupcake from Wikipedia](https://en.wikipedia.org/wiki/Cupcake)
- [Cupcake (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Cupcake_%28disambiguation%29)
- [Cookbook:Cupcakes - Wikibooks](http://en.wikibooks.org/wiki/Cookbook:Cupcakes)
- [Category:Cupcakes - Wikimedia Commons](http://commons.wikimedia.org/wiki/Category:Cupcakes)
- [Guthrie Govan](/Category:Guthrie_Govan "Category:Guthrie Govan") - [Wonderful Slippery Thing](https://en.wikipedia.org/wiki/Guthrie_Govan#Erotic_Cakes_and_The_Fellowship), feat. [Mohini Dey](/Category:Mohini_Dey "Category:Mohini Dey") (2017), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Chocolate Cupcakes with Raspberry Buttercream](http://whitneyinchicago.wordpress.com/2010/02/13/pretty-and-pink/) by [whitney](http://www.flickr.com/people/29298849@N05), February 07, 2010, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Cupcake](http://www.talkchess.com/forum/viewtopic.php?t=44023) by [Dan Honeycutt](/Dan_Honeycutt "Dan Honeycutt"), [CCC](/CCC "CCC"), June 11, 2012

**[Up one Level](/Engines "Engines")**