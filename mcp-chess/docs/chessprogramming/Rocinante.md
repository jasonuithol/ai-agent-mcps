# Rocinante

Source: https://www.chessprogramming.org/Rocinante

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Rocinante**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Don_Quijote_and_Sancho_Panza.jpg/250px-Don_Quijote_and_Sancho_Panza.jpg)](/File:Don_Quijote_and_Sancho_Panza.jpg)

[Gustave Doré](/Category:Gustave_Dor%C3%A9 "Category:Gustave Doré") - Don Quixote and Sancho Panza [[1]](#cite_note-1)

**Rocinante**,  
an [UCI](/UCI "UCI") compliant, experimental [open source chess engine](/Category:Open_Source "Category:Open Source") by [Antonio Torrecillas](/Antonio_Torrecillas "Antonio Torrecillas"), written in [C++](/Cpp "Cpp") and licensed under the [GNU General Public License](/Free_Software_Foundation#GPL "Free Software Foundation"). Rocinante was developed as test bed for [best-first](/Best-First "Best-First") search algorithms, notably [PB\*](/B* "B*") by [Hans Berliner](/Hans_Berliner "Hans Berliner") and [Chris McConnell](/Chris_McConnell "Chris McConnell") [[2]](#cite_note-2), and was first released in August 2009 [[3]](#cite_note-3). Rocinante **2.0**, released in May 2012, was a rewrite changing the board representation from [bitboards](/Bitboards "Bitboards") to [mailbox](/Mailbox "Mailbox"), and further added a [greedy](https://en.wikipedia.org/wiki/Greedy_algorithm) [Monte-Carlo Tree Search](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") without random playouts, dubbed [MCαβ](/MC%CE%B1%CE%B2 "MCαβ"), as additional search algorithm [[4]](#cite_note-4). Both, MCαβ and PB\* Rocinante may be configured to apply a shallow [alpha-beta search](/Alpha-Beta "Alpha-Beta") as a replacement for the [static evaluation](/Evaluation "Evaluation") [[5]](#cite_note-5). Rocinante source can be compiled to run under various platforms and operating systems such as [Windows](/Windows "Windows"), [Linux](/Linux "Linux") and [Android](/Android "Android").

# Etymology

[Rocinante](https://en.wikipedia.org/wiki/Rocinante) is [Don Quixote's](https://en.wikipedia.org/wiki/Don_Quixote) horse in the novel *[The Ingenious Gentleman Don Quixote of La Mancha](https://en.wikipedia.org/wiki/Don_Quixote)* by [Miguel de Cervantes](https://en.wikipedia.org/wiki/Miguel_de_Cervantes). In many ways, Rocinante is not only Don Quixote's horse, but also his [double](https://en.wikipedia.org/wiki/Double): like Don Quixote, he is awkward, past his prime, and engaged in a task beyond his capacities. Rocín in [Spanish](https://en.wikipedia.org/wiki/Spanish_language) means a [work horse](https://en.wikipedia.org/wiki/Draft_horse) or low-quality horse, but can also mean an illiterate or rough man. The name is a complex pun. In Spanish, [ante](https://en.wiktionary.org/wiki/ante) has several meanings and can function as a standalone word as well as a [suffix](https://en.wikipedia.org/wiki/Suffix). One meaning is "before" or "previously". Another is "in front of". As a suffix, [-ante](https://en.wiktionary.org/wiki/-ante#Spanish) in Spanish is [adverbial](https://en.wikipedia.org/wiki/Adverbial); rocinante refers to functioning as, or being, a rocín. "Rocinante," then, follows Cervantes' pattern using ambiguous, multivalent words, common throughout the novel [[6]](#cite_note-6).

# See also

- [B\*](/B* "B*")
- [MCαβ](/MC%CE%B1%CE%B2 "MCαβ")
- [Simplex](/Simplex "Simplex")

# Forum Posts

- [engine Rocinante is available](http://www.talkchess.com/forum/viewtopic.php?t=29360) by [Antonio Torrecillas](/Antonio_Torrecillas "Antonio Torrecillas"), [CCC](/CCC "CCC"), August 12, 2009
- [Rocinante, why ?](http://www.talkchess.com/forum/viewtopic.php?t=41158) by [Antonio Torrecillas](/Antonio_Torrecillas "Antonio Torrecillas"), [CCC](/CCC "CCC"), November 20, 2011
- [Rocinante 2.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=43895) by [Antonio Torrecillas](/Antonio_Torrecillas "Antonio Torrecillas"), [CCC](/CCC "CCC"), May 30, 2012
- [Whish list for Rocinante](http://www.talkchess.com/forum/viewtopic.php?t=46105) by [Antonio Torrecillas](/Antonio_Torrecillas "Antonio Torrecillas"), [CCC](/CCC "CCC"), November 21, 2012

# External Links

## Chess Engine

- [Barajando Trebejos](https://sites.google.com/site/barajandotrebejos/) (Download Rocinante and [Simplex](/Simplex "Simplex"))
- [Index of /chess/engines/Jim Ablett/ROCINANTE](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/ROCINANTE/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")

:   [Index of /chess/engines/Jim Ablett/+++ LINUX ENGINES ++/32 BIT/rocinante](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/+++%20LINUX%20ENGINES%20++/32%20BIT/rocinante/)
:   [Index of /chess/engines/Jim Ablett/+++ LINUX ENGINES ++/64 BIT/rocinante](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/+++%20LINUX%20ENGINES%20++/64%20BIT/rocinante/)

- [Rocinante 2.0 64-bit (mcts)](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Rocinante%202.0%2064-bit%20%28mcts%29) in [CCRL 40/4](/CCRL "CCRL")
- [Rocinante 2.0 64-bit (PB\*) in CCRL 40/4](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Rocinante%202.0%2064-bit%20%28PB*%29) in [CCRL 40/4](/CCRL "CCRL")

## Misc

- [Rocinante from Wikipedia](https://en.wikipedia.org/wiki/Rocinante)
- [Rocinante (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Rocinante_%28disambiguation%29)
- [If](/Category:If "Category:If") - [Don Quixote's Masquerade](https://en.wikipedia.org/wiki/Tea_Break_Over%E2%80%93Back_on_Your_%27Eads!), 1975, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Don Quixote](https://en.wikipedia.org/wiki/Don_Quixote) and [Sancho Panza](https://en.wikipedia.org/wiki/Sancho_Panza), in an 1868 edition of [Miguel de Cervantes’](https://en.wikipedia.org/wiki/Miguel_de_Cervantes) [Don Quixote](https://en.wikipedia.org/wiki/Don_Quixote) with illustrations by [Gustave Doré](/Category:Gustave_Dor%C3%A9 "Category:Gustave Doré"), [Gustave Doré's Exquisite Engravings of Cervantes' Don Quixote | Open Culture](http://www.openculture.com/2013/12/gustave-dores-definitive-engravings-of-don-quixote.html), December 10, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Hans Berliner](/Hans_Berliner "Hans Berliner"), [Chris McConnell](/Chris_McConnell "Chris McConnell") (**1995**). *B\* Probability Based Search.* [Carnegie Mellon University](/Carnegie_Mellon_University "Carnegie Mellon University") Computer Science research report
3. [↑](#cite_ref-3) [engine Rocinante is available](http://www.talkchess.com/forum/viewtopic.php?t=29360) by [Antonio Torrecillas](/Antonio_Torrecillas "Antonio Torrecillas"), [CCC](/CCC "CCC"), August 12, 2009
4. [↑](#cite_ref-4) [MCTS without random playout?](http://www.talkchess.com/forum/viewtopic.php?t=41730) by [Antonio Torrecillas](/Antonio_Torrecillas "Antonio Torrecillas"), [CCC](/CCC "CCC"), January 01, 2012
5. [↑](#cite_ref-5) [Rocinante 2.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=43895) by [Antonio Torrecillas](/Antonio_Torrecillas "Antonio Torrecillas"), [CCC](/CCC "CCC"), May 30, 2012
6. [↑](#cite_ref-6) [Rocinante from Wikipedia](https://en.wikipedia.org/wiki/Rocinante)

**[Up one Level](/Engines "Engines")**