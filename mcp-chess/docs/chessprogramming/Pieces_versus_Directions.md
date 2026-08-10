# Pieces versus Directions

Source: https://www.chessprogramming.org/Pieces_versus_Directions

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* Pieces versus Directions**

Despite the [generation of moves](/Move_Generation "Move Generation") to one [target square](/Target_Square "Target Square") by [pieces](/Pieces "Pieces") from different [directions](/Direction "Direction") as mentioned [Square Attacked By](/Square_Attacked_By "Square Attacked By"), there are two approaches to [generate](/Move_Generation "Move Generation") [moves](/Moves "Moves") in an [origin centric](/Origin_Square "Origin Square") manner to determine a set of distinct target squares. The classical approach, also applied in [Mailbox](/Mailbox "Mailbox") [array](/Array "Array") representation, is to generate [attacks](/Attacks "Attacks") and moves piece by piece. Alternately there are set-wise approaches, to determine distinct direction attacks for sets of multiple pieces and [pawns](/Pawn "Pawn"). [Sliding pieces](/Sliding_Pieces "Sliding Pieces") rely on [dumb7fill](/Dumb7Fill "Dumb7Fill"), [kogge-stone algorithm](/Kogge-Stone_Algorithm "Kogge-Stone Algorithm") or [fill by subtraction](/Fill_by_Subtraction "Fill by Subtraction").

# Piece by Piece

In general there are lookup techniques to determine attack- or move-target sets for each individual [pawn](/Pawn "Pawn") or [piece](/Pieces "Pieces"), indexed by [bitscanned](/BitScan "BitScan") square and for the sliders by occupancy. Each piece-wise attack covers all their inherited [ray- or knight directions](/Direction "Direction"). This classical approach traverses all pieces and generates attack sets and move sets by following techniques:

