# Pawn Center

Source: https://www.chessprogramming.org/Pawn_Center

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Pawn Structure](/Pawn_Structure "Pawn Structure") \* Pawn Center**

Chess theory holds that it is advantageous to [control](/Square_Control "Square Control") the [center](/Center "Center") with pawns. This principle has been stressed especially in the classical period of [chess theory](https://en.wikipedia.org/wiki/Chess_theory) to the extent that some perfectly healthy [openings](/Opening "Opening") were considered disadvantageous on the grounds that they "give up the center" like the [Rubinstein line in the French](https://en.wikipedia.org/wiki/French_Defence#Rubinstein_Variation_3...dxe4). Many of the [hypermodern openings](https://en.wikipedia.org/wiki/Hypermodernism_%28chess%29) adopt the opposite attitude, allowing the opponent to build the pawn center in order to attack it later on. It follows that the evaluation function, in order to remain flexible, should not assign too great weights to pawn center - else it would be unable to evaluate this kind of position correctly.

# Terms

related to Pawn Center by [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") [[1]](#cite_note-1) [[2]](#cite_note-2)

- Center lever - A [lever](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)") wholly within the two center files
- Center pawn - Pawn on the d- or e-file
- Centerswap - A capture from and to the d- or e-file that produces a [doubled pawn](/Doubled_Pawn "Doubled Pawn")
- Innerswap - A capture towards the center that produces a doubled pawn

# Coding

Coding pawn center evaluation routine, one can

1. use values in a [piece-square table](/Piece-Square_Tables "Piece-Square Tables") for pawns
2. raise the [material](/Material "Material") value of central pawns or
3. assign bonuses for certain pawn configurations, like the following:
   1. good formation of white pawns on d4 and c4
   2. e4 or d4 pawn defended by another pawn

Some other evaluation factors are interrelated with the pawn center, like the penalty for a [knight on c3](/Evaluation_of_Pieces#Knight "Evaluation of Pieces") blocking c2 pawn in the closed openings.

# See also

- [Center](/Center "Center")
- [Center Control](/Center_Control "Center Control")
- [Evaluation of Pieces](/Evaluation_of_Pieces "Evaluation of Pieces")
- [Pawn Levers (Bitboards)](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)")
- [Pawn Rams (Bitboards)](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)")
- [Strategy](/Strategy "Strategy")

# Publications

- [Andrew Soltis](https://en.wikipedia.org/wiki/Andrew_Soltis) (**1976, 1995, 2013**). *Pawn Structure Chess*. Tartan Books, 1995 McKay, 2013 Batsford Chess [[3]](#cite_note-3)

# Forum Posts

- [Why a Pawn Center?](https://www.stmintz.com/ccc/index.php?id=40195) by Laurence Chen, [CCC](/CCC "CCC"), January 20, 1999
- [Closed pawn center and Kingsafety](https://www.stmintz.com/ccc/index.php?id=352984) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), March 05, 2004
- [Pawn checks and center levers](http://www.talkchess.com/forum/viewtopic.php?t=55292) by [Lyudmil Tsvetkov](/Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](/CCC "CCC"), February 11, 2015
- [Re: Tcec season 18](https://groups.google.com/d/msg/fishcooking/Tc7XRkbRrSs/x9tUlRK1AgAJ) by [Warren D. Smith](/Warren_D._Smith "Warren D. Smith"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), June 28, 2020 » [TCEC Season 18 Sufi Game 63 10... c4](/TCEC_Season_18#Sufi63 "TCEC Season 18")

# External Links

- [Chess Strategy | The center | The pawn center from Wikibooks](http://en.wikibooks.org/wiki/Chess_Strategy/The_center#The_pawn_center)
- [School of chess from Wikipedia](https://en.wikipedia.org/wiki/School_of_chess)
- [Hypermodernism (chess) from Wikipedia](https://en.wikipedia.org/wiki/Hypermodernism_%28chess%29)
- [Pawn Center Types](http://www.fraserheightschess.com/Documents/Pawn_Center_Types.pdf) (pdf) from [Fraser Heights Chess Club](http://www.fraserheightschess.com/)
- [What to do with the pawn center?](http://www.chess.com/article/view/what-to-do-with-the-pawn-center), [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")
- [5 main pawns positions in the center. Part 1 of 2 (open and closed center only)](http://www.chess.com/forum/view/livechess/5-main-pawn-position-in-the-center), [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")
- [5 main pawns positions in the center. Part 2 of 2 (mobile,fixed & dynamic)](http://www.chess.com/forum/view/livechess/5-main-pawns-positions-in-the-center-part-2-of-2-mobilefixed-amp-dynamic), [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")
- [JROBICHESS CHESS BLOG: Pawn Centres I: Open Centre](http://jrobichess.blogspot.com/2007/12/pawn-centres-i-open-centre.html)
- [JROBICHESS CHESS BLOG: Pawn Centres II: Closed Centre](http://jrobichess.blogspot.com/2008/01/pawn-centres-ii-closed-centre.html)

# References

1. [↑](#cite_ref-1) [Glossary for Pawn Power In Chess by Hans Kmoch](http://www.chessville.com/Reference_Center/Pawn_Power_Glossary.htm)
2. [↑](#cite_ref-2) [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6, [Google Books](http://books.google.com/books?id=FT7hpAiec3EC&dq=Pawn+Power+in+Chess&pg=PP1&ots=q_yCx72Ms_&sig=sKrQzXouaweUYbwCjfTcaplUF4U&hl=de&sa=X&oi=book_result&resnum=1&ct=result#PPA1,M1), [amazon](http://www.amazon.com/Pawn-Power-Chess-Hans-Kmoch/dp/0486264866)
3. [↑](#cite_ref-3) [Re: Tcec season 18](https://groups.google.com/d/msg/fishcooking/Tc7XRkbRrSs/x9tUlRK1AgAJ) by [Warren D. Smith](/Warren_D._Smith "Warren D. Smith"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), June 28, 2020 » [TCEC Season 18 Sufi Game 63 10... c4](/TCEC_Season_18#Sufi63 "TCEC Season 18")

**[Up one Level](/Pawn_Structure "Pawn Structure")**