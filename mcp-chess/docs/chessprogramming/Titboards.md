# Titboards

Source: https://www.chessprogramming.org/Titboards

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Titboards**

**Titboards**,  
a bitboard-based [move generation](/Move_Generation "Move Generation") technique invented by [Zach Wegner](/Zach_Wegner "Zach Wegner") [[1]](#cite_note-1) and first implemented by Malik Tremain [[2]](#cite_note-TDFA-2). Titboards are based on an extension of bitboards to ternary boards, hence the name ("bit" means binary digit, "tit" mean [ternary digit](https://en.wikipedia.org/wiki/Ternary_numeral_system)). Titboards are only used for move generation, not for any other purposes that typical bitboard attack-getters will be used for.

The idea of titboards is to eliminate [bitscans](/BitScan "BitScan"). Typical bitboard move generation techniques generate a bitboard, intersect it with the set of allowable [squares](/Squares "Squares") (empty or enemy-occupied), and then [serialize](/Bitboard_Serialization "Bitboard Serialization") that into a list of moves. Titboards take a bitboard occupancy for each side for just one rank, file, or diagonal, and convert them to ternary representations and add them together. This index can determine which squares can actually be moved to, instead of just attacked. It is used in a lookup table of 3^7=2187 entries per [direction](/Direction "Direction") per square.

Titboards are not typically used (there is one known engine that implements them [[2]](#cite_note-TDFA-2)). This is because they are currently slower than modern alternatives while being harder to implement. They require a large look-up table (~8.9 MB) and they work very differently from modern generation techniques likes [Magic Bitboards](/Magic_Bitboards "Magic Bitboards"), where they require each direction to be calculated individually {File, Rank, Diagonal, Anti-Diagonal}. For each direction they require the input of (square, us, them), as a pose to (square, occupied) which is more commonly used.

# Speed

Testing shows that titboards have no speed advantage over magic bitboards on modern hardware, however, the gap seemingly narrows on older CPUs that offer less efficient bitscan operations. A full array of results can be found here[[3]](#cite_note-3).

```
CPU: AMD Ryzen 9 5950X 16-Core Processor

Titboard perft group:
All tests completed with mean nps: 22290500

Pext perft group:
All tests completed with mean nps: 40633688

Magic Bitboard perft group:
All tests completed with mean nps: 37989088
```

```
CPU: Ryzen 5 5600x
Titboard perft group:
All tests completed with mean nps: 21250050

Pext perft group:
All tests completed with mean nps: 36773955

Magic Bitboard perft group:
All tests completed with mean nps: 34421651
```

# Forum Posts

- [Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623) by [Zach Wegner](/Zach_Wegner "Zach Wegner"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 22, 2006 » [Move Generation](/Move_Generation "Move Generation")

:   [Re: Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623&start=6) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), October 01, 2006 [[4]](#cite_note-4)

# References

1. [↑](#cite_ref-1) [Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623&p=27838) by [Zach Wegner](/Zach_Wegner "Zach Wegner"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 22, 2006
2. ↑ [2.0](#cite_ref-TDFA_2-0) [2.1](#cite_ref-TDFA_2-1) [TDFA - Titboard Engine](https://github.com/TiltedDFA/TDFA) by Malik Tremain, January 22, 2024
3. [↑](#cite_ref-3) [TDFA - Perft result comparison](https://github.com/TiltedDFA/TDFA/blob/3c4110f860f9c98b619a3f2565d139c92fe606c8/RunResults.txt)
4. [↑](#cite_ref-4) [Re: multi-dimensional piece/square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=52861&start=8) by Tony P., [CCC](/CCC "CCC"), January 28, 2020 » [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")

**[Up one level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**