- [Pawn Push](/Pawn_Push "Pawn Push")
- [Attacks of a Single Pawn](/Pawn_Attacks_(Bitboards)#AttacksOfaSinglePawn "Pawn Attacks (Bitboards)")
- [Knight Attacks by Lookup](/Knight_Pattern#ByLookup "Knight Pattern")
- [King Attacks by Lookup](/King_Pattern#KingAttacks "King Pattern")
- [Single Sliding Piece Attacks](/Sliding_Piece_Attacks#SingleSlidingPieceAttacks "Sliding Piece Attacks")

As usual, [captures](/Captures "Captures") are determined by [intersection](/General_Setwise_Operations#Intersection "General Setwise Operations") of attacks with opponent pieces or [en passant](/En_passant "En passant") target, while all other attacks or push targets of empty squares are [quiet moves](/Quiet_Moves "Quiet Moves").

```
for all pieces {
  generateMovetargets(piece);
  for all capture targets
      generate captures (move or capture list)
  for all empty square targets
      generate quite moves (move list)
}
```

# Directions

The [direction-wise](/Direction "Direction") approach relies on following set-wise techniques to determine move-targets. As usual, [captures](/Captures "Captures") are determined by [intersection](/General_Setwise_Operations#Intersection "General Setwise Operations") of attacks with opponent pieces or [en passant](/En_passant "En passant") target, while all other attacks or push targets of empty squares are [quiet moves](/Quiet_Moves "Quiet Moves").

- [Pushes set-wise](/Pawn_Pushes_(Bitboards)#PawnPushSetwise "Pawn Pushes (Bitboards)")
- [Pawn Attacks set-wise](/Pawn_Attacks_(Bitboards)#PawnAttacks "Pawn Attacks (Bitboards)")
- [Multiple Knight Attacks](/Knight_Pattern#MultipleKnightAttacks "Knight Pattern")
- [King Attacks by Calculation](/King_Pattern#byCalculation "King Pattern") with [Direction-Steps](/General_Setwise_Operations#OneStepOnly "General Setwise Operations")
- [Multiple Sliding Pieces](/Sliding_Piece_Attacks#Multiple "Sliding Piece Attacks")

For [move generation](/Move_Generation "Move Generation") purpose one may store target-sets of different piece types per direction. Thus, 16 bitboards as a kind of unsorted [move list](/Move_List "Move List"). Each [target square](/Target_Square "Target Square") in each ray-direction set has an unique one-to-one relation to it's [source square](/Origin_Square "Origin Square").

```
for all 16 ray- and knight directions {
  generateMovetargets(dirtargets[dir], dir);
}
```

Likely this loop is unrolled - at least for the ray-attacks - where pawns, kings, bishops, rooks or queens may involved. See the proposal of [DirGolem](/DirGolem "DirGolem") for a branch-less direction-wise generation of [legal moves](/Legal_Move "Legal Move").

An incremental [finite state machine](https://en.wikipedia.org/wiki/Finite_state_machine) - move-getter may scan and reset the target squares per direction. For distant source squares of [sliding pieces](/Sliding_Pieces "Sliding Pieces"), one may [intersect](/General_Setwise_Operations#Intersection "General Setwise Operations") the [ray-wise masks](/On_an_empty_Board#RayAttacks "On an empty Board") per direction and [target-square](/Target_Square "Target Square") with the occupancy - to use either [bitscan](/BitScan "BitScan") [reverse](/BitScan#Bitscanreverse "BitScan") or [forward](/BitScan#Bitscanforward "BitScan") for the [positive](/On_an_empty_Board#PositiveRays "On an empty Board") or [negative](/On_an_empty_Board#NegativeRays "On an empty Board") directions - similar to the [classical approach](/Classical_Approach "Classical Approach"), except one don't needs the if (blocker) - condition, which is always true. However, one may delay determining the source square and moving piece until [make move](/Make_Move "Make Move") time, and to [encode moves](/Encoding_Moves "Encoding Moves") uniquely with target square (six bits) and direction (4 bits).

Alternatively, one may process a ray in one run, to bitscan the most farthest [destination square](/Target_Square "Target Square") from one distinct direction, i.e. bitscan reverse of positive ray attacks, and to loop over all intermediate targets by adding offsets until the source square is arrived. The below loop considers that move-target bits may already reset due to staged move generation, i.e. [hash move](/Hash_Move "Hash Move") or [killer moves](/Killer_Move "Killer Move") may already tried. Therefor the extra condition with *testAndResetBit* [[1]](#cite_note-1).

```
while ( northMoveTargets )
{
    targetSquare = bitScanReverse( northMoveTargets );
    sourceSquare = bitScanReverse( rayAttacks[sout][targetSquare] & occupied);
    storeMoveOrCapture( sourceSquare, targetSquare); 
    resetBit (northMoveTargets, targetSquare);
    targetSquare -= 8; 
    while ( targetSquare > sourceSquare) {
       if ( testAndResetBit (northMoveTargets, targetSquare) )
          storeMove( sourceSquare, targetSquare); 
       targetSquare -= 8; 
    }
}
```

# Hybrid

One may combine both approaches with usual [move lists](/Move_List "Move List"). For instance direction-wise attacks for all pawns, piece-wise attacks for none-pawns. The target set-of pawn-captures should be considered early, since this are winning or at least equal captures.

# See also

- [Bitboard Serialization](/Bitboard_Serialization "Bitboard Serialization")
- [BitScan](/BitScan "BitScan")
- [Classical Approach](/Classical_Approach "Classical Approach") of [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks")
- [DirGolem](/DirGolem "DirGolem")
- [Move Generation](/Move_Generation "Move Generation")
- [Square Attacked By](/Square_Attacked_By "Square Attacked By")

# External Links

- [Miles Davis](/Category:Miles_Davis "Category:Miles Davis") - [Call It Anything](https://en.wikipedia.org/wiki/A_Different_Kind_of_Blue), [Isle of Wight Festival](https://en.wikipedia.org/wiki/Isle_of_Wight_Festival_1970), August 29, 1970, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Miles Davis](/Category:Miles_Davis "Category:Miles Davis"), [Gary Bartz](https://en.wikipedia.org/wiki/Gary_Bartz), [Chick Corea](/Category:Chick_Corea "Category:Chick Corea"), [Keith Jarrett](/Category:Keith_Jarrett "Category:Keith Jarrett"), [Dave Holland](/Category:Dave_Holland "Category:Dave Holland"), [Jack DeJohnette](/Category:Jack_DeJohnette "Category:Jack DeJohnette"), [Airto Moreira](/Category:Airto_Moreira "Category:Airto Moreira") [[2]](#cite_note-2) [[3]](#cite_note-3)
:   [Directions](https://en.wikipedia.org/wiki/Bitches_Brew_Live#Track_listing) ([Joe Zawinul](/Category:Joe_Zawinul "Category:Joe Zawinul")) 0:00 (7:30), [Bitches Brew](https://en.wikipedia.org/wiki/Bitches_Brew) 7:30 (10:09), [It's About That Time](https://en.wikipedia.org/wiki/Live_at_the_Fillmore_East,_March_7,_1970:_It%27s_About_that_Time) 17:39 (6:17),
:   [Sanctuary](https://en.wikipedia.org/wiki/Bitches_Brew#Track_listing) ([Wayne Shorter](/Category:Wayne_Shorter "Category:Wayne Shorter")) 23:56 (1:10), [Spanish Key](https://en.wikipedia.org/wiki/Bitches_Brew) 25:06 (8:15), [The Theme](https://en.wikipedia.org/wiki/Bitches_Brew_Live) 33:21 (2:10)

# References

1. [↑](#cite_ref-1) [\_bittestandreset, \_bittestandreset64](http://msdn.microsoft.com/en-us/library/hd0hzyf8%28VS.100%29.aspx)
2. [↑](#cite_ref-2) [Does anyone know the name of the instrument Airto Moreira uses during the Isle of Wight Festival (1970)?](https://answers.yahoo.com/question/index?qid=20101214072119AASF0pn) | [Yahoo! Answers](https://en.wikipedia.org/wiki/Yahoo!_Answers)
3. [↑](#cite_ref-3) [Cuíca from Wikipedia](https://en.wikipedia.org/wiki/Cu%C3%ADca)

**[Up one Level](/Bitboards "Bitboards")**