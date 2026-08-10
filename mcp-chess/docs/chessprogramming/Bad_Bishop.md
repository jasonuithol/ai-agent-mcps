# Bad Bishop

Source: https://www.chessprogramming.org/Bad_Bishop

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Evaluation of Pieces](/Evaluation_of_Pieces "Evaluation of Pieces") \* Bad bishop**

**Bad bishop**,  
a bishop whose [mobility](/Mobility "Mobility") is restricted by own pawns. As opposed to normal mobility problems, this situation is semi-permanent (more so if the position is blocked), which fact justifies singling it out as another evaluation term. Bad bishop is not such a liability if it is placed outside the pawn chain (Bf5 in the Slav). For that reason some programs, like [Crafty](/Crafty "Crafty"), score a bishop as bad only if its forward mobility is impaired.

For a [bitboard-based](/Bitboards "Bitboards") program a feasible approach would be to create an array of 64 bitboards, indexed by a Bishop's position, and marking the pawn positions which would make our bishop bad.

# See also

- [Pawn Rams (Bitboards)](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)")
- [Bishops of Opposite Colors](/Bishops_of_Opposite_Colors "Bishops of Opposite Colors")
- [Color of a Square](/Color_of_a_Square "Color of a Square")
- [Color Weakness](/Color_Weakness "Color Weakness")

# Publications

- [Matej Guid](/Matej_Guid "Matej Guid"), [Martin Možina](/Martin_Mo%C5%BEina "Martin Možina"), [Jana Krivec](/Jana_Krivec "Jana Krivec"), [Aleksander Sadikov](/Aleksander_Sadikov "Aleksander Sadikov"), [Ivan Bratko](/Ivan_Bratko "Ivan Bratko") (**2008**). *[Learning Positional Features for Annotating Chess Games: A Case Study](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_18)*. [CG 2008](/CG_2008 "CG 2008"), [pdf](http://www.ailab.si/matej/doc/Learning_Positional_Features-Case_Study.pdf)

# Forum Posts

- [Evaluating bad bishops](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4815) by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [Winboard Programming Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 15, 2006
- [Bad/good bishops in R3 and IPPOLIT/IvanHoe](http://www.open-chess.org/viewtopic.php?f=5&t=785) by [Mark Watkins](/Mark_Watkins "Mark Watkins"), [Open Chess Programming Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 30, 2010

# External Links

- [Good bishop and bad bishop from Wikipedia](https://en.wikipedia.org/wiki/Bishop_%28chess%29#Good_bishop_and_bad_bishop)
- [How Bad is a Bad Bishop?](http://www.chess.com/article/view/how-bad-is-a-bad-bishop) by [Iryna Zenyuk](http://www.chess.com/members/view/energia), [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), February 27, 2019
- [The Bishow's Show: Bad Bishop](http://www.chess.com/article/view/the-bishows-show-bad-bishop) by [Iryna Zenyuk](http://www.chess.com/members/view/energia), [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), March 09, 2012

**[Up one Level](/Evaluation_of_Pieces "Evaluation of Pieces")**