# Pawn Islands (Bitboards)

Source: https://www.chessprogramming.org/Pawn_Islands_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Pawn Islands**

[![](/images/9/98/Drowned.jpg)](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bbd)

[Samuel Bak](/Category:Samuel_Bak "Category:Samuel Bak") - Drowned [[1]](#cite_note-1)

**Pawn Islands** of either side are groups of pawns (at least one), separated by files without own pawns. Those files are therefore either [halfopen](/Pawns_and_Files_(Bitboards)#HalfopenFiles "Pawns and Files (Bitboards)") or [open](/Pawns_and_Files_(Bitboards)#OpenFiles "Pawns and Files (Bitboards)"). All other things being equal, the side with fewer pawn islands has an advantage, because the individual pawns are easier to defend against enemy attacks. Each island has a west- or east border file. Rook-files may be the most outer borders.

# Sample Filesets

Black has three islands here, white two:

```
 . . . . . . . .
 b . . . . . . b
 . b . b b . b .
 . . . . . . . .
 . . . . . . . .
 . w . . . w . .
 w . w . . . w w
 . . . . . . . .
```

Those are the black and white [filesets](/Pawns_and_Files_(Bitboards)#Fileset "Pawns and Files (Bitboards)"), one byte each.

```
 b b . b b . b b

 w w w . . w w w
```

# Island Borders

Based on [filesets](/Pawns_and_Files_(Bitboards)#Fileset "Pawns and Files (Bitboards)"), we can simply determine the west- or east border-files of each island. By shifting left or right one, xor with the original fileset to get all the 0-1 or 1-0 transitions - to finally intersect it with the original fileset to restrict the transitions inside this set of occupied files. The result are the files with [half-isolanis](/Isolated_Pawns_(Bitboards)#IsolanisSetWise "Isolated Pawns (Bitboards)").

Since [conjunction](/General_Setwise_Operations#Intersection "General Setwise Operations") is distributive over [xor](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations"), one may alternately swap both operands. In fact it is the [relative complement](/General_Setwise_Operations#XorWithout "General Setwise Operations") of the shifted files in files and takes three operations each.

## East

```
 b b . b b . b b
 . b . . b . . b

 w w w . . w w w
 . . w . . . . w
```

```
BYTE islandsEastFiles(BYTE f) {return f & (f ^ (f >> 1));}
BYTE islandsEastFiles(BYTE f) {return f ^ (f & (f >> 1));}
BYTE islandsEastFiles(BYTE f) {return f &     ~(f >> 1) ;}
```

```
1 . . . 1 1 . .  files
. . . 1 1 . . .  files >> 1 (board left or west)
1 . . 1 . 1 . .  xor       -> all the west 0-1 or 1-0 file-transitions
1 . . . . 1 . .  and files -> east files of each island
```

## West

```
 b b . b b . b b
 b . . b . . b .

 w w w . . w w w
 w . . . . w . .
```

```
BYTE islandsWestFiles(BYTE f) {return f & (f ^ (f << 1));} // ... (f+f)
BYTE islandsWestFiles(BYTE f) {return f ^ (f & (f << 1));}
BYTE islandsWestFiles(BYTE f) {return f &     ~(f << 1) ;}
```

```
1 . . . 1 1 . .  files
. 1 . . . 1 1 .  files << 1  (board right or east)
1 1 . . 1 . 1 .  xor       -> all the east 0-1 or 1-0 file-transitions
1 . . . 1 . . .  and files -> west files of each island
```

# Number of Islands

Since each island has exactly one west- and one east border-file, the [population count](/Population_Count "Population Count") of either border-set might be used to determine the numbers of islands, see [dispersion](/Dispersion_and_Distortion "Dispersion and Distortion"). Of course all byte-wise calculations may be implemented by small, preinitialized lookup tables, indexed by fileset (0..255), containing the number of islands, bitboards of isolated files and whatever else. The maximum number of islands is four.

# Isolated Files

The intersection of east- and west border-files are already files with [isolated pawns](/Isolated_Pawns_(Bitboards)#IsolanisSetWise "Isolated Pawns (Bitboards)").

```
1 . . . . 1 . .  east files of each island
1 . . . 1 . . .  west files of each island
1 . . . . . . .  and -> isolated files
. . . . 1 1 . .  xor -> resets isolated files
```

To isolate wider (2..8) islands is not that hard either.

# External Links

- [Glossary of chess from Wikipedia - P](https://en.wikipedia.org/wiki/Glossary_of_chess#P)
- [Steps Ahead](/Category:Steps_Ahead "Category:Steps Ahead") - [Islands](https://en.wikipedia.org/wiki/Steps_Ahead_(album)), 1983, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   lineup:. [Mike Mainieri](/Category:Mike_Mainieri "Category:Mike Mainieri"), [Michael Brecker](/Category:Michael_Brecker "Category:Michael Brecker"), [Eddie Gómez](https://en.wikipedia.org/wiki/Eddie_G%C3%B3mez), [Peter Erskine](/Category:Peter_Erskine "Category:Peter Erskine"), [Elaine Elias](https://en.wikipedia.org/wiki/Eliane_Elias)

# References

1. [↑](#cite_ref-1) [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bbd), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](/University_of_Minnesota "University of Minnesota")

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**