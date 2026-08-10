# Senpai

Source: https://www.chessprogramming.org/Senpai

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Senpai**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Great_Wave_off_Kanagawa2.jpg/330px-Great_Wave_off_Kanagawa2.jpg)](/File:Great_Wave_off_Kanagawa2.jpg)

[Katsushika Hokusai](/Category:Katsushika_Hokusai "Category:Katsushika Hokusai"), The Great Wave off Kanagawa [[1]](#cite_note-1)

**Senpai**, (Japanese: 先輩)  
an [UCI](/UCI "UCI") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), written from scratch in [C++11](/Cpp#11 "Cpp") and distributed under the [GNU General Public License version 3](/Free_Software_Foundation#GPL "Free Software Foundation"). Senpai 1.0 was precisely published ten years after the release of [Fruit 1.0](/Fruit "Fruit") on March 17, 2014 [[2]](#cite_note-2) . It comes with one source file, senpai\_10.cpp, structured by namespaces, further with [executables](https://en.wikipedia.org/wiki/Executable) for various platforms and operating systems, such as [Linux](/Linux "Linux"), [Mac OS](/Mac_OS "Mac OS"), [Windows](/Windows "Windows") and [Android](/Android "Android") [[3]](#cite_note-3). Senpai **2.0** released in November 2017 was a complete rewrite with a consistent codebase for multiple games such as [Draughts](/Draughts "Draughts"), [Chess960](/Chess960 "Chess960"), [Shogi](/Shogi "Shogi"), and [Othello](/Othello "Othello") [[4]](#cite_note-4).

# Description

## Board Representation

Senpai is a [bitboard](/Bitboards "Bitboards") engine and [maps](/Square_Mapping_Considerations#LittleEndianFileRankMapping "Square Mapping Considerations") consecutive bits to squares along a [file](/Files "Files") (a1,a2,...,a8,b1,...h8). With the option to implement [magic bitboards](/Magic_Bitboards "Magic Bitboards") later, Senpai so far uses the [Blockers and Beyond](/Blockers_and_Beyond "Blockers and Beyond") loop approach to determine attack-sets for all pieces except pawns, while Senpai **2.0** features [PEXT bitboards](/BMI2#PEXTBitboards "BMI2") for [BMI2](/BMI2 "BMI2") platforms. [BitScan](/BitScan "BitScan") aka [trailing zero count](/BitScan#TrailingZeroCount "BitScan"), and [population count](/Population_Count "Population Count") use [GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) builtins [[5]](#cite_note-5) if available for the target architecture, and otherwise rely on [De Bruijn multiplication](/BitScan#DeBruijnMultiplation "BitScan") and [SWAR-popcount](/Population_Count#SWARPopcount "Population Count"). In Senpai **2.0** the [copy/make](/Copy-Make "Copy-Make") approach is used, customary in games with fewer [piece types](/Pieces "Pieces") than chess.

[![Lefr.JPG](/images/thumb/2/27/Lefr.JPG/326px-Lefr.JPG)](/Bibob "Bibob")

Senpai's [Little-Endian File-Rank Mapping](/Square_Mapping_Considerations#LittleEndianFileRankMapping "Square Mapping Considerations") [[6]](#cite_note-6)

## Search

Senpai applies a [parallel search](/Parallel_Search "Parallel Search") with one master and a pool of helper [threads](/Thread "Thread"), following the [Young Brothers Wait Concept](/Young_Brothers_Wait_Concept "Young Brothers Wait Concept"). The serial search is [PVS](/Principal_Variation_Search "Principal Variation Search") [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition table](/Transposition_Table "Transposition Table") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](/Aspiration_Windows "Aspiration Windows"). Beside the obligarory [Null move pruning](/Null_Move_Pruning "Null Move Pruning") and [LMR](/Late_Move_Reductions "Late Move Reductions"), Senpai further uses [late move pruning](/Futility_Pruning#MoveCountBasedPruning "Futility Pruning") and more aggressive [futility pruning](/Futility_Pruning "Futility Pruning") the last few plies. Senpai **2.0** further applies [restricted singular extensions](/Singular_Extensions#RestrictedSE "Singular Extensions") and additional [reduction](/Reductions "Reductions")/[pruning](/Pruning "Pruning") of "losing" moves ([SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation")< 0).

## Evaluation

Compared to Fruit's [evaluation](/Evaluation "Evaluation"), Senpai has a more precise [mobility](/Mobility "Mobility") considering safety and [center weights](/Center_Control "Center Control"), and evaluates tactical moves. Senpai **2.0** considers a [tempo](/Tempo "Tempo") and [space](/Space "Space"), and uses a scoring by [logistic regression](/Automated_Tuning#LogisticRegression "Automated Tuning").

# Etymology

Senpai is a Japanese term applied to the mentor system in wide use in [Japanese culture](https://en.wikipedia.org/wiki/Culture_of_Japan), roughly equivalent to the Western concept of a [mentorship](https://en.wikipedia.org/wiki/Mentorship). In [Japanese martial arts](https://en.wikipedia.org/wiki/Japanese_martial_arts), the term Senpai generally refers to senior level students who hold a [black belt](https://en.wikipedia.org/wiki/Black_belt_%28martial_arts%29) [[7]](#cite_note-7) . Use in English may carry humorous or affectionate connotations. This is possibly due to (assumed) reference to modern [Japanese media](https://en.wikipedia.org/wiki/Media_of_Japan), or possibly a [lexical gap](https://en.wikipedia.org/wiki/Accidental_gap) [[8]](#cite_note-8) .

# See also

- [Chess-64](/Chess-64 "Chess-64")
- [Fruit](/Fruit "Fruit")
- [Kōhai](/index.php?title=K%C5%8Dhai&action=edit&redlink=1 "Kōhai (page does not exist)") [[9]](#cite_note-9) [[10]](#cite_note-10)

# Forum Posts

- [Senpai 1.0 (new engine)](http://www.talkchess.com/forum/viewtopic.php?t=51637) by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), [CCC](/CCC "CCC"), March 17, 2014
- [First blitz impressions: Senpai 1.0 et al](http://www.talkchess.com/forum/viewtopic.php?t=51652) by [Mike Scheidl](/index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](/CCC "CCC"), March 18, 2014
- [C++11 threads seem to get shafted for cycles](http://www.open-chess.org/viewtopic.php?f=5&t=2618) by [User923005](/Dann_Corbit "Dann Corbit"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 18, 2014 » [C++](/Cpp "Cpp"), [Parallel Search](/Parallel_Search "Parallel Search"), [Thread](/Thread "Thread")
- [Kohai 1.0 Released - a Senpai Derivative](http://www.talkchess.com/forum/viewtopic.php?t=60393) by [Michael B](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), June 06, 2016
- [Senpai 2.0](http://www.talkchess.com/forum/viewtopic.php?t=65680) by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), [CCC](/CCC "CCC"), November 10, 2017

# External Links

## Chess engine

- [Senpai Chess Engine - Computer Chess Programming](http://www.chessprogramming.net/senpai/) hosted by [Steve Maughan](/Steve_Maughan "Steve Maughan")
- [Frank's Chess Page, Senpai by Fabian Letouzey](http://www.amateurschach.de/main/_senpai.htm) hosted by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky")
- [Senpai 2.0 64-bit 4CPU](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Senpai%202.0%2064-bit%204CPU#Senpai_2_0_64-bit_4CPU) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Senpai and kōhai - Wikipedia](https://en.wikipedia.org/wiki/Senpai_and_k%C5%8Dhai)
- [senpai - Wiktionary](http://en.wiktionary.org/wiki/senpai)
- [先輩 - Wiktionary](http://en.wiktionary.org/wiki/%E5%85%88%E8%BC%A9)
- [Sensei - Wikipedia](https://en.wikipedia.org/wiki/Sensei)
- [Hiromi The Trio Project](https://www.ronniescotts.co.uk/performances/view/896-hiromi-the-trio-project-featuring-steve-smith-and-anthony-jackson) – [Dançando no Paraíso](https://en.wikipedia.org/wiki/Another_Mind), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Hiromi Uehara](/Category:Hiromi_Uehara "Category:Hiromi Uehara"), [Anthony Jackson](/Category:Anthony_Jackson "Category:Anthony Jackson"), [Steve Smith](/Category:Steve_Smith "Category:Steve Smith")

# References

1. [↑](#cite_ref-1) [The Great Wave off Kanagawa](https://en.wikipedia.org/wiki/The_Great_Wave_off_Kanagawa), [Katsushika Hokusai](/Category:Katsushika_Hokusai "Category:Katsushika Hokusai"), c. 1829–32, the first print in Hokusai's series [Thirty-six Views of Mount Fuji](https://en.wikipedia.org/wiki/Thirty-six_Views_of_Mount_Fuji), current location: [Library of Congress](https://en.wikipedia.org/wiki/Library_of_Congress), see [Culture of Japan](https://en.wikipedia.org/wiki/Culture_of_Japan)
2. [↑](#cite_ref-2) [Senpai 1.0 (new engine)](http://www.talkchess.com/forum/viewtopic.php?t=51637) by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), [CCC](/CCC "CCC"), March 17, 2014
3. [↑](#cite_ref-3) [Senpai Chess Engine - Computer Chess Programming](http://www.chessprogramming.net/senpai/) hosted by [Steve Maughan](/Steve_Maughan "Steve Maughan")
4. [↑](#cite_ref-4) [Senpai 2.0](http://www.talkchess.com/forum/viewtopic.php?t=65680) by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), [CCC](/CCC "CCC"), November 10, 2017
5. [↑](#cite_ref-5) \_\_builtin\_ctzll,\_\_ builtin\_popcountll, [Other Builtins - Using the GNU Compiler Collection (GCC)](http://gcc.gnu.org/onlinedocs/gcc-3.4.3/gcc/Other-Builtins.html)
6. [↑](#cite_ref-6) [Bibob](/Bibob "Bibob") image
7. [↑](#cite_ref-7) [Senpai and kōhai - Wikipedia](https://en.wikipedia.org/wiki/Senpai_and_k%C5%8Dhai)
8. [↑](#cite_ref-8) [senpai - Wiktionary](http://en.wiktionary.org/wiki/senpai)
9. [↑](#cite_ref-9) [Kohai 1.0 Released - a Senpai Derivative](http://www.talkchess.com/forum/viewtopic.php?t=60393) by [Michael B](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), June 06, 2016
10. [↑](#cite_ref-10) [GitHub - MichaelB7/Kohai-Chess: UCI Chess Engine, a derivative of Senpai 1.0](https://github.com/MichaelB7/Kohai-Chess)

**[Up one level](/Engines "Engines")**