# Defended Pawns (Bitboards)

Source: https://www.chessprogramming.org/Defended_Pawns_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Defended Pawns**

Each pawn, member of the own [pawn attack set](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)") is obviously **defended** by a pawn, thus likely not a winning capture target for opponent pieces (except pawns). If a defended pawn is [open](/Open_Pawns_(Bitboards) "Open Pawns (Bitboards)"), opponent rooks on [half-open](/Pawns_and_Files_(Bitboards)#HalfopenFiles "Pawns and Files (Bitboards)") files bang one's head against a brick wall.

*Working in the bitboard centric world to determine pawn related pattern set-wise*.

# Defended

Again, it is advantageous to keep disjoint east-west attack sets for a unique 1:1 source-target relationship. On demand we can use the union or intersection on the fly. Note that attack direction is related to the target square. East attack is from south/north-west to north/south-east

```
white pawns         defended            defended
                    from west ->        from east <-
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . 1 . . .     . . . . . . . .
. . . 1 . . 1 .     . . . 1 . . . .     . . . . . . 1 .
. . 1 . . . . 1     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
```

```
U64 wPawnDefendedFromWest(U64 wpawns) {
   return wpawns & wPawnEastAttacks(wpawns);
}

U64 wPawnDefendedFromEast(U64 wpawns) {
   return wpawns & wPawnWestAttacks(wpawns);
}
```

# Defenders

To get the set of defenders on the fly, we use the intersection of white pawns with it's "black" attacks:

```
white pawns         defenders           defenders
                    from west           from east
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . . . . .     . . . . . . . .
. . . 1 . . 1 .     . . . 1 . . . .     . . . . . . . .
. . 1 . . . . 1     . . 1 . . . . .     . . . . . . . 1
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
```

```
U64 wPawnDefendersFromWest(U64 wpawns) {
   return wpawns & bPawnWestAttacks(wpawns);
}

U64 wPawnDefendersFromEast(U64 wpawns) {
   return wpawns & bPawnEastAttacks(wpawns);
}
```

Otherwise, if the set of defenders was already determined (or vice versa), we can already take advantage of the unique target/source relation ship:

```
wPawnDefendersFromWest = wPawnDefendedFromWest >> 9;
wPawnDefendersFromEast = wPawnDefendedFromEast >> 7;
```

# Defended Defenders

Defended defenders already are the inner pawns of a at least [triple-chain](/Pawn_Chain "Pawn Chain"), the d5 pawn for instance:

```
white pawns         defended            defended
                    from west           from east
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . 1 . . .     . . . . . . . .
. . . 1 . . 1 .     . . . 1 . . . .     . . . . . . 1 .
. . 1 . . . . 1     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

white pawns         defenders           defenders
                    from west           from east
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . . . . .     . . . . . . . .
. . . 1 . . 1 .     . . . 1 . . . .     . . . . . . . .
. . 1 . . . . 1     . . 1 . . . . .     . . . . . . . 1
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

                    defenders and       defenders and
white pawns         defended            defended
                    from west           from east
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . . . . .     . . . . . . . .
. . . 1 . . 1 .     . . . 1 . . . .     . . . . . . . .
. . 1 . . . . 1     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
```

# Not Defended Defenders

Not defended defenders are the base of a [chain](/Pawn_Chain "Pawn Chain") - target of opponent attacks:

```
                    not defended        not defended
white pawns         defenders           defenders
                    from west           from east
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . . . . .     . . . . . . . .
. . . 1 . . 1 .     . . . . . . . .     . . . . . . . .
. . 1 . . . . 1     . . 1 . . . . .     . . . . . . . 1
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
```

# Not Defending Defended

Defended pawns not defending other pawns are likely the peak of a [chain](/Pawn_Chain "Pawn Chain").

```
                    not defending       not defending
white pawns         defended            defended
                    from west           from east
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . 1 . . .     . . . . 1 . . .     . . . . . . . .
. . . 1 . . 1 .     . . . . . . . .     . . . . . . 1 .
. . 1 . . . . 1     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
```

# Forum Posts

- [pattern coding in bitboards](http://www.talkchess.com/forum/viewtopic.php?t=55477) by [Pawel Koziol](/Pawel_Koziol "Pawel Koziol"), [CCC](/CCC "CCC"), February 26, 2015 » [Pawn Chain](/Pawn_Chain "Pawn Chain")

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**