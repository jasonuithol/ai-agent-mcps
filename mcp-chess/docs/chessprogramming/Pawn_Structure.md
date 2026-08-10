# Pawn Structure

Source: https://www.chessprogramming.org/Pawn_Structure

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* Pawn Structure**

[![](/images/thumb/9/9c/Elke_Rehder_Chess_Schach_Bauern_Pawns_Chain.jpg/342px-Elke_Rehder_Chess_Schach_Bauern_Pawns_Chain.jpg)](http://www.elke-rehder.de/Chess_Paintings.htm)

[Elke Rehder](/Arts#Rehder "Arts"), Chain of Pawns [[1]](#cite_note-1)

**Pawn structure** is a term used to describe the positions of all the pawns on the board, ignoring all other pieces. Pawn structure encompasses a broad range of ideas, from the general shape of the pawns (such as closed or open) to specific characteristics of individual pawns.

# Hashing Pawns

*see main article [Pawn Hash Table](/Pawn_Hash_Table "Pawn Hash Table")*

Full evaluation of pawn structure might be quite expensive. To speed up the evaluation, many programs use a separate [pawn hash table](/Pawn_Hash_Table "Pawn Hash Table"), addressed by a special key derived from the pawn's (and possibly also king's) position. Since pawn structure changes rather slowly, hit rate for such table is typically above 95%. Anything strictly pawn related can be stored in this hash table, including [pawn shield](/King_Safety#PawnShield "King Safety") terms to be used dynamically for [king safety](/King_Safety "King Safety").

# Standard Terms

## Single Pawn

- [Backward Pawn](/Backward_Pawn "Backward Pawn")
- [Candidate Passed Pawn](/Candidate_Passed_Pawn "Candidate Passed Pawn")
- [Doubled Pawn](/Doubled_Pawn "Doubled Pawn")
- [Faker](/Faker "Faker")
- [Hidden Passed Pawn](/Hidden_Passed_Pawn "Hidden Passed Pawn")
- [Isolated Pawn](/Isolated_Pawn "Isolated Pawn")
- [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [Sentry](/Sentry "Sentry")

## Groups of Pawns

- [Blockage Detection](/Blockage_Detection "Blockage Detection")
- [Connected Pawns](/Connected_Pawns "Connected Pawns")
- [Hanging Pawns](/Hanging_Pawns "Hanging Pawns")
- [Minority Attack](/Minority_Attack "Minority Attack")
- [Pawn Chain](/Pawn_Chain "Pawn Chain")
- [Pawn Islands](/Pawn_Islands "Pawn Islands")
- [Pawn Majority](/Pawn_Majority "Pawn Majority")

## General

- [Holes](/Holes "Holes")
- [Pawn Center](/Pawn_Center "Pawn Center")
- [Pawn Race](/Pawn_Race "Pawn Race")
- [Weak Pawns](/Weak_Pawns "Weak Pawns")

# Dependent on Pawn Structure

- [Bad Bishop](/Bad_Bishop "Bad Bishop")
- [Color Weakness](/Color_Weakness "Color Weakness")
- [King Pawn Tropism](/King_Pawn_Tropism "King Pawn Tropism")
- [King Safety](/King_Safety "King Safety")

:   [Pawn Shield](/King_Safety#PawnShield "King Safety")
:   [Pawn Storm](/King_Safety#PawnStorm "King Safety")

- [Outposts](/Outposts "Outposts")
- [Rook on (Semi) Open File](/Rook_on_Open_File "Rook on Open File")

# See also

- [CPW-Engine\_eval](/CPW-Engine_eval "CPW-Engine eval")
- [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") pawn structure aspects concerning [bitboards](/Bitboards "Bitboards")
  - [Pawn Levers (Bitboards)](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)")
  - [Pawn Rams (Bitboards)](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)")
- [Strategy](/Strategy "Strategy")

# Publications

- [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. 1959 McKay, 1990 Dover
- [Andrew Soltis](https://en.wikipedia.org/wiki/Andrew_Soltis) (**1976, 1995, 2013**). *Pawn Structure Chess*. Tartan Books, 1995 McKay, 2013 Batsford Chess [[2]](#cite_note-2)
- [Soei Tan](/Soei_Tan "Soei Tan") (**1977**). *Describing Pawn Structures.* [Advances in Computer Chess 1](/Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
- [Danny Kopec](/Danny_Kopec "Danny Kopec") (**1977**). *Recent developments in computer chess*, in Firbush News 7 Edinburgh: Machine Intelligence Research Unit, [University of Edinburgh](/University_of_Edinburgh "University of Edinburgh") (ed. [D. Michie](/Donald_Michie "Donald Michie")), [pdg](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_45_AI.pdf)
- [Michael Goeller](http://www.rci.rutgers.edu/~goeller/) (**2007**). *Pawn Battle Rules and Strategies*.[pdf](http://www.kenilworthchessclub.org/media/Pawn_Battle_Strategies.pdf)
- [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2017**). *Pawns*. [amazon](https://www.amazon.com/Pawns-Lyudmil-Tsvetkov-ebook/dp/B074S2MYQV)

# Forum Posts

## 2000 ...

- [how to detect information about pawn structure based on bitboard](https://www.stmintz.com/ccc/index.php?id=271055) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), December 17, 2002
- [pawn structure, pawn hash, square-of-pawn, pawn-races](https://www.stmintz.com/ccc/index.php?id=383014) by [Stuart Cracraft](/Stuart_Cracraft "Stuart Cracraft"), [CCC](/CCC "CCC"), August 19, 2004

## 2010 ...

- [Double levers](http://www.talkchess.com/forum/viewtopic.php?t=52609) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), June 11, 2014
- [Some more pawns](http://www.talkchess.com/forum/viewtopic.php?t=53507) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), August 31, 2014

## 2015 ...

- [Binders](http://www.talkchess.com/forum/viewtopic.php?t=55214) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 04, 2015
- [En passant bonus](http://www.talkchess.com/forum/viewtopic.php?t=55290) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 10, 2015 » [En passant](/En_passant "En passant")
- [Pawn checks and center levers](http://www.talkchess.com/forum/viewtopic.php?t=55292) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 11, 2015
- [Kind of backward](http://www.talkchess.com/forum/viewtopic.php?t=55319) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 13, 2015
- [Double pawn push](http://www.talkchess.com/forum/viewtopic.php?t=55343) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 14, 2015
- [Lever evaluation](http://www.talkchess.com/forum/viewtopic.php?t=56191) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), May 01, 2015 » [Pawn Levers (Bitboards)](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)")
- [Chain, duo, connected](http://www.talkchess.com/forum/viewtopic.php?t=56206) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), May 02, 2015 » [Pawn Chain](/Pawn_Chain "Pawn Chain"), [Duo Trio Quart (Bitboards)](/Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)")
- [Some more pawns](http://www.talkchess.com/forum/viewtopic.php?t=56213) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), May 03, 2015
- [Assorted tweaks](http://www.talkchess.com/forum/viewtopic.php?t=56282) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), May 08, 2015
- [A possible new pawn structure evaluation term?](http://www.talkchess.com/forum/viewtopic.php?t=57949) by [Árpád Rusz](/%C3%81rp%C3%A1d_Rusz "Árpád Rusz"), [CCC](/CCC "CCC"), October 15, 2015

## 2020 ...

- [Pawn structure tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73629) by [Vivien Clauzon](/Vivien_Clauzon "Vivien Clauzon"), [CCC](/CCC "CCC"), April 11, 2020 » [Automated Tuning](/Automated_Tuning "Automated Tuning"), [Ethereal](/Ethereal "Ethereal")
- [Re: Tcec season 18](https://groups.google.com/d/msg/fishcooking/Tc7XRkbRrSs/x9tUlRK1AgAJ) by [Warren D. Smith](/Warren_D._Smith "Warren D. Smith"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), June 28, 2020 » [Pawn Center](/Pawn_Center "Pawn Center"), [TCEC Season 18 Sufi Game 63 10... c4](/TCEC_Season_18#Sufi63 "TCEC Season 18")

# External Links

- [Pawn structure from Wikipedia](https://en.wikipedia.org/wiki/Pawn_structure), pattern of common [chess openings](https://en.wikipedia.org/wiki/Chess_opening)
- [Positional Play : Pawn Structure](http://www.mark-weeks.com/aboutcom/aa03j11.htm) by [Mark Weeks](/Mark_Weeks "Mark Weeks")

# References

1. [↑](#cite_ref-1) [Chess paintings in oil on canvas](http://www.elke-rehder.de/Chess_Paintings.htm) by [Elke Rehder](/Arts#Rehder "Arts")
2. [↑](#cite_ref-2) [Re: Tcec season 18](https://groups.google.com/d/msg/fishcooking/Tc7XRkbRrSs/x9tUlRK1AgAJ) by [Warren D. Smith](/Warren_D._Smith "Warren D. Smith"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), June 28, 2020 » [Pawn Center](/Pawn_Center "Pawn Center"), [TCEC Season 18 Sufi Game 63 10... c4](/TCEC_Season_18#Sufi63 "TCEC Season 18")

**[Up one level](/Evaluation "Evaluation")**