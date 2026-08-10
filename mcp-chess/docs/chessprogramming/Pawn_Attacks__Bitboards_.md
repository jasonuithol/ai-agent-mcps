# Pawn Attacks (Bitboards)

Source: https://www.chessprogramming.org/Pawn_Attacks_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Pawn Attacks**

A pawn captures diagonally forward, and controls or [attacks](/Attacks "Attacks") one (rook pawn) or two squares one step ahead in diagonal [direction(s)](/Direction "Direction"). For white versus black pawns forward and backward are considered relative from either whites or blacks point of view.

# Single Pawn

## Attacks

To get attacks, we use a lookup of pre-calculated pawn-attacks, similar to knight- and king-attacks, except the need to consider color of the pawn.

```
whitePawnAttacks = arrPawnAttacks[white][sqOfWhitePawn];
if ( whitePawnAttacks & pieceBB[black] ) -> pseudo legal captures possible
```

```
arrPawnAttacks[white][d4]
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . 1 . 1 . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
```

## Captures

Only intersection with the opponent pieces is required.
We may include a possible [en passant](/En_passant "En passant") target square.

# Pawns set-wise

Working in the **bitboard centric** world to determine attacks and properties set-wise.

## Attacks

Generate all squares that are attacked by pawns of a color. It makes sense to keep disjoint sets for both attacking directions. For [move geneneration](/Move_Generation "Move Generation") purpose, disjoint east-west attacks has the advantage of unique source-target relation ship (+-7,9). After obtaining the direction-wise target-set a reverse shift is sufficient to get the source-set without further intersections and wrap issues.

*The code snippets rely on [shifting bitboards](/General_Setwise_Operations#ShiftingBitboards "General Setwise Operations"), specially by [one step only](/General_Setwise_Operations#OneStepOnly "General Setwise Operations").*

```
U64 wPawnEastAttacks(U64 wpawns) {return noEaOne(wpawns);}
U64 wPawnWestAttacks(U64 wpawns) {return noWeOne(wpawns);}

U64 bPawnEastAttacks(U64 bpawns) {return soEaOne(bpawns);}
U64 bPawnWestAttacks(U64 bpawns) {return soWeOne(bpawns);}
```

A bit-wise boolean instruction to combine those disjoint sets:

```
U64 wPawnAnyAttacks(U64 wpawns) {
   return wPawnEastAttacks(wpawns) | wPawnWestAttacks(wpawns);
}

U64 wPawnDblAttacks(U64 wpawns) {
   return wPawnEastAttacks(wpawns) & wPawnWestAttacks(wpawns);
}

U64 wPawnSingleAttacks(U64 wpawns) {
   return wPawnEastAttacks(wpawns) ^ wPawnWestAttacks(wpawns);
}
```

and similar for black.

```
 white pawns       white pawns << 9  &       notAFile     ==   wPawnEastAttacks
. . . . . . . .     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . . 
. . . . . . . .     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . . 
. . . . . . . .     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . . 
. . . . . . . .     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . . 
. . . . . . . .     h . . c . . . .      . 1 1 1 1 1 1 1      . . . c . . . . 
. . c . . . . .     . a b . d . f g      . 1 1 1 1 1 1 1      . a b . d . f g 
a b . d . f g h     . . . . . . . .      . 1 1 1 1 1 1 1      . . . . . . . . 
. . . . . . . .     / . . . . . . .      . 1 1 1 1 1 1 1      / . . . . . . . 

 white pawns       white pawns << 7  &       notHFile     ==  wPawnWestAttacks
. . . . . . . .     . . . . . . . .      1 1 1 1 1 1 1 .      . . . . . . . . 
. . . . . . . .     . . . . . . . .      1 1 1 1 1 1 1 .      . . . . . . . . 
. . . . . . . .     . . . . . . . .      1 1 1 1 1 1 1 .      . . . . . . . . 
. . . . . . . .     . . . . . . . .      1 1 1 1 1 1 1 .      . . . . . . . . 
. . . . . . . .     . c . . . . . .      1 1 1 1 1 1 1 .      . c . . . . . . 
. . c . . . . .     b . d . f g h .      1 1 1 1 1 1 1 .      b . d . f g h . 
a b . d . f g h     . . . . . . . a      1 1 1 1 1 1 1 .      . . . . . . . . 
. . . . . . . .     . . . . . . . \      1 1 1 1 1 1 1 .      . . . . . . . \ 

 white pawns                                                  wPawnAnyAttacks
. . . . . . . .                                               . . . . . . . .  
. . . . . . . .                                               . . . . . . . .  
. . . . . . . .                                               . . . . . . . .  
. . . . . . . .                                               . . . . . . . .  
. . . . . . . .                                               . c . c . . . .  
. . c . . . . .                                               b a 1 . 1 g 1 g  
a b . d . f g h                                               . . . . . . . .  
. . . . . . . .                                               . . . . . . . .
```

## Attack Maps

One idea to combine pawn-attacks is about safe squares or push-targets for white respectively black pawns. A kind if of set-wise static exchange evaluation - only considering pawn-attacks from both sides. A square is assumed safe, if the number of own pawn defends if greater or equal than opponent pawn attacks. That is true if the own side defends a square twice, or the opposite side has no attacks at all, or own side attacks once and opponent not twice.

```
U64 wSafePawnSquares(U64 wpawns, U64 bpawns) {
   U64 wPawnEastAttacks =  wPawnEastAttacks (wpawns);
   U64 wPawnWestAttacks =  wPawnWestAttacks (wpawns);
   U64 bPawnEastAttacks =  bPawnEastAttacks (bpawns);
   U64 bPawnWestAttacks =  bPawnWestAttacks (bpawns);
   U64 wPawnDblAttacks  =  wPawnEastAttacks &  wPawnWestAttacks;
   U64 wPawnOddAttacks  =  wPawnEastAttacks ^  wPawnWestAttacks;
   U64 bPawnDblAttacks  =  bPawnEastAttacks &  bPawnWestAttacks;
   U64 bPawnAnyAttacks  =  bPawnEastAttacks |  bPawnWestAttacks;
   return wPawnDblAttacks |~bPawnAnyAttacks | (wPawnOddAttacks &~bPawnDblAttacks);
}
```

Those attack maps are among other things useful to decide about [candidates](/Candidates_(Bitboards) "Candidates (Bitboards)") and [backward pawns](/Backward_Pawns_(Bitboards) "Backward Pawns (Bitboards)") .

## Captures

As usual, capture targets are the intersection of attack-sets with opponent pieces. Except [en passant](/En_passant "En passant") captures of course. A reverse shift of disjoint direction-wise sets obtains the pawns which may capture.

To find the pawn set, which can actually capture, on the fly, we can start with the target squares as well:

```
U64 wPawnsAble2CaptureEast(U64 wpawns, U64 bpieces) {
   return wpawns & bPawnWestAttacks(bpieces);
}

U64 wPawnsAble2CaptureWest(U64 wpawns, U64 bpieces) {
   return wpawns & bPawnEastAttacks(bpieces);
}

U64 wPawnsAble2CaptureAny(U64 wpawns, U64 bpieces) {
   return wpawns & bPawnAnyAttacks(bpieces);
}
```

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**