# Corresponding Squares

Source: https://www.chessprogramming.org/Corresponding_Squares

**[Home](/Main_Page "Main Page") \* [Evaluation](/Evaluation "Evaluation") \* [Game Phases](/Game_Phases "Game Phases") \* [Endgame](/Endgame "Endgame") \* [Pawn Endgame](/Pawn_Endgame "Pawn Endgame") \* Corresponding Squares**

[![](/images/b/b4/CoSq.jpg.png)](/File:CoSq.jpg.png)

6k1/3p4/3p4/3P4/4P1p1/6P1/8/K7 w - -

**Corresponding Squares**, also called **Co-ordinate Squares** is a concept to analyse pawn endgames. Using [retrograde analysis](/Retrograde_Analysis "Retrograde Analysis"), [Zugzwang](/Zugzwang "Zugzwang") positions and Critical Squares are found. Corresponding Squares Systems were one of the first human attempts of finding formulas and finally solving certain chess positions. This concept is only possible due to the limited mobility in pawn endgames. King-oppositions and Zugzwangs are the main motives arising.

# Theory

To get an idea, the concept is described using an example position by [Charles Dealtry Lockock](https://en.wikipedia.org/wiki/Charles_Dealtry_Locock), 1892 [[1]](#cite_note-1) :

## Finding Critical Squares

In the presented position there exist two critical squares. First when the white king reaches d4, white threatens 1. e5 dxe5 2. Kxe5 (threatening attacking both Pd7 and Pg4 in the next move). To defend this threat the black king must be able to move to f6 after Kd4. Secondly when the white king reaches e3, white threatens 1. Kf4 ... 2. Kxg4. In order to avoid this the black king must stand on g5.

To summarize, the two critical squares are e5 and f4. The according corresponding squares where both sides have mutual zugzwang are Kd4 - Kf6 and Ke3 - Kg5.

## Constructing Corresponding Square System

[![CoSq2.png](/images/3/3a/CoSq2.png)](/File:CoSq2.png)

This particular example, where two Corresponding Squares are connected diagonally and there is enough space for a 3x3 square, [Averbakh](https://en.wikipedia.org/wiki/Yuri_Averbakh) called the eight-square system. The construction of this Corresponding Square System starts with numbering the first two Corresponding Squares 1 and 2 accordingly. The square connecting the two receives the number 3. The outer squares of the 3x3 field receive the numbers 4 to 8. Further outside the numbering can continue by using the number of a square exactly two squares away either diagonally, horizontally or vertically. The image below should exemplify this process.

## Using the Corresponding Square System

The numbers tell us that if the white king manages to step on a square with the same number as the square on which the black king is standing, he automatically wins the fight for the critical squares. The same case occurs if the white king can step on a square the black king can not reach in the next move. The contrary is also possible. As soon as the black king moves on the same numbered square as the white king he can automatically defend the Corresponding Squares.

The way to take advantage of the Corresponding Square System is easy now. White must move towards the critical squares, never stepping on squares the black king can defend.

```
1. Kb1! (steps on 3, the black king can not reach any 3-squares) Kg7
2. Kc1 (steps on the same number as the black king: 5) Kg6
3. Kd1 Kg5 4. Kc2 Kh5 5. Kc3 Kg5 6. Kc4 Kg6 7. Kd3 Kg5 8. Ke3
```

# Computer Chess Implementation

First of all it must be noted that the concept of Corresponding Squares was designed to give the human chess player a tool to efficiently analyze a complex pawn endgame. Computers can very easily solve such positions using their Transposition Tables. Just as an example it takes Computers only a couple of seconds to reach > depth 20 in the [Lasker-Reichhelm position](/Lasker-Reichhelm_Position "Lasker-Reichhelm Position"), also referred as [Fine](https://en.wikipedia.org/wiki/Reuben_Fine) #70 [[2]](#cite_note-2) and thus find the opponent's Zugzwang. Nevertheless Computers also have some disadvantages. The main problem is the point where the chess engine has to decide whether to enter a certain pawn ending or not. Usually these positions offer a lot more mobility, thus conducting a deep enough search seems infeasible.

The first attempt of tackling Corresponding Squares with a computer chess engine was made by [Rafael B. Andrist](/Rafael_B._Andrist "Rafael B. Andrist") and his chess program [Wilhelm](/Wilhelm "Wilhelm") [[3]](#cite_note-3) [[4]](#cite_note-4). More recent research was done by [Edmund Moshammer](/Edmund_Moshammer "Edmund Moshammer"):

# Algorithm by Moshammer

In principle this approach is quite similar to an [Endgame Tablebase](/Endgame_Tablebases "Endgame Tablebases") Generation process. The main difference is its optimization to be used on the fly in chess engines. To represent the Corresponding Squares 64 [bitboards](/Bitboards "Bitboards") are used, which for every position of the attacking king represent the squares where the opponent king must stand to prevent the attacker from achieving a predefined objective.

Definitions:

```
U64 legalSq[2]; // stores the squares where attacking/defending king may move to
                //     (ie.: not attacked by a pawn or occupied by a own pawn)
U64 coSq[64];   // stores the Corresponding Squares for each attacking king position
U64 bbSQ[64];   // bbSQ[i] = 1 << i;
int kingmoves[8] = {-9, -8, -7, -1, 1, 7, 8, 9};  // used for move generation later

U64 mgen_fill_KING(U64 squares);  // shifts squares one step in all 8 directions
```

The main retrograde routine to build the Corresponding Square system:

- initialize coSq: for every position of the attacking king, the defending one may not stand on neighboring squares or squares previously defined illegal (attacked by attacker's pawns or occupied by own pawns)
- set changes to a full bitboard - ie: all squares have to be looked at in the first pass
- loop until all Zugzwang situations have been resolved:changes == 0
- loop through all unresolved positions of the board
  - reset the square on 'changes', as the position is being examined now
  - initialize Katt: squares from which the attacking King can move to attack the current square
  - initialize Kdef: squares from which the defending King can defend the attacking king to reach the current square - ie: the neighboring squares of the current square and the squares one king move away from the corresponding squares of the current position
  - for each of the attacking king moves
    - checks that the move is on the board and is part of the legal moves (Katt)
    - if coSq is changed on the resulting position, set 'changes' accordingly, so that the changes are considered in the next pass
    - the Corresponding Squares of each neighboring attacking King position have to collide with the Corresponding Squares one Kingmove away from this position

```
// attacker .. attacking side
// coSq ...... pointer to the Corresponding Squares Bitboards

void coSq_setupSystem(int attacker, U64 * coSq) {
  for (int i=0; i<64; i++) 
    coSq[i] &= ~mgen_fill_KING(bbSQ[i]) & ~bbSQ[i] & legalSq[!attacker];

  U64 changes = 0xFFFFFFFFFFFFFFFF;
  while (changes) {
    for (int i=0; i<64; i++) {
      if (changes & bbSQ[i]) {
        changes ^= bbSQ[i];
        U64 Katt = mgen_fill_KING(bbSQ[i]) & legalSq[attacker];
        U64 Kdef = mgen_fill_KING(bbSQ[i]) | mgen_fill_KING(coSq[i]);

        for (int j=0; j<8; j++) {
          int Ksq = i + kingmoves[j];
          if (!(Ksq & ~0x3F) && (bbSQ[Ksq] & Katt)) {
            changes |= bbSQ[Ksq] * ((coSq[Ksq] & ~Kdef) != 0);
            coSq[Ksq] &= Kdef;
          }
        }
      }
    }
  }
}
```

Before the function above is called, the Corresponding Squares must be initialized. Therefore all bits in the coSq-bitboards get set. Then the first Critical Squares are defined by setting the bitboard of the attacking king at the Critical Square to 0. In other words, if the king manages to occupy the square the defending king has no squares to stand on from which he can defend the threat.

The setupSystem function itself does nothing else than looping through the bitboards and uses the rule that the defending king may only stand on a square from which he can reach all corresponding squares the attacking king may create within one move. This is done as long as no further changes are made to the bitboard.

The time it takes to analyze a position is about linear. For the [Lasker-Reichhelm position](/Lasker-Reichhelm_Position "Lasker-Reichhelm Position") ([Fine](https://en.wikipedia.org/wiki/Reuben_Fine) #70), it took 10 cycles through the 64 squares of the board to find out that the black king can impossibly defend all of its pawns.

There is however one open question - the definition of the Critical Square. A straight forward approach would be to set the critical Squares to capturing the opponent's pawns. If in the end alpha > 0 and the defending king is standing on a Corresponding Square one can safely fail low at that point. A more complex approach would be necessary to find out whether a position is won or drawn.

# Publications

- [Vitaly Halberstadt](https://en.wikipedia.org/wiki/Vitaly_Halberstadt), [Marcel Duchamp](/Category:Marcel_Duchamp "Category:Marcel Duchamp") (**1932**). *L'opposition et les cases conjuguées sont réconciliées*.

:   Paris-Brussels 1932, German Edition 2001 *[Opposition und Schwesterfelder](http://www.buecher-nach-isbn.info/3-608/3608500359-Opposition-und-Schwesterfelder-Marcel-Duchamp-Vitali-Halberstadt-3-608-50035-9.html)*, ISBN 3-932170-35-0

- [Kenneth W. Church](/Kenneth_W._Church "Kenneth W. Church") (**1978**). *[Co-ordinate Squares: A Solution to Many Chess Pawn Endgames](http://dl.acm.org/citation.cfm?id=67030)*. B.Sc. thesis, [Massachusetts Institute of Technology](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), reprinted 1988 in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
- [Kenneth W. Church](/Kenneth_W._Church "Kenneth W. Church") (**1979**). *Co-ordinate Squares: A Solution to Many Chess Pawn Endgames*. abbreviated version of B.Sc. thesis, [IJCAI-79](/Conferences#IJCAI1979 "Conferences"), Tokyo, Japan
- [Peter W. Frey](/Peter_W._Frey "Peter W. Frey"), [Larry Atkin](/Larry_Atkin "Larry Atkin") (**1979**). *[Creating a Chess-Player, Part 4: Thoughts on Strategy](https://archive.org/stream/byte-magazine-1979-01/1979_01_BYTE_04-01_Life_Algorithms#page/n127/mode/2up)*. In [Blaise W. Liffick](http://cs.millersville.edu/~liffick/) (ed.), [The Byte Book of Pascal](http://books.google.com/books/about/The_BYTE_book_of_Pascal.html?id=ofpfQgAACAAJ), pp. 143-155. Byte Publications, also [BYTE, Vol. 4, No. 1](/Byte_Magazine#BYTE401 "Byte Magazine")
- [Mike Clarke](/Mike_Clarke "Mike Clarke") (**1980**). *The Theory of Coordinate Squares*. [Advances in Computer Chess 2](/Advances_in_Computer_Chess_2 "Advances in Computer Chess 2"), pp. 97-102
- [Yuri Averbakh](https://en.wikipedia.org/wiki/Yuri_Averbakh), [Ilia Maizelis](http://de.wikipedia.org/wiki/Ilja_Lwowitsch_Maiselis) (**1987**). *Comprehensive Chess Endings Vol 4: Pawn Endings*. Cadogan Books 1987
- [Karsten Müller](/Karsten_M%C3%BCller "Karsten Müller"), [Frank Lamprecht](https://en.wikipedia.org/wiki/Frank_Lamprecht) (**2000**). *Secrets of Pawn Endings*. [Everyman Chess](https://en.wikipedia.org/wiki/Everyman_Chess), (**2007**). [re-issue](http://dev.jeremysilman.com/shop/pc/Secrets-of-Pawn-Endings-p3748.htm) by [Gambit Publications](https://en.wikipedia.org/wiki/Gambit_Publications)
- [Karsten Müller](/Karsten_M%C3%BCller "Karsten Müller") (**2004**). *Endgame Corner - The Mystical Sister Squares*, [pdf](http://www.chesscafe.com/text/mueller38.pdf) from [ChessCafe.com](https://en.wikipedia.org/wiki/ChessCafe.com)
- [Omid David](/Eli_David "Eli David"), [Ariel Felner](/Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](/Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *Blockage Detection in Pawn Endgames*. [ICGA Journal, Vol. 27, No. 3](/ICGA_Journal#27_3 "ICGA Journal")

# Postings

- [chess program "Wilhelm" released](https://www.stmintz.com/ccc/index.php?id=184365) by [Rafael B. Andrist](/Rafael_B._Andrist "Rafael B. Andrist"), [CCC](/CCC "CCC"), August 19, 2001
- [Re: Fine 70 same 7 engines (more)](https://www.stmintz.com/ccc/index.php?id=188245) by [Rafael B. Andrist](/Rafael_B._Andrist "Rafael B. Andrist"), [CCC](/CCC "CCC"), September 10, 2001
- [A new(?) technique to recognize draws](https://www.stmintz.com/ccc/index.php?id=233270) by [Heiner Marxen](/Heiner_Marxen "Heiner Marxen"), [CCC](/CCC "CCC"), June 01, 2002 » [Chest](/Chest "Chest")
- [Corresponding squares, easy position](http://www.talkchess.com/forum/viewtopic.php?t=45238) by [Vincent Lejeune](/index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](/CCC "CCC"), September 20, 2012
- [Corresponding Squares 1](http://ruszchessstudies.blogspot.com/2016/11/corresponding-squares-1.html) by [Árpád Rusz](/%C3%81rp%C3%A1d_Rusz "Árpád Rusz"), [Chess Endgame Study Composition](http://ruszchessstudies.blogspot.com/), November 24, 2016

# External Links

- [Corresponding squares from Wikipedia](https://en.wikipedia.org/wiki/Corresponding_squares)
- [Chess improvement by effort: Corresponding squares](http://temposchlucker.blogspot.com/2006/02/corresponding-squares.html)
- [Chess Training: Corresponding Squares and Triangulation](http://chess-training.blogspot.com/2006/11/corresponding-squares-and-triangulation.html)
- [Chess Training: Endgame Lab - King and Pawn Endings](http://chess-training.blogspot.com/2006/11/endgame-lab-king-and-pawn-endings_24.html)

# References

1. [↑](#cite_ref-1) Position by [Charles Dealtry Lockock](https://en.wikipedia.org/wiki/Charles_Dealtry_Locock), 1892, from [Yuri Averbakh](https://en.wikipedia.org/wiki/Yuri_Averbakh), [Ilia Maizelis](https://lv.wikipedia.org/wiki/I%C4%BCja_Maizelis) (**1987**). *Comprehensive Chess Endings Vol 4: PawnEndings*. Cadogan Books
2. [↑](#cite_ref-2) [Reuben Fine](https://en.wikipedia.org/wiki/Reuben_Fine) (**1941**). *[Basic Chess Endings](https://en.wikipedia.org/wiki/Basic_Chess_Endings)*
3. [↑](#cite_ref-3) [chess program "Wilhelm" released](https://www.stmintz.com/ccc/index.php?id=184365) by [Rafael B. Andrist](/Rafael_B._Andrist "Rafael B. Andrist"), [CCC](/CCC "CCC"), August 19, 2001
4. [↑](#cite_ref-4) [Gegenfeldsysteme und Schachprogramm](http://www.mysnip.de/forum-archiv/thema/1578/299490/Gegenfeldsysteme+und+Schachprogramm.html) by [Rafael B. Andrist](/Rafael_B._Andrist "Rafael B. Andrist"), [ChessBits Forum](/ChessBits "ChessBits"), August 19, 2001 (German)

**[Up one level](/Pawn_Endgame "Pawn Endgame")**