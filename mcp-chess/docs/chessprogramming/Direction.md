# Direction

Source: https://www.chessprogramming.org/Direction

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Squares](/Squares "Squares") \* Direction**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/WInd_Rose_Aguiar.png/330px-WInd_Rose_Aguiar.png)](/File:WInd_Rose_Aguiar.png)

wind rose [[1]](#cite_note-1)

The **Direction** is a information of the geometrical relation of two squares on a [chessboard](/Chessboard "Chessboard") without the information of [distance](/Distance "Distance"). Mathematically, direction may be uniquely specified by a [unit vector](https://en.wikipedia.org/wiki/Unit_vector), or equivalently by the [angle](https://en.wikipedia.org/wiki/Angle) with respect to a specified set of axes.

# Move Directions

Directions on the chessboard are usually related to from- to-coordinates of [moves](/Moves "Moves"), that is four orthogonal and four diagonal ray-directions plus the eight directions a [knight](/Knight "Knight") may move. Following [Compass roses](https://en.wikipedia.org/wiki/Compass_rose) give the directions and single step increments of an [8x8 Board](/8x8_Board "8x8 Board").

## Ray Directions

```
  northwest    north   northeast
  noWe         nort         noEa
          +7    +8    +9
              \  |  /
  west    -1 <-  0 -> +1    east
              /  |  \
          -9    -8    -7
  soWe         sout         soEa
  southwest    south   southeast
```

## Knight Directions

```
        noNoWe    noNoEa
            +15  +17
             |     |
noWeWe  +6 __|     |__+10  noEaEa
              \   /
               >0<
           __ /   \ __
soWeWe -10   |     |   -6  soEaEa
             |     |
            -17  -15
        soSoWe    soSoEa
```

# Directions between any Squares

## In Degrees

Based on [arctangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the quotient of [file-](/Files#FileDistance "Files") and [rank-distance](/Ranks#RankDistance "Ranks"), one may calculate following 15 times 15 sheet with all possible angels which might occur between any squares in [Degree](https://en.wikipedia.org/wiki/Degree_%28angle%29) (rounded to integer). Inner squares whose angle occur on farther squares are left blank, so each angle given is distinct, 144 from 224 (15x15-1), move directions are given in bold:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **315** | 319 | 324 | 330 | 337 | 344 | 352 | **0** | 8 | 16 | 23 | 30 | 36 | 41 | **45** |
| 311 |  | 320 | 326 | **333** | 342 | 351 | | | 9 | 18 | **27** | 34 | 40 |  | 49 |
| 306 | 310 |  | 321 | 329 | 338 | 349 | | | 11 | 22 | 31 | 39 |  | 50 | 54 |
| 300 | 304 | 309 |  | 323 |  | 346 | | | 14 |  | 37 |  | 51 | 56 | 60 |
| 293 | **297** | 301 | 307 |  |  |  | | |  |  |  | 53 | 59 | **63** | 67 |
| 286 | 288 | 292 |  |  |  |  | | |  |  |  |  | 68 | 72 | 74 |
| 278 | 279 | 281 | 284 |  |  |  | | |  |  |  | 76 | 79 | 81 | 82 |
| **270** | - | - | - | - | - | - | + | - | - | - | - | - | - | **90** |
| 262 | 261 | 259 | 256 |  |  |  | | |  |  |  | 104 | 101 | 99 | 98 |
| 254 | 252 | 248 |  |  |  |  | | |  |  |  |  | 112 | 108 | 106 |
| 247 | **243** | 239 | 233 |  |  |  | | |  |  |  | 127 | 121 | **117** | 113 |
| 240 | 236 | 231 |  | 217 |  | 194 | | | 166 |  | 143 |  | 129 | 124 | 120 |
| 234 | 230 |  | 219 | 211 | 202 | 191 | | | 169 | 158 | 149 | 141 |  | 130 | 126 |
| 229 |  | 220 | 214 | **207** | 198 | 189 | | | 171 | 162 | **153** | 146 | 140 |  | 131 |
| **225** | 221 | 216 | 210 | 203 | 196 | 188 | **180** | 172 | 164 | 157 | 150 | 144 | 139 | **135** |

## In Begrees

Enumerating all distinct integer degrees of the above rose in order but without any gaps, leaves a circle with 144 board degrees (Begrees) - only the 16 angels with modulo 9 equals zero are actually covered by move directions (bold). A possible application of Begrees is to select moves with a direction to an "interesting" area of the board, specified by some center- or gravity square.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **126** | 127 | 131 | 134 | 136 | 139 | 143 | **0** | 1 | 5 | 8 | 10 | 13 | 17 | **18** |
| 125 |  | 128 | 132 | **135** | 138 | 142 | | | 2 | 6 | **9** | 12 | 16 |  | 19 |
| 121 | 124 |  | 129 | 133 | 137 | 141 | | | 3 | 7 | 11 | 15 |  | 20 | 23 |
| 118 | 120 | 123 |  | 130 |  | 140 | | | 4 |  | 14 |  | 21 | 24 | 26 |
| 116 | **117** | 119 | 122 |  |  |  | | |  |  |  | 22 | 25 | **27** | 28 |
| 113 | 114 | 115 |  |  |  |  | | |  |  |  |  | 29 | 30 | 31 |
| 109 | 110 | 111 | 112 |  |  |  | | |  |  |  | 32 | 33 | 34 | 35 |
| **108** | - | - | - | - | - | - | + | - | - | - | - | - | - | **36** |
| 107 | 106 | 105 | 104 |  |  |  | | |  |  |  | 40 | 39 | 38 | 37 |
| 103 | 102 | 101 |  |  |  |  | | |  |  |  |  | 43 | 42 | 41 |
| 100 | **99** | 97 | 94 |  |  |  | | |  |  |  | 50 | 47 | **45** | 44 |
| 98 | 96 | 93 |  | 86 |  | 76 | | | 68 |  | 58 |  | 51 | 48 | 46 |
| 95 | 92 |  | 87 | 83 | 79 | 75 | | | 69 | 65 | 61 | 57 |  | 52 | 49 |
| 91 |  | 88 | 84 | **81** | 78 | 74 | | | 70 | 66 | **63** | 60 | 56 |  | 53 |
| **90** | 89 | 85 | 82 | 80 | 77 | 73 | \_**72** | \_71 | \_67 | \_64 | \_62 | \_59 | \_55 | \_**54** |

Opposed to the compass-rose above, all inner squares are filled with Begrees as well.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **126** | 127 | 131 | 134 | 136 | 139 | 143 | **0** | 1 | 5 | 8 | 10 | 13 | 17 | **18** |
| 125 | **126** | 128 | 132 | **135** | 138 | 142 | **0** | 2 | 6 | **9** | 12 | 16 | **18** | 19 |
| 121 | 124 | **126** | 129 | 133 | 137 | 141 | **0** | 3 | 7 | 11 | 15 | **18** | 20 | 23 |
| 118 | 120 | 123 | **126** | 130 | **135** | 140 | **0** | 4 | **9** | 14 | **18** | 21 | 24 | 26 |
| 116 | **117** | 119 | 122 | **126** | 132 | 138 | **0** | 6 | 12 | **18** | 22 | 25 | **27** | 28 |
| 113 | 114 | 115 | **117** | 120 | **126** | **135** | **0** | **9** | **18** | 24 | **27** | 29 | 30 | 31 |
| 109 | 110 | 111 | 112 | 114 | **117** | **126** | **0** | **18** | **27** | 30 | 32 | 33 | 34 | 35 |
| **108** | **108** | **108** | **108** | **108** | **108** | **108** | + | **36** | **36** | **36** | **36** | **36** | **36** | **36** |
| 107 | 106 | 105 | 104 | 102 | **99** | **90** | **72** | **54** | **45** | 42 | 40 | 39 | 38 | 37 |
| 103 | 102 | 101 | **99** | 96 | **90** | **81** | **72** | **63** | **54** | 48 | **45** | 43 | 42 | 41 |
| 100 | **99** | 97 | 94 | **90** | 84 | 78 | **72** | 66 | 60 | **54** | 50 | 47 | **45** | 44 |
| 98 | 96 | 93 | **90** | 86 | **81** | 76 | **72** | 68 | **63** | 58 | **54** | 51 | 48 | 46 |
| 95 | 92 | **90** | 87 | 83 | 79 | 75 | **72** | 69 | 65 | 61 | 57 | **54** | 52 | 49 |
| 91 | **90** | 88 | 84 | **81** | 78 | 74 | **72** | 70 | 66 | **63** | 60 | 56 | **54** | 53 |
| **90** | 89 | 85 | 82 | 80 | 77 | 73 | \_**72** | \_71 | \_67 | \_64 | \_62 | \_59 | \_55 | \_**54** |

# Lookup

Since the computation is quite expensive, a two dimensional table with pre-calculated values might be used for that purpose. The enumerated type enumDir might contain only ray- or move directions, Degrees, Begrees, or a structure combining them.

```
enumDir arrDirection[64][64]; // 4 KByte

enumDir direction(enumSquare sq1, enumSquare sq2) {
   return arrDirection[sq1][sq2];
}
```

# Lookup by 0x88 Difference

The [0x88](/0x88 "0x88") [square relation](/0x88#SquareRelations "0x88") permits a denser lookup approach. The difference of valid 0x88 coordinates of two squares is unique with respect to [distance](/Distance "Distance") and direction. That way, one can greatly reduce the size of the lookup [array](/Array "Array") to only 240 instead of 4096 elements. Some additional computation required, if one has to convert usual square coordinates to 0x88. If one already relies on 0x88 coordinates, it becomes even cheaper:

```
enumDir arrDirectionBy0x88Diff[240];

unsigned int x88diff(enumSquare sq1, enumSquare sq2) {
   return sq2 - sq1 + (sq2|7) - (sq1|7) + 120;
}

enumDir direction(enumSquare sq1, enumSquare sq2) {
   return arrDirectionBy0x88Diff[x88diff(sq1, sq2)];
}
```

# See also

- [0x88 Square Relations](/0x88#SquareRelations "0x88")
- [Attacks on the otherwise empty Board](/On_an_empty_Board "On an empty Board")
- [Butterfly Boards](/Butterfly_Boards "Butterfly Boards")
- [Distance](/Distance "Distance")
- [Flipping Mirroring and Rotating](/Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
- [Intersection Squares](/Intersection_Squares "Intersection Squares")
- [Knight-Distance](/Knight-Distance "Knight-Distance")
- [Manhattan-Distance](/Manhattan-Distance "Manhattan-Distance")
- [Pieces versus Directions](/Pieces_versus_Directions "Pieces versus Directions")
- [Vector Attacks](/Vector_Attacks "Vector Attacks")
- [Two Squares on a File](/Files#TwoSquares "Files")
- [Two Squares on a Rank](/Ranks#TwoSquares "Ranks")
- [Two Squares on a Diagonal](/Diagonals#TwoSquares "Diagonals")
- [Two Squares on a Anti-Diagonal](/Anti-Diagonals#TwoSquares "Anti-Diagonals")

# Forum Posts

- [Extract direction (ray) informations from two squares](http://www.talkchess.com/forum/viewtopic.php?t=48322) by [Mathieu Pagé](/Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](/CCC "CCC"), June 18, 2013 » [Rays](/Rays "Rays"), [Square Attacked By](/Square_Attacked_By "Square Attacked By")
- [An undetected bug for 10 years](http://talkchess.com/forum3/viewtopic.php?f=7&t=74821) by [Oliver Brausch](/Oliver_Brausch "Oliver Brausch"), [CCC](/CCC "CCC"), August 18, 2020 » [Two Squares on a Diagonal](/Diagonals#TwoSquares "Diagonals")

# External Links

- [Direction from Wikipedia](https://en.wikipedia.org/wiki/Direction_%28geometry%29)
- [Relative direction from Wikipedia](https://en.wikipedia.org/wiki/Relative_direction)
- [Windward and leeward from Wikipedia](https://en.wikipedia.org/wiki/Windward_and_leeward)
- [Starboard from Wikipedia](https://en.wikipedia.org/wiki/Starboard)
- [Port (nautical) from Wikipedia](https://en.wikipedia.org/wiki/Port_%28nautical%29)
- [Origins of the Compass Rose](http://www.gisnet.com/notebook/comprose.php) by [Bill Thoen](http://www.gisnet.com/gisnet/thoen/Thoen_CV.htm)
- [Boxing the compass from Wikipedia](https://en.wikipedia.org/wiki/Boxing_the_compass)
- [Weather Report](/Category:Weather_Report "Category:Weather Report") - [Directions](http://rutracker.org/forum/viewtopic.php?t=4514776), [73rd NDR-Jazzworkshop](https://web.archive.org/web/20060303055049/http://www.uni-duisburg.de/AVMZ/frohne/discos/hamburg.htm), [IFA](https://en.wikipedia.org/wiki/Internationale_Funkausstellung_Berlin) [Berlin](https://en.wikipedia.org/wiki/West_Berlin), September 03, 1971, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   [Joe Zawinul](/Category:Joe_Zawinul "Category:Joe Zawinul"), [Wayne Shorter](/Category:Wayne_Shorter "Category:Wayne Shorter"), [Miroslav Vitouš](/Category:Miroslav_Vitou%C5%A1 "Category:Miroslav Vitouš"), [Alphonse Mouzon](/Category:Alphonse_Mouzon "Category:Alphonse Mouzon"), [Dom Um Romão](/Category:Dom_Um_Rom%C3%A3o "Category:Dom Um Romão"), & guests [John Surman](https://en.wikipedia.org/wiki/John_Surman), [Eje Thelin](https://en.wikipedia.org/wiki/Eje_Thelin), [Alan Skidmore](/Category:Alan_Skidmore "Category:Alan Skidmore")

# References

1. [↑](#cite_ref-1) Replica of a wind rose from a chart of Jorge de Aguiar, 1492, [Compass rose - Wikimedia Commons](https://commons.wikimedia.org/wiki/Compass_rose)

**[Up one Level](/Squares "Squares")**