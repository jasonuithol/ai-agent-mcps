# Rotated Indices

Source: https://www.chessprogramming.org/Rotated_Indices

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Rotated Indices**

[![](/images/thumb/1/18/Mittman_Yellow_Cherries.jpg/300px-Mittman_Yellow_Cherries.jpg)](http://www.barbaramittman.com/Site/Yellow_Cherries.html)

[Barbara Mittman](/Category:Barbara_Mittman "Category:Barbara Mittman") - Yellow Cherries [[1]](#cite_note-1)

**Rotated indices**,  
a deconcentrated version of [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards"), proposed by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani") [[2]](#cite_note-2) as used in his engine [Fortress](/Fortress_(Engine) "Fortress (Engine)"). Instead of using rotated bitboards with packed 15 [diagonals](/Diagonals "Diagonals") and 15 [anti-diagonals](/Anti-Diagonals "Anti-Diagonals") each, Alessandro applies an [array](/Array "Array") of 16 + 30 rotated indices for all 16 orthogonal and 30 diagonal lines on the board. Those indices are [incrementally updated](/Incremental_Updates "Incremental Updates") during [make](/Make_Move "Make Move")/[unmake](/Unmake_Move "Unmake Move"), which takes a tad more effort - but once updated, the rotated indices pay off, the more often they are used inside a [node](/Node "Node") of the [search](/Search "Search"). No further computation is required to look up attacks, pure indexed memory accesses.

The possible disadvantage - rotated indices, similar or slightly worse than rotated bitboards, are not as versatile as techniques relying on one occupancy bitboard only - if it is about a temporary change of the occupancy on the fly for [x-rays](/X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)") and [pinned pieces](/Pin "Pin") etc..

# See also

- [Flipping Mirroring and Rotating](/Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
- [Fortress](/Fortress_(Engine) "Fortress (Engine)")
- [Rotated Bitboards](/Rotated_Bitboards "Rotated Bitboards")
- [Rotated Indices in Gk](/Gk#SlidingAttacks "Gk")

# Forum Posts

- [Re: Rotated bitboards](http://groups.google.com/group/rec.games.chess.computer/msg/5c1c40a08c7176f8) by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 31, 1997
- [Re: Resources about rotated bitboards](https://www.stmintz.com/ccc/index.php?id=342812) by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), [CCC](/CCC "CCC"), January 16, 2004

# References

1. [↑](#cite_ref-1) [Still Lifes](http://www.barbaramittman.com/Site/Still_Lifes.html) by [Barbara Mittman](/Category:Barbara_Mittman "Category:Barbara Mittman")
2. [↑](#cite_ref-2) [Re: Rotated bitboards](http://groups.google.com/group/rec.games.chess.computer/msg/5c1c40a08c7176f8) by [Alessandro Damiani](/Alessandro_Damiani "Alessandro Damiani"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 31, 1997

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**