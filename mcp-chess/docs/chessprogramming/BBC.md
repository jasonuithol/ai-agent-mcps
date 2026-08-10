# BBC

Source: https://www.chessprogramming.org/BBC

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* BBC**

**BBC**, (Bit Board Chess)  
a didactic bitboard chess engine by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh") alias Code Monkey King, written in [C](/C "C"). BBC is subject of a [YouTube](https://en.wikipedia.org/wiki/YouTube) [video tutorial](https://en.wikipedia.org/wiki/Tutorial) started in summer 2020 [[1]](#cite_note-1), actually work in progress.
The [open source engine](/Category:Open_Source "Category:Open Source") is further published on [GitHub](https://en.wikipedia.org/wiki/GitHub) [[2]](#cite_note-2), and will be compliant to the [UCI](/UCI "UCI") protocol.
While the series offers a nice introduction in chess engine programming and [bitboard](/Bitboards "Bitboards") techniques,
the advanced approach of [Magic Bitboards](/Magic_Bitboards "Magic Bitboards") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") with all its lengthy initialization topics might be hard to understand and deterrent for the intended novice target group.
The linewise approaches of [First Rank Attacks](/First_Rank_Attacks "First Rank Attacks") to introduce occupancy lookups, followed by [Kindergarten Bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards") - as intermediate step towards magics bitboards - seem didactically more appropriate. Anyway, a valuable video series covering various aspects of computer chess programming. **BBC 1.0** was released on September 24, 2020 [[3]](#cite_note-3), **BBC 1.3** on October 21, 2020, utilizing [Stockfish's NNUE](/Stockfish_NNUE "Stockfish NNUE") evaluation via [Daniel Shawul's](/Daniel_Shawul "Daniel Shawul") [Scorpio NNUE](/Scorpio#ScorpioNNUE "Scorpio") [egbbdll](/Scorpio#Bitbases "Scorpio") probing library [[4]](#cite_note-4).

# See also

- [BMCP](/BMCP "BMCP")
- [PeSTO](/PeSTO "PeSTO")
- [Vice](/Vice "Vice")

# Forum Posts

- [Comparing 4 move generators: 0x88 vs 10x12 vs 10x12 + bitboards HYBRID vs Pure MAGIC BITBOARDS](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74917) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), August 28, 2020
- [Bitboard CHESS ENGINE in C: YouTube series by Code Monkey King](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75017) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), September 06, 2020
- [Zobrist hashing tutorials on YouTube](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75155) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), September 19, 2020
- [BBC 1.0 release - UCI chess engine by CMK](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75199) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), September 24, 2020
- [How to rate my engine in CCRL?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75204) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), September 25, 2020 » [CCRL](/CCRL "CCRL")
- [BBC GUI release - PLAY IT ONLINE!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75380) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 12, 2020 » [Web GUI Tutorial](#GUI)
- [How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 17, 2020 » [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE"), [Scorpio NNUE](/Scorpio#NNUE "Scorpio")

:   [Re: How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415&start=3) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), October 17, 2020

- [Embedding Stockfish NNUE to ANY CHESS ENGINE: YouTube series](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75418) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 17, 2020 » [NNUE](/NNUE "NNUE")
- [BBC 1.3 + Stockfish NNUE released!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75482) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 21, 2020
- [BBC 1.4 + Stockfish NNUE + Online GUI + Opening book - FINAL RELEASE!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75541) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 25, 2020
- [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle"), [CCC](/CCC "CCC"), June 17, 2021 » [NNUE](/NNUE "NNUE")

# External Links

## GitHub

- [GitHub - maksimKorzh/bbc: Bit Board Chess (BBC) - The easiest to understand bitboard chess engine by Code Monkey King](https://github.com/maksimKorzh/bbc)
- [GitHub - maksimKorzh/uci-gui: Web based GUI for UCI chess engine](https://github.com/maksimKorzh/uci-gui)

## YouTube

### BBC

**Bitboard CHESS ENGINE in C**

1. [Intro](https://youtu.be/QUNP-UjujBM) » [Bitboards](/Bitboards "Bitboards")
2. [Creating comfortable conditions for development](https://youtu.be/o-ySJ2EBarY)
3. [Generating pre-calculated PAWN ATTACK tables](https://youtu.be/OTWG4dERdSc) » [Pawn Attacks (Bitboards)](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)")
4. [Generating pre-calculated KNIGHT ATTACK table](https://youtu.be/nZLuLn9JW0E) » [Knight Attacks](/Knight_Pattern#KnightAttacks "Knight Pattern")
5. [Generating pre-calculated KING ATTACK tables](https://youtu.be/dWfwcfWg4XY) » [King Attacks](/King_Pattern#KingAttacks "King Pattern")
6. [Masking relevant bishop occupancy bits to form a key for MAGIC BITBOARDS](https://youtu.be/Obe1-u3S0Y4) » [Magic Bitboards](/Magic_Bitboards "Magic Bitboards")
7. [Masking relevant ROOK OCCUPANCY BITS to form a key for MAGIC BITBOARDS](https://youtu.be/bL7LW3jntw0)
8. [Generating SLIDER PIECES ATTACKS on the fly for MAGIC BITBOARD purposes](https://youtu.be/XFiZ3tjt7K4) » [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks")
9. [Implementing BIT COUNT routine (Brian Kernighan's way)](https://youtu.be/0F_aeUik91A) » [Population Count - Brian Kernighan's way](/Population_Count#BrianKernighansway "Population Count")
10. [Getting least significant 1st BIT INDEX](https://youtu.be/JhLgV2P9sBg) » [Index of LS1B by Popcount](/BitScan#Index_of_LS1B_by_Popcount "BitScan")
11. [Populating OCCUPANCY sets to multiply them later by MAGIC NUMBERS](https://youtu.be/nyk3usU95IY)
12. [Generating relevant OCCUPANCY BIT COUNT lookup tables for sliding pieces](https://youtu.be/gaXLyW-yMvg)
13. [Implementing pseudo RANDOM NUMBER generator using XORSHIFT32 algorithm](https://youtu.be/JjFYmkUhLN4) » [Pseudorandom Number Generator](/Pseudorandom_Number_Generator "Pseudorandom Number Generator")
14. [Generating MAGIC NUMBER candidates](https://youtu.be/KqWeOVyOoyU) » [Looking for Magics](/Looking_for_Magics "Looking for Magics")
15. [Generating MAGIC NUMBERS via brute force trial and error method](https://youtu.be/UnEu5GOiSEs)
16. [Initializing SLIDER PIECES attack tables using PLAIN MAGIC BITBOARDS](https://youtu.be/1lAM8ffBg0A) » [Plain Magic Bitboards](/Magic_Bitboards#Plain "Magic Bitboards")
17. [Defining BITBOARDS, OCCUPANCIES and helper variables](https://youtu.be/ZBBju42pKvw) » [Bitboard Board-Definition](/Bitboard_Board-Definition "Bitboard Board-Definition")
18. [Printing CHESS BOARD position and game state variables](https://youtu.be/iJ0VpXq90zY) » [Chess Position](/Chess_Position "Chess Position")
19. [Parsing FEN string to initialize BITBOARDS, OCUUPANCIES & board state](https://youtu.be/IdFHFRiQtj8) » [Forsyth-Edwards Notation](/Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
20. [Getting QUEEN ATTACKS by looking up bishop & rook attack tables](https://youtu.be/KSs4KRQPOKE)
21. [Implementing routine to find out whether SQUARE IS ATTACKED](https://youtu.be/v9CEqjliv3E) » [Square Attacked By](/Square_Attacked_By "Square Attacked By")
22. [Writing GENERATE MOVES function skeleton](https://youtu.be/eRvCLaa-3Rk) »[Move Generation](/Move_Generation "Move Generation")
23. [Generating QUIET PAWN moves](https://youtu.be/62Hy1JEehqI) » [Pawn Pushes (Bitboards)](/Pawn_Pushes_(Bitboards) "Pawn Pushes (Bitboards)")
24. [Generating PAWN CAPTURE moves](https://youtu.be/cezEoX8WpWs) » [Pawn Captures](/Pawn_Attacks_(Bitboards)#PawnCaptures "Pawn Attacks (Bitboards)")
25. [Generating CASTLING MOVES](https://youtu.be/TXvV2jVl7co) » [Castling](/Castling "Castling")
26. [Generating SLIDER & LEAPER piece MOVES by attack tables lookup](https://youtu.be/clNvT1W93o4)
27. [Binary formatting of MOVE ITEMS](https://youtu.be/ubX5lyIQoSs) » [Encoding Moves](/Encoding_Moves "Encoding Moves")
28. [Encoding & decoding MOVE ITEMS](https://youtu.be/gyf3mr1LI7A)
29. [Implementing MOVE LIST + ADD MOVE, PRINT MOVE, PRINT MOVE LIST functions](https://youtu.be/AINYYiV-83I) » [Move List](/Move_List "Move List")
30. [Populating MOVE LIST with newly GENERATED MOVES](https://youtu.be/944aTQQnWAA)
31. [Preserving & restoring BOARD STATE aka COPY/MAKE approach](https://youtu.be/CsUelozl0a8) » [Copy-Make](/Copy-Make "Copy-Make")
32. [Implementing MAKE MOVE function (moving pieces)](https://youtu.be/coVPpTJN9iU) » [Make Move](/Make_Move "Make Move")
33. [Implementing MAKE MOVE function (handling captures)](https://youtu.be/nkRrQnhRo80) » [Captures](/Captures "Captures")
34. [Implementing MAKE MOVE function (handling pawn promotions)](https://youtu.be/gnDyJImkfVo) » [Promotions](/Promotions "Promotions")
35. [Implementing MAKE MOVE function (handling enpassant moves)](https://youtu.be/5h5Z3bx0EKc) » [En passant](/En_passant "En passant")
36. [Implementing MAKE MOVE function (handling double pawn pushes)](https://youtu.be/J-k2p1g6VTQ) » [Double Pawn Push](/Pawn_Push#DoublePush "Pawn Push")
37. [Implementing MAKE MOVE function (handling castling moves)](https://youtu.be/pHohRpH30a0) » [Castling](/Castling "Castling")
38. [Implementing MAKE MOVE function (updating castling rights)](https://youtu.be/zOWPZ4fuLGg) » [Castling Rights](/Castling_Rights "Castling Rights")
39. [Implementing MAKE MOVE function (updating occupancy bitboards)](https://youtu.be/ZBotXGrgbdg) » [Occupancy](/Occupancy "Occupancy")
40. [Implementing MAKE MOVE function (checking whether the king is in check)](https://youtu.be/sg4AMsXYuk4) » [Check](/Check "Check")
41. [Writing a cross-platform function for GETTING TIME IN MILLISECONDS](https://youtu.be/bK_dg_gMW6s)
42. [Writing PERFT DRIVER function](https://youtu.be/o0xCJDhbSUM) » [Perft](/Perft "Perft")
43. [Writing PERFT TEST function](https://youtu.be/p2VuC0xTPoc)
44. [Connecting to the GUI (parse move string)](https://youtu.be/1gOYB9HelXk) » [GUI](/GUI "GUI"), [UCI](/UCI "UCI")
45. [Connecting to the GUI (parse "position" command)](https://youtu.be/giSqiH6aa_o)
46. [Connecting to the GUI (parse "go" command)](https://youtu.be/lb46nX6gSBw)
47. [Connecting to the GUI (main loop) + BONUS (TSCP vs BBC blitz game)](https://youtu.be/rW2jzTA4kW4) » [TSCP](/TSCP "TSCP")
48. [Implementing RUDIMENTARY EVALUATION (material score)](https://youtu.be/CMshozGbBdw) » [Evaluation](/Evaluation "Evaluation"), [Material](/Material "Material")
49. [Implementing RUDIMENTARY EVALUATION (positional piece scores)](https://youtu.be/E2JzRNI1ODI)
50. [Writing NEGAMAX ALPHA BETA skeleton](https://youtu.be/b8OcJM3VeaU) » [Negamax](/Negamax "Negamax"), [Alpha-Beta](/Alpha-Beta "Alpha-Beta")
51. [Detecting CHECKMATE and STALEMATE](https://youtu.be/lAAdjCkWd9s) » [Checkmate](/Checkmate "Checkmate"), [Stalemate](/Stalemate "Stalemate")
52. [Implementing QUIESCENCE SEARCH](https://youtu.be/WzEhVjdNByg) » [Quiescence Search](/Quiescence_Search "Quiescence Search")
53. [Defining MVV LVA (Most Valuable Victim - Least Valuable Attacker) table](https://youtu.be/NMNBWxinpPY) » [MVV/LVA](/MVV-LVA "MVV-LVA")
54. [Writing SCORE MOVE function](https://youtu.be/VeJnLN7jFm4) » [Move Ordering](/Move_Ordering "Move Ordering")
55. [Writing SORT MOVES function](https://youtu.be/3-9tzzmtQQ0)
56. [Applying MOVE ORDERING to sort captures](https://youtu.be/DVSp_31iTBU) » [Captures](/Captures "Captures")
57. [Sorting KILLER & HISTORY moves](https://youtu.be/MA6d1hZ1YBE) » [Killer Heuristic](/Killer_Heuristic "Killer Heuristic"), [History Heuristic](/History_Heuristic "History Heuristic")
58. [Collecting PV (Principle Variation) from the search](https://youtu.be/LOR-dkAkUyM) » [Principal Variation](/Principal_Variation "Principal Variation")
59. [Implementing ITERATIVE DEEPENING](https://youtu.be/yVyQSUYts0A) » [Iterative Deepening](/Iterative_Deepening "Iterative Deepening")
60. [Sorting PV moves + some BONUS TALK at the end](https://youtu.be/heJUljl_zNE)
61. [Implementing PVS (Principle Variation Search)](https://youtu.be/Gs4Zk6aihyQ) » [Principal Variation Search](/Principal_Variation_Search "Principal Variation Search")
62. [Applying LMR (Late Move Reduction)](https://youtu.be/OLT0bU0SIeg) » [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
63. [Applying NULL MOVE PRUNING](https://youtu.be/n6xAzopULxU) » [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
64. [Adjusting ASPIRATION WINDOW during iterative deepening](https://youtu.be/1LmdOHshYkI) » [Aspiration Windows](/Aspiration_Windows "Aspiration Windows")
65. [BUG ALERT!!! Fixing PVS duplication bug](https://youtu.be/azEmgbdiecc)
66. [Handling TIME CONTROLS (forked from VICE by BluefeverSoftware)](https://youtu.be/t48NYINOekw) » [Vice](/Vice "Vice")
67. [Zobrist HASHING (initialize random keys)](https://youtu.be/W7dah-dat8Q) » [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")
68. [Zobrist HASHING (generate hash key)](https://youtu.be/sV2C7hx-gOE)
69. [Zobrist HASHING (hash keys incremental updates)](https://youtu.be/5EMLgIFv5Qg) » [Incremental Updates](/Incremental_Updates "Incremental Updates")
70. [Implementing HASH TABLE aka transposition table (define & initialize)](https://youtu.be/fEHjpzrcRxk) » [Transposition Table](/Transposition_Table "Transposition Table") [[5]](#cite_note-5)
71. [Implementing HASH TABLE aka transposition table (read/write hash entry)](https://youtu.be/NcboP08y_JQ)
72. [Implementing HASH TABLE aka transposition table (connecting to search)](https://youtu.be/HNtAt9RMJVs)
73. [BUG ALERT! Fixing lack of enpassant & side hashing on null move](https://youtu.be/4SXKBTGUkjk)
74. [More search BUG FIXES &CLEANUPS](https://youtu.be/g1b_rT9VqAw)
75. [Handling MATING SCORES in HASH TABLE aka transposition table](https://youtu.be/XfeuxubYlT0) » [Mate Scores](/Score#MateScores "Score")
76. [Sending MATING SCORES to GUI + some cleanups & adjustments](https://youtu.be/WcoOTg7Aq4E)
77. [Detecting THREE FOLD REPETITIONS](https://youtu.be/QhFtquEeffA) » [Repetitions](/Repetitions "Repetitions")
78. [Final (hopefully!) SEARCH BUG FIXES](https://youtu.be/F8ueIueVsHI)
79. [Improving EVALUATION (setting file & rank masks)](https://youtu.be/Yqpm6Ad4scI) » [Evaluation](/Evaluation "Evaluation"), [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")
80. [Improving EVALUATION (initializing isolated & passed pawn masks)](https://youtu.be/iwBkAEC4KSs) » [Isolated Pawns (Bitboards)](/Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)"), [Passed Pawns (Bitboards)](/Passed_Pawns_(Bitboards) "Passed Pawns (Bitboards)")
81. [Improving EVALUATION (double & isolated penalties, passed pawns bonus)](https://youtu.be/CgvZMsJImJg)
82. [Improving EVALUATION (open & semi open file scoring)](https://youtu.be/Bp4F_321j4I) » [Pawns and Files (Bitboards)](/Pawns_and_Files_(Bitboards) "Pawns and Files (Bitboards)"), [Open File](/Open_File "Open File")
83. [Improving EVALUATION (mobility and king safety)](https://youtu.be/iq2lxyjWZvA) » [Mobility](/Mobility "Mobility"), [King Safety](/King_Safety "King Safety")
84. [BBC 1.0 - RELEASE](https://youtu.be/1SgnTKzWuss)
85. [Improving BBC chess engine: TAPERED EVALUATION (getting game phase scores)](https://youtu.be/JYF6A0xvvtY) » [Tapered Eval](/Tapered_Eval "Tapered Eval"), [PeSTO](/PeSTO "PeSTO")
86. [Improving BBC chess engine: TAPERED EVALUATION (interpolating scores) + BONUS: BBC vs VICE match!](https://youtu.be/bOmXClI6Xpw) » [Vice](/Vice "Vice")

### [GUI](/GUI "GUI")

**Web based GUI for UCI CHESS ENGINE**

1. [INTRO & DEMO](https://youtu.be/_0uKZbHWVKM)
2. [Install dependencies, CREATE WEB APP & render the CHESS BOARD](https://youtu.be/OjZy52Tt6mY)
3. [Connecting engine back-end & MAKING IT PLAY!](https://youtu.be/9Hn1gnTYNS4)
4. [Printing game status, FEN & PGN](https://youtu.be/ZIyDWQN2buk)
5. [Adding GAME CONTROL buttons](https://youtu.be/ihHHW_CA72M)
6. [Adding MOVE STATS](https://youtu.be/TlxgZRd8VWk)
7. [Fixing layout & setting position from FEN string on button click](https://youtu.be/PWnypt2k56I)
8. [Adding MOVE TIME & FIXED DEPTH controls](https://youtu.be/DCWtkpEF8KY)
9. [Implementing DOWNLOAD PGN feature](https://youtu.be/tqR4tRyfTIg)
10. [Encapsulating CHESS ENGINE for SIMULTANEOUS PLAY](https://youtu.be/w67CEEjqIjw)
11. [final adjustments and DEPLOY at pythonanywhere.com](https://youtu.be/_u-VAFwY95U)

### [NNUE](/NNUE "NNUE")

**Embedding Stockfish NNUE to ANY CHESS ENGINE**

1. [Intro & demo](https://youtu.be/zieTAE2zN9w) » [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE"), [Scorpio NNUE](/Scorpio#NNUE "Scorpio")
2. [Compiling existing ENGINE with NNUE library](https://youtu.be/59Fp4JVNob0)
3. [Extracting PIECES & SQUARES for direct NNUE probing](https://youtu.be/puLvzQnUoH8)
4. [Incorporating NNUE SCORES into EVALUATION function](https://youtu.be/cOdPe1JvVU8)
5. [bug fixes & experiments](https://youtu.be/30L9hx6hsmg)
6. [WINDOWS compatibility added](https://youtu.be/xFeJ9PBWpco)
7. [Switching to pure NNUE evaluation + important BUG FIX](https://youtu.be/Olnk9aa1zMI)

# References

1. [↑](#cite_ref-1) [Bitboard CHESS ENGINE in C: intro](https://youtu.be/QUNP-UjujBM)
2. [↑](#cite_ref-2) [GitHub - maksimKorzh/bbc: Bit Board Chess (BBC) - The easiest to understand bitboard chess engine by Code Monkey King](https://github.com/maksimKorzh/bbc)
3. [↑](#cite_ref-3) [BBC 1.0 release - UCI chess engine by CMK](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75199) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), September 24, 2020
4. [↑](#cite_ref-4) [BBC 1.3 + Stockfish NNUE released!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75482) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 21, 2020
5. [↑](#cite_ref-5) [The Main Transposition Table](http://web.archive.org/web/20070809015843/www.seanet.com/%7Ebrucemo/topics/hashing.htm) from [Bruce Moreland's](/Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)

**[Up one Level](/Engines "Engines")**