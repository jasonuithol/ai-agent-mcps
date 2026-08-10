# Mate at a Glance

Source: https://www.chessprogramming.org/Mate_at_a_Glance

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [King Safety](/King_Safety "King Safety") \* Mate at a Glance**

[![](/images/thumb/3/36/Xeque-mate.jpg/300px-Xeque-mate.jpg)](https://sites.google.com/site/caroluschess/famous-people/artists/maria-helena-vieira-da-silva)

[Maria Helena Vieira da Silva](/Category:Maria_Helena_Vieira_da_Silva "Category:Maria Helena Vieira da Silva") - Xeque Mate, 1949 [[1]](#cite_note-1)

**Mate at a Glance**,  
an attempt to detect positions statically in [evaluation](/Evaluation "Evaluation"), where one side (not necessarily the [side to move](/Side_to_move "Side to move")) has a [legal move](/Legal_Move "Legal Move") to [checkmate](/Checkmate "Checkmate") its opponent [king](/King "King"). This is either a direct mate for the side to move or a mate threat, where one needs to defend accordantly rather than to [stand pat](/Quiescence_Search#StandPat "Quiescence Search") at a [quiescent node](/Quiescent_Node "Quiescent Node").

*Mate at a Glance* was introduced in 1978 by [John Birmingham](/John_Birmingham "John Birmingham") and [Peter Kent](/Peter_Kent "Peter Kent") at [Advances in Computer Chess 2](/Advances_in_Computer_Chess_2 "Advances in Computer Chess 2"), as implemented in their *Minimax algorithm Tester [Master](/Master "Master")*, and published 1980 in the conference proceedings [[2]](#cite_note-2). Some mate pattern were implemented in various programs, as known for instance from [Rebel](/Rebel "Rebel") [[3]](#cite_note-3), [Chess System Tal](/Chess_System_Tal "Chess System Tal") [[4]](#cite_note-4), [XiniX](/XiniX "XiniX") and [IsiChess](/IsiChess "IsiChess") [[5]](#cite_note-5) . Some programmers apply *Mate at a Glance* only for cheap and simple cases which occur frequently, like obvious [back rank mates](https://en.wikipedia.org/wiki/Back_rank_checkmate), some close mates with the [queen](/Queen "Queen"), and possibly mates with [knight](/Knight "Knight") like the [smothered mate](https://en.wikipedia.org/wiki/Smothered_mate). A few programmers apply more general, but also likely more complicated and error-prone pattern.

# Is it worth?

Whether the effort and amount of code for *Mate at a Glance* is worth, is disputed, considering [mate threats](/Null_Move_Pruning#ThreatDetection "Null Move Pruning") from [null move pruning](/Null_Move_Pruning "Null Move Pruning") as well the inconsistency in knowing some mates but not others. However, programs with a sophisticated [King Safety](/King_Safety "King Safety") evaluation and appropriate data-structures like [attack and defend maps](/Attack_and_Defend_Maps "Attack and Defend Maps") may detect [tactical motives](/Tactics "Tactics") like [skewers](/Skewer "Skewer") and some mates "en passant", to either control the [search](/Search "Search") with less strict conditions, or with a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) like approach, where [false positives](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) refer to **no mate**, to immediate return [mate scores](/Score#MateScores "Score") for [true negatives](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors).

# Mate Pattern

## Close Queen Mate

A [queen](/Queen "Queen") can often mate close to the opponent king on straight (or less frequent diagonal) adjacent squares, most often in front of a king on the back rank. Following conditions may be applied conjunctively in an order from cheap to expensive.

1. A set of all "mating squares" is determined by the [intersection](/General_Setwise_Operations#Intersection "General Setwise Operations") of queen attacks with all squares exclusively defended by the opponent king, but not occupied by pawns and pieces of the queen side.
2. A "mate square" is attacked not only by one queen, but additionally by any other piece, even indirectly due to a [battery](/Battery "Battery")
3. The queen is not [absolutely pinned](/Pin#AbsolutePin "Pin") on a [direction](/Direction "Direction") other than its [moving direction](/Direction#MoveDirections "Direction")
4. The "mate square" is not indirectly defended by a slider of the king side through the queen.
5. The set of up to two possible escape squares is empty, even after playing the queen move.
   1. off the boards (in case of border king)
   2. occupied by pieces of the king side
   3. attacked by pieces from the queen side, but not exclusively by the queen itself, which no longer controls this square after moving.

## Epaulette Mate

The [Epaulette mate](https://en.wikipedia.org/wiki/Checkmate_pattern#Epaulette_mate) with the [queen](/Queen "Queen") is a quite simple pattern to detect.

## Mates with sliding Pieces

This also covers the typical [back rank mates](https://en.wikipedia.org/wiki/Back-rank_checkmate) as well as the rare [Boden's Mate](https://en.wikipedia.org/wiki/Boden%27s_Mate). As preconditions to look further, a [vulnerable king](/King_Pattern#VulnerableOnDistantChecks "King Pattern") with only up to two escape squares (if any) exclusively on one line, either [rank](/Ranks "Ranks"), [file](/Files "Files"), [diagonal](/Diagonals "Diagonals") or [anti-diagonal](/Anti-Diagonals "Anti-Diagonals"), and an attacking [sliding piece](/Sliding_Pieces "Sliding Pieces"), which can safely move to that line. Further conditions necessary cover defenders blocking distant checks, including discovered defenses - and similar to the closer queen mates, whether the check giving piece decontrols a former taboo escape square of the king. Some programs even detect some mates in N statically, considering "worthless" delaying blocking moves.

# See also

- [Attack and Defend Maps](/Attack_and_Defend_Maps "Attack and Defend Maps")
- [Checkmate](/Checkmate "Checkmate")
- [Checks and Pinned Pieces (Bitboards)](/Checks_and_Pinned_Pieces_(Bitboards) "Checks and Pinned Pieces (Bitboards)")
- [Evaluation Patterns](/Evaluation_Patterns "Evaluation Patterns")
- [King Safety](/King_Safety "King Safety")
- [Mate Distance Pruning](/Mate_Distance_Pruning "Mate Distance Pruning")
- [Mate Search](/Mate_Search "Mate Search")
- [Mate Threat Extensions](/Mate_Threat_Extensions "Mate Threat Extensions")
- [Vulnerable on distant Checks](/King_Pattern#VulnerableOnDistantChecks "King Pattern") from [King Pattern](/King_Pattern "King Pattern") in [Bitboards](/Bitboards "Bitboards")
- [X-ray Attacks (Bitboards)](/X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)")

# Selected Publications

- [John Birmingham](/John_Birmingham "John Birmingham"), [Peter Kent](/Peter_Kent "Peter Kent") [[6]](#cite_note-6) (**1980**). *Mate at a Glance.* [Advances in Computer Chess 2](/Advances_in_Computer_Chess_2 "Advances in Computer Chess 2"), reprinted in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")

# Forum Posts

- [Static Mate Detection](https://www.stmintz.com/ccc/index.php?id=209201) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), January 22, 2002
- [Ptterns](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49676) by [Manuel Peña](/index.php?title=Manuel_Pe%C3%B1a&action=edit&redlink=1 "Manuel Peña (page does not exist)"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 20, 2008
- [Algorithm for mate recognition](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64460) by Fulvio, [CCC](/CCC "CCC"), June 30, 2017

# External Links

- [Back-rank checkmate from Wikipedia](https://en.wikipedia.org/wiki/Back-rank_checkmate)
- [Boden's Mate from Wikipedia](https://en.wikipedia.org/wiki/Boden%27s_Mate)
- [Checkmate pattern from Wikipedia](https://en.wikipedia.org/wiki/Checkmate_pattern)
- [Smothered mate from Wikipedia](https://en.wikipedia.org/wiki/Smothered_mate)

# References

1. [↑](#cite_ref-1) [Maria Helena Vieira da Silva - Carolus Chess](https://sites.google.com/site/caroluschess/famous-people/artists/maria-helena-vieira-da-silva)
2. [↑](#cite_ref-2) [John Birmingham](/John_Birmingham "John Birmingham"), [Peter Kent](/Peter_Kent "Peter Kent") (**1980**). *Mate at a Glance.* [Advances in Computer Chess 2](/Advances_in_Computer_Chess_2 "Advances in Computer Chess 2"), reprinted in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
3. [↑](#cite_ref-3) [Re: Static Mate Detection](https://www.stmintz.com/ccc/index.php?id=209405) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), January 23, 2002
4. [↑](#cite_ref-4) [move count frequency](https://www.stmintz.com/ccc/index.php?id=12822) by [Chris Whittington](/Chris_Whittington "Chris Whittington"), [CCC](/CCC "CCC"), December, 08, 1997
5. [↑](#cite_ref-5) [Static Mate Detection](https://www.stmintz.com/ccc/index.php?id=209201) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), January 22, 2002
6. [↑](#cite_ref-6) In the ICGA Database John Birmingham is mentioned as sole author

**[Up one Level](/King_Safety "King Safety")**