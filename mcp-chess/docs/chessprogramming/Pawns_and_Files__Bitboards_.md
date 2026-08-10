# Pawns and Files (Bitboards)

Source: https://www.chessprogramming.org/Pawns_and_Files_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Pawns and Files**

Based on [pawns](/Pawn "Pawn"), [files](/Files "Files") are either **closed**, [open](/Open_File "Open File") or [half-open](/Half-open_File "Half-open File"). [Rooks](/Rook "Rook") prefer open files for [Mobility](/Mobility "Mobility"), to eventually enter the opponent side of the board. Rooks further prefer own half-open files to attack opponent pawns if they are weak, such as [backward](/Backward_Pawn "Backward Pawn") or [isolated](/Isolated_Pawn "Isolated Pawn").

# Closed Files

Closed files have at least one white and one black pawn as member. They are the intersection of both white and black [filefills](/Pawn_Fills#FileFill "Pawn Fills"). See [semi-closed files](/Open_Pawns_(Bitboards)#SemiClosedFiles "Open Pawns (Bitboards)").

```
U64 closedFiles(U64 wpanws, U64 bpawns) {
   return fileFill(wpanws) & fileFill(bpawns);
}
```

```
white pawns         black pawns
. . . . . . . .     . . . . . . . .
. . . . . . . .     . 1 . . . 1 1 .
. . . . . . . .     1 . 1 . . . . 1
. . . . . . . .     . . . 1 . . . .
1 . . . . 1 . .     . . . . . . . .
. . 1 . . . . .     . . . . . . . .
. 1 1 . . . 1 1     . . . . . . . .
. . . . . . . .     . . . . . . . .
white file fill  &  black file fill  =  closed files
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1     1 1 1 . . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1     1 1 1 . . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1     1 1 1 . . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1     1 1 1 . . 1 1 1
1 1 1 . . 1 1 1  &  1 1 1 1 . 1 1 1  =  1 1 1 . . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1     1 1 1 . . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1     1 1 1 . . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1     1 1 1 . . 1 1 1
```

The complement set of closed files are either the open or halfopen files.

# Open Files

[Open files](/Open_File "Open File") don't have any white or black pawn as member, thus it is the intersection of the [filefills](/Pawn_Fills#FileFill "Pawn Fills") complements:

```
U64 openFiles(U64 wpanws, U64 bpawns) {
   return ~fileFill(wpanws) & ~fileFill(bpawns);
}
```

```
white pawns         black pawns
. . . . . . . .     . . . . . . . .
. . . . . . . .     . 1 . . . 1 1 .
. . . . . . . .     1 . 1 . . . . 1
. . . . . . . .     . . . 1 . . . .
1 . . . . 1 . .     . . . . . . . .
. . 1 . . . . .     . . . . . . . .
. 1 1 . . . 1 1     . . . . . . . .
. . . . . . . .     . . . . . . . .
~white file fill  & ~black file fill =  open files
. . . 1 1 . . .     . . . . 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . . 1 . . .
. . . 1 1 . . .  &  . . . . 1 . . .  =  . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . . 1 . . .
```

Alternative applying [De Morgan](/General_Setwise_Operations#DeMorganslaws "General Setwise Operations") , the complement of the unions:

```
U64 openFiles(U64 wpanws, U64 bpawns) {
   return ~(fileFill(wpanws) | fileFill(bpawns));
}
```

Or we may fill the union of both pawns, but it may be smarter to rely on common subexpression to allow inter-function optimizations of inlined functions:

```
U64 openFiles(U64 wpanws, U64 bpawns) {
   return ~fileFill(wpanws | bpawns);
}
```

# Half-open Files

The complements of white or black [filefills](/Pawn_Fills#FileFill "Pawn Fills") are either [half-open](/Half-open_File "Half-open File") (for either color) or [open](/Open_File "Open File").

```
U64 halfOpenOrOpenFile(U64 gen) {return ~fileFill(gen);}
```

```
white pawns         black pawns
. . . . . . . .     . . . . . . . .
. . . . . . . .     . 1 . . . 1 1 .
. . . . . . . .     1 . 1 . . . . 1
. . . . . . . .     . . . 1 . . . .
1 . . . . 1 . .     . . . . . . . .
. . 1 . . . . .     . . . . . . . .
. 1 1 . . . 1 1     . . . . . . . .
. . . . . . . .     . . . . . . . .
white file fill     black file fill
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
white halfopen      black halfopen
or open files       or open files
. . . 1 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .
. . . 1 1 . . .     . . . . 1 . . .
```

Excluding open files by relative complement (xor), leaves the half-open files with at least one opponent pawn, but no own pawn.

```
U64 wHalfOpenFile(U64 wpawns, U64 bpanws) {
   return halfOpenOrOpenFile(wpawns)
        ^ openFiles(wpanws, bpawns);
}
```

```
white halfopen                          white halfopen
or open files    ^  open files       =  files
. . . 1 1 . . .     . . . . 1 . . .     . . . 1 . . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . 1 . . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . 1 . . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . 1 . . . .
. . . 1 1 . . .  ^  . . . . 1 . . .  =  . . . 1 . . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . 1 . . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . 1 . . . .
. . . 1 1 . . .     . . . . 1 . . .     . . . 1 . . . .
```

# Semi-closed Files

So far we considered following D-file closed, since both sides have one pawn on it. In fact due to captures the pawns are [open](/Open_Pawns_(Bitboards) "Open Pawns (Bitboards)"), they are not member of any opponent frontspan. Thus, the file is more like eventually mutual half-open file. We need to [filefill](/Pawn_Fills#FileFill "Pawn Fills") [open pawns](/Open_Pawns_(Bitboards) "Open Pawns (Bitboards)") on closed files, to consider this subset.

```
white pawns         black pawns
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . 1 . . . .     . . . . . . . .
. . . . . . . .     . . . 1 . . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
```

# Filesets

As mentioned, the boolean information whether a file is occupied by a pawn or not, may be stored in one [byte](/Byte "Byte") only - a fileset. South fill and casting to BYTE aka unsigned char is sufficient:

```
BYTE fileSet(U64 gen) {return (BYTE) soutFill(gen);}
```

Of course we can simply restore a filefill by zero-extending the fileset to a bitboard plus applying a [north-fill multiplication](/General_Setwise_Operations#Multiplication "General Setwise Operations") with the A-file.

```
U64 filefill(BYTE fset) {
  U64 ff = fset;
  return ff * C64(0x0101010101010101);
}
```

All the mentioned file-type sets may be handled this way. The advantage with one rank as set only - beside 1/8 space in pawnhash-table - there are no wraps to consider.

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**